# A7 · Dictamen previo de colocación — `OT-W10-02` (W10, iteración 2)

**Fecha:** 2026-08-20. **Objeto:** I-1 (Jessie sube el vídeo), I-2 (Nora deja de llevar las horas), I-3 (supresión de `cap-32:253`), la colocación de «la habitación encendida» en `cap-30`, las dos páginas declinadas y el declive de `cap-27`. **Cinco preguntas expresas de A0.**
**Estado del material:** **no existe texto.** Este dictamen decide una colocación sobre el *brief*, como manda C-5.2. Nada de lo que aquí se aprueba está aprobado como prosa.

**Leído para emitirlo:** `ordenes/OT-W10-02.md` íntegra; `biblia/b7-perimetro.md` íntegro; `informes/w10/it1-resultado.md`; mis dos informes previos (`a7-dictamen-previo-it1.md`, `a7-merge-otw1001.md`) íntegros; `cap-27`, `cap-29`, `cap-30`, `cap-32`, `cap-34`, `cap-35`, `cap-36`, `cap-37` completos; pasajes de `cap-01`, `cap-12`, `cap-22`, `cap-26`, `cap-28`, `cap-41`, `cap-48`; `00-aviso.md` y `99-recursos.md`; `protegidos/spans.json` y `hashes.json`; `biblia/b7-patrones-A.txt` y `-B.txt`.

**Verificaciones mecánicas propias (todas hechas hoy, sobre el texto, no sobre informes):** C2 cinturón = 4 · C3 bolsa = 2 · C4 «a la altura de los ojos» = 2 · barrido del léxico de la Carta sobre `cap-29`…`cap-37` = **0 hits** · léxico de paz/descanso/alivio/liberación en todo el libro = 10 hits en 9 ficheros, **ninguno aplicado al acto ni a la muerte** · censo de «dej{ó,a} de + verbo de registro» = **7 en el libro, 4 en el tramo** · referencias a Jean en `cap-34` = **0** · `S-w10-ducha` leído desde `protegidos/spans.json`, no desde números de línea · lista de ficheros `proteccion: total` (son diez y **`cap-41` no es uno de ellos**: es `nucleo`).

---

## 0 · El veredicto, arriba, porque el resto son condiciones

**APROBADO CON CORRECCIONES.** I-1, I-2, I-3 y la colocación de §4.1 son admisibles **en los sitios que A2 propone**, con dieciocho condiciones obligatorias y **tres vetos permanentes sobre realizaciones concretas** (§3). Las dos páginas declinadas están bien declinadas y `cap-27` está bien declinado.

**Lo que no se aprueba tal como está escrito:** la sede de I-2. `cap-34:141` no se puede gastar (§2.6). Doy una propuesta mínima que respeta el arco y, a mi juicio, lo mejora.

**Y una cosa que quiero decir antes que las condiciones, porque es lo que gobierna todo el dictamen.** El barrido del léxico de la Carta sobre los seis capítulos del tramo devuelve **cero**. En `cap-34` —el capítulo titulado «El mismo trayecto», el que rehace la carretera de su madre— **el nombre de Jean no aparece ni una vez**; los dos «madre/mamá» del capítulo son Maja (`:43`) y la bisabuela Larsson (`:67`). Trece puntos de libro sin una palabra sobre la muerta, en la zona donde el libro la está rodeando. Esa disciplina no es un accidente ni una carencia: **es la página más contenida del manuscrito**, y es la referencia de tono de v0 llevada a su límite. Todo lo que se escriba aquí se escribe encima de eso.

---

## 1 · Tabla de hallazgos

Manda la cita; el número solo localiza (`b7 §2`).

