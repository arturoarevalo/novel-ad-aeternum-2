// Generador de .docx (interior de imprenta 6"x9") SIN dependencias externas.
// Emite OOXML a mano y empaqueta el ZIP con node:zlib. Los estilos replican la
// plantilla builds/Template-6x9.docx (tema "Endure" de KDP): mismas fuentes,
// cuerpos, interlineados exactos y geometría de página.
//
// Autocontenido a propósito: para reutilizarlo en otra novela basta copiar este
// fichero y scripts/src/build-docx.ts.

import { deflateRawSync } from "node:zlib";

// ---------------------------------------------------------------------------
// Modelo de entrada
// ---------------------------------------------------------------------------

export interface ParteDocx {
    n: number;
    titulo: string;
    capitulo_inicial: number;
    capitulo_final?: number;
}

export interface CapituloDocx {
    n: number;
    titulo: string;
    /** Cuerpo markdown del capítulo (sin front-matter). */
    cuerpo: string;
}

export interface OpcionesDocx {
    titulo: string;
    subtitulo?: string;
    autor: string;
    /** Año de la página de copyright (por defecto, el actual). */
    anio?: number;
    /** Texto de la dedicatoria; si falta, no se genera la página. */
    dedicatoria?: string;
    /** Índice (CONTENIDO) con campo TOC actualizable en Word. */
    incluirIndice?: boolean;
    partes: ParteDocx[];
    capitulos: CapituloDocx[];
}

export interface EstadisticasDocx {
    capitulos: number;
    partes: number;
    insets: number;
    tablas: number;
    separadores: number;
}

// ---------------------------------------------------------------------------
// Geometría y constantes visuales (medidas en twips, tomadas de la plantilla)
// ---------------------------------------------------------------------------

const PAGINA = { w: 8640, h: 12960 }; // 6" x 9"
const MARGEN_FRONT = { top: 864, right: 864, bottom: 864, left: 1094, header: 504, footer: 504 };
const MARGEN_CUERPO = { top: 794, right: 851, bottom: 794, left: 1077, header: 454, footer: 454 };
const ANCHO_TEXTO_CUERPO = PAGINA.w - MARGEN_CUERPO.left - MARGEN_CUERPO.right; // 6712
const ANCHO_TEXTO_FRONT = PAGINA.w - MARGEN_FRONT.left - MARGEN_FRONT.right; // 6682

const COLOR_CAJA = "EFEFEF"; // fondo de los insets (gris muy tenue)
const COLOR_CAJA_CABECERA = "E2E2E2"; // fila de cabecera de tablas dentro de insets
const COLOR_BORDE_TABLA = "BFBFBF";
const PADDING_CAJA = { v: 130, h: 170 }; // padding interior de la caja (twips)

// ---------------------------------------------------------------------------
// ZIP mínimo (deflate + CRC32), suficiente para un paquete OPC
// ---------------------------------------------------------------------------

function crc32(buf: Buffer): number {
    let c = ~0;
    for (let i = 0; i < buf.length; i++) {
        c ^= buf[i]!;
        for (let k = 0; k < 8; k++) c = (c >>> 1) ^ (0xedb88320 & -(c & 1));
    }
    return ~c >>> 0;
}

// Fecha DOS fija (2026-01-01) para que el binario sea reproducible.
const FECHA_DOS = ((((2026 - 1980) << 9) | (1 << 5) | 1) << 16) >>> 0;

function zipear(entradas: { nombre: string; datos: string | Buffer }[]): Buffer {
    const locales: Buffer[] = [];
    const centrales: Buffer[] = [];
    let offset = 0;
    for (const e of entradas) {
        const datos = Buffer.isBuffer(e.datos) ? e.datos : Buffer.from(e.datos, "utf8");
        const nombre = Buffer.from(e.nombre, "utf8");
        const comprimido = deflateRawSync(datos, { level: 9 });
        const crc = crc32(datos);

        const lfh = Buffer.alloc(30);
        lfh.writeUInt32LE(0x04034b50, 0);
        lfh.writeUInt16LE(20, 4); // versión necesaria
        lfh.writeUInt16LE(0x0800, 6); // nombres en UTF-8
        lfh.writeUInt16LE(8, 8); // método: deflate
        lfh.writeUInt32LE(FECHA_DOS, 10);
        lfh.writeUInt32LE(crc, 14);
        lfh.writeUInt32LE(comprimido.length, 18);
        lfh.writeUInt32LE(datos.length, 22);
        lfh.writeUInt16LE(nombre.length, 26);
        lfh.writeUInt16LE(0, 28);
        locales.push(lfh, nombre, comprimido);

        const cen = Buffer.alloc(46);
        cen.writeUInt32LE(0x02014b50, 0);
        cen.writeUInt16LE(20, 4); // creado por
        cen.writeUInt16LE(20, 6); // versión necesaria
        cen.writeUInt16LE(0x0800, 8);
        cen.writeUInt16LE(8, 10);
        cen.writeUInt32LE(FECHA_DOS, 12);
        cen.writeUInt32LE(crc, 16);
        cen.writeUInt32LE(comprimido.length, 20);
        cen.writeUInt32LE(datos.length, 24);
        cen.writeUInt16LE(nombre.length, 28);
        cen.writeUInt32LE(offset, 42);
        centrales.push(cen, nombre);

        offset += 30 + nombre.length + comprimido.length;
    }
    const directorio = Buffer.concat(centrales);
    const eocd = Buffer.alloc(22);
    eocd.writeUInt32LE(0x06054b50, 0);
    eocd.writeUInt16LE(entradas.length, 8);
    eocd.writeUInt16LE(entradas.length, 10);
    eocd.writeUInt32LE(directorio.length, 12);
    eocd.writeUInt32LE(offset, 16);
    return Buffer.concat([...locales, directorio, eocd]);
}

