import { normalizar, palabras, media, desviacion, STOP_ES, raizLigera } from "./util";
import type { Frase } from "./util";
import type { Hallazgo, Severidad } from "./tipos";

export interface ContextoAnalisis {
  archivo: string;
  frases: Frase[];
  prosa: string;
  esCapitulo: boolean;
  /** POV declarado en el front-matter del capítulo (si lo hay). */
  pov?: string;
  /** Desplazamiento de línea del cuerpo respecto al fichero (para reportar bien). */
  offsetLinea: number;
  /** Cuerpo original (sin front-matter), con su markdown: para localizar separadores de escena. */
  cuerpo: string;
}

// Estructura flexible: las reglas leen lo que necesitan con valores por defecto.
export type ConfigLint = Record<string, any>;

export interface Regla {
  nombre: string;
  /** Máximo de ocurrencias por capítulo antes de convertirse en error; null = cada ocurrencia es aviso. */
  limitePorCapitulo(cfg: ConfigLint): number | null;
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[];
}

function frag(s: string, max = 90): string {
  const t = s.trim().replace(/\s+/g, " ");
  return t.length > max ? t.slice(0, max) + "…" : t;
}

function h(
  regla: string,
  sev: Severidad,
  archivo: string,
  linea: number,
  fragmento: string,
  mensaje: string
): Hallazgo {
  return { regla, severidad: sev, archivo, linea, fragmento: frag(fragmento), mensaje };
}

function ultimaPalabra(frase: string): string {
  const ps = palabras(frase);
  return ps.length ? normalizar(ps[ps.length - 1]!) : "";
}

function sufijoClase(palabra: string): string {
  if (palabra.endsWith("ndo")) return "gerundio";
  if (palabra.endsWith("mente")) return "mente";
  if (/(ado|ido|ada|ida)$/.test(palabra)) return "participio";
  if (/(cion|sion)$/.test(palabra)) return "cion";
  if (/(aba|ia|aban|ian)$/.test(palabra)) return "imperfecto";
  return "otro";
}

// 1) Antítesis negativa "No era X. Era Y." (prohibida) + variante "no... sino..."
export class ReglaAntitesis implements Regla {
  nombre = "antitesis-negativa";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis): Hallazgo[] {
    const out: Hallazgo[] = [];
    const ser = "(era|fue|es|seria|sera|parecia|estaba|fueron|eran|seria)";
    const reNeg = new RegExp(`^no\\s+${ser}\\b`);
    const reAfirm = new RegExp(`^${ser}\\b`);
    const fs = ctx.frases;
    for (let i = 0; i < fs.length - 1; i++) {
      const a = normalizar(fs[i]!.texto);
      const b = normalizar(fs[i + 1]!.texto);
      if (reNeg.test(a) && reAfirm.test(b)) {
        out.push(
          h(
            this.nombre,
            "error",
            ctx.archivo,
            fs[i]!.linea,
            `${fs[i]!.texto} ${fs[i + 1]!.texto}`,
            'Estructura antitética prohibida del tipo "No era X. Era Y.". Reescribe sin el contraste negativo→positivo.'
          )
        );
      }
    }
    // variante "no era ... sino ..."
    const reSino = new RegExp(`\\bno\\s+${ser}\\b.*\\bsino\\b`);
    for (const f of fs) {
      if (reSino.test(normalizar(f.texto))) {
        out.push(
          h(this.nombre, "aviso", ctx.archivo, f.linea, f.texto, 'Antítesis "no... sino...": valora una formulación más directa.')
        );
      }
    }
    return out;
  }
}

// 2) Personificación de lo abstracto
export class ReglaPersonificacion implements Regla {
  nombre = "personificacion-abstracta";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const sus: string[] = cfg.personificacion?.sustantivos ?? [];
    const ver: string[] = cfg.personificacion?.verbos ?? [];
    if (sus.length === 0 || ver.length === 0) return [];
    const re = new RegExp(
      `\\b(el|la|los|las)\\s+(${sus.map(normalizar).join("|")})\\s+(${ver.map(normalizar).join("|")})\\b`
    );
    const out: Hallazgo[] = [];
    for (const f of ctx.frases) {
      const m = normalizar(f.texto).match(re);
      if (m) {
        out.push(
          h(this.nombre, "error", ctx.archivo, f.linea, f.texto, `No atribuyas voluntad a lo abstracto ("${m[2]} ${m[3]}").`)
        );
      }
    }
    return out;
  }
}

