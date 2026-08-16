import { writeFileSync, mkdirSync } from "node:fs";
import { Proyecto, Capitulo } from "./lib/Proyecto";
import { existe, contarPalabras, c } from "./lib/util";

export function run(_args: string[]): number {
  const proyecto = new Proyecto();
  const meta = proyecto.metadatos();
  const ordenados = [...meta.capitulos].sort((a, b) => a.n - b.n);

  const partes: string[] = [];
  partes.push(`# ${meta.titulo}`);
  if (meta.subtitulo) partes.push(`\n### ${meta.subtitulo}`);
  partes.push(`\n_${meta.autor}_\n`);
  if (meta.sinopsis_corta) partes.push(`\n> ${meta.sinopsis_corta}\n`);
  partes.push("\n---\n");

  let totalPalabras = 0;
  let escritos = 0;
  const faltan: number[] = [];

  for (const cm of ordenados) {
    const p = proyecto.ruta("capitulos", cm.archivo);
    if (!existe(p)) {
      faltan.push(cm.n);
      continue;
    }
    const cap = new Capitulo(p);
    const titulo = cap.titulo || cm.titulo || `Capítulo ${cm.n}`;
    // quita un posible H1 inicial del cuerpo para no duplicar título
    const cuerpo = cap.cuerpo.replace(/^\s*#\s+.*\n/, "").trim();
    partes.push(`\n## ${cm.n}. ${titulo}\n`);
    partes.push(cuerpo);
    partes.push("\n");
    totalPalabras += contarPalabras(cap.prosa());
    escritos++;
  }

  mkdirSync(proyecto.ruta("builds"), { recursive: true });
  const salida = proyecto.ruta("builds", `${meta.slug}.md`);
  writeFileSync(salida, partes.join("\n"), "utf8");

  console.log(c.verde(`✔ build: ${salida}`));
  console.log(`  capítulos: ${escritos}/${ordenados.length}` + (faltan.length ? c.amarillo(`  (faltan: ${faltan.join(", ")})`) : ""));
  console.log(`  palabras:  ${totalPalabras.toLocaleString("es-ES")}`);
  return 0;
}