// ---------------------------------------------------------------------------
// Markdown de capítulo → modelo de bloques
// ---------------------------------------------------------------------------

interface Run {
    texto: string;
    cursiva: boolean;
    negrita: boolean;
}

type ItemInset = { tipo: "p"; runs: Run[] } | { tipo: "tabla"; filas: Run[][][] };

type Bloque =
    | { tipo: "parrafo"; runs: Run[]; primero: boolean }
    | { tipo: "separador" }
    | { tipo: "inset"; items: ItemInset[] };

/**
 * Énfasis en línea: *cursiva*, **negrita**, ***ambas***.
 * Con cursivaBase=true (dentro de un inset) la marca de cursiva se invierte:
 * lo marcado en cursiva dentro de un bloque ya cursivo se compone en redonda.
 */
function parseInline(texto: string, cursivaBase = false): Run[] {
    const runs: Run[] = [];
    let cursiva = false;
    let negrita = false;
    let buf = "";
    const cerrar = () => {
        if (!buf) return;
        runs.push({ texto: buf, cursiva: cursivaBase ? !cursiva : cursiva, negrita });
        buf = "";
    };
    // El código en línea (`…`) va primero: dentro no se interpretan asteriscos.
    // Son nombres de fichero y texto de máquina: en una novela se componen en
    // cursiva del cuerpo, como cualquier texto citado (redonda dentro de insets).
    const segmentos = texto.split(/`([^`]*)`/);
    segmentos.forEach((segmento, idx) => {
        if (idx % 2 === 1) {
            cerrar();
            if (segmento) runs.push({ texto: segmento, cursiva: !cursivaBase, negrita: false });
            return;
        }
        for (const trozo of segmento.split(/(\*{1,3})/)) {
            if (trozo === "***") { cerrar(); cursiva = !cursiva; negrita = !negrita; }
            else if (trozo === "**") { cerrar(); negrita = !negrita; }
            else if (trozo === "*") { cerrar(); cursiva = !cursiva; }
            else buf += trozo;
        }
        cerrar();
    });
    return runs;
}

function parseTabla(lineas: string[]): ItemInset {
    const filas: Run[][][] = [];
    for (const linea of lineas) {
        const celdas = linea.replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim());
        if (celdas.every((c) => /^:?-+:?$/.test(c))) continue; // fila separadora de markdown
        filas.push(celdas.map((c) => parseInline(c, false)));
    }
    const columnas = Math.max(...filas.map((f) => f.length), 1);
    for (const f of filas) while (f.length < columnas) f.push([]);
    return { tipo: "tabla", filas };
}

function parseInset(lineas: string[]): ItemInset[] {
    const items: ItemInset[] = [];
    let i = 0;
    while (i < lineas.length) {
        const t = lineas[i]!.trim();
        if (!t) { i++; continue; }
        if (t.startsWith("|")) {
            const tabla: string[] = [];
            while (i < lineas.length && lineas[i]!.trim().startsWith("|")) { tabla.push(lineas[i]!.trim()); i++; }
            items.push(parseTabla(tabla));
            continue;
        }
        items.push({ tipo: "p", runs: parseInline(t, true) });
        i++;
    }
    return items;
}

/** Cuerpo markdown → bloques. Cada línea no vacía es un párrafo (convención del repo). */
function parseCuerpo(cuerpo: string): Bloque[] {
    const limpio = cuerpo
        .replace(/<!--[\s\S]*?-->/g, "") // comentarios (marcadores de intercalados, notas…)
        .replace(/^\s*#\s+[^\n]*\n/, ""); // posible H1 inicial redundante con el título
    const lineas = limpio.split(/\r?\n/);
    const bloques: Bloque[] = [];
    let i = 0;
    while (i < lineas.length) {
        const t = lineas[i]!.trim();
        if (!t) { i++; continue; }
        if (/^\*(\s*\*)+$/.test(t)) {
            // colapsa separadores consecutivos (restos de intercalados comentados)
            if (bloques[bloques.length - 1]?.tipo !== "separador") bloques.push({ tipo: "separador" });
            i++;
            continue;
        }
        if (t.startsWith(">")) {
            const internas: string[] = [];
            while (i < lineas.length && lineas[i]!.trim().startsWith(">")) {
                internas.push(lineas[i]!.trim().replace(/^>\s?/, ""));
                i++;
            }
            bloques.push({ tipo: "inset", items: parseInset(internas) });
            continue;
        }
        bloques.push({ tipo: "parrafo", runs: parseInline(t), primero: false });
        i++;
    }
    // Separadores huérfanos al abrir o cerrar el capítulo sobran.
    while (bloques[0]?.tipo === "separador") bloques.shift();
    while (bloques[bloques.length - 1]?.tipo === "separador") bloques.pop();
    // El primer párrafo del capítulo y el primero tras separador o inset van sin sangría.
    let primero = true;
    for (const b of bloques) {
        if (b.tipo === "parrafo") { b.primero = primero; primero = false; }
        else primero = true;
    }
    return bloques;
}

// ---------------------------------------------------------------------------
// Emisión OOXML
// ---------------------------------------------------------------------------

const XML_DECL = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n`;
const NS_W = `xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"`;
const NS_W14 = `xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"`;
const NS_MC = `xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"`;
const NS_R = `xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"`;
const ATRS_RAIZ = `${NS_W} ${NS_W14} ${NS_R} ${NS_MC} mc:Ignorable="w14"`;

