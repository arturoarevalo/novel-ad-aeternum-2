import { AnalizadorRepeticiones } from "./lib/AnalizadorRepeticiones";
import { Proyecto, raizProyecto } from "./lib/Proyecto";
import { existe, leer, c } from "./lib/util";
import { join, basename } from "node:path";

export function run(args: string[]): number {
  const proyecto = new Proyecto();
  const caps = proyecto.capitulos();
  if (caps.length === 0) {
    console.log(c.gris("repeticiones: aún no hay capítulos."));
    return 0;
  }

  const cfgPath = join(raizProyecto(), "lint-prosa.config.json");
  const cfg = existe(cfgPath) ? (JSON.parse(leer(cfgPath)) as Record<string, any>) : {};
  const registroPath = join(raizProyecto(), "memoria", "rasgos.md");
  const registro = AnalizadorRepeticiones.leerRegistro(registroPath);

  const inf = new AnalizadorRepeticiones(cfg.repeticiones ?? {}).analizar(caps, registro);

  if (registro.length === 0) {
    console.log(
      c.gris(
        "registro vacío (memoria/rasgos.md): solo se buscan ecos no catalogados. El archivista rellena rasgos.md a medida que se escribe."
      )
    );
  }

  const porClase = (clase: string) => inf.avisos.filter((a) => a.clase === clase);
  let problemas = 0;

  const bloque = (titulo: string, clase: string) => {
    const avs = porClase(clase);
    if (avs.length === 0) return;
    console.log(c.amarillo(`⚠ ${titulo}:`));
    for (const a of avs) {
      problemas++;
      const donde =
        a.ejemploArchivo && a.ejemploLinea
          ? c.gris(`  (${basename(a.ejemploArchivo)}:${a.ejemploLinea})`)
          : c.gris("  → " + a.capitulos.join(", "));
      console.log(`  ${a.mensaje}${donde}`);
    }
  };

  bloque("Recurso por encima de su tope", "tope");
  bloque("Rasgo físico redescrito", "rasgo-redescrito");
  bloque("Tic en capítulos consecutivos", "consecutivos");
  bloque("Ecos corporales/sensoriales sin catalogar", "eco");

  if (inf.huerfanos.length && args.includes("--huerfanos")) {
    console.log(c.gris(`\nEntradas del registro no encontradas en el texto (${inf.huerfanos.length}):`));
    for (const hstr of inf.huerfanos) console.log(c.gris(`  · ${hstr}`));
  }

  if (problemas === 0) console.log(c.verde("✔ repeticiones: sin reincidencias de rasgos/sensaciones."));
  return args.includes("--estricto") && problemas > 0 ? 1 : 0;
}
