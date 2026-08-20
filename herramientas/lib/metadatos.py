#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Única vía de escritura de los campos OPERATIVOS de biblia/metadatos.json (§2.4 del plan).
Campos de AUTOR (titulo, subtitulo, autor, dedicatoria, sinopsis_corta, dinkus, letras-capitales,
idioma, slug, publicacion) — INTOCABLES: el script aborta si el resultado los altera, salvo
--gate-autor "<motivo>" (queda registrado en informes/registro-gates-autor.md).

Subcomandos:
  palabras-real                 recalcula palabras_real por capítulo (recuento canónico, sin frontmatter)
  objetivo N --gate-autor M     fija palabras_objetivo (decisión de autor)
  presupuestos [--v0]           palabras := palabras_real + delta_objetivo (delta leído del frontmatter);
                                con --v0, palabras_real se toma del recuento del tag v0 (git show v0:...)
  registrar ARCHIVO             registra un capítulo nuevo (solo tras G-A2), origen "REVISIÓN 10"
  renumerar --w7 --gate-autor M renumera capitulo/rangos de partes (UNA vez, en W7)
  verificar [--v0-ref]          invariantes: JSON válido, campos autor == tag v0, archivos existen,
                                capitulos[] coincide con capitulos/ (salvo nuevos no registrados)
  mostrar                       resumen tabular
