import { basename } from "node:path";
import { Proyecto, Capitulo } from "./Proyecto";
import { existe } from "./util";

export interface ProblemaCronologia {
  severidad: "error" | "aviso";
  capitulo: string;
  mensaje: string;
}

/**
 * Comprueba que la fecha en el front-matter de cada capítulo no retrocede
 * respecto al orden narrativo (salvo capítulos marcados analepsis: true),
 * y avisa de fechas ausentes.
 */
export class Cronologia {
  constructor(private proyecto: Proyecto) {}

  validar(): ProblemaCronologia[] {
    const problemas: ProblemaCronologia[] = [];
    const meta = this.proyecto.metadatos();
    const ordenados = [...meta.capitulos].sort((a, b) => a.n - b.n);

    let ultimaFecha: number | null = null;
    let ultimoCap = "";

    for (const cm of ordenados) {
      const p = this.proyecto.ruta("capitulos", cm.archivo);
      if (!existe(p)) continue;
      const c = new Capitulo(p);
      const nombre = basename(p).replace(/\.md$/, "");
      const fechaStr = c.fecha;

      if (!fechaStr) {
        problemas.push({ severidad: "aviso", capitulo: nombre, mensaje: "Sin campo 'fecha' en el front-matter; no se puede validar cronología." });
        continue;
      }
      const t = Date.parse(fechaStr);
      if (Number.isNaN(t)) {
        problemas.push({ severidad: "aviso", capitulo: nombre, mensaje: `Fecha no interpretable: "${fechaStr}" (usa ISO, p. ej. 1992-04-05 o 1992-04-05T21:30).` });
        continue;
      }
      if (c.esAnalepsis) {
        ultimoCap = nombre;
        continue; // los flashbacks pueden retroceder
      }
      if (ultimaFecha !== null && t < ultimaFecha) {
        problemas.push({
          severidad: "error",
          capitulo: nombre,
          mensaje: `La fecha (${fechaStr}) es anterior a la de ${ultimoCap}. Si es intencionado, marca 'analepsis: true'.`,
        });
      }
      ultimaFecha = t;
      ultimoCap = nombre;
    }

    return problemas;
  }
}
