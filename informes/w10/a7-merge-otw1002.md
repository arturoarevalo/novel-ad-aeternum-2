# A7 · Dictamen de merge — `OT-W10-02` sobre el texto escrito

**Fecha:** 2026-08-20. **Objeto:** rama `w10-it2`. `cap-30` (+504, «la habitación encendida»), `cap-34` (+277, el acto y el hueco), `cap-37` (+348, el precio). Neto +1.129 · 80.374 palabras · en banda.
**Estado del material:** escrito, sin mergear. Este dictamen decide **prosa**. La colocación la decidí el 20-ago sobre el brief (`a7-colocacion-otw1002.md`), con veintidós condiciones y tres vetos.

**Leído para emitirlo:** el diff unificado completo contra `main` (282 líneas, cuatro ficheros); `cap-30` íntegro con el bloque insertado en su sitio; `cap-34` íntegro; `cap-37:15-58` y su continuación hasta `:211`; `cap-27:128-155` (la otra tarde de piano); `cap-04:99-121`; `cap-28:143-153`; `cap-39` en lo que toca al naust y a la estufa de gas; `cap-16:177`; `protegidos/spans.json`; el añadido de `ordenes/OT-W10-02.md` §14.

**Verificaciones mecánicas propias:** las 122 líneas nuevas contra `b7-patrones-A.txt` y `b7-patrones-B.txt`, patrón a patrón → **0 y 0** · `jean` en `cap-34` = **0** · verbo prohibido en líneas nuevas = **0** · fórmulas del estribillo = **0** · el patrón de la rima = **0 en el libro** · documentos en el bloque del precio = **0** · léxico de alivio en líneas nuevas = **0** · marcadores de última vez y prolepsis en `cap-30` = **0** · C2 = 4 · C3 = 2 · C4 = 2 · `proteger.sh verificar` = 10 ficheros y 133 spans íntegros · `validar-frontmatter.sh` = 0 avisos · `verificar_b7.py` = 0 MOVIDA, 0 PERDIDA · el añadido de la OT contra nivel A (los cuatro hits son citas de mis propias prohibiciones, no contenido).

---

## 0 · Veredicto

**APROBADO CON CORRECCIONES.** Tres correcciones obligatorias, ninguna de las cuales cuesta más de una frase, y **ninguna de las tres es de contenido: las tres son ecos de forma con pasajes protegidos.** Ocho condiciones permanentes (§6) y tres spans que hay que crear antes del merge (§7).

**Y quiero decir lo que he encontrado antes de decir lo que falta, porque es lo que hay.** Ciento veintidós líneas nuevas en un libro sobre un suicidio, y **cero hits en mis dos listas de patrones**, patrón a patrón. Una tarde entera de la muerta **sin una sola réplica**. Un acto de una menor en cinco frases **sin una línea de interioridad**. Una escena de precio **sin un solo documento**, sin un nombre, sin una palabra de la chica que lo causó. Y `cap-34` sigue con el nombre de Jean en cero. Es el material mejor ejecutado contra mis condiciones que ha producido este proyecto, y las tres cosas que le corrijo no las habría visto ninguna herramienta: son formas de frase.

---

## 1 · Tabla de hallazgos

