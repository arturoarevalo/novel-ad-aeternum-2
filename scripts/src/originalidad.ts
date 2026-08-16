import { AnalizadorOriginalidad } from "./lib/AnalizadorOriginalidad";
import { Proyecto, raizProyecto } from "./lib/Proyecto";
import { existe, leer, c } from "./lib/util";
import { join } from "node:path";
import { mkdirSync, writeFileSync } from "node:fs";

export function run(_args: string[]): number {
  const proyecto = new Proyecto();
  const cfgPath = join(raizProyecto(), "lint-prosa.config.json");
  const cfg = existe(cfgPath) ? (JSON.parse(leer(cfgPath)) as Record<string, any>) : {};
  const inf = new AnalizadorOriginalidad(proyecto, cfg.originalidad ?? {}).analizar();

  const criticos = inf.candidatos.filter((x) => x.prioridad === "CRITICO");
  const altas = inf.candidatos.filter((x) => x.prioridad === "ALTA");
  const medias = inf.candidatos.filter((x) => x.prioridad === "MEDIA");

  const fmt = (l: typeof inf.candidatos) =>
    l.map((x, i) => `${i + 1}. [${x.cap} L${x.linea} · ${x.tipo}]\n   "${x.texto}"`).join("\n");

  const hoy = new Date().toISOString().slice(0, 10);
  const salida = `# Candidatos de verificación de originalidad (${hoy})

Generado por \`npm run originalidad\` (determinista; NO busca en la web). Verificación: skill **/originalidad**
(agente verificador con búsqueda web) o a mano: busca cada frase EXACTA entre comillas en un buscador.
Una frase original de 8-12 palabras casi nunca devuelve coincidencias; si las devuelve, revisa.

## CRÍTICO — versos, epígrafes y citas atribuidas (verificar TODOS)
${criticos.length ? fmt(criticos) : "_(ninguno)_"}

## ALTA — aperturas, cierres y aforismos (verificar todos)
${fmt(altas)}

## MEDIA — n-gramas distintivos (muestreo por rareza léxica)
${fmt(medias)}

## Términos y nombres a comprobar (colisión con ficción existente)
${inf.terminos.length ? inf.terminos.map((t) => `- ${t}`).join("\n") : "_(memoria/nombres.md vacío)_"}
`;

  const dir = join(raizProyecto(), "informe");
  mkdirSync(dir, { recursive: true });
  const destino = join(dir, "originalidad-candidatos.md");
  writeFileSync(destino, salida, "utf8");

  console.log(`${c.verde("✔")} ${destino}`);
  console.log(`  CRÍTICO: ${criticos.length} · ALTA: ${altas.length} · MEDIA: ${medias.length} · términos: ${inf.terminos.length}`);
  if (criticos.length > 0) {
    console.log(c.amarillo(`  ${criticos.length} candidato(s) CRÍTICOS (versos/citas): verificación obligada antes de publicar.`));
  }
  return 0;
}
