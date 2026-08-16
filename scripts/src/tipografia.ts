import { AnalizadorTipografia } from "./lib/AnalizadorTipografia";
import { Proyecto } from "./lib/Proyecto";
import { c } from "./lib/util";

export function run(args: string[]): number {
  const fix = args.includes("--fix");
  const estricto = args.includes("--estricto");
  const ficheros = args.filter((a) => !a.startsWith("--"));
  const objetivo = ficheros.length ? ficheros : new Proyecto().ficherosCapitulo();

  if (objetivo.length === 0) {
    console.log(c.gris("tipografia: no hay capítulos que revisar."));
    return 0;
  }

  const informes = new AnalizadorTipografia().analizarVarios(objetivo, fix);
  let totalFixes = 0;
  let totalAvisos = 0;

  for (const inf of informes) {
    if (inf.fixes.length === 0 && inf.avisos.length === 0) continue;
    console.log(`\n${inf.fichero}`);
    const porTipo = new Map<string, number>();
    for (const f of inf.fixes) porTipo.set(`${f.tipo}: ${f.detalle}`, (porTipo.get(`${f.tipo}: ${f.detalle}`) ?? 0) + 1);
    for (const [k, n] of porTipo) {
      console.log(`  ${inf.aplicado ? c.verde("✔ corregido") : c.amarillo("✎ corregible")} ${k}${n > 1 ? c.gris(` ×${n}`) : ""}`);
    }
    for (const a of inf.avisos) {
      console.log(`  ${c.amarillo("aviso")} L${a.linea} [${a.tipo}] ${a.detalle}`);
    }
    totalFixes += inf.fixes.length;
    totalAvisos += inf.avisos.length;
  }

  if (totalFixes === 0 && totalAvisos === 0) {
    console.log(c.verde("✔ tipografía: sin problemas."));
  } else if (!fix && totalFixes > 0) {
    console.log(`\n${totalFixes} corrección(es) automática(s) disponibles → ${c.negrita("npm run tipografia -- --fix")} · ${totalAvisos} aviso(s) manual(es)`);
  } else {
    console.log(`\n${fix ? `${totalFixes} corrección(es) aplicadas` : ""} · ${totalAvisos} aviso(s) que requieren juicio`);
  }
  return estricto && (totalAvisos > 0 || (!fix && totalFixes > 0)) ? 1 : 0;
}