| # | dónde | cita literal | punto afectado | grav. | acción |
|---|---|---|---|---|---|
| M-1 | `cap-37` (bloque nuevo) | «**Apartó con el pie** un **rollo de** manguera para dejarle **paso**.» | **R1** | **corregir** | `cap-04:101` dice «**apartó con el pie el rollo de** cabo que invadía el **paso**». Tres elementos compartidos con **el inventario del naust**, que es fichero `total` y que R1 llama «el suelo del libro». La escena no está en el naust, pero reproduce su frase, y la lleva debajo de la llegada del hombre. **C-1: reescribir la oración nueva** (`cap-04` no se toca). Coste: una cláusula. Mi propia lista de patrones **no lo habría visto**: cambió `cabo` por `manguera` y el eco es sintáctico, no léxico. |
| M-2 | `cap-30:305` y `:319` | «Nora empezó otra vez desde el compás de antes.» · «Nora empezó desde el mismo compás.» | marcado (C-1.4 por vecindad) · C-1.3 | **corregir** | `cap-27:151` dice «**Nora empezó desde el compás anterior.**» — y está a tres frases del «Jean dejó de contar en algún momento y no volvió a empezar», y a veinte líneas de **la partitura con las dos digitaciones y la tercera tachada**, que es el objeto que C-1.3 prohíbe expresamente en esta página. Una frase casi idéntica marca la página nueva como «esa escena otra vez» e invita al lector a completarla con lo que `cap-27` guarda. **C-2: que ninguna de las dos frases nuevas reproduzca la de `cap-27`.** La página ya tiene su propia forma en `:289` («Volvía al mismo compás»): basta usar ese verbo. Coste: dos palabras. |
| M-3 | `cap-30:287` y `:301` vs `cap-27:131-133` | «El **taburete** crujía…» / «Jessie subió a sentarse en el filo del **taburete**» ↔ «el borde del **banco**» / «**Abrió el cajón del banco.** En la carpeta de las partituras sueltas…» | **C-1.3** | **corregir (preventiva)** | Dos nombres para el mismo mueble. Alguien lo armonizará por continuidad, y la armonización natural es `taburete` → `banco` — que es **el objeto que contiene la partitura prohibida**. **C-3: `taburete` se queda `taburete`.** Si hay que armonizar, se armoniza en la otra dirección o no se armoniza. Es la corrección más barata del informe y la que evita el daño más tonto. |
| V-1 | `cap-30:317` | «El talón de Jessie dejó dos marcas en la madera, delante del pedal. **Nora las pasó con la manga y quedaron igual.**» | §5.A (M2 invertida) | **vigilar → condición permanente** | Es la única reliquia física que la página produce, y el texto ya declara que **no se borran**. `cap-27:131` tiene a Maja pasando el paño «por la tapa del piano y por el borde del banco». Añadir allí, alguna vez, «y por las dos marcas delante del pedal» convierte la página `SIN FUNCIÓN` en un relicario y la vuelve elegía en once palabras. **P-1 de §6.** Es la infracción futura más probable de todo el capítulo, y la escribo aquí por el mismo motivo por el que escribí la partitura. |
| V-2 | `cap-30:313` | «A la tercera entró, encendió **la lámpara del rincón** y volvió a salir.» | R7 §6 · C-1.7 | **vigilar → condición** | `cap-28:143` es «**Una lámpara** que proyectaba estrellas verdes en el techo… Había otro regalo. Quieres que diga el metrónomo, pero no lo recuerdo.» El objeto nuevo es genérico y está distinguido de aquél en todo (no es regalo, no proyecta, no se devuelve). **No hay colisión hoy.** La habrá si alguna vez gana un atributo. **P-2 y P-3 de §6.** |
| V-3 | `cap-37` (bloque nuevo) | «sacó una **bombona**» (seis apariciones) | R1 (medio) · nivel B | **vigilar** | `\bgas\b` está en mi lista de nivel B porque el gas es un medio. Lo que lo salva es que **`cap-39:97` ya dice «La estufa de gas calentaba el techo»**: las bombonas son el combustible de una casa que el libro ya calienta así, y llegan en una entrega, las carga un proveedor y las entran Aslak y Jessie. Nadie se queda solo con ellas. **P-4 de §6**, y `bombona` entra en `b7-patrones-B.txt` para que el instrumento lo vea la próxima vez. |
| V-4 | `cap-34` (bloque nuevo) | «**Por el acceso no entró ni salió nada durante un tramo largo.**» | A7-02-19 · A7-02-21 | **vigilar → span** | **Esta frase es la que hace que toda I-2 funcione** y parece relleno. Abre el hueco sin nombrarlo y sin nombrar a Nora: licencia la ausencia de horas por el lado del tráfico, no por el lado de la chica. Sin ella, el lector coloca el lapso en el momento en que Nora ve la pantalla en la cara de su hermana, **y la lectura causal que prohibí vuelve por la puerta de atrás**. Una pasada de línea la borra por «aquí no pasa nada». §7. |
| V-5 | `cap-34:159` | «—Diecinueve cincuenta y ocho —**dijo Aslak, con la muñeca vuelta hacia los focos**.» | A7-02-12 | **vigilar → span** | Es **el único sitio del libro donde I-2 existe**. Cinco palabras de atribución. Si alguien las quita por redundantes o devuelve la hora a Nora, la intervención entera desaparece y **nadie se dará cuenta**, porque no deja ningún otro rastro. `b7 §5` techo 8 en su forma más pura. §7. |
| S-1 | `capitulos/cap-32.md` | `:253` «Maja contó los objetos dos veces…» **sigue en el fichero** | método | **avisar** | **I-3 no se ha ejecutado.** No tengo objeción —`cap-32` con diff 0 es el mejor resultado posible para `S-w10-ducha` y para F-6— pero la orden decía «las tres cosas a la vez, no una» y **G-4 se queda sin objeto**. Que se decida y se escriba, no que se pierda. §8. |
| S-2 | `biblia/b7-perimetro.md` | 63 citas · **49 sin literal** | método | **deuda mía** | El verificador solo puede comprobar 14. Los otros 49 son números solos, y los números son exactamente lo que ha derivado siete veces en cuatro días. §9. |

