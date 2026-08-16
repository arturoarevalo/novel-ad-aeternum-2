---
name: informe
description: Genera un informe editorial profesional de la novela completa (review de comité, puntuaciones, escenarios de ventas) y un plan de acción con checkboxes que el autor marca y ejecuta después con /ejecutar-plan. Úsalo cuando el usuario diga "/informe", "review editorial", "informe de lectura", "¿está lista mi novela?" o "evalúa la novela completa". No edita nada.
---

# /informe — review editorial + plan de acción

Evaluación de novela completa con ojos de comité editorial. **Aquí no se edita nada**: el resultado es `informe/informe-editorial.md` (diagnóstico en 21 secciones con puntuaciones) y `informe/plan-de-accion.md` (acciones marcables con `[x]`). La ejecución es de `/ejecutar-plan`.

## 1. Preparación (0 tokens)
- Ejecuta y guárdate los resúmenes: `npm run lint -- --todos`, `npm run repeticiones`, `npm run similitud`, `npm run hilos`, `npm run salud`, y `wc -w capitulos/*.md | tail -1`.
- Comprueba si existe `notas/_resumen-pulido.md` (pásalo también si está).
- Si faltan capítulos de `biblia/metadatos.json`, no bloquees: el informe evaluará potencial vs demostrado; dilo en el encargo.

## 2. Informe → subagente **editorial**
Lánzalo con: el recuento de palabras, los resúmenes del instrumental y la ruta de su guion (`.claude/skills/informe/plantilla-informe.md`). Él lee biblia/estados/prosa por su cuenta (muestreo si es larga), escribe el informe y el plan, y te devuelve un parte breve.

Es la llamada más cara del sistema (lee media novela o entera): avisa al autor antes si la novela supera ~80.000 palabras.

## 3. Devolución al autor (breve, en chat)
- Veredicto + recomendación editorial simulada.
- Las 5 puntuaciones más bajas de la matriz.
- Nº de acciones del plan por bloque (A estructurales / B capítulos / C prosa / D empaquetado).
- Instrucción: "Abre `informe/plan-de-accion.md`, marca con `[x]` lo que apruebas y lanza `/ejecutar-plan`."

Commit de los dos ficheros: `git commit -m "Informe editorial + plan de acción"`.

## Reglas de la casa
- Prohibido editar `capitulos/`, `biblia/` o `memoria/` en esta skill.
- No maquilles el informe al resumirlo: si el veredicto es duro, se transmite duro.
- `informe/` está fuera del grafo de coherencia a propósito: un informe no vuelve obsoleto ningún capítulo; eso solo lo hacen las decisiones del autor al ejecutar el plan.
