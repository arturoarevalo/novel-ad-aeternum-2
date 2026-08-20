# A7 · Gate de merge · W10 · iteración 3 · `cap-w1.md` «La mosquitera»

**Rama `w10-it3`, sin mergear. 833 palabras, POV Maja, `orden_lectura: 21.5`, `analepsis: true`,
fecha solo en el frontmatter (`2060-07-09`), entre «Cuchillo» y «No determinista».**

Leído el capítulo entero dos veces, sus dos vecinos, y releído `cap-27:71-73`, `cap-17`,
`cap-05:59`, `cap-39:79` y `cap-30:273-307` contra él. Todo lo que afirmo abajo lo he verificado
yo con mis propios comandos; donde repito un dato de A0 lo digo.

---

## 1 · Verificación material (mía, no heredada)

| comprobación | resultado |
|---|---|
| recuento | **833 palabras** ✓ (coincide con A0; techo que puse: 1.000; `cap-17` mide 1.096) |
| la cadena ve el fichero | `chapter_paths()` → **48 capítulos, `cap-w1` visto: True** ✓ |
| validador de frontmatter | **0 avisos** ✓ |
| M9 | **10 ficheros y 136 spans íntegros** ✓ |
| `sensibilidad.sh` | **cero hits atribuidos a `cap-w1`** ✓ |
| `b7-patrones-A` (14 patrones) | **cero hits** ✓ |
| `b7-patrones-B` (9 patrones) | **cero hits** ✓ |
| `b6-lista-negra-patrones` | **cero hits** ✓ |
| barrido propio de vocabulario de riesgo | tres coincidencias, las tres benignas: «se salía **siempre** por la esquina de abajo», «la que se salía **siempre**», «el **último** lado». Iterativo de la tarea y lado del marco. **Ninguna es materia de Carta.** |
| parte | `orden_lectura 21.5` cae en **Parte II «Fije la vista» (13-24)**. **No es la cuenta atrás.** ✓ `S2` |

---

## 2 · Dos discrepancias entre el informe de A0 y el fichero

Las digo primero porque afectan a la frase «la verifiqué yo además de A3b»: si lo verificado fue
otro borrador, la verificación no cubre lo que está en la rama.

| A0 dice | el fichero dice |
|---|---|
| «Termina en **«Entró a ras.»**» | «Entró a ras.» es la **línea 139**; el capítulo sigue **36 líneas más** y termina en «**—Floja —dijo Jean. / —Puesta.**» (`:173-175`) |
| «**cuatro** réplicas de Jessie» | **tres**: `:81` «—Nos vamos a casa de Ida.», `:85` «—Detrás.», `:89` «—Vale.» |

**Ninguna de las dos empeora el capítulo — el final real es mejor que el que A0 describe**, porque
cierra el bucle de `:29-31` («—Va a quedar floja.» / «—Va a quedar puesta») y porque «Entró a ras»
como último verso habría sido un cierre con carga. Pero **el dictamen que sigue está emitido sobre
el fichero, no sobre la descripción**, y conviene que A0 vuelva a mirar qué revisó.

---

## 3 · Auditoría condición por condición

### Del sitio

| | veredicto | verificación |
|---|---|---|
| **S1** no adyacencia a `cap-04`, `10`, `23`, `34`, `39`, `41`, `45`, `46`, `47`, `48` | **✓** | vecinos: `cap-21` «Cuchillo» y `cap-22` «No determinista». Ninguno en la lista. |
| **S2** fuera de la cuenta atrás | **✓** | Parte II. |
| **S3** después de `cap-06` | **✓** | 21,5 > 6. |
| **S4** fecha solo en el frontmatter | **✓** | La prosa da **dos horas de reloj** («A las nueve», «A las diez aquí») y **ninguna fecha**. Una hora dentro del día no sitúa. |
| **S5** fuera del mørketid | **✓ · ejecución óptima** | «A las nueve el sol seguía dando en el mismo sitio de la pared», ventana abierta, niñas en bicicleta hasta las diez, mosquitos de la hierba. **Es verano, y el lector lo sabe sin que nadie lo diga.** El espinazo del libro no ocupa esa estación en ninguna página: no hay con qué alinearla. Esto es exactamente la coartada que pedí, y está mejor resuelta de lo que la escribí. |
| **S6** ninguna magnitud medida dos veces | **✓ por construcción** | ver abajo |

