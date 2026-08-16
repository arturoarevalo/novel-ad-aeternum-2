#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inyecta/actualiza en el frontmatter de capitulos/*.md los campos del PLAN (§2.4):
  estado_plan, proteccion, ot, delta_objetivo, orden_lectura
a partir de ordenes/tabla-5-1.json. NUNCA toca campos del autor (capitulo, titulo, pov, fecha, estado,
analepsis, persona…): sus líneas se copian byte a byte. Idempotente. El cuerpo se copia byte a byte.

Uso: inyectar_frontmatter.py [--solo cap-08.md ...] [--dry-run]
     inyectar_frontmatter.py --set cap-08.md estado=en_oleada    (cambia SOLO 'estado' u otro campo del plan)
"""
import sys, os, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

TABLA = os.path.join(aa.ROOT, "ordenes", "tabla-5-1.json")
ORDEN_CAMPOS = ["estado_plan", "proteccion", "ot", "delta_objetivo", "orden_lectura"]
CAMPOS_MODIFICABLES = set(ORDEN_CAMPOS) | {"estado"}   # 'estado' (autor) solo cambia de valor según ciclo de vida §2.4

def _fmt(k, v):
    if k == "delta_objetivo":
        v = int(v)
        return f"{k}: {'+' if v > 0 else ''}{v}"
    if k == "orden_lectura":
        return f"{k}: {int(v) if float(v).is_integer() else v}"
    return f"{k}: {aa.format_scalar(v)}"

def aplicar(path, valores, dry=False):
    fm, lines, body, text = aa.read_chapter(path)
    if not lines:
        sys.exit(f"{path}: sin frontmatter")
    nuevas, vistos = [], set()
    for line in lines:
        k = line.split(":", 1)[0].strip() if ":" in line else None
        if k in valores:
            nuevas.append(_fmt(k, valores[k])); vistos.add(k)
        else:
            nuevas.append(line)
    for k in ORDEN_CAMPOS:
        if k in valores and k not in vistos:
            nuevas.append(_fmt(k, valores[k]))
    for k in valores:
        if k not in vistos and k not in ORDEN_CAMPOS:
            nuevas.append(_fmt(k, valores[k]))
    out = aa.build_file(nuevas, body)
    if out != text and not dry:
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
    return out != text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--set", nargs=2, metavar=("ARCHIVO", "CLAVE=VALOR"))
    a = ap.parse_args()
    if a.set:
        archivo, kv = a.set
        k, v = kv.split("=", 1)
        if k not in CAMPOS_MODIFICABLES:
            sys.exit(f"campo no modificable por esta herramienta: {k}")
        p = os.path.join(aa.CAPITULOS, os.path.basename(archivo))
        ch = aplicar(p, {k: aa._parse_scalar(v)}, a.dry_run)
        print(f"{archivo}: {k}={v} {'(cambiado)' if ch else '(sin cambios)'}")
        return
    tabla = json.load(open(TABLA, encoding="utf-8"))["ordenes"]
    n = 0
    for o in tabla:
        p = os.path.join(aa.CAPITULOS, o["archivo"])
        if a.solo and o["archivo"] not in a.solo:
            continue
        if not os.path.exists(p):
            continue   # capítulos nuevos aún no escritos
        vals = {"estado_plan": o["estado_plan"], "proteccion": o["proteccion"], "ot": o["ot"],
                "delta_objetivo": o["delta_objetivo"], "orden_lectura": o["orden_lectura"]}
        ch = aplicar(p, vals, a.dry_run)
        n += ch
        print(f"{o['archivo']}: {'actualizado' if ch else 'sin cambios'}")
    print(f"{n} ficheros {'que cambiarían' if a.dry_run else 'modificados'}")

if __name__ == "__main__":
    main()
