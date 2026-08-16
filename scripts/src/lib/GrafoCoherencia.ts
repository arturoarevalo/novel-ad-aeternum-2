import { join, relative, basename } from "node:path";
import { leer, existe, listarFicheros, mtime, compilarGlob } from "./util";
import type { ConfigCoherencia, Arista } from "./tipos";

interface Nodo {
  id: string;
  path: string; // relativo a la raíz
  tipo: string;
  mtime: number;
}

export class GrafoCoherencia {
  private readonly raiz: string;
  private readonly config: ConfigCoherencia;
  private nodos = new Map<string, Nodo>();
  private porPath = new Map<string, Nodo>();
  private aristas: Arista[] = [];
  private avisosScan: string[] = [];

  constructor(raiz: string, configPath: string) {
    this.raiz = raiz;
    if (!existe(configPath)) {
      throw new Error(`No existe ${configPath}`);
    }
    this.config = JSON.parse(leer(configPath)) as ConfigCoherencia;
  }

  private rel(abs: string): string {
    return relative(this.raiz, abs).split("\\").join("/");
  }

  scan(): void {
    this.nodos.clear();
    this.porPath.clear();
    this.aristas = [];
    this.avisosScan = [];

    // 1) Nodos
    for (const s of this.config.scan) {
      const dir = join(this.raiz, s.path);
      for (const abs of listarFicheros(dir, ".md")) {
        if (abs.endsWith("README.md")) continue;
        const path = this.rel(abs);
        const id = `${s.tipo}:${basename(abs).replace(/\.md$/, "")}`;
        if (this.nodos.has(id)) {
          this.avisosScan.push(`Colisión de id de nodo: ${id} (${path})`);
        }
        const nodo: Nodo = { id, path, tipo: s.tipo, mtime: mtime(abs) };
        this.nodos.set(id, nodo);
        this.porPath.set(path, nodo);
      }
    }

    // 2) Aristas a partir de reglas (from -> to)
    for (const regla of this.config.reglas) {
      const gFrom = compilarGlob(regla.from);
      const gTo = compilarGlob(regla.to);
      let emparejadas = 0;
      const fromNodos = [...this.porPath.values()].filter((n) => gFrom.re.test(n.path));
      const toNodos = [...this.porPath.values()].filter((n) => gTo.re.test(n.path));

      for (const fn of fromNodos) {
        const mFrom = fn.path.match(gFrom.re);
        for (const tn of toNodos) {
          if (fn.path === tn.path) continue; // self-loop excluido
          // Si hay capturas compartidas, deben coincidir (emparejado 1-a-1)
          if (gFrom.capturas.length > 0 && gTo.capturas.length > 0) {
            const mTo = tn.path.match(gTo.re);
            const compartidas = gFrom.capturas.filter((x) => gTo.capturas.includes(x));
            let ok = true;
            for (const cap of compartidas) {
              const iF = gFrom.capturas.indexOf(cap) + 1;
              const iT = gTo.capturas.indexOf(cap) + 1;
              if (mFrom?.[iF] !== mTo?.[iT]) ok = false;
            }
            if (!ok) continue;
          }
          this.aristas.push({
            fromId: fn.id,
            toId: tn.id,
            relacion: regla.relacion,
            fromPath: fn.path,
            toPath: tn.path,
          });
          emparejadas++;
        }
      }
      if (emparejadas === 0) {
        this.avisosScan.push(`Regla sin coincidencias: "${regla.nombre}" (${regla.from} -> ${regla.to})`);
      }
    }
  }

  get avisos(): string[] {
    return this.avisosScan;
  }

  /** Aristas cuyo destino es más antiguo que el origen => destino obsoleto. */
  obsoletos(): { arista: Arista; deltaMin: number }[] {
    const out: { arista: Arista; deltaMin: number }[] = [];
    for (const a of this.aristas) {
      const nf = this.porPath.get(a.fromPath);
      const nt = this.porPath.get(a.toPath);
      if (!nf || !nt) continue;
      if (nt.mtime < nf.mtime) {
        out.push({ arista: a, deltaMin: (nf.mtime - nt.mtime) / 60000 });
      }
    }
    return out.sort((x, y) => y.deltaMin - x.deltaMin);
  }

  /** Todo lo que depende (aguas abajo) de un fichero dado. */
  impacto(pathRel: string, profundidad = Infinity): { id: string; relacion: string; nivel: number }[] {
    const visitados = new Set<string>();
    const resultado: { id: string; relacion: string; nivel: number }[] = [];
    const inicio = this.porPath.get(pathRel);
    if (!inicio) return resultado;

    let frontera: { path: string; rel: string; nivel: number }[] = [
      { path: inicio.path, rel: "", nivel: 0 },
    ];
    while (frontera.length > 0) {
      const siguiente: { path: string; rel: string; nivel: number }[] = [];
      for (const f of frontera) {
        if (f.nivel >= profundidad) continue;
        for (const a of this.aristas) {
          if (a.fromPath === f.path && !visitados.has(a.toPath)) {
            visitados.add(a.toPath);
            const nodo = this.porPath.get(a.toPath);
            if (nodo) {
              resultado.push({ id: nodo.id, relacion: a.relacion, nivel: f.nivel + 1 });
              siguiente.push({ path: a.toPath, rel: a.relacion, nivel: f.nivel + 1 });
            }
          }
        }
      }
      frontera = siguiente;
    }
    return resultado;
  }

  /** Validación: referencias rotas (reglas que apuntan a nada) y ciclos. */
  validar(): string[] {
    const problemas: string[] = [...this.avisosScan];
    // Ciclos (DFS)
    const adj = new Map<string, string[]>();
    for (const a of this.aristas) {
      const arr = adj.get(a.fromId) ?? [];
      arr.push(a.toId);
      adj.set(a.fromId, arr);
    }
    const estado = new Map<string, number>(); // 0 sin visitar, 1 en pila, 2 hecho
    const pila: string[] = [];
    const dfs = (u: string): boolean => {
      estado.set(u, 1);
      pila.push(u);
      for (const v of adj.get(u) ?? []) {
        const e = estado.get(v) ?? 0;
        if (e === 1) {
          problemas.push(`Ciclo de dependencias: ${[...pila, v].join(" -> ")}`);
          return true;
        }
        if (e === 0 && dfs(v)) return true;
      }
      pila.pop();
      estado.set(u, 2);
      return false;
    };
    for (const id of this.nodos.keys()) {
      if ((estado.get(id) ?? 0) === 0) dfs(id);
    }
    return problemas;
  }

  resumen(): { nodos: number; aristas: number } {
    return { nodos: this.nodos.size, aristas: this.aristas.length };
  }

  arbol(): string {
    const lineas: string[] = [];
    const salientes = new Map<string, Arista[]>();
    for (const a of this.aristas) {
      const arr = salientes.get(a.fromId) ?? [];
      arr.push(a);
      salientes.set(a.fromId, arr);
    }
    for (const id of [...this.nodos.keys()].sort()) {
      const outs = salientes.get(id) ?? [];
      lineas.push(id);
      for (const a of outs) lineas.push(`   -> ${a.toId} (${a.relacion})`);
    }
    return lineas.join("\n");
  }
}
