# RUNBOOK — cómo escribir una novela con esta plantilla

Manual de operación, paso a paso. Para el porqué de cada pieza, mira `CLAUDE.md` y `biblia/estilo.md`.

---

## 0. Preparar el repositorio

1. Crea un repo nuevo **desde esta plantilla** (un repo por novela).
2. Ábrelo en el dev container (`.devcontainer`) o en tu máquina con Node ≥ 20 y Claude Code instalado.
    - Instalación de Claude Code (si no usas el container): `npm install -g @anthropic-ai/claude-code`.
    - Dependencias del instrumental: `npm install`.
3. Comprueba que el instrumental va: `npm run salud` (al principio dirá que faltan capítulos; es normal).
4. Inicializa git si no lo está: `git init && git add -A && git commit -m "Plantilla inicial"`.

---

## 1. Material de partida

Deja en `input/` lo que tengas (ver `input/README.md`): una idea, un manuscrito entero, revisiones de un editor, referencias… en cualquier mezcla. Marca lo que no se deba tocar con `<<INTOCABLE>> … <<FIN>>`.

No hace falta que sea mucho: con una buena premisa basta. El sistema **no** pone el alma ni el giro genial: eso lo pones tú. El sistema te ahorra el andamiaje y evita que la prosa cante a IA.

---

## 2. Lanzar Claude Code

Para una sesión normal:

```bash
claude
```

Para tiradas autónomas largas (sin ir confirmando permisos), con el modelo más potente:

```bash
claude --dangerously-skip-permissions --model opus
```

- **`--dangerously-skip-permissions`** deja que Claude ejecute las herramientas sin pedirte permiso en cada paso. Úsalo cuando ya confíes en el flujo (p. ej. para escribir varios capítulos seguidos). En un repo dedicado y bajo control de versiones, el riesgo es asumible.
- **Modelo**: `opus` para la sesión principal y para redactor/crítico/editor (donde está la calidad). El archivista y el investigador usan Sonnet automáticamente (enrutado por subagente).
- **Pensar más en los momentos clave**: al diseñar la biblia o un brief difícil, pídele explícitamente que **piense a fondo** (por ejemplo escribiendo `ultrathink` en tu instrucción). No lo dejes puesto para todo: pensar gasta tokens.
- No existe ningún "modo ultracode". Las palancas reales son estas tres: saltarse permisos, usar Opus, y pedir más pensamiento donde toca.

---

## 3. Construir la biblia → `/arquitecto`

En la sesión de Claude:

```
/arquitecto
```

Leerá `input/`, diseñará la novela y rellenará `biblia/` y `biblia/metadatos.json` (con la lista de capítulos). Marcará sus decisiones dudosas con `<<DECISIÓN: … >>`.

**Revisa la biblia antes de seguir.** Es el paso más rentable: corregir aquí cuesta minutos; corregir en la prosa cuesta capítulos. Mira sobre todo:

- `premisa.md` (¿engancha de verdad?), `estructura.md` (mapa de intensidad sin mesetas), `outline.md` (cada escena gira; ganchos y anzuelos), `plan-revelacion.md` (la matriz cuadra).
- Resuelve las `<<DECISIÓN>>` y marca pasajes intocables si reutilizas manuscrito.
- Edita a mano lo que quieras; vuelve a pasar `npm run coherencia -- scan` si tocas mucho.

---

## 4. Escribir el capítulo 1 → `/capitulo 1`

```
/capitulo 1
```

Ejecuta el pipeline completo (brief → redactor → lint → crítico → editor → archivista → build). Cuando termine:

- Lee el capítulo (`capitulos/cap-01.md`) con calma. **Este capítulo fija la voz** de toda la novela.
- Si la voz no es la que quieres, ajústala donde más manda: pega 1-2 pasajes de muestra en `estilo/ejemplos.md`, afina reglas en `biblia/estilo.md`, y vuelve a generar o usa `/pulir 1` y aplica sus notas con `/aplicar-notas 1`.
- Repite hasta que el capítulo 1 te guste. Cuanto mejor esté, mejor saldrá el resto (sirve de patrón).

