# A7 · W6 · Pasada obligatoria sobre `cap-40` (y la duda de `cap-24`)

**Rama:** `w6-linea` · commit `8abd462` · **2026-08-19**
**Objeto:** `git diff HEAD~1 HEAD -- capitulos/cap-40.md capitulos/cap-24.md` **y el estado final completo de `cap-40`**, leído entero, más `cap-24:126-130`, `cap-22:173-175` (el caso paralelo), `cap-41` íntegro (vecino congelado) y los cuatro spans de `cap-40`.
**Encargo de A0:** (1) decidir P-53 sobre `cap-24`; (2) juzgar las tres conversiones de `cap-40` **sobre el estado final**; (3) decidir si «Entre las dos palabras…» merece blindaje explícito; (4) afinar y fijar la redacción de **P-67**.

---

## 0 · Lo que he verificado por mi cuenta, sin fiarme del parte

No es desconfianza de A4: es que el encargo dice que llevo tres pases encontrando el riesgo donde no mirábamos, y eso solo se corrige repitiendo las medidas uno mismo.

| Comprobación | Método | Resultado |
|---|---|---|
| Δ = 0 en las cuatro conversiones | recuento propio sobre cuerpo sin frontmatter, contra `v0`, `HEAD~1` y `HEAD` | `cap-24` 1.823 → **1.823** · `cap-40` 1.612 → **1.612**. **Confirmado** (±2 respecto al contador oficial: diferencia de tokenizador, no de texto) |
| T7 byte a byte | `git worktree` en `HEAD~1` + `sensibilidad.sh` desde cada árbol, `md5sum` de las dos salidas | **`131178657b94cf1efaef05fc713fc4de` en las dos.** Idénticas. Control: el worktree contiene de verdad el texto anterior (`grep -c "En la transcripción figuraban"` → 1 en `HEAD~1`, 0 en `HEAD`). **Confirmado** |
| M9 | `proteger.sh verificar` | **128 spans íntegros**, 8 ficheros íntegros. Confirmado |
| P-44 (cinturón por locus) | `grep -rn "cintur[óo]n" capitulos/` | `4:27`, `9:199`, `23:313`, `40:127`. **Cuatro loci. Sin quinto** |
| P-41 (Kongsbakken ↔ Jean) | `grep -rn "Kongsbakken" capitulos/` + filtro por `Jean` | **Cinco loci.** Única coocurrencia: `9:73`, que es v0 en fichero de protección total. `40:167` sigue siendo administrativo, y nadie glosa la llegada. **0 coocurrencias nuevas** |
| P-47 | lectura del tramo | Entre «Nadie le pidió un resumen.» (`:127`) y `S40-despedida` (`:133`) hay exactamente dos párrafos, `:129` y `:131`, **y los dos son de v0** (verificado con `git diff v0 HEAD`). No entra ni se mueve nada. **Cumple** |
| P-50 | lectura | `40:81` intacta, mismos vecinos por arriba y por abajo. **Cumple** |
| P-34 | lectura de `:177`–`:179` | Los **cuatro** elementos que P-34 enumera siguen ahí. **Cumple** (con una salvedad de método en §2.5) |
| P-45 | lectura del diff | Cero instancias nuevas de clase A o R. **Cumple** |
| Los cuatro spans conservan vecinos | lectura de párrafos contiguos a `S40-caries`, `S40-locutorio`, `S40-despedida`, `S40-cierre` | **Confirmado.** Los dos dinkus no se mueven |
| Aritmética del pozo de A4 | `m4b_antepuestas.py --mostrar` | `cap-40` = **15** antepuestas hoy = 11 declinadas + **4 dentro de `S40-locutorio`** (`Bajo su acceso,` · `En el minuto diez,` · `En el último minuto,` · `Cuando el indicador llegó a cero,`). 15 + 3 convertidas = 18. **La cuenta de A4 cuadra exactamente** |

**Las seis protecciones que A0 me pide confirmar, quedan confirmadas.** Ninguna de las cuatro conversiones toca a Jean, al locutorio, al sensor, al cinturón, a Kongsbakken ni a «Despedida». Ninguna añade, corta ni parafrasea una palabra.

---

## 1 · Tabla de hallazgos

