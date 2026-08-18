#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Métricas M1–M10 (§2.3, §7.2 del plan). Uso: metricas.py <etiqueta> [--baseline v0] [--solo M1,M4]
Escribe informes/metricas-<etiqueta>.json e informes/dashboard-<etiqueta>.md. Compara con informes/metricas-<baseline>.json.

M1 opacidad: términos de sistema únicos y ocurrencias por 1.000 palabras, por capítulo (lexicón B3 o de arranque).
M2 mecánicas: primera aparición de términos por capítulo (orden de lectura); mecánicas nuevas por capítulo respecto a la baseline (≤1).
M3 presencia familiar: % de palabras en POV Maja/Nora/Jessie por parte.
M4 cierres-objeto: detector heurístico de cierres de escena sobre objeto inanimado (lista para revisión humana).
M5 ritmo: longitud, escenas, ratio diálogo, longitud de frase, tramo máximo sin diálogo (proxy de sumario/procedimiento).
M6 voz: clasificador ciego (Naive Bayes multinomial + rasgos de estilo, leave-one-out) de réplicas con atribución explícita.
M7 cronología: secuencia de fechas, cuenta atrás, horas del clímax, aritmética de cohorte, inventario de fechas en prosa.
M8 banda de palabras: total vs palabras_objetivo ± 1.000 y real vs presupuesto por capítulo.
M9 protegidos: proteger.sh verificar.
M10 ledger Chéjov: % pagado o sin-pago-intencional (biblia/b4-ledger.json).
"""
import sys, os, re, json, math, argparse, subprocess, datetime, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

FAMILIA = {"Maja", "Nora", "Jessie"}
DENSOS_T1 = ["cap-08.md", "cap-13.md", "cap-17.md", "cap-21.md", "cap-30.md", "cap-36.md"]

# ------------------------------------------------------------------ utilidades
def cargar_lexicon():
    p = os.path.join(aa.BIBLIA, "b3-lexicon.json")
    if not os.path.exists(p):
        p = os.path.join(aa.ROOT, "herramientas", "metricas", "lexicon-bootstrap.json")
    d = json.load(open(p, encoding="utf-8"))
    terms = []
    for t in d["terminos"]:
        vs = sorted(set(t.get("variantes", []) + [t.get("canonico", t["id"])]), key=len, reverse=True)
        pats = []
        for v in vs:
            if not v: continue
            pats.append(r"(?<![\w-])" + re.escape(v) + r"(?![\w-])")
        terms.append({"id": t["id"], "categoria": t.get("categoria", "?"), "re": re.compile("|".join(pats))})
    return os.path.relpath(p, aa.ROOT), terms

def texto_plano(body):
    return aa.strip_markdown("\n".join(l for l in body.split("\n") if not aa.es_dinkus(l)))

# ------------------------------------------------------------------ M1 / M2
def m1_m2(orden):
    src, terms = cargar_lexicon()
    m1 = {}; primera = {}; por_cap_nuevos = {}
    for d in orden:
        t = texto_plano(d["body"]); n = aa.count_words(d["body"]) or 1
        unicos = []; occ = 0
        for term in terms:
            k = len(term["re"].findall(t))
            if k:
                unicos.append(term["id"]); occ += k
                if term["id"] not in primera:
                    primera[term["id"]] = d["archivo"]
                    por_cap_nuevos.setdefault(d["archivo"], []).append((term["id"], term["categoria"]))
        m1[d["archivo"]] = {"palabras": n, "terminos_unicos": len(unicos), "ocurrencias": occ,
                            "unicos_por_1000": round(1000 * len(unicos) / n, 1), "ocurrencias_por_1000": round(1000 * occ / n, 1),
                            "terminos": unicos}
    m2 = {}
    for d in orden:
        nuevos = por_cap_nuevos.get(d["archivo"], [])
        mec = [x for x, c in nuevos if c in ("mecanica", "proceso")]
        m2[d["archivo"]] = {"terminos_nuevos": [x for x, _ in nuevos], "mecanicas_nuevas": mec, "n_mecanicas_nuevas": len(mec)}
    return {"lexicon": src, "n_terminos_lexicon": len(terms), "por_capitulo": m1}, {"primera_aparicion": primera, "por_capitulo": m2}

# ------------------------------------------------------------------ M3
def m3(orden, manifest):
    partes = {}
    for d in orden:
        pn = aa.parte_de(d["orden"], manifest)
        w = aa.count_words(d["body"])
        povs = [p.strip() for p in re.split(r"→|->|/", str(d["fm"].get("pov", "")))]
        povs = [re.sub(r"\s*\(.*\)", "", p) for p in povs]
        fam_names = [p for p in povs if p.split()[0] in FAMILIA] if povs else []
        if len(povs) > 1:
            escenas = aa.split_scenes(d["body"])
            if len(escenas) == len(povs):
                fam_w = sum(aa.count_words(s) for s, p in zip(escenas, povs) if p.split()[0] in FAMILIA)
            else:
                fam_w = round(w * len(fam_names) / len(povs))
        else:
            fam_w = w if fam_names else 0
        e = partes.setdefault(pn, {"palabras": 0, "familia": 0, "capitulos_familia": []})
        e["palabras"] += w; e["familia"] += fam_w
        if fam_w: e["capitulos_familia"].append(d["archivo"])
    for pn, e in partes.items():
        e["pct_familia"] = round(100 * e["familia"] / e["palabras"], 1) if e["palabras"] else 0
    tot = sum(e["palabras"] for e in partes.values()); fam = sum(e["familia"] for e in partes.values())
    return {"por_parte": partes, "total_pct_familia": round(100 * fam / tot, 1) if tot else 0}

# ------------------------------------------------------------------ M4
NOMBRES = r"(Jean|Maja|Nora|Jessie|Alana|Astrid|Mats|Tomas|Aslak|Gunnar|Inger|Henrik|Dahl|EDDA|Coro|Nieve|Cuchillo|Madre|Jardinera|Utsi|Vik|Larsson|Armstrong)"
PERSONAS = r"\b(mujer|hombre|médica|médico|técnico|técnica|funcionaria|funcionario|jueza|juez|secretaria|periodista|operaria|operario|conserje|instalador|consejera|consejero|patrón|profesora|profesor|tutora|tutor|niña|niño|gemelas|hijas|hija|madre|padre|abogada|abogado|inspectora|policía|enfermera|chica|chico|alguien|nadie|todos|ambas|ambos|ellas|ellos|ella|él)\b"
def m4(orden):
    hallazgos = []
    for d in orden:
        for i, esc in enumerate(aa.split_scenes(d["body"]), 1):
            pars = aa.paragraphs(esc)
            if not pars: continue
            last = pars[-1]
            plano = aa.strip_markdown(last).strip()
            if not plano: continue
            es_reg = last.strip().startswith("`") or last.strip().startswith(">")
            es_dial = aa.es_dialogo(last)
            frases = aa.sentences(plano)
            nw = len(plano.split())
            if es_dial or es_reg:
                tipo = "diálogo" if es_dial else "registro"
                if es_reg:
                    hallazgos.append({"archivo": d["archivo"], "escena": i, "tipo": "cierre-registro", "texto": plano[:140]})
                continue
            ultima = frases[-1] if frases else plano
            nwu = len(ultima.split())
            corta = nwu <= 28
            sujeto_persona = bool(re.search(NOMBRES, ultima[:45])) or bool(re.search(PERSONAS, ultima[:35], re.I)) or bool(re.search(r"\b(yo|me|mi|nos|nosotras)\b", ultima[:25], re.I))
            arranque = re.match(r"^(El|La|Los|Las|Un|Una|Unos|Unas|Su|Sus|Al|Del|Aquel|Aquella|Otra|Otro|Ninguna|Ningún|Cada|Todo|Toda|En|Sobre|Bajo|Desde|Detrás|Fuera|Dentro|Después|Luego|Todavía|Aún|Solo|Sólo|Ya|Entre|Junto|Frente|Encima|Debajo|Al otro lado|A|Con|Por|Sin)\b", ultima)
            # el sujeto gramatical no es persona: sin nombre propio ni sustantivo de persona en el arranque; y sin verbo de habla
            if corta and arranque and not sujeto_persona and not re.search(r"\b(dijo|preguntó|respondió|añadió|pensó|miró|leyó|firmó|escribió|esperó|entró|salió|se levantó|se sentó)\b", ultima[:60]):
                hallazgos.append({"archivo": d["archivo"], "escena": i, "tipo": "cierre-objeto", "texto": ultima[:160], "parrafo": plano[:200]})
    n_obj = sum(1 for h in hallazgos if h["tipo"] == "cierre-objeto")
    n_reg = sum(1 for h in hallazgos if h["tipo"] == "cierre-registro")
    return {"cierres_objeto": n_obj, "cierres_registro": n_reg, "hallazgos": hallazgos}

# ------------------------------------------------------------------ M5
def m5(orden, manifest):
    out = {}
    for d in orden:
        pars_raw = aa.paragraphs(d["body"])
        pars = [p for p in pars_raw if not aa.es_dinkus(p)]
        w_total = aa.count_words(d["body"]) or 1
        w_dial = sum(aa.count_words(p) for p in pars if aa.es_dialogo(p))
        w_reg = sum(aa.count_words(p) for p in pars if p.startswith("`") or p.startswith(">"))
        narr = [p for p in pars if not aa.es_dialogo(p) and not (p.startswith("`") or p.startswith(">"))]
        frases = [f for p in narr for f in aa.sentences(p)]
        lens = [len(f.split()) for f in frases if f.split()]
        media = sum(lens) / len(lens) if lens else 0
        # tramo máximo consecutivo de palabras sin diálogo (proxy de sumario/procedimiento)
        run = best = 0
        for p in pars:
            if aa.es_dialogo(p): run = 0
            else: run += aa.count_words(p); best = max(best, run)
        # Variante por ESCENA: el dinkus también reinicia. Se recorre `pars_raw`, NO `pars`: arriba
        # se filtran los dinkus de la lista (`pars = [p for p in pars if not es_dinkus(p)]`), y ese
        # filtro —que parece limpieza inocua para no contar sus palabras— borra la frontera de
        # escena de la secuencia, de modo que el proxy deja correr el tramo a través de un cambio
        # de escena. Eso no es una carrera que ningún lector experimente: tras el dinkus hay blanco
        # y empieza otra cosa. En cap-34 la diferencia es 469 vs 329. Se AÑADE en vez de sustituir
        # porque `max_tramo_sin_dialogo` es contrato del plan (M5) y sus cifras históricas deben
        # seguir siendo comparables. Hallazgo de A3b en W5.
        run_e = best_e = 0
        for p in pars_raw:
            if aa.es_dialogo(p) or aa.es_dinkus(p): run_e = 0
            else: run_e += aa.count_words(p); best_e = max(best_e, run_e)
        out[d["archivo"]] = {"palabras": w_total, "escenas": len(aa.split_scenes(d["body"])), "parrafos": len(pars),
                             "pct_dialogo": round(100 * w_dial / w_total, 1), "pct_registro": round(100 * w_reg / w_total, 1),
                             "frase_media": round(media, 1), "pct_frases_cortas_le6": round(100 * sum(1 for l in lens if l <= 6) / len(lens), 1) if lens else 0,
                             "pct_frases_largas_ge25": round(100 * sum(1 for l in lens if l >= 25) / len(lens), 1) if lens else 0,
                             "max_tramo_sin_dialogo": best, "max_tramo_escena": best_e, "parte": aa.parte_de(d["orden"], manifest), "pov": d["fm"].get("pov")}
    return out

# ------------------------------------------------------------------ M6
VERBOS_DICENDI = r"(dijo|dice|preguntó|pregunta|respondió|responde|añadió|añade|repitió|repite|insistió|insiste|contestó|contesta|leyó|lee|murmuró|pidió|pide|explicó|corrigió|corrige|advirtió|propuso|siguió|continuó|concluyó|precisó|admitió|confirmó|negó|susurró|gritó|ordenó|resumió|recordó|señaló|anunció|apuntó|replicó|sugirió|comentó|informó|indicó|aclaró|prosiguió|terminó|empezó|intervino|matizó|reconoció|reclamó|protestó|observó|declaró|afirmó|soltó|dictó|escribió|tecleó)"
NOMBRE_RE = re.compile(r"\b(Jean|Maja|Nora|Jessie|Alana|Astrid|Mats|Tomas|Aslak|Gunnar|Inger|Henrik|EDDA|Coro|Nieve|Cuchillo|Madre|La Jardinera|Jardinera)\b")
def extraer_replicas(orden):
    reps = []
    for d in orden:
        for p in aa.paragraphs(d["body"]):
            if not aa.es_dialogo(p): continue
            spk = None
            m = re.search(r"—\s*" + VERBOS_DICENDI + r"\s+([^—.,;]{0,40})", p)
            if m:
                nm = NOMBRE_RE.search(m.group(2))
                if nm: spk = nm.group(1)
            if not spk:
                m = re.search(r"—\s*(" + NOMBRE_RE.pattern[2:-2] + r")\s+" + VERBOS_DICENDI, p)
                if m: spk = m.group(1)
            if not spk:
                m = re.search(r"—\s*(le\s+)?" + VERBOS_DICENDI + r"\s+(la|el)\s+\w+", p)
                if m: spk = None
            if spk:
                spk = "La Jardinera" if spk == "Jardinera" else spk
                # segmentos separados por raya: [vacío, habla, inciso narrador, habla, inciso, …]
                segs = p.split("—")
                habla = " ".join(seg.strip() for i, seg in enumerate(segs) if i >= 1 and i % 2 == 1)
                habla = re.sub(r"^\s*[.,;:]\s*", "", habla).strip()
                if len(habla.split()) >= 2 and not NOMBRE_RE.search(habla) or (len(habla.split()) >= 2 and spk not in habla):
                    reps.append({"archivo": d["archivo"], "hablante": spk, "texto": habla})
    return reps

def rasgos(texto):
    t = texto.lower()
    toks = re.findall(r"\w+|[¿?¡!…]", t)
    feats = collections.Counter()
    for tk in toks: feats["w:" + tk] += 1
    for a, b in zip(toks, toks[1:]): feats["b:" + a + "_" + b] += 1
    n = len(toks) or 1
    feats["f:len_" + ("s" if n <= 5 else "m" if n <= 14 else "l")] += 1
    if "?" in t: feats["f:preg"] += 1
    if "…" in t: feats["f:susp"] += 1
    if re.search(r"\b(joder|puta|mierda|coño|hostia|cabrón|cabrones|gilipollas|cojones)\b", t): feats["f:vulg"] += 1
    if re.search(r"\b(que|porque|aunque|cuando|si|mientras|donde|como)\b", t): feats["f:subord"] += 1
    if re.search(r"\b(tú|te|tu|tienes|eres|haces|puedes|quieres|sabes)\b", t): feats["f:2p"] += 1
    if re.search(r"\b(si|cuando)\b.*\b(paro|abortamos|se aborta|no salgo|nos vamos)\b", t): feats["f:cond_op"] += 1
    if sum(1 for c in texto if c.isupper()) > 0.5 * max(1, sum(1 for c in texto if c.isalpha())): feats["f:mayus"] += 1
    if re.search(r"\b(no|nunca|nada|ninguna|ningún|tampoco)\b", t): feats["f:neg"] += 1
    if re.search(r"\b(medir|medí|comparar|comparé|contar|conté|calcular|calculé|estimar|verificar|comprobar|comprobé|datos|dato|segundos|minutos|porcentaje|serie|series|muestra|prueba)\b", t): feats["f:medir"] += 1
    return feats

def m6(orden, min_rep=12):
    reps = extraer_replicas(orden)
    por = collections.Counter(r["hablante"] for r in reps)
    hablantes = sorted(h for h, c in por.items() if c >= min_rep)
    data = [r for r in reps if r["hablante"] in hablantes]
    if len(hablantes) < 2:
        return {"replicas_atribuidas": len(reps), "hablantes": dict(por), "acierto": None, "nota": "muestra insuficiente"}
    feats = [rasgos(r["texto"]) for r in data]
    labels = [r["hablante"] for r in data]
    vocab = set()
    for f in feats: vocab.update(f.keys())
    V = len(vocab)
    aciertos = 0; conf = collections.Counter(); por_hablante = collections.Counter(); ok_h = collections.Counter()
    # leave-one-out NB multinomial con suavizado
    tot_counts = {h: collections.Counter() for h in hablantes}; tot_n = collections.Counter(); doc_n = collections.Counter()
    for f, l in zip(feats, labels):
        tot_counts[l].update(f); tot_n[l] += sum(f.values()); doc_n[l] += 1
    for i, (f, l) in enumerate(zip(feats, labels)):
        best, bests = None, -1e18
        for h in hablantes:
            cnt = tot_counts[h]; n_h = tot_n[h]; dn = doc_n[h]
            if h == l:
                n_h -= sum(f.values()); dn -= 1
            if dn <= 0: continue
            logp = math.log(dn / (len(data) - 1))
            for k, v in f.items():
                c = cnt[k] - (v if h == l else 0)
                logp += v * math.log((c + 0.5) / (n_h + 0.5 * V))
            if logp > bests: bests, best = logp, h
        por_hablante[l] += 1
        if best == l: aciertos += 1; ok_h[l] += 1
        else: conf[(l, best)] += 1
    acc = round(100 * aciertos / len(data), 1)
    pares = {}
    for a in hablantes:
        for b in hablantes:
            if a < b:
                sub = [(f, l) for f, l in zip(feats, labels) if l in (a, b)]
                pares[f"{a}/{b}"] = None
    # acierto por par (Nora/Jessie, Astrid/Maja, Astrid/Alana, Maja/Alana) mediante NB binario
    def par_acc(a, b):
        sub = [(f, l) for f, l in zip(feats, labels) if l in (a, b)]
        if len(sub) < 2 * min_rep: return None
        cnts = {a: collections.Counter(), b: collections.Counter()}; ns = collections.Counter(); dn = collections.Counter()
        for f, l in sub: cnts[l].update(f); ns[l] += sum(f.values()); dn[l] += 1
        vocab2 = set(); [vocab2.update(f.keys()) for f, _ in sub]; V2 = len(vocab2)
        ok = 0
        for f, l in sub:
            sc = {}
            for h in (a, b):
                n_h = ns[h] - (sum(f.values()) if h == l else 0); d_h = dn[h] - (1 if h == l else 0)
                if d_h <= 0: sc[h] = -1e18; continue
                lp = math.log(d_h / (len(sub) - 1))
                for k, v in f.items():
                    c = cnts[h][k] - (v if h == l else 0)
                    lp += v * math.log((c + 0.5) / (n_h + 0.5 * V2))
                sc[h] = lp
            if max(sc, key=sc.get) == l: ok += 1
        return round(100 * ok / len(sub), 1)
    pares = {}
    for a, b in [("Nora", "Jessie"), ("Astrid", "Maja"), ("Astrid", "Alana"), ("Maja", "Alana"), ("Maja", "Nora"), ("Maja", "Jessie")]:
        if a in hablantes and b in hablantes:
            pares[f"{a}/{b}"] = par_acc(a, b)
    return {"replicas_atribuidas": len(reps), "replicas_usadas": len(data), "hablantes": {h: por[h] for h in hablantes},
            "acierto": acc, "acierto_por_hablante": {h: round(100 * ok_h[h] / por_hablante[h], 1) for h in hablantes},
            "confusiones_top": [f"{a}→{b}: {c}" for (a, b), c in conf.most_common(8)], "pares": pares,
            "nota": "clasificador NB multinomial (unigramas+bigramas+rasgos de estilo), leave-one-out, solo réplicas con atribución explícita"}

# ------------------------------------------------------------------ M7
HORAS_CLIMAX = ["12:38", "12:46:01", "12:46:50", "12:47", "13:07", "13:11"]
def parse_fecha(v):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}))?", str(v))
    if not m: return None
    y, mo, d, h, mi = m.groups()
    return datetime.datetime(int(y), int(mo), int(d), int(h or 0), int(mi or 0))
MESES = {"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}
def m7(orden, manifest):
    errores, avisos = [], []
    prev = None; prev_a = None
    for d in orden:
        f = parse_fecha(d["fm"].get("fecha"))
        if f is None: errores.append(f"{d['archivo']}: fecha no parseable"); continue
        if prev and f < prev and not d["fm"].get("analepsis"):
            errores.append(f"{d['archivo']} ({f.date()}) retrocede respecto a {prev_a} ({prev.date()}) sin analepsis")
        if not d["fm"].get("analepsis"): prev, prev_a = f, d["archivo"]
    SOLD = datetime.date(2061, 1, 21)
    for p in manifest["partes"]:
        mm = re.match(r"(\d{1,2}) de (\w+) de (\d{4}) · Faltan (\d+) días", p["subtitulo"])
        if mm:
            fecha = datetime.date(int(mm.group(3)), MESES[mm.group(2).lower()], int(mm.group(1)))
            if (SOLD - fecha).days != int(mm.group(4)):
                errores.append(f"parte {p['n']}: cuenta atrás incorrecta")
    horas = {}
    for h in HORAS_CLIMAX:
        caps = [d["archivo"] for d in orden if re.search(r"(?<![\d:])" + re.escape(h) + r"(?![\d])", d["body"])]
        horas[h] = caps
        if not caps: errores.append(f"hora del clímax {h} ausente del manuscrito")
    # orden: la primera aparición de cada hora no debe estar en un capítulo posterior al de la hora siguiente… (aviso, no error)
    idx = {d["archivo"]: i for i, d in enumerate(orden)}
    firsts = [(h, min(idx[c] for c in horas[h])) for h in HORAS_CLIMAX if horas[h]]
    for (h1, i1), (h2, i2) in zip(firsts, firsts[1:]):
        if i2 < i1 - 1: avisos.append(f"{h2} aparece antes ({orden[i2]['archivo']}) que {h1} ({orden[i1]['archivo']})")
    # aritmética de cohorte
    canon = {"4.096", "4.095", "1.185", "2.911", "2.311", "597"}
    encontrados = collections.Counter()
    sospechosos = []
    for d in orden:
        for m in re.finditer(r"\b(\d{1,2}\.\d{3}|\d{3,4})\b(?=[^\n]{0,60}\b(orígenes|origen|rutas|ruta|trayectorias|continuidades|ramas|ejecuciones|adhesiones|papeletas|filas)\b)", d["body"]):
            n = m.group(1); encontrados[n] += 1
            if n not in canon and n not in ("2.401", "979", "2.427", "60", "90"):
                sospechosos.append(f"{d['archivo']}: «{n}» junto a «{m.group(2)}»")
    if 4096 - 1185 != 2911 or 2311 + 597 + 3 != 2911: errores.append("aritmética de cohorte rota (constantes)")
    for d in orden:   # presencia de las cifras canónicas en cualquier contexto
        for c in ["4.096", "1.185", "2.911", "2.311", "597"]:
            if re.search(r"(?<![\d.])" + re.escape(c) + r"(?![\d.])", d["body"]):
                encontrados[c] += 0   # asegura la clave
                encontrados[c] = max(encontrados[c], 1)
    faltan = [c for c in ["4.096", "1.185", "2.911", "2.311", "597"] if encontrados[c] == 0]
    if faltan: avisos.append("cifras de cohorte no encontradas en prosa: " + ", ".join(faltan))
    # inventario de fechas explícitas en prosa
    inventario = {}
    for d in orden:
        fs = re.findall(r"\b(\d{1,2}) de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)(?: de (\d{4}))?", d["body"])
        anios = re.findall(r"\b(20[3-6]\d)\b", d["body"])
        if fs or anios:
            inventario[d["archivo"]] = {"fechas": [" ".join(x for x in f if x) for f in fs][:12], "años": sorted(set(anios))}
    return {"errores": errores, "avisos": avisos, "horas_climax": horas, "cifras_cohorte": dict(encontrados),
            "cifras_sospechosas": sospechosos, "inventario_fechas_prosa": inventario}

# ------------------------------------------------------------------ M8 / M9 / M10
def m8(orden, manifest):
    obj = int(manifest.get("palabras_objetivo", 0)); banda = 1000
    total = sum(aa.count_words(d["body"]) for d in orden)
    pres = {c["archivo"]: c.get("palabras") for c in manifest["capitulos"]}
    por_cap = {}
    for d in orden:
        w = aa.count_words(d["body"]); b = pres.get(d["archivo"])
        por_cap[d["archivo"]] = {"real": w, "presupuesto": b, "delta": (w - b) if b is not None else None}
    return {"total": total, "objetivo": obj, "banda": [obj - banda, obj + banda], "en_banda": obj - banda <= total <= obj + banda,
            "suma_presupuestos": sum(v for v in pres.values() if v), "por_capitulo": por_cap}

def m9():
    r = subprocess.run([os.path.join(aa.ROOT, "herramientas", "proteger.sh"), "verificar"], capture_output=True, text=True, cwd=aa.ROOT)
    return {"ok": r.returncode == 0, "salida": (r.stdout + r.stderr).strip()}

def m10():
    p = os.path.join(aa.BIBLIA, "b4-ledger.json")
    if not os.path.exists(p):
        return {"ok": None, "nota": "biblia/b4-ledger.json aún no existe (B4)"}
    d = json.load(open(p, encoding="utf-8"))
    ent = d.get("entradas", [])
    est = collections.Counter(e.get("estado_actual", e.get("estado_v0")) for e in ent)
    cerrados = est.get("PAGADO", 0) + est.get("SIN-PAGO-INTENCIONAL", 0)
    return {"total": len(ent), "por_estado": dict(est), "pct_cerrado": round(100 * cerrados / len(ent), 1) if ent else None,
            "pendientes": [e["id"] for e in ent if e.get("estado_actual", e.get("estado_v0")) == "PENDIENTE-ASIGNAR"]}

# ------------------------------------------------------------------ dashboard
def sem(ok, ambar=False):
    return "🟢" if ok else ("🟡" if ambar else "🔴")

def dashboard(et, R, B):
    L = []
    L.append(f"# Dashboard de métricas · {et}\n\n_Generado {R['generado']} · baseline de comparación: {B['etiqueta'] if B else '—'}_\n")
    m8v = R["M8"]
    L.append(f"## M8 · Palabras\n\n- Total: **{m8v['total']}** · objetivo {m8v['objetivo']} (banda {m8v['banda'][0]}–{m8v['banda'][1]}) → {sem(m8v['en_banda'])}"
             f" · suma de presupuestos del manifiesto: {m8v['suma_presupuestos']}\n")
    L.append("## M1 · Opacidad (términos de sistema por 1.000 palabras) — objetivo T1: −30 % en 8, 13, 17, 21, 30, 36 (cap. 5 = referencia)\n")
    L.append(f"_Lexicón: `{R['M1']['lexicon']}` ({R['M1']['n_terminos_lexicon']} términos)_\n")
    L.append("| capítulo | pov | palabras | únicos | únicos/1000 | ocurr./1000 | Δ vs baseline (únicos/1000) | M2 mecánicas nuevas | M2 vs baseline |")
    L.append("|---|---|---:|---:|---:|---:|---:|---:|---|")
    for arch, v in R["M1"]["por_capitulo"].items():
        b = B["M1"]["por_capitulo"].get(arch) if B else None
        delta = f"{100*(v['unicos_por_1000']-b['unicos_por_1000'])/b['unicos_por_1000']:+.0f} %" if b and b["unicos_por_1000"] else "—"
        m2v = R["M2"]["por_capitulo"][arch]
        m2b = ""
        if B:
            prev_first = B["M2"]["primera_aparicion"]
            idx = list(R["M1"]["por_capitulo"].keys())
            movidas = [t for t in m2v["mecanicas_nuevas"] if prev_first.get(t) not in (None, arch) and idx.index(prev_first[t]) > idx.index(arch)] + [t for t in m2v["mecanicas_nuevas"] if prev_first.get(t) is None]
            m2b = ("🔴 " if len(movidas) > 1 else "🟢 ") + (", ".join(movidas) if movidas else "0 nuevas")
        marca = " **(T1)**" if arch in DENSOS_T1 else ""
        pov = str(R["M5"][arch]["pov"])[:14]
        L.append(f"| {arch}{marca} | {pov} | {v['palabras']} | {v['terminos_unicos']} | {v['unicos_por_1000']} | {v['ocurrencias_por_1000']} | {delta} | {m2v['n_mecanicas_nuevas']} ({', '.join(m2v['mecanicas_nuevas'][:6])}) | {m2b} |")
    L.append("")
    L.append("## M3 · Presencia familiar (POV Maja/Nora/Jessie) por parte\n")
    L.append("| parte | palabras | familia | % familia | Δ vs baseline |\n|---|---:|---:|---:|---:|")
    for pn, e in sorted(R["M3"]["por_parte"].items(), key=lambda x: int(x[0])):
        b = B["M3"]["por_parte"].get(str(pn)) if B else None
        L.append(f"| {pn} | {e['palabras']} | {e['familia']} | {e['pct_familia']} % | {('%+.1f' % (e['pct_familia']-b['pct_familia'])) if b else '—'} |")
    L.append(f"\nTotal familia: {R['M3']['total_pct_familia']} %\n")
    L.append(f"## M4 · Cierres de escena sobre objeto (heurístico) — objetivo ≤ 18 en vF (lista blanca de 12)\n\n- Cierres-objeto detectados: **{R['M4']['cierres_objeto']}** · cierres sobre registro (`…`): {R['M4']['cierres_registro']}"
             + (f" · baseline: {B['M4']['cierres_objeto']}" if B else "") + "\n")
    L.append("| capítulo | escena | tipo | texto |\n|---|---:|---|---|")
    for h in R["M4"]["hallazgos"]:
        if h["tipo"] == "cierre-objeto":
            L.append(f"| {h['archivo']} | {h['escena']} | {h['tipo']} | {h['texto'].replace('|','/')} |")
    L.append("")
    L.append("## M5 · Ritmo (proxies)\n")
    L.append("| capítulo | parte | pov | palabras | escenas | % diálogo | % registro | frase media | % ≤6 | % ≥25 | máx. tramo sin diálogo | máx. tramo por escena |\n|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for arch, v in R["M5"].items():
        L.append(f"| {arch} | {v['parte']} | {str(v['pov'])[:14]} | {v['palabras']} | {v['escenas']} | {v['pct_dialogo']} | {v['pct_registro']} | {v['frase_media']} | {v['pct_frases_cortas_le6']} | {v['pct_frases_largas_ge25']} | {v['max_tramo_sin_dialogo']} | {v['max_tramo_escena']} |")
    L.append("")
    m6v = R["M6"]
    L.append(f"## M6 · Voz (clasificador ciego, leave-one-out) — objetivo ≥ 80 %\n\n- Réplicas con atribución explícita: {m6v.get('replicas_atribuidas')} · usadas: {m6v.get('replicas_usadas')} · **acierto global: {m6v.get('acierto')} %**"
             + (f" · baseline: {B['M6'].get('acierto')} %" if B else "") + f"\n- Por hablante: {m6v.get('acierto_por_hablante')}\n- Pares críticos: {m6v.get('pares')}\n- Confusiones más frecuentes: {m6v.get('confusiones_top')}\n- _{m6v.get('nota')}_\n")
    m7v = R["M7"]
    L.append(f"## M7 · Cronología — {sem(not m7v['errores'])}\n\n- Errores: {m7v['errores'] or 'ninguno'}\n- Avisos: {m7v['avisos'] or 'ninguno'}\n- Horas del clímax: {m7v['horas_climax']}\n- Cifras de cohorte encontradas: {m7v['cifras_cohorte']}\n- Cifras sospechosas: {m7v['cifras_sospechosas'] or 'ninguna'}\n")
    L.append(f"## M9 · Protegidos — {sem(R['M9']['ok'])}\n\n```\n{R['M9']['salida']}\n```\n")
    m10v = R["M10"]
    L.append(f"## M10 · Ledger Chéjov — {sem(m10v.get('pct_cerrado') == 100, ambar=True) if m10v.get('ok') is not False else '⚪'}\n\n- {m10v}\n")
    L.append("## M8 · Real vs presupuesto por capítulo\n\n| capítulo | real | presupuesto | Δ |\n|---|---:|---:|---:|")
    for arch, v in m8v["por_capitulo"].items():
        L.append(f"| {arch} | {v['real']} | {v['presupuesto']} | {v['delta'] if v['delta'] is not None else '—'} |")
    return "\n".join(L) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("etiqueta")
    ap.add_argument("--baseline", default="v0")
    a = ap.parse_args()
    manifest = aa.load_manifest()
    orden = aa.reading_order()
    R = {"etiqueta": a.etiqueta, "generado": datetime.datetime.now().isoformat(timespec="seconds")}
    R["M1"], R["M2"] = m1_m2(orden)
    R["M3"] = m3(orden, manifest)
    R["M4"] = m4(orden)
    R["M5"] = m5(orden, manifest)
    R["M6"] = m6(orden)
    R["M7"] = m7(orden, manifest)
    R["M8"] = m8(orden, manifest)
    R["M9"] = m9()
    R["M10"] = m10()
    os.makedirs(aa.INFORMES, exist_ok=True)
    pj = os.path.join(aa.INFORMES, f"metricas-{a.etiqueta}.json")
    with open(pj, "w", encoding="utf-8") as f:
        json.dump(R, f, ensure_ascii=False, indent=1)
    B = None
    pb = os.path.join(aa.INFORMES, f"metricas-{a.baseline}.json")
    if a.baseline != a.etiqueta and os.path.exists(pb):
        B = json.load(open(pb, encoding="utf-8"))
    pd = os.path.join(aa.INFORMES, f"dashboard-{a.etiqueta}.md")
    with open(pd, "w", encoding="utf-8") as f:
        f.write(dashboard(a.etiqueta, R, B))
    print(f"métricas → {os.path.relpath(pj, aa.ROOT)} · dashboard → {os.path.relpath(pd, aa.ROOT)}")
    print(f"M8 total {R['M8']['total']} {'EN BANDA' if R['M8']['en_banda'] else 'fuera de banda'} · M4 cierres-objeto {R['M4']['cierres_objeto']} · M6 acierto {R['M6'].get('acierto')} % · M7 errores {len(R['M7']['errores'])} · M9 {'OK' if R['M9']['ok'] else 'FALLO'} · M10 {R['M10'].get('pct_cerrado')}")

if __name__ == "__main__":
    main()