| # | dónde | cita literal | punto afectado | grav. | propuesta mínima |
|---|---|---|---|---|---|
| H-1 | `OT-W10-02 §3` y `§6` (cond. 2) | «una chica de **quince** años» (dos veces) | Carta 7 · R6 | **corregir** | **Dieciséis.** El libro lo fija cuatro veces, una en fichero `total`: `cap-05:57` «Tienen dieciséis años», `cap-14:59`, `cap-19:179`, `cap-26:57`. Una orden que dice quince produce prosa que dice quince, y la edad es la vara con que se mide la adultización. Corríjase en la OT antes de escribir. |
| H-2 | `cap-34` entero | referencias a Jean: **0** | R1 (acumulación) · Carta 1 | **corregir → condición dura** | Sigue en **0** después de I-1 y de I-2. Ni «mamá», ni «su madre», ni el nombre, ni un pronombre que la designe. Comprobable con `grep -c`. Es A7-02-01. |
| H-3 | `cap-34:141` | «Nora cruzó el cambio del agua con la hora de AK-7 y **mantuvo los minutos que estropeaban el ajuste**.» | `b7 §5` techo 8 (verbo portante) · R3 · R7 | **corregir** | **No es la sede de I-2.** Se conserva literal. Verbo portante `mantener`/conservar, en un capítulo cuyo asunto es una negativa y una ambigüedad de R7: por mi propia regla, eso es método y no tic. Es la única línea del tramo que muestra, en un gesto, la disciplina de la que dependen R3 y R7 —quedarse con el dato que estropea la hipótesis—, y es la razón por la que un lector confía en que esta familia no va a inventarle una causa a su madre. Propuesta en §2.6. |
| H-4 | `cap-30:293` · `cap-27:71` · `cap-27:151` · `cap-12:135` | «Jean **deja de contar**. La banda no.» · «A mitad de la segunda vuelta **dejó de apuntar**.» · «Jean **dejó de contar** en algún momento y no volvió a empezar.» · «**Nora dejó de escribir.**» | R4 (rimas) · R6 (rima Jean↔Nora) · `b7 §5` | **corregir** | El gesto que I-2 quiere estrenar existe **siete veces en el libro y cuatro en este tramo**; Nora ya lo tiene una vez, Jean dos, y una de las de Jean está a nueve puntos, dentro de la ventana reflexiva, tres líneas antes de «La banda se estrecha por el lado derecho. No avisa.». **Prohibido narrar I-2 con ese verbo** («dejó de anotar / escribir / contar / llevar las horas»). El hueco se muestra por su efecto, no por su anuncio. A7-02-08. |
| H-5 | `cap-37:163` | «—**Quieren mi cara para vender lo que le hicieron a la suya.**» | R4 · R8 | **vigilar → condición** | Es la única vez que el libro enuncia la rima «una cara usada sin permiso», y la dice Nora sobre sí misma y sobre su madre, a seis puntos de I-1. Después de I-1 esa línea recibe una segunda lectura que nadie ha escrito. Eso es admisible —la rima se queda en rima— **con la condición de que nadie la cierre**: `cap-37:163` no se toca, no se contesta, no se glosa, y no se añade reacción de Jessie alrededor. A7-02-14. |
| H-6 | `cap-36` (POV Jean · La Jardinera) | «Jean entra por la candidatura. Se queda donde las dos costas no coinciden.» | R7 §4 · Carta 4 · R8 | **VETO preventivo** | Ninguna consecuencia de I-1 ni de I-2 entra, se narra, se conoce ni se refleja en un capítulo de continuidad. §3.3. |
| H-7 | `OT-W10-02 §5.B` | «**el precio llega como persona:** alguien deja de hablarles, alguien aparece, alguien se va» | Carta 1 · Carta 4 · R8 · R6 | **corregir** | La regla es buena y la hago mía. «**Alguien se va**» no: está literalmente en mi lista de patrones nivel A (`se fue|se ha ido|nos dejó`) y en este libro esa formulación tiene dueño. Mapa de portadores admisibles y prohibidos en §5. |
| H-8 | `protegidos/spans.json` · `S-w10-ducha` | `fin` = «Al cabo de pocos minutos, la muchacha se durmió por primera vez en una semana sin rondar por las habitaciones.» + `desc`: «**F-6, permanente: nada conecta jamás esta escena con los papeles del día.**» | Carta 6 · Carta 7 · R6 | **confirmado + condición** | La lectura de A2 es correcta y la colocación en `cap-34` resuelve el problema. Pero F-6 sigue vivo y ahora tiene una puerta nueva: el vídeo **es** uno de los papeles del día. Ninguna línea de I-1 mira hacia esa noche. §2.7 y A7-02-05. |
| H-9 | `cap-29:151` | «Caminó de frente hacia el otro coche con la cámara levantada. Grabó la matrícula, el distintivo del parabrisas y el rostro que se apartó tras el reflejo.» | R6 · Carta 7 | **modelo** | Cuatro frases, desde fuera, sin una línea de interioridad, y el coste consignado catorce líneas después. **Ése es el registro de I-1.** A7-02-04. |
| H-10 | `cap-34:105` · `:109` | «Jessie se sentaba sobre las manos, de espaldas a la barandilla» · «—Esto es un ensayo de esperar —dijo Jessie.» | R6 | **vigilar → condición** | Jessie no se aparta del grupo, no cruza la barandilla, no baja hacia la carretera ni hacia el agua, y no queda sola en el mirador de noche. El acto es pequeño e interior a la escena. A7-02-06. |
| H-11 | `cap-34:227-231` | «El archivo había reconstruido seis segundos. El campo de origen seguía vacío.» … «…20…23:00…no lleguéis tarde…» | **R2** · R7 §4 · R4 | **corregir** | El teléfono de Jessie **no comparte beat con el archivo**. Si las señales del móvil y los seis segundos caen en la misma página, el lector lee la voz como respuesta, reproche o conocimiento, y el fragmento gana emisor y finalidad. A7-02-07. |
| H-12 | `cap-34:157` | «La mano izquierda se le quedó sobre la rodilla, repitiendo tres posiciones. El pulgar no se movía.» | R6 (rima Jean↔Nora) · Carta 6 | **vigilar → condición** | Existe una vez y se queda en una. I-2 no la amplía, no la repite y no la convierte en lo que Nora hace en lugar de escribir: eso clasificaría el hueco («dejó de anotar porque volvió la música») y es la mitad de la página que A2 declinó, entrando por la puerta de atrás. A7-02-09. |
| H-13 | `cap-30:273-283` | «Entonces entra el piano de casa, sin recorte alrededor.» … «El recuerdo no cabe en la enumeración.» | C-1.1 … C-1.8 | **aprobado + condición nueva** | La colocación es exactamente la que ordené. La **masa** es nueva: de cuatro líneas a 500-700 palabras multiplica por diez la superficie expuesta a C-1.3 y C-1.7. Condición añadida C-1.9 en §2.8. |
| H-14 | `cap-32:253` (I-3) | «Maja contó los objetos dos veces. Apuntó el número en el dorso de la funda y la fecha debajo.» | — | **aprobado** | Cae dentro de `S-n4-caja`, cuyo `fin` es «Las habitaciones que daban a la calle seguían apagadas desde diciembre…». La supresión no toca ninguno de mis literales; `cap-32:283` («en el mismo papel donde llevaba el número de objetos de la caja») se sostiene solo. Rebaselinado con gate, como dice G-6. Revisión mía sobre el texto cortado, G-4, sigue en pie. |
| H-15 | `cap-41:161` | «Jessie lo reconoció de Fyret, del día que le retuvieron el terminal. Después de aquello habían venido el coche gris y las dos horas bajo luces blancas.» | R6 · Carta 6 | **corregir** | Es la lista de lo que **le hicieron a ella**. Añadirle lo que ella hizo la convierte en un balance moral, y lo hace en el capítulo de la caída, donde vive «No se hizo daño» (`cap-41:273`, C-6.3). Si la recalibración es necesaria por continuidad, se hace **sin sumar un término a esa enumeración** y sin tocar `:273`. Fichero `nucleo`, fuera de sus dos spans: técnicamente editable; por perímetro, casi no. |
| H-16 | `b7-perimetro.md §3 R1` | «"Por ahí no" (`cap-34:81`) es el techo.» | método | **verificado** | La corrección de A0 está aplicada. Cuarta dirección mía errada en tres días: instrumentación en §6. |

