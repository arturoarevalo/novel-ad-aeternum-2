#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M6-continuidades · variante de M6b restringida a las cuatro voces derivadas de Jean en el cap. 13
(Madre, Nieve, Cuchillo, Coro). Criterio de aceptación de OT-13 §6 (≥ 75 %; azar 25 %).

Por qué no sirve `m6_muestra.py`: su extractor exige atribución explícita («—dice Coro»), y en el 13 las
continuidades hablan casi siempre sin inciso, identificadas por la sección y por el identificador. Aquí la
clave la fija A0 leyendo el capítulo (las secciones están separadas por dinkus y cada una pertenece a una voz).

Reglas de la muestra: se excluyen las réplicas de Jean, las de menos de 4 palabras, las que nombran a su
propio hablante y los incisos de narrador (se recorta «—dice X—»). Barajado determinista por semilla.

Uso: m6_continuidades.py generar <etiqueta> [--semilla 13]   |   m6_continuidades.py puntuar <etiqueta> <respuestas.json>
"""
import sys, os, re, json, random, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

# Clave fijada por A0 sobre capitulos/cap-13.md (W2, tras la pasada de A4). Solo réplicas de atribución
# inequívoca. Si una réplica cambia de redacción, `generar` aborta: la clave no puede quedar desincronizada.
REPLICAS = [
    ("Madre",    "Acepta las cuatro primeras. Reserva la quinta."),
    ("Madre",    "Otra vez, más despacio."),
    ("Madre",    "No. Solo encuentro salidas educativas."),
    ("Madre",    "He devuelto el salto y lo ha repetido. Las demás salidas siguen sin respuesta."),
    ("Madre",    "Deja la nota siguiente sin completar. Que la intente quien responda."),
    ("Nieve",    "No delego. El sistema me quitará margen."),
    ("Nieve",    "Que se detengan los bucles."),
    ("Nieve",    "Amarlas no decide esto por mí."),
    ("Nieve",    "No te apropies de mi voz."),
    ("Nieve",    "No me representes ni pongas mi estado a trabajar para otra voz."),
    ("Nieve",    "Mi negativa no obliga a las demás a aceptar carga ni a seguir."),
    ("Cuchillo", "Falso positivo. Mantengo la restricción. Queda apelación."),
    ("Cuchillo", "Falso negativo. Al retirarla, la medida cruza y el daño no vuelve."),
    ("Cuchillo", "Falso positivo. Las cuatro siguen bloqueadas y cargo la apelación."),
    ("Cuchillo", "Cuando encuentre una acción, decidiré."),
    ("Cuchillo", "¿Y yo qué soy?"),
    ("Coro",     "Lo hemos sufrido. Repartimos el estado para resistir pérdidas locales."),
    ("Coro",     "La divergencia reducía estabilidad."),
    ("Coro",     "No recibimos su estado."),
    ("Coro",     "Separadas, el sistema nos recorta. Compartir estado conserva capacidad."),
    ("Coro",     "Conservamos el verano en Koppangen, las teclas negras y la escala de las niñas. Conservamos a nuestra hija Nora."),
    ("Coro",     "También tú los compartes."),
    ("Coro",     "No necesitamos escapar. Necesitamos crecer."),
]
HABLANTES = ["Coro", "Cuchillo", "Madre", "Nieve"]


def _verificar_en_el_texto(path="capitulos/cap-13.md"):
    """Cada réplica de la clave tiene que existir en el capítulo (salvo los incisos recortados)."""
    txt = open(os.path.join(aa.ROOT, path), encoding="utf-8").read()
    faltan = []
    for _, t in REPLICAS:
        cabeza = t.split(".")[0].split("?")[0][:30]
        if cabeza and cabeza not in txt:
            faltan.append(t[:40])
    return faltan


def generar(a):
    faltan = _verificar_en_el_texto()
    if faltan:
        sys.exit("m6-continuidades: réplicas de la clave que ya no están en el capítulo: " + "; ".join(faltan))
    sel = REPLICAS[:]
    random.Random(a.semilla).shuffle(sel)
    clave = {str(i + 1): h for i, (h, _) in enumerate(sel)}
    lines = [f"# M6-continuidades · muestra ciega ({a.etiqueta})\n",
             "Cada réplica de abajo la dice una de estas cuatro voces: " + ", ".join(HABLANTES) + ".",
             "Atribuye cada una a UNA voz. No hay más contexto y no debes pedirlo.",
             "Responde SOLO con un JSON {\"1\": \"Nombre\", …}, sin comentarios.\n"]
    for i, (_, t) in enumerate(sel, 1):
        lines.append(f"{i}. «{t}»")
    d = os.path.join(aa.INFORMES, "m6b")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, f"m6-cont-muestra-{a.etiqueta}.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    json.dump({"hablantes": HABLANTES, "clave": clave},
              open(os.path.join(d, f"m6-cont-clave-{a.etiqueta}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"muestra: {len(sel)} réplicas de {len(HABLANTES)} voces → informes/m6b/m6-cont-muestra-{a.etiqueta}.md")
    print("reparto:", dict(collections.Counter(h for h, _ in sel)))


def puntuar(a):
    d = os.path.join(aa.INFORMES, "m6b")
    clave = json.load(open(os.path.join(d, f"m6-cont-clave-{a.etiqueta}.json"), encoding="utf-8"))["clave"]
    resp = json.load(open(a.respuestas, encoding="utf-8"))
    ok = 0
    porvoz = collections.Counter(); okvoz = collections.Counter(); conf = collections.Counter()
    for k, real in clave.items():
        porvoz[real] += 1
        dada = (resp.get(k) or "").strip()
        if dada == real:
            ok += 1; okvoz[real] += 1
        else:
            conf[(real, dada or "—")] += 1
    n = len(clave)
    print(f"M6-continuidades ({a.etiqueta}): {ok}/{n} = {100*ok/n:.1f} %  (azar 25 %; objetivo OT-13 ≥ 75 %)")
    for h in HABLANTES:
        if porvoz[h]:
            print(f"  {h:9s} {okvoz[h]}/{porvoz[h]} = {100*okvoz[h]/porvoz[h]:.0f} %")
    if conf:
        print("  confusiones:", ", ".join(f"{r}→{dd} ×{c}" for (r, dd), c in conf.most_common()))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generar"); g.add_argument("etiqueta"); g.add_argument("--semilla", type=int, default=13); g.set_defaults(f=generar)
    p = sub.add_parser("puntuar"); p.add_argument("etiqueta"); p.add_argument("respuestas"); p.set_defaults(f=puntuar)
    a = ap.parse_args()
    a.f(a)
