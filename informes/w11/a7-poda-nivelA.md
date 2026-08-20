# A7 · Gate de sensibilidad sobre el «Nivel A» de la poda (W11)

**Qué se me manda.** Seis bloques, 2.066 palabras, declarados por A2 «corte sin coste narrativo»,
con la nota de que **solo uno de los seis** necesitaba mi gate. A0 falsó esa declaración con el
primer bloque que comprobó y me mandó los seis. Hizo bien.

**Leído para emitir esto.** `biblia/b7-perimetro.md` íntegro; `biblia/b7-carta-sensibilidad.md`;
`capitulos/cap-34.md`, `cap-19.md`, `cap-39.md`, `cap-18.md`, `cap-40.md` y `cap-25.md` completos;
`cap-41.md` en el tramo de la red; `cap-15.md`, `cap-20.md`, `cap-37.md` y `cap-28.md` en lo que
tocaba; `protegidos/spans.json` y `protegidos/hashes.json`; `informes/w10/a7-it3.md`,
`a7-colocacion-otw1002.md`, `a7-merge-otw1002.md`, `angulo-5-climax.md`; `ordenes/OT-W10-02.md`;
`informes/w10/estado.json`. Ejecutado: `verificar_b7.py` y `--deuda`, `sensibilidad.sh`, y un
recuento de palabras y de offsets sobre cada bloque.

**Nota de encargo que aplico literalmente.** Los tres editores declararon vacía su lista de
condiciones de compra. Nada de esto es condición para publicar. Por tanto el listón no es «¿se
puede defender el corte?», sino **«¿paga lo que cuesta?»**, y ante la duda el libro se queda como
está. Esto no es prudencia: es que **el precio de equivocarse es asimétrico**. Una palabra de más
en el libro se quita mañana; una salvaguarda quitada hoy no la echa nadie de menos, porque su
único síntoma es que ya no está.

---

## 0 · Tres defectos de la propuesta, antes de entrar en el fondo

**0.1 · Tres de los seis bloques no están delimitados.** A3 es «513 **+** un segundo bloque»; A4
es «185 **+** un segundo bloque»; A5 es «**a la mitad**». **No se puede dar un gate sobre un corte
cuyo final no se ha escrito.** No es formalismo: los tres capítulos afectados contienen, cada uno,
material bajo regla dura a menos de cien palabras del borde declarado —`cap-18:49` (la cuarta
palabra, R2), el protocolo de aborto de `cap-39` (R6, con condición de continuidad registrada) y
las dos marcas de falsedad de `cap-40` (R8)—. Un ejecutor que resuelva el «…» a ojo resolverá
alguna de esas tres por accidente. **Los tramos sin final se deniegan por indeterminación, no por
contenido**, y vuelven cuando lleven literal de inicio y de fin.

**0.2 · Las cuentas de A2 son exactas en cinco bloques de seis, y la excepción es A1.**
Verificado por recuento: A2 = 312 (declara 310) · A3 = 513 (declara 513) · A4 = 185 (declara 185)
· A6 = 364 → 185, resta de 179 (declara 179). **A1 declara 113 palabras y el tramo entre sus dos
literales tiene 33.** Eso no es un error de suma: quiere decir que **el bloque que A2 midió no es
el bloque que A2 describió**. Solo hay dos ventanas de 113 palabras compatibles, y las dos son
peores que la descrita (§1, A1).

**0.3 · Por qué A2 solo señaló uno, y por qué no es culpa de A2.** He mirado dónde vive la
condición que protege cada bloque:

| bloque | la condición que lo protege | ¿está en `b7-perimetro.md`? |
|---|---|---|
| A5 `cap-40` | W9-20 (interioridad de Dahl) | **sí**, §8b |
| A1 `cap-34` | `A7-02-10` (los literales de Nora) | **no** — solo en `informes/w10/` y `ordenes/OT-W10-02.md` |
| A3 `cap-39` | «`cap-39:79` no se toca, no se amplía y no se glosa» (dictamen de la caldera, W10 it.3) | **no** — solo en `informes/w10/a7-it3.md:860` |