**`S6`, magnitud por magnitud.** Objetos y ritos de `cap-17` —salero, metrónomo, taza reparada,
táper SOPA, cuchara de servir, paragüero, felpudo, sopa, pan, piano—: **ninguno presente**. Alana:
**ausente**. Edad de las gemelas: Jessie aparece cinco líneas sin un solo marcador de edad ni de
cuerpo. Estado de la casa: nada degradado, nada comparado. Reparto de tareas: **una tarea, una
persona**. Piano: **ausente**. Atributos de Jean: ver §4.

### De la escena

`E1` tercera cosa **✓** (la goma de una mosquitera) · `E2` sin marco y sin recordante **✓** ·
`E3` cero síntoma **✓** (§4) · `E4` cero marcador de última vez **✓** · `E5` prueba de relectura
invertida **✓ con dos vigilancias** (§5) · `E6a`/`E6b` cero objetos de `cap-04`, cero caldera
**✓** · `E7` cero origen de las cuatro palabras **✓** · `E8` cero Kongsbakken **✓** · `E9` cero
noveno cumpleaños **✓** · `E10` cero cinturón **✓** · `E11` lugar admisible **✓** · `E12` nadie
habla del porqué del divorcio **✓** · `E13` no fija cuándo se vieron por última vez **✓** ·
`E14` nadie enuncia una rima **✓** · `E15` las menores a lo suyo **✓**.

**`E4` y `E13` merecen una frase, porque están resueltos por una decisión de forma y no por
vigilancia: la escena no tiene umbral.** Nadie llega y nadie se va. Una escena sin puerta **no
puede ser una despedida**, y no puede fechar el último encuentro. Es la solución estructural
correcta y no se me había ocurrido a mí.

**`E2`.** La primera oración es impersonal e iterativa —«El marco de la mosquitera se sacaba una
vez al año»— y el iterativo es **de la tarea, no de las visitas**, que es la diferencia entre una
escena y una costumbre de ver a alguien. Maja es el agente desde el párrafo dos, y la única
interioridad del capítulo es procedimental y suya: «Si se dejaba a la mitad de un lado, la goma
hacía un bulto. Había que sacarla entera». **No hay sabedor.**

### `T1` y `C7`

**`T1` (techo declarado):** no está en el presente anterior a la muerte. **✓**

**`C7` — «la escena no puede explicar “No lo había”, ni a distancia». Verificado por mí, no
heredado. PASA.** Releído `cap-27:71-73` inmediatamente después: las dos líneas siguen igual de
opacas. En la escena nueva **nadie pide nada, nadie retiene nada, no hay altillo, no hay repuestos
y no hay ningún objeto que pase de una mano a otra**. Y la única afirmación disputada de Maja que
el texto no confirma por resultado —«Ese estaba dentro antes de la malla»— **es verdadera y el
lector la ha visto**: el mosquito entra en `:41` y la malla se extiende en `:43`. Comprobado línea
a línea.

---

## 4 · Las cuatro cosas que A0 somete

### 4.1 · «—Eso se hace con tijeras». **Se queda. No la toques.**

La Carta prohíbe **el método del acto**, y el método del acto **no existe en este libro en ninguna
forma**: no hay nada hacia lo que unas tijeras puedan acumular. `R1` habla de acumulación de
objetos que un lector pueda montar como preparación; una tijera **nombrada para ser descartada**,
en una cocina de julio, en un capítulo sin relación con la muerte, no monta nada.

Y hay una razón positiva para conservarla que pesa más que la ausencia de objeción: es una de las
cuatro disputas de procedimiento, y es aquella en la que la respuesta de Maja **demuestra oficio**
(«—Eso se hace con el canto»). Esa demostración es parte de la maquinaria que protege el capítulo
(§4.3). Quitarla debilitaría lo que lo defiende.

> **Y lo digo con todas las letras porque importa más que un veto: borrar una palabra de filo por
> si acaso es superstición, y la superstición dentro de un perímetro lo corroe.** Un perímetro que
> empieza a tachar objetos cortantes de escenas domésticas acaba tachando cocinas. Se queda.

