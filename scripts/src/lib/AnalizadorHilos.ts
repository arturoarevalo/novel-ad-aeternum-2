import { basename } from "node:path";
import { leer, existe, normalizar } from "./util";
import type { Proyecto } from "./Proyecto";

/**
 * Salud narrativa determinista (0 tokens) a partir de los ledgers de la biblia:
 *
 * - Presagios (biblia/presagios.md): avisa de los que ya deberían haberse
 *   recogido (recogida prevista ≤ último capítulo escrito y siguen abiertos)
 *   y de los marcados huérfanos. Igual con las pistas falsas sin desactivar.
 * - Tensión (memoria/preguntas-abiertas.md): si no queda NINGUNA pregunta
 *   dramática mayor abierta y aún faltan capítulos, la novela va sin motor.
 * - Forma: capítulos cuya longitud se desvía demasiado de la mediana
 *   (caza el desinfle progresivo típico de las tiradas largas).
 */

export interface PresagioRiesgo {
  id: string;
  que: string;
  prevista?: number;
  estado: string;
}

export interface CapDesviado {
  cap: string;
  palabras: number;
  pct: number;
}

export interface PresupuestoInfo {
  objetivoTotal?: number;
  escritas: number;
  proyeccion?: number;
  desvioProyeccionPct?: number;
  capsSobre: { cap: string; palabras: number; objetivo: number; pct: number }[];
}

export interface InformeHilos {
  presagiosVencidos: PresagioRiesgo[];
  presagiosHuerfanos: PresagioRiesgo[];
  pistasSinDesactivar: PresagioRiesgo[];
  preguntasMayoresAbiertas: number;
  preguntasMayoresTotal: number;
  tensionCero: boolean;
  medianaPalabras: number;
  capsDesviados: CapDesviado[];
  presupuesto: PresupuestoInfo;
  /** Total de señales (para la puerta de salud). */
  senales: number;
}

type Cfg = { desvio_longitud_pct?: number; tolerancia_capitulo_pct?: number; tolerancia_proyeccion_pct?: number };

function primerNumero(s: string): number | undefined {
  const m = s.match(/(\d+)/);
  return m ? Number(m[1]) : undefined;
}

function filaReal(celda: string | undefined): boolean {
  if (!celda) return false;
  const t = celda.trim();
  return t !== "" && !t.startsWith("_") && !t.startsWith("[") && !/^[-:\s]+$/.test(t);
}

export class AnalizadorHilos {
  constructor(
    private proyecto: Proyecto,
    private cfg: Cfg = {}
  ) {}