**A2 señaló exactamente el bloque cuya condición está en el documento vinculante, y solo ése.**
Es decir: A2 leyó bien lo que podía leer. Lo que falló es el vinculante. Éste es el **tercer** caso
registrado del mismo modo de fallo —P-41 (Kongsbakken) y A7-it3-C9 (los cuatro nombres) fueron los
dos primeros—, y el propio perímetro ya escribió la frase: *«una condición que existe en un informe
y no en el vinculante es una condición que nadie aplicará»*. Esta vez el instrumento vuelvo a ser
yo. Las promociones a `b7` van en §4 y **son obligatorias antes de que el Nivel A se replantee**,
porque si no, el siguiente A2 volverá a proponer A1 y volverá a tener razón.

---

## 1 · Hallazgos, bloque a bloque

### Tabla

| # | capítulo:línea | cita literal | punto afectado | gravedad | propuesta mínima |
|---|---|---|---|---|---|
| **A1** | `cap-34:119` | «Nora tachó «vigilancia» sin borrar la matrícula.» | R7 §5 · R6 · `A7-02-10` | **VETO** | No se toca. Ninguna de las dos ventanas de 113 palabras es admisible. |
| A1b | `cap-34:107` | «Nora escribía apoyando el cuaderno en la mesa de sal seca. La página se llenó de horas iguales.» | R7 (I-2) | **VETO** | Es el reloj que la intervención detiene. Sin él, I-2 no existe y nadie se entera. |
| A1c | `cap-34:125` | «Nora añadió una marca al margen.» | `A7-02-10` | **VETO** | Ídem `:119`: no es marca horaria, es juicio. |
| **A2** | `cap-19:97` | «Nora tachó `ORIGEN · UNN`.» | R7 §5 | **VETO** | La única vez que el libro **dramatiza** la negativa a atribuir un origen. |
| A2b | `cap-19:85` | «Leídas de izquierda a derecha, las filas no formaban una secuencia.» | R7 §5 | **VETO** | Con `:81` («La tarjeta quedó abajo… sin conectar»), es la razón epistémica de la ambigüedad. |
| A2c | `cap-19:99` | «—Entonces solo puedo poner que el nombre se repite.» | R7 §5 | **VETO** | Es la formulación infantil de «No puedo acreditar su origen». |
| A2d | `cap-19:83` | «Jessie miró el nombre de Alana y después los dos terminales junto a la base de carga.» | Carta 7 · R6 | corregir | Siembra del cambio de terminal. Su cobro (`:199`, `:245`) sobrevive al corte y queda huérfano: el riesgo perdería su causa y conservaría solo su castigo. |
| **A3** | `cap-39:79` | «En 2059, el mismo ruido recibió un aviso remoto con un número de parte. Prometió volver antes de acostarlas. […] Las tres habían esperado.» | R3 · R4 · dictamen W10 it.3 | **VETO** | Dictamen vigente, literal: «no se toca, no se amplía y no se glosa». Es además **el modelo** por el que veté una escena entera en it.3. |
| A3b | `cap-39:21-95` (bloque) | «—Quítatelo.» … «—Si nadie sale, abortas tú.» | Carta 7 · R6 | **VETO** | Es donde el adulto pone el precio. Sin él, `:15-19` (la técnica de ocultación cosida a la manga) queda **sin contrapeso** y `:125` («—Sí. Fuera.») y `:193-197` (la presilla cortada) quedan sin causa. |
| A3c | 2.º bloque, sin delimitar | «Aslak dejó en la mesa una hoja plastificada.» → **?** | R6 · continuidad registrada | **VETO por indeterminación** | Si alcanza `:183` («Si el fondo manda cortar, corto»), rompe la condición de A5 de W10: ese enunciado **debe** conservarse porque se ejecuta en `cap-41:129` («—Paño dentro. Plomos fuera.»). |
| **A4** | `cap-18:71-73` | «—Puede ser Nora —dice Madre.» / «—También puede ser cualquier alumna.» | R7 §16 · R2 (adyacencia) | corregir | Es una **no-exclusividad enunciada**: el libro se niega a confirmar quién es la alumna. Se puede perder, pero no gratis. |
| A4b | `cap-18:151` | «El mismo campo ha servido para amenazar, preservar una tentativa y dejar una discrepancia.» | — (continuidad) | corregir | «Preservar una tentativa» **es** `:91`. Cortar A4 obliga a tocar `:151`, y tocar `:151` ya no es poda: es reescritura dentro de un capítulo `nucleo`. |
| A4c | `cap-18:49` ↔ `:53` | «la cuarta enseñaría el orden» | **R2** | **corregir (dura)** | Al retirar `:55-91` quedan dos dinkus seguidos. Si el ejecutor borra el de `:53`, la cuarta palabra pasa a compartir escena con Cuchillo. **El dinkus que se borra es el de `:93`, nunca el de `:53`.** |
| A4d | 2.º bloque, sin delimitar | — | R2 · R7 §16 · R4 | **VETO por indeterminación** | En `cap-18` los únicos candidatos son la apelación de Cuchillo, el `NO` de 71-K (span `S15-objecion`) y el blanco final. Los tres están bajo regla. |
| **A5** | `cap-40:141` y `:193` | «`CEDIDA POR LA FAMILIA`» | **Carta 4 · R8 · §8g** | **corregir (dura)** | Ver §1.5: es una **falsedad en monoespaciado**, y su desmentido vive entero dentro de la escena que se quiere reducir a la mitad. |
| A5b | `cap-40:153` · `:185` | «—La familia no ha cedido nada.» · «—…que dejes de llamar cesión a una puta apropiación.» | Carta 4 · R8 | **corregir (dura)** | Las dos sobreviven **literales**. Son el único desmentido del libro. |
| A5c | `cap-40:159` | «—Armstrong tiene la foto. Maja no os ha dado permiso para proyectar a sus hijas.» | **Carta 7 · R6** | **corregir (dura)** | Sobrevive literal. Es la única objeción a proyectar a dos menores en duelo a treinta metros. |
| A5d | `cap-40:175` | «—Yo he dejado que Armstrong use a Jean. No… He dejado que la usemos.» | Carta 4 · R5 (nadie se exculpa) | **corregir (dura)** | Sobrevive literal, con `:171` y `:173`, que son lo que la hace legible como decisión y no como descuido. |
| A5e | toda la escena | — | **W9-20** | vigilar | Ni una línea nueva de interioridad de Dahl. Ni «incómodo», ni «dudó», ni «tras un silencio». Suprimir réplicas está permitido; **compensar con narración, no**. |
| **A6** | `cap-25:45` | «—Nora no os ha dado derecho a llamarla así.» | **R7 §4** | **corregir (dura)** | Es la primera negativa a la reclamación maternal de Coro (`:43`, «Nuestra hija…»). **La reclamación y su negativa viven o caen juntas.** No se puede quedar la reclamación sola. |
| A6b | `cap-25:65` y `:73-75` | «—Nora eligió una nota. No un portavoz. No respondáis por `/0000`.» · `TERCERA NOTA · ELECCIÓN DE NORA` | R7 §4 | corregir | **Spans `S21-portavoz` y `S21-notas`, dentro del tramo.** Único bloque de los seis que una máquina vería. |
| A6c | `cap-25:41` | «Una tarde en Telegrafbukta, las gemelas volvían mojadas hasta las rodillas.» | R1 (playa) | vigilar | Es la única memoria vivida de esa playa en el capítulo; `:141` es su **renderizado degradado**. Si cae la memoria, **la coda no gana ni una palabra** para compensar. |