function esc(s: string): string {
    return s
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}

/**
 * baseCursiva indica que el ESTILO del párrafo ya es cursivo (insets): ahí la
 * redonda hay que pedirla explícitamente con i w:val="0", porque omitir la
 * propiedad hereda la cursiva del estilo.
 */
function xmlRun(r: Run, baseCursiva = false, extraRPr = ""): string {
    let props = "";
    if (r.negrita) props += "<w:b/>";
    if (baseCursiva) {
        if (!r.cursiva) props += `<w:i w:val="0"/><w:iCs w:val="0"/>`;
    } else if (r.cursiva) {
        props += "<w:i/>";
    }
    props += extraRPr;
    const rpr = props ? `<w:rPr>${props}</w:rPr>` : "";
    return `<w:r>${rpr}<w:t xml:space="preserve">${esc(r.texto)}</w:t></w:r>`;
}

function xmlTexto(texto: string): string {
    return xmlRun({ texto, cursiva: false, negrita: false });
}

/** pPrExtra debe venir en orden de esquema (keepNext < spacing < jc < sectPr). */
function xmlP(estilo: string | null, contenido: string, pPrExtra = ""): string {
    const pPr =
        estilo || pPrExtra
            ? `<w:pPr>${estilo ? `<w:pStyle w:val="${estilo}"/>` : ""}${pPrExtra}</w:pPr>`
            : "";
    return `<w:p>${pPr}${contenido}</w:p>`;
}

const P_VACIO = "<w:p/>";

/** Entrada TC oculta para el índice (colección C). */
function campoTC(texto: string, nivel: number): string {
    const instr = ` TC "${texto.replace(/"/g, "'")}" \\f C \\l ${nivel} `;
    const v = `<w:rPr><w:vanish/></w:rPr>`;
    return (
        `<w:r>${v}<w:fldChar w:fldCharType="begin"/></w:r>` +
        `<w:r>${v}<w:instrText xml:space="preserve">${esc(instr)}</w:instrText></w:r>` +
        `<w:r>${v}<w:fldChar w:fldCharType="end"/></w:r>`
    );
}

// Identificadores de relación de document.xml.rels
const RID = {
    estilos: "rId1",
    ajustes: "rId2",
    fuentes: "rId3",
    hdrVacio: "rId4",
    hdrAutor: "rId5", // páginas pares (verso)
    hdrTitulo: "rId6", // páginas impares (recto)
    ftrVacio: "rId7",
    ftrNumero: "rId8",
};

interface OpcionesSeccion {
    tipo?: "nextPage" | "oddPage";
    front?: boolean; // márgenes de front matter y numeración romana, sin cabeceras
    vAlign?: "center" | "bottom";
    inicioPagina?: number;
    folioPrimera?: boolean; // número de página visible en la primera página de la sección
}

function xmlSectPr(o: OpcionesSeccion): string {
    const m = o.front ? MARGEN_FRONT : MARGEN_CUERPO;
    const ref = (tag: string, tipo: string, id: string) =>
        `<w:${tag} w:type="${tipo}" r:id="${id}"/>`;
    const refs = o.front
        ? ref("headerReference", "even", RID.hdrVacio) +
        ref("headerReference", "default", RID.hdrVacio) +
        ref("headerReference", "first", RID.hdrVacio) +
        ref("footerReference", "even", RID.ftrVacio) +
        ref("footerReference", "default", RID.ftrVacio) +
        ref("footerReference", "first", RID.ftrVacio)
        : ref("headerReference", "even", RID.hdrAutor) +
        ref("headerReference", "default", RID.hdrTitulo) +
        ref("headerReference", "first", RID.hdrVacio) +
        ref("footerReference", "even", RID.ftrNumero) +
        ref("footerReference", "default", RID.ftrNumero) +
        ref("footerReference", "first", o.folioPrimera ? RID.ftrNumero : RID.ftrVacio);
    const pgNum = o.front
        ? `<w:pgNumType w:fmt="lowerRoman"/>`
        : o.inicioPagina
            ? `<w:pgNumType w:start="${o.inicioPagina}"/>`
            : "";
    return (
        `<w:sectPr>${refs}` +
        (o.tipo ? `<w:type w:val="${o.tipo}"/>` : "") +
        `<w:pgSz w:w="${PAGINA.w}" w:h="${PAGINA.h}"/>` +
        `<w:pgMar w:top="${m.top}" w:right="${m.right}" w:bottom="${m.bottom}" w:left="${m.left}" w:header="${m.header}" w:footer="${m.footer}" w:gutter="0"/>` +
        pgNum +
        `<w:cols w:space="720"/>` +
        (o.vAlign ? `<w:vAlign w:val="${o.vAlign}"/>` : "") +
        `<w:titlePg/>` +
        `<w:docGrid w:linePitch="360"/>` +
        `</w:sectPr>`
    );
}

/** Párrafo casi invisible que separa las cajas del texto (media línea escasa). */
const P_SEPARA_CAJA = `<w:p><w:pPr><w:spacing w:after="0" w:line="110" w:lineRule="exact"/><w:rPr><w:sz w:val="2"/></w:rPr></w:pPr></w:p>`;

