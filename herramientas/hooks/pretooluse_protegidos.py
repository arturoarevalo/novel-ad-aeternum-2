#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lógica del hook PreToolUse (ver pretooluse-protegidos.sh). Lee el JSON del hook por stdin; argv[1] = raíz del proyecto."""
import sys, json, os, re

root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
tool = data.get("tool_name", "")
ti = data.get("tool_input", {}) or {}

def cargar_protegidos():
    p = os.path.join(root, "protegidos", "spans.json")
    try:
        tot = json.load(open(p, encoding="utf-8")).get("ficheros_total", [])
    except Exception:
        tot = []
    return [os.path.normpath(os.path.join(root, t)) for t in tot]

def tiene_proteccion_total(path):
    try:
        with open(path, encoding="utf-8") as f:
            head = f.read(2000)
        return bool(re.search(r"^proteccion:\s*total\s*$", head, re.M))
    except Exception:
        return False

def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                      "permissionDecision": "deny", "permissionDecisionReason": reason}}, ensure_ascii=False))
    sys.exit(0)

protegidos = cargar_protegidos()
manifiesto = os.path.normpath(os.path.join(root, "biblia", "metadatos.json"))
hashes = os.path.normpath(os.path.join(root, "protegidos", "hashes.json"))

if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
    fp = ti.get("file_path") or ti.get("notebook_path") or ""
    if not fp:
        sys.exit(0)
    ap = os.path.normpath(fp if os.path.isabs(fp) else os.path.join(root, fp))
    if ap in protegidos or tiene_proteccion_total(ap):
        deny(f"BLOQUEADO (M9): {os.path.relpath(ap, root)} tiene proteccion: total (Apéndice A). Diff debe ser 0; "
             f"solo ortotipografía aprobada en gate de autor, y entonces vía Bash con AA_GATE_AUTOR=\"motivo\" y rebaseline.")
    if ap == manifiesto:
        deny("BLOQUEADO: biblia/metadatos.json solo se modifica vía herramientas/actualizar-metadatos.sh (§2.4).")
    if ap == hashes:
        deny("BLOQUEADO: protegidos/hashes.json solo lo escribe herramientas/proteger.sh baseline.")
    sys.exit(0)

if tool == "Bash":
    cmd = ti.get("command", "") or ""
    if re.match(r'^\s*AA_GATE_AUTOR=', cmd):
        sys.exit(0)   # excepción explícita de gate de autor; el pre-commit (M9) sigue vigilando
    nombres = [os.path.basename(p) for p in protegidos] + ["metadatos.json", "hashes.json"]
    menciona = [n for n in nombres if n in cmd]
    if not menciona:
        sys.exit(0)
    alt = "|".join(re.escape(n) for n in menciona)
    escritura = re.compile(
        r"(\bsed\s+(-[a-zA-Z]*i|--in-place)|\bperl\s+-\S*i\S*\s|open\([^)]*['\"][wa]|"
        r">\s*\S*(" + alt + r")|>>\s*\S*(" + alt + r")|\btee\s+(-a\s+)?\S*(" + alt + r")|"
        r"\b(mv|cp|rm|truncate|install|ln)\b[^|;&]*(" + alt + r"))")
    oficial = re.search(r"herramientas/(actualizar-metadatos\.sh|proteger\.sh|inyectar-frontmatter\.sh|compilar\.sh|medir\.sh)", cmd)
    if escritura.search(cmd):
        deny("BLOQUEADO (M9): el comando parece escribir sobre un fichero protegido / el manifiesto / los hashes (" +
             ", ".join(menciona) + "). Usa las herramientas oficiales (actualizar-metadatos.sh, proteger.sh); "
             "para excepciones aprobadas en gate de autor, prefija AA_GATE_AUTOR=\"motivo\".")
    if oficial:
        sys.exit(0)
    sys.exit(0)
sys.exit(0)