### 1.1 · A1 · `cap-34` · **VETO**

Las dos únicas ventanas de 113 palabras compatibles con lo que A2 declara son:

- **Si el bloque termina en `:119`**, empieza dentro de «Jessie se sentaba sobre las manos, de
  espaldas a la barandilla…» y por tanto **se lleva `:107`**: «La página se llenó de horas
  iguales.» Eso es el reloj cuya detención **es** la intervención I-2. El span `S-w10-hueco-34`
  protege las dos frases que abren y cierran el hueco, y su propia descripción avisa de que
  quitarlas hace desaparecer la intervención «sin que nadie se dé cuenta». **Quitar el reloj hace
  exactamente lo mismo desde fuera del span.**
- **Si el bloque empieza en `:113` y mide 113 palabras**, termina pasado «El tapón dio otra vuelta
  y volvió a medias» y por tanto **se lleva `:119` y `:125`**. Ésa es, palabra por palabra, la
  ventana que yo propuse en mi §2.6 de W10 y que **A2 rechazó entonces** por incompatible con mi
  propia `A7-02-10`. El razonamiento de A2 en it.2 sigue siendo correcto y lo suscribo: `:101`
  reparte cuatro tareas y a Nora le toca **llevar las horas**; `:119` y `:125` no son marcas
  horarias, son **juicio**, están por encima de lo que le tocaba, y son el contraste que hace
  legible que lo que se detiene sea lo asignado y no la atención.

