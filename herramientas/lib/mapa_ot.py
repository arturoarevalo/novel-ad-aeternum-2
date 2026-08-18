#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapa de intervenciones (Fase 2): lee todas las `ordenes/OT-*.md`, extrae cabecera (Δ, presupuesto, oleada, escritor,
estado), cuenta intervenciones y etiquetas de función, detecta spans marcados «REQUIERE LIBERACIÓN» y ripples, y
comprueba coherencia con `ordenes/tabla-5-1.json` (Δ, oleada, estado_plan) y con el manifiesto (presupuesto vF).
Uso: mapa_ot.py [--md]   (tabla resumen; --md imprime markdown para informes/)
"""
import sys, os, re, json, glob, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

TAGS = ["ORIENTACIÓN", "INTERIORIDAD", "TENSIÓN", "AGENCIA", "TEXTURA", "PAGO"]

def parse_ot(path):
    s = open(path, encoding="utf-8").read()
    ot = os.path.basename(path)[:-3]
    d = {"ot": ot, "path": path, "palabras_doc": aa.count_words(s)}
    m = re.search(r"\|\s*Δ objetivo[^|]*\|\s*([^|]*)\|", s)
    d["delta_txt"] = m.group(1).strip() if m else ""
    m2 = re.search(r"([+\-−±]\s?\d[\d.]*)", d["delta_txt"])
    d["delta"] = None
    if m2:
        t = m2.group(1).replace("−", "-").replace("±", "+").replace(" ", "").replace(".", "")
        try: d["delta"] = int(t)
        except: d["delta"] = None
    m = re.search(r"\|\s*Oleada[^|]*\|\s*([^|]*)\|", s)
    d["oleada"] = (re.search(r"W\d", m.group(1)).group(0) if (m and re.search(r"W\d", m.group(1))) else ("—" if m else ""))
    d["escritor"] = ("A3a" if (m and "A3a" in m.group(1)) else ("A3b" if (m and "A3b" in m.group(1)) else ""))
    m = re.search(r"\|\s*Estado de la OT\s*\|\s*([^|]*)\|", s)
    d["estado"] = m.group(1).strip() if m else ""
    m = re.search(r"\|\s*estado_plan[^|]*\|\s*([^|]*)\|", s)
    d["estado_plan"] = m.group(1).strip() if m else ""
    inter = re.findall(r"\*\*I-(\d+)\s*[·:]\s*`?([A-ZÁÉÍÓÚÑ]+)`?", s)
    d["n_inter"] = len(inter)
    d["tags"] = collections.Counter(t for _, t in inter)
    d["sin_etiqueta"] = [n for n, t in inter if t not in TAGS]
    d["liberar"] = sorted(set(re.findall(r"(S\d\d-[a-z0-9\-]+)[^\n]{0,80}REQUIERE LIBERACI", s)) |
                          set(re.findall(r"REQUIERE LIBERACI[^\n]{0,120}?(S\d\d-[a-z0-9\-]+)", s)))
    d["requiere_liberacion"] = "REQUIERE LIBERACIÓN" in s or "REQUIERE LIBERACION" in s
    d["gate"] = len(re.findall(r"G-A1", s))
    d["carta_f"] = ("Carta F" in s) or ("A7" in s)
    d["secciones"] = [h.strip() for h in re.findall(r"^## (.+)$", s, re.M)]
    return d

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--md", action="store_true"); a = ap.parse_args()
    tabla = {o["ot"]: o for o in json.load(open(os.path.join(aa.ROOT, "ordenes", "tabla-5-1.json"), encoding="utf-8"))["ordenes"]}
    ots = {parse_ot(p)["ot"]: parse_ot(p) for p in sorted(glob.glob(os.path.join(aa.ROOT, "ordenes", "OT-*.md")))}
    faltan = [k for k in tabla if k not in ots]
    # OT que existen en disco pero no en la tabla 5.1 (las «b»: OT-22b, OT-25b...). El bucle de
    # salida lo gobierna la tabla, así que sin esto quedaban INVISIBLES en el mapa: una orden real,
    # con su Δ, que ninguna verificación veía. Un informe que calla no es un informe (mismo fallo
    # que `sensibilidad.sh --solo` en W2). No se funden en la tabla —su Δ no está en la proyección
    # de 5.1— sino que se reportan aparte, con su suma, para que el número siga siendo honesto.
    huerfanas = sorted(k for k in ots if k not in tabla)
    filas = []; tot_delta = 0; por_oleada = collections.Counter(); tags = collections.Counter(); avisos = []
    for k, t in tabla.items():
        d = ots.get(k)
        if not d:
            filas.append((k, t["titulo"], t["estado_plan"], t["delta_objetivo"], "—", t["oleada"], "", "", "", "FALTA")); continue
        aviso = []
        if d["delta"] is not None and d["delta"] != t["delta_objetivo"]:
            aviso.append(f"Δ OT {d['delta']} ≠ tabla {t['delta_objetivo']}")
        if d["oleada"] and t["oleada"] not in ("—",) and d["oleada"] != t["oleada"]:
            aviso.append(f"oleada OT {d['oleada']} ≠ tabla {t['oleada']}")
        if d["sin_etiqueta"]:
            aviso.append("intervenciones sin etiqueta válida: I-" + ",".join(d["sin_etiqueta"]))
        if d["n_inter"] == 0 and t["estado_plan"] != "P":
            aviso.append("sin intervenciones detectadas (formato)")
        tot_delta += t["delta_objetivo"]; por_oleada[t["oleada"]] += t["delta_objetivo"]; tags.update(d["tags"])
        filas.append((k, t["titulo"], t["estado_plan"], t["delta_objetivo"], d["delta"], t["oleada"], d["escritor"], d["n_inter"],
                      "+".join(f"{v}{x[:3]}" for x, v in sorted(d["tags"].items())), "; ".join(aviso) + (" · LIBERAR: " + ",".join(d["liberar"]) if d["liberar"] else (" · REQUIERE LIBERACIÓN (ver OT)" if d["requiere_liberacion"] else ""))))
    if a.md:
        print("| OT | Capítulo | Estado | Δ tabla | Δ OT | Oleada | Escritor | Interv. | Etiquetas | Avisos |")
        print("|---|---|---|---:|---:|---|---|---:|---|---|")
        for f in filas: print("| " + " | ".join(str(x) if x is not None else "—" for x in f) + " |")
        print(f"\n**Σ Δ tabla 5.1 = {tot_delta:+,} palabras** → proyección {62750 + tot_delta:,} (sin reserva). Por oleada: " +
              ", ".join(f"{k}: {v:+,}" for k, v in sorted(por_oleada.items())) + f". Etiquetas: {dict(tags)}. OT que faltan: {faltan or 'ninguna'}.")
        if huerfanas:
            dh = sum(ots[k]["delta"] or 0 for k in huerfanas)
            print(f"\n**OT fuera de la tabla 5.1** ({len(huerfanas)}): " +
                  ", ".join(f"{k} (Δ {ots[k]['delta']:+,})" if ots[k]["delta"] is not None else f"{k} (Δ —)" for k in huerfanas) +
                  f". **Σ Δ fuera de tabla = {dh:+,}** → proyección total {62750 + tot_delta + dh:,}.")
    else:
        for f in filas: print("\t".join(str(x) for x in f))
        for k in huerfanas:
            d = ots[k]
            print("\t".join([k, "(fuera de tabla 5.1)", "", "—", str(d["delta"]), d["oleada"] or "", d["escritor"] or "", str(d["n_inter"]), "", ""]))
        print("Σ Δ", tot_delta, "faltan", faltan, "fuera de tabla", huerfanas)

if __name__ == "__main__":
    main()