// 3) Punto y coma / dos puntos (minimizar)
export class ReglaPuntuacion implements Regla {
  nombre = "puntuacion-pesada";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const out: Hallazgo[] = [];
    const np = palabras(ctx.prosa).length || 1;
    const pyc = (ctx.prosa.match(/;/g) ?? []).length;
    const dp = (ctx.prosa.match(/(?<!\d):(?!\d)/g) ?? []).length;
    const limPyc = cfg.limites?.punto_y_coma_por_mil ?? 2;
    const limDp = cfg.limites?.dos_puntos_por_mil ?? 3;
    const densPyc = (pyc * 1000) / np;
    const densDp = (dp * 1000) / np;
    if (densPyc > limPyc) {
      out.push(
        h(this.nombre, "aviso", ctx.archivo, 1, `${pyc} punto y coma`, `Densidad de ";" alta (${densPyc.toFixed(1)}/1000, máx ${limPyc}).`)
      );
    }
    if (densDp > limDp) {
      out.push(
        h(this.nombre, "aviso", ctx.archivo, 1, `${dp} dos puntos`, `Densidad de ":" alta (${densDp.toFixed(1)}/1000, máx ${limDp}).`)
      );
    }
    return out;
  }
}

// 4) Adverbios en -mente: ración por capítulo (1-2) + racimos en una frase.
//    Dentro de ración, silencio. A partir de ahí, cada sobrante es error.
export class ReglaMente implements Regla {
  nombre = "adverbios-mente";
  // La ración se gestiona dentro de analizar() para no molestar cuando se cumple.
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const out: Hallazgo[] = [];
    const cuota = cfg.limites?.mente_por_capitulo ?? 2;
    const occ: { linea: number; texto: string; palabra: string }[] = [];
    for (const f of ctx.frases) {
      const enFrase = normalizar(f.texto).match(/\w+mente\b/g) ?? [];
      for (const w of enFrase) occ.push({ linea: f.linea, texto: f.texto, palabra: w });
      // Dos -mente en la misma frase molestan aunque quepan en la ración: avísalo.
      if (enFrase.length >= 2) {
        out.push(
          h(this.nombre, "aviso", ctx.archivo, f.linea, f.texto, `Dos adverbios -mente en la misma frase (${enFrase.join(", ")}). Deja como mucho uno.`)
        );
      }
    }
    // Ración por capítulo: los que exceden la cuota son error (uno por sobrante).
    if (ctx.esCapitulo && occ.length > cuota) {
      for (let i = cuota; i < occ.length; i++) {
        const o = occ[i]!;
        out.push(
          h(this.nombre, "error", ctx.archivo, o.linea, o.texto, `Adverbio en -mente por encima de la ración (${occ.length} en el capítulo, máximo ${cuota}). Cambia "${o.palabra}" por un verbo más preciso.`)
        );
      }
    }
    return out;
  }
}

// 5) Cadencia monótona (coeficiente de variación de longitudes)
export class ReglaCadencia implements Regla {
  nombre = "cadencia-monotona";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const out: Hallazgo[] = [];
    const ventana = cfg.limites?.ventana_cadencia ?? 8;
    const cvMin = cfg.limites?.cv_cadencia_min ?? 0.45;
    const longs = ctx.frases.map((f) => palabras(f.texto).length);
    if (longs.length < ventana) return out;
    for (let i = 0; i + ventana <= longs.length; i += ventana) {
      const trozo = longs.slice(i, i + ventana);
      const m = media(trozo);
      if (m < 5) continue; // tramos muy cortos (diálogo) se ignoran
      const cv = desviacion(trozo) / m;
      if (cv < cvMin) {
        out.push(
          h(this.nombre, "aviso", ctx.archivo, ctx.frases[i]!.linea, `frases de longitud ~${m.toFixed(0)} palabras`, `Ritmo uniforme (CV=${cv.toFixed(2)}, mín ${cvMin}). Varía longitudes: alterna frases muy cortas con otras largas.`)
        );
      }
    }
    return out;
  }
}

