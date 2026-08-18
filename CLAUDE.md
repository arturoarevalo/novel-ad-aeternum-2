# Proyecto: revisión-expansión de la novela «Ad aeternum»

## Contrato de operación

- Plan maestro: `plan-revision-ad-aeternum.md`. **A0 lo lee ÍNTEGRO al arrancar cada sesión** (con la herramienta Read). NO se importa con `@`: todo lo que hay en CLAUDE.md llega al contexto de TODOS los subagentes, y los lectores en frío (A6, A6b, lector-frio) no deben ver jamás el plan.
- Crítica de referencia (baseline de puntuaciones): `critica-ad-aeternum.md`. Solo la lee A0 (al arrancar); jamás se pasa ni se importa para A6/A6b/lector-frio.
- Tú eres A0 (orquestador). Los demás roles son subagentes según §2.1 y §2.5 del plan.
- **Aislamiento de los lectores en frío (regla dura):** A6, A6b, `lector-frio` y `m6-atribuidor` se lanzan ÚNICAMENTE con `herramientas/critica-fria.sh` (`claude -p` —o `codex exec` con `--motor codex`— desde fuera del repositorio, system prompt = rúbrica del agente, modelo fijado por ID, sin herramientas, insumo único inline: compilado/extracto), NUNCA como subagentes de la sesión: todo subagente hereda CLAUDE.md, la memoria y el email (verificado con sonda haiku el 2026-08-16; los `@`-imports además contaminaban con el plan y la crítica: `informes/a6-v0-critico-{1,2,3}.md`, conservados como evidencia). Protocolo y evidencia: `informes/d1-aislamiento.md`. Ningún prompt ni fichero accesible a un lector frío puede contener el plan, la crítica de referencia, los changelogs ni los informes de gate.

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
- `herramientas/critica-fria.sh <rol> <insumo> --salida <informe.md>` — lectura en frío real (A6/A6b/lector-frio/m6-atribuidor) desde fuera del repo; `--sonda` verifica el aislamiento; env `AA_FRIO_DIR` = directorio de ejecución (scratchpad). Motor: `claude` por defecto; **`--motor codex`** (o `motor: codex` en el frontmatter del agente) ejecuta el rol con `codex exec`/`gpt-5.6-sol` bajo la suscripción del autor — lo usa A6-3. Antes de cada campaña de scoring: `critica-fria.sh --sonda --motor codex` (falla cerrada; protocolo y salvedades en `informes/d1-aislamiento.md` §5).
- `herramientas/auditor-adverso.sh <cap-NN.md> [--orden OT] [--base v0]` — auditoría adversarial de inserciones (¿paga cada una su etiqueta de función?, riesgo «hinchazón» §8) con `gpt-5.6-sol` max vía codex; escribe `informes/auditoria-adversa-<cap>.md`. NO es un gate: A0 decide qué se borra.
- `herramientas/validar-frontmatter.sh`, `herramientas/auditar-manifiesto.sh`, `herramientas/inyectar-frontmatter.sh` (campos del plan; `--set cap-NN.md estado=en_oleada`), `herramientas/sensibilidad.sh` (pre-chequeo T7: hits nuevos vs baseline de A7), `herramientas/lib/m6_muestra.py` (M6b), `herramientas/lib/m4b_antepuestas.py` (M4b subordinadas antepuestas), `herramientas/lib/huella.py` (B6 datos).
- Hooks: PreToolUse en `.claude/settings.json`; pre-commit vía `git config core.hooksPath herramientas/hooks` (repetir en clones nuevos). Excepción de gate de autor en Bash: prefijo `AA_GATE_AUTOR="motivo"`.
- Los subagentes de `.claude/agents/` (18, con `model`/`effort` de §2.5; `m6-atribuidor` añadido en F1) se indexan al arrancar la sesión: tras crearlos o editarlos hay que reiniciar la sesión para lanzarlos por nombre.
- Documento vivo de estado: `informes/estado-proceso.md`. Gates: `informes/g0-gate.md`, …

## Modelos y esfuerzo

