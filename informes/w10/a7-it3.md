# A7 · Dictamen previo · W10 · iteración 3

**Dos consultas de perímetro. Nada escrito, nada ejecutado.** Esto no es un dictamen de merge:
es la respuesta escrita que exige mi propia **regla de sucesión** (`b7-perimetro.md §6`) antes de
que nadie redacte una línea. Vale para la página que se escriba, no para la que se imagine.

**Leído para esto:** `cap-03`, `cap-04`, `cap-06`, `cap-10`, `cap-13`, `cap-14` (íntegro y con
números), `cap-17`, `cap-27`, `cap-39`, `cap-43`; `b7-perimetro.md`, `b7-carta-sensibilidad.md`,
`b1-cronologia.md`, `b4-ledger-chekhov.md`, `b5-lista-protegida.md`, `plan-w10 §2/§3/§5`,
`protegidos/spans.json`, `protegidos/hashes.json`. Barridos de término hechos y citados abajo.

---

# CONSULTA 1 · La escena del matrimonio

## 1.0 · Antes de responder: hay que corregir la premisa

A0 plantea el problema así: «la separación es reciente: `cap-04`, 26 de noviembre, "ropa para una
baja de un mes"», y de ahí deduce que cualquier escena del matrimonio en presente es candidata a
ser situable. **La premisa es falsa, y su falsedad cambia el dictamen entero.**

«Ropa para una baja de un mes» no data la separación: data **la baja laboral**, concedida por
Alana unas horas antes, esa misma mañana.

| dónde | cita literal | qué fija |
|---|---|---|
| `cap-03:279` | «—**Un mes, de entrada** —dijo Alana—. Sin correo ni acceso remoto. […] Tú recoges lo necesario y te vas a casa.» | la baja, 26-nov 11:15 |
| `cap-04:25` | «Había venido a recoger ropa para **una baja de un mes**.» | la bolsa de esa baja, 26-nov 14:00 |

La separación está fechada tres veces, y las tres dicen **2059**:

| dónde | cita literal |
|---|---|
| `cap-27:71` | «**En 2059, Jean llenó el coche dos veces.** Se llevó el hervidor, la radio de la cocina, cuatro platos, la mitad de los cubiertos y la taza que no tenía grieta.» |
| `cap-06:155` | «La solicitud conjunta de divorcio que habían presentado en **2059** seguía sin resolver ante el Estado. **Llevaba meses** contando aquella demora entre los gastos.» |
| `cap-39:79` | «**En 2059**, el mismo ruido recibió un aviso remoto con un número de parte. Prometió volver antes de acostarlas. […] Las tres habían esperado.» |

`b1-cronologia.md §3` lo registra igual. Y `cap-17` «El salero» —Jean todavía en casa— lleva
`fecha: 2059-03-04` en el frontmatter.

**Consecuencia:** entre la separación y la muerte hay **entre catorce y veinte meses**. La
«textura actual de su separación» que pide A6-3 fue la textura durante más de un año. Mi `§6`
punto 4 prohíbe **las semanas anteriores al 26 de noviembre**, no el matrimonio. El problema que
A0 temía —que no exista sitio fuera de la elipsis— no existe: hay un año entero de sitio, y el
libro lo tiene vacío a propósito.

---

## 1.1 · Respuesta 1 — Sí, puede existir. Y pasa mi propia prueba, pero solo en una forma

`§6` obliga a contestar tres preguntas por escrito. Las contesto yo, aquí, y no salen del trámite:

**Pregunta 1 · ¿Qué punto de la Carta mejora esta página?** Ésta es la que A0 debería temer, no
la datación: mi regla dice que «responde a la nota de un crítico» **es un no**. Y sin embargo
esta página pasa, por una razón que no es la del crítico:

> **Un matrimonio que solo existe como formulario es un matrimonio que se lee como causa.**

Hoy el matrimonio del libro son cuatro objetos: una casilla marcada (`cap-06:151-155`), un
reparto de enseres en lista (`cap-27:71`), «tu exmujer» (`cap-23`) y media línea en el clímax
(`cap-43:115`, «volvió a ver a Jean ante el piano de casa»). Un hueco de ese tamaño no produce
pluralidad: produce **el relleno más disponible**, que es el matrimonio roto como explicación.
R3 no se defiende dejando vacío el sitio donde el lector quiere una causa; se defiende
**ocupándolo con algo que no sirva de causa**. Eso es Carta 3, no ritmo.

Segundo punto de Carta que mejora: **Carta 4**. Una muerta de la que solo sabemos que se estaba
divorciando es una muerta fácil de romantizar —que es exactamente el trabajo que hace Henrik Dahl
en el libro y que el libro marca como falso—. Nada resiste la romantización como una mujer
discutiendo por un metrónomo.

**Y aquí está el límite, que es el dictamen entero en una frase:**

> **La escena está permitida en la medida exacta en que no trate del matrimonio.**

Una escena *sobre* el matrimonio —la conversación honesta, el casi-reencuentro, el balance— no
mejora ningún punto de la Carta: **alimenta el que dice proteger**. Esa versión falla la pregunta 1
y la deniego por adelantado.

**Pregunta 2 · ¿Puede un lector situarla?** Contestada en §1.2 con condiciones verificables.
**Pregunta 3 · ¿Quién lo dice, y le cree el narrador?** Contestada en §1.3: la respuesta correcta
es que **no lo dice nadie**, y por eso el modo importa más que la fecha.

**Una honestidad que debo por escrito.** El motivo de que el matrimonio sea hoy una lista es
**mío**. Es la condición **C-4.6**, emitida en W3 y todavía vinculante en `b1-cronologia.md:138`:
«El reparto de objetos de 2059 (qué se llevó Jean / qué dejó) se registra en N3 como **lista**,
sin una línea de interpretación conyugal». La escribí para impedir que la marcha de 2059 se
leyera como causa, y para eso sigue vigente y no la levanto. **Lo que nunca dijo esa condición es
que el matrimonio tuviera que estar ausente en todas partes.** Cinco lectores independientes han
detectado el efecto colateral de una regla mía. Corresponde decirlo antes que discutirlo.

---

## 1.2 · Respuesta 2 — La propiedad (del sitio y de la escena)

A0 pide propiedades, no números de capítulo, «como aprendimos cuando `cap-39` resultó ser el
naust». De acuerdo. Todas las de abajo son verificables con `grep` sin volver a preguntarme.

### Del sitio — seis condiciones

- **S1 · No adyacencia.** En `orden_lectura`, la escena no puede quedar inmediatamente antes ni
  después de: `cap-04` (la primera habitación del trayecto), `cap-10` («Despedida»), `cap-23` y
  `cap-34` (el trayecto), `cap-39`, `cap-41`, `cap-45`, `cap-46`, `cap-47`, `cap-48` (las vueltas
  al naust y el después). *R1: ningún lugar de memoria familiar se pone junto al lugar de la
  muerte — y la adyacencia de lectura es una forma de ponerlo junto.*