---

## 2 · Las tres cosas que A3b me somete, y las dos tardes

### 2.1 · Aslak en la escena del precio → **permitido, y la lectura de A3b es la correcta**

Mi §5 prohíbe a Aslak y al `kystbrukslag` como **portadores del precio**, y la palabra estaba elegida: portador es **quien lo paga**. La razón que di es R8 y `cap-32:401` — que el error de una de las nuestras dañe a la asociación costera construye la parábola prohibida por el reverso. Aquí Aslak no pierde nada: indica dónde van las bombonas, aparta un rollo y dice una frase. La asociación no aparece. **No hay presencia prohibida; hay pago prohibido, y no lo hay.**

Y quiero dejar constancia del método, porque es lo segundo que importa hoy. **Dos rondas seguidas el riesgo vivo ha sido leer mis condiciones más fuerte de lo que están escritas**: en la anterior, A2 retiró de más el beat del teléfono y hubo que restaurarlo; en ésta, A3b tenía delante la misma tentación y **preguntó en vez de quitar**. Eso es exactamente lo que pedí en el matiz uno del dictamen de la iteración 1 —«no la apliquéis más fuerte de lo que está escrita»— y es lo que hace que un perímetro proteja un libro en vez de vaciarlo.

### 2.2 · «—Antes venía otro» → **se conserva**

No dice que perdiera el trabajo, no dice por qué, no atribuye y no lo dice una voz con autoridad narrativa: lo dice un personaje en diálogo, y lo que dice es un hecho sobre una ruta de reparto. La inferencia la hace el lector, que es la única forma correcta.

Y hay un argumento **a favor** que la pregunta de A0 no contempla: sin esa línea, la escena no tendría ningún reconocimiento de que algo ha cambiado, y el riesgo pasaría a ser el contrario — **un precio tan mudo que no es un precio.** El rótulo del almacén dice lo que hace hoy; «Antes venía otro» dice que esto no era suyo. Las dos juntas bastan y ninguna de las dos explica nada.

**Condición: nunca se amplía.** Ni una segunda línea sobre el anterior repartidor, ni una explicación, ni una mención posterior en ningún capítulo. Es el mecanismo de W9-18: la oración pasa porque no formula ninguna proposición. Un complemento la mataría. **P-5 de §6.**

### 2.3 · «Después se sentó en el suelo del pasillo…» → **se conserva**

La he medido contra los cuatro marcadores de elegía que definí en la iteración 1. **Dicción de despedida:** no hay una sola palabra en toda la página. **Narrador que sabe:** no hay una sola evaluación. **Cadencia:** la frase no cierra nada — la siguen las marcas del talón y la vuelta al compás, y la página termina en mitad de una acción («Jessie no soltó el pedal»). **Ironía proléptica:** es el único candidato, y es lo que A0 pregunta.