// 6) Finales de frase monótonos (cadenas de misma forma)
export class ReglaFinalesMonotonos implements Regla {
  nombre = "finales-monotonos";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const out: Hallazgo[] = [];
    const minRun = cfg.limites?.run_finales_monotonos ?? 3;
    const clases = ctx.frases.map((f) => sufijoClase(ultimaPalabra(f.texto)));
    let i = 0;
    while (i < clases.length) {
      const cl = clases[i]!;
      let j = i;
      while (j < clases.length && clases[j] === cl) j++;
      const run = j - i;
      if (cl !== "otro" && run >= minRun) {
        out.push(h(this.nombre, "aviso", ctx.archivo, ctx.frases[i]!.linea, ctx.frases[i]!.texto, `${run} frases seguidas terminan en ${cl}. Rompe el patrón.`));
      }
      i = j;
    }
    // misma palabra final repetida en 3+ frases consecutivas
    let k = 0;
    const ult = ctx.frases.map((f) => ultimaPalabra(f.texto));
    while (k < ult.length) {
      const w = ult[k]!;
      let j = k;
      while (j < ult.length && ult[j] === w) j++;
      if (w && j - k >= 3) out.push(h(this.nombre, "aviso", ctx.archivo, ctx.frases[k]!.linea, ctx.frases[k]!.texto, `La palabra "${w}" cierra ${j - k} frases seguidas.`));
      k = j;
    }
    return out;
  }
}

// Utilidad: regla basada en lista de frases/regex con límite por capítulo
abstract class ReglaLista implements Regla {
  abstract nombre: string;
  abstract claveLista: string;
  abstract claveLimite: string;
  abstract mensaje: string;
  severidad: Severidad = "aviso";
  limitePorCapitulo(cfg: ConfigLint): number | null {
    const v = cfg.limites?.[this.claveLimite];
    return typeof v === "number" ? v : null;
  }
  patrones(cfg: ConfigLint): string[] {
    return cfg[this.claveLista] ?? [];
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const out: Hallazgo[] = [];
    const pats = this.patrones(cfg).map((p) => new RegExp(`\\b${normalizar(p).replace(/\s+/g, "\\s+")}\\b`));
    for (const f of ctx.frases) {
      const n = normalizar(f.texto);
      for (let pi = 0; pi < pats.length; pi++) {
        if (pats[pi]!.test(n)) {
          out.push(h(this.nombre, this.severidad, ctx.archivo, f.linea, f.texto, `${this.mensaje}: "${this.patrones(cfg)[pi]}".`));
        }
      }
    }
    return out;
  }
}

// 7) Clichés de IA / romance en español
export class ReglaCliches extends ReglaLista {
  nombre = "cliche-ia";
  claveLista = "cliches";
  claveLimite = "cliches_por_capitulo";
  mensaje = "Cliché frecuente en prosa de IA";
}

// 8) Micro-gestos sobreusados
export class ReglaMicroGestos extends ReglaLista {
  nombre = "micro-gestos";
  claveLista = "micro_gestos";
  claveLimite = "micro_gestos_por_capitulo";
  mensaje = "Micro-gesto repetitivo";
}

// 9) Filter words (distancian al lector)
export class ReglaFilterWords extends ReglaLista {
  nombre = "filter-words";
  claveLista = "filter_words";
  claveLimite = "filter_words_por_capitulo";
  mensaje = 'Verbo de filtro (acerca al POV quitándolo: "vio que la puerta..." → "la puerta...")';
}