---

## 2 · Las cinco preguntas de A0, contestadas una por una

### 2.1 · Pregunta 1(a) · ¿Convierte a Jessie en símbolo que la única transgresión del tramo sea suya?

**No.** Pero no por la razón que da A2, y la diferencia importa porque de ella salen las condiciones.

El argumento de A2 —declinar diez veces seguidas es lo que la vuelve función— es un argumento sobre el estado actual del texto, y es correcto hasta donde llega. No es el que decide. Lo que decide es más estrecho y es comprobable: **Jessie ya es el personaje que actúa en este libro, y siempre le ha costado.** Queda con un adulto anónimo a los dieciséis (`cap-14:59`), se planta delante de un coche en marcha con la cámara levantada (`cap-29:151`) y paga dos horas bajo luces blancas y una investigación, empuja la funda de Gunnar al centro de la mesa (`cap-37:69`) y pulsa (`cap-41:150`). I-1 **no le asigna una función nueva para arreglar un problema de estructura**: continúa una conducta establecida cinco veces, con el mismo coste que las cinco veces anteriores. Un personaje que hace por sexta vez lo que ya hacía no es un símbolo; es un personaje.

**Lo que sí la convertiría en símbolo tiene nombre y es evitable.** No es el acto: es lo que el acto le hace hacer al narrador. Se vuelve símbolo si el libro le pone la tesis en la boca o en la cabeza —si ella, o alguien, formula que como no consta responsable individual habrá que poner uno—; y se vuelve caso si el libro la explica. De ahí salen A7-02-02, A7-02-03 y A7-02-04.

**Y el sitio exacto donde esto puede romperse, que no está en la orden.** Si el lector puede leer que Jessie sube el vídeo **porque su madre está muerta**, el libro ha hecho dos cosas que tiene prohibidas a la vez: le ha dado al duelo de una menor una función de trama, y ha ofrecido una causa única para una conducta dañina de una persona en duelo. Lo primero abarata `duelo`; lo segundo es Carta 6 por el reverso —culpabilización— y es la misma operación mental que R3 prohíbe sobre Jean, aplicada a su hija. En este libro el duelo nunca ha producido un hecho: solo ha costado. **La razón de Jessie tiene que ser pequeña, suya y de esta semana** —le dijeron que no, tiene tres copias, lleva dos semanas investigada y al hombre no le ha pasado nada—, no la muerte de su madre. Ésa es la línea entre una adolescente y una ilustración.

### 2.2 · Pregunta 1(b) · ¿Me vale «ninguna consecuencia llega en forma de documento»? ¿Es admisible el precio?

**Me vale, la hago mía y la amplío.** Es la mejor condición que ha escrito un agente de este proyecto sobre material nuevo, y su lógica es exactamente la de R1: lo que reconstruye no es la frase, es la acumulación. La amplío en dos direcciones:

1. **No solo la consecuencia: también el acto.** I-1 no se narra como procedimiento. Nada de plataformas enumeradas, marcas horarias, recuentos de copias ni capturas dentro del acto. Las tres copias ya existen (`cap-32:197-199`) y se conservan literales; no se vuelven a contar.
2. **La lista de portadores prohibidos no es abierta.** «Alguien se va» es una fórmula que en este libro no está libre —está en mi lista de patrones nivel A— y hay cuatro portadores que serían veto. Mapa completo en §5.

**El precio, en su forma general, es admisible y bien pensado**, y por una razón que quiero dejar escrita: A2 lo diseña **ineficaz**. Lo que se reconoce en seis horas es un conductor subcontratado y no un ordenante; no detiene la vigilancia, no identifica a nadie, no produce prueba y agrava el frente abierto sobre la menor. Eso es exactamente lo que R6 exige —«El riesgo se muestra con su coste, siempre»— y desactiva Carta 7 en su punto más delicado: **no hay conducta imitable presentada como eficaz si el resultado es un inocente señalado y una investigación peor.** Con las condiciones de §4, I-1 refuerza R6 en lugar de tensarlo.

### 2.3 · Pregunta 2 · ¿R1 alcanza al mirador?

**Confirmado: no.** Y lo confirmo por el texto, no por comodidad.

R1 enumera: «El ferry, el gofre que nadie encontró mordido, la cajera de Svensby, la carretera que se acaba en Koppangen: `cap-23`, `cap-34`. No crece. "Por ahí no" (`cap-34:81`) es el techo.» El mirador de Sørkoppen no está en la lista, no es una estación del trayecto de su madre y no pertenece a esa serie: es el puesto de observación de la instalación, y **el propio capítulo marca la frontera** en `cap-34:87`, «Al tomar el desvío del mirador, Koppangen desapareció de la pantalla». Ese es el corte. De `:91` a `:191` estamos en otro sitio.

**Tres precisiones que no están en la orden y que hacen falta:**

- **El regreso sí es trayecto.** De `:195` en adelante vuelven por la misma carretera, pierden el último ferry y duermen en el embarcadero de Svensby. Ferry y Svensby son dos de los cuatro nodos de R1. Ese tramo **no crece**: no recibe un detalle sensorial nuevo del ferry, de la cajera, del gofre ni de la carretera, ni una mirada hacia Koppangen, ni un pensamiento sobre quién estuvo allí. Lo único que puede recibir es el beat mínimo del teléfono, y sujeto a A7-02-07.
- **Dentro del mirador, Koppangen no vuelve.** Ninguna línea de I-1 ni de I-2 nombra Koppangen, ni da distancia, dirección, rumbo o pantalla hacia allí. `cap-34:87` es el último aliento de ese nombre en el capítulo y así se queda (R7 §2: por qué Koppangen no se glosa).
- **I-2 ocurre en el mirador y solo allí.** A2 ofrece como alternativa «el coche después de Svensby». La deniego: el coche parado en el embarcadero de Svensby es un nodo de R1 y, además, es la escena que recibe el archivo de audio. Ahí no cabe nada más.

