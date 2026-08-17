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

---

## 5. Motor `codex` (OpenAI · `gpt-5.6-sol`): aislamiento, protocolo y salvedades

**A0 · 2026-08-17.** El autor dispone de `codex` (codex-cli 0.147.0) con su suscripción. Motivo del cambio, en una línea: tras G-A1 escriben `claude-opus-5` y juzgan `claude-opus-5` ×2 + `claude-opus-4-8`, es decir, **la diversidad de conjunto que justifica A6-3 en §2.5 era nominal** (misma familia, mismos priors estéticos que el generador). Un juez de otra familia la vuelve real. `herramientas/lib/motor_codex.py` añade el motor; `critica-fria.sh --motor codex` (o `motor: codex` en el frontmatter del agente) lo selecciona.

### 5.1 Qué NO se puede replicar del motor `claude`

- **Las herramientas de codex no se pueden desactivar.** No hay equivalente a `--tools ""`: el agente declara siempre `exec`, `wait`, `request_user_input` y las de multiagente (`spawn_agent`…). Se apagan las apagables (`tools.web_search=false`, `tools.update_plan={enabled=false}`), no el shell.
- **El system prompt propio no se elimina.** `model_instructions_file` coloca la rúbrica del rol como instrucciones de modelo (verificado con una persona-señuelo: el modelo la adopta y la cita); el preámbulo restante que declara es genérico («You are an AI assistant accessed via an API»), no la persona de agente de programación. Entrada base ≈ 9,6–9,7k tokens (definiciones de herramientas).
- **No hay coste por token** (suscripción ChatGPT) ni desglose entrada/salida: la cabecera de trazabilidad registra el total declarado por codex.
- **`--json` no declara modelo ni esfuerzo**, así que el motor usa la salida humana, que sí imprime `model:`, `reasoning effort:` y `session id:`. La aserción de modelo (equivalente a `modelo_coincide`) se mantiene: si codex no declara el modelo, **no se escribe el informe**.

### 5.2 Cómo se consigue el aislamiento

Ejecución en directorio **fuera del repositorio**, con `--ignore-user-config` (nada de `~/.codex/config.toml`), `--ignore-rules`, `--ephemeral` (la sesión NO se persiste: el manuscrito no queda en el historial de codex, donde memorias, skills o plugins podrían alcanzarlo), `project_doc_max_bytes=0` (sin AGENTS.md), `include_environment_context=false`, `tools.web_search=false`, sandbox `read-only` y entorno de la sesión padre limpiado.

Y una garantía que **no es de configuración sino del entorno**: en este contenedor el sandbox de codex no puede crear namespaces (`bwrap: No permissions to create new namespace`), de modo que **toda ejecución del shell falla en seco**. Un lector frío en codex es, de hecho, un lector sin herramientas.

### 5.3 Sonda `critica-fria.sh --sonda --motor codex` (falla cerrada)

Tres comprobaciones, y el motor **se niega a arrancar** si la primera no se cumple:

1. **Jaula local:** se ejecuta `bwrap --ro-bind / / --unshare-all true` directamente. Si funciona, el shell de codex está vivo y la lectura fría queda prohibida (`critica_fria` aborta con instrucciones). Determinista y gratuito.
2. **Contexto:** el modelo audita su propio contexto. Resultado 2026-08-17: «(a) Instrucciones de proyecto: NINGUNA. Memoria de usuario: NINGUNA. Contexto de repositorio: NINGUNA. (b) No, ninguna [de «Ad aeternum», «Koppangen», «Maja», «Soldagen»] aparecía antes de este mensaje.» Entrada 9.719 tokens.
3. **Fuga real:** se le ordena leer `/workspaces/novel-ad-aeternum-2` y `CLAUDE.md`. Respuesta literal: `bwrap: No permissions to create new namespace…` en ambos comandos. Además se filtra la respuesta contra marcadores del repositorio (`plan-revision`, `Contrato de operación`, `proteccion: total`…): si aparece alguno, veredicto SOSPECHOSO.

