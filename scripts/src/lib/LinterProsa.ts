import { dirname, join } from "node:path";
import { leer, existe, soloProsa, dividirFrases, parseFrontMatter, normalizar, STOP_ES } from "./util";
import { REGLAS } from "./reglas";
import type { ContextoAnalisis, ConfigLint } from "./reglas";
import type { Hallazgo } from "./tipos";

export interface InformeLint {
  hallazgos: Hallazgo[];
  errores: number;
  avisos: number;
}

/** Extrae de memoria/nombres.md el material que usan las reglas de nombres y cabezeo. */
export function cargarNombres(raiz: string): { personajes: string[]; tokensTilde: { exacto: string; norm: string }[]; tokensTodos: string[] } {
  const vacio = { personajes: [] as string[], tokensTilde: [] as { exacto: string; norm: string }[], tokensTodos: [] as string[] };
  const p = join(raiz, "memoria", "nombres.md");
  if (!existe(p)) return vacio;
  const personajes: string[] = [];
  const tokensTodos = new Set<string>();
  let seccion = "";
  for (const linea of leer(p).split("\n")) {
    const t = linea.trim();
    if (t.startsWith("## ")) {
      seccion = t.slice(3).toLowerCase();
      continue;
    }
    if (!t.startsWith("- ") || t.startsWith("- _") || t.startsWith("- [")) continue;
    const resto = t.slice(2);
    const canon = (resto.split(" — ")[0] ?? "").trim();
    if (!canon) continue;
    const alias = [...resto.matchAll(/"([^"]+)"|«([^»]+)»/g)].map((m) => (m[1] ?? m[2] ?? "").trim()).filter(Boolean);
    const formas = [canon, ...alias];
    for (const forma of formas) {
      for (const tok of forma.split(/\s+/)) {
        const limpio = tok.replace(/[^\p{L}]/gu, "");
        // Las formas canónicas incluyen títulos de obras y rótulos («¿Qué les pasa…?»):
        // sus palabras funcionales no son nombres y envenenarían el pool (cada «que»
        // de la prosa saldría marcado contra «Qué»).
        if (limpio.length >= 3 && !STOP_ES.has(normalizar(limpio))) tokensTodos.add(limpio);
      }
    }
    if (seccion.startsWith("personaje")) {
      for (const forma of formas) {
        const primero = (forma.split(/\s+/)[0] ?? "").replace(/[^\p{L}]/gu, "");
        if (primero.length >= 3) personajes.push(primero);
      }
    }
  }
  const norm = (s: string) => s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
  const tokensTilde = [...tokensTodos]
    .filter((tok) => /[áéíóúüñÁÉÍÓÚÜÑ]/.test(tok))
    .map((exacto) => ({ exacto, norm: norm(exacto) }));
  return { personajes: [...new Set(personajes)], tokensTilde, tokensTodos: [...tokensTodos] };
}

export class LinterProsa {
  private cfg: ConfigLint;

  constructor(configPath: string) {
    this.cfg = existe(configPath) ? (JSON.parse(leer(configPath)) as ConfigLint) : {};
    // Material canónico para las reglas de nombres/cabezeo (clave interna).
    this.cfg.__nombres = cargarNombres(dirname(configPath));
  }

  private contexto(archivo: string, esCapitulo: boolean): ContextoAnalisis {
    const doc = parseFrontMatter(leer(archivo));
    const prosa = soloProsa(doc.cuerpo);
    const frases = dividirFrases(prosa, doc.lineaCuerpo - 1);
    const pov = typeof doc.fm["pov"] === "string" && doc.fm["pov"] ? String(doc.fm["pov"]) : undefined;
    return { archivo, prosa, frases, esCapitulo, pov, offsetLinea: doc.lineaCuerpo - 1, cuerpo: doc.cuerpo };
  }

  /** Analiza un único fichero. */
  analizarFichero(archivo: string, esCapitulo = true): InformeLint {
    const ctx = this.contexto(archivo, esCapitulo);
    const hallazgos: Hallazgo[] = [];
    const conteo = new Map<string, number>();

    for (const regla of REGLAS) {
      const hs = regla.analizar(ctx, this.cfg);
      for (const x of hs) conteo.set(x.regla, (conteo.get(x.regla) ?? 0) + 1);
      hallazgos.push(...hs);

      const limite = regla.limitePorCapitulo(this.cfg);
      const n = conteo.get(regla.nombre) ?? 0;
      if (limite !== null && n > limite) {
        hallazgos.push({
          regla: regla.nombre,
          severidad: "error",
          archivo,
          linea: 1,
          fragmento: `${n} ocurrencias`,
          mensaje: `Límite por capítulo superado para "${regla.nombre}": ${n} > ${limite}.`,
        });
      }
    }

    hallazgos.sort((a, b) => a.linea - b.linea);
    return {
      hallazgos,
      errores: hallazgos.filter((x) => x.severidad === "error").length,
      avisos: hallazgos.filter((x) => x.severidad === "aviso").length,
    };
  }

  /** Conteos por regla agregados sobre varios ficheros (para límites de toda la novela). */
  limitesNovela(archivos: string[]): Hallazgo[] {
    const limPorNovela: Record<string, number> = this.cfg.limites_novela ?? {};
    if (Object.keys(limPorNovela).length === 0) return [];
    const total = new Map<string, number>();
    for (const a of archivos) {
      const inf = this.analizarFichero(a, true);
      for (const x of inf.hallazgos) {
        if (x.severidad === "error" && x.fragmento.endsWith("ocurrencias")) continue;
        total.set(x.regla, (total.get(x.regla) ?? 0) + 1);
      }
    }
    const out: Hallazgo[] = [];
    for (const [regla, lim] of Object.entries(limPorNovela)) {
      const n = total.get(regla) ?? 0;
      if (n > lim) {
        out.push({
          regla,
          severidad: "error",
          archivo: "(toda la novela)",
          linea: 1,
          fragmento: `${n} ocurrencias`,
          mensaje: `Límite de novela superado para "${regla}": ${n} > ${lim}.`,
        });
      }
    }
    return out;
  }
}
