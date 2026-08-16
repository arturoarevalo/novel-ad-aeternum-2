import { AnalizadorSimilitud } from "./lib/AnalizadorSimilitud";
import { Proyecto, raizProyecto } from "./lib/Proyecto";
import { existe, leer, c } from "./lib/util";
import { join } from "node:path";

export function run(_args: string[]): number {
  const proyecto = new Proyecto();
  const caps = proyecto.capitulos();
  if (caps.length < 2) {
    console.log(c.gris("similitud: hacen falta al menos 2 capítulos."));
    return 0;
  }
  const cfgPath = join(raizProyecto(), "lint-prosa.config.json");
  const cfg = existe(cfgPath) ? (JSON.parse(leer(cfgPath)) as Record<string, any>) : {};
  const inf = new AnalizadorSimilitud(cfg.similitud ?? {}).analizar(caps);

  let problemas = 0;

  if (inf.aperturasRepetidas.length) {
    console.log(c.amarillo("⚠ Aperturas de capítulo repetidas:"));
    for (const a of inf.aperturasRepetidas) {
      problemas++;
      console.log(`  "${a.inicio}…"  ${c.gris("→ " + a.capitulos.join(", "))}`);
    }
  }
  if (inf.ngramasCompartidos.length) {
    console.log(c.amarillo(`⚠ Secuencias repetidas entre capítulos (${inf.ngramasCompartidos.length}):`));
    for (const g of inf.ngramasCompartidos.slice(0, 20)) {
      problemas++;
      console.log(`  "${g.ngrama}"  ${c.gris("→ " + g.capitulos.join(", "))}`);
    }
  }
  if (inf.motivosSobreusados.length) {
    console.log(c.amarillo("⚠ Motivos sobreusados:"));
    for (const m of inf.motivosSobreusados) {
      problemas++;
      console.log(`  "${m.motivo}" ×${m.total}  ${c.gris("→ " + m.capitulos.join(", "))}`);
    }
  }

  if (problemas === 0) console.log(c.verde("✔ similitud: sin reincidencias notables."));
  return 0;
}
