# W10 · Iteración 0 · Ángulo 3 — **El corte**

**A2 arquitecto. Insumo único: `compilado/ad-aeternum-vF.md`, leído entero.**
No he abierto ningún informe de crítica ni `informes/w10/estado.json`. Vinculante consultado: `plan-w10.md` §4b y `biblia/b7-perimetro.md`.

**Recuento propio del compilado** (cuerpo de los 48 capítulos, sin paratextos ni cabeceras de parte): **80.459 palabras**. Uso esta cifra, no la del encabezado del encargo, y todos los porcentajes salen de ella.

---

## 0 · Veredicto, primero

**El libro de 65.000 palabras no existe dentro de éste. Puedo demostrarlo y la demostración es aritmética, no de gusto.**

Hay **4.700 palabras de corte que se defienden por función** — un 5,8 %. A partir de ahí, para llegar a 15.000 hay que quitar otras 10.300, y solo pueden salir de un sitio: los **siete capítulos que no avanzan la trama**. Esos siete son, exactamente, las siete salvaguardas del libro. Suman 11.136 palabras y su lista es esta:

| Cap. | Título | Palabras | Qué impide que ocurra |
|---:|---|---:|---|
| 26 | Auditoría | 1.826 | que la reclamación de Jean sea un acto de fe |
| 35 | La poda | 1.428 | que la victoria del clímax sea gratuita |
| 45 | Depósito | 1.696 | que el libro acabe en triunfo |
| 47 | Acta | 1.459 | que el libro sea una parábola sobre una sola injusticia (R8) |
| 27 | Inventario | 1.737 | que la Parte III sea diez capítulos de expediente sin duelo |
| 17 | El salero | 1.096 | que la traición de Alana no cueste nada |
| 11 | La primera cita (resto) | 1.894 | el milagro terapéutico (R5) |
| | **Total** | **11.136** | |

**No es casualidad que la aritmética caiga ahí.** Un corte por longitud busca lo que no mueve la trama; en este libro, lo que no mueve la trama es lo que impide siete fallos concretos. El libro de 65.000 palabras es un thriller de datos competente al que le han quitado el duelo, la amistad, la ley, el coste y la otra injusticia. Se lee más rápido y no es esta novela.

**Lo que sí recomiendo hacer** está en §2: 4.700 palabras, ocho cortes, cinco de ellos por duplicación funcional literal. Y un hallazgo de §4 que creo que vale más que el corte entero.

---

## 1 · El hecho estructural que gobierna la respuesta

El libro tiene **cinco hilos que convergen en un solo minuto** (12:46:50, cap. 41). Para que la convergencia funcione, cada hilo llega al minuto con un personaje conocido, una capacidad que el lector ha visto adquirir y una razón para arriesgarla.

| Hilo | Llega | Capacidad | Sembrada en | Andamiaje |
|---|---|---|---|---:|
| Agua | Maja + Aslak | AK-7, barca, red | 19, 22, 32, 39 | ~5.000 |
| Puerta | Jessie + Tomas | llave de Gunnar, INC-441 | 14, 22, 29, 37, 40 | ~5.500 |
| Cabina | Nora | acreditación, la escala | 12, 18, 21, 24, 33, 40 | ~6.000 |
| Dentro | Jean | testimonio votado, margen | 15, 25, 30, 36 | ~6.500 |
| Acta | Astrid | acta preparada, custodia | 22, 26, 35 | ~4.500 |

**~27.500 palabras de andamiaje, un 34 % del libro.** Ninguna pieza es prescindible porque el clímax las usa **todas a la vez y en tres minutos**. Ese es el precio de un clímax convergente de cinco piezas, y es la razón real de que el centro pese.

**Corolario que hay que decir en voz alta:** el libro no es largo. Es un libro de 80.000 palabras cuyo clímax exige cinco preparaciones. Quitarle 15.000 no lo acorta: lo deja **incompleto**, porque el clímax sigue pidiendo cinco piezas y una de ellas ya no está sembrada.