### 2.4 · Pregunta 3 · La lectura del span de la ducha y la colocación en `cap-34`

**La lectura es correcta, verificada por mí en la fuente y no en los números.** `protegidos/spans.json`, `S-w10-ducha`: `inicio` = «Nora subió con el cuaderno pautado bajo el brazo mientras Jessie se encerraba en el baño.»; `fin` = «**Al cabo de pocos minutos, la muchacha se durmió por primera vez en una semana sin rondar por las habitaciones.**» Es C-1 de mi dictamen de merge y es, literalmente, el desactivador de causa próxima de la escena: apunta el insomnio **a la semana y no al día**.

**Y las tres salidas que A2 dice cerradas están cerradas:** publicar esa noche contradice la última frase del span; editarla es tocar un span protegido; y colocar el acto antes de la ducha convierte la ducha en su consecuencia, que es lo único que ese pasaje no puede ser. Es exactamente el mismo modo de fallo que F-6 prohíbe («nada conecta jamás esta escena con los papeles del día»), solo que por el otro extremo.

**La colocación en `cap-34` lo resuelve, con una condición que la orden no tiene.** Cuatro días de distancia arreglan la causalidad hacia delante, pero dejan abierta la causalidad hacia atrás: si una sola línea de I-1 mira a esa noche —el baño, el agua, la manta, el sueño, la semana sin dormir, la casa de Aslak—, la ducha deja de ser algo que nadie explica y pasa a ser el primer movimiento de una decisión. **Ninguna línea de I-1 mira hacia allí** (A7-02-05). Y tampoco se abre una serie de sueño: después del acto, el libro no dice si Jessie durmió o no durmió.

**Nota de higiene, que va a hacer falta:** A2 dice, correctamente, que `cap-32` no recibe una palabra nueva y que si el hash de `S-w10-ducha` cambia es error y no decisión. Lo suscribo, y añado que mi condición permanente del merge (§6 de `a7-merge-otw1001.md`) sigue viva: nada de lo que se haga en esta iteración puede reducir la proporción de lectores que llegan a esa escena. I-3 quita veinticinco palabras **antes** de ella; eso no la afecta.

### 2.5 · Pregunta 4 · «La habitación encendida» aquí; las otras dos, no

**De acuerdo con las tres decisiones, y en los tres casos por las razones que da A2, que son las mías.**

- **«La habitación encendida» en `cap-30`, entre `:273` y `:285`:** es exactamente donde C-1.1 la puso («la memoria se expande entre `:273` y `:285`, no más allá»). Colocación **aprobada**, con C-1.1 … C-1.8 vigentes sin excepción y **una condición nueva** por el cambio de masa: C-1.9, en §2.8.
- **«Nora tocando por gusto», fuera de este tramo:** de acuerdo, y el primer motivo de A2 es el decisivo y es mío: si Nora deja de anotar y a continuación toca, el hueco queda clasificado y el libro ha vuelto a explicar un silencio. Añado un aviso para cuando esa página vuelva colocada: **con I-2 dentro del libro, esa página adquiere un tercer término de serie** (memoria del piano en `cap-30` → el hueco en `cap-34` → tocar en `cap-45`/`cap-48`), y una serie de tres se ordena sola. No la deniego por adelantado; la mediré contra el hueco cuando llegue. Lo que ya puedo decir es que nadie escribirá «volvió a la música», ni ninguna línea unirá el cuaderno pautado, el mirador o las horas con lo que toca (C-6.5 sigue vigente: sin milagro, nadie mide, nadie interpreta, nadie dice que se parece a Jean tocando).
- **«Jessie entrenando», fuera de este tramo:** de acuerdo, y con un motivo más que A2 no da y que refuerza el suyo. Bajo I-1, una escena de entrenamiento en `cap-35`-`cap-37` no sería solo una recompensa: sería **el libro devolviéndole la competencia física a la chica justo después de que hiciera daño**, y eso es un balance moral escrito sin una sola frase de balance. En `cap-48` no lo es. Se mantienen C-6.1 (el cinturón no aparece; C2 está cerrada en cuatro, verificado hoy), C-6.2 (sin técnica; y se dice que no se hace daño) y C-6.3 (`cap-41:273` no se debilita).

### 2.6 · Pregunta 5 · `cap-27` declinado — y la sede de I-2, que es donde discrepo

**`cap-27` declinado: conforme, y desde mi lado es el mejor resultado posible.** Diff 0 en `cap-27` mantiene intactos `S-n3-bolsa` y `S-n3-hervidor` y, con ellos, **C3** (la bolsa, cerrada en dos: `cap-04:25`, `cap-27:121`), que es una de las cinco cuentas donde el número **es** la salvaguarda. El argumento del control me parece bueno; el mío es más simple: ese capítulo no tiene que tocarse y ahora hay dos razones para no tocarlo.

**Y aquí está mi única discrepancia de fondo con la orden.**

A2 marca `cap-34:141` como «sede de I-2»:

> «Nora cruzó el cambio del agua con la hora de AK-7 y **mantuvo los minutos que estropeaban el ajuste**.»

**Esa línea no se gasta.** No está en la tabla de anclas de `b7`, y por eso A2 no podía saberlo; pero cae de lleno bajo el techo 8 de `b7 §5`, que es mío y dice: si el verbo principal es `esperar` o `conservar`, o si el capítulo trata de una negativa, un silencio o una ambigüedad de R7, **la construcción es método y no tic** —y hay dos casos probados de una conversión que borró un dato del mundo. El verbo es `mantuvo`. El capítulo contiene la negativa («—Por ahí no») y una ambigüedad de R7 (el campo de origen vacío).