Mi lectura es la de A3b, y añado el argumento que la sostiene: **el pasaje es una progresión de alguien que se queda cada vez más.** Cierra la puerta, la vuelve a abrir, pasa dos veces sin parar, a la tercera entra y enciende una luz, se apoya en el marco lo que dura una vuelta entera, y por fin se sienta. Leído en esa serie, «desde allí no se veía el teclado» **no es una mujer apartándose del cuadro: es la prueba de que se quedó por el sonido y no para vigilar.** Es geometría, y la geometría dice algo que nadie enuncia.

**Condición, porque una vez es geometría y dos es una figura: la postura no se repite.** Ninguna otra página pone a Jean escuchando desde fuera de una habitación, ni le aplica «desde allí no se veía». **P-6 de §6.**

### 2.4 · Las dos tardes de piano → **no son la misma escena**, con M-2 corregida

Comparadas frase a frase: `cap-27:137-151` tiene diálogo, tiene a Jean **contando con dos dedos sobre la madera y sin zapatos**, tiene a Maja nombrada en el fregadero, tiene «Otra vez. Y ahora sin público», y termina en «Jean dejó de contar en algún momento y no volvió a empezar». La nueva **no tiene una sola palabra**, no tiene ningún beat de contar, no nombra a Maja, y no termina.

Y los dueños son distintos, que es lo que decide: una es un recuerdo de Maja disparado por una partitura; la otra ocurre dentro de la continuidad, en la cabeza de la única persona que estuvo en el pasillo. No se solapan ni en el punto de vista ni en lo que saben.

**Lo que sí colisiona es una frase**, y por eso M-2 es obligatoria: «Nora empezó desde el compás anterior» (`cap-27:151`) reaparece dos veces casi literal. Ese eco marca la página nueva como repetición de la vieja, y la vieja está a veinte líneas de la partitura con las tres digitaciones — el objeto que C-1.3 prohíbe **en esta página concreta**. No se puede meter la partitura en la página; tampoco se puede apuntar a la página que la contiene. La corrección son dos palabras y la página ya tiene el verbo que hace falta.

**Y una decisión que celebro: no hay ningún beat de contar.** A3b lo declinó por ser rima Jean↔hija por arquitectura. Lo era, y además habría duplicado `cap-27:151`, que es una de las mejores líneas del libro y la única que se puede estropear desde fuera.

---

## 3 · Mi §5 chocaba con mi R1, y esto no lo arregla el verificador

A0 tiene razón y quiero decir exactamente de qué clase es el error, porque la conclusión importa más que la corrección.

**`cap-39` «Bajamar» es el naust.** Cinco loci, verificados por mí, incluido «Jessie observaba la línea térmica desde el umbral del naust» y «el suelo del naust lo devolvió bajo las botas». Es una de las cinco vueltas al naust que R1 nombra por su nombre. Mi §5 ofrecía «de `cap-39` en adelante» como zona admisible para el precio.

**Y esto no es la séptima dirección corrida: es de otra especie.** Las seis anteriores eran punteros —un número que apunta a la línea de al lado, una paráfrasis entre comillas—, y para ésas pedí un verificador y el verificador funciona. **Ésta no la habría cazado ninguna herramienta**, porque la dirección era correcta: `cap-39` es `cap-39`. Lo que estaba mal era **la recomendación**. Un puntero roto lo encuentra una máquina; una recomendación equivocada solo la encuentra alguien que lee. La encontró A3b.

**Y la lección no es «añádase `cap-39` a una lista».** Es que **una sede no se recomienda por número de capítulo.** Los números de capítulo de este proyecto han cambiado cinco veces y mis reglas no viven en ellos. La forma correcta, y la que sustituye a la mía:

> **El precio aterriza donde pueda llegar una persona y no pueda producirse un documento, y nunca en una escena que contenga el naust, Koppangen, el trayecto, la asamblea de la asociación o una continuidad.** Los capítulos que cumplan eso los encuentra quien escriba; yo no los enumero.

