#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Censo de puntos de abandono de una campaña — el criterio de salida que puso el autor.

  «Ningún capítulo nombrado como punto de abandono por dos o más lectores en el mismo hito.»
  (decisión de autor, 2026-08-18)

Existe porque el extractor de `w10_scores.py` —`re.search(r"abandonar[^.]{0,160}\\.")`— ha
devuelto cadena vacía en dos de las tres campañas de W10 y media frase en la tercera. Un
criterio que nadie puede leer no es un criterio: es la misma lección de `OT-13` §6, que llevó
tres mediciones fallando sin que ningún gate lo marcara.

Este lee la frase entera, saca TODOS los números de capítulo que nombra —principal y
secundarios—, los traduce a fichero y posición porcentual, y cuenta cuántos lectores nombran
cada uno. Distingue nominación principal de secundaria, porque las dos cuentas dan resultados
distintos y hay que decir cuál se usa.

  python3 herramientas/lib/censo_abandonos.py <etiqueta>
"""
import io, os, re, sys, glob, collections
sys.path.insert(0, os.path.dirname(__file__)); import aa

def posiciones():
    o = aa.reading_order(); ws = [aa.count_words(d["body"]) for d in o]; tot = sum(ws)
    out, acc = {}, 0
    for i, (d, w) in enumerate(zip(o, ws), 1):
        out[i] = (d["archivo"], d["fm"].get("titulo", "?"), 100 * (acc + w / 2) / tot); acc += w
    return out

DISPARO = re.compile(r"(?:más cerca de |a punto de |estuve? .{0,20})?abandon\w*", re.I)
CAPNUM  = re.compile(r"cap(?:[íi]tulo)?s?\.?\s*(\d{1,2})|\bel\s+(\d{1,2})\b|\by\s+el\s+(\d{1,2})\b")

def frase_de_abandono(texto):
    """Devuelve el bloque de texto que contiene la respuesta a la pregunta obligatoria."""
    for l in texto.split("\n"):
        if DISPARO.search(l) and len(l) > 60:
            return l
    return ""

def numeros(frase):
    """Primero el principal (el más cercano al disparo), después los demás, en orden."""
    m = DISPARO.search(frase)
    if not m: return []
    cola = frase[m.end():]
    vistos, orden = set(), []
    for mm in CAPNUM.finditer(cola):
        n = int(next(g for g in mm.groups() if g))
        if 1 <= n <= 60 and n not in vistos:
            vistos.add(n); orden.append(n)
    return orden

def main():
    etq = sys.argv[1]
    d = os.path.join(aa.ROOT, "informes", "w10")
    pos = posiciones()
    # n=7: los tres críticos de rúbrica MÁS los cuatro lectores beta, que es el conjunto con
    # que se midió vF. Contar solo los tres críticos y compararlo con vF mezcla dos
    # instrumentos de potencia muy distinta: a n=3 el criterio pasa por azar entre el 69 % y
    # el 94 % de las veces, y a n=7 baja al 3,8 %.
    ficheros = sorted(glob.glob(os.path.join(d, "a6-%s-critico-*.md" % etq))
                    + glob.glob(os.path.join(d, "a6b-beta-*-%s.md" % etq)))
    deriva = glob.glob(os.path.join(d, "a6-%s-deriva-v0.md" % etq))
    principal, cualquiera, detalle = collections.Counter(), collections.Counter(), []
    for f in ficheros:
        t = io.open(f, encoding="utf-8").read()
        fr = frase_de_abandono(t); ns = numeros(fr)
        detalle.append((os.path.basename(f), ns, fr[:150]))
        if ns:
            principal[ns[0]] += 1
            for n in ns: cualquiera[n] += 1
    print("CENSO DE ABANDONOS · %s · %d lectores" % (etq, len(ficheros)))
    print("  AVISO: los números de capítulo se traducen contra el orden de lectura de HOY.")
    print("  Para campañas de un texto anterior (vF tenía 48 capítulos, hoy hay 47), el")
    print("  RECUENTO es válido pero la IDENTIDAD del capítulo no: el impreso 31 de vF era")
    print("  «Interferencias» y hoy es «Casa prestada». Los números localizan; solo la cita")
    print("  literal identifica.\n")
    for nom, ns, fr in detalle:
        etiquetas = " · ".join("%d=%s(%.1f%%)" % (n, pos.get(n, ("?", "?", 0))[0], pos.get(n, ("?", "?", 0))[2])
                               for n in ns) or "NO LOCALIZADO"
        print("  %-28s %s" % (nom.replace("a6-%s-" % etq, ""), etiquetas))
        if not ns: print("      frase: %s" % fr[:120])
    # INSTRUMENTO Nº 24, encontrado por A2 al cerrar la fase: EL CENSO CUENTA NOMBRES DE
    # CAPÍTULO Y LOS LECTORES NOMBRAN CLASES. Un lector aporta entre 0 y 5 nominaciones según
    # lo específico que decida ser: uno escribió «la segunda mitad de la parte II» y aportó
    # cero; otro dio cinco ejemplos. Consecuencia exacta y medida: si los dos lectores que
    # nombraron «EDDA» hubieran escrito «en los capítulos-máquina» sin dar ejemplos, el
    # criterio del autor PASARÍA. Misma lectura, mismo abandono, veredicto opuesto.
    #
    # Corrección de A2, que no rompe la comparabilidad con vF: resolver POR LECTOR y contar
    # solo la nominación PRINCIPAL. Un lector, un voto. Las secundarias se registran pero no
    # deciden, porque su número mide la locuacidad del lector y no el libro.
    def tabla(c, titulo):
        print("\n  %s" % titulo)
        fallan = []
        for n, k in c.most_common():
            a, t, p = pos.get(n, ("?", "?", 0))
            marca = "  <<< INCUMPLE" if k >= 2 else ""
            if k >= 2: fallan.append(n)
            print("    %-3d %-12s «%-22s» %5.1f %%  ×%d%s" % (n, a, t[:22], p, k, marca))
        return fallan
    ilegibles = [n for n, ns, fr in detalle if not ns]
    if ilegibles:
        print("\n  *** SIN VEREDICTO: no se ha podido leer la respuesta de %d de %d lectores ***"
              % (len(ilegibles), len(ficheros)))
        for n in ilegibles: print("      ilegible: %s" % n)
        print("  Un censo que no ha leído a todos los lectores NO PUEDE decir si el criterio")
        print("  se cumple: la ausencia de una nominación y la incapacidad de leerla son")
        print("  indistinguibles para este script, y la segunda siempre inclina hacia CUMPLE.")
        print("  Cuéntalo a mano y no te fíes de un OK que no ha mirado. (Lección de W10: el")
        print("  instrumento 21 informaba «OK» sobre un capítulo que no veía.)")
    f1 = tabla(principal, "por nominación PRINCIPAL:")
    f2 = tabla(cualquiera, "contando también las secundarias:")
    if ilegibles:
        print("\n  CRITERIO DEL AUTOR: **NO DETERMINADO** (%d lectores ilegibles)." % len(ilegibles))
        sys.exit(2)
    print("\n  CRITERIO DEL AUTOR — ningún capítulo con dos o más nominaciones:")
    print("    POR LECTOR, solo principales (la cuenta buena): %s"
          % ("INCUMPLE en %s" % f1 if f1 else "CUMPLE"))
    print("    con secundarias (informativa, NO decide — mide locuacidad, no el libro): %s"
          % ("INCUMPLE en %s" % f2 if f2 else "CUMPLE"))
    print("\n  Potencia: P(pasar por azar) = 0,94 a n=3 · 0,26 a n=5 · 0,038 a n=7 (pool empírico).")
    print("  Una medición a n=3 NO es interpretable. Solo n=7 tiene potencia.")
    if deriva:
        t = io.open(deriva[0], encoding="utf-8").read()
        fr = frase_de_abandono(t); ns = numeros(fr)
        print("\n  control de deriva sobre v0 (numeración de v0, no traducible): %s" % (ns or "no localizado"))

if __name__ == "__main__":
    main()