Para ver solo el encargo sin redactar: `/capitulo 1 --solo-brief`.

---

## 5. Escribir el resto → `/escribir-resto`

Con la biblia revisada y el capítulo 1 a tu gusto:

```
/escribir-resto
```

Escribe todos los capítulos pendientes, uno a uno, **con contexto fresco**, pasando la puerta de calidad (`npm run salud`) entre capítulos. Si uno no pasa, **se detiene** para que lo revises; al relanzar, **continúa donde se quedó** (checkpoint en `.runner-state.json`).

Consejos para la tirada:

```bash
# Vista previa de lo que haría, sin escribir:
npm run escribir-resto -- --dry-run
# Tirada completa reaprovechando caché (capítulos seguidos):
CLAUDE_CACHE_TTL=1h npm run escribir-resto
# Un tramo:
npm run escribir-resto -- --desde 5 --hasta 12
```

---

## 6. Revisar e incorporar feedback

- **Informe editorial**: `/informe` con el borrador completo. Genera `informe/informe-editorial.md` (review de comité) y `informe/plan-de-accion.md`. Marca `[x]` lo que apruebes y lanza `/ejecutar-plan`. Macro antes que micro: informe y plan primero, `/pulir` después.
- **Podar**: `/podar 95000` cuando la novela se pasa del objetivo. Plan de poda en dos niveles (estructural + línea) con checkboxes, y ejecución con el editor en modo poda.
- **Pulir**: `/pulir` (toda la novela) o `/pulir 7` (un capítulo). Genera notas en `notas/cap-NN.md` sin tocar la prosa; revísalas y aplícalas con `/aplicar-notas`.
- **Tus notas**: escribe en `notas/cap-07.md` con `<<NOTA: … >>` y ejecuta `/aplicar-notas 7`. Los cambios locales se aplican; los **estructurales** (que tocan la biblia) se te proponen con su impacto antes de tocar nada (cascada dirigida, no ciega).
- **Renombrar algo en todo el libro**: es un cambio mecánico; se hace por búsqueda/reemplazo determinista.

---

## 7. Comprobaciones y entrega

En cualquier momento:

```bash
npm run lint -- --todos      # AI-ismos y estilo en todos los capítulos
npm run coherencia -- status # documentos obsoletos
npm run cronologia           # fechas coherentes
npm run similitud            # frases/aperturas repetidas entre capítulos
npm run repeticiones         # tics/rasgos/sensaciones que un personaje repite
npm run hilos                # presagios, tensión, longitud y presupuesto de palabras
npm run tipografia -- --fix  # ortotipografía de imprenta (corrige sola lo inequívoco)
npm run originalidad         # candidatos antiplagio → informe/ (verificar con /originalidad)
npm run salud                # todo junto (Definition of Done)
npm run build                # genera builds/<slug>.md
npm run deploy               # previsualización HTML (stub: sustituir por subida real)
```

`builds/<slug>.md` es el manuscrito completo. `deploy` es un esqueleto para que enchufes tu publicación real (web, EPUB, lo que uses).

---

## 8. Resolución de problemas

- **"No existe biblia/metadatos.json"**: ejecuta `/arquitecto` primero.
- **`salud` FALLA**: mira qué bloque está en rojo. Errores de prosa → `/pulir N` y `/aplicar-notas N`. Cronología → revisa `fecha:` en el front-matter (o marca `analepsis: true`).
- **Coherencia avisa de obsoletos**: cambiaste la biblia y hay capítulos que dependían de eso. Usa `npm run coherencia -- impact biblia/<fichero>.md` para ver qué regenerar, y decide.
- **El linter molesta con algo que es tu estilo**: ajusta umbrales y listas en `lint-prosa.config.json`, o añade tus recursos propios a `estilo/base-autor.md`.
- **Se cortó una tirada larga**: vuelve a lanzar `/escribir-resto`; continúa por donde iba.

---

## Resumen de un vistazo

```
input/  →  /arquitecto  →  (revisar biblia)  →  /capitulo 1  →  (afinar voz)  →  /escribir-resto  →  /informe  →  /ejecutar-plan  →  /pulir  →  /aplicar-notas  →  /originalidad  →  build
```