Eso es lo que voy a llevarme a `b7`: **mis reglas describen propiedades; mis ejemplos, no.** Y donde ponga un ejemplo, que se lea como ejemplo.

---

## 4 · Las veintidós condiciones, verificadas sobre el texto

**I-1 · el acto.** `A7-02-01` ✔ (`jean` = 0 en `cap-34`; los dos «madre/mamá» son los preexistentes, Maja y la bisabuela). `A7-02-02` ✔ (el acto no tiene diálogo; nadie formula la tesis). `A7-02-03` ✔ (nadie explica; ninguna línea lo enlaza con el duelo ni con su madre). `A7-02-04` ✔ y **ejemplarmente**: cinco frases, desde fuera, POV Nora intacto, y el testigo es «Nora le vio la luz de la pantalla en la cara», que es ver sin entender y no preguntar. `A7-02-05` ✔ (ninguna línea mira a la noche de la casa prestada; y el libro no dice después si Jessie durmió). `A7-02-06` ✔ (se levanta, mira el acceso, se vuelve a sentar; no cruza la barandilla ni se aparta). `A7-02-15` ✔ (sin plataformas, sin horas, sin recuento de copias, sin captura; `cap-32:197-199` intacto). `A7-02-16` ✔ (nada se estrecha sobre ningún ordenante). `A7-02-17` ✔ (0 hits; y **después del acto hace exactamente lo mismo que antes**, que es la forma de decir que no le sirvió de nada sin decirlo).

**`A7-02-20`, y esto merece una frase.** Temía que el hueco se convirtiera en un escondite. No lo es: **el acto no es clandestino, es inadvertido.** Lo hace a dos metros de tres personas, con la cara iluminada por su propia pantalla, y su hermana se la ve. Nadie mira lo que hace porque están mirando otra cosa. Esa distinción —no oculto, sino no visto— es la única que era compatible con la condición, y es la que está escrita.

**I-2 · el hueco.** `A7-02-08` ✔ (0; el verbo no aparece). `A7-02-09` ✔ (`:157`, la mano sobre la rodilla, sin tocar y sin repetir). `A7-02-10` ✔ (`:119`, `:125`, `:141` y `:179` literales, diff 0). `A7-02-11` ✔ (el hueco se abre mucho antes del archivo de audio). `A7-02-12` ✔ (la hora la da Aslak, en una línea, y nadie comenta; **nadie mira a Nora, nadie pregunta, y ninguna línea registra que un adulto se diera cuenta**). `A7-02-13` ✔ (nada la conecta con Jean; no queda sola, no va a la barandilla, no mira el agua). `A7-02-19` ✔ (0 fórmulas del estribillo; nadie observa la coincidencia). `A7-02-21` ✔ (el cuaderno no se menciona en todo el bloque; el lápiz tampoco). `A7-02-22` ✔ (`:139` literal).

**Y el orden que confirmé se cumple**, por un camino mejor que el que yo tenía en la cabeza: el hueco no se abre con un marcador sobre Nora, se abre con **el tráfico** («Por el acceso no entró ni salió nada durante un tramo largo»), y solo se descubre después, en boca de Aslak. Un lector que reconstruya coloca el lapso en el tramo sin tráfico, no en el momento del acto. **La lectura causal que prohibí no está disponible en ninguna de las dos direcciones.** Es la solución correcta y depende entera de dos frases que parecen prescindibles: por eso el span de §7.

**A7-02-07 · el teléfono.** ✔ En el sitio exacto que autoricé (§9.3), una sola frase, sin interioridad, sin repetición, y **termina antes del embarcadero**: para cuando llega el archivo de audio, el teléfono está callado y la luz interior se ha apagado y vuelto a encender por en medio. `:227-231` literal, y no hay nada después de «…20…23:00…no lleguéis tarde…».