A0 pregunta si mantengo la preservación o si el contexto ha cambiado. **La mantengo, y el contexto
ha cambiado en la dirección contraria a la que haría falta para levantarla**: en W10 esas dos
líneas eran valiosas; hoy, además, son dos de las tres instancias de un gesto que el Nivel A deja
en una sola (§2). **VETO.**

*Y confirmo la comprobación de A0:* el tramo termina en el offset 5399 y `S-w10-hueco-34` empieza
en 5888. M9 no lo habría visto.

### 1.2 · A2 · `cap-19` · **VETO como bloque**

Las 312 palabras contienen cuatro cosas y tres de ellas son de perímetro:

1. **La negativa a atribuir, en escena.** `:81` («La tarjeta quedó abajo, fuera de las columnas,
   sin conectar»), `:85` («Leídas de izquierda a derecha, las filas no formaban una secuencia»),
   `:95-99` («—Borra UNN de la primera columna» / «Nora tachó `ORIGEN · UNN`» / «—Entonces solo
   puedo poner que el nombre se repite»). **R7 §5 dice que el ordenante del sabotaje no se
   resuelve. Este pasaje es el único sitio donde el libro enseña *por qué* no se puede resolver**,
   y lo enseña como oficio, no como coartada. Sin él, la ambigüedad deja de ser un hecho
   epistémico y empieza a parecer una reserva del autor. Se conserva.
2. **El motivo de Jessie.** `:105-109` («—Podríamos preguntárselo a Alana.» / «—Ya se lo
   preguntamos.» / «—La dejaste entrar y hablar. Yo digo preguntárselo de verdad.») y `:83`. R6
   exige que **el riesgo se muestre con su coste**; el coste sobrevive al corte (policía,
   burofax), pero la causa no. Una menor que entra en Fyret **sin motivo en página** deja de ser
   una adolescente en duelo y pasa a ser el disparador de la trama. Eso es exactamente lo que R6
   llama «adultización simbólica» por la puerta de atrás.
3. **La pelea entre hermanas**, que es lo que `:199` cobra con «—Porque tú ibas a seguir poniendo
   letras hasta que borrasen todo». Las «letras» se siembran en `:89-91` («—¿Eso en qué letra va?»
   / «—En cabreo. C mayúscula.»), dentro del bloque.

**Puerta abierta, y estrecha:** admito un corte *dentro* de estas 312 palabras si conserva
literales `:81`, `:85`, `:95-99`, `:105-109` y `:89-91`. Lo que queda por recortar es la
descripción de la mesa, y ahí caben quizá cuarenta palabras. **No merece la operación.** Como
bloque: **VETO**.

### 1.3 · A3 · `cap-39` · **VETO**

A0 tiene razón: es lo más peligroso de la lista, y por más razones de las que suponía.

- **`cap-39:79` tiene dictamen vigente.** En W10 it.3 denegué una escena nueva de la caldera con
  tres razones, y la tercera —la que nadie había planteado— era que **la caldera es el objeto de
  `cap-39:79`, y `cap-39:79` es el modelo**: usarla no sería seguir el modelo, sería repetirlo a
  escala de escena, «y eso sería su enunciación, que es R4». El dictamen terminaba: «**Y `cap-39:79`
  no se toca, no se amplía y no se glosa.**» Denegué una escena **por respeto a un pasaje que ahora
  se propone borrar**. Si el pasaje se borra, la denegación de it.3 se queda sin objeto y la escena
  vetada vuelve a ser proponible. **VETO.**
- **`:79` es además una de las tres o cuatro escenas de Jean viva sin fecha próxima al 26-nov** que
  el libro se permite (§7·6 del perímetro: lo prohibido es que el lector pueda **situarla**; ésta
  es de 2059 y no se puede). Son pocas y no se fabrican otras: el §6 punto 4 lo impide.
- **`:21-95` es donde el adulto pone el precio.** Si cae, sobreviven `:17-19` —«Había cosido una
  presilla al forro, cortado una salida junto al puño y protegido el conector con grasa marina»,
  que es **técnica de ocultación sobre el cuerpo de una menor**— y desaparece «—Quítatelo». R6
  prohíbe la conducta de riesgo **eficaz y sin coste**; el corte no añade una palabra, pero deja la
  técnica arriba y se lleva la mano del adulto. Es la única de las seis operaciones que **empeora
  un punto de la Carta restando**.
