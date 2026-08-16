import { AnalizadorHilos } from "./lib/AnalizadorHilos";
import { Proyecto, raizProyecto } from "./lib/Proyecto";
import { existe, leer, c } from "./lib/util";
import { join } from "node:path";

export function run(args: string[]): number {
  const proyecto = new Proyecto();
  const cfgPath = join(raizProyecto(), "lint-prosa.config.json");
  const cfg = existe(cfgPath) ? (JSON.parse(leer(cfgPath)) as Record<string, any>) : {};
  const inf = new AnalizadorHilos(proyecto, cfg.hilos ?? {}).analizar();

  let problemas = 0;

  if (inf.presagiosVencidos.length) {
    console.log(c.amarillo("⚠ Presagios vencidos (la recogida prevista ya pasó y siguen sin pagar):"));
    for (const p of inf.presagiosVencidos) {
      problemas++;
      console.log(`  ${p.id} — ${p.que}  ${c.gris(`(prevista cap. ${p.prevista}, estado: ${p.estado})`)}`);
    }
  }
  if (inf.presagiosHuerfanos.length) {
    console.log(c.amarillo("⚠ Presagios marcados huérfanos (sembrados sin recogida):"));
    for (const p of inf.presagiosHuerfanos) {
      problemas++;
      console.log(`  ${p.id} — ${p.que}`);
    }
  }
  if (inf.pistasSinDesactivar.length) {
    console.log(c.amarillo("⚠ Pistas falsas sin desactivar (el engaño debía deshacerse ya):"));
    for (const p of inf.pistasSinDesactivar) {
      problemas++;
      console.log(`  ${p.id} — ${p.que}  ${c.gris(`(desactivación prevista cap. ${p.prevista})`)}`);
    }
  }
  if (inf.tensionCero) {
    problemas++;
    console.log(c.amarillo("⚠ Tensión a cero:") + ` no queda ninguna pregunta dramática mayor abierta y aún faltan capítulos. Abre una nueva o reactiva una (memoria/preguntas-abiertas.md).`);
  }
  if (inf.capsDesviados.length) {
    console.log(c.amarillo(`⚠ Longitud desviada de la mediana (${inf.medianaPalabras} palabras):`));
    for (const d of inf.capsDesviados) {
      problemas++;
      console.log(`  ${d.cap}: ${d.palabras} palabras (${d.pct}% de desvío). ¿Capítulo desinflado o hipertrofiado?`);
    }
  }

  const p = inf.presupuesto;
  if (p.objetivoTotal) {
    if (p.capsSobre.length) {
      console.log(c.amarillo("⚠ Capítulos por encima de su presupuesto:"));
      for (const s of p.capsSobre) {
        problemas++;
        console.log(`  ${s.cap}: ${s.palabras} palabras (objetivo ${s.objetivo}, +${s.pct}%). Editor en modo poda.`);
      }
    }
    if (p.proyeccion !== undefined && p.desvioProyeccionPct !== undefined) {
      const fuera = Math.abs(p.desvioProyeccionPct) > 10;
      const msg = `Presupuesto: ${p.escritas} palabras escritas · objetivo ${p.objetivoTotal} · proyección final ${p.proyeccion} (${p.desvioProyeccionPct >= 0 ? "+" : ""}${p.desvioProyeccionPct}%)`;
      if (fuera && p.desvioProyeccionPct > 0) {
        problemas++;
        console.log(c.amarillo("⚠ " + msg) + " → baja el objetivo de los próximos briefs o recorta beats del outline.");
      } else if (fuera) {
        problemas++;
        console.log(c.amarillo("⚠ " + msg));
      } else {
        console.log(c.gris("  " + msg));
      }
    }
  }

  if (problemas === 0) {
    const detalle =
      inf.preguntasMayoresTotal > 0
        ? ` (${inf.preguntasMayoresAbiertas}/${inf.preguntasMayoresTotal} preguntas mayores abiertas)`
        : "";
    console.log(c.verde("✔ hilos: presagios al día, tensión viva y longitudes en rango." + detalle));
  }
  return args.includes("--estricto") && problemas > 0 ? 1 : 0;
}