"""
import sys, os, json, subprocess, argparse, datetime, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

def _git_show(ref, relpath):
    r = subprocess.run(["git", "show", f"{ref}:{relpath}"], capture_output=True, text=True, cwd=aa.ROOT)
    if r.returncode != 0:
        return None
    return r.stdout

def _autor_snapshot(m):
    return {k: m.get(k) for k in aa.CAMPOS_AUTOR_MANIFIESTO}

def _registrar_gate(motivo, accion):
    os.makedirs(aa.INFORMES, exist_ok=True)
    p = os.path.join(aa.INFORMES, "registro-gates-autor.md")
    nuevo = not os.path.exists(p)
    with open(p, "a", encoding="utf-8") as f:
        if nuevo:
            f.write("# Registro de gates de autor (cambios en campos de autor / decisiones de autor)\n\n")
        f.write(f"- {datetime.datetime.now().isoformat(timespec='seconds')} · {accion} · motivo: {motivo}\n")

def _guardar(m, antes, gate_autor=None, accion=""):
    despues = _autor_snapshot(m)
    if despues != antes:
        if not gate_autor:
            sys.exit("ABORTADO: la operación alteraría campos de AUTOR del manifiesto sin --gate-autor.")
        _registrar_gate(gate_autor, accion)
    aa.dump_manifest(m)

def _capitulos_reales():
    out = {}
    for d in aa.reading_order():
        out[d["archivo"]] = d
    return out

def cmd_palabras_real(args):
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    reales = _capitulos_reales()
    for c in m["capitulos"]:
        d = reales.get(c["archivo"])
        if d is None:
            print(f"AVISO: {c['archivo']} registrado pero no existe en capitulos/", file=sys.stderr); continue
        c["palabras_real"] = aa.count_words(d["body"])
    _guardar(m, antes)
    total = sum(c.get("palabras_real", 0) for c in m["capitulos"])
    print(f"palabras_real actualizado en {len(m['capitulos'])} capítulos · total {total}")

def cmd_objetivo(args):
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    if not args.gate_autor:
        sys.exit("palabras_objetivo es decisión de autor: requiere --gate-autor \"motivo\".")
    viejo = m.get("palabras_objetivo")
    m["palabras_objetivo"] = int(args.n)
    _registrar_gate(args.gate_autor, f"palabras_objetivo {viejo} → {args.n}")
    _guardar(m, antes)
    print(f"palabras_objetivo: {viejo} → {args.n}")

def cmd_presupuestos(args):
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    reales = _capitulos_reales()
    cambios = []
    for c in m["capitulos"]:
        d = reales.get(c["archivo"])
        if d is None:
            continue
        delta = d["fm"].get("delta_objetivo", 0)
        try:
            delta = int(str(delta).replace("+", ""))
        except Exception:
            delta = 0
        if args.v0:
            texto = _git_show("v0", f"capitulos/{c['archivo']}")
            if texto is None:
                base = c.get("palabras_real")
            else:
                _, _, body = aa.parse_frontmatter(texto)
                base = aa.count_words(body)
        else:
            base = c.get("palabras_real")
        if base is None:
            sys.exit(f"Falta palabras_real en {c['archivo']}: ejecuta antes 'palabras-real'.")
        nuevo = int(base) + delta
        cambios.append((c["archivo"], c.get("palabras"), nuevo, base, delta))
        c["palabras"] = nuevo
    _guardar(m, antes)
    for a, v, n, b, dl in cambios:
        print(f"{a}: palabras {v} → {n}  (real_v0 {b} {'+' if dl>=0 else ''}{dl})")
    print("suma presupuestos:", sum(c["palabras"] for c in m["capitulos"]))

def cmd_registrar(args):
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    archivo = os.path.basename(args.archivo)
    if any(c["archivo"] == archivo for c in m["capitulos"]):
        sys.exit(f"{archivo} ya está registrado.")
    p = os.path.join(aa.CAPITULOS, archivo)
    if not os.path.exists(p):
        sys.exit(f"No existe {p}")
    fm, _, body, _ = aa.read_chapter(p)
    if not args.gate:
        sys.exit("Registrar un capítulo nuevo exige haber superado G-A2: pasa --gate \"G-A2 <fecha> <ref>\".")
    titulo = fm.get("titulo")
    slug = re.sub(r"[^a-z0-9]+", "-", _sin_tildes(str(titulo)).lower()).strip("-")
    orden = fm.get("orden_lectura")
    entrada = {"n": None, "slug": slug, "titulo": titulo, "archivo": archivo,
               "palabras": int(str(fm.get("delta_objetivo", 0)).replace("+", "")),
               "palabras_real": aa.count_words(body), "origen": "REVISIÓN 10",
               "orden_lectura": orden}
    if fm.get("persona"):
        entrada["persona"] = fm["persona"]
    # insertar en posición de lectura
    caps = m["capitulos"]
    idx = len(caps)
    for i, c in enumerate(caps):
        o = c.get("orden_lectura", c.get("n"))
        if o is not None and float(o) > float(orden):
            idx = i; break
    caps.insert(idx, entrada)
    _registrar_gate(args.gate, f"registrar {archivo} ({titulo}) orden_lectura {orden}")
    _guardar(m, antes)
    print(f"registrado {archivo} en posición {idx} con orden_lectura {orden} (n queda null hasta W7)")

def _sin_tildes(s):
    import unicodedata
    return "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")

def cmd_renumerar(args):
    if not (args.w7 and args.gate_autor):
        sys.exit("renumerar solo en W7 y con --w7 --gate-autor \"motivo\".")
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    orden = aa.reading_order()
    pos = {d["archivo"]: i + 1 for i, d in enumerate(orden)}
    for c in m["capitulos"]:
        c["n"] = pos.get(c["archivo"], c.get("n"))
    m["capitulos"].sort(key=lambda c: c["n"] if c["n"] is not None else 9999)
    # rangos de partes: recalculados por el orden vigente de partes (primer/último capítulo por parte)
    partes = m["partes"]
    for p in partes:
        p["_ini_old"], p["_fin_old"] = p["capitulo_inicial"], p["capitulo_final"]
    for i, d in enumerate(orden):
        n = i + 1
        for p in partes:
            if p["_ini_old"] <= d["orden"] <= p["_fin_old"] + 0.9999:
                p.setdefault("_ini_new", n); p["_fin_new"] = n
    for p in partes:
        p["capitulo_inicial"], p["capitulo_final"] = p.pop("_ini_new"), p.pop("_fin_new")
        p.pop("_ini_old"); p.pop("_fin_old")
    _registrar_gate(args.gate_autor, "renumeración W7 de capitulos[].n y partes[] rangos")
    _guardar(m, antes)
    print("renumerado:", [(c["archivo"], c["n"]) for c in m["capitulos"]])
    print("partes:", [(p["n"], p["capitulo_inicial"], p["capitulo_final"]) for p in m["partes"]])
    print("RECUERDA: renumerar también el campo 'capitulo' del frontmatter (herramientas/inyectar-frontmatter.sh --renumerar-w7).")

def cmd_fundir(args):
    """W10 · funde el capítulo <origen> dentro de <destino>: retira la entrada del origen,
    reajusta el recuento del destino, renumera `n` de los posteriores y encoge el rango de
    la parte afectada. Existe porque hasta W10 el proyecto no podía fundir capítulos y la
    operación no tenía herramienta: hacerlo a mano habría violado la regla del manifiesto."""
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    if not args.gate:
        sys.exit("Fundir capítulos exige --gate \"OT-... A7 <fecha>\": es estructural y pasa por A7.")
    org, dst = os.path.basename(args.origen), os.path.basename(args.destino)
    caps = m["capitulos"]
    ce = next((c for c in caps if c["archivo"] == org), None)
    cd = next((c for c in caps if c["archivo"] == dst), None)
    if ce is None: sys.exit(f"{org} no está en el manifiesto.")
    if cd is None: sys.exit(f"{dst} no está en el manifiesto.")
    if os.path.exists(os.path.join(aa.CAPITULOS, org)):
        sys.exit(f"{org} todavía existe en capitulos/: funde el texto primero y bórralo.")
    reales = _capitulos_reales()
    if dst not in reales: sys.exit(f"No encuentro {dst} en el orden de lectura.")
    n_org = ce.get("n")
    caps.remove(ce)
    nuevo_real = aa.count_words(reales[dst]["body"])
    cd["palabras_real"] = nuevo_real
    cd["palabras"] = nuevo_real
    cd["origen"] = f"{cd.get('origen','?')} + {ce.get('origen','?')} (fusión {args.gate})"
    # NO se renumera. Se deja un HUECO en la numeración, documentado en b0-mapa-renumeracion.md.
    #
    # Renumerar aquí desincroniza `n` de los `orden_lectura` de los ficheros y de sus nombres,
    # que es exactamente el fallo que b7-perimetro.md §2 documenta: «durante unas horas, quien
    # aplicara el perímetro por número de fichero habría errado en cuarenta de los cuarenta y
    # ocho casos». Con 133 spans, 65 citas del perímetro y un mapa de equivalencias apuntando a
    # nombres de fichero, el coste de renumerar en caliente supera con mucho el de un hueco.
    # La renumeración es una operación aparte, se hace UNA VEZ y al final, como en W7.
    #
    # Los rangos de `partes[]` NO se tocan: describen cotas de orden_lectura, no cuentas, y el
    # compilador numera 1..N por orden de lectura, así que el libro impreso sale correlativo.
    hueco = n_org
    _registrar_gate(args.gate, f"fundir {org} dentro de {dst}: {len(caps)+1} -> {len(caps)} capítulos, hueco en n={hueco}")
    _guardar(m, antes)
    print(f"fundido {org} en {dst}: {len(caps)} capítulos · {dst} pasa a {nuevo_real} palabras")
    print(f"  hueco documentado en n={hueco}; rangos de partes intactos; renumerar es operación aparte")


def cmd_retitular(args):
    """Sincroniza `titulo` y `slug` del manifiesto con el frontmatter del fichero.

    Existe porque en W10 it.4 A7 vetó un título ya registrado y no había forma oficial de
    cambiarlo: `registrar` rechaza lo ya registrado y `palabras-real` no toca títulos. El
    compilado sale bien porque lee el frontmatter, así que el manifiesto se queda mintiendo
    en silencio — que es el modo de fallo de la casa."""
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    arch = os.path.basename(args.archivo)
    c = next((c for c in m["capitulos"] if c["archivo"] == arch), None)
    if c is None: sys.exit(f"{arch} no está registrado.")
    fm, _, _, _ = aa.read_chapter(os.path.join(aa.CAPITULOS, arch))
    viejo = c.get("titulo")
    c["titulo"] = fm.get("titulo")
    c["slug"] = re.sub(r"[^a-z0-9]+", "-", _sin_tildes(str(c["titulo"])).lower()).strip("-")
    _registrar_gate(args.gate or "sincronización de título", f"retitular {arch}: «{viejo}» -> «{c['titulo']}»")
    _guardar(m, antes)
    print(f"{arch}: «{viejo}» -> «{c['titulo']}» (slug {c['slug']})")


def cmd_verificar(args):
    m = aa.load_manifest()
    errores, avisos = [], []
    v0 = _git_show("v0", "biblia/metadatos.json")
    if v0 is None:
        avisos.append("no se pudo leer biblia/metadatos.json en el tag v0")
    else:
        m0 = json.loads(v0)
        for k in aa.CAMPOS_AUTOR_MANIFIESTO:
            if m0.get(k) != m.get(k):
                errores.append(f"campo de autor alterado respecto a v0: {k}")
        # cambios de campos de autor con gate registrados
        if errores:
            reg = os.path.join(aa.INFORMES, "registro-gates-autor.md")
            if os.path.exists(reg):
                avisos.append("existen gates de autor registrados; revisa informes/registro-gates-autor.md")
    reales = _capitulos_reales()
    for c in m["capitulos"]:
        p = os.path.join(aa.CAPITULOS, c["archivo"])
        if not os.path.exists(p):
            errores.append(f"archivo registrado inexistente: {c['archivo']}")
            continue
        d = reales[c["archivo"]]
        fm = d["fm"]
        if str(fm.get("titulo")) != str(c["titulo"]):
            errores.append(f"{c['archivo']}: titulo manifiesto «{c['titulo']}» ≠ frontmatter «{fm.get('titulo')}»")
        if c.get("n") is not None and fm.get("capitulo") != c["n"]:
            errores.append(f"{c['archivo']}: n={c['n']} ≠ frontmatter capitulo={fm.get('capitulo')}")
        if c.get("persona") and fm.get("persona") and fm.get("persona") != c.get("persona"):
            errores.append(f"{c['archivo']}: persona manifiesto ≠ frontmatter")
    registrados = {c["archivo"] for c in m["capitulos"]}
    for a, d in reales.items():
        if a not in registrados:
            estado = d["fm"].get("estado_plan")
            (avisos if estado == "N" else errores).append(f"capítulo en capitulos/ no registrado: {a} (estado_plan={estado})")
    # rangos de partes
    ns = [c["n"] for c in m["capitulos"] if c.get("n") is not None]
    for p in m["partes"]:
        if p["capitulo_inicial"] > p["capitulo_final"]:
            errores.append(f"parte {p['n']}: rango invertido")
    if ns and (min(ns) != m["partes"][0]["capitulo_inicial"] or max(ns) != m["partes"][-1]["capitulo_final"]):
        errores.append("rangos de partes no cubren 1..N")
    tot = sum(c.get("palabras", 0) for c in m["capitulos"])
    tot_real = sum(c.get("palabras_real", 0) for c in m["capitulos"] if c.get("palabras_real") is not None)
    print(f"presupuesto total (palabras): {tot} · palabras_real total: {tot_real} · objetivo: {m.get('palabras_objetivo')}")
    for a in avisos: print("AVISO:", a)
    for e in errores: print("ERROR:", e)
    if errores:
        sys.exit(1)
    print("manifiesto OK")

def cmd_paratexto(args):
    """Registra/actualiza un paratexto (aviso, recursos) en manifest['paratextos'] (campo operativo, §2.4)."""
    m = aa.load_manifest(); antes = _autor_snapshot(m)
    archivo = os.path.basename(args.archivo)
    p = os.path.join(aa.CAPITULOS, archivo)
    if not os.path.exists(p):
        sys.exit(f"No existe {p}")
    fm, _, body, _ = aa.read_chapter(p)
    entrada = {"tipo": fm.get("tipo"), "titulo": fm.get("titulo"), "archivo": archivo,
               "posicion": fm.get("posicion"), "provisional": bool(fm.get("provisional")),
               "palabras_real": aa.count_words(body)}
    lst = m.setdefault("paratextos", [])
    for i, e in enumerate(lst):
        if e["archivo"] == archivo:
            lst[i] = entrada; break
    else:
        lst.append(entrada)
    _guardar(m, antes)
    print("paratexto registrado:", entrada)

def cmd_mostrar(args):
    m = aa.load_manifest()
    print(f"{'n':>3} {'archivo':10} {'titulo':26} {'cuota':>6} {'real':>6} {'origen'}")
    for c in m["capitulos"]:
        print(f"{str(c.get('n')):>3} {c['archivo']:10} {c['titulo'][:26]:26} {str(c.get('palabras')):>6} {str(c.get('palabras_real')):>6} {c.get('origen','')}")
    print("palabras_objetivo:", m.get("palabras_objetivo"))

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("palabras-real")
    p = sub.add_parser("objetivo"); p.add_argument("n"); p.add_argument("--gate-autor")
    p = sub.add_parser("presupuestos"); p.add_argument("--v0", action="store_true")
    p = sub.add_parser("registrar"); p.add_argument("archivo"); p.add_argument("--gate")
    p = sub.add_parser("renumerar"); p.add_argument("--w7", action="store_true"); p.add_argument("--gate-autor")
    p = sub.add_parser("fundir"); p.add_argument("--origen", required=True); p.add_argument("--destino", required=True); p.add_argument("--gate")
    p = sub.add_parser("retitular"); p.add_argument("archivo"); p.add_argument("--gate")
    p = sub.add_parser("verificar")
    p = sub.add_parser("paratexto"); p.add_argument("archivo")
    sub.add_parser("mostrar")
    args = ap.parse_args()
    {"palabras-real": cmd_palabras_real, "objetivo": cmd_objetivo, "presupuestos": cmd_presupuestos,
     "registrar": cmd_registrar, "renumerar": cmd_renumerar, "verificar": cmd_verificar,
     "fundir": cmd_fundir, "retitular": cmd_retitular,
     "paratexto": cmd_paratexto, "mostrar": cmd_mostrar}[args.cmd](args)

if __name__ == "__main__":
    main()