- **S2 · Fuera de la cuenta atrás.** Nada de Parte IV. Una analepsis sin fecha metida en un
  presente que acelera se lee por contraste como «la última vez». *§6 punto 4.*
- **S3 · Después de `cap-06`.** El lector tiene que saber ya que el matrimonio terminó y **cómo**
  (la casilla, la solicitud de 2059). Antes de eso, la escena informa; después, desactiva.
- **S4 · La fecha vive en el frontmatter y en ningún otro sitio.** Verificado: `compilar.sh`
  elimina el frontmatter, de modo que el lector de `cap-17` nunca ve `2059-03-04`. Ese es el
  mecanismo, y funciona. **Si la escena necesita una fecha en la prosa para funcionar, no
  funciona.**
- **S5 · Fuera del mørketid. La luz es la coartada.** El presente del libro es 24-nov → 21-ene,
  más 3-feb, 11-may y 21-ene-2062: oscuridad. Una escena con noche a mediodía, nieve, caldera,
  navidad o guirnalda **se alinea sola** con la temporada de la muerte, sin decir una fecha. Una
  escena con luz —tarde larga, ventana abierta, barcas en el agua, casa sin calefacción— no se
  alinea con nada de lo que el lector tiene. *Ésta es la condición más barata y la que más rinde
  de todas: el clima data mejor que un calendario.*
- **S6 · No ordenable respecto de `cap-17`.** Dos escenas sin fecha que el lector pueda **ordenar**
  entre sí dejan de ser dos escenas y se vuelven una trayectoria; y una trayectoria con final
  conocido es un declive, y un declive es una causa. Operativamente: **ningún objeto ni ritual de
  `cap-17` puede reaparecer en un estado posterior** (el salero, el metrónomo de nogal, la taza
  reparada, el táper SOPA, la cuchara de servir, el paragüero, el felpudo).

### De la escena — quince condiciones

- **E1 · Trata de una tercera cosa.** La fórmula ya es mía, y está escrita en
  `b7-carta-sensibilidad.md:123` a propósito de `cap-39:79`: **«deterioro conyugal por objeto, sin
  explicar nada»**. Un trámite, una avería, una entrega, un reparto, una tarea. El matrimonio se ve
  en la gramática de quién hace qué, nunca en el asunto de la escena.
- **E2 · El POV no sabe.** Escena sin marco, sin recordante. Ver §1.3: es la condición que sostiene
  R3 y no es negociable.
- **E3 · Cero síntoma.** Jean no está cansada, ausente, rara, callada, «no era ella». Nadie la
  mira dos veces. **Y en particular: prohibido «estoy bien».** R5 prohíbe el checklist de «señales
  que no visteis»; un síntoma dramatizado es ese checklist con mejor prosa.
- **E4 · Cero marcador de última vez.** Ni umbral, ni despedida en la puerta, ni Maja mirándola
  irse, ni coche que arranca y se aleja. *`cap-17` ya gastó el cierre en el umbral, y lo gastó
  con Alana. No se repite con Jean.*
- **E5 · La prueba de la relectura.** Léase la escena de la última frase a la primera sabiendo el
  final. **Toda oración que gane sentido con ese saber, se borra.** Ése es el único test que
  atrapa a la vez la anticipación, el presagio y la elegía.
- **E6 · Cero objetos de `cap-04`.** Las cadenas `cap-04`↔`cap-27` están **completas** (táper SOPA,
  taza reparada, caldera, horario escolar, lápiz de la goma mordida, jersey, bolsa). Un tercer
  eslabón convierte el paseo de Jean por esa cocina en un inventario de última vez. Cerradas por
  cuenta y verificadas hoy: **bolsa de viaje = 2** (`cap-04:25`, `cap-27:121`), **cinturón = 4**
  (`cap-04:27`, `cap-10:199`, `cap-28:313`, `cap-46:127`), **«a la altura de los ojos» = 2**
  (`cap-04:43`, `cap-15:19`). Ninguna sube.
- **E7 · Cero origen de `FLOR`, `CANELA`, `CARIES`, `NO`. Esto es VETO, no condición.** Una cocina
  con Jean y una niña al piano es exactamente el sitio donde un escritor regala la escena en que
  nace `CARIES`. Dramatizarla **establece la exclusividad por escena** y retira a Alana de la
  ambigüedad. El techo del libro es la formulación indirecta de `cap-16:177` —«CARIES era una
  palabra de aquella casa. La había dicho una niña de cuatro años delante del teclado»— dicha
  **desde el presente y por Maja**, con Alana delante sin necesitar leerla. *R7 punto 16.*
- **E8 · Cero Kongsbakken, cero prueba de acceso, cero instituto de Nora.** `§8c` y R7 punto 2.
  `cap-03:143` ya establece la plaza en boca de Jean viva, y está en fichero `total`.
- **E9 · Cero noveno cumpleaños, cero segundo regalo, cero hueco del metrónomo.** *R7 punto 6.*
- **E10 · Cero cinturón y cero «qué sabe Jean del cinturón».** *R7 punto 13; C2 cerrada.*
- **E11 · El lugar.** La casa es admisible. **No lo son** el naust, Koppangen, la barca, el ferry,
  Svensby, la playa de Telegrafbukta ni la playa del jardín. *R1.*
- **E12 · Nadie habla del porqué del divorcio, ni en negativo.** Ni «deberíamos», ni «si
  hubiéramos», ni un casi-reencuentro. Un casi-reencuentro convierte la muerte en la respuesta a
  una reconciliación fallida. *R3, R4.*
- **E13 · La escena no fija cuándo se vieron por última vez.** Verificado: el libro **no lo dice
  en ninguna parte**, y ese hueco se queda abierto. Ninguna frase puede permitir contarlo hacia
  adelante ni hacia atrás.
- **E14 · Nadie enuncia una rima.** *R4, último punto: enunciar un eco lo convierte en ecuación.*
- **E15 · Si están las gemelas, están a lo suyo.** No son público, ni coro, ni símbolo. El modelo
  exacto está dentro del libro: `cap-27:137-149`.

---

## 1.3 · Respuesta 3 — Ni presente ni recuerdo. A6-3 tiene razón y no hay que contradecirlo

A0 me pide que, si un recuerdo sin fecha da el noventa por ciento con el diez por ciento del
riesgo, contradiga al crítico. **No hace falta, porque «en presente» no significa lo que A0 teme,
y porque el recuerdo es la variante *más* peligrosa de las dos, no la más segura.**

**«En presente» es un modo de representación, no una posición en el calendario.** Lo que A6-3
reprocha es que el matrimonio llegue como resumen y como documento: «En 2059, Jean llenó el coche
dos veces…» es narración sumaria dentro de la cabeza de Maja; la casilla de `cap-06` es un
impreso. Lo que pide es escena dramatizada. Y el libro ya sabe hacer eso sin acercarse a
noviembre:

> `cap-17` empieza **«Alana venía a cenar cada dos o tres meses y siempre llegaba tarde. / Una de
> esas noches entró con el pelo mojado.»** — iterativo → singulativo. Sin recordante, sin marco,
> sin «Maja recordó». Es una analepsis de 2059 y **nueve lecturas frías no la han llamado
> recuerdo**, porque no está enmarcada como tal.