  analizar(): InformeHilos {
    const caps = this.proyecto.capitulos();
    const nums = caps.map((c) => c.numero).filter((n): n is number => typeof n === "number");
    const maxCap = nums.length ? Math.max(...nums) : 0;

    let pendientes = 0;
    try {
      pendientes = this.proyecto.capitulosPendientes().length;
    } catch {
      /* sin metadatos aún */
    }

    // --- Presagios y pistas falsas ---
    const presagiosVencidos: PresagioRiesgo[] = [];
    const presagiosHuerfanos: PresagioRiesgo[] = [];
    const pistasSinDesactivar: PresagioRiesgo[] = [];
    const pPres = this.proyecto.ruta("biblia", "presagios.md");
    if (existe(pPres)) {
      let seccion = "";
      for (const linea of leer(pPres).split("\n")) {
        const t = linea.trim();
        if (t.startsWith("## ")) {
          seccion = normalizar(t.slice(3));
          continue;
        }
        if (!t.startsWith("|")) continue;
        const celdas = t.split("|").slice(1, -1).map((x) => x.trim());
        if (celdas.length < 4) continue;
        const [id, que] = celdas;
        if (!filaReal(id) || /^id$/i.test(id!) || !filaReal(que)) continue;

        if (seccion.startsWith("presagio")) {
          // | id | qué | siembra | refuerzos | recogida prevista | estado |
          const prevista = primerNumero(celdas[4] ?? "");
          const estado = normalizar(celdas[5] ?? "");
          if (estado.includes("huerfano")) {
            presagiosHuerfanos.push({ id: id!, que: que!, prevista, estado: celdas[5] ?? "" });
          } else if (!estado.includes("pagado") && prevista !== undefined && maxCap > 0 && prevista <= maxCap) {
            presagiosVencidos.push({ id: id!, que: que!, prevista, estado: celdas[5] ?? "" });
          }
        } else if (seccion.startsWith("pistas")) {
          // | id | falsa pista | siembra | a qué apunta | desactivación | estado |
          const prevista = primerNumero(celdas[4] ?? "");
          const estado = normalizar(celdas[5] ?? "");
          if (estado.includes("activa") && prevista !== undefined && maxCap > 0 && prevista <= maxCap) {
            pistasSinDesactivar.push({ id: id!, que: que!, prevista, estado: celdas[5] ?? "" });
          }
        }
      }
    }

    // --- Preguntas dramáticas mayores ---
    let mayoresTotal = 0;
    let mayoresAbiertas = 0;
    const pPreg = this.proyecto.ruta("memoria", "preguntas-abiertas.md");
    if (existe(pPreg)) {
      let enMayores = false;
      for (const linea of leer(pPreg).split("\n")) {
        const t = linea.trim();
        if (t.startsWith("## ")) {
          enMayores = normalizar(t).includes("mayores");
          continue;
        }
        if (!enMayores || !t.startsWith("- ") || t.startsWith("- _") || t.startsWith("- [")) continue;
        mayoresTotal++;
        const estado = normalizar(t.split("—").pop() ?? "");
        if (estado.includes("abierta") && !estado.includes("cerrada")) mayoresAbiertas++;
      }
    }
    const tensionCero = mayoresTotal > 0 && mayoresAbiertas === 0 && pendientes > 0;

    // --- Longitud de capítulos vs mediana ---
    const pct = this.cfg.desvio_longitud_pct ?? 30;
    const capsDesviados: CapDesviado[] = [];
    let mediana = 0;
    if (caps.length >= 3) {
      const longs = caps.map((c) => c.numPalabras()).sort((a, b) => a - b);
      mediana = longs[Math.floor(longs.length / 2)]!;
      if (mediana > 0) {
        for (const c of caps) {
          const n = c.numPalabras();
          const desvio = (Math.abs(n - mediana) * 100) / mediana;
          if (desvio > pct) {
            capsDesviados.push({ cap: basename(c.path).replace(/\.md$/, ""), palabras: n, pct: Math.round(desvio) });
          }
        }
      }
    }

    // --- Presupuesto de palabras (nivel y proyección; solo si metadatos lo declara) ---
    const presupuesto: PresupuestoInfo = {
      escritas: caps.reduce((a, c) => a + c.numPalabras(), 0),
      capsSobre: [],
    };
    try {
      const md = this.proyecto.metadatos() as Record<string, any>;
      const plan: any[] = md.capitulos ?? [];
      const objetivoTotal = typeof md.palabras_objetivo === "number" && md.palabras_objetivo > 0 ? md.palabras_objetivo : undefined;
      if (objetivoTotal) {
        presupuesto.objetivoTotal = objetivoTotal;
        const tolCap = this.cfg.tolerancia_capitulo_pct ?? 15;
        const porCap = new Map<number, number>();
        for (const e of plan) if (typeof e.palabras === "number" && e.palabras > 0) porCap.set(e.n, e.palabras);
        const porDefecto = plan.length > 0 ? objetivoTotal / plan.length : 0;
        for (const c of caps) {
          const obj = porCap.get(c.numero ?? -1) ?? porDefecto;
          if (obj <= 0) continue;
          const pctSobre = ((c.numPalabras() - obj) * 100) / obj;
          if (pctSobre > tolCap) {
            presupuesto.capsSobre.push({ cap: basename(c.path).replace(/\.md$/, ""), palabras: c.numPalabras(), objetivo: Math.round(obj), pct: Math.round(pctSobre) });
          }
        }
        if (caps.length > 0 && plan.length > 0) {
          presupuesto.proyeccion = Math.round((presupuesto.escritas / caps.length) * plan.length);
          presupuesto.desvioProyeccionPct = Math.round(((presupuesto.proyeccion - objetivoTotal) * 100) / objetivoTotal);
        }
      }
    } catch {
      /* sin metadatos aún */
    }
    const tolProyFinal = this.cfg.tolerancia_proyeccion_pct ?? 10;
    const proyeccionFuera = presupuesto.desvioProyeccionPct !== undefined && Math.abs(presupuesto.desvioProyeccionPct) > tolProyFinal;

    const senales =
      presagiosVencidos.length +
      presagiosHuerfanos.length +
      pistasSinDesactivar.length +
      (tensionCero ? 1 : 0) +
      capsDesviados.length +
      presupuesto.capsSobre.length +
      (proyeccionFuera ? 1 : 0);

    return {
      presagiosVencidos,
      presagiosHuerfanos,
      pistasSinDesactivar,
      preguntasMayoresAbiertas: mayoresAbiertas,
      preguntasMayoresTotal: mayoresTotal,
      tensionCero,
      medianaPalabras: mediana,
      capsDesviados,
      presupuesto,
      senales,
    };
  }
}