// 10) Verbos de habla ornamentados
export class ReglaVerbosHabla extends ReglaLista {
  nombre = "verbos-habla-ornados";
  claveLista = "verbos_habla_ornados";
  claveLimite = "verbos_habla_ornados_por_capitulo";
  mensaje = 'Acotación de habla recargada (prefiere "dijo/preguntó")';
}

// 11) Tricolon ("A, B y C")
export class ReglaTricolon implements Regla {
  nombre = "tricolon";
  limitePorCapitulo(cfg: ConfigLint): number | null {
    return cfg.limites?.tricolon_por_capitulo ?? null;
  }
  analizar(ctx: ContextoAnalisis): Hallazgo[] {
    const out: Hallazgo[] = [];
    const re = /,\s[^,.;:]+,\s[^,.;:]+\s(?:y|e)\s[^,.;:]+/;
    for (const f of ctx.frases) {
      if (re.test(f.texto)) out.push(h(this.nombre, "aviso", ctx.archivo, f.linea, f.texto, "Patrón de tres elementos (tricolon). Úsalo con moderación."));
    }
    return out;
  }
}

// 12) Apertura débil del capítulo
export class ReglaAperturaDebil implements Regla {
  nombre = "apertura-debil";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    if (!ctx.esCapitulo || ctx.frases.length === 0) return [];
    const pats: string[] = cfg.apertura_debil ?? [];
    const primera = ctx.frases[0]!;
    const n = normalizar(primera.texto);
    for (const p of pats) {
      if (new RegExp(p).test(n)) {
        return [h(this.nombre, "aviso", ctx.archivo, primera.linea, primera.texto, "Apertura de capítulo débil (clima/despertar/espejo/tópico). El primer párrafo debe enganchar.")];
      }
    }
    return [];
  }
}

// 13) Cierre sentencioso del capítulo
export class ReglaCierreSentencioso implements Regla {
  nombre = "cierre-sentencioso";
  limitePorCapitulo(): number | null {
    return null;
  }
  private evaluar(frase: Frase, cfg: ConfigLint, archivo: string, donde: string): Hallazgo | null {
    const n = normalizar(frase.texto);
    const plantillas: string[] = cfg.cierre_sentencioso?.plantillas ?? [];
    for (const p of plantillas) {
      if (new RegExp(p).test(n)) {
        return h(this.nombre, "aviso", archivo, frase.linea, frase.texto, `Cierre sentencioso/epifonema (${donde}). Termina anclado en acción física, diálogo o detalle sensorial neutro.`);
      }
    }
    const abstractos: string[] = cfg.cierre_sentencioso?.sustantivos_abstractos ?? [];
    const concretos = /(mir|dij|cogi|abri|cerr|camin|toc|corr|golpe|sonri|llor|tembl|apret|empuj|gir|solt|arranc|salt)/;
    const tieneAbstracto = abstractos.some((a) => new RegExp(`\\b${normalizar(a)}\\b`).test(n));
    if (tieneAbstracto && !concretos.test(n)) {
      return h(this.nombre, "aviso", archivo, frase.linea, frase.texto, `Cierra en abstracción sin ancla física (${donde}). Busca un final concreto.`);
    }
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    if (!ctx.esCapitulo || ctx.frases.length === 0) return [];
    const out: Hallazgo[] = [];
    const fin = this.evaluar(ctx.frases[ctx.frases.length - 1]!, cfg, ctx.archivo, "fin de capítulo");
    if (fin) out.push(fin);
    // Cierres de escena: última frase antes de cada separador `* * *` del cuerpo original
    const lineas = ctx.cuerpo.split("\n");
    for (let i = 0; i < lineas.length; i++) {
      if (!/^\s*\*(\s*\*)+\s*$/.test(lineas[i]!)) continue;
      const lineaSep = i + 1 + ctx.offsetLinea;
      let previa: Frase | undefined;
      for (const f of ctx.frases) {
        if (f.linea < lineaSep) previa = f;
        else break;
      }
      if (previa) {
        const esc = this.evaluar(previa, cfg, ctx.archivo, "fin de escena");
        if (esc) out.push(esc);
      }
    }
    return out;
  }
}