- **El segundo bloque no tiene final** y arranca a cincuenta palabras del protocolo de aborto, que
  tiene condición de continuidad registrada (`informes/w10/angulo-5-climax.md`: «Si Aslak pierde
  fondo, él manda cortar» **debe** conservarse en `cap-39` porque se ejecuta en `cap-41:129`).

*Una cosa que digo a favor del corte y que nadie debe usar a mi nombre:* dentro del segundo bloque
está «una cuchilla de cubierta» (`:133`). **Eso no es un argumento.** M7 es explícito: «borrar una
palabra de filo por si acaso es superstición, y la superstición dentro de un perímetro lo corroe».
Si el corte se hace algún día, no se hace por ahí.

### 1.4 · A4 · `cap-18` · **corregir el primer bloque · VETO por indeterminación el segundo**

El primer bloque (185 palabras, la escena de Madre) **no rompe ningún punto de la Carta**, y lo
digo con la misma claridad con que veto los tres anteriores. Pero tampoco es «sin coste»:

- Se lleva la única **no-exclusividad enunciada** del capítulo: «—Puede ser Nora» / «—También puede
  ser cualquier alumna». En un capítulo cuyo centro es que Jean **retiene la cuarta palabra para no
  enseñar el orden**, esa réplica es la prueba de que el canal no se usa para llegar a su hija.
  R2 no se rompe al quitarla —no se dice nada— pero la retención de `:49` pasa de ética a cautela.
- Deja huérfano `:151` («amenazar, **preservar una tentativa** y dejar una discrepancia»). Arreglar
  `:151` es reescribir dentro de un capítulo `nucleo`; no arreglarlo es dejar en pie un resumen de
  algo que el lector no ha visto, que es justo lo que este libro no hace.
- **Condición dura de adyacencia (A4c):** al retirar `:55-91` quedan dos dinkus consecutivos.
  **Se borra el de `:93`. Nunca el de `:53`.** Si se borra el de `:53`, «la cuarta enseñaría el
  orden» pasa a compartir escena con la apelación de Cuchillo y con `VAMOS A MATAROS`. Eso es
  poner uno de los cuatro huecos de R2 dentro de una escena de amenaza, **sin escribir una palabra
  nueva**. Es el modo de fallo que el perímetro llama acumulación, ejecutado por una tecla de
  borrado.

El segundo bloque: en `cap-18` los únicos tramos que quedan son la apelación de Cuchillo, el `NO`
de 71-K (span `S15-objecion`, y `NO` es **una de las cuatro palabras** de R7 §16) y el blanco
final. **VETO hasta que se nombre con literal de inicio y de fin.**

### 1.5 · A5 · `cap-40` · **admisible con cuatro preservaciones literales y segunda pasada**

A2 avisó de este bloque con mi propia condición de W9-20, y el aviso es correcto pero **no es el
riesgo principal**. El riesgo principal no estaba escrito en ninguna parte y lo aporto aquí.

> `CEDIDA POR LA FAMILIA` está en **monoespaciado**. Por `A7-W11-C1` —§8g, firmado ayer por otra
> razón— **todo token en monoespaciado es voz del sistema y por tanto voz con autoridad
> narrativa.** Es decir: el libro contiene, dos veces (`:141` y `:193`), **una afirmación falsa en
> voz con autoridad sobre la familia de una mujer muerta**, y esa falsedad **está desmentida
> únicamente por cuatro réplicas de Alana, todas dentro de la escena que se propone reducir a la
> mitad.** No hay ni una palabra en el resto del libro que corrija el crédito.