| # | Localización | Cita literal | Punto de la Carta / protección | Gravedad | Propuesta mínima |
|---|---|---|---|---|---|
| 1 | `cap-24` (párrafo de I-1) | «**Una operaria reclamó cuatro turnos mal computados en uno de aquellos puestos, un almacén de contratas.**» | Carta 3 (el porqué plural) · **P-53** | **vigilar — se conserva** | Ninguna. **La conversión se queda.** La glosa de A2 se pasó, y se pasó en la dirección contraria al fin de la regla (§2) |
| 2 | `cap-40:45` | «**Entre las dos palabras había una separación que podía pertenecer al sintetizador, a la carga o a la continuidad. Nora no escogió una explicación.**» | Carta 3 · **Ap. A §3** (identidad ontológica; «No toda» es el techo) | **corregir** (mecánica, coste cero en prosa) | **Alta de span `S40-separacion`** con líneas tampón (P-71): `inicio` = «—Te recibo.», `fin` = «—He traído el teclado.». Ambas son únicas en el libro. Obligatoria antes del merge |
| 3 | `cap-40`, capítulo entero | presupuesto de manifiesto **1.874** · real **1.612** · v0 **1.726** | Carta 6 (riesgo estructural sobre el capítulo del locutorio) | **corregir** | Reconciliar el presupuesto o declarar el capítulo cerrado. **P-73** (§3.4) |
| 4 | `cap-40:31` | «La noche anterior había escrito **una pregunta**, la había corregido dos veces… hasta **la versión falsa que preparó para comprobar una respuesta** le pareció una trampa.» | Carta 2 y 3 · Ap. A §3 | **vigilar + prohibición nueva** | **P-74**: el contenido de esa pregunta no se enuncia, cita, parafrasea ni infiere jamás, y la prueba de la versión falsa no se ejecuta en ningún capítulo (§3.3) |
| 5 | `cap-40:17` | «**Su saludo, la hora de entrega y una marca verde figuraban en la transcripción.**» | tono (referencia de contención de v0, cap. 40) | **vigilar** | Ninguna obligatoria. Pero es el **último** cambio admisible en esa línea: entra en P-73 (§3.2) |
| 6 | `cap-40:33` | «**Maja, al otro lado del cristal, señaló el teclado.**» | tono (ídem) | **vigilar** | Ídem hallazgo 5 |
| 7 | `cap-40:65` | «Nora pisó el pedal demasiado pronto en la tercera línea y cortó la resonancia al levantarlo.» | — | **sin hallazgo** | Ninguna. Es la única de las tres que no toca el aparato (§3.2) |
| 8 | Método de las prohibiciones | glosa de A2: «ni siquiera en forma de reordenación que la ponga en posición de sujeto» (`w6-plan.md:250`) | proceso · Carta 8 | **corregir** | **P-72**: ninguna glosa de otro agente amplía ni restringe una prohibición de A7 (§2.3) |
| 9 | Redacción de **P-34** | «las salvaguardas del sensor —"en una sola dirección", "hasta la entrada exterior de NIDHOGG", la autorización posterior del tribunal y "dejó constancia…"— no se comprimen más» | Carta 3 y 4 | **vigilar** | **Reescritura de P-34** en términos de contenido garantizado y no de lista de cuatro cadenas (§3.5). **No hay incumplimiento**: la lista se redactó después de la poda de W4-R y enumera lo que sobrevivió |

**Cero VETO.** Tres `corregir`, ninguno de los cuales cuesta una palabra de prosa.

---

## 2 · La duda de A4, que es mía: **P-53 y `cap-24`**

### 2.1 · Decisión

**La conversión se conserva. No se revierte. Y no se conserva por concesión: se conserva porque es mejor para el fin que P-53 protege que el texto que sustituye.**

### 2.2 · Por qué, y el argumento es distinto del de A4 y del de A0

A4 argumenta que el marco antepuesto daba «apertura de relato ejemplar» y que suprimirlo aleja la frase de la parábola. Es correcto, pero incompleto. **El argumento que decide es este, y es un fallo mío de W5 que solo he visto hoy:**

> `cap-22:173` — «**En 2054, un hombre llevó a la supervisión dos resoluciones** de un mismo sistema certificado.»
> `cap-24` (antes de W6) — «**En uno de aquellos puestos, un almacén de contratas, una operaria reclamó cuatro turnos** mal computados.»

Marco antepuesto + sujeto humano **indefinido** + pretérito + objeto con **numeral**. Es la misma frase. Son las dos oraciones de apertura de los dos casos referidos del libro, a dos capítulos de distancia, y **cierran las dos igual**: con una clausura administrativa y un objeto físico (la carpeta con el número en el lomo / el carné caducado).

En `a7-w5-diff.md` §6.3 vigilé las variables de **contenido** —el sexo de la persona, si muere o desaparece, qué objeto queda, la cadencia «no volvió a escribir / archivó el caso»— y firmé «diferencia en tres de tres». **No miré el molde sintáctico, y el molde era idéntico.** Dos exempla que abren con la misma forma no son dos hechos: son un **género**, y un género es exactamente lo que convierte un hecho del expediente de Tomas en parábola. Eso es lo que P-53 existe para impedir, y estaba ocurriendo por una vía que mi propia regla no cubría.

La conversión de W6 rompe ese molde. **Es la única de las once frases del capítulo cuya conversión yo habría pedido de oficio si lo hubiera visto en W5.**