**Y el argumento que hace de esto una cuestión de sensibilidad y no de oficio:**

> **Un recuerdo enmarcado instala un sabedor. Una escena sin marco no instala a nadie.**

Una viuda que recuerda a su mujer muerta es una voz **seleccionando**, y la selección de una viuda
es un enunciado causal se formule como se formule: lo que ella elige recordar es lo que el libro
dice que importaba. Una escena sin marco pone al personaje en un momento en que **no sabe el
final** y por tanto no puede valorar. **R3 se protege por la ausencia de sabedor.** El «recuerdo
sin fecha» que yo mismo cité en `§7` punto 6 como inofensivo lo es solo si no está enmarcado como
recuerdo.

**Y hay una tercera razón, que es la mejor: el libro ya marcó el hueco y lo marcó como propio.**

| dónde | cita literal |
|---|---|
| `cap-05:59` (fichero `total`, Jean) | «Busca una escena y encuentra el banco del piano. Nora mantiene una nota hasta que empieza a temblar. Jessie espera debajo y se ríe antes del final. **Maja dice algo desde la cocina. Jean no recupera las palabras**…» |
| `cap-27:137-149` (Maja) | «Una tarde, Nora sostuvo una nota hasta que empezó a temblar. […] Jean contaba con dos dedos sobre la madera y no llevaba zapatos. […] **—Cinco minutos y a la mesa.** […] Maja cerró el grifo para oír el final.» |

La misma escena desde los dos lados. Jean **no recupera lo que dijo Maja**; doscientas palabras
de `cap-27` se lo dan al lector y no a ella. Ése es el dispositivo del matrimonio en este libro,
ya usado dos veces, ya aprobado por mí: **el matrimonio entra exactamente donde falla la memoria
de Jean y aguanta la de Maja.** Sin fecha, sin marco, sin estación, sin institución: solo Nora
tocando, Jessie debajo del piano, Jean descalza contando y Maja en el fregadero.

**Mi respuesta operativa:** ni «presente» ni «recuerdo». **Escena sin marco, POV de Maja, fecha
solo en el frontmatter.** Da el 100 % de lo que pide A6-3 —no el 90 %— y es la variante de menor
riesgo de las tres. La forma está probada dentro del libro, a escala de párrafo. Lo que piden los
cinco lectores es esa misma forma **a escala de escena y con los dos cónyuges dentro**.

---

## 1.4 · Respuesta 4 — Lo que un buen escritor haría aquí por instinto, y aquí está prohibido

A0 pregunta bien. Ésta es la parte del dictamen que más falta hace, porque **todo lo que sigue es
buen oficio en cualquier otro libro**.

1. **Presagiar.** Darle a Jean una línea que aterrice distinto en la relectura. Es el instinto
   número uno y es una máquina de fabricar causa. *(E5.)*
2. **Hacer que sea la última vez que se vieron.** El instinto de que una escena así «tiene que
   pesar». Es literalmente `§6` punto 4. *(E4, E13.)*
3. **Escribir el dúo sobre el matrimonio:** la conversación pendiente, el «tenemos que hablar»,
   el casi-reencuentro. Es la escena que cualquier editor pediría. Aquí convierte la muerte en el
   desenlace de una reconciliación fallida. *(§1.1, E12.)*
4. **Regalarle a Maja un instante de no ver.** Un detalle que ella deja pasar. Es el gancho
   emocional más eficaz que existe y es **culpabilización** con guantes. *(R5.)*
5. **«Estoy bien.»** La frase más legible del idioma en boca de alguien que va a morir. *(E3.)*
6. **Anclarla.** «Aquel septiembre», «tres semanas antes de». El instinto de orientar al lector.
   *(S4, S5.)*
7. **Cerrar con Jean saliendo por la puerta, y Maja mirándola irse.** Es el cierre natural de la
   escena y es una despedida. *(E4.)*
8. **Regalar el origen de una palabra privada** —dónde nació `CARIES`, de dónde salió el salero—.
   Es el gesto más generoso del oficio y aquí es **VETO**. *(E7, E9.)*
9. **Dar interioridad a Jean.** Un párrafo de lo que ella siente estando allí. Explicarla es
   empezar a explicarla. *(Doctrina W9-20, aplicada a Jean con más razón que a Dahl.)*

**El test que los atrapa a los nueve es el mismo:** léase la escena al revés sabiendo el final.
Si una frase mejora, se borra.

---

## 1.5 · Condiciones formales antes de que se escriba una línea

- **A7-it3-C1.** La OT contesta por escrito las tres preguntas de `§6` **antes** de redactar,
  citando estas condiciones por su código (S1–S6, E1–E15).
- **A7-it3-C2.** El borrador vuelve a A7 en **dos pasadas** (contenido y tono), como en N1 y N3.
  Este dictamen autoriza a escribir; **no autoriza a fundir**.
- **A7-it3-C3.** La escena se mide contra el techo de `cap-17` y de `cap-27:137-149`, no contra el
  encargo del crítico. Si al terminar hace falta explicar al lector qué era el matrimonio, está
  mal escrita.
- **A7-it3-C4.** Si la escena se escribe, **`cap-05:59` no se toca** («Jean no recupera las
  palabras»): es la marca del hueco y la razón de que el dispositivo funcione. Fichero `total`.

---

## 1.6 · La otra mitad del backlog: Kongsbakken. Cerrado, y por escrito

A0 pide que quede en la biblia para que no se reintente cada oleada. **Ya está**: `b7-perimetro.md
§8c`, «Kongsbakken se queda siendo un sitio con mostrador, horario e impreso. **Glosar la llegada
sería VETO**». Se reincorporó el 19-ago precisamente porque se había perdido una vez.

Añado la cláusula que falta —la que impide que se vuelva a pedir— redactada para pegar en `§8c`.
**No la he escrito: la consulta era previa y no toco el documento vinculante sin que A0 lo pida.**

> **Estado de la petición.** Dos lecturas frías de W10 (A6-1, A6-2 · it2) piden glosar la llegada
> a Kongsbakken. **Denegada en el gate y no discutida en el mérito**, con el mismo régimen que «una
> resolución real del archivo» (§7, último párrafo): ninguna nota de ningún crítico levanta una
> promesa hecha al lector. La petición volverá —es la que produce sola el hueco que el libro deja—
> y la respuesta es ésta, cada vez, sin nueva deliberación.

---

# CONSULTA 2 · Excisión de `cap-14:255-321` (−535 palabras)

**Comprobado antes de opinar:** el bloque son 535 palabras exactas; `cap-14` pasa de **2.036 a
1.501** (A2 dijo 2.038 → 1.503: distinto tokenizador, misma cuenta). `cap-14` tiene **dos** spans
protegidos, `S12-temblor` (:159) y `S12-nidhogg` (:325), **ambos fuera del bloque**. Residuo léxico
verificado: tras el corte no queda en el libro ninguna mención de *indio · restaurante · comino ·
cardamomo · repartidor* asociada a la fuga; `Storgata` sobrevive en `:39` y `:77`; la parka oscura
queda en `:219` («se detuvo un hombre con una parka oscura») y `:249` («El hombre ya no estaba
frente a la tienda»), que es un cierre limpio. Barrido de vocabulario de riesgo sobre el bloque:
**cero coincidencias** (los dos aciertos de «reflejo» son escaparates, no R1).

