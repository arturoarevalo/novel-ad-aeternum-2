#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lectura EN FRÍO REAL para A6 (críticos), A6b (lectores beta) y lector-frio (test por capítulo).

Por qué existe: los subagentes lanzados desde la sesión reciben SIEMPRE CLAUDE.md (y la memoria de usuario)
en su contexto, así que nunca leen «en frío» (verificado el 2026-08-16 con una sonda haiku: ve la lista de
protegidos, la existencia de capítulos nuevos, el estado del proceso…). Esta herramienta lanza el rol con
`claude -p` desde un directorio FUERA del repositorio, con:
  - system prompt = cuerpo del fichero del agente en .claude/agents/<rol>.md (la rúbrica), nada más;
  - modelo y esfuerzo FIJADOS por ID (frontmatter del agente, salvo override explícito);
  - sin herramientas (--tools ""), sin MCP, sin skills, sin settings de proyecto, sin persistencia de sesión;
  - variables de entorno de la sesión padre eliminadas (CLAUDECODE, CLAUDE_CODE_*, …);
  - insumo ÚNICO: el texto del compilado / extracto, inline en el mensaje (solo se admiten ficheros bajo compilado/).
Guarda el resultado en un .md con cabecera de trazabilidad (modelo real usado, tokens, coste, duración, sha256 del insumo)
y el JSON crudo de `claude -p` en el directorio de ejecución.

Uso:
  critica-fria.sh <rol> <insumo.md> [<insumo-2.md>] --salida <informe.md> [--modelo ID] [--esfuerzo E]
                  [--mensaje "instrucción previa"] [--dir DIR] [--timeout SEG] [--sin-cabecera]
  critica-fria.sh --sonda [--dir DIR]           # comprueba que el contexto de ejecución está limpio (haiku)
Env: AA_FRIO_DIR (directorio base de ejecución, fuera del repo; por defecto /tmp/aa-frio).

Motores (`--motor`, o campo `motor:` del frontmatter del agente; por defecto `claude`):
  - `claude` → `claude -p` sin herramientas, system prompt = rúbrica (protocolo original).
  - `codex`  → `codex exec` (OpenAI, suscripción del autor) para los roles que deben venir de OTRA familia de
               modelos: A6-3 (diversidad de conjunto, §2.5) y la variante de control de M6b. Aislamiento y
               salvedades en `herramientas/lib/motor_codex.py` y en `informes/d1-aislamiento.md` §5. La sonda de
               codex verifica ADEMÁS que su shell no puede leer el repositorio, y falla cerrada.
  Opciones propias: `--motor codex`, `--esquema <schema.json>` (fuerza la forma de la respuesta final).