// 14) Arranques monótonos: N frases seguidas empezando por la misma palabra
export class ReglaArranques implements Regla {
  nombre = "arranques-monotonos";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const minRun = cfg.limites?.run_arranques ?? 3;
    const inicios = ctx.frases.map((f) => {
      const t = f.texto.trim();
      if (/^[—–]/.test(t)) return ""; // el diálogo puede repetir arranque a propósito
      const ps = palabras(t.replace(/^[«"'\s]+/, ""));
      return ps.length ? normalizar(ps[0]!) : "";
    });
    const out: Hallazgo[] = [];
    let i = 0;
    while (i < inicios.length) {
      const w = inicios[i]!;
      let j = i;
      while (j < inicios.length && inicios[j] === w && w !== "") j++;
      if (w !== "" && j - i >= minRun) {
        out.push(
          h(this.nombre, "aviso", ctx.archivo, ctx.frases[i]!.linea, ctx.frases[i]!.texto, `${j - i} frases seguidas empiezan por "${w}". Varía el arranque (estilo §1).`)
        );
      }
      i = Math.max(j, i + 1);
    }
    return out;
  }
}

// 15) Eco léxico de proximidad: misma raíz significativa en frases muy cercanas
export class ReglaEcoLexico implements Regla {
  nombre = "eco-lexico";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const ventana = cfg.limites?.eco_ventana ?? 3;
    const minLen = cfg.limites?.eco_min_len ?? 4;
    if (ventana <= 0) return [];
    const out: Hallazgo[] = [];
    // Raíces significativas por frase (excluye funcionales y probables nombres propios)
    const porFrase = ctx.frases.map((f) => {
      const set = new Set<string>();
      for (const w of palabras(f.texto)) {
        if (/^[A-ZÁÉÍÓÚÜÑ]/.test(w)) continue; // nombres propios y arranques: otros vigilantes
        const n = normalizar(w);
        if (STOP_ES.has(n) || n.length <= 3) continue;
        const r = raizLigera(n);
        if (r.length >= minLen) set.add(r);
      }
      return set;
    });
    const ultimaVista = new Map<string, number>();
    for (let i = 0; i < porFrase.length; i++) {
      for (const r of porFrase[i]!) {
        const prev = ultimaVista.get(r);
        if (prev !== undefined && i - prev >= 1 && i - prev <= ventana) {
          out.push(
            h(this.nombre, "aviso", ctx.archivo, ctx.frases[i]!.linea, ctx.frases[i]!.texto, `Eco léxico: "${r}…" reaparece a ${i - prev} frase(s) de la anterior. Sustituye o distancia.`)
          );
        }
        ultimaVista.set(r, i);
      }
    }
    return out;
  }
}

// Verbos de vida interior (formas normalizadas, sin tildes)
const VERBOS_MENTALES =
  "penso|pensaba|supo|sabia|sintio|sentia|recordo|recordaba|comprendio|comprendia|imagino|imaginaba|deseo|deseaba|temio|temia|creyo|creia|intuyo|intuia|sospecho|sospechaba|quiso|anhelo|anhelaba|se pregunto|se preguntaba|se dijo";

// 16) Cabezeo (head-hopping): vida interior de un personaje que no es el POV
export class ReglaCabezeo implements Regla {
  nombre = "cabezeo";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    if (!ctx.esCapitulo || !ctx.pov) return [];
    const nombres: string[] = cfg.__nombres?.personajes ?? [];
    if (nombres.length === 0) return [];
    const povTokens = new Set(palabras(normalizar(ctx.pov)));
    const otros = nombres.map(normalizar).filter((n) => n.length >= 3 && !povTokens.has(n));
    if (otros.length === 0) return [];
    const alt = otros.join("|");
    const reDirecta = new RegExp(`\\b(${alt})\\s+(?:${VERBOS_MENTALES})\\b`);
    const reInversa = new RegExp(`\\b(?:${VERBOS_MENTALES})\\s+(${alt})\\b`);
    const out: Hallazgo[] = [];
    for (const f of ctx.frases) {
      const n = normalizar(f.texto);
      const m = n.match(reDirecta) ?? n.match(reInversa);
      if (m) {
        out.push(
          h(this.nombre, "aviso", ctx.archivo, f.linea, f.texto, `Posible cabezeo: vida interior de "${m[1]}" con POV ${ctx.pov}. Una sola cabeza por escena (estilo §8): muestra a los demás desde fuera (acción, diálogo, gesto).`)
        );
      }
    }
    return out;
  }
}

