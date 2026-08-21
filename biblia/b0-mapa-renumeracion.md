# B0 · Mapa de renumeración (W10-prep, 2026-08-19)

**Los ficheros de `capitulos/` y `ordenes/` pasan a numeración consecutiva `cap-01`…`cap-48` y `OT-01`…`OT-48`, coherente con el orden de lectura y con `capitulos[]` del manifiesto.** Antes convivían `cap-01…cap-41` con `cap-n1…cap-n7` intercalados por `orden_lectura` decimal.

**Qué se actualizó:** `protegidos/spans.json` (los 129 spans), `biblia/metadatos.json` (campo `archivo`), toda `biblia/` **salvo `b3-lexicon.json`, que NO se actualizó y cuyas 311 referencias siguen en la numeración anterior** *(corregido el 2026-08-20: la afirmación original era un «OK» falso dentro del documento que existe precisamente para explicar la renumeración — la misma especie de fallo que este proyecto lleva veinticuatro veces registrando. Lo encontró A7.)*, toda `ordenes/`, y el campo `ot` del frontmatter de los 41 capítulos afectados.

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
| B | **`cap-w2.md` «Papeletas»** | **36,5** | 389 |

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


---

## RENUMERACIÓN FINAL · 2026-08-21 · decisión de autor

**Se acabaron los huecos y los decimales.** El libro tiene **49 capítulos** y los
ficheros van del 01 al 49 **sin saltos**, con `n` y `orden_lectura` correlativos y
coincidentes con el número impreso. Es la operación que W10 aplazó dos veces —«se hace
una vez y al final, como en W7»— y ésta es esa vez.

**Estado del que se venía:** ficheros del 01 al 48 **con un hueco en el 31** (fundido en
W10 it.1), más `cap-w1` (orden 21,5) y `cap-w2` (orden 36,5), los dos capítulos escritos
en W10.

| antes | ahora | título |
|---|---|---|
| `cap-w1` | **`cap-22`** | La mosquitera |
| `cap-22` | **`cap-23`** | No determinista |
| `cap-23` | **`cap-24`** | NIDHOGG |
| `cap-24` | **`cap-25`** | La cuarta nota |
| `cap-25` | **`cap-26`** | Coro |
| `cap-26` | **`cap-27`** | Auditoría |
| `cap-27` | **`cap-28`** | Inventario |
| `cap-28` | **`cap-29`** | La canción |
| `cap-29` | **`cap-30`** | Accidente |
| `cap-30` | **`cap-31`** | EDDA |
| `cap-w2` | **`cap-37`** | Papeletas |
| `cap-37` | **`cap-38`** | El ladrillo |
| `cap-38` | **`cap-39`** | La oferta |
| `cap-39` | **`cap-40`** | Bajamar |
| `cap-40` | **`cap-41`** | Soldagen |
| `cap-41` | **`cap-42`** | Caída |
| `cap-42` | **`cap-43`** | Cuchillo abre los ojos |
| `cap-43` | **`cap-44`** | No soy un modelo |
| `cap-44` | **`cap-45`** | Norna |
| `cap-45` | **`cap-46`** | Depósito |
| `cap-46` | **`cap-47`** | Sombra |
| `cap-47` | **`cap-48`** | Acta |
| `cap-48` | **`cap-49`** | El siguiente Soldagen |

*(Los 26 restantes conservan su nombre. El 31 vuelve a existir: lo ocupa el que era el
30, «EDDA».)*

### Qué se reescribió y qué NO

**Reescrito:** el manifiesto (`n`, `archivo`, `orden_lectura`), el frontmatter de los 49
capítulos, `spans.json` (71 spans re-apuntados), los hashes (regenerados) y las
referencias de `b1`, `b2`, `b3-canon`, `b4-chekhov`, `b5`, `b6`, `b7-carta`,
`b7-perimetro`, `b8` y `CLAUDE.md`. Todo **en una sola pasada por fichero**, que es la
lección de W7: la primera vez se hizo en pasadas sucesivas y un capítulo quedó ambiguo
entre dos distintos.

**NO reescrito, a propósito:**

- **Este documento por encima de esta línea.** Su tabla es el registro de la
  renumeración de W7 y reescribirla la destruiría. *(Se reescribió por error durante
  esta operación y se restauró de inmediato.)*
- **`informes/` y `ordenes/`** — 6.646 referencias. Son el registro histórico de lo que
  se decidió y cuándo, y cada informe habla del libro **tal como era el día que se
  escribió**. Mismo criterio que en W7.
- **`b3-lexicon.json` y `b4-ledger.json`.** No por criterio: **porque sus referencias ya
  estaban ancladas a la numeración anterior a W7**, como descubrió A7 en W11. Aplicarles
  el mapa de hoy sobre una base ya falsa produciría **un error nuevo con aspecto de
  corrección**. Necesitan reconstrucción completa por cita literal, no traducción.

### Y la advertencia que vale para todo lo reescrito

**Se ha traducido el número de capítulo, no el número de línea.** Donde una referencia
decía `30:247` ahora dice `31:247`, y la línea 247 sigue siendo la que era **solo si
nadie tocó ese capítulo después de escribirse la referencia**. Varios se tocaron.

**Los números localizan; solo la cita literal instruye y verifica.**