---

## 2 · La lista de cortes que sí se defienden

Ocho cortes. Cinco son duplicación funcional verificada por grep. **4.700 palabras, 5,8 %.**

### C1 · Capítulo 8 «Turno» entero, con un trasplante — **1.589 netas**

**Bloque:** `capitulos/cap-08.md`, capítulo entero.
> primera: «Una silla en un portal ocupa el centro.»
> última: «—Nora. Jessie. Maja. Alana.»
> **1.835 palabras.**

**Función que cumplía:** que el lector sienta el volumen del trabajo de Jean y su coste moral; instalar «un turno = 10.000 imágenes»; instalar la letanía de los cuatro nombres.

**Dónde se recupera — las tres, ya, antes y después:**
- El volumen y el coste moral: cap. 7 «Lote rojo» (el accidente, el arma, la muchacha del cordón que Jean confunde con Jessie) y cap. 9 «Milisegundos» (los sesenta contra los noventa grados: «A sesenta grados, alguien tiene que bajarle los platos del estante»).
- «Lo que no se entrega, se infiere»: ya está literal en el cap. 7 — «Su silencio sale clasificado como REVISAR.»
- La letanía: cap. 7, línea 1333, «Nora. Jessie. Maja. Alana.» **Solo hay dos instancias en todo el libro y las dos están en 7 y 8.**
- El eco Jean↔Nora↔piano: ya lo hace el cap. 9 — «El cuarto dedo de la derecha caía tarde. Otra vez, más despacio».

**Verificación de que no siembra nada:** `zueco`, `andador`, `cuartilla`, `escurridor`, `yeso`, `polvo de la manga` — **cero apariciones fuera del capítulo 8.** Al terminar el 8, Jean sabe exactamente lo que sabía al terminar el 7, y el 9 no necesita nada de él.

**Qué se pierde, y es real:** el mejor caso del libro sobre «tu trabajo llega a alguien y nunca sabrás qué pasó».
> «Una habitación con la puerta abierta y la luz del pasillo entrando en diagonal.» … «El campo no guarda nada de él. Ni el andador, ni la cuartilla, ni el zueco.» — **368 palabras.**

**Recuperación propuesta:** trasplantar ese bloque de 368 al cap. 7, **sustituyendo** la secuencia genérica del lote rojo:
> «Entonces aparece el rojo.» … «—Tiempo de decisión dentro del rango óptimo.» — **122 palabras.**

Ahorro neto: 1.835 − 368 + 122 = **1.589**.

**Aviso de honestidad:** el cap. 8 es material de `REVISIÓN 10`. Mi corte mayor cae sobre lo que este proceso añadió.

---

### C2 · Capítulo 34, la vigilancia del mirador y el regreso — **971**

**Bloque:** `capitulos/cap-34.md`, desde el segundo dinkus.
> primera: «Aslak las esperaba junto a la barandilla, con los prismáticos colgados por dentro de la chaqueta para resguardar las lentes.»
> última: «…20…23:00…no lleguéis tarde…»
> **1.051 palabras.** Sutura estimada en el 37: 80. Neto **971**.

**Funciones y dónde se recuperan:**
1. *La vigilancia es aburrida y no produce nada.* Ya lo hacen el 26 (Astrid contando puertas y esperando seis minutos por una credencial), el 29 (Tomas midiendo desde cada base), el 39 (nueve minutos junto al transductor en los que «solo cambiaron las cifras pequeñas»). **Cuádruple.**
2. *La fecha 20-ene 23:00.* La da Astrid explícita en el 35 y Jean en el 37. **Triple.**
3. *Han hecho reconocimiento del sitio.* Se recupera con una oración en el 37.

**Qué se pierde:** «Ellas también formaban parte del tráfico que alguien podía aprenderse.» Es la mejor línea del bloque y no tiene sitio en otra parte. **Lo cuento como pérdida neta.**

