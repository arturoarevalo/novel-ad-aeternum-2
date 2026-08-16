import { leer, existe, normalizar, palabras, STOP_ES, parseFrontMatter, soloProsa, dividirFrases } from "./util";
import { cargarNombres } from "./LinterProsa";
import type { Proyecto } from "./Proyecto";
import { basename } from "node:path";

/**
 * Antiplagio, capa determinista (0 tokens): NO busca en la web; extrae y
 * prioriza los CANDIDATOS que hay que verificar con búsqueda exacta, porque
 * la memorización de los modelos no se distribuye uniforme:
 *
 * - CRÍTICO: versos/epígrafes (blockquotes y líneas enteras en cursiva) y
 *   citas atribuidas a nombres que no son personajes. Verificar TODOS.
 * - ALTA: primera y última frase de cada capítulo (ecos de aperturas/cierres
 *   célebres) y aforismos (frase corta con verbo copulativo + abstracto).
 * - MEDIA: n-gramas distintivos (ventanas de ~10 palabras con léxico raro),
 *   muestreo con mayor puntuación de rareza por capítulo.
 * - TÉRMINOS: nombres propios y neologismos de memoria/nombres.md (colisión
 *   con ficción existente).
 */

export interface Candidato {
  prioridad: "CRITICO" | "ALTA" | "MEDIA";
  tipo: string;
  cap: string;
  linea: number;
  texto: string;
}

export interface InformeOriginalidad {
  candidatos: Candidato[];
  terminos: string[];
}

type Cfg = { ngramas_por_capitulo?: number; ngrama_len?: number; aforismos_por_capitulo?: number };

function rareza(ws: string[]): number {
  let p = 0;
  for (const w of ws) {
    const n = normalizar(w);
    if (STOP_ES.has(n) || n.length < 7) continue;
    p += n.length + (n.length >= 10 ? 3 : 0);
  }
  return p;
}

export class AnalizadorOriginalidad {
  constructor(
    private proyecto: Proyecto,
    private cfg: Cfg = {}
  ) {}

  analizar(): InformeOriginalidad {
    const K = this.cfg.ngramas_por_capitulo ?? 4;
    const N = this.cfg.ngrama_len ?? 10;
    const maxAfor = this.cfg.aforismos_por_capitulo ?? 3;
    const candidatos: Candidato[] = [];
    const nombres = cargarNombres(this.proyecto.ruta());
    const personajesNorm = new Set(nombres.personajes.map(normalizar));

    let abstractos: string[] = [];
    const cfgLintPath = this.proyecto.ruta("lint-prosa.config.json");
    if (existe(cfgLintPath)) {
      try {
        abstractos = (JSON.parse(leer(cfgLintPath)).cierre_sentencioso?.sustantivos_abstractos ?? []) as string[];
      } catch {
        /* sin config */
      }
    }
    const reCopula = /\b(es|era|eran|son|fue|sera|seria|parece|parecia)\b/;
    const reCita = /[«"][^»"]{20,}[»"]\s*[—–-]\s*([A-ZÁÉÍÓÚÜÑ][\p{L}]+)/u;

    for (const c of this.proyecto.capitulos()) {
      const cap = basename(c.path).replace(/\.md$/, "");
      const doc = parseFrontMatter(leer(c.path));
      const off = doc.lineaCuerpo - 1;
      const frases = dividirFrases(soloProsa(doc.cuerpo), off);
      if (frases.length === 0) continue;

      const lineas = doc.cuerpo.split("\n");
      for (let i = 0; i < lineas.length; i++) {
        const t = lineas[i]!.trim();
        const esQuote = t.startsWith("> ") && t.length > 12;
        const esCursiva = /^[*_][^*_].{10,}[*_]$/.test(t);
        if (esQuote || esCursiva) {
          candidatos.push({ prioridad: "CRITICO", tipo: esQuote ? "epígrafe/cita" : "verso/cursiva", cap, linea: i + 1 + off, texto: t.replace(/^>\s*/, "").replace(/^[*_]|[*_]$/g, "").trim() });
        }
      }

      for (const f of frases) {
        const m = f.texto.match(reCita);
        if (m && !personajesNorm.has(normalizar(m[1]!))) {
          candidatos.push({ prioridad: "CRITICO", tipo: `cita atribuida a ${m[1]}`, cap, linea: f.linea, texto: f.texto.trim() });
        }
      }

      candidatos.push({ prioridad: "ALTA", tipo: "apertura", cap, linea: frases[0]!.linea, texto: frases[0]!.texto.trim() });
      const ult = frases[frases.length - 1]!;
      candidatos.push({ prioridad: "ALTA", tipo: "cierre", cap, linea: ult.linea, texto: ult.texto.trim() });

      const afor = frases
        .filter((f) => {
          const ws = palabras(f.texto);
          if (ws.length < 4 || ws.length > 14) return false;
          const n = normalizar(f.texto);
          return reCopula.test(n) && abstractos.some((a) => n.includes(normalizar(a)));
        })
        .sort((a, b) => rareza(palabras(b.texto)) - rareza(palabras(a.texto)))
        .slice(0, maxAfor);
      for (const f of afor) candidatos.push({ prioridad: "ALTA", tipo: "aforismo", cap, linea: f.linea, texto: f.texto.trim() });

      const ventanas: { linea: number; texto: string; p: number; clave: string }[] = [];
      for (const f of frases) {
        const ws = palabras(f.texto);
        for (let i = 0; i + N <= ws.length; i += 3) {
          const v = ws.slice(i, i + N);
          ventanas.push({ linea: f.linea, texto: v.join(" "), p: rareza(v), clave: `${f.linea}` });
        }
      }
      ventanas.sort((a, b) => b.p - a.p);
      const usadas = new Set<string>();
      for (const v of ventanas) {
        if (usadas.size >= K) break;
        if (v.p < 20 || usadas.has(v.clave)) continue;
        usadas.add(v.clave);
        candidatos.push({ prioridad: "MEDIA", tipo: "n-grama distintivo", cap, linea: v.linea, texto: v.texto });
      }
    }

    const terminos = new Set<string>();
    const pNombres = this.proyecto.ruta("memoria", "nombres.md");
    if (existe(pNombres)) {
      for (const linea of leer(pNombres).split("\n")) {
        const t = linea.trim();
        if (!t.startsWith("- ") || t.startsWith("- _") || t.startsWith("- [")) continue;
        const canon = (t.slice(2).split(" — ")[0] ?? "").trim();
        if (canon.length >= 3) terminos.add(canon);
      }
    }

    return { candidatos, terminos: [...terminos] };
  }
}
