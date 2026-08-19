# Proyecto: revisión-expansión de la novela «Ad aeternum»

## Contrato de operación

- **EN W10: el contrato es `plan-w10.md` y A0 LO LEE ÍNTEGRO AL ARRANCAR, junto con `informes/w10/estado.json` (la memoria de la fase: hipótesis ya probadas y callejones sin salida) y `biblia/b7-perimetro.md` (lo único vinculante que queda). El plan maestro histórico queda como referencia, no como contrato.**
- Plan maestro (histórico): `plan-revision-ad-aeternum.md`. **A0 lo lee ÍNTEGRO al arrancar cada sesión** (con la herramienta Read). NO se importa con `@`: todo lo que hay en CLAUDE.md llega al contexto de TODOS los subagentes, y los lectores en frío (A6, A6b, lector-frio) no deben ver jamás el plan.
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

- **Fase actual: W10, autónoma, autorizada por el autor el 2026-08-19. Contrato: `plan-w10.md` — A0 LO LEE ÍNTEGRO AL ARRANCAR, junto con `informes/w10/estado.json`.** Objetivo: 9,0 en los diez ejes y en la nota global. Se ejecuta **sin intervención humana**, iterando cuantas veces haga falta, y entrega `informes/w10/informe-final.md`.
- **En W10 CAE la restricción estructural**: se pueden fundir, partir, mover, cortar y escribir capítulos, abrir los diez ficheros que eran `proteccion: total` y reescribir prosa del autor. Los hashes pasan de cerradura a **registro** (`proteger.sh baseline --rebaseline --gate "W10: …"` tras cada cambio consciente). Se pueden modificar herramientas y agentes.
- **Lo único que NO cae: `biblia/b7-perimetro.md` y el veto de A7, que sigue siendo absoluto.** No es restricción de oficio: el libro le promete al lector en su primera página que el acto no se describe en ninguna página, y ese aviso está congelado por hash. «Despedida» no se abre; Kongsbakken no se escribe; la bolsa no reaparece.
- **El dato que gobierna la fase.** En 48 lecturas frías de todas las versiones, v0 incluida: **estructura (máx. 8,5), trama (8,5), ritmo (8,0) y la nota global (8,5) NO han llegado a 9 ni una sola vez.** Los otros seis ejes sí. Los cuatro que faltan son los estructurales, y la estructura es lo que esta fase desbloquea por primera vez. Un «no se puede» documentado vale más que un 8,5 sin explicar.
- **Bucle:** `herramientas/w10-campana.sh <etq>` (compila · sondas · tres críticos + **control de deriva sobre v0 el mismo día** · medianas · guardia de regresión de ±0,5 · estado) → diagnóstico con **`a2-arquitecto`** (agente nuevo, sin restricción estructural) → intervención → verificación (A5, **A7 si toca su perímetro**) → remedición. Si el eje objetivo no sube fuera del ruido, **se revierte** y se anota el callejón. `herramientas/lib/w10_estado.py` es la memoria entre sesiones.
- **Se para** con los once ejes en 9,0; o con **tres iteraciones seguidas sin mejora fuera del ruido**; o ante una **regresión en `duelo` o `tema`**; o ante un veto de A7 sin arreglo mínimo.
- **Estado del libro al entrar en W10: 48 capítulos, 79.794 palabras, en banda (80.000 ± 1.000).** Ficheros y órdenes renumerados a `cap-01`…`cap-48` y `OT-01`…`OT-48`, coherentes con el manifiesto; tabla de equivalencia en `biblia/b0-mapa-renumeracion.md` (los siete capítulos nuevos del plan son hoy el **8, 11, 17, 20, 27, 31 y 47**). M7 0 · M9 10 ficheros y 129 spans · M10 100 % · frontmatter 0 avisos · cuotas = recuento real.
- **Resultados que W10 hereda y no debe repetir.** Global 8,5 y ritmo 7,5 en vF, igual que v0: **la rúbrica no distingue vF de v0**, y está medido que el mismo juez varía hasta un punto entero sobre texto idéntico. Lo que sí se movió: **la A/B ciega da 5 de 5 a vF**, el punto de abandono pasó del 40 % al 62 % del libro, y el lector beta que abandonaba en el capítulo 15 llega ahora al final. **Los tres puntos de abandono de vF son capítulos nuestros** (hoy el 27 y el 31). Y la prosa de los siete capítulos nuevos **no se distingue**: prueba ciega con 1,75 aciertos de 7 contra un azar de 3,5.
- **Once instrumentos del proyecto resultaron medir algo distinto de lo que decía su nombre, y los once fallaban a la baja y en silencio.** Suponer que los que quedan están bien sería el duodécimo. Detalle en los gates de W4-R a W9.
- Última versión aceptada: **vF** (`compilado/ad-aeternum-vF.md`). Baseline congelada: v0 (tag), 62.750 palabras, 41 capítulos.