**Se conserva íntegro** el primer tramo del capítulo (ferry, Jessie y el gofre, la lección de leer la costura, la cajera de Svensby, «—Por ahí no —dijo Maja»): 619 palabras que el perímetro protege por su nombre (R1, el trayecto no crece; «Por ahí no» es el techo) y que cuelgan sin problema del final del 32 o de la apertura del 37.

---

### C3 · Capítulo 19, la mesa de las tres columnas — **312**

**Bloque:** `capitulos/cap-19.md`.
> primera: «Nora dejó los horarios en el margen del cuaderno pautado. Maja atravesó el sobre encima.»
> última: «—Entonces no os equivoquéis.»
> **312 palabras.**

**Función:** la familia pone documentos sobre una mesa y descubre que no dicen nada; y Maja enseña a no atribuir lo que no se puede probar («—Borra UNN de la primera columna»).

**Dónde se recupera:** la escena de la mesa existe **cuatro veces**: aquí, en el 22 («Leyeron el informe a tres voces porque los huecos cambiaban el sentido de cada frase» … «Ningún nombre»), en el 31 dos veces (Jessie con la notificación; «Sobre la mesa de la cocina, Maja puso los tres papeles en fila»). La del 31 es la mejor con diferencia: *tres formatos, tres tipos de letra, un solo día*.
La lección de no atribuir existe **tres veces**: aquí, en el 22 («—He dicho "era ella". Me he adelantado.») y en el 26 («—Los relojes no comparten sincronización acreditada. Retira el intervalo.»). La del 26 es la mejor del libro: Nora borra la flecha ella misma, sin defenderla, y queda la franja gris entre los pentagramas.

**Se conserva** desde «A medianoche, ya 14 de diciembre…», que siembra el cambio de terminales y por tanto Fyret.

**Qué se pierde:** un momento de Maja como profesional del dato. Se compensa: el capítulo sigue teniendo AK-7 cuatro párrafos más abajo.

---

### C4 · Fusión de los capítulos 37 y 39 — **839**

Dos bloques del `capitulos/cap-39.md`:

**C4a — la negociación repetida:**
> primera: «—Quítatelo.»
> última: «—Ven al naust. Lleva la llave.»
> **513 palabras.**

**C4b — las condiciones de aborto:**
> primera: «Aslak dejó en la mesa una hoja plastificada. Había marcado tres horas, dos direcciones de corriente y una franja tachada junto al cambio de marea.»
> última: «Jessie se metió las manos en los bolsillos para comprobar el peso de cada objeto. Esta vez Maja no le pidió que los sacara.»
> **446 palabras.** Reposición de la condición de aborto, una sola vez, en el 37: ~120. Neto de los dos: **839**.

**Función y duplicación:** la discusión «tú no entras / no te lo estoy preguntando» ocurre **tres veces** — 37 (líneas 9102-9105 y 9218-9222), 39 (C4a), 41 (implícita en «—A mi alcance»). Las condiciones de aborto de Aslak se enuncian **tres veces** — 37 («Si el hielo impide trabajar, la corriente vira o el ADCP desmiente la tabla, recojo»), 39 (C4b), 41 (se cumplen). Fundidos, el «—¿Quieres vivir?» / «—Quiero poder elegir. Es la primera vez.» deja de estar a dos capítulos del acto.

**Se conserva íntegro** el cierre del 39, que es una de las mejores cosas del libro y no se repite en ninguna parte: la marea bajando, los nueve minutos, y la consolidación vista desde una tableta en un cobertizo —
> «La madera húmeda crujió bajo sus botas.» … «En la tableta, el quinto hueco no volvió a abrirse.» — 366 palabras.

**Qué se pierde:** el trabajo manual de Jessie con la cinta de vulcanizar y la presilla cosida al forro, que es la mejor caracterización física que tiene el personaje. **Pérdida neta y me duele.**

