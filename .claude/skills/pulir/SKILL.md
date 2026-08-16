---
name: pulir
description: Pasada de pulido de una novela terminada, capítulo a capítulo, SIN editar la prosa; genera notas accionables en notas/cap-NN.md (manierismos repetidos, repeticiones semánticas entre capítulos, AI-ismos, diálogos, show-don't-tell) y un resumen final. Úsalo cuando el usuario diga "/pulir", "/pulir N", "pule la novela", "pasada final" o "quita el olor a IA". Las notas se aplican después con /aplicar-notas.
---

# /pulir [N] — pasada de pulido (solo notas)

Diagnóstico fino de novela terminada. **Aquí no se edita nada**: el resultado son notas por capítulo (`notas/cap-NN.md`, marcador `<<NOTA: … >>`) que el autor revisa y aplica luego con `/aplicar-notas`.

## 0. Alcance y reanudación
- Con argumento (`/pulir 7`): solo `cap-07`.
- Sin argumento: TODOS los capítulos de `biblia/metadatos.json`, **en orden** (importa: el radar anti-repetición se acumula de capítulo en capítulo).
- Checkpoint en `.pulir-state.json` → `{"hechos": ["cap-01", …]}`. Si existe al arrancar sin argumento, pregunta al autor: ¿reanudar o empezar de cero? (de cero = borrar el checkpoint y `notas/_recursos.md`).

## 1. Instrumental global (0 tokens, una sola vez)
`npm run lint -- --todos`, `npm run repeticiones`, `npm run similitud` y `npm run hilos`.
Guárdate los hallazgos agrupados por capítulo: se los repartirás a los subagentes. Las señales globales (pares de `similitud`, ecos de `repeticiones`, avisos de `hilos`) asígnalas al capítulo donde está la segunda aparición o donde se puede arreglar.

## 2. Bucle por capítulo (secuencial, en orden)
Para cada `cap-NN` pendiente:
1. **Lector-cero** (Haiku, casi gratis): pásale SOLO la ruta del capítulo. Guarda su parte (aburrimiento, confusión, predicción, personajes planos).
2. **Pulidor** (Opus): encárgale el capítulo pegándole en el prompt (a) los hallazgos del instrumental de ESE capítulo y las señales globales que lo toquen, y (b) el parte del lector-cero. Él lee por su cuenta `estilo.md`, `rasgos.md` y `notas/_recursos.md`, escribe `notas/cap-NN.md`, actualiza el radar `notas/_recursos.md` y te devuelve un recuento de una línea.
3. Apunta `cap-NN` en `.pulir-state.json`.

No proceses capítulos en paralelo: `_recursos.md` debe crecer en orden.
Modo económico (solo si el autor lo pide): saltar el lector-cero, o pulidor en Sonnet (pierde finura justo en repeticiones semánticas).

## 3. Resumen final → `notas/_resumen-pulido.md`
Al terminar el alcance:
- Tabla por capítulo: notas totales / ALTA / categorías dominantes / estructurales.
- **Transversales**: repeticiones semánticas entre capítulos (pares cap-X ↔ cap-Y), tics globales de la novela, señales vivas de `hilos`.
- Siguientes pasos: revisar las notas → `/aplicar-notas NN` (capítulo a capítulo, o todo) → `npm run salud` y `npm run build`.

Muestra el resumen (breve) en el chat, borra `.pulir-state.json` y commitea SOLO las notas: `git commit -m "Pulido: notas cap NN–MM"`.

> Aviso esperable: con notas pendientes, `npm run coherencia`/`salud` marcará esos capítulos como obsoletos. Es el diseño (nota pendiente ⇒ capítulo por reprocesar); desaparece al aplicarlas.

## Reglas de la casa
- Prohibido editar `capitulos/`, `biblia/` o `memoria/` en esta skill. Solo `notas/*` y el checkpoint.
- El pulidor decide qué merece nota; tú (director) no añadas notas de tu cosecha ni reescribas las suyas.
- Si un capítulo ya tiene `notas/cap-NN.md` del autor, el pulidor añade las suyas bajo `--- pulido ---` sin pisar nada.
