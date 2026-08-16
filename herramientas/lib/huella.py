#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B6 (parte cuantitativa) · Huella estilística de una versión: distribución de longitud de frase (narración),
ratio diálogo/narración, densidad de subordinación, léxico frecuente (sin stopwords), patrón de cierre de escena,
longitud de párrafo, uso de registros en `…`, por grupo de POV (Jean/continuidades · familia · otros) y global.
Uso: huella.py <etiqueta>  → biblia/b6-huella-datos-<etiqueta>.json e informes/b6-huella-<etiqueta>.md
"""
import sys, os, re, json, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa

STOP = set("""de la que el en y a los del se las por un para con no una su al lo como más pero sus le ya o este sí porque esta entre cuando muy sin sobre también me hasta hay donde quien desde todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mí antes algunos qué unos yo otro otras otra él tanto esa estos mucho quienes nada muchos cual poco ella estar estas algunas algo nosotros mi mis tú te ti tu tus ellas nosotras vosotros vosotras os mío mía míos mías tuyo tuya tuyos tuyas suyo suya suyos suyas nuestro nuestra nuestros nuestras vuestro vuestra vuestros vuestras esos esas estoy estás está estamos estáis están esté estés estemos estéis estén estaré estarás estará estaremos estaréis estarán estaría estarías estaríamos estaríais estarían estaba estabas estábamos estabais estaban estuve estuviste estuvo estuvimos estuvisteis estuvieron he has ha hemos habéis han haya hayas hayamos hayáis hayan habré habrás habrá habremos habréis habrán habría habrías habríamos habríais habrían había habías habíamos habíais habían hube hubiste hubo hubimos hubisteis hubieron soy eres es somos sois son sea seas seamos seáis sean seré serás será seremos seréis serán sería serías seríamos seríais serían era eras éramos erais eran fui fuiste fue fuimos fuisteis fueron tengo tienes tiene tenemos tenéis tienen tenga tengas tengamos tengáis tengan tendré tendrás tendrá tendremos tendréis tendrán tendría tendrías tendríamos tendríais tendrían tenía tenías teníamos teníais tenían tuve tuviste tuvo tuvimos tuvisteis tuvieron si le les ha había han después luego aún todavía cada dos tres otra otro sólo solo mismo misma vez veces bajo tras según hacia""".split())
SUBORD = re.compile(r"\b(que|porque|aunque|cuando|mientras|donde|como|si|para que|hasta que|antes de que|después de que|puesto que|ya que|sino|cuyo|cuya|quien|quienes|cual|cuales)\b", re.I)

def grupo(pov):
    p = str(pov)
    if "Jean" in p and "→" not in p: return "jean"
    first = p.split("→")[0].strip().split()[0] if p.strip() else ""
    if first in ("Maja", "Nora", "Jessie"): return "familia"
    return "otros"

def analizar(orden):
    G = collections.defaultdict(lambda: {"frases": [], "parrafos": [], "w_dial": 0, "w_narr": 0, "w_reg": 0, "subord": 0, "narr_tokens": 0,
                                         "lex": collections.Counter(), "cierres": collections.Counter(), "arranques": collections.Counter(), "n_caps": 0})
    for d in orden:
        g = grupo(d["fm"].get("pov")); GG = [G[g], G["global"]]
        for e in GG: e["n_caps"] += 1
        pars = [p for p in aa.paragraphs(d["body"]) if not aa.es_dinkus(p)]
        for p in pars:
            w = aa.count_words(p)
            if aa.es_dialogo(p):
                for e in GG: e["w_dial"] += w
            elif p.startswith("`") or p.startswith(">"):
                for e in GG: e["w_reg"] += w
            else:
                for e in GG:
                    e["w_narr"] += w; e["parrafos"].append(w)
                    plano = aa.strip_markdown(p)
                    fr = aa.sentences(plano)
                    e["frases"] += [len(f.split()) for f in fr if f.split()]
                    e["subord"] += len(SUBORD.findall(plano)); e["narr_tokens"] += len(plano.split())
                    for tk in re.findall(r"[a-záéíóúñü]+", plano.lower()):
                        if tk not in STOP and len(tk) > 3: e["lex"][tk] += 1
                    for f in fr:
                        m = re.match(r"^(\w+)", f)
                        if m: e["arranques"][m.group(1)] += 1
        for esc in aa.split_scenes(d["body"]):
            ps = aa.paragraphs(esc)
            if not ps: continue
            last = ps[-1]
            tipo = "diálogo" if aa.es_dialogo(last) else ("registro" if last.startswith("`") or last.startswith(">") else "narración")
            for e in GG: e["cierres"][tipo] += 1
    out = {}
    for g, e in G.items():
        fr = e["frases"]
        if not fr: continue
        fr_sorted = sorted(fr)
        def pct(x): return round(100 * sum(1 for l in fr if x(l)) / len(fr), 1)
        tot = e["w_dial"] + e["w_narr"] + e["w_reg"] or 1
        out[g] = {"capitulos": e["n_caps"], "frases_narracion": len(fr), "frase_media": round(statistics.mean(fr), 2), "frase_mediana": statistics.median(fr),
                  "frase_p10": fr_sorted[len(fr)//10], "frase_p90": fr_sorted[9*len(fr)//10], "frase_max": max(fr),
                  "pct_frases_le5": pct(lambda l: l <= 5), "pct_frases_6_12": pct(lambda l: 6 <= l <= 12), "pct_frases_13_20": pct(lambda l: 13 <= l <= 20),
                  "pct_frases_21_30": pct(lambda l: 21 <= l <= 30), "pct_frases_ge31": pct(lambda l: l >= 31),
                  "pct_dialogo": round(100 * e["w_dial"] / tot, 1), "pct_narracion": round(100 * e["w_narr"] / tot, 1), "pct_registro": round(100 * e["w_reg"] / tot, 1),
                  "subordinantes_por_100_palabras": round(100 * e["subord"] / (e["narr_tokens"] or 1), 2),
                  "parrafo_medio_palabras": round(statistics.mean(e["parrafos"]), 1) if e["parrafos"] else 0,
                  "pct_parrafos_1_frase": None,
                  "cierres_escena": dict(e["cierres"]),
                  "lexico_top60": e["lex"].most_common(60), "arranques_frase_top25": e["arranques"].most_common(25)}
    return out

def main():
    et = sys.argv[1] if len(sys.argv) > 1 else "v0"
    R = analizar(aa.reading_order())
    os.makedirs(aa.INFORMES, exist_ok=True)
    json.dump(R, open(os.path.join(aa.BIBLIA, f"b6-huella-datos-{et}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = [f"# B6 · Huella estilística — datos cuantitativos ({et})\n"]
    for g in ["global", "jean", "familia", "otros"]:
        if g not in R: continue
        e = R[g]
        L.append(f"## Grupo: {g} ({e['capitulos']} capítulos)\n")
        L.append(f"- Frases de narración: {e['frases_narracion']} · media {e['frase_media']} palabras · mediana {e['frase_mediana']} · p10 {e['frase_p10']} · p90 {e['frase_p90']} · máx {e['frase_max']}")
        L.append(f"- Distribución: ≤5: {e['pct_frases_le5']} % · 6–12: {e['pct_frases_6_12']} % · 13–20: {e['pct_frases_13_20']} % · 21–30: {e['pct_frases_21_30']} % · ≥31: {e['pct_frases_ge31']} %")
        L.append(f"- Diálogo {e['pct_dialogo']} % · narración {e['pct_narracion']} % · registros `…` {e['pct_registro']} % · subordinantes/100 palabras de narración: {e['subordinantes_por_100_palabras']} · párrafo medio {e['parrafo_medio_palabras']} palabras")
        L.append(f"- Cierres de escena por tipo: {e['cierres_escena']}")
        L.append(f"- Léxico frecuente (sin stopwords): {', '.join(f'{w} ({c})' for w, c in e['lexico_top60'][:40])}")
        L.append(f"- Arranques de frase más frecuentes: {', '.join(f'{w} ({c})' for w, c in e['arranques_frase_top25'][:15])}\n")
    open(os.path.join(aa.INFORMES, f"b6-huella-{et}.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[:12]))

if __name__ == "__main__":
    main()