### 4.2 · Jean recoge desecho dos veces. **No lo leo como puesta en orden. Aprobado con dos condiciones.**

Las dos: «Jean la enrolló en dos vueltas y la dejó en el borde de la mesa» (`:39`, la goma vieja) y
«Jean recogió la tira del suelo y la dejó encima de la goma vieja» (`:149`, el recorte).

`R3` prohíbe expresamente el marcador de **puesta en orden**, y la pregunta es buena. **No lo es,
por tres razones concretas:**

1. **No son sus cosas.** Poner los asuntos en orden es disponer de lo propio o cerrar obligaciones.
   Jean apila **basura ajena, en la mesa ajena, durante el trabajo ajeno**. Lo que eso retrata es a
   alguien que quiere participar en una tarea que no la deja entrar y hace lo único que puede
   tocar. Es exclusión, no despedida.
2. **Está construido como textura, no como beat.** No cae en un corte de sección, no cierra el
   capítulo, no la mira nadie y va dentro de una secuencia de acciones sobre el recorte. Mi prueba
   de `E5` no es «¿puede alguien alegorizarlo?» —todo puede alegorizarse—, sino **«¿está construido
   para ganar?»**. No lo está.
3. **Son dos.** Dos es una manía; tres sería un motivo.

> **Condiciones permanentes (`A7-it3-M1`).** **No hay un tercero**, ni en este capítulo ni en
> ninguna otra escena de Jean viva. **Y nadie lo comenta jamás**: ninguna voz —personaje o
> narrador, aquí o en cualquier capítulo posterior— observa que Jean recogiera, ordenara o dejara
> las cosas colocadas. En el momento en que alguien lo nota, deja de ser una manía y pasa a ser un
> signo.

### 4.3 · «Maja exacta con hechos pequeños», el puente de mala fe. **Aprobado, y explico por qué no cierra nada**

El puente es real y A0 hace bien en someterlo: si la escena establece que Maja no se equivoca con
hechos domésticos, entonces «había otro en el altillo / No lo había» se desplaza de *error* hacia
*mentira*.

**Ese desplazamiento existe y es admisible, por dos razones que conviene dejar escritas:**

1. **Mi `C7` prohíbe «un patrón del que la mentira del hervidor sea instancia». Esto es el patrón
   contrario.** Una instancia sería que Maja también retuviera algo aquí. No retiene nada, no niega
   nada y no cede en nada. La mentira del hervidor queda como **una desviación de su norma**, no
   como un ejemplo de ella. Saber que fue una desviación hace las dos líneas **más filosas**, no
   más explicadas — y `R3` protege contra la explicación, no contra la fuerza.
2. **Lo que la Carta 3 protege es el porqué de la muerte, no la legibilidad de un personaje.**
   Que Maja mintiera sobre un hervidor es un hecho sobre una mujer que se queda con un hervidor.
   No es una causa, no está cerca de una causa, y ninguna voz lo conecta con nada.

> **Condición permanente (`A7-it3-M2`).** **Ninguna línea, en ningún capítulo ni en ningún
> paratexto, conecta la exactitud de Maja con el hervidor.** Ni «Maja no se equivocaba con estas
> cosas», ni un eco, ni una vuelta al altillo. La enunciación sería la ecuación (`R4`), y es lo
> único que convertiría este puente en un puente de verdad.

### 4.4 · La vecindad de `cap-21:179`. **Vigilar. La defensa ya está en el libro y hay que no tocarla**

`cap-21:179` —«En casa la tocaban a cuatro manos: todas las teclas negras, sin orden…»— es un
recuerdo doméstico en POV Jean a dieciocho líneas del final de su capítulo. El riesgo que A0
intuye es el correcto y es grave si se materializa: **que el lector atribuya el capítulo nuevo a la
memoria de Jean**, lo que le instalaría un recordante — y el recordante sería una muerta dentro de
una máquina buscando su matrimonio. Eso es exactamente la versión que prohibí.

**No ocurre, por cuatro cosas verificadas:**

