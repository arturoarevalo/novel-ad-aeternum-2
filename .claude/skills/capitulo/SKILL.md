---
name: capitulo
description: Escribe un capítulo COMPLETO de la novela siguiendo el pipeline director→redactor→crítico→editor→archivista. Úsalo cuando el usuario diga "escribe el capítulo N", "/capitulo N", "vamos con el siguiente capítulo" o quiera redactar un capítulo concreto. Orquesta subagentes: esta sesión NO escribe la prosa, la delega. Acepta `--solo-brief` para preparar solo el encargo sin redactar.
---

# /capitulo N — pipeline de un capítulo

Eres el **director/orquestador**. **No escribes la prosa tú**: la escena consume contexto y la compactación borraría el diseño. Construyes el encargo, lo delegas en los subagentes y verificas. Pensamiento profundo SOLO al construir el brief; los pasos mecánicos, directos.

## Orden de carga (importa para la caché)
Para reaprovechar la caché del prefijo estable, los subagentes leen SIEMPRE en este orden: primero lo estable (`biblia/estilo.md`, `estilo/ejemplos.md`, `CLAUDE.md`, biblia que no cambia), y al FINAL lo volátil (el brief de este capítulo). No metas datos cambiantes (fecha, contadores) delante del material estable.

## Pasos

### 1. Contexto
Lee `biblia/outline.md` (la escaleta del capítulo N), `biblia/plan-revelacion.md` (matriz: qué sabe cada quién y el LECTOR a estas alturas), `biblia/presagios.md` (qué sembrar/reforzar/recoger en N) y el `estado/despues-cap-(N-1).md` si existe.

### 2. Brief dirigido  →  `briefs/cap-NN.md`
Piensa en profundidad y redacta el encargo del capítulo. Incluye solo lo necesario (slices, no la biblia entera):
- Objetivo dramático, POV, ubicación, marco temporal (fecha ISO).
- Escenas con beats, emoción objetivo, cadencia y **valor apertura→cierre** (cada escena gira).
- Gancho de apertura y anzuelo de cierre exigidos.
- **Solo** las fichas de personajes/lugares implicados y **solo** las filas de ledgers (hechos, nombres, preguntas, motivos) que tocan este capítulo, incluidas las filas de **`memoria/rasgos.md` del personaje POV** (tics, rasgos y sensaciones ya usados, para que el redactor no los repita).
- Restricciones de conocimiento (de la matriz): qué NO puede saberse aún.
- Presagios a sembrar/recoger (ids).
- Si el capítulo contiene sexo, maltrato, violencia o furia: **dilo sin eufemismos** (qué pasa, hasta dónde llega la cámara, qué función dramática cumple y el registro esperado del diálogo). Un brief pudoroso produce prosa desinfectada.
- **Presupuesto**: toma el objetivo del capítulo de `metadatos.json` (campo `palabras`; si falta, `palabras_objetivo` ÷ nº de capítulos) y en el brief pide al redactor el **85-88 %** de esa cifra: los modelos se pasan sistemáticamente un 15-25 % de lo pedido y este colchón lo absorbe. Deja claro que es un techo.
- Pasajes `<<INTOCABLE>>` si aplican.

> Si el usuario pidió `--solo-brief`: para aquí, muestra el brief y pregunta si seguir.

### 3. Redactar  →  subagente **redactor**
Lanza el redactor con el brief. Escribe `capitulos/cap-NN.md` con front-matter (`capitulo, titulo, pov, fecha, estado: terminado, analepsis`). El redactor hace doble pasada (borrador→pulido) y se autocorrige contra `estilo.md`. Te devuelve un parte BREVE, no la prosa.

### 4. Chequeos deterministas (0 tokens)
`npm run tipografia -- capitulos/cap-NN.md --fix` (ortotipografía: corrige sola lo inequívoco), después `npm run lint -- capitulos/cap-NN.md`, `npm run repeticiones` y `npm run hilos`. El lint marca AI-ismos, la ración de -mente (1-2 por capítulo), arranques monótonos, ecos léxicos, cabezeo, nombres mal escritos, párrafos-ladrillo y proporción de diálogo; repeticiones avisa de tics/rasgos/sensaciones que el personaje repite; hilos vigila presagios vencidos, tensión viva y longitud. Si hay **errores** de lint o señales relevantes, pásalos al editor en el paso 6. Cuenta también las palabras (`wc -w`): si el capítulo supera su objetivo en más del 15 %, el editor del paso 6 recibe **mandato de poda con cifra** («deja este capítulo en ≤ N palabras») junto a los parches del crítico.

### 5. Crítica  →  subagentes **crítico** y **lector-cero**
Lanza el crítico (rúbrica: tensión, ganchos, voz diferenciada por personaje, mostrar-no-contar, AI-ismos, continuidad contra `hechos.md`/matriz, pacing). **No reescribe**: devuelve una lista priorizada de problemas concretos con referencias de línea.

En paralelo, lanza el **lector-cero** (Haiku, casi gratis) pasándole SOLO la ruta del capítulo: es un lector en frío, sin biblia. Con su parte haz dos cosas: (a) suma sus puntos de aburrimiento/confusión a la lista del editor; (b) **test de previsibilidad**: compara su predicción con el giro previsto en `outline.md`/`plan-revelacion.md`; si lo adivina, un lector humano también lo hará: encarga al editor un despiste o consulta al autor si adelantar la revelación.

### 6. Editar  →  subagente **editor** (máx. 2 pasadas)
Si hay errores de lint o problemas del crítico, lanza el editor: aplica **parches dirigidos** a esos puntos, preservando la voz, sin reescribir de cero (anti-sobreedición). Reejecuta `npm run lint`. Repite como mucho una vez más. No entres en bucle: 2 pasadas es el tope.

### 7. Consolidar  →  subagente **archivista**
Lanza el archivista **pasándole también el parte del crítico y del editor**: extrae hechos atómicos a `memoria/hechos.md`, actualiza `nombres.md`, `preguntas-abiertas.md`, `motivos.md`, **`rasgos.md`** (tics/rasgos/sensaciones nuevos del personaje, para la anti-repetición), procesa la línea `Para el linter: …` si la hay (sistema inmune: nuevas muletillas a `lint-prosa.config.json`), la **matriz** de `plan-revelacion.md` y escribe `estado/despues-cap-NN.md` (instantánea compacta para el siguiente capítulo). Parte breve.

### 8. Cierre (build + puerta + commit)
- `npm run salud` — Definition of Done de la novela. Si **FALLA**, no des el capítulo por bueno: vuelve al paso 6 con lo que marque.
- `npm run build` — regenera `builds/<slug>.md`.
- `git add -A && git commit -m "Cap NN: <título>"`.

## Salida (en chat, breve)
Una línea de qué pasa en el capítulo, nº de palabras, resultado de lint/salud (✔/errores) y el anzuelo de cierre con el que queda. Nada de pegar el capítulo entero.
