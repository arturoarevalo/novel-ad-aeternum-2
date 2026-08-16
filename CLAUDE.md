# CLAUDE.md — convenciones del proyecto

Repositorio para escribir **una novela larga** (español de España) asistida por Claude Code. Esto son las reglas que siempre se cumplen. Mantenlo corto: es contexto estable (se cachea).

## Regla de oro

**El orquestador (la sesión principal y los comandos `/arquitecto`, `/capitulo`…) NO escribe prosa de la novela.** La prosa la escribe SIEMPRE el subagente **redactor**. El director diseña, delega y verifica. Escribir prosa en la sesión principal gasta contexto y la compactación borraría el diseño.

## Idioma

Toda la novela y la biblia, en **español de España** (vosotros, RAE, léxico peninsular). La raya (—) es la puntuación correcta del diálogo; úsala con normalidad.

## Registro

El registro lo manda la historia: lenguaje malsonante, sexo y violencia están permitidos cuando la escena los requiere, especialmente en diálogo (ver `biblia/estilo.md` §14; el nivel de crudeza de cada novela se declara en `biblia/premisa.md`). No desinfectar. Único límite innegociable: nada que sexualice a menores.

## Estructura

- `biblia/` — diseño (la fuente de verdad). `estilo.md` es la ley de la prosa y no se reescribe a la ligera.
- `memoria/` — estado acumulado: `hechos.md`, `nombres.md`, `preguntas-abiertas.md`, `motivos.md`, `ideas.md`, `rasgos.md` (tics/rasgos/sensaciones por personaje, para anti-repetición).
- `estado/despues-cap-NN.md` — instantánea del mundo tras cada capítulo (la escribe el archivista).
- `capitulos/cap-NN.md` — la prosa. `briefs/cap-NN.md` — el encargo. `notas/cap-NN.md` — feedback del autor.
- `scripts/` — instrumental TypeScript (CLI). `builds/` — salida concatenada.

## Convención de nombres (estricta, la usan los scripts)

`cap-NN.md` con NN de **dos dígitos** (cap-01, cap-02…). Igual para `briefs/cap-NN.md`, `estado/despues-cap-NN.md`, `notas/cap-NN.md`. La lista oficial de capítulos vive en `biblia/metadatos.json`.

## Front-matter de capítulo

```
---
capitulo: N
titulo: <título>
pov: <personaje>
fecha: <ISO: 1992-04-05 o 1992-04-05T21:30>
estado: terminado   # o borrador / pendiente
analepsis: false    # true si retrocede en el tiempo
---
```

## Comandos (instrumental, 0 tokens de modelo)

- `npm run lint -- capitulos/cap-NN.md` — linter de prosa (AI-ismos, cadencia, español).
- `npm run coherencia -- status` — documentos obsoletos. `impact <ruta>` — qué depende de algo.
- `npm run cronologia` — valida fechas. `npm run similitud` — reincidencias entre capítulos.
- `npm run repeticiones` — tics/rasgos/sensaciones que un personaje repite (determinista, 0 tokens).
- `npm run hilos` — presagios vencidos, tensión viva (preguntas mayores), longitud y presupuesto de palabras.
- `npm run tipografia -- --fix` — ortotipografía española (raya de diálogo, «», …, ¿¡, espacios); corrige sola lo inequívoco.
- `npm run originalidad` — extrae candidatos antiplagio (versos, citas, aperturas, n-gramas raros) para la skill /originalidad.
- `npm run salud` — Definition of Done de la novela (puerta de calidad).
- `npm run build` — concatena en `builds/<slug>.md`. `npm run deploy` — previsualización (stub).
- `npm run escribir-resto` — runner autónomo de capítulos pendientes.

## Caché (tokens)

El material estable (estilo, esta guía, biblia que no cambia) va al **principio** de cada prompt de subagente; lo volátil (el brief) al **final**. Para tiradas autónomas: `CLAUDE_CACHE_TTL=1h` y capítulos seguidos.

## Flujo

`/arquitecto` (biblia) → revisar → `/capitulo 1` → revisar voz → `/escribir-resto` → `/informe` → `/ejecutar-plan` → `/pulir` (notas) → `/aplicar-notas` → `/originalidad` (antes de publicar). `/podar <objetivo>` si la novela se pasa. Detalle en RUNBOOK.md.
