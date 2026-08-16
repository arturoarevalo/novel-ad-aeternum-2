---
name: podar
description: Reduce una novela terminada hasta su objetivo de palabras; genera un plan de poda en dos niveles (estructural y de línea) con checkboxes, el autor marca lo que aprueba y la skill lo ejecuta con el editor en modo poda y el pipeline completo. Úsalo cuando el usuario diga "/podar 95000", "la novela se ha pasado de palabras", "recorta la novela" o similar.
---

# /podar <objetivo> — reducir sin romper

Para novelas que superan su presupuesto. **Regla de realismo**: la poda de línea rinde un 10-15 %; un recorte del 25-30 % o más solo sale de cortes estructurales (escenas espejo, subtramas, capítulos fusionados). El plan siempre refleja esa aritmética: nada de prometer −40 % adjetivando menos.

## 0. Preparación
- Objetivo: el argumento (`/podar 95000`); acepta también porcentaje (`/podar -30%`). Persiste la cifra en `biblia/metadatos.json` → `palabras_objetivo` (y, si faltan, reparte objetivos por capítulo en el campo `palabras`: los necesitará el modo poda).
- Diagnóstico determinista: `npm run hilos` (presupuesto: exceso total, capítulos más pasados), `npm run similitud` (escenas espejo candidatas) y `notas/_resumen-pulido.md` si existe (repeticiones semánticas ya cazadas).
- Checkpoint `.podar-state.json`, reanudable, como los demás runners.

## 1. Plan de poda → subagente **editorial** (modo plan de poda)
Encárgale: «plan de poda de X a Y palabras», pegándole el diagnóstico determinista. Escribe `informe/plan-de-poda.md` con checkboxes:
- **Nivel 1 · Estructural**: escenas/capítulos a cortar, fusionar o condensar, con ahorro estimado y qué contenido de continuidad se conserva o reubica.
- **Nivel 2 · Línea**: cifra objetivo por capítulo para el recorte restante, proporcional al exceso de cada uno.
Muestra en chat el resumen (exceso, suma de ahorros propuestos por nivel) y pide al autor que marque `[x]`.

## 2. Ejecución (tras marcar)
**Nivel 1 primero** (no se lima lo que se va a talar). Por cada ítem marcado:
1. `npm run coherencia -- impact` sobre lo afectado → cascada concreta → **visto bueno del autor**.
2. Cortes y fusiones con el pipeline completo: brief de reescritura (qué se elimina, qué se conserva como `<<INTOCABLE>>`, presagios/hechos a reubicar) → redactor → chequeos → crítico/lector-cero → editor → archivista. Si desaparecen capítulos: renumera ficheros, `metadatos.json` y `estado/` (mecánico, lo hace el director; el archivista actualiza memoria y matriz).
**Nivel 2 después**, capítulo a capítulo: **editor en modo poda** con la cifra del plan («deja cap-NN en ≤ N palabras»), luego `npm run lint` y `npm run tipografia -- --fix`. Verifica el conteo tras cada capítulo y apunta el checkpoint.

## 3. Cierre
`npm run hilos` (la proyección debe quedar dentro de tolerancia), `npm run repeticiones`, `npm run salud`, `npm run build`. Parte final: palabras antes → después, por dónde salió el ahorro (nivel 1 vs 2), ítems sin marcar que quedan para otra ronda. Commit por nivel. Recomienda una pasada de `/pulir` sobre los capítulos fusionados (las costuras son donde asoma el olor a IA).

## Reglas de la casa
- Nada se corta sin marca `[x]` + visto bueno de cascada en Nivel 1.
- El director no poda prosa a mano: Nivel 1 lo reescribe el redactor, Nivel 2 lo recorta el editor. Todo pasa los chequeos.
- Intocables universales: siembras y pagos de presagios, hechos de continuidad, el registro (estilo §14) y los beats del outline que sobrevivan al plan.