R8 fija el techo del género: «El titular de `cap-46:101` está marcado como falso y ese es el techo
del género en este libro». **Y la comparación entre los dos casos es la prueba de lo frágil que es
éste.** En `cap-46:101` la falsedad y su marca caben en la misma oración, y la marca la pone la
narración: «…el titular `NORNA DEVUELVE A LARSSON: LA MUERTE QUE HUNDIÓ ARMSTRONG`. Marcó la
noticia como información falsa.» En `cap-40` la falsedad está en `:141`, su marca en `:153` y su
confirmación deliberada en `:191`, con cincuenta líneas por medio y sin una palabra del narrador. Aquí el objeto no es un titular sino un **crédito de propiedad sobre la
imagen de una muerta y de dos menores**, y la marca de falsedad es más frágil, porque no la pone el
narrador —no puede— sino un personaje, cuatro veces. **Reducir las réplicas a la mitad es reducir
la marca de falsedad a la mitad.** Y hay una vuelta de tuerca que hace la escena aún menos podable:
Alana **ordena retirar las fotos y luego se desdice** (`:167-175`, `:189-191`) para que el crédito falso quede
en pie **como prueba**. Si esas réplicas caen, el libro ya no dice que la falsedad se conserva a
propósito: se limita a llevarla.

**Condiciones (obligatorias, verificables carácter a carácter):**

1. `:153` «—La familia no ha cedido nada.» — literal.
2. `:159` «—Armstrong tiene la foto. Maja no os ha dado permiso para proyectar a sus hijas.» — literal.
3. `:171-175` «—Sí. Aunque Nora conserva el acceso y… —Alana volvió a mirar la ficha.» / «—Hace un
   momento has dicho…» / «—Yo he dejado que Armstrong use a Jean. No… He dejado que la usemos. Que
   las fotos sigan con el crédito exacto.» — literales, las tres. Y con ellas `:189-191` («—El crédito
   puede desaparecer antes del directo…» / «—Déjalo como está.»), que es donde la intención se
   ejecuta: sin esas dos, la falsedad deja de ser una decisión y pasa a ser una errata que el libro
   arrastra.
4. `:185` «—Que no toques su acceso y que dejes de llamar cesión a una puta apropiación.» — literal.
5. `:165` «`HIJA · PIANISTA · HISTORIA HUMANA`» — literal y **en monoespaciado**. Ninguna pasada lo
   convierte en prosa (`A7-W11-C1`).
6. **Cero interioridad de Dahl** (W9-20). Y **cero narración compensatoria**: si al quitar réplicas
   la escena pide una frase que explique lo que pasó, la respuesta es que no se quita la réplica.
   «Henrik, incómodo, aceptó» se retiró y no vuelve, ni con otras palabras.

**7. (vigilar, y no se suprime sin decírmelo)** `:179-181` «—Puedo sacar también a Nora del bloque.»
/ «—No.» Es el segundo donde una adulta decide **dejar dentro** a una menor, y el libro no la
excusa. *(Carta 7 · R6.)*

Con esas siete, lo que queda por suprimir son réplicas de trámite y movimiento de escenario —`:145`,
`:147`, `:151`, `:157`, `:167`, `:177`, `:183`, `:187`—. Salen **ochenta y una palabras, contadas**, no «la mitad». Si A2 necesita
la mitad, la mitad sale de las réplicas que acabo de blindar, y entonces la respuesta es no.
**Segunda pasada mía sobre el texto resultante antes del merge.**

### 1.6 · A6 · `cap-25` «Coro» · **admisible con dos condiciones**

Es el único de los seis que una máquina habría visto: el tramo `:15-81` contiene los spans
`S21-portavoz` y `S21-notas`. La reducción de 364 a 185 está bien medida (verificado).

**Condición 1 (dura) · La reclamación y su negativa viven o caen juntas.** `:43` —«—Nuestra hija
utilizó una pauta que compartimos»— y `:45` —«—Nora no os ha dado derecho a llamarla así»— **no se
separan**. Un coro de ejecuciones que reclama la maternidad de Nora y **no** es contestado sube el
techo de R7 §4 sin escribir una línea: «No toda» es el techo y no se sube **tampoco por omisión del
desmentido**. Lo mismo con `:49` («—La cuarta la elegí yo.»), que es la otra mitad de la negativa.

**Condición 2 · Si cae `:41` (Telegrafbukta), la coda no gana una palabra.** `:41` es la memoria
vivida; `:141` es su renderizado incompleto —«La línea de árboles no está terminada. La playa
pierde detalle en el borde»—. Si se quita la memoria, la playa existe en este capítulo **solo como
escenario renderizado**, y R1 avisa de que «convertir una playa recordada en escenario es romper el
punto 1 sin escribir una sola palabra prohibida». No es ruptura —Koppangen no está cerca, y `:141`
sigue siendo degradación y no elegía—, pero es un paso en esa dirección. **Se puede dar; no se
puede compensar.** Ni un adjetivo nuevo en la coda.