**Condición de perímetro:** R1 prohíbe que una vuelta al naust *añada* un objeto. Quitar está permitido; pero al comprimir, los objetos restantes ganan peso relativo. **La fusión no puede acercar ningún objeto del naust al 26-nov, al trayecto ni a Koppangen.**

---

### C5 · Capítulo 18, la escena de Madre y la de Cuchillo — **414**

Dos bloques de `capitulos/cap-18.md`:

**C5a:** «Una alumna falla por segunda vez en el mismo intervalo.» … «Jean conserva otra tentativa, no una prueba de identidad.» — **188 palabras.**
**C5b:** «Cuchillo ocupa una apelación de moderación.» … «La decisión principal de la apelación cruza. La amenaza permanece dentro de la tarea y el contacto se extingue con la siguiente asignación.» — **226 palabras.**

**Duplicación verificada:**
- *Madre devuelve un ejercicio al punto de fallo* ocurre **tres veces**: cap. 15 (líneas 3436-3477, con el recuerdo de Nora y el vaso de leche sobre el piano), aquí, y cap. 30 (líneas 7370-7387). La del 15 es la buena porque lleva el ancla exterior.
- *Cuchillo quiere dañar a Armstrong y Jean lo contiene* ocurre **cuatro veces**: cap. 15, aquí, cap. 21 y cap. 42. La del 21 es la que cuenta («—Ya la utilizaste.» / «—Sí.») y la del 42 es el clímax del hilo.

**Se conserva intacto** todo lo que hace el 18 y nada más hace: FLOR / CANELA / CARIES en el campo secundario, la retención de la cuarta palabra —**«la cuarta enseñaría el orden», línea 4317, protegida por R2 y anterior al primer bloque cortado**—, el `NO` de 71-K, la resolución de R-1189, la sanción y el blanco.

**Qué se pierde:** que Madre y Cuchillo tengan tres apariciones en vez de dos. El coste real es de textura, no de trama.

---

### C6 · Capítulo 40, la discusión de Henrik y la foto, a la mitad — **215**

**Bloque:** `capitulos/cap-40.md`.
> primera: «A las diez y veintisiete, Henrik Dahl detuvo el vídeo sobre una fotografía de Jean junto al piano de la casa de Tromsøya.»
> última: «Alana comprobó la lista de participantes con la excusa de revisar el orden. Nora seguía después del vídeo y antes de la apertura técnica de la demo. El canal asignado continuaba habilitado.»
> **425 palabras → 210.** Ahorro **215**.

**Duplicación:** *Armstrong se apropia de la imagen de Jean y Alana protesta sin poder* ocurre **tres veces**: cap. 26 (Dahl ensayando la dedicatoria en el pasillo, a ocho metros de la celda donde Astrid mira las once filas), cap. 33, aquí. Y la propia apropiación se ejecuta en el 43 con la misma foto y el mismo crédito falso.

**Se conserva obligatoriamente:** el crédito «CEDIDA POR LA FAMILIA», la ficha `HIJA · PIANISTA · HISTORIA HUMANA` y la línea de que el acceso de Nora sigue habilitado — sin ellos el 43 no funciona.

> **⚠ Gate de sensibilidad, y es el aviso más importante de este documento.** W9-20 declara que la ausencia de interioridad de Henrik Dahl es un dispositivo, no un descuido: «Preferencia sí; razón, herida, precio, duda o cansancio, nunca». **Este corte se ejecuta por eliminación de réplicas, jamás por resumen narrativizado.** La forma barata de recortar un diálogo es sustituirlo por «Henrik, incómodo, aceptó» — y eso es exactamente la línea que se retiró y no vuelve. **Disparador A7.**

---

### C7 · Capítulo 25, la primera mitad — **180**

**Bloque:** `capitulos/cap-25.md`, de «Jean consulta la salida educativa y recibe `EN MANTENIMIENTO`.» hasta «`ACEPTADA`» — 364 palabras → ~185.