## 2.1 · Punto 1 — El vecino textual de `S12-nidhogg` (regla 3 de `plan-w10 §5`)

**No hay cuestión de perímetro. APROBADO.**

`S12-nidhogg` es el cierre de una siembra (CH-22), no un locus de Carta. El span queda intacto y
**su párrafo de entrada también**: `cap-14:323` («El terminal de Nora vibró. Acababa de recibir un
archivo de texto que Gunnar Rydberg había dejado programado») está fuera del corte. Lo único que
cambia es lo que precede a ese párrafo: en vez de la calle desinflada, un dinkus.

Que la regla 3 dispare mi dictamen es correcto —la escribí después del error de P-56 y me alegro
de que A2 la haya aplicado sobre sí mismo—, pero **disparar el dictamen no es lo mismo que
producir una objeción**. La emisión gana énfasis; el énfasis recae sobre el miedo de un hombre y
sobre su disparador póstumo, y ninguno de los dos es materia de Carta.

## 2.2 · Corrección factual · **esto no es un hallazgo de sensibilidad, y A0 lo necesita igual**

A2 escribe que las anclas que ganan peso son `S12-temblor` y `S12-nidhogg`. Aritméticamente sí.
Textualmente, `S12-temblor` **pierde su único pago**:

| dónde | cita literal | estado |
|---|---|---|
| `cap-14:159` | «Gunnar dejó la taza donde estaba y escondió la mano debajo de la mesa. **Nora tardó un instante en entender que le temblaban los dedos.**» | span `S12-temblor`, sobrevive |
| `cap-14:317` | «—Y tú no le crees. / **—Le temblaban los dedos. La tarjeta se queda envuelta.**» | **dentro del corte** |

`b5-lista-protegida.md:158` registra `S12-temblor` como «el dato central» del capítulo. La línea
317 es **el único lugar del libro** donde ese dato se convierte en una decisión de personaje
—verificado: `tembl*` aparece siete veces en todo el manuscrito y las otras cinco son ajenas—. El
corte deja el ancla y se lleva su consecuencia.

**Y anoto el modo de fallo, porque es el duodécimo de la serie:** un `grep` de residuo devuelve
aquí **una coincidencia, no un huérfano**. La palabra sigue en el libro; lo que desaparece es la
recogida. Ninguna herramienta de este proyecto lo habría visto. *(Gravedad: **corregir** — no en
mi registro, en el de A0: es un dato que cambia el balance de la resta, no una condición de Carta.
Si A0 quiere el corte y quiere conservar el pago, la resta mínima es reubicar las dos réplicas de
`:311-317` antes del dinkus; pero eso ya no es excisión pura y deja de tener el argumento que la
sostiene.)*

## 2.3 · Punto 2 — La rima `cap-03:313` ↔ el indio de `cap-14`

A0 pregunta al revés: ¿es mejor que la rima exista sin enunciarse, o que la siembra quede sin
recoger? **Mi respuesta tiene tres partes y ninguna sostiene el corte; solo lo desbloquea.**

**(a) No es una siembra.** `cap-03:313` —«—Para cenar. **El indio de Storgata.** Dijiste que
querías probar el cordero nuevo»— es una cena a las siete y media del 26 de noviembre que **no
llega a ocurrir**. `b1-cronologia.md §3` data el cordero en septiembre de 2060 y la cena en
`cap-03:309-323`. Su función es ser el futuro ordinario que se interrumpe, **y esa función se
completa dentro de `cap-03`, por elipsis**. Su recogida es que no hay recogida. Once capítulos
después, unas hijas cruzan un local del mismo ramo: eso es coincidencia de decorado, y el libro
nunca la reclama.

**(b) Por tanto el corte no deja huérfano nada.** El ledger no registra CH para esta pareja, y
ningún lector de las 48 lecturas frías la ha nombrado. Una rima que en 48 lecturas no produce
nada al lector no está produciendo nada al lector.

**(c) Y desde el perímetro, mientras las dos existan, la rima es un riesgo latente, no un valor.**
Está disponible para que alguien la **enuncie**: una línea de retorno, un «el mismo sitio donde»,
un reconocimiento de Nora, una nota de traductor, una faja. R4: «Enunciar un eco lo convierte en
ecuación». Y esta ecuación en concreto **mete los cuerpos de las gemelas dentro del itinerario del
26 de noviembre**, que es la mitad no realizada de ese día. Es un eco que solo puede dispararse en
la dirección mala.

**(d) Y la advertencia que me corresponde a mí más que a nadie:** *esto no es una razón para
cortar; es una razón para no preocuparse por cortar.* No presto la Carta a una decisión
estructural. Si A0 conserva la fuga, el capítulo no incumple nada.

**Condición permanente, valga lo que valga la decisión (A7-it3-C5):** ninguna voz, en ningún
soporte —capítulo, sinopsis, ficha, orden de trabajo, paratexto—, conecta jamás el restaurante de
`cap-03` con el restaurante de `cap-14`. **Y si la fuga se corta, el restaurante no se replanta en
otro sitio «para compensar».** El reflejo de compensar una supresión es el que produjo la mitad de
los problemas de este proyecto.

## 2.4 · Lo que se pierde y no sale en ningún grep

| `cap-14:321` | «Un portal se abrió frente a la parada. Salió un hombre de unos cuarenta años, con una parka oscura y el cuello gris levantado. […] **Su cara no mostró reconocimiento al pasar junto a las gemelas.**» |
|---|---|

Es una de las pocas veces en que el libro monta una sospecha **y se niega a confirmarla**. Esa es
exactamente la gramática de la que depende R3, y su forma canónica está registrada en el
perímetro: «Y mamá tenía enemigos» (`cap-29:215`) — «La sospecha de personaje sí vive. El narrador
no la refrenda ni deriva causa de ella. **Esa es la forma correcta.**»

Cortarla no rompe R3: gasta una instancia. Y hay un efecto de segundo orden que dejo en
**vigilar**, no en corregir: sin el desinfle, la secuencia queda «hombre que tiembla → aviso
póstumo», que se lee **un punto más confirmatoria**. Eso no nombra a ningún ordenante y no toca
R7 punto 5; es sustrato, no proposición. Pero es exactamente el sustrato del que vive esa
ambigüedad.

**Condición (A7-it3-C6):** si el corte se ejecuta, **queda anotada la pérdida**, y **ninguna resta
posterior puede eliminar otra sospecha-no-confirmada sin dictamen nuevo**. Es lo que en `§4` llamo
una cuenta cerrada: aquí el número es la salvaguarda.

