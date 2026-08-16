# informe/

Salidas del ciclo editorial de novela completa (fuera del grafo de coherencia: nada de aquí vuelve obsoleto un capítulo).

- `informe-editorial.md` — review profesional (21 secciones, puntuaciones 1-10, escenarios de ventas). Lo genera `/informe`.
- `plan-de-accion.md` — acciones concretas con checkboxes. Marca `[x]` lo que apruebes y lanza `/ejecutar-plan`. Lo no marcado se ignora (queda para otra ronda).
- `empaquetado.md` — título, tagline, sinopsis, comparables (acciones D).

Flujo: borrador completo → `/informe` → marcar `[x]` → `/ejecutar-plan` → `/pulir` → `/aplicar-notas` → `npm run build`.