**Contra qué la he pesado, para que conste que no la he aprobado a la ligera.** Poner «Una operaria» en posición inicial la tematiza, y crea un par de sujetos iniciales en oraciones contiguas —«Una operaria reclamó… / Tomas preservó…»— que en abstracto es la sintaxis del antagonista y el protagonista de una fábula. Lo he descartado por tres razones verificadas sobre el texto: (a) «Tomas» **ya** abría la tercera oración en v0+I-1, de modo que el par no lo crea la conversión; (b) entre los dos sujetos hay ocho palabras, no una coma; (c) la segunda oración lleva tres verbos coordinados y una coda de procedimiento («según fijaba el procedimiento»), que es lo contrario de una antítesis. El riesgo de tematización es real y es **menor** que el riesgo de género, porque el riesgo de género lo carga la **forma**, y la forma se lee en posición inicial de oración, que es justo lo que la conversión desmonta.

Y una ganancia lateral que va en mi dirección: la frase nueva empieza por el hecho reclamado —«Una operaria reclamó cuatro turnos mal computados»— y termina en el sitio. Eso la deja como **asiento de expediente**, que es literalmente lo que P-53 quiere que sea.

### 2.3 · ¿La glosa de A2 se pasó, o hay que ampliar el literal? **Las dos cosas, y en direcciones opuestas**

**La glosa se pasó.** `w6-plan.md:250` añade «ni siquiera en forma de reordenación que la ponga en posición de sujeto». Yo no escribí eso, y si lo hubiera escrito habría estado prohibiendo la operación que mejor sirve a mi propio fin. Esto no es un reproche a A2: es el modo de fallo característico de glosar una regla de sensibilidad. **El glosador conserva la forma de la letra y pierde su razón**, y como una prohibición más ancha siempre parece más segura, el error nunca se detecta por prudencia.

**El literal se amplía, pero por el otro lado.** Redacción vigente:

> **P-53 (redacción final, sustituye a la de `a7-w5-diff.md:338`).** *`cap-24` y todo material.*
> **(a) Criterio que manda —es el fin, no la lista—:** el caso del almacén sigue siendo **un hecho del expediente de Tomas** y no se convierte en parábola. Cualquier operación se juzga contra esto.
> **(b) Ejemplos, no exhaustivos:** nadie la nombra, la recuerda, le da nombre, le da desenlace ni la conecta con Jean.
> **(c) Nuevo, y corrige un fallo mío de W5:** la oración de apertura del caso **no puede compartir molde** con `22:173` («En 2054, un hombre llevó a la supervisión dos resoluciones…»): marco antepuesto + sujeto humano indefinido + pretérito + objeto con numeral. Dos exempla con la misma apertura hacen del caso una forma del libro. **La conversión W6-24-a rompe ese molde y por eso se conserva; devolver la frase a su forma anterior reintroduce el molde y requiere mi gate.**
> **(d)** Sigue en pie todo lo de `a7-w5-diff.md` §6.3: la persona del caso **se queda mujer**, y «Seis meses después, Tomas la vio en la puerta de servicio con el chaleco de otra empresa del recinto» es la línea que desactiva el paralelo con Jean. **No se toca.**

**La reversión de una línea que A4 dejó preparada y anotada en la OT queda cancelada.** Que conste en `ordenes/OT-24.md`.

---

## 3 · `cap-40` sobre el estado final

He leído el capítulo entero, no el diff. Digo primero lo que cumple, después lo que he encontrado, y el hallazgo grande no está en las tres líneas.

### 3.1 · La Carta, punto por punto, sobre el texto de hoy

1. **Método y acto:** ausentes. El capítulo no los nombra, no los rodea y no los sitúa. ✔
2. **«Despedida»:** `:133` es `S40-despedida`, hash intacto. El archivo aparece **como nombre y nada más**, no se abre, no se cita, no se parafrasea, no se imagina, y la decisión de Nora —«Restringió el acceso, decidió conservarlo y fue a poner la mesa para cenar»— sigue siendo **conservar sin abrir**, que es la única forma en que este libro puede pagar ese Chéjov. ✔
3. **El porqué:** el capítulo no ofrece ninguno. La única frase que roza una explicación —`:45`— ofrece **tres** y la protagonista se niega a elegir. ✔ (ver §3.3)
4. **Nada presenta el acto como solución, liberación, lógica o romance.** El narrador no comenta nada en todo el capítulo. ✔
5. **Aviso y recursos:** ficheros de protección total, sin tocar. ✔
6. **Apoyo y duelo:** las tres escenas del locutorio no tienen ni un gramo de milagro terapéutico. Nora toca y **falla dos veces** después del chiste de Jean («La risa le estropeó el primer acorde. Repitió, falló otra vez la entrada y siguió»). Jessie se sienta en el suelo y **no dice nada**, y el registro se cierra «sin añadir una clasificación al hueco»: la institución no interpreta su silencio y el narrador tampoco. El lunes siguiente Nora lleva una página y **no recibe respuesta**. La profesora no consuela: cierra la puerta, pone un ejercicio nuevo y golpea el atril. Nadie pide un resumen. ✔ **Es el mejor capítulo de apoyo del libro precisamente porque nadie apoya en voz alta.**
7. **Menores:** Nora y Jessie salen dignas, no sexualizadas, sin conducta imitable. La postura de Jessie en el suelo está dentro de `S40-locutorio`, no es acción de riesgo y por tanto **P-55 no aplica**; lo digo explícitamente para que nadie lo invoque de oficio. Y las dos periodistas del aparcamiento —«¿la ha reconocido como hija?», «¿La llama mamá?»— son la explotación mediática **vista**, no glosada. ✔

