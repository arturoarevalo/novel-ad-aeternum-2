#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor adversarial de inserciones (riesgo «hinchazón», §8 del plan; formaliza la auditoría del 20% que el plan
encarga a A0). Compara la versión base de un capítulo (por defecto el tag `v0`) con la versión del árbol de
trabajo, y somete CADA inserción a una sola pregunta: ¿paga su etiqueta de función, o es relleno?

Se ejecuta con el motor `codex` (`gpt-5.6-sol`, esfuerzo max) a propósito: es un revisor de OTRA familia de
modelos auditando prosa escrita por agentes Anthropic. Un evaluador que comparte priors estéticos con el
generador tiende a aprobar lo que el generador considera bueno; aquí queremos justo lo contrario.

NO es un lector frío y no sustituye a ningún gate: recibe la orden de trabajo y las dos versiones del capítulo
(nunca el plan, la crítica de referencia, la biblia ni los informes de gate). Su salida es un informe con
veredicto por inserción; quien decide borrar es A0.

Uso:
  auditor-adverso.sh <cap-NN.md|cap-nN.md> [--orden ordenes/OT-NN.md] [--base v0] [--salida informe.md]
                     [--modelo ID] [--esfuerzo E] [--timeout SEG] [--dir DIR]
"""
import argparse, datetime, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aa
import motor_codex

INSTRUCCIONES = """Eres un editor literario veterano, escéptico y ajeno al equipo que ha escrito esta expansión. Te han contratado para lo contrario de aplaudir: para demostrar, cuando se pueda, que el material añadido a un capítulo NO se ha ganado su sitio. La historia de este manuscrito es que cada revisión anterior lo empeoró; tu trabajo es impedir que vuelva a pasar por acumulación de palabras tibias.

CONTEXTO DE TRABAJO. La novela se está expandiendo bajo una regla: expandir no es engordar. Toda inserción debe cumplir UNA función declarada, y solo se admiten estas seis:
- ORIENTACIÓN: da al lector un asidero concreto para no perderse (un caso, un objeto, un marcador temporal). No es explicación: un glosario, una metáfora explicativa del narrador o un personaje que pregunta «¿y eso qué significa?» para informar al lector NO son orientación, son sobre-explicación, y se rechazan.
- INTERIORIDAD: lo que un personaje siente o decide, entrando por percepción, memoria o decisión, no por monólogo emocional ni por nombrar la emoción.
- TENSIÓN: aumenta la presión dramática de una escena existente.
- AGENCIA: un antagonista o un personaje hace algo con consecuencia, en vez de enunciarse.
- TEXTURA: concreción sensorial o de oficio que hace imaginable un mundo ya establecido.
- PAGO: cobra un elemento sembrado antes en el libro.
Una inserción sin función identificable, o cuya función está ya cubierta por texto contiguo, es relleno.

QUÉ RECIBES. La orden de trabajo del capítulo (lo que se pedía y con qué criterio de aceptación), el capítulo en su versión ANTERIOR y el capítulo en su versión ACTUAL. No tienes acceso a nada más y no debes suponer que existe.

CÓMO TRABAJAS. Lee las dos versiones enteras. Localiza cada tramo añadido o reescrito. Para cada uno: cita las primeras palabras y las últimas (lo justo para identificarlo), di qué función declara o se le supone, y emite veredicto:
- PAGA — la función se cumple y el capítulo sería peor sin ella.
- DUDOSA — cumple a medias, o cumple algo que otro pasaje ya cumplía.
- NO PAGA — relleno, redundancia, explicación de lo que ya se entendía, o adorno.
Por defecto, una inserción NO paga: que pague debe demostrarse. Cuando el veredicto no sea PAGA, indica exactamente qué palabras cortarías (cita literal del tramo a suprimir) y cuántas palabras se ahorran aproximadamente.