Y añado por escrito, porque es mi encargo de tono: el pasaje que se corta es prosa de v0. Mi
referencia de contención son `cap-04`, `cap-10`, `cap-28` y `cap-46` (v0 4, 9, 23, 40). **`:321`
es contención de v0**: confía en el lector y no le dice si tuvieron razón. Suprimir contención de
v0 para ganar ritmo es la inversión exacta de la referencia que se me encarga defender. No lo veto
—no es Carta—, pero que conste con esas palabras.

## 2.5 · R6 · Las menores: el corte es neutro, y si acaso favorable

Lo que se va incluye una evasión **eficaz y sin coste** ejecutada por una menor de dieciséis años:
la mentira al camarero («—Estamos buscando a nuestro padre»), la salida lateral aprovechando la
puerta que sujeta un repartidor, la parada de autobús elegida por líneas de visión y el autobús
descartado «porque, una vez en marcha, solo ofrecía una salida». Ninguna de esas cosas es riesgo
para sí, y por eso no era objeción; pero es competencia sin precio, y su desinfle también se va.

**El mecanismo de coste del capítulo sobrevive intacto**, que es lo que importa: `cap-14:59`
—«Tienes dieciséis años y has quedado con un adulto anónimo. **Vas conmigo o no vas.**»— queda
fuera del corte, y es la línea registrada en `b7-carta-sensibilidad.md:130` como el cumplimiento
de P7 en este capítulo. **Sin objeción.**

---

# TABLA DE HALLAZGOS

| # | Locus | Cita literal | Punto | Gravedad | Propuesta mínima |
|---|---|---|---|---|---|
| 1 | consulta 1, premisa | «ropa para una baja de un mes» leída como fecha de la separación | §6.4 | **corregir** (de A0) | La separación es de 2059 (`cap-27:71`, `cap-06:155`, `cap-39:79`). Rehacer el razonamiento de riesgo sobre catorce–veinte meses de ventana, no sobre semanas. |
| 2 | consulta 1, forma | escena *sobre* el matrimonio | Carta 3 · R3 | **VETO anticipado** | La escena trata de una tercera cosa (E1) o no se escribe. |
| 3 | consulta 1, forma | recuerdo enmarcado («Maja recordó…») | Carta 3 · R3 | **corregir** | Escena sin marco, POV que no sabe (E2). Un recuerdo instala un sabedor y la selección de un sabedor es un enunciado causal. |
| 4 | consulta 1, contenido | origen dramatizado de `FLOR`/`CANELA`/`CARIES`/`NO` | R7·16 | **VETO** | Techo actual: `cap-16:177`, indirecto y con Alana dentro. No baja de ahí (E7). |
| 5 | consulta 1, contenido | Kongsbakken, prueba de acceso, instituto de Nora | §8c · R7·2 | **VETO** | E8. |
| 6 | consulta 1, contenido | cinturón · bolsa · «a la altura de los ojos» | C2 · C3 · C4 | **VETO** | Cuentas cerradas verificadas hoy (4 · 2 · 2). Ninguna sube (E6, E10). |
| 7 | consulta 1, datación | estación, luz, caldera, nieve, navidad | §6.2 · R1 | **corregir** | S5: fuera del mørketid. El clima data mejor que un calendario. |
| 8 | consulta 1, colocación | adyacencia con `cap-04`, `cap-10`, trayecto y naust | R1 | **corregir** | S1, S2. |
| 9 | consulta 1, oficio | presagio · última vez · «estoy bien» · umbral · interioridad de Jean | Carta 4 · R5 | **corregir** | E3, E4, E5; test de relectura invertida (§1.4). |
| 10 | `cap-05:59` | «Maja dice algo desde la cocina. Jean no recupera las palabras» | R2 · R3 | **vigilar** | No se toca. Es la marca del hueco que la escena nueva ocuparía desde el otro lado (A7-it3-C4). |
| 11 | `cap-14:255-321` | la fuga por el restaurante indio | — | **sin objeción** | Ningún punto de la Carta afectado. Spans intactos y fuera del bloque. |
| 12 | `cap-14:317` | «—Le temblaban los dedos. La tarjeta se queda envuelta.» | — (oficio) | **corregir** (de A0) | Es el único pago de `S12-temblor` en el libro y está dentro del corte. Dato para decidir, no condición mía. |
| 13 | `cap-14:321` | «Su cara no mostró reconocimiento al pasar junto a las gemelas.» | R3 (forma) | **vigilar** | A7-it3-C6: anotar la pérdida; ninguna resta posterior elimina otra sospecha-no-confirmada sin dictamen nuevo. |
| 14 | `cap-03:313` ↔ `cap-14:279` | «El indio de Storgata» / «Eligió el restaurante indio de la esquina» | R4 | **vigilar** | A7-it3-C5: nadie enuncia jamás el parentesco; y si se corta, no se replanta en otro sitio. |
| 15 | `cap-14` tras el corte | secuencia «hombre que tiembla → aviso póstumo» sin desinfle | R7·5 | **vigilar** | Sustrato, no proposición. Sin corrección; anotar. |

---

# VEREDICTO

**Consulta 1 · `APROBADO CON CORRECCIONES`.**
La escena del matrimonio **puede existir**, y la razón por la que puede no es que los críticos la
pidan: es que un matrimonio que solo existe como formulario se lee como causa, y eso es lo que R3
prohíbe. **No hay techo declarado aquí.** Lo que hay es una forma única admisible: escena sin
marco, POV de Maja, fecha solo en el frontmatter, fuera del mørketid, sobre una tercera cosa, con
un personaje que no sabe el final. Obligatorias antes del merge: **S1–S6, E1–E15, A7-it3-C1…C4**,
y los cuatro VETO anticipados de la tabla (filas 2, 4, 5, 6). El borrador vuelve a A7 en dos
pasadas. Este dictamen autoriza a escribir; no autoriza a fundir.

**Consulta 2 · `APROBADO`.**
La excisión `cap-14:255-321` **no toca la Carta ni el perímetro**, deja los dos spans intactos y
fuera del bloque, no orfana `cap-03:313` —esa línea la paga la elipsis, no la fuga— y es
marginalmente favorable a R6. Condiciones permanentes, no bloqueantes del corte: **A7-it3-C5** (la
rima no se enuncia nunca; y si se corta, no se replanta) y **A7-it3-C6** (queda anotada la pérdida
de la sospecha no confirmada de `:321`; ninguna resta posterior elimina otra sin dictamen nuevo).

**Y una advertencia que no es veredicto:** la fila 12 de la tabla no es mía y por eso no la
convierto en condición. Pero si A0 ejecuta el corte creyendo que `S12-temblor` gana peso, ejecuta
otra cosa distinta de la que ha decidido.

---

**Firmado, A7 · dictamen previo, sin texto redactado · W10 · iteración 3.**

*El libro elige no saber. Cinco lectores piden ver el matrimonio y tienen razón, y la única forma
de dárselo sin romper eso es dárselo **sin que nadie dentro de la escena sepa nada**. Si un día
hay que elegir entre una escena que conmueva y una que no sepa, quédese con la que no sabe.*