**Duplicación literal:** el par `CEDER ESTADO A CORO` / `CONSERVAR ESTADO LOCAL` aparece **dos veces con la misma deliberación y el mismo desenlace**: cap. 15 (líneas 3686-3708) y aquí (6123-6151). El grep lo confirma. La del 15 es la primera y por tanto la que enseña la regla.

**Se conserva íntegro** lo que solo hace el 25: la playa de Telegrafbukta construida y sostenida por alguien («Las dos costas acaban en puntos distintos. Jean se queda donde no coinciden.»), el préstamo de margen de Nieve, y la tesis de Coro:
> «—¿Qué queréis?» / «—Ser inevitables.»

---

### C8 · Capítulo 11, la logística escolar de Maja — **177**

**Bloque:** `capitulos/cap-11.md`.
> primera: «Maja repasó lo que quedaba de semana. El lunes trabajaba.»
> última: «—Eso lo deciden ellas.»
> **177 palabras.**

**Función:** que Maja también reciba atención de Ranveig sin admitirlo.

> **⚠ El corte más discutible del paquete y el único que debe pasar por A7 antes de tocarse.** R5 declara este capítulo *el modelo del libro* y su techo. Mi bloque es posterior a C1 (`—Entonces yo no la conozco`, línea 2395, cuenta cerrada) y no lo toca. Pero si A7 lo objeta, **se cae y no se discute**: 177 palabras no valen una discusión con el perímetro.

---

### Recuento

| # | Corte | Palabras | Parte |
|---|---|---:|---|
| C1 | Cap. 8 entero, con trasplante al 7 | 1.589 | I |
| C2 | Cap. 34, mirador y regreso | 971 | III |
| C3 | Cap. 19, las tres columnas | 312 | II |
| C4 | Fusión 37+39 | 839 | IV |
| C5 | Cap. 18, Madre y Cuchillo | 414 | II |
| C6 | Cap. 40, Henrik a la mitad | 215 | IV |
| C7 | Cap. 25, primera mitad | 180 | III |
| C8 | Cap. 11, logística | 177 | I |
| | **Total** | **4.697** | **5,8 %** |

Manuscrito resultante: **75.762 palabras, 47 capítulos.**

**Ninguno de los ocho bloques toca una cuenta cerrada.** Verificado línea a línea: C1 cinturón (4: líneas 678, 2080, 7034, 11199) · C2 bolsa de viaje (2: 676, 6585) · C3 «a la altura de los ojos» (2: 694, 3424) · C4 pluralidad del porqué (2: 1952, 2395). Todas fuera de los bloques.

---

## 3 · Qué se pierde, en conjunto

Cinco cosas, y las digo sin adorno:

1. **Una imagen irrecuperable:** «Ellas también formaban parte del tráfico que alguien podía aprenderse.» (C2)
2. **La mejor caracterización física de Jessie:** la cinta de vulcanizar, la presilla cosida al forro, las uñas cortadas al ras. (C4) Sobrevive el gesto —conserva la llave y el aborto— pero no las manos.
3. **Un tercio del tiempo que el lector pasa dentro de Jean en la Parte I.** El hilo de Jean-dentro baja de 6.329 a 4.740 palabras en la Parte I. Es el hilo que sostiene `duelo` en 9,5. **Riesgo real de C1, y es el motivo por el que el trasplante del hombre caído al cap. 7 no es opcional: es la condición del corte.**
4. **La sensación de que la vigilancia dura.** Después de C2 quedan tres escenas de esperar en vez de cuatro. Si el libro pierde algo con esto, lo pierde en «mundo», no en «ritmo».
5. **Textura del coro de continuidades:** Madre y Cuchillo con dos apariciones en vez de tres. (C5)

**Y lo que no se pierde y hay que decir que no se pierde**, porque son los cuatro capítulos que un corte por densidad se llevaría primero y que un corte por función tiene que **proteger activamente**:

