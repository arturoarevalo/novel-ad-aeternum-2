import { readFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";
import type { DocConFrontMatter, FrontMatter } from "./tipos";

// --- Colores de consola (sin dependencias) ---
const tty = process.stdout.isTTY;
export const c = {
  rojo: (s: string) => (tty ? `\x1b[31m${s}\x1b[0m` : s),
  verde: (s: string) => (tty ? `\x1b[32m${s}\x1b[0m` : s),
  amarillo: (s: string) => (tty ? `\x1b[33m${s}\x1b[0m` : s),
  azul: (s: string) => (tty ? `\x1b[34m${s}\x1b[0m` : s),
  gris: (s: string) => (tty ? `\x1b[90m${s}\x1b[0m` : s),
  negrita: (s: string) => (tty ? `\x1b[1m${s}\x1b[0m` : s),
};

// --- Normalización para comparaciones insensibles a tildes/mayúsculas ---
export function normalizar(s: string): string {
  return s
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();
}

// --- Léxico funcional del español (para filtrar comparaciones semánticas) ---
export const STOP_ES = new Set(
  "el la los las un una unos unas lo al a de del en y e o u que se su sus mi mis tu tus me te le les nos os con por para mas pero como cuando donde si no ni ya muy es era fue ha han habia había hasta sin sobre entre tras cada este esta esto ese esa eso aquel aquella".split(
    /\s+/
  )
);

/** Stemming ligero y CONSERVADOR del español: recorta una terminación flexiva
 *  frecuente solo si deja una raíz de al menos 3 letras. Suficiente para que
 *  "ajustó / ajustaba / ajustándose" cuenten como el mismo recurso. */
export function raizLigera(palabra: string): string {
  let s = normalizar(palabra);
  s = s.replace(/mente$/, "");
  const term =
    /(aciones|acion|amiento|imiento|abamos|ariamos|eriamos|iriamos|aban|iendo|ando|adas|ados|idas|idos|ada|ado|ida|ido|amos|emos|imos|aron|ieron|aran|eran|iran|aba|ara|era|ira|are|ere|ire|an|en|as|os|es|a|o|e|s)$/;
  const m = s.match(term);
  if (m && s.length - m[0]!.length >= 3) s = s.slice(0, s.length - m[0]!.length);
  return s;
}

// --- Slug ---
export function slugify(s: string): string {
  return normalizar(s)
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

// --- Lectura segura ---
export function leer(path: string): string {
  return readFileSync(path, "utf8");
}

export function existe(path: string): boolean {
  return existsSync(path);
}

export function mtime(path: string): number {
  return statSync(path).mtimeMs;
}

/** Lista ficheros (recursivo) que cumplen un filtro de extensión. */
export function listarFicheros(dir: string, ext = ".md"): string[] {
  if (!existsSync(dir)) return [];
  const out: string[] = [];
  for (const entrada of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, entrada.name);
    if (entrada.isDirectory()) out.push(...listarFicheros(p, ext));
    else if (entrada.name.endsWith(ext)) out.push(p);
  }
  return out.sort();
}

// --- Front-matter YAML sencillo (clave: valor, listas como [a, b] o coma) ---
export function parseFrontMatter(texto: string): DocConFrontMatter {
  if (!texto.startsWith("---")) {
    return { fm: {}, cuerpo: texto, lineaCuerpo: 1 };
  }
  const lineas = texto.split("\n");
  let fin = -1;
  for (let i = 1; i < lineas.length; i++) {
    if (lineas[i]?.trim() === "---") {
      fin = i;
      break;
    }
  }
  if (fin === -1) return { fm: {}, cuerpo: texto, lineaCuerpo: 1 };

  const fm: FrontMatter = {};
  for (let i = 1; i < fin; i++) {
    const linea = lineas[i] ?? "";
    const m = linea.match(/^([\w-]+):\s*(.*)$/);
    if (!m) continue;
    const clave = m[1]!;
    let valor = (m[2] ?? "").trim();
    if (valor.startsWith("[") && valor.endsWith("]")) {
      fm[clave] = valor
        .slice(1, -1)
        .split(",")
        .map((x) => x.trim().replace(/^["']|["']$/g, ""))
        .filter(Boolean);
    } else if (valor === "true" || valor === "false") {
      fm[clave] = valor === "true";
    } else if (valor !== "" && !Number.isNaN(Number(valor))) {
      fm[clave] = Number(valor);
    } else {
      fm[clave] = valor.replace(/^["']|["']$/g, "");
    }
  }
  const cuerpo = lineas.slice(fin + 1).join("\n");
  return { fm, cuerpo, lineaCuerpo: fin + 2 };
}

// --- Tokenización de prosa ---

/** Quita marcas markdown ligeras y bloques de código/encabezados para analizar prosa. */
export function soloProsa(cuerpo: string): string {
  return cuerpo
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/^#{1,6}\s.*$/gm, " ")
    .replace(/^\s*>.*$/gm, " ")
    .replace(/[*_`]/g, "");
}

export interface Frase {
  texto: string;
  /** Línea (1-based, relativa al cuerpo) donde empieza la frase. */
  linea: number;
}

/** Divide en frases respetando ., !, ?, … y cierres de comillas/raya. */
export function dividirFrases(cuerpo: string, offsetLinea = 0): Frase[] {
  const frases: Frase[] = [];
  const lineas = cuerpo.split("\n");
  let acumulado = "";
  let lineaInicio = 1;
  let lineaActual = 1;

  const empujar = () => {
    const t = acumulado.trim();
    if (t.length > 0) frases.push({ texto: t, linea: lineaInicio + offsetLinea });
    acumulado = "";
  };

  for (let li = 0; li < lineas.length; li++) {
    lineaActual = li + 1;
    const linea = lineas[li] ?? "";
    if (linea.trim() === "") {
      empujar();
      lineaInicio = lineaActual + 1;
      continue;
    }
    if (acumulado === "") lineaInicio = lineaActual;
    for (const ch of linea) {
      acumulado += ch;
      if (/[.!?…]/.test(ch)) {
        // cierre de frase (se permite arrastrar comillas/raya posteriores en bruto)
        empujar();
        lineaInicio = lineaActual;
      }
    }
    acumulado += " ";
  }
  empujar();
  return frases;
}

export function palabras(texto: string): string[] {
  const m = texto.match(/[\p{L}\p{N}']+/gu);
  return m ?? [];
}

export function contarPalabras(texto: string): number {
  return palabras(texto).length;
}

export function media(xs: number[]): number {
  if (xs.length === 0) return 0;
  return xs.reduce((a, b) => a + b, 0) / xs.length;
}

export function desviacion(xs: number[]): number {
  if (xs.length < 2) return 0;
  const m = media(xs);
  const v = xs.reduce((a, b) => a + (b - m) ** 2, 0) / xs.length;
  return Math.sqrt(v);
}

// --- Glob muy sencillo (solo *, ?, y {captura}) a RegExp ---
export interface GlobCompilado {
  re: RegExp;
  capturas: string[];
}

export function compilarGlob(patron: string): GlobCompilado {
  const capturas: string[] = [];
  let re = "^";
  for (let i = 0; i < patron.length; i++) {
    const ch = patron[i]!;
    if (ch === "*") re += "[^/]*";
    else if (ch === "?") re += "[^/]";
    else if (ch === "{") {
      let j = i + 1;
      let nombre = "";
      while (j < patron.length && patron[j] !== "}") nombre += patron[j++];
      i = j;
      capturas.push(nombre);
      re += "([^/]+?)";
    } else if (/[.+^${}()|[\]\\]/.test(ch)) re += "\\" + ch;
    else re += ch;
  }
  re += "$";
  return { re: new RegExp(re), capturas };
}
