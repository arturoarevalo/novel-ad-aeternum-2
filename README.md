# Plantilla de novela (Claude Code)

Plantilla de repositorio para escribir **novelas largas en español de España** con Claude Code: agentes, skills, hooks e instrumental en TypeScript. De una idea (o un manuscrito, o revisiones) construye una **biblia** revisable y luego escribe los capítulos, cuidando que la prosa **no parezca de IA** y que la tensión no decaiga.

Un repo por novela: clónala como plantilla y empieza.

## Idea en 30 segundos
- **El director no escribe prosa.** La sesión principal diseña y delega; el subagente **redactor** escribe. Así el diseño no se pierde al compactar el contexto.
- **Biblia como fuente de verdad** (`biblia/`), con un **firmware de prosa** (`biblia/estilo.md`) que veta los tics de IA (la antítesis "No era X. Era Y.", cierres con moraleja, personificación de lo abstracto, micro-gestos, filter words…).
- **Memoria y estado** (`memoria/`, `estado/`) para coherencia a lo largo de cientos de páginas sin releerlo todo (coste lineal, no cuadrático).
- **Instrumental determinista** (`scripts/`, 0 tokens): linter de prosa nativo en español, grafo de coherencia, cronología, auto-similitud, build y una puerta de calidad (`salud`).
- **Tokens bajo control**: prefijo estable cacheado, enrutado de modelo por subagente (Opus donde importa, Sonnet para lo mecánico), bucle de revisión acotado.

## Empezar
1. `npm install`
2. Pon tu material en `input/`
3. En Claude Code: `/arquitecto` → revisa la biblia → `/capitulo 1` → `/escribir-resto`

El manual completo está en **`RUNBOOK.md`**. Las convenciones, en **`CLAUDE.md`**.

## Comandos
`npm run lint · coherencia · cronologia · similitud · salud · build · deploy · escribir-resto`

> Nota honesta: esto te quita el andamiaje y la prosa de relleno, pero el alma, el giro inesperado y el criterio son tuyos. Autor en el bucle.