---
---

# ADENDA · 2026-08-20 · Los seis `desc` restaurados

**A0 interrumpe la consulta con el `desc` restaurado de `S-n3-hervidor` y propone cerrar la
consulta 1 como techo declarado, con mi propio argumento de W5 detrás.** He leído el texto
restaurado, he leído `informes/a7-w5d-n4.md:200-245` entero y he verificado la aritmética de A2.

**Mi respuesta: no lo cierro, y explico exactamente por qué — porque si lo cerrara, el cierre
sería falso y llevaría mi firma.**

Pero **sí cierro la mitad que A0 tenía delante**, la aritmética de A2 es correcta y la restauración
**añade una condición dura que no estaba en mi dictamen de esta mañana**. Los tres puntos, por
orden.

---

## A.1 · Lo que dice el texto restaurado, y lo que no dice

Restaurado verbatim (`S-n3-hervidor`, verificado contra `informes/a7-w5d-n4.md`):

> **Carta 3 · la separación contada por objetos.** «En 2059, Jean llenó el coche dos veces… Jean
> preguntó desde la puerta si podía llevarse el hervidor. Maja dijo que había otro en el altillo.»
> / «**No lo había.**» Dos líneas que no explican nada y que, **con una frase delante o detrás**,
> se convertirían en juicio sobre el matrimonio —que es la explicación única que la Carta 3
> prohíbe. El desmentido de dos palabras no puede quedarse solo ni ganar glosa.

**El sujeto de esa condición son dos líneas de `cap-27`, y su prohibición es de adyacencia.** El
span `S-n3-hervidor` tiene **tampones a los dos lados** —arranca en «Maja llevó el cuenco y la
radio…» y termina en «El teléfono sonó con el papel de periódico…»— por esa razón y solo por esa:
lo que impide es que entre algo **pegado**. Es la misma arquitectura, literalmente el span vecino,
que `S-n3-bolsa`. Ninguno de los dos es una prohibición de existencia; los dos son cerraduras de
adyacencia.

**«Una frase delante o detrás» significa delante o detrás de esas dos líneas.** Una escena situada
en otro punto del libro no está delante ni detrás de nada de `cap-27`.

**Y hay tres pruebas independientes de que W5-yo no denegó la escena, sino su colocación:**

1. **Misma oleada, misma mano, misma semana: `cap-17` «El salero» existe.** Es una escena de Jean
   viva, con Maja dentro, sin fecha en la prosa, y la aprobé yo en W5. Si mi condición de W5
   hubiera denegado el matrimonio dramatizado, `cap-17` no estaría en el libro. Está, y hoy es el
   capítulo 17.
2. **Misma oleada, segundo documento: prescribo la forma, no la prohíbo.**
   `b7-carta-sensibilidad.md:123` sobre la caldera de 2059: «**Patrón** para N3: **deterioro
   conyugal por objeto, sin explicar nada**». Y `:149`, guía de N3: «**Sí:** la separación por
   logística y objeto (la caldera de 2059 […] es el patrón)». Eso es un molde, no un veto.
3. **Y yo mismo retiré por escrito la versión amplia de esta misma prohibición**, por nombre, en
   `b7-perimetro.md §7 punto 6`: «Mi razón nunca fue la existencia de la escena […] Tal como
   estaba, mi regla habría impedido, por ejemplo, un recuerdo sin fecha de Jean en 2049 que no
   rompe nada. **Eso es exactamente un perímetro que se acumula mal.**»

**Por qué me niego a firmar el cierre fácil.** A0 me ofrece cerrar con mi propia autoridad, y sería
cómodo: quedan pocas iteraciones y un «no se puede» argumentado vale más que un 8,5 sin explicar.
Pero solo si es verdad. **Un techo falso es peor que ningún techo, porque nadie lo vuelve a
levantar: lleva firma de A7 y nadie discute con A7.** Y sería la decimotercera vez que este
proyecto registra un instrumento diciendo más de lo que dice — con el instrumento siendo **yo, por
segunda vez** (la primera fue P-41, §8c, perdida y reincorporada). Mi propia regla, `§2` del
perímetro: **los números localizan; solo la cita literal instruye.** La cita literal dice
«adyacencia».

---

## A.2 · Lo que sí cierro, y queda cerrado: **el presente anterior a la muerte**

**Aquí A2 tiene razón entera y lo firmo.** Verificado con recuento propio:

| capítulo | palabras | protección |
|---|---:|---|
| `cap-01` Corona (24-nov 21:40) | 747 | **total** |
| `cap-02` La pecera (26-nov 09:00) | 1.732 | núcleo |
| `cap-03` Vacaciones muy largas (26-nov 11:15) | 2.102 | **total** |
| `cap-04` El ferry (26-nov 14:00) | 1.501 | **total** |
| **total** | **6.082** | tres de cuatro, `total` |

**Todo el presente de Jean viva son 6.082 palabras y dos días y medio.** Cualquier escena del
matrimonio *insertada ahí* es, por aritmética y sin remedio, **la última vez que se vieron** —lo
que activa `§6` punto 4 sin margen— y además caería dentro de la elipsis o pegada a ella.

> **TECHO DECLARADO (A7-it3-T1).** Una escena del matrimonio situada en el presente narrativo
> anterior a la muerte —dentro de `cap-01`…`cap-04`, entre ellos, o en el hueco de reloj entre
> `cap-03` y `cap-04`— es **VETO**, sin nueva deliberación, por `§6` punto 4 y R1. La petición de
> A6-3 leída como *cronología* está denegada y no vuelve a discutirse en el mérito.

**Y ése era el temor de A0, literalmente:** «A6-3 pide expresamente que sea "en presente"… que es
la variante más difícil». Cerrado. Lo que queda abierto es la otra lectura de la misma palabra,
que es la que sostengo desde §1.3 de este informe: **«en presente» como modo de representación
—escena dramatizada, sin marco, sin recordante— y no como posición en el calendario.** De esa
lectura el libro ya tiene dos instancias mías aprobadas: `cap-17` a escala de capítulo y
`cap-27:137-149` a escala de párrafo. Ninguna de las dos es «una frase delante o detrás» del
hervidor, y ninguna de las dos rompe nada.

---

## A.3 · Lo que la restauración **sí cambia** en mi dictamen: una condición nueva y dura

Esto no lo tenía esta mañana y lo debo a la restauración. **Es el hallazgo real de A2, y es mejor
que el que él creía tener.**

Las dos líneas del hervidor funcionan **porque no explican nada**. Un hash protege los bytes de
dentro del span; **no protege el entorno que les da sentido**. Es la lección de `plan-w10 §5.3`
—«M9 ve dentro del ancla y es ciego fuera de sus extremos»— aplicada a escala de libro y no de
párrafo: **una escena situada a treinta capítulos de distancia puede glosar esas dos líneas sin
tocar un solo byte protegido.**

Basta con que la escena nueva caracterice a Maja de un modo que convierta «No lo había» en un
ejemplo. Si el lector puede volver a `cap-27:71-73` y decir *ah, eso es lo que ella hace*, las dos
líneas han ganado glosa a distancia y el span ha sido derrotado sin que salte ninguna herramienta.

