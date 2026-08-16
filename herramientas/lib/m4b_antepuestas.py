#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M4b · Censo del tic de «subordinada / construcción antepuesta + coma» en la narración (hallazgo de los críticos fríos A6-1 y
A6-2 sobre v0: «Sin recibir la ampliación que esperaba, Alana señaló…», «Con los guantes tendidos, Maja señaló», «Al oírla,
Alana se volvió»). Cuenta, por capítulo, las frases narrativas (sin réplicas ni registros) que empiezan por Al/Sin/Con/Tras/
Cuando/Mientras/Aunque/gerundio/participio… y llevan coma antes de la principal. Baseline v0: 237/4.512 = 5,3 %.
Uso: m4b_antepuestas.py [--umbral 8]   (imprime tabla; código de salida 1 si algún capítulo editable supera el umbral)
"""
import sys, os, re, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

PAT = re.compile(r"^(Al |Sin |Con |Tras |Antes de |Después de |Mientras |Cuando |Aunque |Si |Como |Desde |Hasta |Para |Por |Durante |"
                 r"Sobre |Bajo |Entre |Junto |Frente |Ante |Según |Nada más |Una vez |"
                 r"[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:ando|iendo|éndose|ándose|ándola|ándolo|iéndola|iéndolo)\b|"
                 r"[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:ado|ada|ados|adas|ido|ida|idos|idas)\b [a-záéíóúñ]+)[^.;:!?]{0,80}?,\s+[a-záéíóúñA-ZÁÉÍÓÚÑ]")

def censo(body):
    lines = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("—") and not l.strip().startswith("#") and not aa.es_dinkus(l)]
    text = " ".join(lines)
    sents = [s.strip() for s in re.split(r"(?<=[.!?…])\s+", text) if s.strip()]
    sents = [s for s in sents if not s.startswith("—") and not s.startswith("`")]
    hits = [s for s in sents if PAT.match(s)]
    return len(sents), hits

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--umbral", type=float, default=8.0); ap.add_argument("--mostrar", action="store_true")
    a = ap.parse_args()
    tot = 0; th = 0; peor = []
    print("| capítulo | proteccion | frases narr. | antepuestas | % | por 1.000 pal. |\n|---|---|---:|---:|---:|---:|")
    for d in aa.reading_order():
        n, h = censo(d["body"]); w = aa.count_words(d["body"])
        tot += n; th += len(h)
        prot = d["fm"].get("proteccion", "")
        pct = 100 * len(h) / max(n, 1)
        print(f"| {d['archivo']} | {prot} | {n} | {len(h)} | {pct:.1f} | {1000*len(h)/max(w,1):.1f} |")
        if pct > a.umbral and prot != "total":
            peor.append((d["archivo"], pct))
        if a.mostrar:
            for s in h: print("    ·", s[:140])
    print(f"\nTOTAL: {th}/{tot} = {100*th/max(tot,1):.1f} %")
    if peor:
        print("Por encima del umbral (editables):", ", ".join(f"{c} {p:.1f} %" for c, p in peor))
        sys.exit(1)

if __name__ == "__main__":
    main()
