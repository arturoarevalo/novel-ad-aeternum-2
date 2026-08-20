# B0 · Mapa de renumeración (W10-prep, 2026-08-19)

**Los ficheros de `capitulos/` y `ordenes/` pasan a numeración consecutiva `cap-01`…`cap-48` y `OT-01`…`OT-48`, coherente con el orden de lectura y con `capitulos[]` del manifiesto.** Antes convivían `cap-01…cap-41` con `cap-n1…cap-n7` intercalados por `orden_lectura` decimal.

**Qué se actualizó:** `protegidos/spans.json` (los 129 spans), `biblia/metadatos.json` (campo `archivo`), toda `biblia/`, toda `ordenes/`, y el campo `ot` del frontmatter de los 41 capítulos afectados.

**Qué NO se actualizó, a propósito: `informes/`.** Son el registro histórico del proceso, con fecha, y describen el estado del libro en el momento en que se escribieron. Reescribirlos falsearía el rastro. **Para leerlos, usar esta tabla.**

Y sigue rigiendo la regla del proyecto, que ahora importa más que nunca: **los números localizan; solo la cita literal instruye y verifica.**

| antes | ahora | | antes | ahora |
|---|---|---|---|---|
| `cap-01`…`cap-07` | igual | | `cap-25` | `cap-30` |
| **`cap-n5`** | **`cap-08`** | | **`cap-n4`** | **`cap-31`** |
| `cap-08` | `cap-09` | | `cap-26` | `cap-32` |
| `cap-09` | `cap-10` | | `cap-27` | `cap-33` |
| **`cap-n1`** | **`cap-11`** | | `cap-28` | `cap-34` |
| `cap-10` | `cap-12` | | `cap-29` | `cap-35` |
| `cap-11` | `cap-13` | | `cap-30` | `cap-36` |
| `cap-12` | `cap-14` | | `cap-31` | `cap-37` |
| `cap-13` | `cap-15` | | `cap-32` | `cap-38` |
| `cap-14` | `cap-16` | | `cap-33` | `cap-39` |
| **`cap-n7`** | **`cap-17`** | | `cap-34` | `cap-40` |
| `cap-15` | `cap-18` | | `cap-35` | `cap-41` |
| `cap-16` | `cap-19` | | `cap-36` | `cap-42` |
| **`cap-n2`** | **`cap-20`** | | `cap-37` | `cap-43` |
| `cap-17` | `cap-21` | | `cap-38` | `cap-44` |
| `cap-18` | `cap-22` | | `cap-39` | `cap-45` |
| `cap-19` | `cap-23` | | `cap-40` | `cap-46` |
| `cap-20` | `cap-24` | | **`cap-n6`** | **`cap-47`** |
| `cap-21` | `cap-25` | | `cap-41` | `cap-48` |
| `cap-22` | `cap-26` | | | |
| **`cap-n3`** | **`cap-27`** | | | |
| `cap-23` | `cap-28` | | | |
| `cap-24` | `cap-29` | | | |

**Los siete capítulos nuevos del plan** (en negrita) son hoy los **8, 11, 17, 20, 27, 31 y 47**.

**Los diez de protección total** son hoy: `cap-01`, `cap-03`, `cap-04`, `cap-05`, `cap-10`, `cap-24`, `cap-28`, `cap-48`, más `00-aviso` y `99-recursos`.

---

## Hueco de W10 · `cap-31` deja de existir (OT-W10-01, 2026-08-19)

La fusión de `cap-31` «Interferencias» dentro de `cap-32` «Casa prestada» deja **un hueco
deliberado en la numeración**. El libro tiene **47 capítulos** y los ficheros van de
`cap-01` a `cap-48` **sin `cap-31`**.

**No se renumeró, y la razón está escrita en `b7-perimetro.md` §2:** «durante unas horas,
quien aplicara el perímetro por número de fichero habría errado en cuarenta de los cuarenta
y ocho casos». Con 133 spans, 65 citas del perímetro y este mismo mapa apuntando a nombres
de fichero, renumerar en caliente cuesta mucho más que un hueco. La renumeración es una
operación aparte y se hace **una vez y al final**, como en W7.

| | antes | después |
|---|---|---|
| capítulos del libro | 48 | **47** |
| ficheros | `cap-01`…`cap-48` | `cap-01`…`cap-48` **menos `cap-31`** |
| `cap-32.md` | «Casa prestada», 1.770 palabras | «Casa prestada», **3.394** — el capítulo más largo del libro |
| rangos de `partes[]` | 25–36 · 37–48 | **sin tocar** (son cotas de `orden_lectura`, no cuentas) |
| numeración impresa | 1…48 | 1…47, correlativa (el compilador numera por orden de lectura) |

**Consecuencia para cualquiera que trabaje con estos ficheros:** a partir de `cap-32`, el
número de fichero va **uno por delante** del número impreso. `cap-48.md` es el capítulo 47.
Los números localizan; solo la cita literal instruye y verifica.


---

## Segundo cambio de W10 · «La asamblea» se parte en dos (OT-W10-04, 2026-08-20)

`cap-36` «La asamblea» se escinde **por un dinkus que ya estaba en v0** —no se abre una
costura, se asciende la que puso el autor— en:

| | fichero | orden | palabras |
|---|---|---|---|
| A | `cap-36.md` «La asamblea» | 36 | 1.053 |
| B | **`cap-w2.md` «La firma»** | **36,5** | 389 |

Y se suprimen **127 palabras de topografía de playa que añadimos en W2**, incluida la que iba
a quedar en primera posición del capítulo nuevo: «La arena delante del banco queda libre. Las
demás se acercan por tramos y dejan a un lado el aro de piedras con su fuego. Las últimas
esperan detrás, sobre la nieve.» **A7 la vetó ahí** porque reúne el banco, el aro de piedras y
la nieve —los objetos del duelo de las hijas— abriendo un capítulo justo después de un
borrado: «un entierro compuesto, en énfasis máximo».

`cap-w2.md` **abre y cierra en prosa del autor**: «Madre abre tres casillas…» y «En el centro,
la fogata ajena sigue ardiendo sola.»

**Estado de la numeración:** 49 capítulos. Ficheros `cap-01`…`cap-48` **sin `cap-31`**, más
`cap-w1` (orden 21,5) y `cap-w2` (orden 36,5). Los números de fichero y los impresos ya no
coinciden en ningún tramo. **Los números localizan; solo la cita literal instruye y verifica.**
