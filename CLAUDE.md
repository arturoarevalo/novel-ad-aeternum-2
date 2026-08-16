# Proyecto: revisión-expansión de la novela «Ad aeternum»

## Contrato de operación

- Plan maestro: `plan-revision-ad-aeternum.md`. **A0 lo lee ÍNTEGRO al arrancar cada sesión** (con la herramienta Read). NO se importa con `@`: todo lo que hay en CLAUDE.md llega al contexto de TODOS los subagentes, y los lectores en frío (A6, A6b, lector-frio) no deben ver jamás el plan.
- Crítica de referencia (baseline de puntuaciones): `critica-ad-aeternum.md`. Solo la lee A0 (al arrancar); jamás se pasa ni se importa para A6/A6b/lector-frio.
- Tú eres A0 (orquestador). Los demás roles son subagentes según §2.1 y §2.5 del plan.
- **Aislamiento de los lectores en frío (regla dura):** A6, A6b, `lector-frio` y `m6-atribuidor` se lanzan ÚNICAMENTE con `herramientas/critica-fria.sh` (`claude -p` desde fuera del repositorio, system prompt = rúbrica del agente, modelo fijado por ID, sin herramientas, insumo único inline: compilado/extracto), NUNCA como subagentes de la sesión: todo subagente hereda CLAUDE.md, la memoria y el email (verificado con sonda haiku el 2026-08-16; los `@`-imports además contaminaban con el plan y la crítica: `informes/a6-v0-critico-{1,2,3}.md`, conservados como evidencia). Protocolo y evidencia: `informes/d1-aislamiento.md`. Ningún prompt ni fichero accesible a un lector frío puede contener el plan, la crítica de referencia, los changelogs ni los informes de gate.

## Estructura del repositorio

- `capitulos/cap-01.md … cap-41.md` — un capítulo por fichero, frontmatter YAML del autor (`capitulo`, `titulo`, `pov`, `fecha`, `estado`, `analepsis`).
- `capitulos/cap-n1.md … cap-n6.md` — capítulos nuevos del plan (tabla 5.1), con `orden_lectura` decimal (§2.4).
- `biblia/metadatos.json` — MANIFIESTO del proyecto: partes (títulos y subtítulos con cuenta atrás), registro de capítulos (n, slug, archivo, origen, palabras), campos editoriales del autor. Fuente de verdad editorial.
- `biblia/` (resto) — B0–B8 generados por A1 en Fase 0.
- `ordenes/`, `informes/`, `protegidos/`, `herramientas/`, `compilado/` — según §2.2.

## Reglas del manifiesto (metadatos.json)

- Campos de AUTOR — `titulo`, `subtitulo`, `autor`, `dedicatoria`, `sinopsis_corta`, `dinkus`, `letras-capitales`, `idioma`, `slug`, `publicacion` — intocables sin gate de autor.
- Campos OPERATIVOS — `capitulos[]`, `partes[].capitulo_inicial/final`, `palabras`, `palabras_objetivo` — solo se modifican vía `herramientas/actualizar-metadatos.sh` (nunca a mano), con historia git.
- En F0: `palabras_objetivo` 65.000 → 85.000; añade `palabras_real` por capítulo (recuento real, sin frontmatter); reescribe `palabras` como presupuesto vF = palabras_real(v0) + `delta_objetivo` (tabla 5.1). M8 lee la banda del manifiesto (objetivo ± 1.000).
- Capítulos nuevos: se registran en `capitulos[]` SOLO tras superar G-A2, con `origen: "REVISIÓN 10"` (convención del autor: cap-33 consta como "REVISIÓN 9").
- Rangos de `partes[]`: NO se tocan durante el trabajo (los `orden_lectura` decimales caen dentro de los rangos vigentes). Renumeración de `capitulo` y rangos: una sola vez, en W7 (pasan a 1–12, 13–24, 25–36, 37–47).
- `persona` por capítulo (p. ej. `"primera"` en cap-38) es contrato estilístico: el validador falla si la prosa no coincide. El cambio de persona del 38 está protegido (Apéndice A).

## Reglas duras (siempre)