1. Entre `:179` y el corte hay **dieciocho líneas de texto de sistema**, y `cap-21` termina en
   «`COPIA_SUPERVISIÓN` cambia de `PENDIENTE` a `ACEPTADA`.» La distancia tonal con «El marco de la
   mosquitera se sacaba una vez al año» es máxima. Es el mismo corte duro que enmarca `cap-17`.
2. El reparto no coincide: `:179` son **Nora y Jessie**; el capítulo nuevo es **Maja y Jean**.
3. La única interioridad del capítulo nuevo es **procedimental y de Maja**.
4. **Y la defensa fuerte ya estaba escrita, en `cap-05:59`:** «Busca una escena y encuentra el
   banco del piano… **Jean no recupera las palabras.**» El capítulo nuevo es cuarenta y seis
   réplicas de diálogo. **Si fuera de Jean, contradiría una regla que el libro estableció sobre
   ella en el capítulo 5.** No puede ser suya.

> **Condición permanente (`A7-it3-M3`).** `cap-05:59` **no se toca** —es fichero `total` y es lo
> que hace imposible la atribución—; y **no se añade interioridad de Jean a la coda de `cap-21`**.
> Si una oleada futura mueve este capítulo detrás de otro capítulo POV Jean que cierre en imagen
> doméstica, la atribución vuelve a estar disponible y hay que volver a mirarla.

---

## 5 · Dos cosas que A0 **no** somete y que salen de leer los vecinos

### 5.1 · **Que Nora esté fuera de la escena es lo que hace segura la sede `21|22`**

El vecino derecho es `cap-22` «No determinista», que **es el capítulo de Kongsbakken**: «la mesa
donde en mayo le habían pedido que esperase el resultado de la primera prueba», «una acreditación
de visitante. Ni aspirante ni alumna», y `:149` «Kongsbakken era el único centro compatible».

Es decir: el lector sale de una escena doméstica de verano con Jean viva y entra directamente en la
chica que no entró, con credencial de visitante. **Si la escena midiera a Nora, esa sutura sería un
antes/después de la hija del conflicto** —y el conflicto es `cap-10:73`, el único locus cargado del
topónimo—. Sería `S6` roto por composición y `§8c` rozado por adyacencia.

**No lo es porque Nora no aparece.** Está fuera: «—¿Y Nora? —preguntó Jean. / —Detrás.» La única
hija en escena es Jessie, que no es la hija de Kongsbakken. La sede funciona **por esa ausencia**,
y no por casualidad de colocación.

> **Condición permanente (`A7-it3-M4`), y es la más importante de este gate.** **Nora no entra
> nunca en esta escena.** Ni una réplica, ni una entrada por la ventana, ni un plano desde la
> calle. Cualquier oleada futura que quiera «equilibrar a las gemelas» aquí estará convirtiendo la
> sutura con `cap-22` en un antes/después, y la razón por la que hoy pasa el gate desaparecerá sin
> que salte ninguna herramienta. **Y `—¿Y Nora? / —Detrás.` no gana glosa, eco ni recogida en
> ningún capítulo posterior.**

### 5.2 · El mosquito. **Vigilar, con una condición que cierra la puerta antes de que nadie la abra**

El mosquito entra por el hueco antes de que la malla esté puesta (`:41`), se queda en el techo toda
la escena, y al final las dos discuten de dónde vino: «—Por ahí ha entrado ese.» / «—Ese estaba
dentro antes de la malla.» / «—Por ahí ha entrado.»

**Lo que me hizo pararme:** en un libro sobre un suicidio, una discusión sobre si el daño entró por
una barrera o **ya estaba dentro antes de que la barrera existiera** es, en abstracto, un
contrafáctico en miniatura. Y `R3` prohíbe todo contrafáctico sobre la escalada interceptada de
`cap-30:89-105` en cualquier boca, **incluida la negativa cerrada**.

**Comprobado, y por eso no es hallazgo:**

- **No existe pareja de rima en el libro.** Barrido de «ya estaba dentro / desde dentro / se coló /
  lo llevaba dentro» y de «mosquito / insecto / mosquitera / malla»: los únicos «malla» son un
  árbol envuelto en malla (`cap-11:19`) y el paño de pesca de `cap-43`, registros ajenos. **El
  mosquito está solo.** Un eco necesita dos términos.
