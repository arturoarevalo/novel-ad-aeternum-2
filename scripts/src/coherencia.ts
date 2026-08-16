import { GrafoCoherencia } from "./lib/GrafoCoherencia";
import { raizProyecto } from "./lib/Proyecto";
import { join } from "node:path";
import { c } from "./lib/util";

export function run(args: string[]): number {
  const sub = args[0] ?? "status";
  const raiz = raizProyecto();
  const grafo = new GrafoCoherencia(raiz, join(raiz, "coherencia.config.json"));
  grafo.scan();

  const soloAvisos = args.includes("--warn-only");
  const json = args.includes("--json");

  switch (sub) {
    case "scan": {
      const r = grafo.resumen();
      console.log(c.gris(`grafo: ${r.nodos} nodos, ${r.aristas} aristas`));
      for (const a of grafo.avisos) console.log(c.amarillo(`  aviso: ${a}`));
      return 0;
    }
    case "graph": {
      console.log(grafo.arbol());
      return 0;
    }
    case "validate": {
      const problemas = grafo.validar();
      if (problemas.length === 0) {
        console.log(c.verde("✔ coherencia: sin problemas estructurales."));
        return 0;
      }
      for (const p of problemas) console.log(c.amarillo(`  ${p}`));
      return 0;
    }
    case "impact": {
      const objetivo = args[1];
      if (!objetivo) {
        console.error("Uso: coherencia impact <ruta-relativa>");
        return 2;
      }
      const afectados = grafo.impacto(objetivo);
      if (json) {
        console.log(JSON.stringify(afectados, null, 2));
        return 0;
      }
      console.log(c.negrita(`Afectados por cambiar ${objetivo} (${afectados.length}):`));
      for (const a of afectados) console.log(`  • ${a.id}  ${c.gris(`← ${a.relacion} (nivel ${a.nivel})`)}`);
      return 0;
    }
    case "status":
    default: {
      const obs = grafo.obsoletos();
      if (json) {
        console.log(JSON.stringify(obs.map((o) => ({ ...o.arista, deltaMin: Math.round(o.deltaMin) })), null, 2));
        return obs.length ? 1 : 0;
      }
      if (obs.length === 0) {
        if (!soloAvisos) console.log(c.verde("✔ coherencia: todo al día."));
        return 0;
      }
      console.log(c.amarillo(`⚠ ${obs.length} documento(s) posiblemente obsoleto(s):`));
      for (const o of obs) {
        const h = Math.round(o.deltaMin);
        console.log(`  ${c.amarillo(o.arista.toId)}  ${c.gris(`← ${o.arista.fromId} cambió hace ~${h} min (relación: ${o.arista.relacion})`)}`);
      }
      return 1;
    }
  }
}
