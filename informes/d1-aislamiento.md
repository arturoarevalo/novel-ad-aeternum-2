# D1 · Aislamiento de los lectores en frío (A6, A6b, lector-frio): verificación, arreglo y protocolo

**A0 · 2026-08-16 · rama `w1-biblia-diagnostico`.** Cierra el hallazgo crítico de la sesión 2 (`informes/estado-proceso.md`): los tres críticos A6 lanzados como subagentes en sesión reprodujeron el plan (N1/N3/N4/N5, plan B de 31) y la crítica de referencia (frases casi literales, 9/11 notas idénticas). Los tres informes contaminados se conservan como evidencia (`informes/a6-v0-critico-{1,2,3}.md`).

## 1. Verificación empírica (sonda haiku en sesión)

Un subagente `general-purpose` con `model: haiku`, sin herramientas, respondió a una auditoría literal de su propio contexto:

- **Tiene CLAUDE.md íntegro** (primera línea «# Proyecto: revisión-expansión de la novela «Ad aeternum»» y los ocho encabezados). Ya sin los `@`-imports (commit 85aae0b) no ve el plan ni la crítica: «Koppangen», «Ritmo y legibilidad», «5,5», «Interferencias», «Turno», «pistola de Chéjov», «Nota global: 7,5»: **NO** aparecen.
- Pero **sí ve** — y esto sesga a un lector frío — la lista de ficheros `proteccion: total` (cap-01, 03, 04, 05, 09, 20, 23, 41), la existencia de «capítulos nuevos del plan (tabla 5.1)», «Máximo 1 mecánica nueva por capítulo de Jean (M2)», el cambio de persona del 38, «A6×3 v0 contaminados», la carta de sensibilidad, los nombres de todos los roles y sus modelos.
- También recibe **MEMORY.md** (memoria de usuario), el **email del usuario** y la fecha.
- Contexto de sistema estimado ≈ 3.800–4.200 palabras (herramientas diferidas, skills, CLAUDE.md, memoria, metadatos).

**Conclusión:** en sesión no existe «frío real»: cualquier subagente hereda CLAUDE.md y la memoria. Quitar los `@`-imports era necesario pero no suficiente.

## 2. Arreglo: `herramientas/critica-fria.sh` (claude -p fuera del repositorio)

`herramientas/critica-fria.sh <rol> <insumo> --salida <informe.md> [--modelo ID] [--esfuerzo E] [--mensaje "…"] [--dir DIR]` (Python en `herramientas/lib/critica_fria.py`):

- Ejecuta `claude -p` **desde un directorio fuera del repositorio** (`AA_FRIO_DIR`, en el scratchpad de la sesión), con `--system-prompt` = cuerpo del fichero del agente en `.claude/agents/<rol>.md` (la rúbrica y nada más), `--model` y `--effort` **fijados por ID** desde el frontmatter del agente (override explícito posible), `--tools ""` (sin herramientas), `--strict-mcp-config`, `--disable-slash-commands`, `--setting-sources ""`, `--no-session-persistence`, `--output-format json`; variables de entorno de la sesión padre (`CLAUDECODE`, `CLAUDE_CODE_*`, `CLAUDE_*`, `AI_AGENT`) eliminadas.
- Insumo **único e inline** en el mensaje: solo se admiten ficheros bajo `compilado/` (compilado completo o `compilado/extractos/`); `--insumo-libre` solo para muestras ciegas (M6b, `informes/m6-muestra-vX.md`); rechaza plan, crítica, biblia, informes de gate, changelogs, dashboards.
- Comprueba que el directorio de ejecución está fuera del repo y que ni él ni sus ancestros ni `$HOME` contienen `CLAUDE.md`/`.claude`; comprueba que el modelo realmente usado coincide con el pedido (si no, no escribe el informe).
- Escribe el informe con cabecera de trazabilidad (rol, fichero del agente, sha256 y palabras del insumo, modelo pedido/usado, tokens por modelo, coste, duración) y guarda el JSON crudo, el system prompt y el mensaje en el directorio de ejecución.
- `critica-fria.sh --sonda` lanza una sonda haiku desde ese directorio y verifica que el contexto de entrada es mínimo.
- Nota: `--bare` no es utilizable (exige `ANTHROPIC_API_KEY`; esta instalación usa OAuth). El harness añade una llamada auxiliar con haiku (título de sesión) que recibe el mismo prompt: coste marginal, sin efecto sobre el lector.

**Sonda de aislamiento (dos pasadas):** el contexto del lector consta del system prompt («You are a Claude agent, built on Anthropic's Claude Agent SDK.» + rúbrica) y un recordatorio con solo `# userEmail` y `# currentDate`; ninguna instrucción de proyecto, memoria, herramienta ni directorio de trabajo; entrada total 254–1.069 tokens; «Ad aeternum», «Koppangen», «Maja», «Soldagen», «proteccion», «lector frío»: **no aparecen**. VEREDICTO: LIMPIO.

Se han ajustado además los párrafos AISLAMIENTO de `.claude/agents/a6-critico-{1,2,3}.md`, `a6b-beta-*.md` y `lector-frio.md` para que admitan el insumo inline («tu ÚNICO insumo es el manuscrito que recibes íntegro en el propio mensaje… ni existe ningún «proceso» que debas tener en cuenta»). Rúbrica y formato de salida no cambian. Nuevo agente `m6-atribuidor` (M6b, opus-4-8, medium) para la atribución ciega en frío.

## 3. Regla operativa (vinculante desde F1)

- A6, A6b, lector-frio y M6b se lanzan **exclusivamente** con `critica-fria.sh` (nunca como subagentes de la sesión). CLAUDE.md lo recoge como regla dura.
- Los informes fríos llevan el sufijo `-frio` cuando sustituyen a uno contaminado; los contaminados no se borran (evidencia), pero **no valen** como baseline ni para anti-regresión.
- Modelos y esfuerzo por ID (§2.5): A6-1/2 `claude-fable-5` max, A6-3 `claude-opus-4-8` high, A6b `claude-opus-4-8` medium, lector-frio `claude-opus-4-8` medium, m6-atribuidor `claude-opus-4-8` medium (control fable high).
- Para A6/A6b el mensaje incluye una sola instrucción previa: el título de la novela («La novela se titula «Ad aeternum».»), porque el compilado no lo lleva y cualquier lector real ve la cubierta. Nada más.

## 4. Resultado de la relectura fría de v0 (baseline real de anti-regresión)

| Eje | A6-1 fable | A6-2 fable | A6-3 opus | **Mediana** | Referencia (`critica-ad-aeternum.md`) | Contaminados (mediana) |
|---|---:|---:|---:|---:|---:|---:|
| Premisa | 8 | 8 | 9 | **8** | 9 | 9 |
| Estructura | 7,5 | 7,5 | 8,5 | **7,5** | 8 | 8 |
| Prosa | 8 | 8 | 8,5 | **8** | 7,5 | 7,5 |
| Diálogo | 8 | 8 | 8,5 | **8** | 8,5 | 8,5 |
| Personajes | 8 | 7,5 | 8 | **8** | 7 | 7 |
| Mundo | 8 | 8 | 8,5 | **8** | 8,5 | 8,5 |
| Ritmo | 7 | 7 | 7 | **7** | 5,5 | 6 |
| Trama | 7,5 | 7,5 | 8 | **7,5** | 7 | 7 |
| Duelo | 9 | 8,5 | 9 | **9** | 9 | 9 |
| Tema | 8,5 | 8,5 | 9 | **8,5** | 9 | 9 |
| **Global** | 8 | 8 | 8,5 | **8** | 7,5 | 7,5 |

Coste de la relectura: A6-1 4,41 USD (211 s; 172k entrada + 16,8k salida, 13,7k de razonamiento), A6-2 4,34 USD (225 s), A6-3 2,04 USD (122 s). Informes: `informes/a6-v0-critico-{1,2,3}-frio.md`.

Lectura de A0: (a) los jueces fríos son más benévolos que la referencia en Ritmo (7 vs 5,5) y Personajes (8 vs 7) y más severos en Premisa/Tema/Mundo/Diálogo (8–8,5 vs 8,5–9); la mediana global sube de 7,5 a 8,0; (b) el **diagnóstico coincide** con la referencia y con el plan en lo esencial (ritmo como suelo, redundancia de 8/13/15/17/21, valle procedimental, Coro blando, Tomas sin arco, homogeneidad de registro); (c) los dos jueces fable son casi idénticos entre sí (mismo modelo: dos muestras, no dos jueces) y opus es +0,5 en casi todo → la mediana es la de fable; (d) ninguno reproduce el plan ni la referencia: las «tres mejoras» son propias (fundir 13/15/17/21, escribir Kongsbakken/una escena de Jean viva con sus hijas, sembrar a Tomas, podar el coche gris del 24, corregir el tic de subordinadas antepuestas). Esta tabla es la **baseline oficial de anti-regresión (§7.3)**; los objetivos absolutos de vF (global ≥ 9,0; suelo ≥ 8,5) se mantienen y se miden con este mismo jurado.
