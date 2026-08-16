import { basename } from "node:path";
import { normalizar, palabras, existe, leer, STOP_ES, raizLigera } from "./util";
import { Capitulo } from "./Proyecto";

/**
 * Detección de repeticiones semánticas SIN gastar tokens.
 *
 * El juicio semántico (agrupar "se le hizo un nudo en la garganta" y "sintió un
 * nudo" bajo un mismo recurso, o marcar un gesto como tic de un personaje) lo
 * hace el archivista UNA vez por capítulo y lo consolida en `memoria/rasgos.md`.
 * Aquí solo contamos, de forma determinista, cuántas veces reaparece cada
 * recurso registrado y avisamos cuando se pasa de su tope. Además detectamos
 * "ecos" de gestos/sensaciones que aún no están catalogados.
 *
 * La comparación es tolerante a la flexión: se normaliza (sin tildes), se quitan
 * palabras funcionales y se aplica un stemming ligero, de modo que variantes como
 * "ajustó / ajustaba / ajustándose" cuenten como el mismo recurso.
 */

const STOP = STOP_ES;
export { raizLigera };

/** Conjunto de raíces significativas de un sintagma (sin funcionales). */
function stemsDe(sintagma: string): string[] {
  return palabras(normalizar(sintagma))
    .filter((w) => !STOP.has(w) && w.length > 2)
    .map(raizLigera)
    .filter((w) => w.length >= 3);
}

export type TipoRasgo = "tic" | "rasgo" | "sensacion";

export interface EntradaRasgo {
  personaje: string;
  tipo: TipoRasgo;
  canon: string;
  variantes: string[];
  tope?: number;
}

export interface AvisoRepeticion {
  clase: "tope" | "consecutivos" | "rasgo-redescrito" | "eco";
  personaje?: string;
  recurso: string;
  total: number;
  capitulos: string[];
  ejemploArchivo?: string;
  ejemploLinea?: number;
  mensaje: string;
}

export interface InformeRepeticiones {
  avisos: AvisoRepeticion[];
  /** Entradas del registro que no se han encontrado en ningún capítulo (posible desajuste). */
  huerfanos: string[];
}

type Cfg = {
  tope_tic_defecto?: number;
  tope_rasgo_defecto?: number;
  tope_sensacion_defecto?: number;
  avisar_consecutivos?: boolean;
  ngrama_ecos?: number;
  lexico_gesto?: string[];
  lexico_sensacion?: string[];
};

const nombreCap = (c: Capitulo) => basename(c.path).replace(/\.md$/, "");

export class AnalizadorRepeticiones {
  constructor(private cfg: Cfg = {}) {}

  /** Parsea la tabla de `memoria/rasgos.md`. Ignora cabecera, separador y filas de ejemplo. */
  static leerRegistro(path: string): EntradaRasgo[] {
    if (!existe(path)) return [];
    const out: EntradaRasgo[] = [];
    for (const linea of leer(path).split("\n")) {
      const t = linea.trim();
      if (!t.startsWith("|")) continue;
      const celdas = t.split("|").slice(1, -1).map((x) => x.trim());
      if (celdas.length < 4) continue;
      const [personaje, tipoRaw, canon, variantesRaw, , topeRaw] = celdas;
      // Saltar cabecera, separador y ejemplos/placeholder
      if (!personaje || !canon) continue;
      if (/^personaje$/i.test(personaje) || /^[-:\s]+$/.test(personaje)) continue;
      if (personaje.startsWith("_") || personaje.startsWith("[")) continue;
      if (/^[-:\s]+$/.test(canon) || canon.startsWith("_") || canon.startsWith("[")) continue;
      const tipo = (tipoRaw ?? "").toLowerCase();
      const tipoNorm: TipoRasgo = tipo.startsWith("tic")
        ? "tic"
        : tipo.startsWith("sens")
          ? "sensacion"
          : "rasgo";
      const variantes = (variantesRaw ?? "")
        .split(/[;/]/)
        .map((x) => x.trim())
        .filter((x) => x && !x.startsWith("_") && !x.startsWith("["));
      const tope = topeRaw && !Number.isNaN(Number(topeRaw)) ? Number(topeRaw) : undefined;
      out.push({ personaje, tipo: tipoNorm, canon, variantes, tope });
    }
    return out;
  }

  private topePorDefecto(tipo: TipoRasgo): number {
    if (tipo === "tic") return this.cfg.tope_tic_defecto ?? 3;
    if (tipo === "sensacion") return this.cfg.tope_sensacion_defecto ?? 2;
    return this.cfg.tope_rasgo_defecto ?? 2;
  }

  /** ¿El conjunto de raíces `necesita` está contenido en `frase`? */
  private static contiene(fraseStems: Set<string>, necesita: string[]): boolean {
    if (necesita.length === 0) return false;
    return necesita.every((s) => fraseStems.has(s));
  }