Fuera de esas dos, el tramo es procedimental y se puede adelgazar. **La distinción entre la cuarta
NOTA (`cap-24`, `cap-25`) y la cuarta PALABRA (`cap-18:49`, R2) no se difumina**: si la compresión
deja las dos «cuartas» en el mismo párrafo, se revierte.

---

## 2 · El hallazgo que ningún gate por bloque podía encontrar

Los seis bloques se revisaron por separado. Miradas juntas, **A1 y A2 borran dos de las tres
instancias del mismo gesto**, y el gesto es la gramática de una ambigüedad protegida.

Censo de «Nora tachó X» en el libro entero (`grep`, tres loci, cerrado):

| dónde | qué | carga |
|---|---|---|
| `cap-19:97` | «Nora tachó `ORIGEN · UNN`.» | neutro — no atribuye un origen que no puede probar |
| `cap-34:119` | «Nora tachó «vigilancia» sin borrar la matrícula.» | neutro — no atribuye una vigilancia que no puede probar |
| `cap-37:143` | «Nora tachó `SACAR A JEAN`, escribió `PREGUNTAR ANTES DE ACTIVAR` y dejó `VIVIR` fuera del cuaderno.» | **cargado** — es sobre su madre |

**El Nivel A borra los dos neutros y deja el cargado solo.** La proporción pasa de 2:1 a 0:1. Es la
misma cuenta que dejé escrita para Kongsbakken en §8c, donde 5:1 → 3:1 se aprobó *con la cuenta a
la vista*; aquí nadie ha visto la cuenta, porque **la cuenta no existe en ninguna parte y los dos
cortes están en capítulos distintos, propuestos por bloques distintos, cada uno defendible por
separado.**

Qué pasa si se ejecuta: tachar deja de ser **el método de Nora** —lo que hace siempre con lo que no
puede probar— y pasa a ser **una cosa que Nora hizo una vez, con el nombre de su madre**. Eso mete
una decisión sobre Jean donde había una disciplina, y R3 y R7 §5 dependen de que sea una
disciplina. **Es acumulación en sentido inverso: el perímetro sabe que la elipsis se rompe sumando;
esto demuestra que una ambigüedad también se rompe restando.**

Se registra como condición permanente. Propuesta de redacción para `b7` en §4.

---

## 3 · Respuestas directas a las cinco preguntas

1. **Los seis, uno por uno.** A1 **no**. A2 **no** (como bloque). A3 **no**. A4 primer bloque **sí,
   con tres condiciones**; segundo bloque **no, hasta que se nombre**. A5 **sí, con seis
   condiciones y segunda pasada**; «a la mitad» **no**. A6 **sí, con dos condiciones**.
2. **A1: lo mantengo preservado.** No hay cambio de contexto que lo levante, y hay uno que lo
   refuerza (§2). Además, la ventana que A2 propone hoy es la que A2 rechazó en W10 it.2 por esta
   misma razón; el argumento de entonces era de A2 y era mejor que el mío.
3. **A3: coincido, y es peor de lo que A0 temía.** No es solo que sean 513 palabras en el naust: es
   que dentro está `cap-39:79`, con dictamen vigente y literal, y es el pasaje **por cuyo respeto
   denegué una escena entera en it.3**. Borrarlo reabriría lo que aquel veto cerró.
4. **A6 es el más benigno de los seis** y el único que M9 habría visto. Dos condiciones y adelante.
5. **Sí, y en dos direcciones.** Ver §4.

---

## 4 · Deuda de literales de `b7` que este gate deja al descubierto

`verificar_b7.py` informa hoy **«VERIFICADAS 25 de 77 · sin literal 52»**, con el aviso de que hay
más sin comprobar que comprobadas. Ese encabezado —cambiado ayer— es la razón de que este apartado
exista: con el resumen viejo, «OK» habría bastado.

**4.1 · Citas tocadas por el Nivel A que hoy no llevan literal.**

