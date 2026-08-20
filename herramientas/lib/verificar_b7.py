#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador de literales de `biblia/b7-perimetro.md` — y de cualquier documento vinculante.

Existe por un hecho medido: en tres días aparecieron CUATRO condiciones de A7 apuntando a un
sitio equivocado —P-41 desaparecida entera, dos punteros que resolvían a otra línea, y un
`desc` truncado desde W5—, y ninguna la rompió nadie: se rompieron solas, por movimiento del
suelo. A7 lo dejó escrito: «una condición que vive en un número de línea está muerta en
cuanto alguien corta un párrafo por encima. Escríbase la condición donde se rompa, no donde
se lea.»

Este script hace justo eso: **ignora el número y busca el literal**. Tres veredictos por cita:

  OK        el literal existe y el número acierta
  MOVIDA    el literal existe pero en otra línea  → el número se actualiza solo con --arreglar
  PERDIDA   el literal NO existe en el fichero    → alguien lo editó o lo borró. Falla cerrada.

Uso:  python3 herramientas/lib/verificar_b7.py [documento…] [--arreglar]
      (sin argumentos verifica biblia/b7-perimetro.md y protegidos/spans.json)
"""
import io, os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import aa

REF = re.compile(r"`(cap-\d{2}|00-aviso|99-recursos)(?:\.md)?:(\d+)`")
LIT = re.compile(r"«([^»]{6,400})»")

def lineas(arch):
    p = os.path.join(aa.CAPITULOS, arch if arch.endswith(".md") else arch + ".md")
    if not os.path.exists(p): return None
    return io.open(p, encoding="utf-8").read().split("\n")

def verificar_doc(path, arreglar=False):
    txt = io.open(path, encoding="utf-8").read()
    out, cambios, usados = [], 0, set()
    for m in REF.finditer(txt):
        arch, num = m.group(1), int(m.group(2))
        if "~~" in txt[max(0, m.start()-90):m.end()+40]:
            out.append(("TACHADA", arch, num, 0, "entrada tachada a propósito")); continue
        ls = lineas(arch)
        if ls is None:
            out.append(("PERDIDA", arch, num, 0, "el fichero no existe")); continue
        # SOLO el patrón real del documento: «literal» seguido inmediatamente de (`cap-NN:LL`),
        # o `cap-NN:LL` seguido inmediatamente de «literal». Emparejar por proximidad amplia
        # produjo 49 falsos positivos en la primera versión de este script —un literal servía a
        # tres referencias de la misma frase—, que es justo el modo de fallo que viene a cazar.
        # Cobertura menor y honesta antes que alarma masiva: lo que no case se declara NO VERIFICABLE.
        antes = txt[max(0, m.start()-14): m.start()]
        despues = txt[m.end(): m.end()+14]
        lit, marca = None, None
        if "»" in antes:                       # «literal» (`cap-NN:LL`)
            izq, der = txt.rfind("«", 0, m.start()), txt.rfind("»", 0, m.start())
            if izq != -1 and der > izq and (m.start() - der) <= 14:
                lit, marca = txt[izq+1:der].strip(), (izq, der)
        if lit is None and "«" in despues:      # `cap-NN:LL` «literal»
            izq = txt.find("«", m.end()); der = txt.find("»", izq+1) if izq != -1 else -1
            if izq != -1 and der != -1 and (izq - m.end()) <= 14:
                lit, marca = txt[izq+1:der].strip(), (izq, der)
        # Dos referencias comparten un literal —«…» (`cap-A:1`) y `cap-B:2`—: el literal es de la
        # PRIMERA que lo tomó, venga por delante o por detrás. Declarar la segunda NO VERIFICABLE
        # es mejor que buscarle otro: darle el del vecino fue el fallo de las tres versiones
        # anteriores de este script, y produjo 49, 8 y 2 alarmas falsas.
        if marca is not None and marca in usados:
            out.append(("SIN-LITERAL", arch, num, 0, "comparte literal con otra referencia")); continue
        if marca is not None:
            usados.add(marca)
        if not lit or len(lit) < 6:
            out.append(("SIN-LITERAL", arch, num, 0, "no verificable: la cita no lleva literal pegado"))
            continue
        lit = lit.split(" / ")[0].strip()   # los pares de réplica se verifican por la primera
        lit = lit.strip("…").strip()        # b7 abrevia con puntos suspensivos: «…Kongsbakken era…»
        if " + " in lit:                    # descripción de patrón, no cita: «No dice + interrogativa»
            out.append(("SIN-LITERAL", arch, num, 0, "fórmula de patrón, no literal")); continue
        if "~~" in txt[max(0, m.start()-90):m.end()+40]:   # entrada tachada a propósito
            out.append(("TACHADA", arch, num, 0, lit[:60])); continue
        hits = [i+1 for i, l in enumerate(ls) if lit in l]
        if not hits:
            out.append(("PERDIDA", arch, num, 0, lit[:70]))
        elif num in hits:
            # Un literal corto es subcadena de demasiadas cosas: probado, «Por ahí no» sobrevive a
            # que alguien escriba «Por ahí no vamos», que cambia la línea protegida y este script
            # da OK. Se declara la debilidad en vez de fingir que no está: lo que este verificador
            # caza es BORRADO y DESPLAZAMIENTO, no toda modificación.
            out.append(("OK-DEBIL" if len(lit) < 25 else "OK", arch, num, num, lit[:70]))
        else:
            out.append(("MOVIDA", arch, num, hits[0], lit[:70]))
            if arreglar:
                txt = txt[:m.start()] + "`%s:%d`" % (arch, hits[0]) + txt[m.end():]
                cambios += 1
    if arreglar and cambios:
        io.open(path, "w", encoding="utf-8").write(txt)
    return out, cambios

def verificar_spans():
    """Los spans son la otra mitad: su `archivo` puede haber dejado de existir."""
    P = os.path.join(aa.PROTEGIDOS, "spans.json")
    raw = json.load(open(P, encoding="utf-8"))
    items = raw["spans"] if isinstance(raw, dict) and "spans" in raw else raw
    malos = []
    for e in items:
        p = os.path.join(aa.ROOT, e["archivo"])
        if not os.path.exists(p):
            malos.append((e["id"], "fichero inexistente: " + e["archivo"])); continue
        t = io.open(p, encoding="utf-8").read()
        ini, fin = e.get("inicio"), e.get("fin")
        if ini and ini not in t:   malos.append((e["id"], "INICIO no localizable"))
        elif fin and fin not in t: malos.append((e["id"], "FIN no localizable"))
        elif not ini:              malos.append((e["id"], "span sin campo `inicio`: no verificable por literal"))
        d = str(e.get("desc", ""))
        # DETECTOR DETERMINISTA. La heurística «acaba en preposición» encontró cuatro de seis:
        # se le escaparon los dos que el corte dejó terminando en punto, y uno de ellos era el
        # span que A7 llama «el más importante de todo el encargo». El corte real es de longitud
        # EXACTA, así que se comprueba la longitud y no la forma. Un `desc` de 300 caracteres
        # clavados no es una coincidencia: es una amputación.
        if len(d) == 300:
            malos.append((e["id"], "desc AMPUTADO en 300 caracteres exactos: «…%s»" % d[-40:]))
        elif d and re.search(r"\b(de|del|la|el|en|con|por|tras|y)\s*$", d.strip()):
            malos.append((e["id"], "desc probablemente truncado: «…%s»" % d.strip()[-40:]))
    return len(items), malos

def cotejar_descs():
    """Coteja cada `desc` de spans.json contra el informe de A7 que lo originó.

    A7, 2026-08-20: «la longitud exacta 300 caza ESTE corte, no la clase — los diez se
    cortaron al escribir. La comprobación que hoy sí ha funcionado es otra: cotejar cada desc
    contra el informe de A7 que lo originó. Que ésa vaya al hook y la de longitud quede de red
    secundaria.» Tenía razón: el detector de longitud es una firma de un incidente; éste
    compara con la fuente.
    """
    import glob
    P = os.path.join(aa.PROTEGIDOS, "spans.json")
    raw = json.load(open(P, encoding="utf-8"))
    items = raw["spans"] if isinstance(raw, dict) and "spans" in raw else raw
    fuentes = "\n".join(io.open(f, encoding="utf-8").read()
                        for f in glob.glob(os.path.join(aa.INFORMES, "a7-*.md")))
    malos = []
    for e in items:
        d = str(e.get("desc", ""))
        if not d: continue
        d_lim = d.split(" · [")[0].strip()          # quita las notas de restauración
        if len(d_lim) < 40: continue
        m = re.search(r"\|\s*`%s`\s*\|.*?\|.*?\|\s*(.*?)\s*\|\s*$" % re.escape(e["id"]),
                      fuentes, re.M)
        if not m: continue                           # sin informe de origen: no comparable
        orig = m.group(1).strip()
        if len(orig) > len(d_lim) + 20 and orig[:60] == d_lim[:60]:
            malos.append((e["id"], "desc MÁS CORTO que su origen en informes/: %d frente a %d caracteres"
                          % (len(d_lim), len(orig))))
    return malos


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--deuda" in sys.argv:
        # Lista las citas que NO se pueden verificar por literal. A7 se comprometió el
        # 2026-08-20 a darle un literal a cada una o borrarla antes de la próxima orden que
        # toque el perímetro. Sin esta lista, «49 sin literal» es un número y no una tarea.
        d = os.path.join(aa.BIBLIA, "b7-perimetro.md")
        txt = io.open(d, encoding="utf-8").read()
        out, _ = verificar_doc(d)
        sin = [(a, n, m) for est, a, n, r, m in out if est in ("SIN-LITERAL",)]
        print("DEUDA DE LITERALES · %d citas de %s no verificables\n" % (len(sin), os.path.basename(d)))
        lineas_doc = txt.split("\n")
        for a, n, motivo in sin:
            ctx = ""
            for i, l in enumerate(lineas_doc, 1):
                if "`%s:%d`" % (a, n) in l:
                    ctx = "b7:%d · %s" % (i, l.strip()[:110]); break
            print("  %-14s %-38s %s" % ("%s:%d" % (a, n), motivo, ctx))
        sys.exit(0)
    arreglar = "--arreglar" in sys.argv
    docs = args or [os.path.join(aa.BIBLIA, "b7-perimetro.md")]
    fallo = False
    for d in docs:
        out, cam = verificar_doc(d, arreglar)
        n = {k: sum(1 for r in out if r[0] == k) for k in ("OK","OK-DEBIL","MOVIDA","PERDIDA","SIN-LITERAL","TACHADA")}
        print("%s · %d citas · OK %d (+%d débiles) · MOVIDA %d · PERDIDA %d · sin literal %d"
              % (os.path.basename(d), len(out), n["OK"], n["OK-DEBIL"], n["MOVIDA"], n["PERDIDA"],
                 n["SIN-LITERAL"]+n["TACHADA"]))
        for est, arch, num, real, lit in out:
            if est == "OK-DEBIL":
                print("   débil    %s:%d  «%s» — %d caracteres: sobrevive a que le añadan palabras"
                      % (arch, num, lit, len(lit)))
        for est, arch, num, real, lit in out:
            if est == "MOVIDA":
                print("   MOVIDA   %s:%d → :%d  «%s»" % (arch, num, real, lit))
            elif est == "PERDIDA":
                print("   PERDIDA  %s:%d  «%s»" % (arch, num, lit)); fallo = True
        if cam: print("   (%d números actualizados con --arreglar)" % cam)
    tot, malos = verificar_spans()
    malos += cotejar_descs()
    print("spans.json · %d spans · %d con problema" % (tot, len(malos)))
    for i, m in malos:
        print("   %-22s %s" % (i, m)); fallo = True
    sys.exit(1 if fallo else 0)

if __name__ == "__main__":
    main()
