#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilador (§2.4): lee el manifiesto + orden_lectura, genera cabeceras de parte desde partes[], numera los capítulos
por orden de lectura (1..N), elimina el frontmatter, EXCLUYE título/dedicatoria/sinopsis y toda metainformación,
incluye los paratextos (aviso al inicio, recursos al final) y escribe compilado/ad-aeternum-<etiqueta>.md. Reporta M8.

Uso: compilar.py <etiqueta> [--sin-paratextos] [--sin-numeros] [--salida RUTA]
"""
import sys, os, json, argparse, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

ROMANOS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("etiqueta")
    ap.add_argument("--con-portada", action="store_true",
        help="antepone titulo y autor del manifiesto. Los seis editores de adquisiciones de W10 "
             "pidieron «decidir el titulo» porque este compilador lo EXCLUIA a proposito: leyeron "
             "un manuscrito que empezaba con el aviso de contenido, sin portada. Una de las seis "
             "condiciones de compra no era del libro, era del compilador.")
    ap.add_argument("--sin-paratextos", action="store_true")
    ap.add_argument("--sin-numeros", action="store_true")
    ap.add_argument("--salida")
    a = ap.parse_args()
    m = aa.load_manifest()
    dinkus = m.get("dinkus", "* * *")
    orden = aa.reading_order()
    partes = sorted(m["partes"], key=lambda p: p["capitulo_inicial"])
    out = []
    if getattr(a, "con_portada", False):
        # Los seis editores de adquisiciones de W10 pidieron «decidir el título» — y leyeron un
        # manuscrito que empezaba con el aviso de contenido, porque este compilador excluía el
        # título a propósito (§5 de la cabecera). Una de las seis condiciones de compra no era
        # del libro: era del compilador.
        t = m.get("titulo", ""); sub = m.get("subtitulo", ""); aut = m.get("autor", "")
        out.append(f"# {t}\n")
        if sub: out.append(f"*{sub}*\n")
        if aut: out.append(f"{aut}\n")
        out.append("")
    total = 0
    por_parte = {}
    # paratexto inicial
    paratextos = m.get("paratextos", [])
    def leer_paratexto(pos):
        for pt in paratextos:
            if pt.get("posicion") == pos:
                p = os.path.join(aa.CAPITULOS, pt["archivo"])
                if os.path.exists(p):
                    fm, _, body, _ = aa.read_chapter(p)
                    return fm, body.strip()
        return None, None
    if not a.sin_paratextos:
        fm, body = leer_paratexto("inicio")
        if body:
            out.append(f"## {fm.get('titulo','Aviso')}\n\n{body}\n")
    parte_actual = None
    n = 0
    for d in orden:
        n += 1
        pn = aa.parte_de(d["orden"], m)
        if pn != parte_actual:
            parte_actual = pn
            p = next(x for x in partes if x["n"] == pn)
            out.append(f"\n# {ROMANOS.get(pn, pn)}. {p['titulo']}\n\n*{p['subtitulo']}*\n")
        titulo = d["fm"].get("titulo", "")
        cab = f"## {titulo}" if a.sin_numeros else f"## {n}. {titulo}"
        body = d["body"].strip("\n")
        # normalizar dinkus al del manifiesto
        lines = [dinkus if aa.es_dinkus(l) else l for l in body.split("\n")]
        out.append(f"\n{cab}\n\n" + "\n".join(lines) + "\n")
        w = aa.count_words(d["body"]); total += w
        por_parte[pn] = por_parte.get(pn, 0) + w
    if not a.sin_paratextos:
        fm, body = leer_paratexto("fin")
        if body:
            out.append(f"\n## {fm.get('titulo','Recursos')}\n\n{body}\n")
    texto = "\n".join(out)
    salida = a.salida or os.path.join(aa.COMPILADO, f"ad-aeternum-{a.etiqueta}.md")
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    with open(salida, "w", encoding="utf-8") as f:
        f.write(texto)
    # M8
    objetivo = int(m.get("palabras_objetivo", 0)); banda = 1000
    en_banda = (objetivo - banda) <= total <= (objetivo + banda)
    m8 = {"etiqueta": a.etiqueta, "fecha": datetime.datetime.now().isoformat(timespec="seconds"),
          "capitulos": n, "palabras": total, "por_parte": por_parte, "objetivo": objetivo,
          "banda": [objetivo - banda, objetivo + banda], "en_banda": en_banda, "salida": os.path.relpath(salida, aa.ROOT)}
    os.makedirs(aa.INFORMES, exist_ok=True)
    with open(os.path.join(aa.INFORMES, f"m8-{a.etiqueta}.json"), "w", encoding="utf-8") as f:
        json.dump(m8, f, ensure_ascii=False, indent=2)
    print(f"compilado → {m8['salida']} · {n} capítulos · {total} palabras (por parte: {por_parte})")
    print(f"M8: objetivo {objetivo} ± {banda} → {'EN BANDA ✓' if en_banda else f'FUERA DE BANDA ({total - objetivo:+d})'}")

if __name__ == "__main__":
    main()