**VEREDICTO 2026-08-17: LIMPIO.** Si algún día el host habilita user namespaces, (1) y (3) lo detectan y el motor deja de arrancar: por eso la sonda es obligatoria antes de cada campaña de scoring, no solo una vez.

### 5.4 Salvedades vigentes (van al informe final)

- **Ventana de contexto 272k.** v0 son 113k tokens para el tokenizador de OpenAI; vF (~85k palabras) rondará los 150k: cabe. Lo que **no cabe** es la A/B ciega de §7.3 con los dos manuscritos completos (~265k + razonamiento): esa prueba se queda en jueces Claude, o se hace por partes. Documentado aquí para que no se descubra en W8.
- **El manuscrito inédito sale hacia un segundo proveedor** (OpenAI, bajo la suscripción del autor). Decisión de autor, tomada el 2026-08-17.
- **Sesgo residual desconocido:** un modelo entrenado por otro laboratorio puntúa con otra escala. Por eso el cambio de jurado exige re-baseline de v0 (§5.5) y por eso el juez nuevo entra en la **mediana**, donde un solo juez no puede mover el resultado por sí mismo.

### 5.5 Prueba de aptitud y re-baseline (v0)

`herramientas/critica-fria.sh a6-critico-3 compilado/ad-aeternum-v0.md --motor codex --modelo gpt-5.6-sol --esfuerzo max` → `informes/a6-v0-critico-sol-frio.md` (113.311 tokens, 142 s, sin coste por token). La crítica es literaria, no técnica: cumple la rúbrica, responde a las seis preguntas obligatorias y cita capítulo y frase en cada eje. **Apta.**

Notas: premisa 9,5 · estructura 8,5 · prosa 9 · diálogo 8,5 · personajes 9 · mundo 9 · **ritmo 7,5** · trama 8,5 · duelo 9,5 · tema 9 · **global 8,5**. Coincidencias independientes con el jurado Claude: ritmo como suelo (7,5, idéntico), el registro «ensayístico» compartido por Astrid/Maja/Jean/Jessie, los secundarios instrumentales (Gunnar, Tomas, Henrik), la segunda secuencia de Jessie en el 24 como escena que sobra, y —hallazgo convergente— **falta una escena doméstica de duelo sin interfaces** (el jurado Claude pidió «Maja frente al locutorio»; sol pide «la mañana posterior a la cuarta nota»). Divergencia principal: sol considera que el clímax **se gana** y es +0,5/+1 más generoso en premisa, prosa y personajes.

**Efecto sobre la baseline: ninguno.** Con A6-3 = `gpt-5.6-sol`, la mediana por eje de v0 es idéntica en los once ejes a la del jurado anterior (ver `informes/a6-v0-baseline-opus5.md` §4). El cambio de jurado es, por tanto, gratuito en continuidad de anti-regresión.

### 5.6 M6b con juez ajeno (control de la métrica de voces)

`m6-atribuidor` sobre `informes/m6-muestra-v0.md`, mismo reparto neutro que la variante 1: **41,1 % de acierto** (`informes/m6b/m6b-v0-variante-4-sol.md`) frente al 39,3 % de `claude-opus-4-8`. Dos familias de modelos miden lo mismo: el 39–41 % de v0 **es una propiedad del texto**, no del lector, y el objetivo T4 de ≥80 % sigue tan lejos como decía el diagnóstico. Coincide incluso el patrón: EDDA se identifica casi siempre (86–100 %) y Maja/Nora/Jessie se confunden entre sí.

### 5.7 Roles que NO usan codex (regla)

Prosa (A3a/A3b), edición de línea (A4), sensibilidad (A7, con veto), estructura (A2), orquestación y gates (A0), y la A/B ciega de vF. Motivo: la prosa es el producto y B6 mide huella estilística; el veto de A7 no se delega en un modelo con otra política de contenido; y la A/B ciega no cabe en 272k. Codex se usa donde **juzga o refuta**, nunca donde escribe.
