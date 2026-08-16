#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M9 · Guardia de protegidos. Lee protegidos/spans.json.
  baseline [--rebaseline --gate "motivo"]  calcula hashes → protegidos/hashes.json (aditivo; --rebaseline recalcula existentes, exige gate)
  verificar [--staged]                     compara; exit 1 si hay violaciones. --staged lee del índice de git.
  listar                                   muestra ficheros y spans con estado
Reglas: fichero 'total' → hash SHA-256 del fichero completo Y del cuerpo. Span → SHA-256 del texto verbatim.
"""
import sys, os, json, argparse, subprocess, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

SPANS = os.path.join(aa.PROTEGIDOS, "spans.json")
HASHES = os.path.join(aa.PROTEGIDOS, "hashes.json")
REGISTRO = os.path.join(aa.PROTEGIDOS, "registro-rebaselines.md")

def _leer(relpath, staged=False):
    if staged:
        r = subprocess.run(["git", "show", f":{relpath}"], capture_output=True, cwd=aa.ROOT)
        if r.returncode != 0:
            # no está en el índice: usar working tree
            p = os.path.join(aa.ROOT, relpath)
            return open(p, "rb").read() if os.path.exists(p) else None
        return r.stdout
    p = os.path.join(aa.ROOT, relpath)
    return open(p, "rb").read() if os.path.exists(p) else None

def extraer_span(texto, sp):
    ini = sp["inicio"]; fin = sp.get("fin"); occ = int(sp.get("ocurrencia", 1))
    pos = -1; start = 0
    for _ in range(occ):
        pos = texto.find(ini, start)
        if pos < 0:
            return None, f"inicio no encontrado: {ini[:50]!r}"
        start = pos + 1
    if fin is None:
        return texto[pos:pos + len(ini)], None
    e = texto.find(fin, pos + len(ini)) if fin != ini else pos
    if e < 0:
        return None, f"fin no encontrado tras inicio: {fin[:50]!r}"
    return texto[pos:e + len(fin)], None

def calcular(staged=False):
    cfg = json.load(open(SPANS, encoding="utf-8"))
    out = {"ficheros": {}, "spans": {}, "errores": []}
    for rel in cfg["ficheros_total"]:
        raw = _leer(rel, staged)
        if raw is None:
            out["ficheros"][rel] = None
            continue
        texto = raw.decode("utf-8")
        fm, _, body = aa.parse_frontmatter(texto)
        if fm.get("provisional") is True:
            out["ficheros"][rel] = None   # borrador pendiente de validación de autor: sin hash todavía
            out.setdefault("provisionales", []).append(rel)
            continue
        out["ficheros"][rel] = {"fichero": aa.sha256_text(texto), "cuerpo": aa.sha256_text(body)}
    for sp in cfg["spans"]:
        raw = _leer(sp["archivo"], staged)
        if raw is None:
            out["errores"].append(f"{sp['id']}: fichero inexistente {sp['archivo']}"); continue
        texto = raw.decode("utf-8")
        span, err = extraer_span(texto, sp)
        if err:
            out["errores"].append(f"{sp['id']} ({sp['archivo']}): {err}"); continue
        out["spans"][sp["id"]] = {"archivo": sp["archivo"], "hash": aa.sha256_text(span), "longitud": len(span)}
    return cfg, out

def cmd_baseline(args):
    cfg, act = calcular()
    if act["errores"]:
        for e in act["errores"]: print("ERROR:", e)
        sys.exit("baseline abortado: corrige spans.json")
    prev = json.load(open(HASHES, encoding="utf-8")) if os.path.exists(HASHES) else {"ficheros": {}, "spans": {}}
    if args.rebaseline:
        if not args.gate:
            sys.exit("--rebaseline exige --gate \"motivo/gate\"")
        with open(REGISTRO, "a", encoding="utf-8") as f:
            f.write(f"- {datetime.datetime.now().isoformat(timespec='seconds')} · rebaseline · {args.gate}\n")
        nuevo = {"ficheros": act["ficheros"], "spans": act["spans"]}
    else:
        nuevo = {"ficheros": dict(prev.get("ficheros", {})), "spans": dict(prev.get("spans", {}))}
        for k, v in act["ficheros"].items():
            if k not in nuevo["ficheros"] or nuevo["ficheros"][k] is None:
                nuevo["ficheros"][k] = v
        for k, v in act["spans"].items():
            if k not in nuevo["spans"]:
                nuevo["spans"][k] = v
    nuevo["generado"] = datetime.datetime.now().isoformat(timespec="seconds")
    with open(HASHES, "w", encoding="utf-8") as f:
        json.dump(nuevo, f, ensure_ascii=False, indent=2); f.write("\n")
    n_f = sum(1 for v in nuevo["ficheros"].values() if v)
    print(f"baseline escrito: {n_f} ficheros totales, {len(nuevo['spans'])} spans → {os.path.relpath(HASHES, aa.ROOT)}")
    faltan = [k for k, v in nuevo["ficheros"].items() if not v]
    if faltan:
        print("AVISO ficheros protegidos sin hash (inexistentes o provisional: true):", ", ".join(faltan))

def cmd_verificar(args):
    if not os.path.exists(HASHES):
        sys.exit("No hay baseline: ejecuta 'proteger.sh baseline'.")
    ref = json.load(open(HASHES, encoding="utf-8"))
    cfg, act = calcular(staged=args.staged)
    viol = list(act["errores"])
    for rel, h in ref["ficheros"].items():
        if h is None:
            continue
        a = act["ficheros"].get(rel)
        if a is None:
            viol.append(f"fichero protegido desaparecido: {rel}")
        elif a["fichero"] != h["fichero"]:
            if a["cuerpo"] == h["cuerpo"]:
                viol.append(f"{rel}: frontmatter alterado (cuerpo intacto). Los ficheros 'total' exigen rebaseline con gate incluso para metadatos.")
            else:
                viol.append(f"{rel}: CUERPO ALTERADO (proteccion: total, diff debe ser 0)")
    for sid, h in ref["spans"].items():
        a = act["spans"].get(sid)
        if a is None:
            viol.append(f"span {sid}: no localizable en {h['archivo']} (¿texto protegido modificado o movido?)")
        elif a["hash"] != h["hash"]:
            viol.append(f"span {sid} ({h['archivo']}): TEXTO PROTEGIDO ALTERADO")
    for rel in cfg["ficheros_total"]:
        if rel not in ref["ficheros"] or ref["ficheros"][rel] is None:
            if act["ficheros"].get(rel):
                print(f"AVISO: {rel} existe pero no tiene baseline; ejecuta 'proteger.sh baseline'.")
    for rel in act.get("provisionales", []):
        print(f"AVISO: {rel} es provisional (pendiente de validación de autor): sin hash.")
    for sp in cfg["spans"]:
        if sp["id"] not in ref["spans"]:
            print(f"AVISO: span {sp['id']} definido sin baseline; ejecuta 'proteger.sh baseline'.")
    if viol:
        print("M9 · VIOLACIONES DE PROTECCIÓN:")
        for v in viol: print("  ✗", v)
        sys.exit(1)
    print(f"M9 OK · {sum(1 for v in ref['ficheros'].values() if v)} ficheros íntegros · {len(ref['spans'])} spans íntegros")

def cmd_listar(args):
    cfg, act = calcular()
    for rel, v in act["ficheros"].items():
        print(f"TOTAL  {rel:28} {'ok' if v else 'INEXISTENTE'}")
    for sp in cfg["spans"]:
        v = act["spans"].get(sp["id"])
        print(f"SPAN   {sp['id']:18} {sp['archivo']:22} {v['longitud'] if v else 'ERROR':>6}  {sp['desc'][:60]}")
    for e in act["errores"]: print("ERROR:", e)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("baseline"); p.add_argument("--rebaseline", action="store_true"); p.add_argument("--gate")
    p = sub.add_parser("verificar"); p.add_argument("--staged", action="store_true")
    sub.add_parser("listar")
    a = ap.parse_args()
    {"baseline": cmd_baseline, "verificar": cmd_verificar, "listar": cmd_listar}[a.cmd](a)

if __name__ == "__main__":
    main()