  analizar(caps: Capitulo[], registro: EntradaRasgo[]): InformeRepeticiones {
    const avisos: AvisoRepeticion[] = [];
    const huerfanos: string[] = [];

    // Pre-stemmiza cada frase de cada capítulo una sola vez.
    const capData = caps.map((c) => ({
      cap: c,
      nombre: nombreCap(c),
      frases: c.frases().map((f) => ({ linea: f.linea, stems: new Set(stemsDe(f.texto)) })),
    }));

    // 1) Recuento contra el registro
    for (const e of registro) {
      const claves = [stemsDe(e.canon), ...e.variantes.map(stemsDe)].filter((s) => s.length > 0);
      if (claves.length === 0) continue;

      let total = 0;
      const porCap: { nombre: string; n: number }[] = [];
      let ejemploArchivo: string | undefined;
      let ejemploLinea: number | undefined;

      for (const cd of capData) {
        let n = 0;
        for (const fr of cd.frases) {
          if (claves.some((k) => AnalizadorRepeticiones.contiene(fr.stems, k))) {
            n++;
            if (ejemploArchivo === undefined) {
              ejemploArchivo = cd.cap.path;
              ejemploLinea = fr.linea;
            }
          }
        }
        if (n > 0) porCap.push({ nombre: cd.nombre, n });
        total += n;
      }

      if (total === 0) {
        huerfanos.push(`${e.personaje} · ${e.canon}`);
        continue;
      }

      const tope = e.tope ?? this.topePorDefecto(e.tipo);
      const listaCaps = porCap.map((p) => `${p.nombre}×${p.n}`);

      if (total > tope) {
        avisos.push({
          clase: "tope",
          personaje: e.personaje,
          recurso: e.canon,
          total,
          capitulos: listaCaps,
          ejemploArchivo,
          ejemploLinea,
          mensaje: `"${e.canon}" (${e.tipo} de ${e.personaje}) aparece ${total} veces; tope ${tope}. Busca una alternativa o elimina alguna.`,
        });
      }

      // Rasgo físico redescrito: se fija una vez; repetir la descripción sobra.
      if (e.tipo === "rasgo" && total > 1) {
        avisos.push({
          clase: "rasgo-redescrito",
          personaje: e.personaje,
          recurso: e.canon,
          total,
          capitulos: listaCaps,
          ejemploArchivo,
          ejemploLinea,
          mensaje: `El rasgo "${e.canon}" de ${e.personaje} se describe ${total} veces. Un rasgo físico se establece una vez; después basta con nombrarlo de pasada, no redescribirlo.`,
        });
      }

      // Tic en capítulos consecutivos (cansa al lector).
      if (e.tipo === "tic" && (this.cfg.avisar_consecutivos ?? true)) {
        const nums = porCap
          .map((p) => Number((p.nombre.match(/(\d+)/) ?? [])[1]))
          .filter((x) => Number.isFinite(x))
          .sort((a, b) => a - b);
        const consec = nums.some((x, i) => i > 0 && x - nums[i - 1]! === 1);
        if (consec && total > 1) {
          avisos.push({
            clase: "consecutivos",
            personaje: e.personaje,
            recurso: e.canon,
            total,
            capitulos: listaCaps,
            ejemploArchivo,
            ejemploLinea,
            mensaje: `El tic "${e.canon}" de ${e.personaje} se repite en capítulos consecutivos. Espácialo o alterna con otro gesto propio del personaje.`,
          });
        }
      }
    }

    // 2) Ecos NO catalogados: n-gramas de raíces que reaparecen entre capítulos
    //    y que tocan el léxico corporal/sensorial (lo que el archivista aún no fijó).
    if (capData.length >= 2) {
      const n = this.cfg.ngrama_ecos ?? 4;
      const lexico = new Set(
        [...(this.cfg.lexico_gesto ?? []), ...(this.cfg.lexico_sensacion ?? [])].map((w) =>
          raizLigera(w)
        )
      );
      if (lexico.size > 0) {
        const grams = new Map<string, Set<string>>();
        for (const cd of capData) {
          const toks = palabras(normalizar(cd.cap.prosa()))
            .filter((w) => !STOP.has(w) && w.length > 2)
            .map(raizLigera);
          const vistos = new Set<string>();
          for (let i = 0; i + n <= toks.length; i++) {
            const ventana = toks.slice(i, i + n);
            if (!ventana.some((s) => lexico.has(s))) continue;
            const key = ventana.join(" ");
            if (vistos.has(key)) continue;
            vistos.add(key);
            const set = grams.get(key) ?? new Set<string>();
            set.add(cd.nombre);
            grams.set(key, set);
          }
        }
        for (const [key, cs] of grams) {
          if (cs.size >= 2) {
            avisos.push({
              clase: "eco",
              recurso: key,
              total: cs.size,
              capitulos: [...cs].sort(),
              mensaje: `Eco de una imagen corporal/sensorial ("${key}") en ${cs.size} capítulos. Si es intencional, catalógalo en rasgos.md con su tope; si no, varíalo.`,
            });
          }
        }
      }
    }

    return { avisos, huerfanos };
  }
}
