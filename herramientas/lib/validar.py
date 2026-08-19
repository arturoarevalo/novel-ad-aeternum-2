#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de frontmatter y contratos (§2.4). Exit 1 si hay errores.
- Campos del autor presentes y no renombrados: capitulo, titulo, pov, fecha, estado, analepsis.
- Campos del plan válidos: estado_plan∈{P,R,E,RW,N}, proteccion∈{total,nucleo,no}, ot, delta_objetivo (int), orden_lectura (num).
- estado ∈ {terminado, en_oleada, aceptado, vf}.
- Contrato 'persona: primera' (manifiesto) → la prosa debe estar en primera persona (densidad de marcadores de 1.ª persona ≥ umbral).
- Sin notas de trabajo en el cuerpo ([NOTA, TODO, FIXME, <!--, {{ }}, XXX, [A0], [A3 ...).
- Sin frontmatter duplicado / cuerpo vacío.
"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

ESTADOS = {"terminado", "en_oleada", "aceptado", "vf"}
ESTADOS_PLAN = {"P", "R", "E", "RW", "N"}
PROTECCIONES = {"total", "nucleo", "no"}
NOTAS_RE = re.compile(r"\[(NOTA|TODO|FIXME|A[0-9]|OT-)|<!--|\{\{|TODO:|FIXME|\[\[")
PRIMERA_RE = re.compile(r"\b(yo|me|mí|conmigo|mi|mis|mío|mía|míos|mías|nosotras|nosotros|nos|nuestro|nuestra|nuestros|nuestras)\b", re.I)
VERBOS1_RE = re.compile(r"\b(soy|estoy|tengo|he|oigo|leo|veo|siento|elijo|dejo|vuelvo|cierro|pierdo|percibo|necesito|puedo|sé|hago|quedo|conservo|espero|recibo|abro|firmo|decido|reconozco|distingo|añado|excluyo|devuelvo|completo|acredito|entrego|comparo|busco|encuentro|entiendo|creo|quiero|prefiero|acepto|rechazo|respondo|pregunto|escribo|apago|enciendo|guardo|mantengo|sigo|vivo|muero|salgo|entro|llego|paso|pido|doy|voy|estaba|era|fui|hice|dije|vi|supe|pude|tuve|quise|elegí|dejé|volví|cerré|perdí)\b", re.I)
UMBRAL_PRIMERA = 20.0   # ‰ en narración (v0: cap-38 = 31,4‰; máximo del resto = 8,0‰)

def densidad_primera(body):
    """Marcadores de 1.ª persona (pronombres + verbos frecuentes) por mil palabras, SOLO en párrafos narrativos
    (excluye diálogo, registros en ` y citas >). Calibrado sobre v0."""
    pars = [p for p in aa.paragraphs(body) if not aa.es_dialogo(p) and not p.startswith("`") and not p.startswith(">")]
    t = aa.strip_markdown("\n".join(pars))
    n = max(1, len(t.split()))
    return 1000.0 * (len(PRIMERA_RE.findall(t)) + len(VERBOS1_RE.findall(t))) / n

def validar(paths=None, verbose=True):
    m = aa.load_manifest()
    persona = {c["archivo"]: c.get("persona") for c in m["capitulos"]}
    errores, avisos = [], []
    items = aa.reading_order()
    if paths:
        base = {os.path.basename(p) for p in paths}
        items = [d for d in items if d["archivo"] in base]
    for d in items:
        fm, a = d["fm"], d["archivo"]
        for k in aa.CAMPOS_AUTOR_FRONTMATTER:
            if k not in fm:
                errores.append(f"{a}: falta campo de autor '{k}'")
        if fm.get("estado") not in ESTADOS:
            errores.append(f"{a}: estado inválido {fm.get('estado')!r}")
        if "estado_plan" in fm and fm["estado_plan"] not in ESTADOS_PLAN:
            errores.append(f"{a}: estado_plan inválido {fm['estado_plan']!r}")
        if "proteccion" in fm and fm["proteccion"] not in PROTECCIONES:
            errores.append(f"{a}: proteccion inválida {fm['proteccion']!r}")
        if "delta_objetivo" in fm:
            try: int(str(fm["delta_objetivo"]).replace("+", ""))
            except Exception: errores.append(f"{a}: delta_objetivo no entero")
        if "orden_lectura" in fm:
            try: float(fm["orden_lectura"])
            except Exception: errores.append(f"{a}: orden_lectura no numérico")
        # Los capítulos nuevos llevan orden_lectura DECIMAL para intercalarse sin renumerar…
        # …pero solo hasta W7, que es cuando el plan (§2.4) renumera una vez y los decimales
        # pasan a enteros correlativos. Sin esta condición el validador acusa a los siete
        # capítulos nuevos justo después de hacer bien la renumeración. Señal de que W7 ya
        # ocurrió: `capitulo` es un entero (antes era el marcador "N5", "N7"…).
        renumerado_w7 = isinstance(fm.get("capitulo"), int)
        if (fm.get("estado_plan") == "N" and not renumerado_w7
                and "orden_lectura" in fm and float(fm["orden_lectura"]).is_integer()):
            avisos.append(f"{a}: capítulo nuevo con orden_lectura entero (se esperaba decimal hasta W7)")
        if not d["body"].strip():
            errores.append(f"{a}: cuerpo vacío")
        for i, line in enumerate(d["body"].split("\n"), 1):
            if NOTAS_RE.search(line):
                errores.append(f"{a}:{i}: posible nota de trabajo en el cuerpo: {line.strip()[:70]!r}")
        if d["body"].count("\n---\n") > 0:
            avisos.append(f"{a}: '---' dentro del cuerpo (¿segundo frontmatter?)")
        # contrato persona
        per = persona.get(a) or fm.get("persona")
        dens = densidad_primera(d["body"])
        if per == "primera":
            if dens < UMBRAL_PRIMERA:
                errores.append(f"{a}: contrato persona=primera incumplido (densidad 1.ª persona en narración {dens:.1f}‰ < {UMBRAL_PRIMERA:.0f}‰)")
        elif dens > 15.0 and per is None:
            avisos.append(f"{a}: densidad de 1.ª persona en narración alta ({dens:.1f}‰) sin contrato persona=primera")
    if verbose:
        for x in avisos: print("AVISO:", x)
        for x in errores: print("ERROR:", x)
    return errores, avisos

if __name__ == "__main__":
    args = [p for p in sys.argv[1:] if not p.startswith("--")]
    e, a = validar(args or None)
    if e:
        sys.exit(1)
    print(f"validador OK ({len(a)} avisos)")
