#!/usr/bin/env tsx
import { c } from "./lib/util";

type Comando = (args: string[]) => number | Promise<number>;

const comandos: Record<string, () => Promise<{ run: Comando }>> = {
  build: () => import("./build"),
  deploy: () => import("./deploy"),
  coherencia: () => import("./coherencia"),
  lint: () => import("./lint"),
  similitud: () => import("./similitud"),
  repeticiones: () => import("./repeticiones"),
  hilos: () => import("./hilos"),
  tipografia: () => import("./tipografia"),
  originalidad: () => import("./originalidad"),
  cronologia: () => import("./cronologia"),
  salud: () => import("./salud"),
  runner: () => import("./runner"),
  "build-docx": () => import("./build-docx"),
};

const ayuda = `
${c.negrita("novela")} — instrumental de la plantilla

Uso:  npm run <comando> -- [opciones]      o     tsx scripts/src/cli.ts <comando>

Comandos:
  build                 Concatena los capítulos en builds/<slug>.md
  build-docx            Genera el archivo .docx de la novela
  deploy                Genera HTML y simula la subida a previsualización
  coherencia [sub]      scan | status | impact <ruta> | graph | validate
  lint [ficheros|--todos] [--estricto]   Linter de prosa (AI-ismos, cadencia…)
  similitud             Reincidencias entre capítulos (aperturas, n-gramas, motivos)
  repeticiones [--estricto] [--huerfanos]   Tics/rasgos/sensaciones repetidos por personaje
  hilos [--estricto]    Presagios vencidos, tensión, longitud y presupuesto de palabras
  tipografia [fichero] [--fix] [--estricto]  Ortotipografía española (raya, «», …, ¿¡, espacios)
  originalidad          Extrae candidatos antiplagio a informe/originalidad-candidatos.md
  cronologia            Valida fechas del front-matter contra el orden narrativo
  salud [--estricto]    Definition of Done de toda la novela (puerta de calidad)
  runner [--dry-run] [--desde N] [--hasta N] [--modelo opus]
                        Escribe los capítulos pendientes uno a uno con /capitulo
`;

async function main(): Promise<void> {
  const [, , cmd, ...args] = process.argv;
  if (!cmd || cmd === "--help" || cmd === "-h") {
    console.log(ayuda);
    process.exit(cmd ? 0 : 1);
  }
  const cargador = comandos[cmd];
  if (!cargador) {
    console.error(c.rojo(`Comando desconocido: ${cmd}`));
    console.log(ayuda);
    process.exit(2);
  }
  const mod = await cargador();
  const codigo = await mod.run(args);
  process.exit(codigo);
}

main().catch((e) => {
  console.error(c.rojo("Error:"), e instanceof Error ? e.message : e);
  process.exit(1);
});