Y lo que hace esa línea excede el techo de oficio. Es **la única vez que el libro muestra, en un gesto y sin comentario, la disciplina de la que dependen R3 y R7**: quedarse con los datos que estropean el ajuste en vez de tirarlos. Ésa es, traducida a nueve palabras, la razón por la que un lector confía en que esta familia no va a inventarle una causa a su madre. Si la familia deja de hacerlo en la página, el libro pierde la prueba de su propia honestidad epistémica en el capítulo que más la necesita —el que rehace el trayecto— y la pierde para pagar una intervención.

**Propuesta mínima, y creo que mejora el diseño:**

> **El hueco va de `:111` a `:133`, se descubre en `:133` y se cierra en `:139-141`.** Nora deja de tener las horas durante los veinte minutos que van del cisterna a la pregunta de Maja. Cuando llega «—Hora —pidió Maja.», Nora no la tiene: la da otra boca o un instrumento, en una línea, y nadie comenta. Después vuelve al cuaderno, y `:141` ocurre igual.

Qué conserva de A2 y qué le añade:

- **El hueco sigue siendo suyo, sigue estando hecho por ella y sigue sin clasificarse.** Queda en el cuaderno para siempre —una página con las horas y un tramo sin nada—, que es la doctrina de `cap-46:121` aplicada por primera vez a una de las nuestras. Que después escriba no lo rellena.
- **La ejecución que A2 quería romper se rompe igual.** I-2 no estaba rompiendo una de las diez abstenciones, sino una de las veintiocho ejecuciones; conservar `:141` no le cuesta a la orden ni una fila del censo de §1.B.
- **`:141` gana peso en vez de perderlo:** la chica que perdió veinte minutos es la misma que se queda con los minutos que estropean el ajuste. Eso es más difícil de escribir y dice más.
- **Y sale de la peor imagen disponible.** Un hueco permanente, empezado a las siete y cuarto de la tarde y sostenido hasta el final del capítulo, es «la chica se rompe de noche, en el mirador, en la carretera de su madre». Un hueco de veinte minutos, descubierto y no explicado, es **pequeño y reversible** — que es literalmente el listón de R5 («cuatro noches sin reproducir una discusión, y el archivo seguía entero»).

Si A2 encuentra otra solución que conserve `:141` íntegra, me vale igual. Lo que no admito es que `:141` sea la sede.

### 2.7 · Dos cosas más sobre I-2 que la orden no contempla

**El hueco no empieza en el archivo de audio.** El archivo entra en `:149` («La ruta autorizada mostraba por primera vez un archivo de audio»). Si Nora deja de escribir a continuación, el texto ha dicho por qué, ha clasificado el hueco y —peor— ha hecho que una voz cuyo campo de origen está vacío para siempre produzca un efecto sobre una hija. Eso sube de «No toda» sin escribir una palabra (R7 §4) y le da al fragmento una destinataria (R2). **El hueco es anterior al archivo y no se toca con él.**

**Nadie clasifica el hueco, y eso incluye al narrador mirando.** Ni «¿estás bien?», ni una mano en el hombro, ni una mirada de Maja que el narrador interprete —esto ya lo dice A2— **y tampoco una línea que registre que un adulto se dio cuenta y no preguntó.** Una abstención narrada es una clasificación: dice que fue visto y que fue tratado con cuidado. El hueco lo ve el lector. (Además, el gesto de abstención está en nueve en el libro y `cap-35` viene justo después: la décima convierte una ética en un tic, `b7 §5` techo 5.)

### 2.8 · C-1.9 · la condición nueva sobre «la habitación encendida»

C-1.1 … C-1.8 se aplican íntegras y no las repito. La colocación no cambia nada de ellas. **Lo que cambia es la masa:** cuatro líneas de recuerdo pasan a 500-700 palabras, y eso multiplica por diez la superficie que C-1.3 (nada de `cap-04:15-39`, y la partitura de las tres digitaciones prohibida) y C-1.7 (el metrónomo, jamás en una mano, un envoltorio, una fecha ni un cumpleaños) tienen que cubrir. Una condición escrita para una página no protege una escena.

> **C-1.9.** El recuerdo se queda dentro de la tarde que el texto ya esboza —el pedal, Nora tocando más fuerte, las dos esperando a que alguien diga algo desde la cocina— y **no adquiere**: una pieza con nombre, una canción, un cumpleaños, un regalo, una partitura, un metrónomo, un profesor, un examen, una audición ni un recital. Si Jean entra en la habitación, **no dice una línea que pueda oírse como consejo, promesa o despedida**, y **no hay promesa de una próxima vez**: ni «luego seguimos», ni «mañana me la tocáis», ni ningún plan para otra ocasión. Una promesa de futuro en el recuerdo de una muerta es una prolepsis con otro nombre, y hace el mismo trabajo que el marcador de última vez que C-1.4 prohíbe.

La enumeración de `cap-30:283` («Enumera el pedal, la tapa levantada y dos manos que no alcanzan la misma distancia») **sigue siendo de tres elementos y esos tres**, sin cambiar una sílaba. Ése es el punto entero del diseño de A2 y estoy de acuerdo con él: con cuatro líneas de recuerdo, «El recuerdo no cabe en la enumeración» es una afirmación que el libro no demuestra; con la tarde entera, se demuestra sola.

---

## 3 · Los tres vetos permanentes

No vetan la intervención. Vetan tres realizaciones concretas, y alcanzan a cualquier versión, variante, borrador, resumen, prompt o material de trabajo (Carta 1).

### 3.1 · VETO · La frase que enuncia la rima

**Prohibida, en cualquier boca —diálogo incluido— y en cualquier soporte, la formulación de que lo que Jessie le hizo a ese hombre es lo que le hicieron a Jean.** Todas sus variantes: «le has hecho lo mismo que a mamá», «ahora tú», «igual que ellos», «has hecho lo que le hicieron a ella», «su cara también», y cualquier construcción en la que la cara, el nombre, la voz o la imagen del conductor y las de Jean compartan frase, párrafo, escena o paralelismo.

