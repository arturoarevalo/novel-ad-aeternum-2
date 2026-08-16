import { join } from "node:path";
import { Proyecto, raizProyecto } from "./lib/Proyecto";
import { LinterProsa } from "./lib/LinterProsa";
import { GrafoCoherencia } from "./lib/GrafoCoherencia";
import { AnalizadorSimilitud } from "./lib/AnalizadorSimilitud";
import { AnalizadorRepeticiones } from "./lib/AnalizadorRepeticiones";
import { AnalizadorHilos } from "./lib/AnalizadorHilos";
import { AnalizadorTipografia } from "./lib/AnalizadorTipografia";
import { Cronologia } from "./lib/Cronologia";
import { existe, leer, c } from "./lib/util";

export function run(args: string[]): number {
  const raiz = raizProyecto();
  const proyecto = new Proyecto();
  const estricto = args.includes("--estricto");
  const ficheros = proyecto.ficherosCapitulo();

  console.log(c.negrita("\n— Salud de la novela —\n"));

  // 1) Lint de prosa
  const linter = new LinterProsa(join(raiz, "lint-prosa.config.json"));
  let erroresLint = 0;
  let avisosLint = 0;
  for (const f of ficheros) {
    const inf = linter.analizarFichero(f, true);
    erroresLint += inf.errores;
    avisosLint += inf.avisos;
  }
  erroresLint += linter.limitesNovela(ficheros).length;
  línea("Prosa (AI-ismos)", erroresLint === 0, `${erroresLint} errores, ${avisosLint} avisos`, erroresLint > 0);

  // 2) Coherencia
  let stale = 0;
  try {
    const grafo = new GrafoCoherencia(raiz, join(raiz, "coherencia.config.json"));
    grafo.scan();
    stale = grafo.obsoletos().length;
  } catch {
    /* sin config todavía */
  }
  línea("Coherencia (obsoletos)", stale === 0, `${stale} documento(s)`, false, stale > 0);

  // 3) Cronología
  let erroresCron = 0;
  try {
    erroresCron = new Cronologia(proyecto).validar().filter((p) => p.severidad === "error").length;
  } catch {
    /* sin metadatos */
  }
  línea("Cronología", erroresCron === 0, `${erroresCron} conflicto(s)`, erroresCron > 0);

  // 4) Auto-similitud
  let reincidencias = 0;
  if (ficheros.length >= 2) {
    const cfgPath = join(raiz, "lint-prosa.config.json");
    const cfg = existe(cfgPath) ? (JSON.parse(leer(cfgPath)) as Record<string, any>) : {};
    const s = new AnalizadorSimilitud(cfg.similitud ?? {}).analizar(proyecto.capitulos());
    reincidencias = s.aperturasRepetidas.length + s.ngramasCompartidos.length + s.motivosSobreusados.length;
  }
  línea("Auto-similitud", reincidencias === 0, `${reincidencias} señal(es)`, false, reincidencias > 0);

  // 5) Repeticiones semánticas por personaje (rasgos/tics/sensaciones)
  let repeticiones = 0;
  if (ficheros.length >= 1) {
    const cfgPath = join(raiz, "lint-prosa.config.json");
    const cfg = existe(cfgPath) ? (JSON.parse(leer(cfgPath)) as Record<string, any>) : {};
    const registro = AnalizadorRepeticiones.leerRegistro(join(raiz, "memoria", "rasgos.md"));
    const r = new AnalizadorRepeticiones(cfg.repeticiones ?? {}).analizar(proyecto.capitulos(), registro);
    repeticiones = r.avisos.length;
  }
  línea("Repeticiones (rasgos)", repeticiones === 0, `${repeticiones} señal(es)`, false, repeticiones > 0);

  // 6) Hilos narrativos (presagios/tensión) y 7) forma (longitud de capítulos)
  let hilosNarrativos = 0;
  let longitudDesviada = 0;
  let presupuestoSenales = 0;
  let presupuestoDetalle = "sin objetivo declarado";
  try {
    const cfgPath = join(raiz, "lint-prosa.config.json");
    const cfg = existe(cfgPath) ? (JSON.parse(leer(cfgPath)) as Record<string, any>) : {};
    const hInf = new AnalizadorHilos(proyecto, cfg.hilos ?? {}).analizar();
    hilosNarrativos =
      hInf.presagiosVencidos.length +
      hInf.presagiosHuerfanos.length +
      hInf.pistasSinDesactivar.length +
      (hInf.tensionCero ? 1 : 0);
    longitudDesviada = hInf.capsDesviados.length;
    const pInf = hInf.presupuesto;
    if (pInf.objetivoTotal && pInf.proyeccion !== undefined && pInf.desvioProyeccionPct !== undefined) {
      const fuera = Math.abs(pInf.desvioProyeccionPct) > (cfg.hilos?.tolerancia_proyeccion_pct ?? 10);
      presupuestoSenales = pInf.capsSobre.length + (fuera ? 1 : 0);
      presupuestoDetalle = `proy. ${pInf.proyeccion}/${pInf.objetivoTotal} (${pInf.desvioProyeccionPct >= 0 ? "+" : ""}${pInf.desvioProyeccionPct}%), ${pInf.capsSobre.length} cap(s) pasados`;
    }
  } catch {
    /* sin biblia todavía */
  }
  línea("Hilos (presagios/tensión)", hilosNarrativos === 0, `${hilosNarrativos} señal(es)`, false, hilosNarrativos > 0);
  línea("Longitud de capítulos", longitudDesviada === 0, `${longitudDesviada} desviado(s)`, false, longitudDesviada > 0);

  // 8) Ortotipografía
  let tipo = 0;
  try {
    const tInf = new AnalizadorTipografia().analizarVarios(proyecto.ficherosCapitulo(), false);
    tipo = tInf.reduce((a, x) => a + x.fixes.length + x.avisos.length, 0);
  } catch {
    /* sin capítulos */
  }
  línea("Tipografía", tipo === 0, `${tipo} problema(s)`, false, tipo > 0);
  línea("Presupuesto (palabras)", presupuestoSenales === 0, presupuestoDetalle, false, presupuestoSenales > 0);

  // Veredicto
  const bloqueante =
    erroresLint > 0 ||
    erroresCron > 0 ||
    (estricto && (stale > 0 || reincidencias > 0 || repeticiones > 0 || hilosNarrativos > 0 || longitudDesviada > 0 || tipo > 0 || presupuestoSenales > 0));
  console.log("");
  if (bloqueante) {
    console.log(c.rojo(c.negrita("✗ FALLA la Definition of Done.")) + c.gris("  Revisa lo marcado antes de continuar."));
    return 1;
  }
  console.log(c.verde(c.negrita("✔ PASA la Definition of Done.")));
  return 0;
}

function línea(nombre: string, ok: boolean, detalle: string, esError: boolean, esAviso = false): void {
  const marca = ok ? c.verde("✔") : esError ? c.rojo("✗") : c.amarillo("⚠");
  const det = ok ? c.gris(detalle) : esError ? c.rojo(detalle) : c.amarillo(detalle);
  console.log(`  ${marca} ${nombre.padEnd(26)} ${det}`);
  void esAviso;
}
