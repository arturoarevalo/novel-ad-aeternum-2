import { spawnSync } from "node:child_process";
import { writeFileSync, readFileSync } from "node:fs";
import { Proyecto, raizProyecto } from "./lib/Proyecto";
import { existe, c } from "./lib/util";
import { join } from "node:path";
import { run as salud } from "./salud";

interface EstadoRunner {
  completados: number[];
  ultimoIntento: number | null;
  ts: string;
}

const ESTADO_PATH = () => join(raizProyecto(), ".runner-state.json");

function leerEstado(): EstadoRunner {
  const p = ESTADO_PATH();
  if (existe(p)) return JSON.parse(readFileSync(p, "utf8")) as EstadoRunner;
  return { completados: [], ultimoIntento: null, ts: new Date().toISOString() };
}

function guardarEstado(e: EstadoRunner): void {
  e.ts = new Date().toISOString();
  writeFileSync(ESTADO_PATH(), JSON.stringify(e, null, 2), "utf8");
}

export function run(args: string[]): number {
  const proyecto = new Proyecto();
  const dryRun = args.includes("--dry-run");
  const desde = numArg(args, "--desde");
  const hasta = numArg(args, "--hasta");
  const modelo = strArg(args, "--modelo") ?? "opus";

  const pendientes = proyecto
    .capitulosPendientes()
    .filter((p) => (desde == null || p.n >= desde) && (hasta == null || p.n <= hasta));

  if (pendientes.length === 0) {
    console.log(c.verde("runner: no hay capítulos pendientes. 🎉"));
    return 0;
  }

  console.log(c.negrita(`runner: ${pendientes.length} capítulo(s) pendiente(s): ${pendientes.map((p) => p.n).join(", ")}`));
  console.log(
    c.gris(
      "Cada capítulo se escribe con contexto fresco (mejor calidad). Exporta CLAUDE_CACHE_TTL=1h y ejecuta los capítulos seguidos para reaprovechar la caché del prefijo estable.\n"
    )
  );

  const estado = leerEstado();

  for (const cap of pendientes) {
    estado.ultimoIntento = cap.n;
    guardarEstado(estado);

    const prompt = `/capitulo ${cap.n}`;
    const cmd = "claude";
    const cmdArgs = [
      "-p",
      prompt,
      "--permission-mode",
      "bypassPermissions",
      "--model",
      modelo,
    ];

    console.log(c.azul(`\n▶ Capítulo ${cap.n}  (${cap.motivo})`));
    console.log(c.gris(`  $ ${cmd} ${cmdArgs.map((a) => (a.includes(" ") ? `"${a}"` : a)).join(" ")}`));

    if (dryRun) {
      console.log(c.gris("  [dry-run] no se ejecuta."));
      continue;
    }

    const res = spawnSync(cmd, cmdArgs, { stdio: "inherit", env: { ...process.env, CLAUDE_CACHE_TTL: process.env.CLAUDE_CACHE_TTL ?? "1h" } });
    if (res.status !== 0) {
      console.error(c.rojo(`\n✗ El capítulo ${cap.n} terminó con código ${res.status}. Me detengo para que revises.`));
      return 1;
    }

    // Puerta de calidad (Definition of Done)
    console.log(c.gris("\n  Verificando Definition of Done…"));
    const codigoSalud = salud([]);
    if (codigoSalud !== 0) {
      console.error(c.rojo(`\n✗ El capítulo ${cap.n} no pasa la Definition of Done. Me detengo (no sigo construyendo sobre algo roto).`));
      return 1;
    }

    estado.completados.push(cap.n);
    guardarEstado(estado);
    console.log(c.verde(`✔ Capítulo ${cap.n} completado y verificado.`));
  }

  console.log(c.verde(c.negrita("\n✔ runner: novela completada (o tramo solicitado).")));
  return 0;
}

function numArg(args: string[], flag: string): number | null {
  const i = args.indexOf(flag);
  if (i === -1 || i + 1 >= args.length) return null;
  const v = Number(args[i + 1]);
  return Number.isNaN(v) ? null : v;
}
function strArg(args: string[], flag: string): string | null {
  const i = args.indexOf(flag);
  if (i === -1 || i + 1 >= args.length) return null;
  return args[i + 1] ?? null;
}