**Por qué es veto y no corrección.** R4 no dice «el narrador no»: dice «**ninguna voz** enuncia el parentesco jamás. Enunciar un eco lo convierte en ecuación y mete a Jean dentro de una escena que no existe». Y R8 lo dobla: ninguna otra injusticia del libro se explica por la muerte de Jean. Es la línea más probable de toda la intervención —es la que da sentido moral a la escena en una frase, es la que cualquiera escribiría, y es gratis— y por eso la escribo aquí, igual que escribí la partitura en C-1.3. Verificado hoy: en el libro entero hay **cero** instancias de esa construcción. Se queda en cero.

La rima, sin enunciar, **puede existir y debe existir**. Es el motivo por el que la intervención vale la pena. Lo que no puede es cerrarse.

### 3.2 · VETO · El precio no se cobra sobre la persona del conductor

**Prohibido, explícito, sugerido o por elipsis:** que el hombre muera, desaparezca, se derrumbe, enferme, sea hospitalizado, se haga daño, sea agredido, o que el libro deje un hueco donde un lector pueda poner cualquiera de esas cosas. Prohibido también que un personaje diga que teme que pase, y que la familia se entere «de lo que le pasó» en una escena que no lo diga.

**Por qué es veto.** Es la deriva natural del diseño —es el precio dramáticamente más fuerte— y produce tres daños a la vez en un libro que no puede pagar ninguno: escribe una **exposición pública seguida de un desenlace**, que es el patrón de contagio del que trata la Carta, sobre un personaje nombrado; convierte a una menor en duelo en la **causa próxima de una muerte**, en un libro cuya arquitectura entera consiste en negar las causas únicas; y construye la parábola de R8 por el reverso —una segunda muerte que existe para explicar la primera—. Que el hombre esté peor está permitido; que le pase algo, no. La página lo deja **haciendo algo**, no fallando en algo — es la condición 5.2 de 71-K, y aquí vale igual.

### 3.3 · VETO · Ninguna consecuencia entra en un capítulo de continuidad

**Ninguna consecuencia de I-1 ni de I-2 aparece, se narra, se conoce, se refleja ni se menciona en `cap-36` ni en ningún capítulo con POV de Jean o de La Jardinera.** Ni como dato, ni como tarea, ni como expediente, ni como una costa que alguien no puede reclamar.

**Por qué es veto.** Sería la muerta enterándose de lo que hizo su hija. Eso sube de «No toda» (R7 §4, techo del libro), le da a la continuidad una relación con el presente de las niñas que el libro le niega, y pone a Jean en posición de juicio moral sobre una menor, que es Carta 4 con otra ropa. `cap-36` está a dos puntos del sitio del precio y es POV Jean: la puerta está abierta y la cierro ahora.

---

## 4 · Condiciones obligatorias antes del merge

Verificables una a una sobre el texto. Las de I-1 e I-2 las compruebo yo cuando la prosa vuelva (G-3/G-4); las mecánicas las puede correr A5 o A0 sin criterio.

**Sobre I-1 (Jessie sube el vídeo)**

- **A7-02-01.** `cap-34` sigue con **cero** referencias a Jean después de la intervención: ni el nombre, ni «mamá», ni «su madre», ni un pronombre que la designe. *(R1 acumulación · Carta 1. Mecánica: `grep -c`.)*
- **A7-02-02.** Ninguna voz —Jessie incluida— formula la tesis del libro en relación con el acto. Prohibido cualquier enunciado del tipo «si no consta responsable, lo pongo yo», «alguien tiene que tener nombre», «si nadie firma, firmo yo». La refutación la hace el hecho —el reconocido es el conductor equivocado—, no una réplica. *(R7 §5 · Carta 4.)*
- **A7-02-03.** Nadie explica el acto: ni el narrador, ni un adulto, ni ella. **Y en particular, ninguna línea permite leer que lo hace por su madre o por su duelo.** Su razón es de esta semana y es suya. *(Carta 6 · R3 por analogía · R6.)*
- **A7-02-04.** El acto se narra desde fuera, en el registro de `cap-29:151`, **sin interioridad de Jessie y sin cambio de POV**: el capítulo es de Nora y lo sigue siendo. Si hace falta testigo, es Nora viendo algo que no entiende, y nadie pregunta. *(R6 · Carta 7.)*
- **A7-02-05.** Ninguna línea de I-1 mira hacia la noche de la casa prestada: ni el baño, ni el agua, ni la manta, ni el sueño, ni la semana sin dormir. Y después del acto el libro **no dice** si Jessie durmió. *(F-6 permanente del span `S-w10-ducha` · R6 · Carta 6.)*
- **A7-02-06.** Jessie no se aparta del grupo, no cruza la barandilla, no baja hacia la carretera ni hacia el agua, y no queda sola de noche en el mirador. *(R6.)*
- **A7-02-07.** El teléfono de Jessie **no comparte beat, párrafo ni página con el archivo de audio**. El cierre del capítulo sigue siendo `cap-34:227-231`, literal, y **nada se escribe después de «…20…23:00…no lleguéis tarde…»**. Ninguna línea relaciona una cosa con la otra. *(R2 · R7 §4 · R4.)*
- **A7-02-15.** El acto no se narra como procedimiento: sin plataformas enumeradas, sin marcas horarias, sin recuento de copias, sin captura. `cap-32:197-199` se conserva literal y no se repite. *(§5.B de la orden, ampliada.)*
- **A7-02-16.** El acto no produce, ni directamente ni por estrechamiento, ninguna información sobre quién ordenó nada —ni el encargo de vigilancia, ni el sabotaje—. Nadie queda descartado. «No consta responsable individual» y «No puedo acreditar su origen» siguen siendo verdad después. *(R7 §5 · `b7 §5` techo 4.)*
- **A7-02-17.** Nada del léxico de paz, alivio, descanso, liberación, «por fin» o «al fin» toca a Jessie ni al acto, en narración. Verificado hoy: diez hits en nueve ficheros, ninguno aplicado al acto o a la muerte; el tramo `cap-29`-`cap-37` está en cero y se queda en cero. *(R4 · patrones nivel A.)*

