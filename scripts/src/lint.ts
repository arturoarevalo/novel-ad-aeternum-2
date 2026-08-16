import { LinterProsa } from "./lib/LinterProsa";
import { Proyecto } from "./lib/Proyecto";
import { join } from "node:path";
import { raizProyecto } from "./lib/Proyecto";
import { c } from "./lib/util";
import type { Hallazgo } from "./lib/tipos";

function pintar(h: Hallazgo): void {
  const etiqueta =
    h.severidad === "error" ? c.rojo("ERROR") : h.severidad === "aviso" ? c.amarillo("aviso") : c.gris("info");
  console.log(`  ${etiqueta} ${c.gris(`L${h.linea}`)} [${h.regla}] ${h.mensaje}`);
  if (h.fragmento) console.log(`        ${c.gris("» " + h.fragmento)}`);
}

export function run(args: string[]): number {
  const raiz = raizProyecto();
  const linter = new LinterProsa(join(raiz, "lint-prosa.config.json"));
  const estricto = args.includes("--estricto");
  const proyecto = new Proyecto();

  const objetivos = args.filter((a) => !a.startsWith("--"));
  const ficheros =
    args.includes("--todos") || objetivos.length === 0
      ? proyecto.ficherosCapitulo()
      : objetivos.map((o) => (o.startsWith("/") ? o : join(raiz, o)));

  if (ficheros.length === 0) {
    console.log(c.gris("lint: no hay capítulos que analizar todavía."));
    return 0;
  }

  let errores = 0;
  let avisos = 0;
  for (const f of ficheros) {
    const inf = linter.analizarFichero(f, true);
    errores += inf.errores;
    avisos += inf.avisos;
    const rel = f.replace(raiz + "/", "");
    if (inf.hallazgos.length === 0) {
      console.log(c.verde(`✔ ${rel}`));
    } else {
      console.log(c.negrita(rel) + c.gris(`  (${inf.errores} errores, ${inf.avisos} avisos)`));
      for (const h of inf.hallazgos) pintar(h);
    }
  }

  const novela = linter.limitesNovela(ficheros);
  for (const h of novela) {
    errores += 1;
    pintar(h);
  }

  console.log(
    "\n" +
      (errores > 0 ? c.rojo(`${errores} errores`) : c.verde("0 errores")) +
      c.gris(` · ${avisos} avisos · ${ficheros.length} fichero(s)`)
  );
  return estricto && errores > 0 ? 1 : 0;
}