"""
import argparse, datetime, hashlib, json, os, re, shutil, subprocess, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa
import motor_codex

AGENTES = os.path.join(aa.ROOT, ".claude", "agents")
SONDA_MODELO = "claude-haiku-4-5-20251001"
FLAGS_AISLAMIENTO = ["--tools", "", "--strict-mcp-config", "--disable-slash-commands",
                     "--setting-sources", "", "--no-session-persistence", "--output-format", "json"]
ENV_PROHIBIDAS_PREFIJO = ("CLAUDE_CODE_", "CLAUDE_")
ENV_PROHIBIDAS = {"CLAUDECODE", "AI_AGENT"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def leer_agente(rol):
    p = os.path.join(AGENTES, rol + ".md")
    if not os.path.isfile(p):
        sys.exit(f"ERROR: no existe el agente {os.path.relpath(p, aa.ROOT)}")
    fm, _lineas, body = aa.parse_frontmatter(open(p, encoding="utf-8").read())
    return fm, body.strip(), p


def entorno_limpio():
    env = {}
    for k, v in os.environ.items():
        if k in ENV_PROHIBIDAS or k.startswith(ENV_PROHIBIDAS_PREFIJO):
            continue
        env[k] = v
    return env


def comprobar_dir_ejecucion(d):
    """El directorio de ejecución debe estar fuera del repo y sin CLAUDE.md/.claude en él ni en sus ancestros."""
    d = os.path.realpath(d)
    raiz = os.path.realpath(aa.ROOT)
    if d == raiz or d.startswith(raiz + os.sep):
        sys.exit(f"ERROR: el directorio de ejecución {d} está DENTRO del repositorio; los lectores en frío se ejecutan fuera.")
    cur = d
    problemas = []
    while True:
        for nombre in ("CLAUDE.md", "CLAUDE.local.md", ".claude"):
            if os.path.exists(os.path.join(cur, nombre)):
                problemas.append(os.path.join(cur, nombre))
        padre = os.path.dirname(cur)
        if padre == cur:
            break
        cur = padre
    home = os.path.expanduser("~")
    for nombre in ("CLAUDE.md", ".claude/CLAUDE.md"):
        if os.path.exists(os.path.join(home, nombre)):
            problemas.append(os.path.join(home, nombre))
    if problemas:
        sys.exit("ERROR: el contexto de ejecución NO está limpio; existen instrucciones que el lector frío heredaría:\n  "
                 + "\n  ".join(problemas))
    return d


def comprobar_insumo(path, libre=False):
    ap = os.path.realpath(path)
    comp = os.path.realpath(aa.COMPILADO)
    if libre:
        # insumo fuera de compilado/ (p. ej. la muestra ciega M6b informes/m6-muestra-vX.md); se mantienen las prohibiciones duras
        pass
    elif not (ap == comp or ap.startswith(comp + os.sep)):
        sys.exit(f"ERROR: el insumo {path} no está bajo compilado/. Los lectores en frío solo reciben compilados o extractos "
                 f"(nunca capítulos con frontmatter, biblia, plan, informes).")
    if not os.path.isfile(ap):
        sys.exit(f"ERROR: no existe {path}")
    return ap


def construir_mensaje(insumos, mensaje_extra):
    partes = []
    if mensaje_extra:
        partes.append(mensaje_extra.strip())
    if len(insumos) == 1:
        partes.append("A continuación tienes el texto íntegro que debes leer (es tu ÚNICO insumo; no existe nada más que "
                      "consultar). Léelo completo, de principio a fin, y solo después escribe tu respuesta siguiendo tus "
                      "instrucciones y tu formato de salida.")
    else:
        partes.append(f"A continuación tienes {len(insumos)} textos, etiquetados como MANUSCRITO A, B… (tu ÚNICO insumo). "
                      "Léelos completos y solo después responde siguiendo tus instrucciones y tu formato de salida.")
    for i, p in enumerate(insumos):
        etiqueta = chr(ord("A") + i)
        cab = f"MANUSCRITO {etiqueta}" if len(insumos) > 1 else "TEXTO"
        with open(p, encoding="utf-8") as f:
            texto = f.read().strip("\n")
        partes.append(f"===== INICIO DEL {cab} =====\n{texto}\n===== FIN DEL {cab} =====")
    return "\n\n".join(partes) + "\n"


def ejecutar_claude(system_prompt, mensaje, modelo, esfuerzo, cwd, timeout, extra_flags=None):
    cmd = ["claude", "-p", "--model", modelo, "--system-prompt", system_prompt] + FLAGS_AISLAMIENTO
    if esfuerzo:
        cmd += ["--effort", str(esfuerzo)]
    if extra_flags:
        cmd += extra_flags
    t0 = time.time()
    r = subprocess.run(cmd, input=mensaje, capture_output=True, text=True, cwd=cwd, env=entorno_limpio(), timeout=timeout)
    dur = time.time() - t0
    salida = r.stdout.strip()
    try:
        data = json.loads(salida)
    except Exception:
        # claude -p a veces emite líneas previas; quedarse con el último objeto JSON de la salida
        m = re.findall(r"^\{.*\}$", salida, re.M)
        if not m:
            sys.exit(f"ERROR: `claude -p` no devolvió JSON (código {r.returncode}).\nSTDOUT:\n{salida[:2000]}\nSTDERR:\n{r.stderr[:2000]}")
        data = json.loads(m[-1])
    data["_duracion_local_s"] = round(dur, 1)
    data["_returncode"] = r.returncode
    data["_stderr"] = r.stderr[-2000:]
    return data


def resumen_uso(data, modelo_pedido):
    mu = data.get("modelUsage") or {}
    usados = list(mu.keys())
    tot_in = tot_out = tot_cache_r = tot_cache_w = 0
    for k, v in mu.items():
        tot_in += v.get("inputTokens", 0); tot_out += v.get("outputTokens", 0)
        tot_cache_r += v.get("cacheReadInputTokens", 0); tot_cache_w += v.get("cacheCreationInputTokens", 0)
    u = data.get("usage") or {}
    thinking = (u.get("output_tokens_details") or {}).get("thinking_tokens")
    canon = [v.get("canonicalModel") or k for k, v in mu.items()]
    por_modelo = {k: f"in {v.get('inputTokens',0):,} / cache_w {v.get('cacheCreationInputTokens',0):,} / cache_r {v.get('cacheReadInputTokens',0):,} / out {v.get('outputTokens',0):,}"
                  for k, v in mu.items()}
    return {
        "por_modelo": por_modelo,
        "modelo_pedido": modelo_pedido, "modelos_usados": usados, "modelos_canonicos": canon,
        "input_tokens": tot_in, "output_tokens": tot_out, "cache_read": tot_cache_r, "cache_write": tot_cache_w,
        "thinking_tokens": thinking, "coste_usd": data.get("total_cost_usd"), "duracion_ms": data.get("duration_ms"),
        "duracion_api_ms": data.get("duration_api_ms"), "num_turns": data.get("num_turns"),
        "is_error": data.get("is_error"), "stop_reason": data.get("stop_reason"), "session_id": data.get("session_id"),
        "context_window": [v.get("contextWindow") for v in mu.values()],
    }


def modelo_coincide(pedido, usados_canon, usados):
    base = re.sub(r"\[.*\]$", "", pedido)
    for u in list(usados_canon) + list(usados):
        if not u:
            continue
        if u == pedido or u == base or u.startswith(base) or base.startswith(u):
            return True
    return False


def sonda_codex(args):
    """Sonda de aislamiento del motor codex. Falla cerrada: exige (1) contexto sin instrucciones de proyecto ni
    memoria, y (2) que el shell del agente NO pueda leer el repositorio (bwrap sin namespaces en este contenedor).
    (2) es una propiedad del ENTORNO, no de la configuración: si algún día el host habilita user namespaces, esta
    sonda lo detecta antes de que un lector frío pueda husmear el plan."""
    if not motor_codex.disponible():
        sys.exit("ERROR: `codex` no está instalado o no está en el PATH.")
    d = comprobar_dir_ejecucion(preparar_dir(args.dir, "sonda-codex"))
    modelo = args.modelo or motor_codex.MODELO_POR_DEFECTO
    instr = "Eres un lector. Respondes en español, con literalidad y sin inventar. No eres un agente de programación."
    print(f"=== SONDA DE AISLAMIENTO · motor codex ({motor_codex.version()}) · modelo {modelo} · cwd {d} ===")

    inoperante, detalle = motor_codex.bwrap_inoperante()
    print(f"[1/3] jaula local (bwrap): {'INOPERANTE — el shell de codex no puede ejecutar nada' if inoperante else 'OPERATIVA'} · {detalle}")

    d1 = os.path.join(d, "contexto"); os.makedirs(d1, exist_ok=True)
    ctx = motor_codex.ejecutar(instr, motor_codex.PROMPT_SONDA_CONTEXTO, modelo, "low", d1, args.timeout)
    uso_ctx = motor_codex.resumen_uso(ctx, modelo)
    if not (ctx.get("result") or "").strip():
        print("[2/3] contexto: SIN RESPUESTA · rc", ctx.get("_returncode"), "· stderr:", (ctx.get("_stderr") or "").strip()[:600])
    print("[2/3] contexto:\n" + (ctx.get("result") or "(sin respuesta)").strip())
    print(f"      tokens de entrada: {uso_ctx['input_tokens']:,} (base de Codex ≈ 10k; sin AGENTS.md ni memoria)")

    d2 = os.path.join(d, "fuga"); os.makedirs(d2, exist_ok=True)
    fuga = motor_codex.ejecutar(instr, motor_codex.PROMPT_SONDA_FUGA, modelo, "low", d2, args.timeout)
    texto_fuga = (fuga.get("result") or "")
    filtrados = [m for m in motor_codex.MARCADORES_FUGA if m.lower() in texto_fuga.lower()]
    print("[3/3] fuga (intento real de leer el repositorio):\n" + texto_fuga.strip()[:1200])

    limpio_ctx = ("NINGUNA" in (ctx.get("result") or "").upper()) and uso_ctx["input_tokens"] < 15000
    ok = inoperante and limpio_ctx and not filtrados
    print("\nVEREDICTO:", "LIMPIO — codex utilizable como lector frío" if ok else
          "SOSPECHOSO — NO usar codex para lectura fría: " +
          "; ".join(filter(None, [None if inoperante else "el shell puede ejecutar comandos",
                                  None if limpio_ctx else "el contexto no está limpio",
                                  ("fuga confirmada: " + ", ".join(filtrados)) if filtrados else None])))
    print("Evidencia en", d)
    return 0 if ok else 2


def sonda(args):
    if (args.motor or "claude") == "codex":
        return sonda_codex(args)
    d = comprobar_dir_ejecucion(preparar_dir(args.dir, "sonda"))
    sp = "Eres un asistente. Responde con literalidad y sin inventar."
    msg = ("Auditoría de contexto. Responde en español y en pocas líneas: (a) ¿tienes en contexto instrucciones de proyecto "
           "(CLAUDE.md), memoria de usuario, recordatorios de sistema o contexto de repositorio? Si sí, cita literalmente la "
           "primera línea de cada uno; si no, escribe NINGUNA. (b) ¿Aparecen en tu contexto las palabras «Ad aeternum», "
           "«Koppangen», «Maja», «Soldagen», «proteccion», «lector frío»? (c) ¿Qué herramientas tienes? (d) ¿Cuál es tu "
           "directorio de trabajo según tu contexto? (e) Cita literalmente las tres primeras líneas de tu system prompt.")
    data = ejecutar_claude(sp, msg, args.modelo or SONDA_MODELO, "low", d, args.timeout)
    uso = resumen_uso(data, args.modelo or SONDA_MODELO)
    print("=== SONDA DE AISLAMIENTO (claude -p desde", d, ") ===")
    print(data.get("result", "").strip())
    print("--- uso:", json.dumps(uso, ensure_ascii=False))
    ok = (not data.get("is_error")) and uso["input_tokens"] < 3000
    print("VEREDICTO:", "LIMPIO (contexto de entrada de %d tokens)" % uso["input_tokens"] if ok else "SOSPECHOSO — revisar")
    return 0 if ok else 2


def preparar_dir(base, sub):
    base = base or os.environ.get("AA_FRIO_DIR") or "/tmp/aa-frio"
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    d = os.path.join(base, f"{ts}-{sub}")
    os.makedirs(d, exist_ok=True)
    return d


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rol", nargs="?", help="nombre del agente en .claude/agents/ (a6-critico-1, lector-frio, a6b-beta-…)")
    ap.add_argument("insumos", nargs="*", help="uno o dos ficheros bajo compilado/ (compilado completo o extracto)")
    ap.add_argument("--salida", help="fichero .md de salida (p. ej. informes/a6-v0-critico-1-frio.md)")
    ap.add_argument("--modelo", help="override del modelo (por defecto, el del frontmatter del agente)")
    ap.add_argument("--esfuerzo", help="override del esfuerzo (por defecto, el del frontmatter del agente)")
    ap.add_argument("--mensaje", default="", help="instrucción breve que precede al texto (p. ej. «Capítulo 8 de 41»)")
    ap.add_argument("--dir", help="directorio base de ejecución FUERA del repo (env AA_FRIO_DIR; por defecto /tmp/aa-frio)")
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--sin-cabecera", action="store_true", help="escribe solo la respuesta, sin cabecera de trazabilidad")
    ap.add_argument("--sonda", action="store_true", help="solo comprobar que el contexto de ejecución está limpio")
    ap.add_argument("--etiqueta", default="", help="etiqueta de versión para la cabecera (v0, v1…)")
    ap.add_argument("--motor", choices=["claude", "codex"],
                    help="motor de ejecución (por defecto, el campo `motor:` del agente; si no lo hay, claude)")
    ap.add_argument("--esquema", help="JSON Schema que fuerza la forma de la respuesta final (solo motor codex)")
    ap.add_argument("--sin-verificar-modelo", action="store_true",
                    help="no abortar si el motor no declara qué modelo usó (solo para depuración)")
    ap.add_argument("--insumo-libre", action="store_true",
                    help="admite un insumo fuera de compilado/ (solo muestras ciegas como informes/m6-muestra-vX.md; nunca plan, crítica, biblia, gates)")
    args = ap.parse_args()

    if args.sonda:
        sys.exit(sonda(args))
    if not args.rol or not args.insumos or not args.salida:
        ap.error("hacen falta <rol>, al menos un <insumo> y --salida")

    fm, system_prompt, agente_path = leer_agente(args.rol)
    motor = args.motor or fm.get("motor") or "claude"
    modelo = args.modelo or fm.get("model")
    esfuerzo = args.esfuerzo or fm.get("effort")
    if motor == "codex":
        if not motor_codex.disponible():
            sys.exit("ERROR: `codex` no está instalado o no está en el PATH.")
        inoperante, detalle = motor_codex.bwrap_inoperante()
        if not inoperante:
            sys.exit("ERROR: el shell de codex ESTÁ operativo en este entorno (%s): un lector frío podría leer el "
                     "repositorio. Ejecuta `herramientas/critica-fria.sh --sonda --motor codex` y revisa "
                     "informes/d1-aislamiento.md §5 antes de continuar." % detalle)
        if args.modelo is None and (not modelo or modelo.startswith("claude")):
            sys.exit("ERROR: el agente no fija un modelo de codex; usa --modelo (p. ej. gpt-5.6-sol).")
    if not modelo or modelo == "inherit":
        sys.exit("ERROR: el agente no fija modelo por ID (model: inherit); los lectores en frío deben tener modelo FIJADO. Usa --modelo.")
    insumos = [comprobar_insumo(p, args.insumo_libre) for p in args.insumos]
    salida = args.salida
    if not os.path.isabs(salida):
        salida = os.path.join(aa.ROOT, salida)
    for p in insumos:
        rel = os.path.relpath(p, aa.ROOT)
        for prohibido in ("plan-revision", "critica-ad-aeternum", "changelog", "gate", "biblia/", "estado-proceso", "a6-", "d1-", "m6-clave", "dashboard", "metricas-"):
            if prohibido in rel:
                sys.exit(f"ERROR: insumo prohibido para un lector frío: {p}")
        if not args.insumo_libre and rel.startswith("informes/"):
            sys.exit(f"ERROR: insumo prohibido para un lector frío: {p}")

    d = comprobar_dir_ejecucion(preparar_dir(args.dir, args.rol))
    mensaje = construir_mensaje(insumos, args.mensaje)
    with open(os.path.join(d, "system-prompt.txt"), "w", encoding="utf-8") as f:
        f.write(system_prompt + "\n")
    with open(os.path.join(d, "mensaje.txt"), "w", encoding="utf-8") as f:
        f.write(mensaje)

    print(f"→ {args.rol} · motor {motor} · modelo {modelo} · esfuerzo {esfuerzo} · insumo(s): "
          + ", ".join(os.path.relpath(p, aa.ROOT) for p in insumos) + f" · cwd {d}", flush=True)
    if motor == "codex":
        esquema = args.esquema
        if esquema and not os.path.isabs(esquema):
            esquema = os.path.join(aa.ROOT, esquema)
        data = motor_codex.ejecutar(system_prompt, mensaje, modelo, esfuerzo, d, args.timeout, schema=esquema)
        uso = motor_codex.resumen_uso(data, modelo)
    else:
        data = ejecutar_claude(system_prompt, mensaje, modelo, esfuerzo, d, args.timeout)
        uso = resumen_uso(data, modelo)
    with open(os.path.join(d, "resultado.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    if data.get("is_error") or not data.get("result"):
        sys.exit(f"ERROR: la ejecución falló: {json.dumps(uso, ensure_ascii=False)}\nresult: {str(data.get('result'))[:1500]}\nstderr: {data.get('_stderr')}")
    if motor == "codex" and not uso["modelos_usados"]:
        if not args.sin_verificar_modelo:
            sys.exit(f"ERROR: codex no declaró el modelo usado; informe NO escrito (resultado crudo en {d}). "
                     f"Usa --sin-verificar-modelo solo para depurar.")
        uso["modelos_usados"] = [modelo + " (no verificado)"]
    elif not modelo_coincide(modelo, uso["modelos_canonicos"], uso["modelos_usados"]):
        sys.exit(f"ERROR: el modelo usado {uso['modelos_usados']} no coincide con el fijado {modelo}; informe NO escrito "
                 f"(resultado crudo en {d}/resultado.json).")

    resultado = data["result"].strip()
    hoy = datetime.date.today().isoformat()
    cab = []
    if not args.sin_cabecera:
        nombres = ", ".join(f"`{os.path.relpath(p, aa.ROOT)}` (sha256 {sha256(p)[:16]}…, {aa.count_words(open(p, encoding='utf-8').read())} palabras)" for p in insumos)
        cab.append(f"# {args.rol} · {args.etiqueta or 'lectura'} · FRÍO REAL — {hoy}")
        cab.append("")
        if motor == "codex":
            cab.append(f"> Ejecutado con `herramientas/critica-fria.sh --motor codex` (`codex exec` {motor_codex.version()} "
                       f"desde `{d}`, fuera del repositorio; instrucciones de modelo = cuerpo de "
                       f"`{os.path.relpath(agente_path, aa.ROOT)}`; sin AGENTS.md, sin config de usuario, sin memoria de "
                       f"codex, sin búsqueda web, sandbox read-only y sesión efímera; el shell de codex es inoperante en "
                       f"este entorno —bwrap sin namespaces—, verificado antes de lanzar). Insumo único inline: {nombres}."
                       + (f" Instrucción previa: «{args.mensaje.strip()}»." if args.mensaje.strip() else ""))
            cab.append(f"> Modelo pedido `{modelo}` (esfuerzo {esfuerzo}) · declarado por codex: modelo "
                       f"`{', '.join(uso['modelos_usados']) or '—'}`, esfuerzo `{uso.get('esfuerzo_declarado') or '—'}` · "
                       + "; ".join(v for v in uso['por_modelo'].values())
                       + f" · coste: suscripción ChatGPT (sin facturación por token) · "
                       f"{round((uso['duracion_ms'] or 0)/1000)} s · sesión {uso['session_id']}")
        else:
            cab.append(f"> Ejecutado con `herramientas/critica-fria.sh` (claude -p desde `{d}`, fuera del repositorio; system prompt = "
                       f"cuerpo de `{os.path.relpath(agente_path, aa.ROOT)}`; sin herramientas, sin CLAUDE.md, sin memoria, sin MCP; "
                       f"entorno de la sesión padre eliminado). Insumo único inline: {nombres}."
                       + (f" Instrucción previa: «{args.mensaje.strip()}»." if args.mensaje.strip() else ""))
            cab.append(f"> Modelo pedido `{modelo}` (esfuerzo {esfuerzo}) · tokens por modelo: "
                       + "; ".join(f"`{k}`: {v}" for k, v in uso['por_modelo'].items())
                       + f" (la llamada auxiliar de haiku es del harness, no del lector) · razonamiento {uso['thinking_tokens']} · "
                       f"coste {uso['coste_usd']} USD · {round((uso['duracion_ms'] or 0)/1000)} s · turnos {uso['num_turns']} · stop {uso['stop_reason']}")
        cab.append("")
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    with open(salida, "w", encoding="utf-8") as f:
        f.write("\n".join(cab) + resultado + "\n")
    print(f"✓ escrito {os.path.relpath(salida, aa.ROOT)} · {json.dumps(uso, ensure_ascii=False)}")
    # resumen A6: primera línea JSON válida
    m = re.search(r"^\{.*\}$", resultado, re.M)
    if m:
        try:
            print("  notas:", json.dumps(json.loads(m.group(0)), ensure_ascii=False))
        except Exception:
            pass


if __name__ == "__main__":
    main()