/** Distancia de edición ≤ 1 (inserción, borrado o sustitución de una letra). */
function lev1(a: string, b: string): boolean {
  if (a === b) return false;
  const la = a.length;
  const lb = b.length;
  if (Math.abs(la - lb) > 1) return false;
  let i = 0;
  let j = 0;
  let dif = 0;
  while (i < la && j < lb) {
    if (a[i] === b[j]) {
      i++;
      j++;
      continue;
    }
    if (++dif > 1) return false;
    if (la === lb) {
      i++;
      j++;
    } else if (la > lb) i++;
    else j++;
  }
  return dif + (la - i) + (lb - j) <= 1;
}

// 17) Guardián de nombres: tildes exactas y posibles erratas de nombre propio
export class ReglaNombresCanon implements Regla {
  nombre = "nombres-canon";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const conTilde: { exacto: string; norm: string }[] = cfg.__nombres?.tokensTilde ?? [];
    const todos: string[] = cfg.__nombres?.tokensTodos ?? [];
    if (conTilde.length === 0 && todos.length === 0) return [];
    const normTodos = new Set(todos.map(normalizar));
    const out: Hallazgo[] = [];
    for (const f of ctx.frases) {
      const ws = palabras(f.texto);
      for (let wi = 0; wi < ws.length; wi++) {
        const w = ws[wi]!;
        const wn = normalizar(w);
        // (a) Tilde perdida o cambiada: inequívoco → error
        for (const t of conTilde) {
          if (wn === t.norm && w.toLowerCase() !== t.exacto.toLowerCase()) {
            out.push(
              h(this.nombre, "error", ctx.archivo, f.linea, f.texto, `Nombre mal escrito: "${w}" → la forma canónica es "${t.exacto}" (memoria/nombres.md).`)
            );
          }
        }
        // (b) Errata a 1 letra de un nombre conocido (solo palabras capitalizadas en medio de frase)
        if (wi > 0 && /^[A-ZÁÉÍÓÚÜÑ]/.test(w) && wn.length >= 4 && !normTodos.has(wn)) {
          const cerca = todos.find((tok) => tok.length >= 4 && lev1(wn, normalizar(tok)));
          if (cerca) {
            out.push(
              h(this.nombre, "aviso", ctx.archivo, f.linea, f.texto, `¿Errata de nombre? "${w}" se parece a "${cerca}" (memoria/nombres.md).`)
            );
          }
        }
      }
    }
    return out;
  }
}

// 18) Párrafo-ladrillo
export class ReglaParrafoLadrillo implements Regla {
  nombre = "parrafo-ladrillo";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const max = cfg.limites?.parrafo_max_palabras ?? 150;
    const out: Hallazgo[] = [];
    const lineas = ctx.prosa.split("\n");
    let buf: string[] = [];
    let lineaInicio = 1;
    const cerrar = (finExclusivo: number) => {
      const texto = buf.join("\n").trim();
      if (texto) {
        const n = palabras(texto).length;
        if (n > max) {
          out.push(
            h(this.nombre, "aviso", ctx.archivo, lineaInicio + ctx.offsetLinea, texto, `Párrafo-ladrillo de ${n} palabras (máx ${max}). Trocéalo: respiro, acción o diálogo (estilo §1 y §9).`)
          );
        }
      }
      buf = [];
      lineaInicio = finExclusivo + 1;
    };
    for (let i = 0; i < lineas.length; i++) {
      if ((lineas[i] ?? "").trim() === "") {
        cerrar(i + 1);
      } else {
        if (buf.length === 0) lineaInicio = i + 1;
        buf.push(lineas[i]!);
      }
    }
    cerrar(lineas.length);
    return out;
  }
}

