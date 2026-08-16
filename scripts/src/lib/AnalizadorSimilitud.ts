import { basename } from "node:path";
import { normalizar, palabras } from "./util";
import { Capitulo } from "./Proyecto";

const STOP = new Set(
  "el la los las un una unos unas de del a en y e o u que se su sus me te le les lo nos con por para mas más pero como cuando donde si no ni ya muy era fue es habia había han ha al lo".split(
    /\s+/
  )
);

export interface InformeSimilitud {
  aperturasRepetidas: { inicio: string; capitulos: string[] }[];
  ngramasCompartidos: { ngrama: string; capitulos: string[] }[];
  motivosSobreusados: { motivo: string; total: number; capitulos: string[] }[];
}

export class AnalizadorSimilitud {
  constructor(private cfg: Record<string, any> = {}) {}

  analizar(caps: Capitulo[]): InformeSimilitud {
    const nombre = (c: Capitulo) => basename(c.path).replace(/\.md$/, "");

    // 1) Aperturas repetidas (primeras 4 palabras normalizadas)
    const aperturas = new Map<string, string[]>();
    for (const c of caps) {
      const fs = c.frases();
      if (fs.length === 0) continue;
      const inicio = palabras(normalizar(fs[0]!.texto)).slice(0, 4).join(" ");
      if (!inicio) continue;
      const arr = aperturas.get(inicio) ?? [];
      arr.push(nombre(c));
      aperturas.set(inicio, arr);
    }
    const aperturasRepetidas = [...aperturas.entries()]
      .filter(([, cs]) => cs.length >= 2)
      .map(([inicio, capitulos]) => ({ inicio, capitulos }));

    // 2) 4-gramas compartidos entre capítulos
    const minN = this.cfg.ngrama_n ?? 4;
    const grams = new Map<string, Set<string>>();
    for (const c of caps) {
      const toks = palabras(normalizar(c.prosa()));
      const vistos = new Set<string>();
      for (let i = 0; i + minN <= toks.length; i++) {
        const ventana = toks.slice(i, i + minN);
        if (ventana.every((t) => STOP.has(t))) continue; // descarta gramos solo funcionales
        const key = ventana.join(" ");
        if (vistos.has(key)) continue;
        vistos.add(key);
        const set = grams.get(key) ?? new Set<string>();
        set.add(nombre(c));
        grams.set(key, set);
      }
    }
    const ngramasCompartidos = [...grams.entries()]
      .filter(([, cs]) => cs.size >= 2)
      .map(([ngrama, cs]) => ({ ngrama, capitulos: [...cs].sort() }))
      .sort((a, b) => b.capitulos.length - a.capitulos.length)
      .slice(0, this.cfg.max_ngramas ?? 40);

    // 3) Motivos sobreusados (léxico configurable)
    const motivos: string[] = this.cfg.motivos_vigilados ?? [];
    const motivosSobreusados: { motivo: string; total: number; capitulos: string[] }[] = [];
    for (const m of motivos) {
      const re = new RegExp(`\\b${normalizar(m).replace(/\s+/g, "\\s+")}\\b`, "g");
      let total = 0;
      const cs: string[] = [];
      for (const c of caps) {
        const n = (normalizar(c.prosa()).match(re) ?? []).length;
        if (n > 0) {
          total += n;
          cs.push(`${nombre(c)}×${n}`);
        }
      }
      const lim = this.cfg.motivo_max_total ?? 5;
      if (total > lim) motivosSobreusados.push({ motivo: m, total, capitulos: cs });
    }

    return { aperturasRepetidas, ngramasCompartidos, motivosSobreusados };
  }
}