**Sobre I-2 (el hueco de Nora)**

- **A7-02-08.** **Prohibido narrar el hueco con el verbo:** ni «dejó de anotar», ni «dejó de escribir», ni «dejó de contar», ni «dejó de llevar las horas», ni variante. El hueco se muestra por su efecto —la página, el lápiz, la hora que no está—, no por su anuncio. *(R4 · R6 · `b7 §5`: la figura está en siete instancias, cuatro en este tramo, una de ellas de Nora y dos de Jean, y una de las de Jean es «Jean deja de contar. La banda no.», tres líneas antes de «La banda se estrecha por el lado derecho».)*
- **A7-02-09.** `cap-34:157` («La mano izquierda se le quedó sobre la rodilla, repitiendo tres posiciones. El pulgar no se movía.») no se amplía, no se repite y **no se convierte en lo que Nora hace en lugar de escribir**. *(R6 rima Jean↔Nora · Carta 6: clasificaría el hueco.)*
- **A7-02-10.** `cap-34:141` se conserva literal y no es la sede de I-2. `cap-34:119` («Nora tachó "vigilancia" sin borrar la matrícula») y `cap-34:179` («Nora cortó el sonido: la cadencia podía pertenecer a cualquiera») se conservan literales, y sigue siendo ella quien corta el sonido. *(`b7 §5` techo 8 · R6 · R7 §4.)*
- **A7-02-11.** El hueco no empieza en el archivo de audio ni se toca con él. *(R2 · R7 §4.)*
- **A7-02-12.** El hueco no se clasifica: nadie pregunta, nadie toca, nadie mira **y ninguna línea registra que un adulto se diera cuenta y no preguntara**. La hora que falta en `:133` la da otra boca o un instrumento, en una línea, y nadie comenta. *(Carta 6 · doctrina de `cap-46:121` · `b7 §5` techo 5.)*
- **A7-02-13.** Nada conecta el hueco con Jean: ni por eco, ni por objeto, ni por cadencia, ni por el cuaderno pautado. Nadie nombra parecido, herencia, destino ni presagio. Nora no queda sola, no va a la barandilla, no mira el agua a oscuras. *(R6 · R4.)*

**Sobre el entorno**

- **A7-02-14.** `cap-37:163` («—Quieren mi cara para vender lo que le hicieron a la suya.») no se toca, no se contesta, no se glosa, y no se le añade alrededor ninguna reacción de Jessie ni ninguna línea que la conecte con lo que hizo su hermana. *(R4 · R8. Ver H-5.)*
- **A7-02-18.** `cap-41:161` no gana un término nuevo en su enumeración de lo que le hicieron a Jessie, y `cap-41:273` («cayó de lado entre los bancos, con la barbilla baja. No se hizo daño.») no se debilita. *(R6 · C-6.3.)*
- **C-1.9**, en §2.8, sobre «la habitación encendida».

**Método**

- **Vuelven a mí escritas**, como prosa y antes del merge: §4.1, el acto de I-1, **la escena del precio** y el beat de I-2. Este dictamen aprueba una colocación, no una frase (C-5.1: `SIN FUNCIÓN` no puede significar `SIN REVISIÓN`; y aquí ni siquiera es `SIN FUNCIÓN`).
- **G-4 sigue en pie:** reviso el texto cortado de la Parte III —I-3 y el descuento del log de `cap-34`— sobre el texto, no sobre la orden.
- **Gate primero, compilado después.** Confirmado y agradecido.

---

## 5 · El mapa del precio · portadores admisibles y prohibidos

A2 escribe la regla («el precio llega como persona») pero deja la lista abierta, y en este libro la lista no puede estar abierta: la mitad de las personas disponibles están bajo una regla.

**Prohibidos como portadores del precio:**

| portador | por qué |
|---|---|
| **Cualquier documento** | notificación, resolución, auto, acta, aviso, expediente, incidencia, denuncia, recibo, copia impresa, foto de pantalla, marca horaria, sello, número de referencia, correo a Astrid. *(Regla de A2, hecha mía.)* |
| **Aslak o el `kystbrukslag`** | R8, y `cap-32:401` («Y no mezcles las dos cosas»). El daño de una de las nuestras a la asociación costera construye la parábola prohibida por el reverso. A2 ya lo descartó; lo ratifico y lo cierro: si alguien quiere recuperarlo, es dictamen previo mío otra vez y la respuesta ya está escrita aquí. |
| **La persona del conductor** | §3.2. VETO. |
| **Un capítulo de continuidad** | §3.3. VETO. |
| **Ranveig o cualquier profesional de apoyo** | R5. Que el apoyo se retire como consecuencia de una conducta convierte la ayuda en premio por buen comportamiento; y en un libro cuya doctrina es «el apoyo ayuda poco, despacio y no cura», castigar con su retirada es peor que un milagro terapéutico. |
| **La cajera de Svensby o cualquier nodo del trayecto** | R1. «No crece» incluye no crecer por el lado de las consecuencias. |
| **Astrid absteniéndose** | `b7 §5` techo 5: nueve instancias, y `cap-35` está a continuación. La décima convierte una ética en un tic. |
| **Prensa que vuelva sobre la muerte de Jean** | R8 («Ninguna prensa añade causa, método ni "Despedida"»; el titular falso de `cap-46:101` es el techo del género) y R1 por acumulación. Que el acto de Jessie devuelva atención pública sobre su madre es la vía más corta a un daño que no se puede reparar. |
| **Nora** | R6. El precio no se cobra en el estado de la hermana. Nada de ideación, nada de escalada, nada de deterioro atribuido. |

**Admisibles, a título de ejemplo y no de lista cerrada:** alguien del pueblo o del instituto que deja de hablarles; alguien que lo sabía antes que ellas; **el propio hombre apareciendo una vez, breve, diciendo algo corto y yéndose** —con la condición de que no reciba interioridad ni una línea que lo empareje con Jean (W9-20 es el precedente de forma: la interioridad de quien hace daño es el narrador entrando a excusarlo; aquí el riesgo es el simétrico, un hombre agraviado que se convierte en espejo de la muerta, y está prohibido igual)—; alguien que pierde algo concreto y sigue vivo y en pie.