// 19) Proporción de diálogo fuera de rango
export class ReglaDialogoPct implements Regla {
  nombre = "dialogo-pct";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    if (!ctx.esCapitulo) return [];
    const min = cfg.limites?.dialogo_min_pct ?? 5;
    const max = cfg.limites?.dialogo_max_pct ?? 70;
    const total = palabras(ctx.prosa).length;
    if (total < 300) return []; // fragmentos: sin juicio
    let enDialogo = 0;
    for (const l of ctx.prosa.split("\n")) {
      if (/^\s*[—–]/.test(l)) enDialogo += palabras(l).length;
    }
    const pct = (enDialogo * 100) / total;
    if (pct < min) {
      return [
        h(this.nombre, "aviso", ctx.archivo, 1, `${pct.toFixed(0)}% de diálogo`, `Capítulo casi sin diálogo (${pct.toFixed(0)}%, umbral ${min}%). Si es deliberado, ignóralo; si no, airea la narración con escena dialogada.`),
      ];
    }
    if (pct > max) {
      return [
        h(this.nombre, "aviso", ctx.archivo, 1, `${pct.toFixed(0)}% de diálogo`, `Capítulo casi todo diálogo (${pct.toFixed(0)}% > ${max}%). Ancla las voces con acción, gesto y entorno.`),
      ];
    }
    return [];
  }
}

// 20) Puntuación con sabor a IA: exceso de dos puntos y de punto y coma
export class ReglaPuntuacionIA implements Regla {
  nombre = "puntuacion-ia";
  limitePorCapitulo(): number | null {
    return null;
  }
  analizar(ctx: ContextoAnalisis, cfg: ConfigLint): Hallazgo[] {
    const total = palabras(ctx.prosa).length;
    if (total < 300) return [];
    const maxDos = cfg.limites?.dospuntos_por_mil ?? 2;
    const maxPyc = cfg.limites?.punto_y_coma_por_mil ?? 1.5;
    const sinHoras = ctx.prosa.replace(/\d:\d/g, "");
    const dos = (sinHoras.match(/:/g) ?? []).length;
    const pyc = (ctx.prosa.match(/;/g) ?? []).length;
    const out: Hallazgo[] = [];
    const dosMil = (dos * 1000) / total;
    const pycMil = (pyc * 1000) / total;
    if (dosMil > maxDos) {
      out.push(
        h(this.nombre, "aviso", ctx.archivo, 1, `${dos} dos puntos en ${total} palabras`, `Exceso de dos puntos (${dosMil.toFixed(1)}‰ > ${maxDos}‰). El ":" explicativo es un tic de IA: casi siempre lo sustituye un punto o una reescritura.`)
      );
    }
    if (pycMil > maxPyc) {
      out.push(
        h(this.nombre, "aviso", ctx.archivo, 1, `${pyc} punto(s) y coma en ${total} palabras`, `Exceso de punto y coma (${pycMil.toFixed(1)}‰ > ${maxPyc}‰). En narrativa comercial casi siempre es un punto.`)
      );
    }
    return out;
  }
}

export const REGLAS: Regla[] = [
  new ReglaAntitesis(),
  new ReglaPersonificacion(),
  new ReglaPuntuacion(),
  new ReglaMente(),
  new ReglaCadencia(),
  new ReglaFinalesMonotonos(),
  new ReglaCliches(),
  new ReglaMicroGestos(),
  new ReglaFilterWords(),
  new ReglaVerbosHabla(),
  new ReglaTricolon(),
  new ReglaAperturaDebil(),
  new ReglaCierreSentencioso(),
  new ReglaArranques(),
  new ReglaEcoLexico(),
  new ReglaCabezeo(),
  new ReglaNombresCanon(),
  new ReglaParrafoLadrillo(),
  new ReglaDialogoPct(),
  new ReglaPuntuacionIA(),
];