- **No hay puente léxico con `cap-30`**: ni barrera, ni escalada, ni tarde, ni llegó, ni protección.
- La disputa es sobre **procedencia**, no sobre **tiempo**, que es la variable del contrafáctico.
- Y nadie la enuncia. `R4`: «Enunciar un eco lo convierte en ecuación».

> **Condición permanente (`A7-it3-M5`).** **El mosquito no vuelve** —ni en este capítulo, ni
> nombrado después, ni con una segunda instancia en ninguna parte—. **Y ningún vocabulario de
> malla, barrera, filtro, tamiz, cedazo o «lo que se cuela» se aplica jamás a Jean, a la escalada
> interceptada, al equipo de apoyo, a la ayuda ni a la protección**, en ningún capítulo ni en
> ningún material de trabajo. Hoy la puerta está cerrada porque falta el segundo término; esta
> condición impide que alguien lo plante dentro de un año creyendo que hace una rima bonita.

### 5.3 · El bucle «floja / puesta»

Abre en `:29-31` y cierra en `:173-175`. Es lo más parecido a un símbolo que hay en el capítulo: una
dice que va a quedar floja, la otra dice que va a quedar puesta, y son las últimas dos palabras.

**Pasa, y la razón es que el objeto no se comporta como el matrimonio.** La malla **aguanta**: «Los
muelles entraron a la primera», «El marco no se movió», «Las dos veces cedió lo mismo». Si la
mosquitera fallara, sería un símbolo. Como no falla, **la disanalogía es la protección**. Y he
verificado que no hay pareja de rima: los cuatro «floja/puesta» del resto del libro son una
mordaza, una sudadera, una capucha y una bota.

> **Condición permanente (`A7-it3-M6`).** Nadie ecoa «floja» ni «puesta» fuera de este capítulo con
> sujeto humano o conyugal, **y la mosquitera no falla nunca en ningún texto posterior**. La razón
> por la que hoy no es un símbolo es que el objeto funciona.

---

## 6 · Un error mío, de ayer, que este gate ha destapado

En la adenda II escribí, como magnitud de `S6`: «**el piano con quién lleva el compás**, que el
libro ya mide dos veces (`cap-17` y `cap-27:137-149`): **esa magnitud ya está cerrada en dos y la
escena nueva sería la tercera**».

**Es falso.** Censo hecho hoy: el piano doméstico tiene **más de veinticinco loci** —`cap-03:173-195`,
`cap-05:59/69/89/197`, `cap-07:109`, `cap-10:195-221`, `cap-12:21`, `cap-15:69/293`, `cap-17`,
`cap-21:179`, `cap-22:61`, `cap-24:233-275`, `cap-26:141`, `cap-27:27/131/137-151`, `cap-28`,
`cap-30:273-307`, `cap-40:139-161`, `cap-43:115`, `cap-46:53-67`, `cap-48:59`— y hasta la magnitud
estrecha («quién lleva el compás») está en **tres** y no en dos: `cap-15:69` —«Repetía el compás con
el metrónomo parado»— es la tercera.

**No cambia el gate** (el capítulo no tiene piano), pero **sí cambia la condición**, y la corrijo:

> **`S6`, corrección.** El piano **no** es una magnitud cerrada en dos: es la figura doméstica
> central del libro y está saturada. Queda fuera de la escena nueva **por otra razón**: es, después
> de la caldera, **el objeto más datado del libro** —la tecla del mi un milímetro más baja «desde el
> otoño» (`cap-27:27`), la esquina hundida del metrónomo, las teclas negras, la prueba de mayo—, y
> un objeto con historia documentada es ordenable contra todo. **Prohibición idéntica, razón
> distinta.** Y una regla escrita con la razón equivocada hace daño (`§3`).

**Tercera vez hoy que un recuento mío falla, y las tres han fallado en la misma dirección: dando
por cerrado lo que estaba abierto.** Lo dejo escrito con mi firma porque llevo un día entero
auditando instrumentos que se equivocaban a la baja y en silencio, y el que más veces se ha
equivocado hoy soy yo.

---

## 7 · Tono