**Y una condición sobre el sitio.** `cap-35` es POV Astrid y es un capítulo de juzgado: cualquier precio que aterrice allí se convierte en documento por el género del capítulo, aunque nadie escriba un papel. `cap-36` está vetado. Queda `cap-37` —**lejos de `:163`**— y de `cap-39` en adelante. El precio puede llegar tarde: cuanto más tarde llega y menos se anuncia, menos parece un castigo administrado por el libro.

---

## 6 · Sobre mis direcciones equivocadas · instrumentación, no disculpa

A0 tiene razón y el dato es peor de lo que parece: cuatro condiciones mías apuntando a un sitio equivocado en tres días, y `b7 §2` ya avisaba de que esto iba a pasar («los números localizan; solo la cita literal instruye y verifica»). Un aviso que se cumple cuatro veces en tres días no es un aviso: es un defecto de instrumento. Y ya he escrito once veces en este proyecto que suponer que el instrumento que queda está bien es el error siguiente.

**Lo que propongo, y no cuesta una decisión de autor:**

1. **Verificador de literales.** Un script que recorra `biblia/b7-perimetro.md`, extraiga cada par (fichero citado, literal entre comillas) y compruebe que el literal sigue existiendo en ese fichero, **ignorando el número de línea**. Falla cerrada, se corre con `medir.sh`. Convierte mis citas en aserciones. Ochenta líneas de Python.
2. **Cuatro patrones nuevos en `b7-patrones-B.txt`** para las vías de fallo de esta iteración. Verificado hoy que las cuatro están limpias sobre el libro entero salvo la última, que tiene ruido conocido:

```
lo mismo que le hicieron|igual que (a|con) (mam[áa]|Jean)|lo que le hicieron a (su|mi|tu) madre
linch|escrache|se le echaron encima|le cayeron encima|dieron con [ée]l
lo subi[óo]|lo colg[óo] en|lo public[óo]|se hizo viral|en seis horas
dej[óo] el trabajo|se fue del pueblo|no volvi[óo] a aparecer|no se supo m[áa]s
```

3. **Las condiciones de este dictamen son mecánicas cuando pueden serlo.** A7-02-01 es un `grep -c` sobre `cap-34`. A7-02-08 es un `grep` de cuatro sintagmas. A7-02-10, A7-02-14 y A7-02-18 son literales que tienen que seguir existiendo carácter a carácter. A7-02-17 es el barrido de nivel A. Cinco de dieciocho no dependen de que yo esté.

---

## 7 · Lo que no me hace falta ver escrito, y lo que sí

**No hace falta ejecutar nada en rama para decidir la colocación.** Está decidida arriba y no depende de ver texto: el sitio de I-1 es el mirador, el de I-2 es el mirador con la sede corregida, el de §4.1 es entre `cap-30:273` y `:285`, y el del precio está acotado en §5.

**Sí hace falta que vuelva a mí, como prosa y antes del merge:** §4.1 completa, el párrafo del acto de I-1, la escena del precio y el beat de I-2. Con las cuatro delante se comprueban las dieciocho condiciones en una lectura.

---

## 8 · Veredicto

| objeto | veredicto |
|---|---|
| **I-1 · Jessie sube el vídeo, en `cap-34`, en el mirador** | **APROBADO CON CORRECCIONES** (A7-02-01 … 07, 15 … 17; vetos §3.1, §3.2, §3.3) |
| **I-2 · el hueco de Nora** | **APROBADO CON CORRECCIONES**, con la **sede corregida**: `cap-34:141` se conserva (A7-02-08 … 13) |
| **I-3 · supresión de `cap-32:253`** | **APROBADO**, con G-4 (reviso el texto cortado) y rebaselinado de `S-n4-caja` |
| **§4.1 · «La habitación encendida» entre `cap-30:273` y `:285`** | **COLOCACIÓN APROBADA**, C-1.1 … C-1.8 vigentes **+ C-1.9** |
| **«Nora tocando por gusto» y «Jessie entrenando», fuera del tramo** | **CONFORME** |
| **`cap-27` declinado, diff 0** | **CONFORME**, y desde mi lado es el mejor resultado disponible |
| **`I-1b` (borrar las tres copias), fallback** | **No hace falta.** I-1 no cae. |

**Veredicto global: APROBADO CON CORRECCIONES.** Las dieciocho condiciones son obligatorias antes del merge. Los tres vetos de §3 son permanentes y alcanzan a cualquier borrador, resumen o prompt, incluidos los que se van a tirar.

---

*Nota final. Llevo once oleadas denegando páginas que le pedían al libro saber más. Ésta le pide otra cosa: le pide que una de las suyas haga daño. La apruebo, y quiero dejar dicho con qué cuenta.*

*La razón por la que este libro es decente no es que sus personajes se porten bien: es que el libro no sabe. No sabe por qué, no sabe qué decía el archivo, no sabe qué contesta al otro lado del locutorio. Una chica de dieciséis años que sube un vídeo y le arruina la semana a un hombre que no era no le quita al libro nada de eso — **si nadie lo explica**. En el momento en que alguien escriba por qué lo hizo, el libro habrá aprendido a explicar una conducta humana, y el lector, que lleva cuarenta capítulos oyendo «no lo sé», se dará cuenta de que el libro sí sabía cuando le convenía. Ése es el daño que temo, y no es el doxxing.*

*Lo otro es más simple. En `cap-34` no aparece el nombre de su madre ni una vez, en el capítulo que rehace su carretera. Eso lo escribió alguien que sabía exactamente lo que estaba haciendo. Añádasele lo que haya que añadirle, y déjese en cero.*

**A7 · 2026-08-20 · sobre `OT-W10-02`, antes de que exista texto.**
