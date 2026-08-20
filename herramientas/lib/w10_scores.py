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

# Tres defectos corregidos el 2026-08-19, encontrados por el juez C del panel de la
# iteración 0. Los tres fallaban A LA BAJA y en silencio, como los once anteriores:
#
# 1. La comparación era `dif > RUIDO`, estricta. Tres de los cuatro ejes atascados
#    necesitan EXACTAMENTE +0,5, así que un éxito perfecto se registraba como «sin
#    cambios» y el plan ordenaba revertirlo. Ahora es `>=`.
# 2. El control de deriva del mismo día se leía, se imprimía y NO ENTRABA en ninguna
#    comparación — es decir, no controlaba nada. Ahora se compara en diferencias
#    emparejadas: (candidato - v0 del mismo día) frente a (base - v0 de su día), que es
#    lo único que cancela la oscilación común del jurado.
# 3. `mejor_conocido` era un trinquete: subía cuando el ruido daba un eje de más y no
#    bajaba nunca, así que toda mejora real posterior se medía contra una base inflada.
#    Ahora se compara por suma de medianas y puede bajar.

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
    der_base = (mejor or {}).get("deriva_v0") or {}
    pareado = bool(deriva and der_base)
    print("%-12s %7s %9s %9s %8s" % ("eje","mediana","mejor","techo hist.","Δ pareada"))
    subidas, bajadas = [], []
    for e in EJES:
        m0 = (mejor or {}).get("medianas", {}).get(e)
        techo = est["techos_historicos"].get(e)
        marca = ""; dpar = ""
        if m0 is not None:
            if pareado and e in deriva and e in der_base:
                # diferencia emparejada: cada versión contra SU control de v0 del mismo día
                dif = (med[e] - float(deriva[e])) - (float(m0) - float(der_base[e]))
                dpar = "%+.2f" % dif
            else:
                dif = med[e] - m0
            # CUARTO DEFECTO, encontrado en it3 y es MÍO: emparejar cancela la deriva común
            # pero DUPLICA el ruido independiente. Con n=1 en el control, una oscilación de
            # ±0,5 en v0 —texto que nadie ha tocado— mete ±0,5 en la diferencia emparejada,
            # encima del ruido del candidato. Medido: la estructura de v0, mismo instrumento
            # y texto idéntico, dio 8 · 8 · 8,5 en tres campañas.
            # Por eso el control solo puede VETAR un movimiento, nunca fabricarlo: se exige
            # que la diferencia CRUDA también alcance el umbral, y se avisa cuando el
            # movimiento es de medio punto, que es indistinguible de la varianza demostrada.
            crudo = med[e] - float(m0)
            if dif >= RUIDO and crudo >= RUIDO:   marca = "  SUBE"; subidas.append(e)
            elif dif <= -RUIDO and crudo <= -RUIDO: marca = "  BAJA"; bajadas.append(e)
            if marca and abs(crudo) <= 0.5:
                marca += " (±0,5: dentro de la varianza del propio instrumento sobre texto idéntico)"
        print("%-12s %7.1f %9s %9s %8s%s" % (e, med[e], m0 if m0 is not None else "-", techo, dpar, marca))
    if not pareado:
        print("\n  AVISO: sin control de deriva emparejado — la comparación NO cancela la "
              "oscilación del jurado y no debe dirigir una reversión por sí sola.")

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
    # No es trinquete: se compara por suma de medianas y la mejor conocida puede bajar.
    suma = sum(med.values())
    suma0 = sum((mejor or {}).get("medianas", {}).values()) if mejor else None
    reg["suma_medianas"] = round(suma, 2)
    if mejor is None or suma > suma0:
        est["mejor_conocido"] = reg
        print("\n>>> nueva MEJOR CONOCIDA (suma %.1f%s · %d ejes en 9)"
              % (suma, "" if suma0 is None else " frente a %.1f" % suma0, len(nueve)))
    else:
        print("\n(mejor conocida sin cambio: suma %.1f frente a %.1f)" % (suma, suma0))
    E.guardar(est)

if __name__ == "__main__":
    main()