ALERTAS DURAS (revísalas siempre y decláralas aunque no te las pregunten): (a) si alguna inserción explica el suicidio de un personaje con una causa única, lo romantiza, lo dulcifica o describe o insinúa el método o el acto, es un VETO: cítala literalmente y márcala como VETO; (b) si el narrador —no un personaje— pasa a explicar el funcionamiento del sistema tecnológico, márcalo como SOBRE-EXPLICACIÓN; (c) si la versión actual introduce más de UNA regla o mecanismo nuevo del mundo que el lector no haya visto operar antes, márcalo como MECÁNICA; (d) si una voz de personaje suena a otra voz del mismo libro, márcalo como VOZ.

FORMATO DE SALIDA (español, obligatorio). Primero una línea con un JSON válido: {"inserciones": N, "pagan": N, "dudosas": N, "no_pagan": N, "palabras_recortables": N, "alertas": ["VETO"|"SOBRE-EXPLICACIÓN"|"MECÁNICA"|"VOZ"]} (lista vacía si no hay). Después, una sección por inserción con su cita, función, veredicto y recorte propuesto; y un cierre de cinco líneas como máximo: qué gana el capítulo de verdad con esta expansión, y qué recortarías tú si solo pudieras conservar la mitad de lo añadido. Sé concreto y cita siempre; nada de valoraciones generales sin cita."""


def texto_sin_frontmatter(contenido):
    _fm, _l, cuerpo = aa.parse_frontmatter(contenido)
    return cuerpo.strip()


def version_git(ref, rel):
    r = subprocess.run(["git", "show", f"{ref}:{rel}"], capture_output=True, text=True, cwd=aa.ROOT)
    if r.returncode != 0:
        return None
    return texto_sin_frontmatter(r.stdout)


def preparar_dir(base, sub):
    base = base or os.environ.get("AA_FRIO_DIR") or "/tmp/aa-frio"
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    d = os.path.join(base, f"{ts}-{sub}")
    os.makedirs(d, exist_ok=True)
    raiz = os.path.realpath(aa.ROOT)
    if os.path.realpath(d).startswith(raiz + os.sep):
        sys.exit("ERROR: el directorio de ejecución está dentro del repositorio.")
    return d


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("capitulo", help="fichero de capitulos/ (cap-NN.md)")
    ap.add_argument("--orden", help="orden de trabajo (por defecto, la del campo `ot:` del frontmatter)")
    ap.add_argument("--base", default="v0", help="referencia git de la versión anterior (por defecto v0)")
    ap.add_argument("--salida", help="informe de salida (por defecto informes/auditoria-adversa-<cap>.md)")
    ap.add_argument("--modelo", default=motor_codex.MODELO_POR_DEFECTO)
    ap.add_argument("--esfuerzo", default="max")
    ap.add_argument("--timeout", type=int, default=3000)
    ap.add_argument("--dir", help="directorio de ejecución fuera del repo (env AA_FRIO_DIR)")
    ap.add_argument("--seco", action="store_true", help="prepara el mensaje y no llama al modelo (comprobación)")
    args = ap.parse_args()

    if not motor_codex.disponible():
        sys.exit("ERROR: `codex` no está instalado o no está en el PATH.")

    nombre = os.path.basename(args.capitulo)
    path = os.path.join(aa.CAPITULOS, nombre)
    if not os.path.isfile(path):
        sys.exit(f"ERROR: no existe {path}")
    contenido = open(path, encoding="utf-8").read()
    fm, _l, _c = aa.parse_frontmatter(contenido)
    actual = texto_sin_frontmatter(contenido)
    rel = os.path.relpath(path, aa.ROOT)
    base = version_git(args.base, rel)

    orden_path = args.orden
    if not orden_path and fm.get("ot"):
        orden_path = os.path.join("ordenes", f"{fm['ot']}.md")
    orden_txt = ""
    if orden_path:
        p = orden_path if os.path.isabs(orden_path) else os.path.join(aa.ROOT, orden_path)
        if not os.path.isfile(p):
            sys.exit(f"ERROR: no existe la orden de trabajo {orden_path}")
        orden_txt = open(p, encoding="utf-8").read().strip()

    partes = []
    if orden_txt:
        partes.append("===== ORDEN DE TRABAJO =====\n" + orden_txt + "\n===== FIN DE LA ORDEN =====")
    if base is None:
        partes.append(f"(No hay versión anterior: «{nombre}» es un capítulo nuevo. Audita entonces el capítulo "
                      "entero como si todo él fuese material insertado que debe justificar su existencia.)")
    else:
        partes.append(f"===== VERSIÓN ANTERIOR ({args.base}, {aa.count_words(base)} palabras) =====\n{base}\n"
                      "===== FIN DE LA VERSIÓN ANTERIOR =====")
    partes.append(f"===== VERSIÓN ACTUAL ({aa.count_words(actual)} palabras) =====\n{actual}\n"
                  "===== FIN DE LA VERSIÓN ACTUAL =====")
    mensaje = "\n\n".join(partes) + "\n"

    d = preparar_dir(args.dir, "auditor-adverso-" + nombre.replace(".md", ""))
    with open(os.path.join(d, "mensaje.txt"), "w", encoding="utf-8") as f:
        f.write(mensaje)
    salida = args.salida or os.path.join("informes", f"auditoria-adversa-{nombre.replace('.md','')}.md")
    if not os.path.isabs(salida):
        salida = os.path.join(aa.ROOT, salida)

    delta = aa.count_words(actual) - (aa.count_words(base) if base else 0)
    print(f"→ auditor adverso · {nombre} · base {args.base} · Δ {delta:+d} palabras · modelo {args.modelo} "
          f"(esfuerzo {args.esfuerzo}) · cwd {d}", flush=True)
    if args.seco:
        print(f"[seco] mensaje de {len(mensaje):,} caracteres en {os.path.join(d, 'mensaje.txt')}; "
              f"orden: {orden_path or '(ninguna)'}; base {'ausente (capítulo nuevo)' if base is None else args.base}. "
              f"No se ha llamado al modelo.")
        return
    data = motor_codex.ejecutar(INSTRUCCIONES, mensaje, args.modelo, args.esfuerzo, d, args.timeout)
    uso = motor_codex.resumen_uso(data, args.modelo)
    if data.get("is_error") or not data.get("result"):
        sys.exit(f"ERROR: la ejecución falló (rc {data.get('_returncode')}): {data.get('_stderr')}\n"
                 f"errores: {data.get('errores')}")
    if not uso["modelos_usados"]:
        sys.exit(f"ERROR: codex no declaró el modelo usado; informe NO escrito (crudo en {d}).")
    if args.modelo not in uso["modelos_usados"]:
        sys.exit(f"ERROR: modelo usado {uso['modelos_usados']} ≠ pedido {args.modelo}; informe NO escrito.")

    hoy = datetime.date.today().isoformat()
    cab = [f"# Auditoría adversarial de inserciones · {nombre} · {hoy}", "",
           f"> Motor `codex` ({motor_codex.version()}, modelo declarado `{uso['modelos_usados'][0]}`, esfuerzo "
           f"`{uso.get('esfuerzo_declarado')}`) desde `{d}`, fuera del repositorio, sandbox read-only con el shell "
           f"inoperante. Insumo: "
           + (f"`{orden_path}` + " if orden_txt else "")
           + f"`{rel}` en `{args.base}` ({aa.count_words(base) if base else 0} palabras) y en el árbol de trabajo "
           f"({aa.count_words(actual)} palabras), Δ {delta:+d}. Sin plan, sin crítica de referencia, sin biblia, sin "
           f"informes. {uso['input_tokens']:,} tokens · {round((uso['duracion_ms'] or 0)/1000)} s · suscripción ChatGPT.",
           "", "> Este informe NO es un gate: A0 decide qué se borra.", ""]
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    with open(salida, "w", encoding="utf-8") as f:
        f.write("\n".join(cab) + data["result"].strip() + "\n")
    print(f"✓ escrito {os.path.relpath(salida, aa.ROOT)} · {uso['input_tokens']:,} tokens · "
          f"{round((uso['duracion_ms'] or 0)/1000)} s")


if __name__ == "__main__":
    main()
