#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Librería común de herramientas del proyecto «Ad aeternum» (plan de revisión-expansión).
Solo stdlib. Usada por: actualizar-metadatos, proteger (M9), compilar, medir (M1–M10), validadores.

Convenciones (§2.4 del plan):
- Frontmatter YAML plano (clave: valor) entre dos líneas '---' al inicio del fichero.
- El cuerpo es todo lo que sigue al segundo '---'.
- Recuento canónico de palabras: cuerpo sin frontmatter, marcado markdown eliminado
  (*, _, `, #, >), tokens separados por espacio que contengan al menos un carácter
  alfanumérico (excluye rayas sueltas, dinkus «* * *», comillas huérfanas).
"""
import json, os, re, subprocess, sys, hashlib

def root():
    env = os.environ.get("AA_ROOT")
    if env:
        return env
    try:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True)
        return r.stdout.strip()
    except Exception:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ROOT = root()
CAPITULOS = os.path.join(ROOT, "capitulos")
BIBLIA = os.path.join(ROOT, "biblia")
MANIFIESTO = os.path.join(BIBLIA, "metadatos.json")
PROTEGIDOS = os.path.join(ROOT, "protegidos")
INFORMES = os.path.join(ROOT, "informes")
COMPILADO = os.path.join(ROOT, "compilado")

CAMPOS_AUTOR_MANIFIESTO = ["titulo", "subtitulo", "autor", "dedicatoria", "sinopsis_corta",
                           "dinkus", "letras-capitales", "idioma", "slug", "publicacion"]
CAMPOS_AUTOR_FRONTMATTER = ["capitulo", "titulo", "pov", "fecha", "estado", "analepsis"]
CAMPOS_PLAN_FRONTMATTER = ["estado_plan", "proteccion", "ot", "delta_objetivo", "orden_lectura"]

# ---------------------------------------------------------------- frontmatter
_FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", re.S)

def _parse_scalar(v):
    v = v.strip()
    if v == "":
        return ""
    if (v[0] == v[-1]) and v[0] in "\"'" and len(v) >= 2:
        return v[1:-1]
    low = v.lower()
    # YAML 1.2: solo true/false son booleanos. `yes`/`no` son cadenas — y aquí importa, porque
    # `proteccion: no` es un valor legítimo del frontmatter del plan (§2.4) y con YAML 1.1 se
    # convertía en False y el validador lo rechazaba. Los campos booleanos del repo (analepsis,
    # provisional) se escriben siempre true/false, así que no hay ambigüedad.
    if low == "true":
        return True
    if low == "false":
        return False
    if low in ("null", "~"):
        return None
    if re.fullmatch(r"[+-]?\d+", v):
        return int(v)
    if re.fullmatch(r"[+-]?\d+\.\d+", v):
        return float(v)
    return v

def parse_frontmatter(text):
    """Devuelve (fm:dict, fm_lines:list[str] crudas, body:str). Si no hay frontmatter: ({}, [], text)."""
    m = _FM_RE.match(text)
    if not m:
        return {}, [], text
    raw = m.group(1)
    body = m.group(2)
    fm = {}
    lines = raw.split("\n")
    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = _parse_scalar(v)
    return fm, lines, body

def read_chapter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm, lines, body = parse_frontmatter(text)
    return fm, lines, body, text

def format_scalar(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "null"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if s == "" or re.search(r"[:#]", s) or s.strip() != s or s.lower() in ("true", "false", "null", "yes", "no"):
        return '"' + s.replace('"', '\\"') + '"'
    return s

def build_file(fm_lines, body):
    return "---\n" + "\n".join(fm_lines) + "\n---\n" + body

# ---------------------------------------------------------------- texto
_DINKUS_RE = re.compile(r"^\s*(\*\s*\*\s*\*|\* \* \*|\*\*\*|—\s*—\s*—)\s*$")

def es_dinkus(line):
    return bool(_DINKUS_RE.match(line))

def strip_markdown(text):
    t = re.sub(r"^\s{0,3}#{1,6}\s+", "", text, flags=re.M)      # cabeceras
    t = re.sub(r"^\s{0,3}>\s?", "", t, flags=re.M)             # citas
    t = t.replace("`", "")
    t = re.sub(r"(\*\*|__)", "", t)
    t = re.sub(r"(?<!\w)[*_](?=\S)|(?<=\S)[*_](?!\w)", "", t)  # cursivas
    return t

_WORD_RE = re.compile(r"\w", re.U)

def count_words(body):
    body_sin_dinkus = "\n".join(l for l in body.split("\n") if not es_dinkus(l))
    toks = strip_markdown(body_sin_dinkus).split()
    return sum(1 for tk in toks if _WORD_RE.search(tk))

def split_scenes(body):
    """Divide el cuerpo por dinkus. Devuelve lista de escenas (str), sin vacías."""
    scenes, cur = [], []
    for line in body.split("\n"):
        if es_dinkus(line):
            scenes.append("\n".join(cur)); cur = []
        else:
            cur.append(line)
    scenes.append("\n".join(cur))
    return [s for s in scenes if s.strip()]

def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

def sentences(text):
    t = strip_markdown(text)
    parts = re.split(r"(?<=[.!?…»])\s+(?=[—«¿¡\"'(\[A-ZÁÉÍÓÚÑÜ0-9])", t)
    return [p.strip() for p in parts if p.strip()]

def es_dialogo(par):
    return par.lstrip().startswith(("—", "–", "―"))

# ---------------------------------------------------------------- manifiesto
def load_manifest(path=MANIFIESTO):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def dump_manifest(m, path=MANIFIESTO):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
        f.write("\n")

def chapter_paths():
    # El glob antiguo era r"cap-(\d{2}|n\d)\.md" y NO VEÍA los capítulos nuevos de W10
    # (`cap-w1.md`). Un capítulo invisible para esta función es invisible para el compilador,
    # las métricas, M9, M8 y el validador — Y TODOS INFORMABAN «OK» —, porque todos preguntan
    # aquí. Es el modo de fallo de la casa: silencioso y tranquilizador. Ahora se acepta
    # cualquier `cap-<token>.md`; el orden lo gobierna `orden_lectura`, no el nombre.
    files = sorted(f for f in os.listdir(CAPITULOS) if re.fullmatch(r"cap-[a-z0-9]+\.md", f))
    return [os.path.join(CAPITULOS, f) for f in files]

def reading_order():
    """Lista de dicts {path, archivo, fm, body, orden} ordenada por orden_lectura (o capitulo)."""
    out = []
    for p in chapter_paths():
        fm, lines, body, text = read_chapter(p)
        orden = fm.get("orden_lectura", fm.get("capitulo"))
        try:
            orden = float(orden)
        except Exception:
            orden = 9999.0
        out.append({"path": p, "archivo": os.path.basename(p), "fm": fm, "fm_lines": lines,
                    "body": body, "orden": orden})
    out.sort(key=lambda d: d["orden"])
    return out

def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def parte_de(orden, manifest):
    for p in manifest["partes"]:
        if p["capitulo_inicial"] <= orden <= p["capitulo_final"] + 0.9999:
            return p["n"]
    return None

if __name__ == "__main__":
    # Autotest mínimo
    for d in reading_order():
        print(d["archivo"], d["orden"], count_words(d["body"]))
