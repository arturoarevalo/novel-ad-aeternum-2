import { leer, existe, parseFrontMatter } from "./util";
import { writeFileSync } from "node:fs";

/**
 * Ortotipografía española de imprenta (determinista, 0 tokens).
 *
 * FIXES automáticos (inequívocos): puntos suspensivos "..." → "…"; "--" → "—";
 * comillas inglesas “ ” → « »; comillas rectas "…" por pares → « »; guion o
 * semirraya a inicio de línea (diálogo) → raya —; espacio tras la raya de
 * diálogo; espacios antes de , ; : . ! ? »; espacio tras « ; falta de espacio
 * tras , ; : ! ? (si no son dígitos: respeta 3,14 y 21:30); dobles espacios.
 *
 * AVISOS (requieren juicio): ¿? o ¡! sin signo de apertura en el segmento;
 * comillas rectas impares en una línea; inciso con guion corto " - " en vez
 * de raya. El front-matter y los separadores de escena no se tocan.
 */

export interface HallazgoTipo {
  tipo: string;
  linea: number;
  detalle: string;
}

export interface InformeTipografia {
  fichero: string;
  fixes: HallazgoTipo[];
  avisos: HallazgoTipo[];
  aplicado: boolean;
}

const RE_HR = /^\s*(-{3,}|\*(\s*\*)+\s*)$/; // hr markdown o separador de escena

export class AnalizadorTipografia {
  analizarFichero(path: string, aplicar: boolean): InformeTipografia {
    const doc = parseFrontMatter(leer(path));
    const lineas = doc.cuerpo.split("\n");
    const fixes: HallazgoTipo[] = [];
    const avisos: HallazgoTipo[] = [];
    const off = doc.lineaCuerpo - 1;

    const nuevas = lineas.map((original, i) => {
      const num = i + 1 + off;
      if (RE_HR.test(original) || original.trim() === "") return original;
      let l = original;
      const fx = (tipo: string, detalle: string) => fixes.push({ tipo, linea: num, detalle });

      // 1) Puntos suspensivos
      if (/\.{3,}/.test(l)) {
        fx("suspensivos", '"..." → "…"');
        l = l.replace(/\.{3,}/g, "…");
      }
      // 2) Doble guion
      if (/--+/.test(l)) {
        fx("raya", '"--" → "—"');
        l = l.replace(/--+/g, "—");
      }
      // 3) Comillas tipográficas inglesas
      if (/[“”„‟]/.test(l)) {
        fx("comillas", "“ ” → « »");
        l = l.replace(/[“‟]/g, "«").replace(/[”„]/g, "»");
      }
      // 4) Comillas rectas por pares
      const rectas = (l.match(/"/g) ?? []).length;
      if (rectas > 0) {
        if (rectas % 2 === 0) {
          let abre = true;
          l = l.replace(/"/g, () => (abre = !abre) ? "»" : "«");
          fx("comillas", '"…" → «…»');
        } else {
          avisos.push({ tipo: "comillas", linea: num, detalle: `comilla recta sin pareja (") en la línea: revisa a mano` });
        }
      }
      // 5) Diálogo: guion/semirraya inicial → raya pegada; raya con espacio → pegada
      if (/^(\s*)[-–]\s*(?=[\p{L}¿¡«"'…])/u.test(l)) {
        fx("dialogo", "guion inicial → raya — pegada");
        l = l.replace(/^(\s*)[-–]\s*/u, "$1—");
      }
      if (/^(\s*)—\s+/.test(l)) {
        fx("dialogo", "espacio tras la raya de apertura");
        l = l.replace(/^(\s*)—\s+/, "$1—");
      }
      // 6) Espacios alrededor de puntuación y comillas angulares
      if (/ +[,;:.!?»]/.test(l)) {
        fx("espacios", "espacio antes de puntuación");
        l = l.replace(/ +([,;:.!?»])/g, "$1");
      }
      if (/«\s+/.test(l)) {
        fx("espacios", "espacio tras «");
        l = l.replace(/«\s+/g, "«");
      }
      if (/([,;!?])(?=[\p{L}¿¡«])/u.test(l)) {
        fx("espacios", "falta espacio tras puntuación");
        l = l.replace(/([,;!?])(?=[\p{L}¿¡«])/gu, "$1 ");
      }
      if (/(:)(?=[\p{L}¿¡«])/u.test(l)) {
        fx("espacios", "falta espacio tras dos puntos");
        l = l.replace(/(:)(?=[\p{L}¿¡«])/gu, "$1 ");
      }
      if (/\S  +/.test(l)) {
        fx("espacios", "doble espacio");
        l = l.replace(/(\S)  +/g, "$1 ");
      }
      // 7) Avisos con juicio
      for (const seg of l.split(/(?<=[.!?…])\s+/)) {
        if (seg.includes("?") && !seg.includes("¿")) {
          avisos.push({ tipo: "apertura", linea: num, detalle: `"?" sin "¿" de apertura: «${seg.trim().slice(0, 60)}»` });
        }
        if (seg.includes("!") && !seg.includes("¡")) {
          avisos.push({ tipo: "apertura", linea: num, detalle: `"!" sin "¡" de apertura: «${seg.trim().slice(0, 60)}»` });
        }
      }
      if (/\s[-–]\s/.test(l)) {
        avisos.push({ tipo: "inciso", linea: num, detalle: "inciso con guion corto: en español, raya — pegada al inciso (—así—)" });
      }
      return l;
    });

    let aplicado = false;
    if (aplicar && fixes.length > 0) {
      const fmOriginal = leer(path).split("\n").slice(0, off).join("\n");
      const contenido = off > 0 ? fmOriginal + "\n" + nuevas.join("\n") : nuevas.join("\n");
      writeFileSync(path, contenido, "utf8");
      aplicado = true;
    }
    return { fichero: path, fixes, avisos, aplicado };
  }

  analizarVarios(paths: string[], aplicar: boolean): InformeTipografia[] {
    return paths.filter((p) => existe(p)).map((p) => this.analizarFichero(p, aplicar));
  }
}
