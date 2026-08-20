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

- Ficheros con `proteccion: total` — **cap-01, cap-03, cap-04, cap-05, cap-10, cap-24, cap-28, cap-48, 00-aviso, 99-recursos** (numeración vigente tras W7; los números viejos que figuraban aquí —09, 20, 23, 41— llevaban desactualizados desde la renumeración, y lo detectó A7 en W10) — son INTOCABLES: diff = 0 salvo ortotipografía aprobada en gate. Verificación por hash (M9) en pre-commit; hook PreToolUse bloquea Write/Edit sobre ellos.
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

- **W10 CERRADA el 2026-08-20.** Entregable: `informes/w10/informe-final.md`. Cinco
  iteraciones, once campañas de lectura fría, sesenta y cuatro commits.
- **El objetivo original —9,0 en los once ejes— era una propiedad de la VARA y no del libro:**
  con una rúbrica corregida cuyas reglas escribió el propio jurado, **v0 intacto saca 9,5 de
  global**. El plan preveía este caso (§4b.3) y ordenaba replantear. Se replanteó al criterio
  del autor del 18 de agosto: «ningún capítulo nombrado como punto de abandono por dos o más
  lectores en el mismo hito».
- **Resultado, medido a n=7 con los mismos siete roles que midieron vF:** en vF incumplían
  `cap-31`, `cap-27` y `cap-20` —los tres nuestros— más `cap-15`; hoy incumple **solo `cap-09`
  «Milisegundos», del autor y declarado techo con aritmética**. La formulación es de A2:
  *«quitamos lo nuestro y debajo estaba lo que siempre hubo»*.
- **Estado del libro: 49 capítulos, 80.679 palabras, en banda.** Amplitud de capítulo 1,36 →
  **2,06**. M7 0 · M9 10 ficheros y 139 spans · M10 100 % · validador 0 avisos. Ficheros
  `cap-01`…`cap-48` **sin `cap-31`**, más `cap-w1` (orden 21,5) y `cap-w2` (36,5).
  **Renumeración pendiente: se hace una vez y al final.**
- **La rúbrica está MUERTA como instrumento de decisión, y demostrado:** el control de deriva
  sobre v0 —texto intacto— dio estructura 8/8/8,5/8, trama 8/8/8/8,5 y **duelo 9,5/9,5/9,5/9**
  en cuatro campañas. `duelo` es condición de parada del plan, y bajó sobre texto que nadie
  tocó. Ningún movimiento de ±0,5 es interpretable.
- **El criterio de abandonos solo tiene potencia a n=7** (P de pasar por azar: 0,94 a n=3;
  0,038 a n=7). Toda medición a n=3 queda marcada como no comparable.
- **Veinticuatro instrumentos rotos, trece de esta fase.** Ninguno lo detectó una métrica.
  Detalle en `informes/w10/informe-final.md` §4. El peor: `aa.chapter_paths()` veía 47 ficheros
  de 48, así que un capítulo nuevo era invisible para toda la cadena **mientras todas las
  herramientas informaban «OK»**.
- **Decisiones abiertas para el autor** (§6 del informe): la duplicación «El salero» ↔ «La
  mosquitera», medida y conservada; Kongsbakken, que es el techo real del libro y lo veta el
  perímetro; la renumeración; y la deuda de literales de `b7`.
- Última versión: **`compilado/ad-aeternum-w10it4.md`**. Baseline congelada: v0 (tag), 62.750
  palabras, 41 capítulos.
