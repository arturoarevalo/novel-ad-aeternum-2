#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractos por capítulo para el test de lector frío (F1 y gates de W2/W3): escribe compilado/extractos/<etiqueta>/<archivo>
con la cabecera numerada por orden de lectura y el cuerpo SIN frontmatter (igual que el compilado), un fichero por capítulo.
Insumo ÚNICO del agente `lector-frio`, que no debe ver pov, fecha, protecciones ni estado_plan.

Uso: extractos.py <etiqueta> [archivo1 archivo2 …]   (sin lista → todos los capítulos)
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("etiqueta")
    ap.add_argument("capitulos", nargs="*")
    a = ap.parse_args()
    m = aa.load_manifest()
    dinkus = m.get("dinkus", "* * *")
    orden = aa.reading_order()
    quiere = set(a.capitulos)
    destino = os.path.join(aa.COMPILADO, "extractos", a.etiqueta)
    os.makedirs(destino, exist_ok=True)
    n = 0; escritos = []
    for d in orden:
        n += 1
        if quiere and d["archivo"] not in quiere:
            continue
        titulo = d["fm"].get("titulo", "")
        body = d["body"].strip("\n")
        lines = [dinkus if aa.es_dinkus(l) else l for l in body.split("\n")]
        texto = f"## {n}. {titulo}\n\n" + "\n".join(lines) + "\n"
        salida = os.path.join(destino, d["archivo"])
        with open(salida, "w", encoding="utf-8") as f:
            f.write(texto)
        escritos.append((d["archivo"], aa.count_words(d["body"])))
    for arch, w in escritos:
        print(f"{os.path.relpath(destino, aa.ROOT)}/{arch}  {w} palabras")
    print(f"{len(escritos)} extractos → {os.path.relpath(destino, aa.ROOT)}/")

if __name__ == "__main__":
    main()