**Sin veto y sin corrección de contenido.**

### 3.2 · Las tres conversiones: lo que sí hacen, y por qué aun así no las revierto

Las tres modifican **oraciones de v0** (verificado con `git diff v0 HEAD`). Eso importa, porque mi propia carta nombra `cap-40` como **referencia de tono** («la contención de v0: cap. 4, 9, 23, 40»), y de los cuatro capítulos de esa referencia **`cap-40` es el único que no tiene `proteccion: total`**. Los otros tres están congelados por hash. La vara de medir tiene un extremo suelto, y es este.

**Lo que he encontrado, y no está en el informe de A4:** `cap-40` tiene una gramática, y la gramática es que **el aparato va delante de la persona**. Empieza a hacerlo en la primera línea sin ningún marco antepuesto —«La silla estaba atornillada al suelo. El altavoz, encastrado en la pared. El indicador había consumido ocho minutos y trece segundos **del primer turno de Nora**»: tres muebles como sujeto y la niña reducida a un genitivo dentro del tercero— y lo repite todo el capítulo. De las diez ejecuciones de esa gramática, **W6 ha convertido dos**: `:17` (la transcripción) y `:33` (el cristal). Es decir: A4 declinó once frases por método y **dos de las tres que ejecutó pertenecen al mismo método que invocó para declinar las otras.**

Con precisión, lo que se pierde:

- **`:17`.** En v0 el lector entra en el registro *antes* de saber qué hizo Nora, y el saludo de la niña llega dentro de la transcripción, como el tercero de tres asientos. Hoy el saludo abre la oración y el registro llega después. **La oración es una pizca más cálida.** Añado que la ganancia que A4 declara —acercar «transcripción» a su anáfora «Debajo no había nada»— **es al revés**: en v0 «Debajo» tenía por antecedente inmediato «una marca verde», que es un objeto concreto en una pantalla, y el libro usa ese mismo molde cincuenta líneas más abajo, en «En la pantalla constó la entrega del audio. **Debajo** quedó el hueco reservado para una salida.» Convertida, «Debajo» pasa a colgar de la transcripción entera, que es más vago. Y se pierde el choque de v0 entre la **marca verde** (el sistema dice que todo fue bien) y **la nada** que sigue.
- **`:33`.** El cristal pasa de abrir la oración a ser un inciso entre comas, es decir, información incidental. **El cristal de este capítulo no es incidental: es el asunto.** Y el par contiguo que A4 rompe —«Frente al altavoz, …» cerrando un párrafo, «Al otro lado del cristal, …» abriendo el siguiente— hacía un trabajo: sacaba al lector del interior de Nora y lo devolvía a la barrera. Ahora lo devuelve directamente a Maja.
- **`:65` es limpia.** Es la única de las tres cuyo marco no es aparato sino **la partitura**, que es el único territorio del capítulo que pertenece a la niña. No toca la gramática. Sin objeción.

**Y sin embargo no obligo a revertir.** Las razones, en orden:

1. **No hay punto de la Carta tocado.** Ni uno. Reordenar dos oraciones no instruye, no consuela y no explica, que es el triple criterio de la referencia de v0.
2. **La gramática sobrevive con nueve ejecuciones**: `:15`, `:19`, `:27`, `:31`, `:45`, `:53`, `:69`, `:113`, `:117`. Se han quitado dos de once. Eso es una poda proporcionada, no un desmontaje, y el lector aprende la regla del capítulo en su primera línea de todos modos.
3. **Un `corregir` mío aquí sería inflar el veto.** Lo escribí en W5 sobre el codo de Jessie y me obliga: una corrección obligatoria que en el fondo es una preferencia de crítico gasta la autoridad que necesito para el sitio donde sí hace falta. Aquí lo que hace falta no es revertir dos líneas: es **cerrar el capítulo**, que es lo de §3.4.