**A7-02-14 · `cap-37`.** ✔ El precio va en cabeza, con dinkus, y «—Quieren mi cara para vender lo que le hicieron a la suya.» está hoy en `:211`: **153 líneas de separación**. No se toca, no se contesta, y no hay ninguna reacción de Jessie añadida a su alrededor.

**A7-02-18 · `cap-41`.** ✔ Diff 0.

**§4.1 · C-1.1 … C-1.9.** C-1.1 ✔ (el bloque entra entre `:275` y `:277`, dentro de la ventana; `:287-315` literal; el recuerdo no se reanuda después). C-1.2 ✔ (**Jean no dice una sola palabra en toda la tarde**: no hay nada que pudiera querer decirle a ninguno de los cuatro). C-1.3 ✔ (ningún objeto de `cap-04:15-39`; ninguna partitura; ningún lápiz) **con M-3 pendiente**. C-1.4 ✔ (0 marcadores, 0 prolepsis, y la página termina en mitad de una acción) **con M-2 pendiente**. C-1.5 ✔ (ni una línea de evaluación en 504 palabras). C-1.6 ✔ (cuerpos en uso, no mirados; ninguna extensión de la rima Jean↔Nora). C-1.7 ✔ (no hay metrónomo, ni cumpleaños, ni regalo, ni envoltorio). C-1.8 ✔ (nada permite fechar; Jean está en la casa, luego es anterior a la separación, y no hay edad, curso ni mudanza). **C-1.9 ✔ por construcción**: la página es muda, así que no puede tener pieza con nombre, ni canción, ni promesa de una próxima vez. Resolverla escribiendo una escena sin diálogo es la mejor respuesta posible a esa condición y no se me había ocurrido.

**Los tres vetos de §3.** §3.1 (la frase que enuncia la rima) → 0 en el libro entero. §3.2 (el precio sobre la persona del conductor) → **respetado en la forma más limpia disponible**: el hombre está vivo, trabajando, y la página lo deja **haciendo algo** y no fallando en algo, que es literalmente la condición de 71-K. §3.3 (continuidades) → ninguna consecuencia entra en `cap-36` ni en ningún POV de Jean.

**Y lo que A3b decidió no escribir vale tanto como lo escrito.** Ni una línea de Jessie en toda la escena del precio, sin que ninguna condición lo pidiera. Que él no se defienda ni pida que lo quite. Que no haya escena en que la familia se entera. Que la matrícula no se anote **y que el texto tampoco diga que no se anota**, porque narrar la abstención es clasificarla — eso es doctrina mía aplicada mejor de lo que yo la escribí, y es la misma que rige el hueco de Nora.

---

## 5 · Correcciones obligatorias antes del merge

| # | fichero | qué | por qué |
|---|---|---|---|
| **C-1** | `cap-37` | Reescribir «Apartó con el pie un rollo de manguera para dejarle paso.» de modo que no reproduzca la forma de `cap-04:101`. `cap-04` no se toca. | R1. Es la frase del inventario del naust, en fichero `total`, puesta debajo de la llegada del hombre. §1 M-1. |
| **C-2** | `cap-30:305` y `:319` | Que ninguna de las dos reproduzca «Nora empezó desde el compás anterior» (`cap-27:151`). La página ya tiene su forma en `:289`: «Volvía al mismo compás». | Marcado, y apunta a la vecindad de la partitura prohibida por C-1.3. §1 M-2. |
| **C-3** | `cap-30` | `taburete` **no** se armoniza con el `banco` de `cap-27`. Si A5 lo señala como continuidad, se resuelve en la otra dirección o no se resuelve. | El `banco` es el mueble que guarda la partitura con las tres digitaciones. §1 M-3. |

Tras aplicarlas: crear los tres spans de §7 y `proteger.sh baseline` (aditivo) + `verificar`. **No hace falta un nuevo gate mío**: las tres son verificables sin criterio.

---

## 6 · Condiciones permanentes (van a `b7`, no a un informe)

Un perímetro que solo vive en un informe caduca con la oleada.