- Ficheros con `proteccion: total` — cap-01, cap-03, cap-04, cap-05, cap-09, cap-20, cap-23, cap-41, 00-aviso, 99-recursos — son INTOCABLES: diff = 0 salvo ortotipografía aprobada en gate. Verificación por hash (M9) en pre-commit; hook PreToolUse bloquea Write/Edit sobre ellos.
- Los núcleos con `proteccion: nucleo` (Apéndice A del plan) se verifican por hash de span.
- El tag git `v0` es la baseline congelada: prohibido reescribir historia anterior al tag.
- Carta de sensibilidad (Apéndice F del plan): vinculante en TODO borrador, incluso descartado. Veto de A7 no negociable.
- Máximo 1 mecánica nueva por capítulo de Jean (M2). Toda inserción lleva etiqueta de función; sin etiqueta, se borra.
- Frontmatter: los campos del autor no se eliminan ni renombran jamás; el plan solo AÑADE los suyos (`estado_plan`, `proteccion`, `ot`, `delta_objetivo`, `orden_lectura`). `capitulo` y `titulo` no se renumeran hasta W7. Nada de notas de trabajo en el cuerpo de los capítulos.
- Una rama git por oleada; merge a `main` solo tras superar el gate; un commit por capítulo con el ID de orden de trabajo en el mensaje.
- A6 (críticos fríos) y A6b (beta) reciben ÚNICAMENTE `compilado/ad-aeternum-vX.md` — sin frontmatter, sin dedicatoria ni sinopsis, nunca el plan ni los changelogs.
- En los gates G-A1, G-A2 y G-A3: detente y pregúntame. No los auto-apruebes.

## Comandos

- `herramientas/compilar.sh <etiqueta>` — lee el manifiesto + `orden_lectura`, genera las cabeceras de parte desde `partes[]`, quita frontmatter, excluye dedicatoria/sinopsis, incluye aviso y recursos, escribe en `compilado/` y reporta M8.
- `herramientas/actualizar-metadatos.sh` — única vía de escritura de campos operativos del manifiesto (`palabras-real`, `objetivo`, `presupuestos --v0`, `registrar --gate`, `paratexto`, `renumerar --w7`, `verificar`).
- `herramientas/medir.sh <etiqueta> [--baseline v0]` — ejecuta M1–M10 y vuelca el dashboard en `informes/`.
- `herramientas/proteger.sh baseline|verificar|listar` — M9 (hashes de ficheros `total` y de spans; `--rebaseline --gate` solo para excepciones aprobadas).
- `herramientas/critica-fria.sh <rol> <insumo> --salida <informe.md>` — lectura en frío real (A6/A6b/lector-frio/m6-atribuidor) desde fuera del repo; `--sonda` verifica el aislamiento; env `AA_FRIO_DIR` = directorio de ejecución (scratchpad).
- `herramientas/validar-frontmatter.sh`, `herramientas/auditar-manifiesto.sh`, `herramientas/inyectar-frontmatter.sh` (campos del plan; `--set cap-NN.md estado=en_oleada`), `herramientas/sensibilidad.sh` (pre-chequeo T7: hits nuevos vs baseline de A7), `herramientas/lib/m6_muestra.py` (M6b), `herramientas/lib/m4b_antepuestas.py` (M4b subordinadas antepuestas), `herramientas/lib/huella.py` (B6 datos).
- Hooks: PreToolUse en `.claude/settings.json`; pre-commit vía `git config core.hooksPath herramientas/hooks` (repetir en clones nuevos). Excepción de gate de autor en Bash: prefijo `AA_GATE_AUTOR="motivo"`.
- Los subagentes de `.claude/agents/` (18, con `model`/`effort` de §2.5; `m6-atribuidor` añadido en F1) se indexan al arrancar la sesión: tras crearlos o editarlos hay que reiniciar la sesión para lanzarlos por nombre.
- Documento vivo de estado: `informes/estado-proceso.md`. Gates: `informes/g0-gate.md`, …

## Modelos y esfuerzo

Sesión principal: claude-fable-5 a esfuerzo máximo. Subagentes según la tabla de §2.5 del plan: escritores/línea/sensibilidad con `inherit`; críticos A6 FIJADOS por ID (2× claude-fable-5 + 1× claude-opus-4-8, jueces mixtos también en la A/B ciega); A5 y A6b en claude-opus-4-8; A8 en claude-haiku-4-5 con `effort: low`.

## Estado

- Fase actual: **FASE 2 EN CURSO** (plan estructural: A2 redacta las 47 OT + briefs N1–N6 en la rama `f2-plan-estructural`; merge a `main` tras **G-A1**, gate de autor). W1 (F0 + F1) cerrada: G0 y G1 APROBADOS por el autor y fusionada en `main`. Decisiones de G1 en `informes/registro-gates-autor.md` (M6b ≥ 60 % sustituye a M6 ≥ 80 %; baseline de anti-regresión = jurado frío propio, v0 global 8,0; **la bolsa/efectos personales de Jean SÍ aparecen en vF (N3) bajo protocolo de A7**). Diagnóstico y criterios de aceptación: `informes/d1-diagnostico.md` §10. Checkpoint exacto en `informes/estado-proceso.md`. Actualiza esta línea al cerrar cada fase/oleada.
- Última versión aceptada: v0 (tag). Recuento canónico v0: 62.750 palabras.
