# Herramientas del plan de revisión-expansión de «Ad aeternum»

Todas en Bash + Python 3 (stdlib). Se ejecutan desde la raíz del repositorio. La librería común es `lib/aa.py`
(frontmatter, recuento canónico de palabras, manifiesto, orden de lectura, escenas).

| Herramienta | Qué hace | Cuándo |
|---|---|---|
| `actualizar-metadatos.sh` | ÚNICA vía de escritura de campos operativos de `biblia/metadatos.json`: `palabras-real`, `objetivo N --gate-autor`, `presupuestos [--v0]`, `registrar cap-nX.md --gate "G-A2 …"`, `paratexto`, `renumerar --w7 --gate-autor`, `verificar`, `mostrar`. Aborta si el resultado altera un campo de autor sin gate. | F0; cierre de cada oleada; W7 |
| `inyectar-frontmatter.sh` | Añade/actualiza los campos del plan (§2.4) en el frontmatter desde `ordenes/tabla-5-1.json`; `--set cap-NN.md estado=en_oleada` para el ciclo de vida. Nunca toca campos del autor ni el cuerpo. | F0; inicio/cierre de oleada |
| `proteger.sh` | M9: `baseline` (aditivo; `--rebaseline --gate` para excepciones), `verificar [--staged]`, `listar`. Lee `protegidos/spans.json`, escribe `protegidos/hashes.json`. | pre-commit; cada gate |
| `validar-frontmatter.sh` | Campos autor/plan, `estado`, contrato `persona: primera`, notas de trabajo en el cuerpo. | pre-commit; tras cada escritura |
| `auditar-manifiesto.sh` | B0: manifiesto vs ficheros vs prosa (títulos, slugs, partes, cuenta atrás, persona, deriva de palabras). Solo lectura. | F0; mantenimiento |
| `compilar.sh <etiqueta>` | Compila `compilado/ad-aeternum-<etiqueta>.md` (cabeceras de parte desde `partes[]`, numeración por orden de lectura, sin frontmatter/dedicatoria/sinopsis, con aviso y recursos) y reporta M8. Insumo ÚNICO de A6/A6b. | cada hito de puntuación |
| `medir.sh <etiqueta> [--baseline v0]` | M1–M10 → `informes/metricas-<etiqueta>.json` + `informes/dashboard-<etiqueta>.md`. | cada oleada/hito |
| `lib/m6_muestra.py generar/puntuar` | M6b: muestra ciega de réplicas para atribución por modelo + puntuación. | F1 y hitos |
| `lib/huella.py <etiqueta>` | Parte cuantitativa de B6 (huella estilística). | F0; W6 |
| `hooks/pre-commit` | M9 + manifiesto + validador. Instalar con `git config core.hooksPath herramientas/hooks`. | siempre |
| `hooks/pretooluse-protegidos.sh` | Hook PreToolUse de Claude Code (`.claude/settings.json`): bloquea Write/Edit sobre `proteccion: total`, manifiesto y hashes; heurística para Bash. Excepción de gate: prefijo `AA_GATE_AUTOR="motivo"`. | siempre |

Recuento canónico de palabras: cuerpo sin frontmatter, sin marcado markdown ni dinkus, tokens con al menos un carácter alfanumérico.