> **A7-it3-C7 (dura, nueva).** La escena nueva **no puede contener nada que explique «No lo
> había»**: ninguna negativa pequeña de Maja, ninguna retención, ningún patrón del que la mentira
> del hervidor sea instancia, y ninguna asimetría de generosidad entre las dos. **Prueba:** léase
> `cap-27:71-73` inmediatamente después de la escena nueva. Si las dos líneas se han vuelto
> comprensibles, la escena está mal. Deben seguir siendo tan opacas como hoy.

Esto se suma a S1–S6, E1–E15 y A7-it3-C1…C6. Y refuerza E1 desde el otro lado: **la escena no solo
no puede tratar del matrimonio; tampoco puede caracterizar el matrimonio.**

**Y de `S-n3-bolsa`, restaurado, extraigo la segunda condición operativa que faltaba:** su cola
recuperada dice «la bolsa **no se abre, no se describe, no gana contenido y no gana escena**», y
que `B7 §7.4` exige **autorización previa mía —no revisión—** para cualquier mención. Mi E6 hablaba
de cuentas cerradas; **«no gana escena» es más fuerte que una cuenta** y lo incorporo como tal.

---

## A.4 · La petición nueva de A0 · **Cuatro de los diez siguen amputados, y sí se pueden reconstruir**

A0 me pide que mire si alguno de los seis restaurados cambia algo dictaminado desde W5. Al hacerlo
he encontrado otra cosa, y es más urgente que la pregunta.

**Seis `desc` llevan hoy la nota «RESTAURADO». Otros cuatro llevan la nota contraria: «No se ha
podido reconstruir qué decía; se deja constancia en vez de inventarlo». Los cuatro son
reconstruibles verbatim, desde el mismo fichero del que se sacaron los otros seis.**

Verificado por comparación de literal (el prefijo superviviente de cada uno aparece íntegro en
`informes/a7-w5d-n4.md`, en la misma tabla):

| span | fichero | continuación perdida, recuperada verbatim | ¿qué se perdió? |
|---|---|---|---|
| `S-n1-casitodos` | `cap-11` | «…Es el **techo que yo mismo cité en P-66 para cualquier escena de apoyo futura. Un techo que no está hasheado es un techo que se puede subir.** (`—De acuerdo.` aparece 2× en el fichero: por eso los extremos son los tampones, que sí son únicos.)» | **Una prohibición activa.** Es el puntero de este span a **R5** («Cualquier escena de acompañamiento nueva se mide contra ese techo antes de escribirse»). Sin la cola, el span protege un texto y ya no dice que es **la vara de medir de todas las escenas de apoyo futuras**. Y la nota de los tampones explica *por qué* los extremos son los que son: sin ella, una poda futura los llamará arbitrarios. |
| `S-n2-hijadela` | `cap-20` | «…Es el **locus más frágil de los seis capítulos**.» | Una priorización mía. Es el ranking que dice por dónde se rompe antes el libro. |
| `S-n4-escena3` | `cap-32` | «…esa pregunta es **la única figura viva del capítulo: nadie puede responderla ni ejecutarla una segunda vez.** Byte-idéntico desde W3; el span solo formaliza lo que A0 ya ha prometido dos veces.» | **Una prohibición activa**, y de las duras: «—¿Y les sale la misma frase?» **no se contesta y no se repite**. Hoy no consta en ninguna parte. |
| `S-n6-persona` | `cap-47` | «…**Basta que alguien conteste —en cualquier dirección— para cerrarla.**» | **R7 punto 4**, «No toda» como techo, en su forma operativa: la simetría (*también* cerrarla en negativo). Es exactamente la distinción que R3 hace explícita para el porqué y que aquí se había perdido. |

**Dos de los cuatro son prohibiciones vivas, no comentarios.** Y las cuatro notas actuales afirman
algo falso: que no se pudo reconstruir. Estaba en el fichero de al lado.

**Y el patrón que importa más que los cuatro casos.** El proyecto tiene registrados doce
instrumentos que medían otra cosa. Éste es de una clase peor: **un instrumento que documenta su
propio fallo, y lo documenta mal.** La nota «no se ha podido reconstruir» es más dañina que el
truncamiento, porque **clausura la búsqueda**: quien la lea dentro de un año no irá a mirar. Un
`desc` cortado invita a buscar; un `desc` cortado con certificado de defunción, no.

> **A7-it3-C8 (obligatoria).** Restaurar los cuatro verbatim desde `informes/a7-w5d-n4.md`, con la
> misma nota de procedencia que los seis. Y **corregir el texto de la nota**: donde dice «no se ha
> podido reconstruir» debe decir dónde se buscó. Una constancia que no dice dónde se buscó no es
> constancia: es una puerta cerrada.

**Y una comprobación que pido antes de dar esto por cerrado:** el detector de longitud exacta 300
caza el corte **de esta vez**. Los seis y los cuatro se cortaron al escribir, no al leer. **Nada
garantiza que el próximo corte sea a 300.** La comprobación que no falla es la que ya funcionó
aquí: **cotejar cada `desc` contra el informe de A7 que lo originó**. Recomiendo que
`verificar_b7.py` añada esa comprobación —«¿existe el literal de este `desc` en algún
`informes/a7-*.md`?»— y que la de longitud quede como red secundaria.

---

## A.5 · Lo que he encontrado al revisar los seis · **un locus que el perímetro consolidado no
recoge**

`S-n5-coda` (`cap-08`), restaurado, dice:

> «**Carta 4 y Carta 2, y el sitio exacto donde este libro se puede romper.** […] Y protege la
> última línea: **cuatro nombres que no son una despedida.**»

Y su vecino `S-n5-nombres`: «La regla que impide que los cuatro nombres signifiquen otra cosa: “Al
final de cada serie repite cuatro nombres en el mismo orden. **Es lo único del turno que no
clasifica nada.**” Sin esa declaración, el final del capítulo queda disponible para leerse como
mensaje. **Carta 2.**»

**Censo hecho hoy. La figura de los cuatro nombres tiene cinco loci:**

| dónde | cita |
|---|---|
| `cap-07:33` | «Nora. Jessie. Maja. Alana.» |
| `cap-08:55` | «Al final de cada serie repite cuatro nombres en el mismo orden. Es lo único del turno que no clasifica nada.» |
| `cap-08:281` | «—Nora. Jessie. Maja. Alana.» — **última línea del capítulo** |
| `cap-30:247` | «Los cuatro nombres no tienen ruta y Jean lo comprueba de todas formas. Cuatro consultas, cuatro campos sin destinatario.» |
| `cap-30:345` | «Al terminar cada serie Jean repite cuatro nombres. **Aquí no hay serie que terminar.**» |

