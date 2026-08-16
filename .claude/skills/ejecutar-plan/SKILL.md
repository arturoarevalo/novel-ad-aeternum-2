---
name: ejecutar-plan
description: Ejecuta las acciones marcadas con [x] en informe/plan-de-accion.md; cambios estructurales con cascada dirigida y visto bueno, reescrituras de capítulo con el pipeline completo (redactor→chequeos→crítico→editor→archivista), retoques de prosa vía notas+editor y material de empaquetado. Úsalo cuando el usuario diga "/ejecutar-plan", "aplica el plan", "ejecuta lo marcado" o similar tras un /informe.
---

# /ejecutar-plan — llevar a cabo lo aprobado

Lee `informe/plan-de-accion.md`, toma SOLO las acciones marcadas (`[x]`, `[X]` o `[✔]`) y las ejecuta con el sistema de la casa. **Toda prosa nueva o modificada de la novela la escriben el redactor o el editor bajo `biblia/estilo.md`, y pasa los chequeos deterministas**: el anti-olor-a-IA no es una promesa, es el pipeline.

## 0. Preparación

- Si no hay ninguna acción marcada, dilo y para.
- Checkpoint `.plan-state.json` → `{"hechas": ["A01", …]}`. Si existe, ofrece reanudar.
- Orden de ejecución fijo: **A (estructurales) → B (capítulos) → C (prosa) → D (empaquetado)**. Reestructurar antes de pulir: no se abrillanta lo que se va a demoler.
- Si dos acciones marcadas se contradicen, o una marcada depende de otra sin marcar, avísalo ANTES de empezar y propón cómo resolverlo.

## A · Estructurales (una a una, con visto bueno)

Para cada acción A:

1. Concreta el cambio en la biblia: qué ficheros (`outline.md`, `estructura.md`, `tramas.md`, `plan-revelacion.md`, `presagios.md`, fichas…) y qué texto cambia.
2. `npm run coherencia -- impact <fichero>` → lista real de capítulos afectados. Decide por capítulo: **regenerar** (el cambio toca su espinazo) o **parche dirigido** (ajuste local). Marca pasajes a conservar como `<<INTOCABLE>>` en el brief.
3. Presenta el plan de cascada (cambio de biblia + capítulos y modo) y **espera el visto bueno**: la marca `[x]` aprobó la intención; la cascada concreta tiene coste y se confirma aquí.
4. Tras el OK: edita la biblia, y por cada capítulo afectado ejecuta el pipeline de `/capitulo` en modo reescritura: brief (que incluye la acción, qué conservar y el capítulo actual como material) → **redactor** → chequeos deterministas → **crítico** + **lector-cero** → **editor** (máx. 2 pasadas) → **archivista** (memoria, matriz, estado). Los parches menores van directos al **editor** vía nota.
5. Apunta la acción en el checkpoint y márcala en el plan: `- [x] **A01 ✔** …` con una línea de resultado.

## B · Capítulos

Como el paso A.4 pero sin tocar biblia: brief de reescritura para el capítulo señalado (objetivo de la acción, qué conservar, `<<INTOCABLE>>` si aplica) → redactor → chequeos → crítico/lector-cero → editor → archivista. Si al ejecutar descubres que la acción exige tocar la biblia, es una A encubierta: para y pide visto bueno como en A.3.

## C · Prosa

Convierte cada acción C en su nota: añade `<<NOTA: … >>` (con la referencia de pasaje que trae la acción) a `notas/cap-NN.md` y aplica el flujo de `/aplicar-notas`: **editor** con parches dirigidos, máx. 2 pasadas, `npm run lint` después. Sin reescrituras de cero.

## D · Empaquetado

Escribe/actualiza `informe/empaquetado.md`: título(s) candidatos, tagline, sinopsis de contracubierta, comparables, posicionamiento. No toca la novela. La sinopsis también sin olor a IA: nada de "En un mundo donde…", ni tricolones, ni antítesis de plantilla; gancho concreto, promesa clara.

## Cierre

1. `npm run salud` (y `npm run hilos`): todo lo bloqueante en verde.
2. `npm run build`.
3. Commits por bloque ya hechos durante la ejecución (`"Plan A01: <resumen>"`…); commit final `"Plan ejecutado: <ids>"`.
4. Borra `.plan-state.json`. Parte final en chat: acciones hechas, capítulos regenerados/parcheados, acciones pendientes sin marcar, y recomendación: nueva ronda de `/pulir` sobre los capítulos tocados y, si los cambios fueron gordos, un `/informe` de contraste en unos días.

## Reglas de la casa

- El director no escribe ni retoca prosa de la novela: siempre redactor/editor. Nada se entrega con lint en rojo.
- Las acciones D son material de venta, no prosa de la novela: puede escribirlas el director, con el mismo estándar de estilo.
- Nunca ejecutes acciones sin marcar "porque tienen sentido": el plan es del autor.