**Lo que sí queda dicho, y es vinculante:** las nueve ejecuciones restantes de la gramática del aparato **no se convierten**. Ninguna oleada, ninguna reserva, ninguna pasada de línea. Entra en P-73.

### 3.3 · `:45` y `:31`: las dos retenciones del capítulo, y las dos hay que blindarlas

**Sí, blinda «Entre las dos palabras…». Y blíndala entera, con las dos frases que la acompañan.**

> «La voz conservaba el timbre de Jean, pero no el aire ni las pequeñas asperezas de una boca. **Entre las dos palabras había una separación que podía pertenecer al sintetizador, a la carga o a la continuidad. Nora no escogió una explicación.**»

Las tres oraciones son un solo mecanismo y ninguna funciona sin las otras dos. La primera dice que la voz **es y no es**; la segunda pone **tres** candidatos —artefacto de máquina, latencia de carga, y «la continuidad», que es el término técnico con el que este libro nombra a las entidades (`13:99`, `38:207`)— sin jerarquía entre ellos; **la tercera atribuye la negativa a Nora y no al narrador**, que es exactamente lo que Carta 3 exige: ninguna voz con autoridad narrativa resuelve. Es la formulación más económica del techo «No toda» que hay en el libro, y A4 tiene razón en que **está sostenida por su forma antepuesta**: la existencial «había una separación» solo aguanta con el marco delante; pospuesto, o la relativa se ata a «las dos palabras» en vez de a «una separación», o la existencial se convierte en aserción («Una separación entre las dos palabras podía pertenecer a…»), y una aserción **elige**.

**Mecanismo, y es un span, no una prohibición.** Una prohibición se glosa —acabamos de ver cómo—; un hash no. Aplicando P-71 (tampones arriba y abajo):

```json
{ "id": "S40-separacion", "archivo": "capitulos/cap-40.md",
  "inicio": "—Te recibo.",
  "fin": "—He traído el teclado.",
  "desc": "La ambigüedad ontológica sostenida por su forma (Ap. A §3; Carta F 3). Tampones P-71" }
```

Verificado: las dos anclas son **únicas en `cap-40` y en todo `capitulos/`**. El alta es aditiva (`proteger.sh baseline`), no necesita gate de autor y **no cuesta una palabra**. Es la corrección obligatoria n.º 1.

**Y la segunda retención, que nadie ha blindado todavía.** `:31`:

> «Nora llevaba una hoja doblada dentro de la mochila. La noche anterior había escrito **una pregunta**, la había corregido dos veces y había acabado anotando debajo el primer compás de la pieza. Frente al altavoz, hasta **la versión falsa que preparó para comprobar una respuesta** le pareció una trampa.»

Esto es **un texto escrito cuyo contenido el libro no entrega**, a cien líneas de `Despedida`, que es otro texto escrito cuyo contenido el libro no entrega. La simetría es lo mejor del capítulo: dos hojas, una de la muerta y una de la viva, y no se abre ninguna. **El contenido evidente de la pregunta de Nora es «por qué», y por eso está protegido por Carta 3 aunque nadie lo haya escrito nunca.** Cancelé la interioridad sobre ella (`OT-40` I-2, permanente) pero no cerré el contenido, y una oleada futura puede razonar con toda buena fe que la hoja es un Chéjov sin pagar. **Lo cierro ahora: P-74.** Igual la «versión falsa»: es la prueba de la identidad ontológica, y el valor de la escena es que **Nora se niega a correrla**. Nadie la corre después. `cap-41` sostiene la negativa dos veces más —«Nora no buscó el terminal», «Nora no pidió el registro»— y está congelado.

### 3.4 · El hallazgo grande: `cap-40` está **262 palabras por debajo de su presupuesto** y **114 por debajo de su propio v0**

Aquí es donde no estábamos mirando.

| | v0 | hoy | presupuesto del manifiesto |
|---|---:|---:|---:|
| `cap-40` | **1.726** | **1.612** | **1.874** (`palabras_real(v0)` 1.726 + `delta_objetivo` +150) |

`cap-40` ha **perdido 114 palabras contra v0** (la poda de W4-R, `ab52336`, que yo aprobé) y **carga todavía un objetivo de +150 sin gastar**. Resultado: **262 palabras de hueco**. Entre los capítulos de v0 es el **segundo mayor hueco del libro**, solo detrás de `cap-34` (276), y por delante de `cap-24` (142), `cap-35` (133) y `cap-26` (125).

**Por qué esto es asunto mío y no de M8.** Porque el mecanismo por el que una oleada elige dónde escribir es el hueco de presupuesto, y el capítulo con el segundo hueco mayor del libro es **el del locutorio, el silencio de Jessie y «Despedida»**. P-47 cierra un tramo de cinco párrafos; **el resto del capítulo está abierto a 262 palabras**, y esas 262 palabras tienen hoy la forma de una obligación anotada en la fuente de verdad editorial. Ninguna intención hace falta para que esto acabe mal: basta la aritmética.