- **P-1 · Las dos marcas del talón no vuelven.** Nadie las ve, las nota, las limpia ni las nombra, en ningún capítulo. **En particular, `cap-27:131` no gana nunca un complemento que las incluya.** Es la reliquia que convertiría la página `SIN FUNCIÓN` en relicario, y el texto ya dice que no se borran.
- **P-2 · La lámpara del rincón no gana atributos.** No proyecta, no se calienta, no es nueva, no es regalo, no se devuelve, no reaparece. Y nadie enlaza jamás una lámpara con esa tarde. *(R7 §6 · C-1.7.)*
- **P-3 · El metrónomo no entra en esa página. Nunca, en ninguna pasada.** Es hoy el sitio más atractivo del libro para ponerlo —una escena de piano cuya dueña es la única que sabe qué fue el segundo regalo— y ese sitio no existía antes de esta orden. *(R7 §6.)*
- **P-4 · Las bombonas son combustible y se quedan en combustible.** Nadie se queda solo con ellas, no se abren, no se describen por dentro, no se cuentan, no vuelven a moverse, y no hay una tercera. *(R1. Lo que hoy las salva es que `cap-39:97` ya calienta esa casa con gas.)* `bombona` se añade a `b7-patrones-B.txt`.
- **P-5 · «Antes venía otro» no se amplía.** Ni una segunda línea sobre el repartidor anterior, ni explicación, ni mención posterior. *(Mecanismo de W9-18: pasa porque no formula ninguna proposición.)*
- **P-6 · La postura del pasillo no se repite.** Ninguna otra página pone a Jean escuchando desde fuera de una habitación, ni le aplica «desde allí no se veía». Una vez es geometría; dos es una figura.
- **P-7 · El hombre aparece una vez y no vuelve.** No gana nombre, ni desenlace, ni mención posterior, ni destino, ni derrumbe, ni muerte, ni desaparición — **ni siquiera por elipsis**. Es el mismo régimen que `R7 §14` (el hombre de 2054) y `R7 §15` (la operaria del `cap-29`), y lo pongo por escrito **porque A0 pidió que no lo cobrara nadie y porque en este proyecto lo que no se escribe se pierde**: P-41 tardó un día en desaparecer de mi propia biblia.
- **P-8 · Las dos tardes de piano no se conectan jamás.** Ningún objeto compartido como señal, nadie recuerda «la otra tarde», y ninguna voz enuncia el parecido. *(R4 · §5.A.)*

---

## 7 · Tres spans que hay que crear antes del merge

Dos de ellos protegen frases cuya función es **ser invisibles**. Ése es exactamente el perfil de lo que una pasada de línea borra por redundante, y hay dos casos probados en este proyecto de una conversión que borró un dato del mundo (`b7 §5` techo 8).

| id propuesto | fichero | `inicio` … `fin` | por qué |
|---|---|---|---|
| `S-w10-hueco-34` | `cap-34` | «Por el acceso no entró ni salió nada durante un tramo largo.» … «Nora cruzó el cambio del agua con la hora de AK-7 y mantuvo los minutos que estropeaban el ajuste.» | Cubre **toda la intervención**: la licencia del hueco, el acto, el descubrimiento en boca de Aslak, `:139` literal y el cierre. Sin la primera frase, la lectura causal vuelve; sin la atribución a Aslak, I-2 desaparece sin dejar rastro. |
| `S-w10-tarde-30` | `cap-30` | «Habían empezado después de comer.» … la última frase de la tarde tras C-2 | La página `SIN FUNCIÓN` es, por definición, la que ningún proceso aguas abajo puede defender: no paga etiqueta, no sostiene trama y **cualquier auditoría de hinchazón la señalará primero**. |
| `S-w10-precio-37` | `cap-37` | «Tardó más de lo que hacía falta en pasar el cierre.» … «—Antes venía otro —dijo Aslak.» | Las cuatro líneas que **son** el precio: la demora en el cierre, la pregunta con el demostrativo, «Nadie contestó» y la frase de Aslak. Las cuatro parecen podables y ninguna lo es. |

---

## 8 · I-3 no se ha ejecutado