La referencia que se me encarga defender es la contención de `cap-04`, `cap-10`, `cap-28` y
`cap-46`. **El capítulo está dentro de ella y en algún tramo por debajo:** cuarenta y seis réplicas,
cero metáfora, cero comentario del narrador, cero interioridad que no sea procedimiento, y un final
de dos palabras que no explica nada. No consuela, no instruye y no cierra.

**Y la propiedad que hace todo el trabajo, dicha por si alguien la poda por «repetitiva»: Jean está
exactamente igual que en `cap-17`.** Discutidora, precisa, equivocada, insistente. Una magnitud
**sin cambio** no produce gradiente, y aquí eso no es una casualidad de escritura: es lo único que
impide leer la escena como un antes. **La igualdad de Jean es el antisíntoma.** Si una oleada
futura la matiza —más callada, más cansada, más suave, más presente— el capítulo se convierte en lo
contrario de lo que hoy aprueba este gate.

> **Condición permanente (`A7-it3-M7`).** El retrato de Jean en `cap-w1` no se ablanda, no se
> matiza y no gana un solo gesto de interioridad. Cualquier pasada de línea sobre este capítulo
> vuelve a A7.

---

## 8 · Sobre el instrumento nº 21

`chapter_paths()` con glob `cap-(\d{2}|n\d)\.md`: comprobado que **hoy ve `cap-w1` y cuenta 48**.
Tomo nota de lo que A0 señala y lo hago mío, porque me afecta directamente:

> **Un capítulo con nombre no canónico era invisible para el compilador, para las métricas, para
> M8, para el validador y para M9 — y las cinco herramientas informaban «OK».** Es decir: existía
> una forma de añadir texto a este libro que **mi propia verificación por hash no habría mirado
> nunca**, y que no habría producido ninguna alarma.

Ningún capítulo se escribió así en ninguna oleada anterior (los ficheros históricos son `cap-NN` y
`cap-nN`, y `b0-mapa-renumeracion.md` los cubre), de modo que **no hay daño retroactivo**. Pero el
modo de fallo es el peor de los veintiuno: no medía mal, **no medía**, y decía que sí.

> **`A7-it3-M8`.** M9 no vuelve a informar «OK» sobre un conjunto que no ha enumerado: la salida de
> `proteger.sh verificar` debe decir **cuántos ficheros de `capitulos/` ha visto** y contrastarlo
> con el recuento del manifiesto. Un «íntegro» sobre un conjunto vacío es la misma frase que un
> «íntegro» sobre el libro entero, y eso es inadmisible en la única herramienta que sostiene el
> perímetro por hash.

---

## 9 · Tabla de hallazgos

| # | Locus | Cita literal | Punto | Gravedad | Propuesta |
|---|---|---|---|---|---|
| 32 | `cap-w1` completo | — | Carta 1–8, `S1-S6`, `E1-E15`, `T1`, `C7` | **cumple** | Ninguna corrección de texto. |
| 33 | `cap-w1:145` | «—Eso se hace con tijeras —dijo Jean.» | R1 | **sin objeción · se conserva** | No se borra. Borrarla sería superstición y debilitaría el antisíntoma. |
| 34 | `cap-w1:39`, `:149` | «Jean la enrolló en dos vueltas…» · «Jean recogió la tira del suelo…» | R3 | **vigilar** | `M1`: no hay un tercero y nadie lo comenta jamás. |
| 35 | `cap-w1` ↔ `cap-27:71-73` | «Maja dijo que había otro en el altillo.» / «No lo había.» | R3 · `C7` | **cumple** | `M2`: nadie conecta nunca la exactitud de Maja con el hervidor. |
| 36 | `cap-21:179` ↔ `cap-w1:15` | «En casa la tocaban a cuatro manos…» | `E2` · R3 | **vigilar** | `M3`: `cap-05:59` no se toca; sin interioridad de Jean en la coda de `cap-21`. |
| 37 | `cap-w1:83-85` ↔ `cap-22:15-21` | «—¿Y Nora? —preguntó Jean. / —Detrás.» | `S6` · `§8c` | **vigilar · condición dura** | `M4`: **Nora no entra nunca en esta escena**; la réplica no gana eco. |
| 38 | `cap-w1:41`, `:165-169` | «—Ese estaba dentro antes de la malla.» | R3 (contrafáctico) | **vigilar** | `M5`: el mosquito no vuelve; ningún léxico de malla o barrera se aplica jamás a la ayuda, a la escalada o a Jean. |
| 39 | `cap-w1:29-31`, `:173-175` | «—Va a quedar floja.» / «—Puesta.» | R4 | **vigilar** | `M6`: sin eco humano; la mosquitera no falla nunca. |
| 40 | retrato de Jean | igual que en `cap-17` | Carta 3 · `S6` | **cumple · frágil** | `M7`: no se ablanda. Cualquier pasada de línea vuelve a A7. |
| 41 | adenda II, `S6` | «el piano… ya está cerrada en dos» | método | **corregir (mío)** | Falso: >25 loci, y la magnitud estrecha está en tres. Prohibición idéntica, razón corregida. |
| 42 | informe de A0 | «Termina en “Entró a ras”» · «cuatro réplicas de Jessie» | método | **corregir (de A0)** | El fichero termina 36 líneas después y Jessie tiene tres. Revisar sobre qué texto se verificó. |
| 43 | `chapter_paths()` | glob `cap-(\d{2}\|n\d)\.md` | instrumento | **corregir** | `M8`: M9 debe declarar cuántos ficheros ha enumerado y contrastarlo con el manifiesto. |

