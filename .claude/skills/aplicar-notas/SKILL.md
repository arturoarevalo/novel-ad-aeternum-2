---
name: aplicar-notas
description: Aplica las notas del autor o las revisiones externas sobre uno o varios capítulos, con parches dirigidos. Úsalo cuando el usuario diga "aplica mis notas", "incorpora las correcciones", "/aplicar-notas", "he dejado comentarios en el capítulo N" o cuando haya feedback en notas/. Decide si un cambio es local (parche) o estructural (afecta a la biblia) y, si es estructural, lo marca para regeneración bajo visto bueno.
---

# /aplicar-notas [N] — incorporar feedback

Toma el feedback del autor y lo aplica con cirugía, no a martillazos.

## Entrada
- Notas en `notas/cap-NN.md` (marcadores `<<NOTA: … >>` o texto libre). Si se indica un N, solo ese capítulo; si no, procesa todos los `notas/cap-*.md` con cambios pendientes.

## Clasifica cada nota
1. **Local** (afecta solo a la prosa del capítulo): la aplica el **editor** con parches dirigidos.
2. **De continuidad** (un dato choca con `memoria/hechos.md` o la matriz): corrige el capítulo y avisa si el conflicto nace en otro sitio.
3. **Estructural** (cambia algo de la biblia: arco, trama, presagio, cronología): **no** la apliques a ciegas. Identifica con `npm run coherencia -- impact <ruta>` qué quedaría afectado, propón el cambio en la biblia y la lista de capítulos a regenerar, y **pide visto bueno** antes de tocar nada. (Cascada dirigida, no ciega.)
   - Excepción: renombrados o cambios mecánicos (p. ej. cambiar un nombre en todo el libro) → búsqueda/reemplazo determinista directo.

## Pasos
1. Lee las notas. Clasifícalas.
2. Aplica las locales/continuidad con el **editor** (máx. 2 pasadas) y reejecuta `npm run lint`.
3. Para las estructurales, presenta el plan y espera confirmación.
4. Lanza el **archivista** si cambió algo canónico.
5. `npm run salud`, `npm run build`, commit `git commit -m "Notas aplicadas cap NN"`.
6. Marca las notas como resueltas (o vacía el fichero).

## Salida
Breve: qué notas se aplicaron, cuáles requieren tu decisión (estructurales) y el estado de lint/salud.