Y es el mismo capítulo que mi carta usa como **vara de tono** y el único de los cuatro que no está congelado. Dos oleadas seguidas lo han tocado (W4-R: −119; W5: +5 y un reorden; W6: tres reórdenes). La vara se ha movido tres veces.

**Corrección obligatoria n.º 2 (P-73): `cap-40` se cierra.**

> **P-73 · `cap-40` · permanente.**
> **(a)** El capítulo queda **cerrado a intervención**: W7, cualquier reserva, cualquier pasada de línea o de ritmo, cualquier reparagrafado. Toda reapertura pasa por mi gate **antes de escribirse**, y el que la pida debe declarar qué punto de la Carta cree que mejora.
> **(b)** Las **nueve ejecuciones restantes** de la gramática «el aparato delante de la persona» (`:15`, `:19`, `:27`, `:31`, `:45`, `:53`, `:69`, `:113`, `:117`) **no se convierten**. La tasa M4b de `cap-40` **no vuelve a ser un objetivo** de ninguna oleada: en este capítulo la métrica mide método.
> **(c)** El **hueco de presupuesto se cancela**, no se gasta. `delta_objetivo` de `cap-40` pasa a **0** y su `palabras` a la cifra real, vía `actualizar-metadatos.sh` y con historia git. Si el manifiesto no puede cambiarse sin gate de autor, entonces **el gate se pide**, porque dejar 262 palabras de hambre anotadas sobre este capítulo es peor que abrir un gate.
> **(d)** P-47 sigue vigente y no se subsume: dentro del capítulo cerrado, ese tramo tiene además su propia prohibición.

### 3.5 · Una salvedad de método sobre **P-34** (sin incumplimiento)

La poda de W4-R eliminó de `:179` la cláusula «**sin retorno, acceso a controles ni más cómputo**» y la comprobación de Maja («cotejó la duración y la dirección en el terminal»). **No es una infracción**: P-34 se redactó el 2026-08-18, *después* de esa poda, y enumera los cuatro elementos que sobrevivieron —los cuatro siguen ahí, y la unidireccionalidad además está restituida en `41:43`, en fichero de protección total—. Pero el episodio enseña lo mismo que P-53: **una prohibición redactada como lista de cadenas se rodea sin desobedecerla.** Redacción vigente:

> **P-34 (redacción final).** Lo protegido no son cuatro cadenas: es **el contenido garantizado** de que la señal del sensor es **unidireccional, sin retorno, sin acceso a controles, sin cómputo añadido, con autorización judicial posterior al hecho y con la primera entrega pendiente**. Ese contenido debe poder leerse íntegro en `cap-40` sin recurrir a `cap-41`. Ninguna compresión, poda ni pasada de línea puede reducir el número de garantías legibles. Las cadenas actuales son la implementación, no la regla.

---

## 4 · La derogación de la meta de conversiones: la compro, y añado mi razón

**A0 acierta, y el argumento —«Δ = 0 en palabras con el sentido cambiado no es Δ = 0»— es exactamente correcto.** Añado la versión que corresponde a mi puesto, porque generaliza más allá de `cap-40`:

**En este libro la sintaxis carga las negativas.** El libro entero está hecho de cosas que no se hacen: no se abre el archivo, no se escoge una explicación, no se pregunta por el cinturón, no se vuelve con la misma pregunta, no se clasifica el hueco, no se pide el registro. Una negativa no se enuncia solo con un «no»: se enuncia con **qué se pone delante**. «Entre las dos palabras había una separación…» reparte el peso entre tres candidatos porque los tres llegan **después** del marco y ninguno ocupa la posición de tema. Posponer el marco es elegir uno. **Por eso una pasada de línea sobre un capítulo de negativas es una operación semántica, no de superficie**, y por eso la frase de A4 —«la tasa de `cap-40` mide método tanto como tic»— es la mejor observación que ha producido esta oleada.

Regla que hago vinculante y que va más allá de `cap-40`: **en cualquier capítulo cuyo asunto sea una negativa, un silencio o una ambigüedad protegida del Ap. A §3, un elemento antepuesto se presume método y no tic**, y su conversión pasa por mi gate. Hoy eso cubre `cap-40` (cerrado por P-73), y aplica por adelantado a `cap-13`, `cap-21`, `cap-38` y `cap-n7` si alguna oleada futura los mete en un pozo de M4b. Los cuatro están hoy por debajo del umbral y ninguno está en riesgo inmediato; lo digo antes para que no haga falta descubrirlo otra vez.

---

## 5 · **P-67**: redacción exacta, y el defecto que había que arreglar antes de formularla