function xmlTablaInterior(filas: Run[][][]): string {
    const columnas = filas[0]?.length ?? 1;
    // Columnas cortas (horas, fechas, cifras) rígidas a su ancho natural para que
    // no envuelvan nunca; las de texto largo se reparten el resto y son las que
    // parten línea. ~110 twips por carácter a 8 pt (holgado para fuentes anchas).
    const disponible = ANCHO_TEXTO_CUERPO - 2 * PADDING_CAJA.h;
    const largos: number[] = [];
    for (let c = 0; c < columnas; c++) {
        largos.push(Math.max(...filas.map((f) => f[c]!.map((r) => r.texto).join("").length), 2));
    }
    const natural = (len: number) => (len + 2) * 110;
    const rigidas = largos.map((len) => len <= 14);
    const anchoRigido = largos.reduce((a, len, c) => a + (rigidas[c] ? natural(len) : 0), 0);
    const flexibleNatural = largos.reduce((a, len, c) => a + (rigidas[c] ? 0 : natural(len)), 0);
    let anchos: number[];
    if (!flexibleNatural || anchoRigido + columnas * 300 > disponible) {
        // sin columnas flexibles (o mesa imposible): reparto proporcional simple
        const total = largos.reduce((a, len) => a + natural(len), 0);
        anchos = largos.map((len) => Math.floor((natural(len) * disponible) / total));
    } else {
        const paraFlexibles = disponible - anchoRigido;
        anchos = largos.map((len, c) =>
            rigidas[c] ? natural(len) : Math.max(1000, Math.floor((natural(len) * paraFlexibles) / flexibleNatural))
        );
    }

    const borde = (lado: string) =>
        `<w:${lado} w:val="single" w:sz="4" w:space="0" w:color="${COLOR_BORDE_TABLA}"/>`;
    const bordes = ["top", "left", "bottom", "right", "insideH", "insideV"].map(borde).join("");

    const filasXml = filas
        .map((celdas, i) => {
            const cabecera = i === 0;
            const tds = celdas
                .map((runs, cIdx) => {
                    const shd = cabecera
                        ? `<w:shd w:val="clear" w:color="auto" w:fill="${COLOR_CAJA_CABECERA}"/>`
                        : "";
                    const contenido = runs.map((r) => xmlRun(cabecera ? { ...r, negrita: true } : r)).join("");
                    return (
                        `<w:tc><w:tcPr><w:tcW w:w="${anchos[cIdx]!}" w:type="dxa"/>${shd}</w:tcPr>` +
                        xmlP("EndureInsetTabla", contenido) +
                        `</w:tc>`
                    );
                })
                .join("");
            return `<w:tr>${cabecera ? "<w:trPr><w:tblHeader/></w:trPr>" : ""}${tds}</w:tr>`;
        })
        .join("");

    return (
        `<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/>` +
        `<w:tblBorders>${bordes}</w:tblBorders>` +
        `<w:tblLayout w:type="fixed"/>` +
        `<w:tblCellMar><w:top w:w="30" w:type="dxa"/><w:left w:w="80" w:type="dxa"/><w:bottom w:w="30" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar>` +
        `</w:tblPr><w:tblGrid>${anchos.map((a) => `<w:gridCol w:w="${a}"/>`).join("")}</w:tblGrid>` +
        filasXml +
        `</w:tbl>`
    );
}

/** Caja de inset: tabla 1x1 con fondo tenue, padding y texto en cursiva. */
function xmlCaja(items: ItemInset[]): string {
    const contenido: string[] = [];
    for (const item of items) {
        if (item.tipo === "p") contenido.push(xmlP("EndureInset", item.runs.map((r) => xmlRun(r, true)).join("")));
        else contenido.push(xmlTablaInterior(item.filas));
    }
    // Una celda debe terminar siempre en párrafo.
    if (!items.length || items[items.length - 1]!.tipo === "tabla") {
        contenido.push(`<w:p><w:pPr><w:spacing w:after="0" w:line="40" w:lineRule="exact"/><w:rPr><w:sz w:val="2"/></w:rPr></w:pPr></w:p>`);
    }
    return (
        `<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/>` +
        `<w:tblCellMar><w:top w:w="${PADDING_CAJA.v}" w:type="dxa"/><w:left w:w="${PADDING_CAJA.h}" w:type="dxa"/><w:bottom w:w="${PADDING_CAJA.v}" w:type="dxa"/><w:right w:w="${PADDING_CAJA.h}" w:type="dxa"/></w:tblCellMar>` +
        `</w:tblPr><w:tblGrid><w:gridCol w:w="${ANCHO_TEXTO_CUERPO}"/></w:tblGrid>` +
        `<w:tr><w:tc><w:tcPr><w:tcW w:w="5000" w:type="pct"/><w:shd w:val="clear" w:color="auto" w:fill="${COLOR_CAJA}"/></w:tcPr>` +
        contenido.join("") +
        `</w:tc></w:tr></w:tbl>`
    );
}