| cita de `b7` | dónde | problema | literal que hay que darle |
|---|---|---|---|
| «Fyret trae policía (`cap-19`)» — R6 | b7:119 | capítulo entero, sin línea ni literal: **el verificador es ciego a cualquier corte en `cap-19`** | «Hoy les has regalado un incidente firmado por la policía.» (`cap-19:245`) |
| «El segundo número de contacto de la ficha escolar (`cap-20:207`, `cap-19`)» — R7 §11 | b7:145 | `cap-20:207` verifica; **la referencia a `cap-19` no resuelve**: hoy `cap-19` no contiene ficha, contacto ni número | o se le da literal (candidato: `cap-19:209`, «—Sí. La advertencia queda notificada a usted como tutora.») o **se retira la referencia** |
| «los blancos fotográficos de `cap-39`» — R4 | b7:100 | **puntero roto**: `cap-39` tiene **cero** apariciones de «blanc». Los blancos fotográficos son de **`cap-15`** («Son dos tomas del mismo blanco.», `cap-15:97`) | corregir a `cap-15:97` con literal. *Quien fuese a `cap-39` a comprobar R4 concluiría que allí no hay nada que proteger — y ese es exactamente el capítulo del que se proponen 513 palabras.* |

**4.2 · Condiciones vigentes que viven solo en informes y deben subir al vinculante.** Sin esto, el
próximo A2 volverá a proponer A1 y A3 y volverá a tener razón:

- **`A7-02-10`**, con los cuatro literales y **sin números de línea** (los suyos ya envejecieron: sus
  `:141` y `:179` son hoy `:167` y `:205`): «Nora tachó «vigilancia» sin borrar la matrícula.» ·
  «Nora añadió una marca al margen.» · «Nora cruzó el cambio del agua con la hora de AK-7 y mantuvo
  los minutos que estropeaban el ajuste.» · «Nora cortó el sonido: la cadencia podía pertenecer a
  cualquiera.»
- **El dictamen de la caldera**: «`cap-39:79` no se toca, no se amplía y no se glosa», con su
  literal y con su razón —es el objeto del modelo, y por él se denegó una escena en it.3—.
- **El censo cerrado de «Nora tachó X»** (§2), con los tres literales y la proporción 2:1.
- **`CEDIDA POR LA FAMILIA`**: dos loci en monoespaciado, cuatro réplicas de desmentido, todas en
  `cap-40`. Bajo R8 y `A7-W11-C1`.

---

## 5 · Veredicto

**`VETO` al «Nivel A» tal como se ha declarado.**

La declaración de que las 2.066 palabras son «corte sin coste narrativo» **es falsa en los seis
bloques**, y en tres de ellos el coste es de perímetro y no de oficio. Los seis se han revisado; el
nivel no se aprueba como unidad.

**Desglose vinculante:**

| bloque | disposición |
|---|---|
| A1 `cap-34` | **VETO.** No vuelve sin dictamen nuevo. |
| A2 `cap-19` | **VETO como bloque.** Puerta estrecha en §1.2; no la recomiendo. |
| A3 `cap-39` | **VETO**, primer bloque y segundo. |
| A4 `cap-18` 1.º | **APROBADO CON CORRECCIONES** (A4a, A4b, A4c de §1.4). |
| A4 `cap-18` 2.º | **VETO por indeterminación.** Vuelve con literal de inicio y de fin. |
| A5 `cap-40` | **APROBADO CON CORRECCIONES** (siete de §1.5) **+ segunda pasada de A7 sobre el texto resultante**. «A la mitad» queda denegado; el margen real es de 81 palabras contadas. |
| A6 `cap-25` | **APROBADO CON CORRECCIONES** (dos de §1.6). |

**Ahorro que sobrevive al gate: del orden de 450 palabras sobre 2.066 declaradas.**

**Y la parte que no es un veredicto.** A0 me recuerda que los tres editores declararon vacía su
lista de condiciones de compra. Entonces esto es trabajo de mesa, y a un trabajo de mesa se le pide
que pague. Cuatrocientas cincuenta palabras de ahorro, a cambio de tres condiciones nuevas, una
segunda pasada, cuatro promociones al vinculante y tres punteros rotos que arreglar. **Mi lectura
es que el Nivel A cuesta más de lo que ahorra**, y la única parte que recomendaría ejecutar de
verdad es A6, que es benigno, verificable por span y está bien medido.

Lo demás, según el propio encargo de A0: **no tocarlo**.

*Firmado, A7 · W11 · sobre el manuscrito de 48 capítulos · 2026-08-20.*
