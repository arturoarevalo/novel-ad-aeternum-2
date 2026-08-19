#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
W10 · libro de estado de la fase autónoma.

Por qué existe: W10 corre sin humano y a través de sesiones distintas. Sin un
estado en disco, cada reinicio empieza de cero, repite intervenciones ya probadas
y no puede saber si algo mejoró o empeoró. Este fichero ES la memoria de la fase.

Uso:
    w10_estado.py mostrar
    w10_estado.py iteracion-nueva "<hipotesis>"
    w10_estado.py anotar <clave> <valor>
    w10_estado.py cerrar <aceptada|revertida> "<motivo>"
"""
import json, os, sys, io, argparse
sys.path.insert(0, os.path.dirname(__file__))
import aa

ESTADO = os.path.join(aa.ROOT, "informes", "w10", "estado.json")

BASE = {
    "fase": "W10",
    "objetivo": "9,0 en los diez ejes y en la nota global",
    "techos_historicos": {
        "_nota": "maximo jamas alcanzado en 48 lecturas frias de TODAS las versiones, v0 incluida",
        "premisa": 9.5, "estructura": 8.5, "prosa": 9.0, "dialogo": 9.0,
        "personajes": 9.0, "mundo": 9.0, "ritmo": 8.0, "trama": 8.5,
        "duelo": 9.5, "tema": 9.5, "global": 8.5,
    },
    "nunca_han_llegado_a_9": ["estructura", "ritmo", "trama", "global"],
    "mejor_conocido": None,
    "iteraciones": [],
    "intervenciones_probadas": [],
    "callejones_sin_salida": [],
}

def cargar():
    if os.path.exists(ESTADO):
        return json.load(open(ESTADO, encoding="utf-8"))
    return dict(BASE)

def guardar(d):
    os.makedirs(os.path.dirname(ESTADO), exist_ok=True)
    json.dump(d, io.open(ESTADO, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    io.open(ESTADO, "a", encoding="utf-8").write("\n")

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("mostrar")
    p = sub.add_parser("iteracion-nueva"); p.add_argument("hipotesis")
    p = sub.add_parser("anotar"); p.add_argument("clave"); p.add_argument("valor")
    p = sub.add_parser("cerrar"); p.add_argument("resultado", choices=["aceptada","revertida"]); p.add_argument("motivo")
    a = ap.parse_args()
    d = cargar()

    if a.cmd == "mostrar":
        print(json.dumps(d, ensure_ascii=False, indent=2))
        return
    if a.cmd == "iteracion-nueva":
        n = len(d["iteraciones"]) + 1
        d["iteraciones"].append({"n": n, "hipotesis": a.hipotesis, "estado": "abierta",
                                 "notas": {}, "medicion": None, "resultado": None})
        guardar(d); print("iteracion %d abierta" % n); return
    if not d["iteraciones"]:
        sys.exit("no hay iteracion abierta")
    it = d["iteraciones"][-1]
    if a.cmd == "anotar":
        it["notas"][a.clave] = a.valor; guardar(d); print("anotado"); return
    if a.cmd == "cerrar":
        it["estado"] = "cerrada"; it["resultado"] = {"veredicto": a.resultado, "motivo": a.motivo}
        d["intervenciones_probadas"].append({"n": it["n"], "hipotesis": it["hipotesis"],
                                             "veredicto": a.resultado, "motivo": a.motivo})
        if a.resultado == "revertida":
            d["callejones_sin_salida"].append(it["hipotesis"])
        guardar(d); print("iteracion %d cerrada: %s" % (it["n"], a.resultado)); return

if __name__ == "__main__":
    main()
