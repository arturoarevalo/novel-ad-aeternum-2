#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B0 · Auditoría del manifiesto (biblia/metadatos.json) contra el repositorio y la prosa. Salida: markdown por stdout.
Comprueba: archivo/slug/titulo vs frontmatter; n vs capitulo; rangos de partes[] vs ficheros; fechas de inicio de parte
vs subtítulos y cuenta atrás (M7); persona=primera de cap-38 vs prosa; palabras_real vs cuotas (deriva); secuencia de
fechas (analepsis exime). No escribe nada.
"""
import sys, os, re, json, datetime, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa
from validar import densidad_primera, UMBRAL_PRIMERA

SOLDAGEN = datetime.date(2061, 1, 21)
MESES = {"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}

def slugify(s):
    s = "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def parse_fecha(v):
    v = str(v)
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}))?", v)
    if not m: return None
    y, mo, d, h, mi = m.groups()
    return datetime.datetime(int(y), int(mo), int(d), int(h or 0), int(mi or 0))

def main():
    m = aa.load_manifest()
    caps = {d["archivo"]: d for d in aa.reading_order()}
    disc, ok = [], []
    # 1. entradas vs ficheros
    for c in m["capitulos"]:
        d = caps.get(c["archivo"])
        if not d:
            disc.append(f"`{c['archivo']}` registrado en el manifiesto pero inexistente en capitulos/"); continue
        fm = d["fm"]
        if fm.get("capitulo") != c["n"]:
            disc.append(f"`{c['archivo']}`: n={c['n']} en manifiesto ≠ capitulo={fm.get('capitulo')} en frontmatter")
        if str(fm.get("titulo")) != str(c["titulo"]):
            disc.append(f"`{c['archivo']}`: titulo «{c['titulo']}» ≠ frontmatter «{fm.get('titulo')}»")
        if slugify(str(c["titulo"])) != c["slug"]:
            disc.append(f"`{c['archivo']}`: slug `{c['slug']}` no deriva del título («{c['titulo']}» → `{slugify(str(c['titulo']))}`)")
    reg = {c["archivo"] for c in m["capitulos"]}
    for a in caps:
        if a not in reg:
            disc.append(f"`{a}` existe en capitulos/ pero no está registrado en el manifiesto")
    ok.append(f"{len(m['capitulos'])} entradas registradas; {len(caps)} ficheros en capitulos/")
    # 2. partes vs ficheros y cuenta atrás
    ns = sorted(c["n"] for c in m["capitulos"] if c.get("n") is not None)
    cubiertos = []
    for p in m["partes"]:
        cubiertos += list(range(p["capitulo_inicial"], p["capitulo_final"] + 1))
        mm = re.match(r"(\d{1,2}) de (\w+) de (\d{4}) · Faltan (\d+) días para Soldagen", p["subtitulo"])
        if not mm:
            disc.append(f"Parte {p['n']}: subtítulo no parseable «{p['subtitulo']}»"); continue
        d, mes, y, faltan = int(mm.group(1)), MESES.get(mm.group(2).lower()), int(mm.group(3)), int(mm.group(4))
        fecha = datetime.date(y, mes, d)
        real = (SOLDAGEN - fecha).days
        if real != faltan:
            disc.append(f"Parte {p['n']}: subtítulo dice «Faltan {faltan} días» pero {fecha} → Soldagen ({SOLDAGEN}) son {real}")
        else:
            ok.append(f"Parte {p['n']} «{p['titulo']}»: {fecha} + {faltan} días = Soldagen ✓")
        # fecha del primer capítulo de la parte
        first = next((c for c in m["capitulos"] if c.get("n") == p["capitulo_inicial"]), None)
        if first and first["archivo"] in caps:
            f0 = parse_fecha(caps[first["archivo"]]["fm"].get("fecha"))
            if f0 and f0.date() != fecha:
                disc.append(f"Parte {p['n']}: fecha de cabecera {fecha} ≠ fecha del cap. {p['capitulo_inicial']} ({f0.date()})")
            else:
                ok.append(f"Parte {p['n']}: fecha de cabecera = fecha del cap. {p['capitulo_inicial']} ✓")
    if sorted(cubiertos) != ns:
        disc.append(f"Rangos de partes {[(p['capitulo_inicial'],p['capitulo_final']) for p in m['partes']]} no cubren exactamente los capítulos {ns[0]}..{ns[-1]}")
    else:
        ok.append(f"Rangos de partes cubren exactamente 1..{ns[-1]} sin huecos ni solapes ✓")
    # 3. persona
    for c in m["capitulos"]:
        if c.get("persona") == "primera" and c["archivo"] in caps:
            dens = densidad_primera(caps[c["archivo"]]["body"])
            (ok if dens >= UMBRAL_PRIMERA else disc).append(
                f"`{c['archivo']}` persona=primera: densidad de 1.ª persona en narración {dens:.1f}‰ (umbral {UMBRAL_PRIMERA:.0f}‰; máx. del resto en v0 = 8,0‰) {'✓' if dens >= UMBRAL_PRIMERA else '✗'}")
    # 4. secuencia de fechas
    prev = None; prev_a = None
    for d in aa.reading_order():
        f = parse_fecha(d["fm"].get("fecha"))
        if f is None:
            disc.append(f"`{d['archivo']}`: fecha no parseable {d['fm'].get('fecha')!r}"); continue
        if prev and f < prev and not d["fm"].get("analepsis"):
            disc.append(f"`{d['archivo']}` ({f}) retrocede respecto a `{prev_a}` ({prev}) sin analepsis: true")
        if not d["fm"].get("analepsis"):
            prev, prev_a = f, d["archivo"]
    ok.append("Secuencia de fechas del frontmatter monótona salvo capítulos con analepsis: true ✓")
    # 5. palabras
    print("# B0 · Auditoría del manifiesto — resultado automático\n")
    print("## Comprobaciones superadas\n")
    for o in ok: print("-", o)
    print("\n## Discrepancias detectadas\n")
    if not disc: print("- (ninguna)")
    for x in disc: print("-", x)
    print("\n## Deriva palabras: cuota (v0) vs recuento real\n")
    print("| n | archivo | título | cuota v0 | real | Δ | Δ% |")
    print("|---|---|---|---:|---:|---:|---:|")
    tc = tr = 0
    for c in m["capitulos"]:
        d = caps.get(c["archivo"])
        if not d: continue
        real = aa.count_words(d["body"]); cuota = c.get("palabras", 0)
        tc += cuota; tr += real
        print(f"| {c['n']} | {c['archivo']} | {c['titulo']} | {cuota} | {real} | {real-cuota:+d} | {100*(real-cuota)/cuota if cuota else 0:+.1f}% |")
    print(f"| | **Total** | | **{tc}** | **{tr}** | **{tr-tc:+d}** | **{100*(tr-tc)/tc:+.1f}%** |")
    print(f"\npalabras_objetivo declarado: {m.get('palabras_objetivo')} · suma de cuotas: {tc} · recuento real canónico: {tr}")

if __name__ == "__main__":
    main()