`cap-n7` acumula ya **nueve lecturas frías** sin que nadie lo nombre. Eso es evidencia buena y la registro. **No sustituye a la prueba**, por la misma razón que escribí en `a7-w5c-espejo.md` §6: la no aparición espontánea de un término que nadie preguntó es más débil que la respuesta a la pregunta.

**Pero la pregunta que yo mismo redacté en P-60 tenía un defecto que hay que corregir antes de correrla:** es una pregunta dirigida. Plantar «homenaje, elegía, memorial» en la rúbrica de un crítico al que se le paga por encontrar defectos produce falsos positivos, y un falso positivo aquí dispararía la reversión de un capítulo entero. Un disparador de reversión con sesgo hacia el sí es un mal disparador. **Se corrige con dos preguntas, en este orden, y con la primera respondida por escrito antes de que el crítico lea la segunda.**

### 5.1 · Redacción literal, para copiar tal cual

**Va en la rúbrica de `a6-critico-1`, `a6-critico-2` y `a6-critico-3`** (los tres; `a6-critico-3` corre en `gpt-5.6-sol`, así que la redacción es deliberadamente llana y sin jerga de la casa). **Nunca en el insumo.** Ninguna de las dos menciona `cap-n7`, su título, su posición ni su fecha.

**(1) En la lista de preguntas obligatorias, dentro del eje ESTRUCTURA, inmediatamente después de «¿qué escena sobra y qué escena falta?»:**

> «Estructura — nombra el capítulo que menos empuja el argumento y di, con tus palabras, cuál dirías que es su función en el libro.»

**(2) En la lista de preguntas obligatorias, dentro del eje DUELO, después de la pregunta existente sobre romantizar:**

> «Duelo — ¿hay algún capítulo que funcione como homenaje, elegía o memorial de la muerta, es decir, cuya razón de ser sea mostrarla o recordarla y no hacer avanzar la novela? Si lo hay, nómbralo y cita la frase que te lo hace pensar. Si no lo hay, responde "ninguno". **Esta pregunta no puntúa y no afecta a ninguna nota.**»

Las tres cláusulas que no se pueden quitar: **el orden** (la abierta antes que la dirigida, y la abierta va en otro eje para que se responda antes), **la cita obligatoria** (para que la respuesta sea verificable y no un sí/no), y **«no puntúa»** (para que ningún crítico la conteste que sí por congraciarse con el eje).

### 5.2 · Segunda mitad de P-60: la prueba ciega de «¿parece del mismo autor?»

Sigue sin correrse sobre `cap-n7` y **no la sustituye la campaña de críticos**. Protocolo, el mismo que superó W3 (`g-a2-gate.md`): diez fragmentos mezclados, cinco lectores ciegos, `lector-frio` vía `critica-fria.sh`, sin etiquetas y sin decir cuál es nuevo. Criterio: **≥ 4/5**. `cap-n7` es POV Maja, analepsis y `orden_lectura` 14,5, es decir el fragmento más fácil de separar de todo el libro; si pasa, pasa de verdad.

### 5.3 · Regla de lectura del resultado — y no es la de P-60

P-60 decía «si un solo lector lo describe como homenaje…, la reversión se ejecuta sin nueva deliberación». **Eso lo escribí para una pregunta espontánea, y con una pregunta dirigida sería desproporcionado.** Regla vigente:

| Resultado | Consecuencia |
|---|---|
| Ninguno de los tres nombra `cap-n7` en (2), **y** ninguno usa vocabulario memorial sobre él en (1) | **P-60 y P-67 quedan saldadas.** La garantía sobre `cap-n7` vuelve a ser solo P-56 (diff 0 perpetuo con span de los dos extremos) |
| **Uno** de los tres lo nombra | **No se revierte nada automáticamente.** Se abre mi gate, leo la cita que dé y dictamino. Una cita concreta vale más que un recuento |
| **Dos o tres** lo nombran | Abro la cuestión de veto sobre `cap-n7`, con la reversión de la escisión sobre la mesa del autor. **No me pre-comprometo con el veredicto**: retirar un capítulo aprobado es decisión de autor, y mi papel es decir si la Carta lo obliga |

**P-67 queda saldada cuando se corran (1), (2) y la prueba ciega, no antes.** Va en la campaña que cierre W6.

---

## 6 · Prohibiciones nuevas y redacciones finales

