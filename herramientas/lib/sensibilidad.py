#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T7 · Pre-chequeo automático de sensibilidad (aviso previo, NO veto): aplica los patrones de A7 (biblia/b7-patrones-A.txt
nivel A, biblia/b7-patrones-B.txt nivel B; una regex -E por línea, sin distinción de mayúsculas) al cuerpo de todos los
ficheros de capitulos/, y compara con la baseline informes/a7-baseline-v0.tsv (o la que se indique): lista los hits NUEVOS
(texto de línea no presente en la baseline) para que A0 se los pase a A7. Filtra «Cuchillo» (nombre de continuidad).
Uso: sensibilidad.py [--baseline informes/a7-baseline-v0.tsv] [--escribir informes/a7-hits-<etiqueta>.tsv] [--solo cap-08.md …]
Exit 0 siempre (es un aviso), salvo error de ficheros.
"""
import sys, os, re, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

def cargar_patrones(p):
    pats = []
    for line in open(p, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"): continue
        pats.append((line, re.compile(line, re.I)))
    return pats

def hits(paths, patsA, patsB):
    out = []
    for path in paths:
        fm, _, body, text = aa.read_chapter(path)
        # número de línea real en el fichero: contar líneas del frontmatter
        offset = text[:text.find(body)].count("\n") if body and body in text else 0
        for i, line in enumerate(body.split("\n"), 1):
            if not line.strip(): continue
            plano = line
            for nivel, pats in (("A", patsA), ("B", patsB)):
                for src, rx in pats:
                    if rx.search(plano):
                        if nivel == "B" and re.search(r"\bCuchillo\b", plano) and not re.search(r"\bcuchillo\b", plano):
                            continue
                        out.append((nivel, os.path.basename(path), i + offset, src[:40], plano.strip()[:200]))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", default=os.path.join(aa.INFORMES, "a7-baseline-v0.tsv"))
    ap.add_argument("--escribir")
    ap.add_argument("--solo", nargs="*")
    a = ap.parse_args()
    patsA = cargar_patrones(os.path.join(aa.BIBLIA, "b7-patrones-A.txt"))
    patsB = cargar_patrones(os.path.join(aa.BIBLIA, "b7-patrones-B.txt"))
    paths = sorted(os.path.join(aa.CAPITULOS, f) for f in os.listdir(aa.CAPITULOS) if f.endswith(".md"))
    if a.solo:
        # se admite tanto `cap-08.md` como `capitulos/cap-08.md`; un nombre que no case es ERROR,
        # no una lista vacía: este pre-chequeo alimenta un gate con veto y no puede fallar abierto.
        pedidos = [os.path.basename(s) for s in a.solo]
        disponibles = {os.path.basename(p) for p in paths}
        faltan = [s for s in pedidos if s not in disponibles]
        if faltan:
            sys.exit(f"sensibilidad: no existe(n) en capitulos/: {', '.join(faltan)}")
        paths = [p for p in paths if os.path.basename(p) in pedidos]
    H = hits(paths, patsA, patsB)
    base_textos = set()
    if os.path.exists(a.baseline):
        for line in open(a.baseline, encoding="utf-8"):
            if line.startswith("#") or line.startswith("nivel\t"): continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) >= 5: base_textos.add((cols[1], cols[4].strip()[:120]))
    nuevos = [h for h in H if (h[1], h[4][:120]) not in base_textos]
    if a.escribir:
        with open(a.escribir, "w", encoding="utf-8") as f:
            f.write("nivel\tfichero\tlinea\tpatron\ttexto\n")
            for h in H: f.write("\t".join(map(str, h)) + "\n")
    print(f"T7 pre-chequeo: {len(H)} hits totales ({sum(1 for h in H if h[0]=='A')} A / {sum(1 for h in H if h[0]=='B')} B) · NUEVOS respecto a baseline: {len(nuevos)}")
    for h in nuevos:
        print(f"  [{h[0]}] {h[1]}:{h[2]} ({h[3]}) → {h[4][:140]}")
    if nuevos:
        print("→ Pasar la lista de NUEVOS a A7 (nivel A: lectura obligatoria).")

if __name__ == "__main__":
    main()