function romano(n: number): string {
    const pares: [number, string][] = [
        [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"],
        [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"],
    ];
    let resto = n;
    let salida = "";
    for (const [valor, letra] of pares) {
        while (resto >= valor) { salida += letra; resto -= valor; }
    }
    return salida;
}

// ---------------------------------------------------------------------------
// Partes fijas del paquete
// ---------------------------------------------------------------------------

function xmlEstilos(): string {
    const estilo = (
        tipo: string,
        id: string,
        nombre: string,
        cuerpo: string,
        extraCabecera = ""
    ) =>
        `<w:style w:type="${tipo}" w:styleId="${id}"><w:name w:val="${nombre}"/>${extraCabecera}${cuerpo}</w:style>`;

    return (
        XML_DECL +
        `<w:styles ${ATRS_RAIZ}>` +
        `<w:docDefaults><w:rPrDefault><w:rPr>` +
        `<w:rFonts w:ascii="Amazon Endure Book" w:eastAsia="Calibri" w:hAnsi="Amazon Endure Book" w:cs="Times New Roman"/>` +
        `<w:sz w:val="18"/><w:szCs w:val="18"/>` +
        `<w:lang w:val="es-ES" w:eastAsia="en-US" w:bidi="ar-SA"/>` +
        `</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="220" w:lineRule="exact"/></w:pPr></w:pPrDefault></w:docDefaults>` +
        // Base
        `<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/>` +
        `<w:pPr><w:widowControl w:val="0"/><w:spacing w:after="0" w:line="220" w:lineRule="exact"/></w:pPr></w:style>` +
        `<w:style w:type="character" w:default="1" w:styleId="FuentePredeterminada"><w:name w:val="Default Paragraph Font"/><w:uiPriority w:val="1"/><w:semiHidden/><w:unhideWhenUsed/></w:style>` +
        `<w:style w:type="table" w:default="1" w:styleId="TablaNormal"><w:name w:val="Normal Table"/><w:uiPriority w:val="99"/><w:semiHidden/><w:unhideWhenUsed/>` +
        `<w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>` +
        // Portada y front matter (tema Endure)
        estilo("paragraph", "EndureBookTitle", "Endure - Book Title",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:line="240" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>` +
            `<w:rPr><w:rFonts w:ascii="Amazon Endure Light" w:hAnsi="Amazon Endure Light"/><w:sz w:val="72"/><w:szCs w:val="72"/></w:rPr>`) +
        estilo("paragraph", "EndureBookSubtitle", "Endure - Book Subtitle",
            `<w:basedOn w:val="EndureBookTitle"/><w:qFormat/>` +
            `<w:rPr><w:color w:val="595959"/><w:spacing w:val="15"/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr>`) +
        estilo("paragraph", "EndureAuthorName", "Endure - Author Name",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="200" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>` +
            `<w:rPr><w:rFonts w:ascii="Amazon Endure Light" w:hAnsi="Amazon Endure Light"/><w:spacing w:val="10"/><w:sz w:val="27"/><w:szCs w:val="36"/></w:rPr>`) +
        estilo("paragraph", "EndureCopyrightPage", "Endure - Copyright Page",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:line="240" w:lineRule="auto"/></w:pPr>` +
            `<w:rPr><w:spacing w:val="4"/><w:sz w:val="17"/><w:szCs w:val="20"/><w14:numForm w14:val="lining"/></w:rPr>`) +
        estilo("paragraph", "EndureFrontMatterBodyText", "Endure - Front Matter Body Text",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:line="250" w:lineRule="exact"/><w:jc w:val="center"/></w:pPr>`) +
        // Títulos de parte y capítulo
        estilo("paragraph", "EndureChapterTitle", "Endure - Chapter Title",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:line="317" w:lineRule="exact"/><w:jc w:val="center"/></w:pPr>` +
            `<w:rPr><w:caps/><w:spacing w:val="6"/><w:sz w:val="26"/><w:szCs w:val="28"/><w14:numForm w14:val="lining"/></w:rPr>`) +
        // Cuerpo
        estilo("paragraph", "EndureChapterBodyText", "Endure - Chapter Body Text",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:ind w:firstLine="180"/><w:jc w:val="both"/></w:pPr>`) +
        estilo("paragraph", "EndureFirstParagraphBodyText", "Endure - First Paragraph Body Text",
            `<w:basedOn w:val="EndureChapterBodyText"/><w:next w:val="EndureChapterBodyText"/><w:qFormat/><w:pPr><w:ind w:firstLine="0"/></w:pPr>`) +
        estilo("paragraph", "EndureSceneBreak", "Endure - Scene Break",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:before="110" w:after="110"/><w:jc w:val="center"/></w:pPr>` +
            `<w:rPr><w:spacing w:val="20"/></w:rPr>`) +
        // Insets
        estilo("paragraph", "EndureInset", "Endure - Inset",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="110"/><w:jc w:val="both"/></w:pPr>` +
            `<w:rPr><w:i/><w:iCs/></w:rPr>`) +
        estilo("paragraph", "EndureInsetTabla", "Endure - Inset Tabla",
            `<w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>` +
            `<w:rPr><w:sz w:val="16"/><w:szCs w:val="16"/></w:rPr>`) +
        // Cabeceras, pies e índice
        estilo("paragraph", "Encabezado", "header",
            `<w:basedOn w:val="Normal"/><w:pPr><w:jc w:val="center"/></w:pPr><w:rPr><w:spacing w:val="6"/></w:rPr>`,
            "") +
        estilo("paragraph", "Piedepagina", "footer",
            `<w:basedOn w:val="Normal"/><w:pPr><w:jc w:val="center"/></w:pPr>`) +
        estilo("character", "Numerodepagina", "page number",
            `<w:rPr><w:rFonts w:ascii="Amazon Endure Book" w:hAnsi="Amazon Endure Book"/><w:b w:val="0"/><w:i w:val="0"/><w:sz w:val="18"/><w14:numForm w14:val="lining"/></w:rPr>`) +
        estilo("paragraph", "TOC1", "toc 1",
            `<w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="${ANCHO_TEXTO_FRONT}"/></w:tabs><w:spacing w:before="160" w:after="40"/></w:pPr>` +
            `<w:rPr><w:b/><w14:numForm w14:val="lining"/></w:rPr>`) +
        estilo("paragraph", "TOC2", "toc 2",
            `<w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="${ANCHO_TEXTO_FRONT}"/></w:tabs><w:spacing w:after="40"/><w:ind w:left="240"/></w:pPr>` +
            `<w:rPr><w14:numForm w14:val="lining"/></w:rPr>`) +
        `</w:styles>`
    );
}

function xmlAjustes(): string {
    return (
        XML_DECL +
        `<w:settings ${ATRS_RAIZ}>` +
        `<w:zoom w:percent="100"/>` +
        `<w:mirrorMargins/>` +
        `<w:defaultTabStop w:val="720"/>` +
        `<w:autoHyphenation/>` +
        `<w:consecutiveHyphenLimit w:val="2"/>` +
        `<w:hyphenationZone w:val="425"/>` +
        `<w:doNotHyphenateCaps/>` +
        `<w:evenAndOddHeaders/>` +
        `<w:characterSpacingControl w:val="doNotCompress"/>` +
        `<w:updateFields w:val="true"/>` +
        `<w:compat>` +
        `<w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/>` +
        `<w:compatSetting w:name="overrideTableStyleFontSizeAndJustification" w:uri="http://schemas.microsoft.com/office/word" w:val="1"/>` +
        `<w:compatSetting w:name="enableOpenTypeFeatures" w:uri="http://schemas.microsoft.com/office/word" w:val="1"/>` +
        `<w:compatSetting w:name="doNotFlipMirrorIndents" w:uri="http://schemas.microsoft.com/office/word" w:val="1"/>` +
        `<w:compatSetting w:name="differentiateMultirowTableHeaders" w:uri="http://schemas.microsoft.com/office/word" w:val="1"/>` +
        `</w:compat>` +
        `<w:decimalSymbol w:val=","/>` +
        `<w:listSeparator w:val=";"/>` +
        `</w:settings>`
    );
}

function xmlFuentes(): string {
    const fuente = (nombre: string, extra: string) =>
        `<w:font w:name="${nombre}">${extra}</w:font>`;
    const sigEndure = `<w:sig w:usb0="A00000EF" w:usb1="5000205B" w:usb2="00000000" w:usb3="00000000" w:csb0="00000093" w:csb1="00000000"/>`;
    const endure = (nombre: string) =>
        fuente(nombre,
            `<w:altName w:val="Garamond"/><w:charset w:val="00"/><w:family w:val="modern"/><w:notTrueType/><w:pitch w:val="variable"/>${sigEndure}`);
    return (
        XML_DECL +
        `<w:fonts ${ATRS_RAIZ}>` +
        endure("Amazon Endure Book") +
        endure("Amazon Endure Light") +
        endure("Amazon Endure SemiBold") +
        fuente("Garamond",
            `<w:panose1 w:val="02020404030301010803"/><w:charset w:val="00"/><w:family w:val="roman"/><w:pitch w:val="variable"/>` +
            `<w:sig w:usb0="00000287" w:usb1="00000000" w:usb2="00000000" w:usb3="00000000" w:csb0="0000009F" w:csb1="00000000"/>`) +
        fuente("Calibri",
            `<w:panose1 w:val="020F0502020204030204"/><w:charset w:val="00"/><w:family w:val="swiss"/><w:pitch w:val="variable"/>` +
            `<w:sig w:usb0="E4002EFF" w:usb1="C200247B" w:usb2="00000009" w:usb3="00000000" w:csb0="000001FF" w:csb1="00000000"/>`) +
        `</w:fonts>`
    );
}

function xmlCabecera(texto: string): string {
    const runs = texto ? xmlTexto(texto) : "";
    return XML_DECL + `<w:hdr ${ATRS_RAIZ}><w:p><w:pPr><w:pStyle w:val="Encabezado"/></w:pPr>${runs}</w:p></w:hdr>`;
}

function xmlPieVacio(): string {
    return XML_DECL + `<w:ftr ${ATRS_RAIZ}><w:p><w:pPr><w:pStyle w:val="Piedepagina"/></w:pPr></w:p></w:ftr>`;
}

function xmlPieNumero(): string {
    const rpr = `<w:rPr><w:rStyle w:val="Numerodepagina"/></w:rPr>`;
    return (
        XML_DECL +
        `<w:ftr ${ATRS_RAIZ}><w:p><w:pPr><w:pStyle w:val="Piedepagina"/></w:pPr>` +
        `<w:r>${rpr}<w:fldChar w:fldCharType="begin"/></w:r>` +
        `<w:r>${rpr}<w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>` +
        `<w:r>${rpr}<w:fldChar w:fldCharType="separate"/></w:r>` +
        `<w:r><w:rPr><w:rStyle w:val="Numerodepagina"/><w:noProof/></w:rPr><w:t>2</w:t></w:r>` +
        `<w:r>${rpr}<w:fldChar w:fldCharType="end"/></w:r>` +
        `</w:p></w:ftr>`
    );
}

function xmlContentTypes(): string {
    const o = (parte: string, tipo: string) => `<Override PartName="${parte}" ContentType="${tipo}"/>`;
    const wml = "application/vnd.openxmlformats-officedocument.wordprocessingml";
    return (
        XML_DECL +
        `<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">` +
        `<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>` +
        `<Default Extension="xml" ContentType="application/xml"/>` +
        o("/word/document.xml", `${wml}.document.main+xml`) +
        o("/word/styles.xml", `${wml}.styles+xml`) +
        o("/word/settings.xml", `${wml}.settings+xml`) +
        o("/word/fontTable.xml", `${wml}.fontTable+xml`) +
        o("/word/header1.xml", `${wml}.header+xml`) +
        o("/word/header2.xml", `${wml}.header+xml`) +
        o("/word/header3.xml", `${wml}.header+xml`) +
        o("/word/footer1.xml", `${wml}.footer+xml`) +
        o("/word/footer2.xml", `${wml}.footer+xml`) +
        o("/docProps/core.xml", "application/vnd.openxmlformats-package.core-properties+xml") +
        o("/docProps/app.xml", "application/vnd.openxmlformats-officedocument.extended-properties+xml") +
        `</Types>`
    );
}

function xmlRelsPaquete(): string {
    return (
        XML_DECL +
        `<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">` +
        `<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>` +
        `<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>` +
        `<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>` +
        `</Relationships>`
    );
}

function xmlRelsDocumento(): string {
    const rel = (id: string, tipo: string, destino: string) =>
        `<Relationship Id="${id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/${tipo}" Target="${destino}"/>`;
    return (
        XML_DECL +
        `<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">` +
        rel(RID.estilos, "styles", "styles.xml") +
        rel(RID.ajustes, "settings", "settings.xml") +
        rel(RID.fuentes, "fontTable", "fontTable.xml") +
        rel(RID.hdrVacio, "header", "header1.xml") +
        rel(RID.hdrAutor, "header", "header2.xml") +
        rel(RID.hdrTitulo, "header", "header3.xml") +
        rel(RID.ftrVacio, "footer", "footer1.xml") +
        rel(RID.ftrNumero, "footer", "footer2.xml") +
        `</Relationships>`
    );
}

function xmlCore(titulo: string, autor: string): string {
    return (
        XML_DECL +
        `<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" ` +
        `xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" ` +
        `xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">` +
        `<dc:title>${esc(titulo)}</dc:title><dc:creator>${esc(autor)}</dc:creator><dc:language>es-ES</dc:language>` +
        `</cp:coreProperties>`
    );
}

function xmlApp(): string {
    return (
        XML_DECL +
        `<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">` +
        `<Application>novela-cli</Application>` +
        `</Properties>`
    );
}

// ---------------------------------------------------------------------------
// Documento principal
// ---------------------------------------------------------------------------

export function generarDocx(op: OpcionesDocx): { docx: Buffer; stats: EstadisticasDocx } {
    const anio = op.anio ?? new Date().getFullYear();
    const incluirIndice = op.incluirIndice !== false;
    const capitulos = [...op.capitulos].sort((a, b) => a.n - b.n);
    const partesPorInicio = new Map<number, ParteDocx>();
    for (const p of op.partes) partesPorInicio.set(p.capitulo_inicial, p);

    const stats: EstadisticasDocx = { capitulos: 0, partes: 0, insets: 0, tablas: 0, separadores: 0 };
    const cuerpo: string[] = [];

    // --- Portada (sección centrada en vertical) ---
    cuerpo.push(xmlP("EndureBookTitle", xmlTexto(op.titulo)));
    cuerpo.push(P_VACIO, P_VACIO);
    if (op.subtitulo) {
        cuerpo.push(xmlP("EndureBookSubtitle", xmlTexto(op.subtitulo)));
    }
    for (let i = 0; i < 9; i++) cuerpo.push(P_VACIO);
    cuerpo.push(xmlP("EndureAuthorName", xmlTexto(op.autor), xmlSectPr({ front: true, vAlign: "center" })));

    // --- Copyright (alineado abajo; el espaciador cubre a los visores sin vAlign de sección) ---
    cuerpo.push(xmlP("EndureCopyrightPage", xmlTexto(`Derechos de autor © ${anio} ${op.autor}`), `<w:spacing w:before="10300"/>`));
    cuerpo.push(xmlP("EndureCopyrightPage", xmlTexto("Todos los derechos reservados."), xmlSectPr({ front: true, vAlign: "bottom" })));

    // --- Dedicatoria (opcional) ---
    if (op.dedicatoria) {
        cuerpo.push(xmlP("EndureChapterTitle", xmlTexto("Dedicatoria")));
        cuerpo.push(xmlP("EndureChapterTitle", ""), xmlP("EndureChapterTitle", ""));
        const lineas = op.dedicatoria.split(/\r?\n/).filter((l) => l.trim());
        lineas.forEach((linea, i) => {
            const esUltima = i === lineas.length - 1;
            cuerpo.push(
                xmlP("EndureFrontMatterBodyText", xmlTexto(linea.trim()), esUltima ? xmlSectPr({ front: true, vAlign: "center" }) : "")
            );
        });
    }

    // --- Contenido (índice con campo TOC) ---
    if (incluirIndice && capitulos.length) {
        cuerpo.push(xmlP("EndureChapterTitle", xmlTexto("Contenido")));
        cuerpo.push(xmlP("EndureChapterTitle", ""));
        const entradas: { estilo: string; texto: string }[] = [];
        for (const cap of capitulos) {
            const parte = partesPorInicio.get(cap.n);
            if (parte) entradas.push({ estilo: "TOC1", texto: `PARTE ${romano(parte.n)} — ${parte.titulo}` });
            entradas.push({ estilo: "TOC2", texto: `${cap.n}. ${cap.titulo}` });
        }
        const campoInicio =
            `<w:r><w:fldChar w:fldCharType="begin"/></w:r>` +
            `<w:r><w:instrText xml:space="preserve"> TOC \\f C \\z </w:instrText></w:r>` +
            `<w:r><w:fldChar w:fldCharType="separate"/></w:r>`;
        const campoFin = `<w:r><w:fldChar w:fldCharType="end"/></w:r>`;
        entradas.forEach((e, i) => {
            const runs =
                (i === 0 ? campoInicio : "") +
                xmlTexto(e.texto) +
                (i === entradas.length - 1 ? campoFin : "");
            cuerpo.push(xmlP(e.estilo, runs));
        });
        cuerpo.push(xmlP(null, "", xmlSectPr({ front: true })));
    }

    // --- Cuerpo de la novela ---
    let sectPrFinal = xmlSectPr({ inicioPagina: op.partes.length ? undefined : 1, folioPrimera: true });
    let primeraSeccionCuerpo = true;

    capitulos.forEach((cap, idx) => {
        const parte = partesPorInicio.get(cap.n);
        let capituloAbreParte = false;
        if (parte) {
            stats.partes++;
            capituloAbreParte = true;
            cuerpo.push(
                xmlP(
                    "EndureChapterTitle",
                    xmlTexto(`Parte ${romano(parte.n)}`) + campoTC(`PARTE ${romano(parte.n)} — ${parte.titulo}`, 1),
                    `<w:keepNext/><w:spacing w:before="5040"/>`
                )
            );
            cuerpo.push(xmlP("EndureBookSubtitle", xmlTexto(parte.titulo.toLocaleUpperCase("es-ES")), `<w:spacing w:before="240"/>`));
            // Cierre de la sección de la página de parte (empieza en página impar, sin folio).
            cuerpo.push(
                xmlP(null, "", xmlSectPr({ tipo: "oddPage", folioPrimera: false, inicioPagina: primeraSeccionCuerpo ? 1 : undefined }))
            );
            primeraSeccionCuerpo = false;
        }

        stats.capitulos++;
        cuerpo.push(
            xmlP(
                "EndureChapterTitle",
                xmlTexto(String(cap.n)) + campoTC(`${cap.n}. ${cap.titulo}`, 2),
                `<w:keepNext/><w:spacing w:before="1580"/>`
            )
        );
        cuerpo.push(xmlP("EndureChapterTitle", xmlTexto(cap.titulo), `<w:keepNext/><w:spacing w:after="317"/>`));

        for (const bloque of parseCuerpo(cap.cuerpo)) {
            if (bloque.tipo === "separador") {
                stats.separadores++;
                cuerpo.push(xmlP("EndureSceneBreak", xmlTexto("* * *")));
            } else if (bloque.tipo === "parrafo") {
                cuerpo.push(
                    xmlP(
                        bloque.primero ? "EndureFirstParagraphBodyText" : "EndureChapterBodyText",
                        bloque.runs.map((r) => xmlRun(r)).join("")
                    )
                );
            } else {
                stats.insets++;
                stats.tablas += bloque.items.filter((i) => i.tipo === "tabla").length;
                cuerpo.push(P_SEPARA_CAJA, xmlCaja(bloque.items), P_SEPARA_CAJA);
            }
        }

        const opcionesSeccion: OpcionesSeccion = {
            tipo: capituloAbreParte ? "oddPage" : "nextPage",
            folioPrimera: true,
            inicioPagina: primeraSeccionCuerpo ? 1 : undefined,
        };
        primeraSeccionCuerpo = false;
        if (idx === capitulos.length - 1) {
            sectPrFinal = xmlSectPr(opcionesSeccion);
        } else {
            cuerpo.push(xmlP(null, "", xmlSectPr(opcionesSeccion)));
        }
    });

    const documento =
        XML_DECL +
        `<w:document ${ATRS_RAIZ}><w:body>` +
        cuerpo.join("") +
        sectPrFinal +
        `</w:body></w:document>`;

    const docx = zipear([
        { nombre: "[Content_Types].xml", datos: xmlContentTypes() },
        { nombre: "_rels/.rels", datos: xmlRelsPaquete() },
        { nombre: "docProps/core.xml", datos: xmlCore(op.titulo, op.autor) },
        { nombre: "docProps/app.xml", datos: xmlApp() },
        { nombre: "word/document.xml", datos: documento },
        { nombre: "word/_rels/document.xml.rels", datos: xmlRelsDocumento() },
        { nombre: "word/styles.xml", datos: xmlEstilos() },
        { nombre: "word/settings.xml", datos: xmlAjustes() },
        { nombre: "word/fontTable.xml", datos: xmlFuentes() },
        { nombre: "word/header1.xml", datos: xmlCabecera("") },
        { nombre: "word/header2.xml", datos: xmlCabecera(op.autor.toLocaleUpperCase("es-ES")) },
        { nombre: "word/header3.xml", datos: xmlCabecera(op.titulo.toLocaleUpperCase("es-ES")) },
        { nombre: "word/footer1.xml", datos: xmlPieVacio() },
        { nombre: "word/footer2.xml", datos: xmlPieNumero() },
    ]);

    return { docx, stats };
}