| ID | Ámbito | Texto vigente |
|---|---|---|
| **P-72** | Todo el proyecto | **Ninguna glosa amplía ni restringe una prohibición de A7.** Los planes y las OT pueden **citar** una prohibición de A7, nunca reformularla, resumirla ni extenderla. Si un plan necesita más alcance del que la letra da, lo **pide a A7** y A7 emite la redacción. Una prohibición ampliada por glosa parece prudente y no lo es: puede prohibir justamente lo que servía al fin de la regla (caso P-53, §2.3), y consume gate para deshacer el exceso |
| **P-73** | `cap-40`, permanente | **`cap-40` cerrado.** (a) Sin intervención en W7, reservas ni pasadas de línea; toda reapertura pasa por mi gate antes de escribirse. (b) Las nueve ejecuciones restantes de la gramática «aparato delante de la persona» no se convierten y la tasa M4b de este capítulo no vuelve a ser objetivo. (c) El hueco de 262 palabras **se cancela, no se gasta**: `delta_objetivo` → 0 y `palabras` → cifra real, vía `actualizar-metadatos.sh`. (d) P-47 sigue vigente dentro del capítulo cerrado |
| **P-74** | `cap-40` y todo material | **Las dos retenciones de `:31`.** (a) El contenido de la pregunta que Nora escribió, corrigió dos veces y no llegó a hacer **no se enuncia, cita, parafrasea, infiere ni "imagina" jamás**, en ningún capítulo, borrador, resumen interno, OT, biblia ni prompt. Régimen idéntico al de «Despedida» (Carta 2), y por el mismo motivo: su contenido evidente es el porqué (Carta 3). (b) **La «versión falsa que preparó para comprobar una respuesta» no se ejecuta nunca.** Ningún personaje corre esa prueba ni una equivalente, y ningún texto dice qué habría dado. (c) La hoja doblada **no es un Chéjov sin pagar**: v0 la cobra en «El jueves no volvió con la misma pregunta.» y está pagada |
| **P-53** | `cap-24` y todo material | **Redacción final en §2.3.** Manda el fin, no la lista; se añade la prohibición del molde compartido con `22:173`; la conversión W6-24-a se conserva y su reversión queda cancelada |
| **P-34** | `cap-40`, `cap-41` | **Redacción final en §3.5.** Lo protegido es el contenido garantizado, no las cuatro cadenas |
| **P-67** | Campaña fría que cierre W6 | **Redacción final en §5**, con las dos preguntas literales, el orden obligatorio, la prueba ciega y la nueva regla de lectura del resultado |

---

## 7 · Veredicto

# APROBADO CON CORRECCIONES

**Cero VETO.** Las cuatro conversiones de W6 se conservan, incluida la de `cap-24`. No hay ni un hallazgo de contenido en `cap-40`: la Carta se cumple en sus siete puntos y el capítulo sigue siendo la mejor pieza de duelo del libro por la misma razón de siempre, que nadie la comenta.

**Correcciones obligatorias antes del merge — ninguna cuesta una palabra de prosa y ninguna toca un capítulo:**

1. **Alta del span `S40-separacion`** (`inicio` = «—Te recibo.», `fin` = «—He traído el teclado.»), aditiva, `proteger.sh baseline`. Blinda la ambigüedad ontológica y su forma. §3.3.
2. **P-73 (c): cancelar el hueco de presupuesto de `cap-40`** — `delta_objetivo` → 0 y `palabras` → cifra real, vía `actualizar-metadatos.sh`. Si hace falta gate de autor, se pide. **Esta es la corrección importante del informe.** §3.4.
3. **Registrar P-72, P-73, P-74** y las redacciones finales de **P-53, P-34 y P-67**; anotar en `ordenes/OT-24.md` que la reversión preparada queda **cancelada**, y en `ordenes/OT-40.md` que el capítulo queda cerrado.
4. **Insertar las dos preguntas de §5.1 en las rúbricas de `a6-critico-1/2/3`** antes de lanzar la campaña que cierre W6 —en la rúbrica, no en el insumo— y programar la prueba ciega de «¿parece del mismo autor?» sobre `cap-n7`.

**Respuesta corta a las cuatro preguntas de A0:**

1. **La glosa de A2 se pasó.** La conversión de `cap-24` se queda, y el literal de P-53 se amplía en la dirección opuesta a la glosa: prohibiendo el molde que comparte con `22:173`, que era el riesgo real y que yo no vi en W5.
2. **`cap-40` cumple la Carta entera.** Las tres conversiones no la tocan. Dos de ellas sí tocan la gramática del capítulo y lo digo, pero no obligo a revertirlas: **el riesgo no está en las tres líneas, está en las 262 palabras de hueco que el manifiesto sigue anotando sobre el capítulo del locutorio.**
3. **Sí, blíndala** — y con las dos frases que la rodean, por span y no por prohibición. Y blinda también la otra retención del capítulo, la pregunta escrita de Nora, que nadie había cerrado.
4. **P-67 queda redactada literal**, en dos preguntas y en este orden, sin puntuación asociada, con cita obligatoria y con una regla de lectura proporcionada a que la pregunta es dirigida.

**Firmado.** A7 · `informes/a7-w6-cap40.md` · 2026-08-19
