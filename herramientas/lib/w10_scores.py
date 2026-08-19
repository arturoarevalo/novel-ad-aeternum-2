#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""W10 · lee las cuatro lecturas de una campaña, saca medianas, compara con la mejor
conocida y con el control de deriva del mismo día, y actualiza el estado.

La guardia de regresión existe porque este proyecto ha medido que el jurado oscila
hasta 1,0 sobre texto idéntico: una bajada de 0,5 en un eje NO es una regresión, y
una subida de 0,5 tampoco es una mejora. Solo se acepta lo que supera el ruido.
"""
import json, re, io, os, sys, statistics as st
sys.path.insert(0, os.path.dirname(__file__)); import aa
import w10_estado as E

EJES = ["premisa","estructura","prosa","dialogo","personajes","mundo","ritmo","trama","duelo","tema","global"]
RUIDO = 0.5   # medido en W4-R: el mismo juez varía hasta 1,0 sobre texto idéntico

def leer(p):
    try: t = io.open(p, encoding="utf-8").read()
    except Exception: return None
    m = re.search(r'^\{.*\}$', t, re.M)
    if not m: return None
    try: return json.loads(m.group(0))
    except Exception: return None

def abandono(p):
    try: t = io.open(p, encoding="utf-8").read()
    except Exception: return ""
    m = re.search(r"abandonar[^.]{0,160}\.", t)
    return m.group(0)[:150] if m else ""

def main():
    etq = sys.argv[1]
    d = os.path.join(aa.ROOT, "informes", "w10")
    crit = [leer(os.path.join(d, "a6-%s-critico-%d.md" % (etq, i))) for i in (1,2,3)]
    crit = [c for c in crit if c]
    if not crit: sys.exit("sin lecturas válidas")
    deriva = leer(os.path.join(d, "a6-%s-deriva-v0.md" % etq))
    med = {e: st.median([float(c[e]) for c in crit if e in c]) for e in EJES}
    aband = [abandono(os.path.join(d, "a6-%s-critico-%d.md" % (etq, i))) for i in (1,2,3)]

    est = E.cargar()
    mejor = est.get("mejor_conocido")
    print("%-12s %7s %9s %9s" % ("eje","mediana","mejor","techo hist."))
    subidas, bajadas = [], []
    for e in EJES:
        m0 = (mejor or {}).get("medianas", {}).get(e)
        techo = est["techos_historicos"].get(e)
        marca = ""
        if m0 is not None:
            dif = med[e] - m0
            if dif > RUIDO:  marca = "  SUBE"; subidas.append(e)
            elif dif < -RUIDO: marca = "  BAJA"; bajadas.append(e)
        print("%-12s %7.1f %9s %9s%s" % (e, med[e], m0 if m0 is not None else "-", techo, marca))

    if deriva:
        print("\ncontrol de deriva sobre v0, mismo día: ritmo %.1f · global %.1f"
              % (float(deriva.get("ritmo",0)), float(deriva.get("global",0))))
    print("\npuntos de abandono:")
    for i,a in enumerate(aband,1): print("  A6-%d: %s" % (i, a))

    nueve = [e for e in EJES if med[e] >= 9.0]
    print("\nejes en 9,0 o mas: %d de 11 -> %s" % (len(nueve), ", ".join(nueve) or "ninguno"))
    if bajadas: print("REGRESION mas alla del ruido en: %s" % ", ".join(bajadas))
    if subidas: print("MEJORA mas alla del ruido en: %s" % ", ".join(subidas))
    if not subidas and not bajadas: print("Sin cambios fuera del ruido (+-%.1f)." % RUIDO)

    reg = {"etiqueta": etq, "medianas": med, "deriva_v0": deriva, "abandonos": aband,
           "ejes_en_9": nueve}
    if est["iteraciones"] and est["iteraciones"][-1]["estado"] == "abierta":
        est["iteraciones"][-1]["medicion"] = reg
    if mejor is None or len(nueve) > len(mejor.get("ejes_en_9", [])):
        est["mejor_conocido"] = reg
        print("\n>>> nueva MEJOR CONOCIDA (%d ejes en 9)" % len(nueve))
    E.guardar(est)

if __name__ == "__main__":
    main()
