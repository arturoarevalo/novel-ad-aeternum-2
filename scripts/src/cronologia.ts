import { Cronologia } from "./lib/Cronologia";
import { Proyecto } from "./lib/Proyecto";
import { c } from "./lib/util";

export function run(_args: string[]): number {
  const proyecto = new Proyecto();
  const problemas = new Cronologia(proyecto).validar();
  const errores = problemas.filter((p) => p.severidad === "error");
  if (problemas.length === 0) {
    console.log(c.verde("✔ cronología: coherente."));
    return 0;
  }
  for (const p of problemas) {
    const et = p.severidad === "error" ? c.rojo("ERROR") : c.amarillo("aviso");
    console.log(`  ${et} ${c.negrita(p.capitulo)}: ${p.mensaje}`);
  }
  return errores.length > 0 ? 1 : 0;
}