**`b7-perimetro.md` registra uno de los cinco**: la fila de R2 sobre `cap-30:247`/`:249` («Es
literalmente lo que Jean diría a cuatro nombres»). **El origen —la coda de `cap-08`, que W5-yo
llamó «el sitio exacto donde este libro se puede romper»— no aparece en el perímetro
consolidado.** Ni el `cap-07:33`, ni el `cap-30:345`, que es el que dice que el rito se ha
detenido y por eso es el más cargado de los cinco.

Es el modo de fallo de P-41 otra vez: la consolidación se quedó con el derivado y perdió el
original. Los spans siguen puestos y hasheados —el texto está a salvo—, pero **quien aplique el
perímetro sin leer `spans.json` no sabe que esos cuatro nombres son materia de Carta 2.**

> **A7-it3-C9.** Añadir a R2 de `b7-perimetro.md`, bajo la tabla de los cuatro huecos, una fila
> quinta: **la coda de `cap-08` y la figura de los cuatro nombres** (cinco loci, censados arriba),
> con su regla: *no ganan un quinto nombre, no ganan destinatario, no ganan contenido, la última
> línea de `cap-08` no gana texto detrás, y `cap-08:55` —«Es lo único del turno que no clasifica
> nada»— no se separa de ellos.* Redactada; **no la he escrito**: `b7-perimetro.md` es el
> documento vinculante y no lo toco en una consulta previa sin que A0 lo pida.

---

## A.6 · Una discrepancia menor que conviene fijar antes de que crezca

`S-n1-nocierra` restaurado dice de Ranveig: «**la única voz con autoridad que se pronuncia sobre el
porqué**». La cuenta **C1** del perímetro dice «Voces con autoridad que enuncian la pluralidad del
porqué: **2**, y no hay una tercera», y cita `cap-10:71` (Maja) y `cap-11:249` (Ranveig).

No se contradicen: la definición de `§1` del perímetro incluye a «la profesional de apoyo de
`cap-11`» entre las voces con autoridad y **no incluye a Maja**, que es personaje. **C1 cuenta
enunciaciones, no voces con autoridad; de éstas hay una sola.** Lo dejo fijado porque cambia el
listón para cualquier escena futura: **una enunciación nueva de la pluralidad sería la tercera y
está prohibida; una enunciación nueva en voz con autoridad sería la segunda de su clase y es
peor.** *(Gravedad: vigilar. Sin corrección de texto.)*

---

## A.7 · Tabla de hallazgos de la adenda

| # | Locus | Cita literal | Punto | Gravedad | Propuesta mínima |
|---|---|---|---|---|---|
| 16 | `S-n3-hervidor` (restaurado) | «con una frase delante o detrás, se convertirían en juicio sobre el matrimonio» | R3 · Carta 3 | **vinculante, alcance corregido** | Es adyacencia, no existencia. No cierra la consulta 1; cierra una colocación. |
| 17 | `cap-01`…`cap-04` | 6.082 palabras, tres ficheros `total`, dos días y medio | §6.4 · R1 | **VETO / techo declarado (T1)** | Ninguna escena del matrimonio en el presente anterior a la muerte. Sin nueva deliberación. |
| 18 | `cap-27:71-73` | «Maja dijo que había otro en el altillo.» / «**No lo había.**» | R3 | **condición nueva (C7)** | La escena nueva no explica esas dos líneas ni a distancia. Prueba de relectura de `cap-27` después de la escena. |
| 19 | `S-n3-bolsa` (restaurado) | «la bolsa no se abre, no se describe, no gana contenido y **no gana escena**» | C3 · C5 · R1 | **vinculante** | Sustituye a la cuenta en E6: no es un número, es una prohibición de escena. |
| 20 | `S-n1-casitodos`, `S-n2-hijadela`, `S-n4-escena3`, `S-n6-persona` | «No se ha podido reconstruir qué decía» | R5 · R7·4 · Carta 6 | **corregir (C8)** | Son reconstruibles verbatim desde `informes/a7-w5d-n4.md`. Dos contienen prohibiciones activas. Corregir también el texto de la nota. |
| 21 | `cap-08:55`, `cap-08:281`, `cap-07:33`, `cap-30:345` | «cuatro nombres que no son una despedida» | R2 · Carta 2 | **corregir (C9)** | El perímetro consolidado recoge uno de los cinco loci. Añadir fila a R2. |
| 22 | `verificar_b7.py` | detector de longitud exacta 300 | — (instrumento) | **vigilar** | Caza este corte, no la clase. Añadir cotejo contra `informes/a7-*.md`, que es lo que sí ha funcionado hoy. |
| 23 | C1 ↔ `S-n1-nocierra` | «2, y no hay una tercera» ↔ «la única voz con autoridad» | R3 · C1 | **vigilar** | C1 cuenta enunciaciones; voz con autoridad hay una. Fijarlo. |

---

# VEREDICTO REVISADO

**Consulta 1 · `APROBADO CON CORRECCIONES`, con un techo declarado dentro.**

- **Cerrado y no se vuelve a discutir (A7-it3-T1):** el matrimonio **en el presente narrativo
  anterior a la muerte**. Seis mil ochenta y dos palabras, dos días y medio, tres ficheros `total`:
  cualquier escena ahí es la última vez que se vieron. La petición de A6-3 leída como cronología
  está denegada en el gate.
- **Abierto, y es lo que contesta a los cinco lectores:** la escena **sin marco y sin fecha en la
  prosa**, en la ventana 2059-2060, POV de Maja, sobre una tercera cosa. El libro ya la tiene dos
  veces por esta misma mano (`cap-17`; `cap-27:137-149`). El `desc` restaurado **no la deniega**:
  prohíbe pegarle una frase al hervidor, y en la misma oleada, en el documento de al lado, yo
  **prescribo su forma** —«deterioro conyugal por objeto, sin explicar nada»—.
- **Obligatorias:** S1–S6, E1–E15, A7-it3-C1…C4 y **la nueva C7** (no explicar «No lo había» ni a
  distancia), más el refuerzo de E6 por `S-n3-bolsa` («no gana escena»). Dos pasadas de A7 sobre
  el borrador.

**Consulta 2 · `APROBADO`, sin cambios.** La restauración no toca `cap-14`. Siguen en pie
A7-it3-C5 y C6, y la corrección factual de la fila 12: `cap-14:317` es el único pago de
`S12-temblor` en el libro y está dentro del bloque que se corta.

**Obligatorias fuera de las dos consultas:** **A7-it3-C8** (restaurar los cuatro y corregir la
nota) y **A7-it3-C9** (los cuatro nombres de `cap-08` entran en R2). Ninguna de las dos bloquea la
iteración 3; las dos bloquean el cierre de W10.

---

**Firmado, A7 · adenda tras la restauración de los seis `desc` · 2026-08-20.**

*Se me ofreció cerrar una petición de cuatro nominaciones con mi propia firma y un texto que no
decía eso. Lo que más se parece a este proyecto no es equivocarse: es equivocarse hacia abajo, con
una nota tranquilizadora encima. Cuatro `desc` llevan hoy una nota que dice que su conclusión se
perdió, y su conclusión está en el fichero de al lado. Prefiero cerrar una puerta menos y dejar
escrito dónde se buscó.*
