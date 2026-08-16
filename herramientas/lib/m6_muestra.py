#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M6b · Atribución ciega por modelo. Genera una muestra barajada de réplicas SIN hablante (informes/m6-muestra-<et>.md)
y una clave oculta (informes/m6-clave-<et>.json). Un agente lector (sin acceso a la clave) atribuye cada réplica a un
personaje de la lista; después `m6_muestra.py puntuar <et> <respuestas.json>` calcula el acierto (global y por par).
Uso: m6_muestra.py generar <etiqueta> [--n 60] [--semilla 7]  |  m6_muestra.py puntuar <etiqueta> <respuestas.json>
respuestas.json = {"1": "Nora", "2": "Maja", …}
"""
import sys, os, json, random, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa
from metricas import extraer_replicas

def generar(a):
    reps = [r for r in extraer_replicas(aa.reading_order()) if len(r["texto"].split()) >= 4]
    por = collections.defaultdict(list)
    for r in reps: por[r["hablante"]].append(r)
    hablantes = sorted(h for h, l in por.items() if len(l) >= 8)
    rnd = random.Random(a.semilla)
    cuota = max(3, a.n // len(hablantes))
    sel = []
    for h in hablantes:
        l = por[h][:]; rnd.shuffle(l); sel += l[:cuota]
    rnd.shuffle(sel); sel = sel[:a.n]
    clave = {str(i + 1): r["hablante"] for i, r in enumerate(sel)}
    lines = [f"# M6b · Muestra ciega de réplicas ({a.etiqueta})\n",
             "Atribuye cada réplica a UNO de estos personajes: " + ", ".join(hablantes) + ".",
             "Responde SOLO con un JSON {\"1\": \"Nombre\", …}. No consultes ningún otro fichero.\n"]
    for i, r in enumerate(sel, 1):
        lines.append(f"{i}. «{r['texto']}»")
    os.makedirs(aa.INFORMES, exist_ok=True)
    open(os.path.join(aa.INFORMES, f"m6-muestra-{a.etiqueta}.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump({"hablantes": hablantes, "clave": clave}, open(os.path.join(aa.INFORMES, f"m6-clave-{a.etiqueta}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"muestra: {len(sel)} réplicas de {len(hablantes)} hablantes → informes/m6-muestra-{a.etiqueta}.md (clave oculta en m6-clave-{a.etiqueta}.json)")

def puntuar(a):
    clave = json.load(open(os.path.join(aa.INFORMES, f"m6-clave-{a.etiqueta}.json"), encoding="utf-8"))["clave"]
    resp = json.load(open(a.respuestas, encoding="utf-8"))
    ok = 0; por = collections.Counter(); okh = collections.Counter(); conf = collections.Counter()
    for k, v in clave.items():
        r = str(resp.get(k, "")).strip()
        por[v] += 1
        if r == v: ok += 1; okh[v] += 1
        else: conf[(v, r)] += 1
    n = len(clave)
    print(f"M6b acierto global: {100*ok/n:.1f} % ({ok}/{n})")
    for h in sorted(por): print(f"  {h}: {100*okh[h]/por[h]:.0f} % ({okh[h]}/{por[h]})")
    print("  confusiones:", conf.most_common(10))
    # pares
    for a1, b1 in [("Nora", "Jessie"), ("Astrid", "Maja"), ("Astrid", "Alana"), ("Maja", "Alana")]:
        sub = [(k, v) for k, v in clave.items() if v in (a1, b1)]
        if sub:
            okp = sum(1 for k, v in sub if str(resp.get(k, "")).strip() == v)
            print(f"  par {a1}/{b1}: {100*okp/len(sub):.0f} %")

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("generar"); p.add_argument("etiqueta"); p.add_argument("--n", type=int, default=60); p.add_argument("--semilla", type=int, default=7)
    p = sub.add_parser("puntuar"); p.add_argument("etiqueta"); p.add_argument("respuestas")
    a = ap.parse_args()
    (generar if a.cmd == "generar" else puntuar)(a)

if __name__ == "__main__":
    main()