---

# VEREDICTO

## `APROBADO`

**`capitulos/cap-w1.md` «La mosquitera» pasa el gate de sensibilidad sin una sola corrección de
texto.** Cumple la Carta en sus ocho puntos, las nueve reglas, las cinco cuentas, el techo `T1` y
las veintiuna condiciones que emití para esta escena. La prueba obligatoria `C7` la he verificado
yo línea a línea y pasa.

**Tres cosas quiero decir sin ahorrar, ya que A0 lo pide.**

**Primera: no mide.** Lo he buscado por las siete magnitudes de `S6`, una a una, y por la prueba de
relectura invertida. La única magnitud que la escena comparte con `cap-17` es el carácter de Jean,
**y no ha cambiado** — que es lo contrario de medir. La textura de la separación la entrega una
sola línea oblicua («—¿Y en tu cocina?»), y la entrega **la ausencia de reparto**, no una
comparación.

**Segunda: dos de sus aciertos no son míos y merecen constar.** La escena **sin umbral** resuelve
`E4` y `E13` por forma en vez de por vigilancia, y no se me había ocurrido. Y **dejar a Nora
fuera** es lo que hace segura una sede que yo aprobé sin haber leído su vecino derecho: la aprobé
por lo que no tenía, y funciona por algo que sí tiene.

**Tercera: lo que queda frágil no es el texto, es su futuro.** Este capítulo pasa por siete
propiedades que un editor bienintencionado retiraría por mejorarlo: la ausencia de puerta, la
ausencia de Nora, la dureza de Jean, el mosquito que no significa nada, la mosquitera que no falla,
las dos palabras finales y las tijeras que no se usan. **Las siete están ahora en `M1`–`M7` y son
permanentes.**

**Obligatorias antes de cerrar W10, ninguna bloquea el merge:**
`A7-it3-M1`…`M8` al perímetro (`b7-perimetro.md`, sección propia para `cap-w1`; **no la he escrito:
es el vinculante y no lo toco sin que A0 lo pida**); la corrección de `S6` en la adenda II; y que
A0 verifique sobre qué texto se hizo su verificación, dadas las dos discrepancias del §2.

**Y siguen vivas de las consultas previas:** `A7-it3-C5`, `C6` (reformulada), `C8` (los cuatro
`desc`), `C9` (los cuatro nombres de `cap-08` a R2).

---

**Firmado, A7 · gate de merge · `w10-it3` · 2026-08-20.**

*Pedí una escena que no supiera nada y me han dado una en la que dos mujeres discuten cuatro veces
sobre por dónde se empieza a meter una goma, y en la que lo único que queda al final es un mosquito
que ya estaba dentro y una malla que aguanta. No explica el matrimonio, no lo juzga y no lo mide:
lo deja pasar por delante mientras alguien trabaja. Es lo que pedían los cinco lectores y es lo que
la Carta permite, y no es frecuente que coincidan.*