- **Cap. 27 «Inventario»** (1.737). No mueve la trama. Es el único capítulo de la Parte III donde alguien hace duelo sin instrumento. Sin él, la Parte III son diez capítulos seguidos de expedientes. **Declino cortarlo y pido que se declare protegido durante W10.**
- **Cap. 17 «El salero»** (1.096). No mueve la trama. Es lo único que hace que la traición de Alana cueste algo.
- **Cap. 47 «Acta»** (1.459). No mueve el desenlace de Jean. Es el único lugar del último tercio donde la cámara sale de la órbita de Jean, y donde vive la línea que impide la parábola: «—Nos han escuchado por lo de Armstrong.» / «—Eso no está en el sobre.»
- **Cap. 45 «Depósito»** (1.696). El libro sin él termina en victoria. «—Cada uno de ustedes puede impedir algo. Sigo buscando quién puede hacerlo.»

---

## 4 · El hallazgo que creo que vale más que el corte

Mientras medía encontré esto, y no es una propuesta de longitud: es una medición de forma.

### 4.1 · El libro es un metrónomo

| Parte | Palabras | Caps | Media/cap |
|---|---:|---:|---:|
| I. Mørketid | 20.002 | 12 | 1.667 |
| II. Fije la vista | 20.461 | 12 | 1.705 |
| III. Propiedad intelectual | 20.316 | 12 | 1.693 |
| IV. Soldagen | 19.680 | 12 | 1.640 |

Cuatro partes con **459 palabras de diferencia entre la mayor y la menor** (2,3 %) y capítulos de longitud prácticamente idéntica de principio a fin. Capítulos 1-6: media 1.676. Capítulos 43-48 —clímax, desenlace, coda—: media 1.545. **El libro acelera un 8 %.**

Un clímax en el 87 % con la misma cadencia de capítulo que la exposición. Esto es una propiedad medible del objeto, no una impresión.

### 4.2 · El libro reparte su espacio al revés de sus puntuaciones

| Hilo | Caps | Palabras | Media/cap |
|---|---:|---:|---:|
| Jean (dentro) | 12 | 17.114 | **1.426** |
| Jean (viva) | 5 | 7.190 | **1.438** |
| Familia | 19 | 33.264 | 1.751 |
| Institucional | 11 | 20.647 | **1.877** |

**Los capítulos de Jean son un 24 % más cortos que los institucionales.** El POV que sostiene `duelo` y `tema` en 9,5 tiene los capítulos más breves del libro; el POV procedimental, los más largos.

Y el reparto se degrada según avanza:

| Parte | Jean (dentro+viva) | Institucional |
|---|---:|---:|
| I | 12.423 (**62 %**) | 0 (0 %) |
| II | 5.155 (25 %) | 6.417 (31 %) |
| III | 4.106 (20 %) | 6.993 (34 %) |
| IV | 2.620 (**13 %**) | 7.237 (**37 %**) |

**El libro empieza siendo la historia de Jean y termina siendo la historia del procedimiento en torno a Jean.** La proporción del POV con las puntuaciones altas cae del 62 % al 13 % justo donde se miden estructura y ritmo.

### 4.3 · Lo que esto implica, y es contrario a lo que yo mismo vine a proponer

**Si se quiere mover `ritmo` con longitud, la palanca no es cortar el centro: es romper la uniformidad.** Y —dato que descarta una vía entera— **no se puede hacer cortando la cola**: la Parte IV es la parte más eficiente del libro. Fuera de C4 y C6 no encuentro en ella 400 palabras que se defiendan como cortables. La rampa hay que hacerla **partiendo capítulos** en la Parte IV y **redistribuyendo peso hacia Jean**, no adelgazando.

Formulado como hipótesis medible para el bucle de §4, que es lo que se me pide entregar:

> **H-3.** El eje `ritmo` no responde al volumen total sino a la **derivada de la longitud de capítulo**. Intervención: partir los cuatro capítulos más largos de la Parte IV (40 · 2.312, 43 · 2.244, 41 · 1.849, 38 · 1.770) en unidades de 900-1.200, sin quitar una palabra, hasta que la Parte IV tenga 16 capítulos de media 1.230 frente a los 12 de media 1.667 de la Parte I. Coste: cero palabras, cero prosa nueva, `git revert` limpio. Predicción: si `ritmo` no se mueve más allá de ±0,5, **el volumen no es la variable y toda la familia de intervenciones de longitud queda cerrada para W10.**