**Decisión de autor (G-A1, 2026-08-17; supersede la tabla §2.5 del plan): ningún agente usa `claude-fable-5`.** Todos los subagentes llevan modelo FIJADO por ID en `.claude/agents/`: A2, A3a, A3b, A7 y A6-1/A6-2 en `claude-opus-5` (esfuerzo max); A1-F0 y A4 en `claude-opus-5` (high); A6-3 en **`gpt-5.6-sol` (OpenAI, esfuerzo max, `motor: codex`)** — decisión de autor 2026-08-17: juez de OTRA familia de modelos, porque con todo el jurado en Anthropic la diversidad de conjunto de §2.5 era nominal; A5, A6b ×4, `lector-frio`, `m6-atribuidor` y A1-mantenimiento en `claude-opus-4-8` (medium); A8 en `claude-haiku-4-5` (low). La sesión principal (A0) la elige el autor al arrancar (recomendado `claude-opus-5` a esfuerzo max). Los lectores en frío se ejecutan siempre con `herramientas/critica-fria.sh` (modelo y motor leídos del frontmatter del agente). **Codex no escribe prosa ni juzga sensibilidad**: A3a/A3b, A4, A7, A2, A0 y la A/B ciega final siguen en Claude (la A/B con dos manuscritos no cabe en los 272k de sol). Baseline de anti-regresión con el jurado vigente: ver «Estado».

## Estado

- Fase actual: **W4-R (campaña de ritmo) EN EJECUCIÓN, rama `w4r-ritmo`, sin fusionar.** Oleada creada por A0 bajo autonomía delegada del autor (2026-08-18); la primera que RESTA texto. Hechos y verificados: N3/N2 −1.007 y bloque de cierre 34–41 −728 netos; **A7 APROBÓ W4-R sin veto y sin condiciones pendientes**; A5 pasa con menores; M9 109 spans. **HISTÓRICO: W2 y W3 aprobadas y fusionadas; W4 fusionada (`1686b1c`); G-A1 y G-A2 APROBADOS por el autor.**
- **La medición que gobierna lo que queda.** Tres críticos fríos sobre el compilado podado + control de deriva sobre v0: **Ritmo mediana 7,5 (quinta consecutiva), Personajes 8,5 sin caída, global 8,5, ningún eje cae.** Criterio del autor «Ritmo ≥ 8,0 y Personajes sin caída»: Personajes CUMPLE, Ritmo NO. **v0 también da 7,5 hoy**: la poda del cierre estaba bien hecha y aplicada al tercio equivocado. Los cuatro lectores coinciden por primera vez y **ninguno nombra el cierre**: abandonan en `cap-n4`, `cap-13` (×2) y `cap-30`. El eje es **reiteración, no densidad**.
- **El diagnóstico del centro (A2, `informes/w4r-diagnostico-centro.md`)**: la Parte III era la más corta del libro (14.089) y hoy es la más larga (22.063), **+57 %**, y el 86 % de ese crecimiento son N3, la coda R2 del 25 y N4 — 7.974 palabras nuestras. **De trece nominaciones de punto de abandono en cinco hitos, doce caen en Partes II–III y ninguna en el cierre.** CH-27 se pagó dos veces: `b4-ledger.json` lo asigna a «N2 y N4», única entrada de 83 con dos capítulos nuevos.
- **Instrumentos retirados (`informes/w4r-instrumentos-ritmo.md`).** El **% de diálogo de M5 no mide el ritmo de este libro** (el interlocutor de Jean contesta en tres palabras): medido como mancha máxima entre respiros visuales, la mediana es 146 palabras y no hay defecto micro. M5 se conserva como contrato del plan pero **A0 no dirige trabajo con él**. La repetición léxica **sobredispara** donde el ritual ES el contenido. **No se añade textura para mover un número de M5**; en capítulos por debajo del 15 % de diálogo, la textura va en réplica o no va.
- **Enmienda a G-3, vinculante para W5/W6 (de P-37 de A7):** **vaciar el párrafo vecino de una línea protegida cuenta como modificarla** — el paragrafado es énfasis y el hash NO lo detecta. No afecta a las líneas autorizadas aisladas de origen. Descubierta en `n3:321`, donde una poda que no tocó un carácter cambió el sentido de la frase.
- En ejecución: A4 poda el centro (−479; **n2, n3 y 13 a cero**), hoja ya aprobada por A7; A3a escribe **R5 en cap-13** (+80…+120). Después **G-1** (reasignar la función de la escena 1 de n4, ±0 palabras), **G-4** (vía B, después de G-1) y **W5**, que va DETRÁS de la poda. Decisiones en `informes/w4r-decisiones-centro.md`.
- Ledger: manuscrito **79.844**, por debajo del suelo (banda 80.000–82.000, relajada por A0 desde 85.000). W5 lo repone; techo de poda adicional ≈ 1.230.
- Última versión aceptada: v0 (tag). Recuento canónico v0: 62.750 palabras.
