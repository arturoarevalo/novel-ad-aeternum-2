import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { leer, existe, listarFicheros, parseFrontMatter, soloProsa, dividirFrases, contarPalabras } from "./util";
import type { Frase } from "./util";
import type { Metadatos, FrontMatter } from "./tipos";

/** Raíz del repositorio (dos niveles por encima de scripts/src/lib). */
export function raizProyecto(): string {
  const aqui = dirname(fileURLToPath(import.meta.url));
  return resolve(aqui, "..", "..", "..");
}

export class Capitulo {
  readonly path: string;
  readonly fm: FrontMatter;
  readonly cuerpo: string;
  private readonly lineaCuerpo: number;

  constructor(path: string) {
    this.path = path;
    const doc = parseFrontMatter(leer(path));
    this.fm = doc.fm;
    this.cuerpo = doc.cuerpo;
    this.lineaCuerpo = doc.lineaCuerpo;
  }

  get numero(): number | undefined {
    const n = this.fm["capitulo"] ?? this.fm["n"];
    return typeof n === "number" ? n : undefined;
  }

  get titulo(): string {
    return String(this.fm["titulo"] ?? "");
  }

  get pov(): string {
    return String(this.fm["pov"] ?? "");
  }

  get fecha(): string {
    return String(this.fm["fecha"] ?? "");
  }

  get estado(): string {
    return String(this.fm["estado"] ?? "");
  }

  get esAnalepsis(): boolean {
    return this.fm["analepsis"] === true;
  }

  /** Texto de prosa limpio (sin marcas markdown). */
  prosa(): string {
    return soloProsa(this.cuerpo);
  }

  frases(): Frase[] {
    return dividirFrases(this.prosa(), this.lineaCuerpo - 1);
  }

  numPalabras(): number {
    return contarPalabras(this.prosa());
  }
}

export class Proyecto {
  readonly raiz: string;

  constructor(raiz = raizProyecto()) {
    this.raiz = raiz;
  }

  ruta(...partes: string[]): string {
    return join(this.raiz, ...partes);
  }

  metadatos(): Metadatos {
    const p = this.ruta("biblia", "metadatos.json");
    if (!existe(p)) {
      throw new Error(`No existe ${p}. Ejecuta /arquitecto para generar la biblia.`);
    }
    return JSON.parse(leer(p)) as Metadatos;
  }

  /** Ficheros de capítulo presentes en disco (orden alfabético = orden de fichero). */
  ficherosCapitulo(): string[] {
    return listarFicheros(this.ruta("capitulos"), ".md").filter(
      (f) => !f.endsWith("README.md")
    );
  }

  capitulos(): Capitulo[] {
    return this.ficherosCapitulo().map((f) => new Capitulo(f));
  }

  /** Capítulos pendientes según metadatos: sin fichero o en estado borrador. */
  capitulosPendientes(): { n: number; archivo: string; motivo: string }[] {
    const meta = this.metadatos();
    const pendientes: { n: number; archivo: string; motivo: string }[] = [];
    for (const cap of meta.capitulos.sort((a, b) => a.n - b.n)) {
      const p = this.ruta("capitulos", cap.archivo);
      if (!existe(p)) {
        pendientes.push({ n: cap.n, archivo: cap.archivo, motivo: "sin fichero" });
        continue;
      }
      const c = new Capitulo(p);
      if (c.estado === "borrador" || c.estado === "pendiente") {
        pendientes.push({ n: cap.n, archivo: cap.archivo, motivo: `estado=${c.estado}` });
      }
    }
    return pendientes;
  }
}