Es barata, es falsable y contradice mi propio ángulo. Por eso la dejo escrita.

---

## 5 · Dos avisos operativos que encontré por el camino

**A · La correspondencia de ficheros del perímetro está obsoleta y eso es peligroso.**
`biblia/b7-perimetro.md` §2 afirma: «La renumeración de W7 puso los capítulos en 1–48. **Los ficheros no se renombraron.**» Ya no es cierto: `capitulos/` contiene hoy `cap-01.md … cap-48.md` en correspondencia 1:1 con el número de capítulo, y `cap-n1 … cap-n7` no existen. Ejemplo comprobado: R1 lista `cap-33` entre las vueltas al naust; según la tabla del perímetro eso es el capítulo 39 «Bajamar» (correcto), pero **`capitulos/cap-33.md` es hoy el capítulo 33 «Apartada», que transcurre en un despacho de Fyret.** Cualquiera que aplique el perímetro por número de fichero apuntará al capítulo equivocado en 40 de 48 casos. **Manda la cita literal, como el propio documento advierte — pero la tabla §2 debe corregirse antes de que nadie más la use.**

**B · Mi corte mayor cae sobre material del propio proceso.** De los siete capítulos con `origen: REVISIÓN 10` (8, 11, 17, 20, 27, 31, 47 — 12.119 palabras), propongo eliminar uno entero (8) y recortar 177 palabras de otro (11). Los otros cinco los defiendo explícitamente contra el corte: **17, 27 y 47 son tres de las siete salvaguardas de §0, y 20 y 31 son insustituibles.** Es decir: cinco de los siete capítulos añadidos por este proceso están hoy entre lo que menos se puede quitar. No es un resultado que yo esperara al empezar a medir.

---

## 6 · Respuesta a las cuatro preguntas del encargo

**1. La lista de cortes.** §2. Ocho bloques, 4.697 palabras, cada uno con cita literal de primera y última frase y recuento verificado.

**2. La función de cada uno y dónde se recupera.** §2, por corte. Cinco de los ocho son duplicación funcional verificada por grep (letanía de los cuatro nombres 2/2 en caps. 7-8; `CEDER/CONSERVAR` 2/2 en 15 y 25; Madre 3 veces; Cuchillo 4 veces; la mesa de documentos 4 veces; la lección de no atribuir 3 veces; la negociación «tú no entras» 3 veces).

**3. Qué se pierde.** §3. Cinco pérdidas, dos de ellas irrecuperables (la línea del tráfico aprendido; las manos de Jessie con la cinta).

**4. ¿Es mejor el libro de 65.000?**

**No, y no por poco.** El de 75.762 es mejor que el de 80.459 —marginalmente, y sobre todo en la Parte I—. El de 65.000 requiere amputar las siete escenas que impiden siete fallos concretos, porque son exactamente las que un corte por longitud encuentra primero: **no avanzan la trama, y por eso mismo son las que sostienen que esto sea una novela sobre un duelo y no un procedimiento con víctima.**

Y la pregunta correcta, si lo que se persigue son `ritmo` y `estructura`, no era la mía. Es la de §4.3: **este libro no tiene un problema de cuántas palabras, tiene un problema de dónde están.** 27.500 palabras de andamiaje para un clímax de cinco piezas, repartidas en cuatro partes que miden lo mismo, con los capítulos más cortos asignados al POV que mejor puntúa. Eso no se arregla cortando, y llevo dos días de medición para decir que no se arregla cortando.

---

**A2 · ángulo 3 · sobre `compilado/ad-aeternum-vF.md`, 48 capítulos, 80.459 palabras · 2026-08-19**