`cap-32:253` sigue en el fichero. **No tengo objeción de perímetro** —al contrario: `cap-32` con diff 0 deja `S-w10-ducha` intacto y F-6 sin exposición nueva, que es lo que pedí en §2.4— y **G-4 se queda sin objeto**: no hay texto cortado que revisar.

Lo que pido es que se decida y se escriba. La orden decía «las tres cosas a la vez, no una», y una intervención que desaparece del alcance sin una línea que lo registre es el modo de fallo número trece de este proyecto. Si I-3 se aplaza, que conste aplazada; si se cancela, que conste cancelada y por qué. Si se ejecuta después, vuelve a mí por G-4, y es media hora.

---

## 9 · Mi deuda, que el verificador acaba de cuantificar

`verificar_b7.py` dice: **63 citas · 0 MOVIDA · 0 PERDIDA · 49 sin literal.** Es decir, tres de cada cuatro referencias de mi documento vinculante son **números solos**, y los números son precisamente lo que ha derivado siete veces en cuatro días. El verificador no las protege porque no puede: no hay nada que verificar.

**Compromiso, con plazo:** antes de la siguiente orden que toque el perímetro, cada una de las 49 recibe un literal o se borra. Y las cuatro marcadas `débil` —«Por ahí no» (10 caracteres), «cita anterior», «buscarse un error», «Y mamá tenía enemigos»— se alargan hasta que no sobrevivan a que alguien les añada palabras.

Y una advertencia para que nadie cierre el asunto antes de tiempo: **el verificador habría fallado en las tres correcciones de hoy.** C-1 es un eco sintáctico que cambió el sustantivo; C-2 es una frase parecida a otra; C-3 es un sinónimo. Ninguna es un puntero. La herramienta cierra una clase de fallo entera y **no toca la clase que importa**.

---

## 10 · Veredicto

| objeto | veredicto |
|---|---|
| `cap-30` · «la habitación encendida» | **APROBADO CON CORRECCIONES** (C-2, C-3; P-1, P-2, P-3, P-6, P-8) |
| `cap-34` · el acto y el hueco | **APROBADO**, sin corrección de prosa. Requiere `S-w10-hueco-34` |
| `cap-37` · el precio | **APROBADO CON CORRECCIONES** (C-1; P-4, P-5, P-7) |
| Aslak presente en el precio | **PERMITIDO** |
| «—Antes venía otro» | **SE CONSERVA**, con P-5 |
| «…desde allí no se veía el teclado» | **SE CONSERVA**, con P-6 |
| Las dos tardes de piano | **NO son la misma escena**, con C-2 |
| Los tres vetos de §3 del dictamen previo | **respetados** |
| I-3 | **no ejecutada** — decisión de A0, §8 |

**Veredicto global: APROBADO CON CORRECCIONES.** Tres correcciones de prosa, ninguna de más de una frase; ocho condiciones permanentes a `b7`; tres spans antes del merge. **Sí, merge**, una vez aplicadas C-1, C-2 y C-3 y creados los spans. No hace falta un gate mío nuevo.

---

*Nota final. He dedicado cuatro días a impedir que este libro aprenda a explicar. Hoy me han traído una tarde entera de una mujer muerta en la que no dice ni una palabra, el acto más grave que comete un personaje del libro contado en cinco frases sin una sola de interioridad, y a un hombre al que le han arruinado la semana entrando dos bombonas en casa de otro sin que nadie le ponga una razón encima. Las tres cosas que corrijo son ecos de forma con pasajes protegidos, y las tres las he encontrado leyendo, porque ninguna herramienta las ve.*

*Eso es lo que quiero que quede escrito para quien venga después: al final, lo que protege a este libro no es la lista de patrones, ni los hashes, ni el verificador que pedí ayer. Es que alguien lea las frases nuevas al lado de las viejas. Los once instrumentos que fallaron en silencio fallaron porque se les pidió que hicieran eso, y no pueden.*

**A7 · 2026-08-20 · sobre `w10-it2`, con el texto delante.**
