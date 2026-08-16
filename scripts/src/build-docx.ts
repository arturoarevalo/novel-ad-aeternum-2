import { writeFileSync, mkdirSync } from "node:fs";
import { Proyecto, Capitulo } from "./lib/Proyecto";
import { existe, c } from "./lib/util";
import { generarDocx, type CapituloDocx, type ParteDocx } from "./lib/DocxNovela";

export function run(_args: string[]): number {
    const proyecto = new Proyecto();
    const meta = proyecto.metadatos();
    const ordenados = [...meta.capitulos].sort((a, b) => a.n - b.n);

    const capitulos: CapituloDocx[] = [];
    const faltan: number[] = [];
    for (const cm of ordenados) {
        const p = proyecto.ruta("capitulos", cm.archivo);
        if (!existe(p)) {
            faltan.push(cm.n);
            continue;
        }
        const cap = new Capitulo(p);
        capitulos.push({
            n: cm.n,
            titulo: cap.titulo || cm.titulo || `Capítulo ${cm.n}`,
            cuerpo: cap.cuerpo,
        });
    }

    const partes: ParteDocx[] = meta.partes ?? [];
    // Sanidad de la partición: cada capítulo debe caer en una parte como mucho.
    if (partes.length) {
        const porOrden = [...partes].sort((a, b) => a.capitulo_inicial - b.capitulo_inicial);
        for (let i = 1; i < porOrden.length; i++) {
            const previa = porOrden[i - 1]!;
            const actual = porOrden[i]!;
            if (previa.capitulo_final !== undefined && actual.capitulo_inicial <= previa.capitulo_final) {
                console.log(
                    c.amarillo(
                        `⚠ partes solapadas en metadatos.json: "${previa.titulo}" acaba en ${previa.capitulo_final} y "${actual.titulo}" empieza en ${actual.capitulo_inicial}`
                    )
                );
            }
        }
    }

    const { docx, stats } = generarDocx({
        titulo: meta.titulo,
        subtitulo: meta.subtitulo || undefined,
        autor: meta.autor,
        anio: meta.anio_copyright,
        dedicatoria: meta.dedicatoria,
        partes,
        capitulos,
    });

    mkdirSync(proyecto.ruta("builds"), { recursive: true });
    const salida = proyecto.ruta("builds", `${meta.slug}.docx`);
    writeFileSync(salida, docx);

    console.log(c.verde(`✔ build-docx: ${salida}`));
    console.log(`  capítulos: ${stats.capitulos}/${ordenados.length}` + (faltan.length ? c.amarillo(`  (faltan: ${faltan.join(", ")})`) : ""));
    console.log(`  partes: ${stats.partes} · insets: ${stats.insets} (${stats.tablas} con tabla) · separadores de escena: ${stats.separadores}`);
    console.log(`  tamaño: ${(docx.length / 1024).toFixed(0)} KB`);
    console.log(c.gris(`  El índice se pagina al abrir el documento en Word (o con Ctrl+A y F9).`));
    return 0;
}
