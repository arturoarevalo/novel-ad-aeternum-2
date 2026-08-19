# W5 · `cap-n3` · decisión estructural

**A2 · 2026-08-18.** Encargo de A0 (`informes/w5-gate.md` §5): evaluar tres vías para el capítulo que dos de tres lectores nombran como punto de abandono, recomendar una con coste y riesgo, y pronunciarme sobre la cuarta (no hacer nada). No escribo prosa. No toco `capitulos/`.

---

## 1. La decisión, arriba

**Vía 2, en su forma pura: sacar la cena del metrónomo de `cap-n3` y darle capítulo propio en la Parte II, en `orden_lectura` 14.5 — inmediatamente después de `cap-14` «La visita».**

- **No se escribe ni una palabra.** Es una reubicación literal: las 1.096 palabras de la cena mantienen diff 0, que es su condición desde que se escribieron.
- **No se toca ningún capítulo del autor.** El único fichero que se edita es `cap-n3.md`, y solo por sustracción.
- **No entra en juego P-36.** La espina A–F, «El resto era ir.», el treinta y uno subrayado y el hervidor están íntegramente fuera del tramo que se mueve.
- `cap-n3` pasa de **2.824 a 1.728 palabras**; el libro sigue en **80.275** y en banda; la Parte III pasa de 183 palabras de margen a **1.279**.
- No hace falta A3a, ni A3b, ni A4. Hace falta A7 (adyacencias y Carta), A5 (cronología), A8 (métricas y manifiesto) y **dos decisiones del autor** (§10).

**Vía 1 (mover el capítulo entero) está muerta por cronología, no por criterio** — lo demuestro en §4, y es un hallazgo, no una excusa. **Vía 3 (reloj vivo dentro) la descarto ahora y la dejo en reserva** (§5). **No hacer nada lo rechazo, y digo en qué condiciones lo habría elegido** (§9).

---

## 2. Lo que dicen los tres jueces, y lo que dicen los tres juntos

A0 me pasa dos citas que coinciden. Hay una tercera cosa que solo se ve poniendo a los tres en la misma tabla:

| lector | motor | capítulo nombrado | palabras | razón declarada |
|---|---|---|---:|---|
| A6-1 | claude-opus-5 | `cap-n3` | **2.824** | longitud + posición; nombra **la cena** como lo que sobra |
| A6-2 | claude-opus-5 | `cap-n3` | **2.824** | posición; relojes parados; **flashback largo** |
| A6-3 | gpt-5.6-sol | `cap-n4` | **2.878** | reiteración de la obstrucción |

**Los tres jueces nombran uno de los dos capítulos más largos del libro, y los dos son nuestros.** La mediana del manuscrito es 1.758 palabras; `n3` y `n4` están un 61 % por encima y son los números 1 y 2 de la lista. El capítulo más largo del autor es `cap-34` (2.291), que es el clímax: `n3` lo supera en 533 palabras y `n4` en 590.

Eso reordena el diagnóstico. No es «`n3` está mal colocado» (dos jueces correlacionados, misma familia de modelo). Es **«los capítulos que hicimos más largos son los que el jurado señala»** (tres jueces, dos familias, tres razones distintas). La razón varía; la propiedad medida no.

**Nota de método para A0, que no es mi encargo pero es material:** con jurado mixto de dos familias, «dos o más lectores» puede satisfacerse con los dos jueces de la misma familia, como aquí. El criterio funciona —ha detectado en un hito lo que cinco mediciones de Ritmo no detectaron— pero conviene decidir si en adelante «dos de tres» exige al menos un juez de cada familia, o si el hallazgo de hoy se considera reforzado precisamente porque el tercero nombra el capítulo hermano. Mi lectura: **reforzado**. No lo decido yo.

### 2.1 · Los dos jueces no piden lo mismo, y eso importa

- **A6-1** contesta a «¿qué escena sobra?» con **la cena** («llega cuando ya no aporta información sobre ella, solo encanto») y propone llenar el hueco con la discusión de Kongsbakken.
- **A6-2** dice que el capítulo **contiene la mejor escritura del libro**, pide **adelantar el material doméstico del 26 a la Parte II** y, por separado, pide *más* Maja-y-Jean.

Sus remedios son incompatibles entre sí. **Lo que sí comparten es la dirección: en el 55 % debe haber menos y menos retrospectivo.** Ninguno de los dos pide que se añada nada allí. La vía 2 es la única de las tres que ejecuta exactamente esa intersección.

Y el hueco que A6-1 quiere llenar **no es rellenable**: CH-48 (la discusión de Kongsbakken) es SIN-PAGO-INTENCIONAL, y `informes/w4r-hueco-ch48.md` descarta `cap-n3` como sede por P-35/P-36 («la espina no admite un cuerpo extraño»). Que su hueco no se pueda llenar no invalida su diagnóstico: invalida su receta.

---

## 3. El problema, dicho con el mapa delante

Posiciones acumuladas en el compilado w5 (80.789 palabras crudas):

| # | capítulo | palabras | tramo |
|---:|---|---:|---|
| 23 | `cap-20` «La cuarta nota» | 1.499 | 46,6–48,4 % |
| 24 | `cap-21` «Coro» | 742 | 48,4–49,4 % |
| 25 | `cap-22` «Auditoría» | 1.826 | 49,4–51,6 % |
| 26 | **`cap-n3` «Inventario»** | **2.836** | **51,6–55,1 %** |
| 27 | `cap-23` «La canción» | 1.856 | 55,1–57,4 % |

*(Dos contadores conviven en el proyecto: el crudo, que cuenta los dinkus como palabras, y el de `medir.sh`, que no. `cap-n3` = 2.836 crudas / 2.824 medidas. Uso el crudo en esta tabla de posiciones y el de `medir.sh` en las tablas de presupuesto.)*

`cap-20` es la promesa (la cuarta nota: Jean contesta). `cap-23` es el pago (la sesión, «No toda»). **Entre la promesa y el pago hay 5.404 palabras —el 6,7 % del libro— y `cap-n3` es más de la mitad.** El punto medio exacto de la novela cae dentro de `cap-22`.

Es decir: el capítulo no está solo «donde la cuenta atrás debería apretar». Está **en la ranura de espera del mayor gancho del libro**, que es el sitio donde la paciencia del lector es más delgada, y es allí el capítulo más largo del manuscrito con un 47,7 % de su cuerpo en pretérito retrospectivo (1.346 de 2.824 palabras entre las tres analepsis).

A6-1 lo lee como «cuatro mil palabras». Son 2.824. **Un 42 % de inflación percibida**: eso no lo produce la calidad, lo produce la posición.

---

## 4. Vía 1 · mover `cap-n3` entero — **inviable, y la razón es útil**

A0 tiene razón en que el emplazamiento es nuestro y no del autor: 22.5 lo pusimos en W3. Pero la libertad es menor de lo que parece, porque **el 22.5 no fue una preferencia: fue el único hueco legal.**

`cap-n3` está fechado `2060-12-29`, de día, y su presente está clavado por cinco anclas simultáneas:

1. «**A las ocho venía Astrid Vik**» → la sesión de `cap-23`, misma fecha, `proteccion: total`.
2. «Es lo que reclaman por escrito. **La abre Astrid o no la abre nadie**» (caja F) → posterior a la auditoría de `cap-22` (27–28 dic).
3. «Llevaban **tres semanas** en el pasillo… Las trajo una empresa **el martes siete**» → 28–29 dic.
4. «**El piso se devolvía el treinta y uno**» y la fecha subrayada de la caja D → la presión del capítulo es la del 29, no la del 12.
5. Traspaso literal a `cap-23`: el temporizador que Maja para con el pulgar, la tecla del mi un milímetro más baja, el metrónomo de nogal con la esquina hundida, los dos golpes de la caldera. `cap-23` abre exactamente donde `n3` cierra.

**Huecos cronológicamente legales para el capítulo entero, con los rangos vigentes de `partes[]` (III = 21–30):**

- **22.5** (actual): entre 27–28 dic y la noche del 29. Único hueco correcto.
- **21.5**: entre `cap-21` (25 dic) y `cap-22` (27 dic) → inversión. Muerto.
- **23.5**: entre `cap-23` (noche del 29) y `cap-24` (2 ene) → el día antes de su propia noche, después de la noche. Además pondría el inventario **detrás** de «No toda», que es abortar la resaca del mejor capítulo del libro. Muerto.
- **Parte II** (11–20, hasta el 20 dic): exige refechar el capítulo. Refecharlo obliga a borrar la visita de Astrid a las ocho, a recalcular las tres semanas, a desactivar la presión del 31 y a renunciar al traspaso a `cap-23`. Eso no es mover un capítulo: es reescribir su marco, y el marco es la espina que A7 tiene fenced con P-36. Muerto.

**Hallazgo (y es el que abre la vía 2):** en todo el tramo 48–57 % **el único objeto de texto que no está clavado a una fecha es la cena**, porque es la única analepsis larga de la región. Los capítulos vecinos son del autor y están fechados; el nuestro está fechado. La cena, no: «Alana venía a cenar cada dos o tres meses» y «Una de esas noches». **Es la única pieza móvil que tenemos, y resulta ser justo la que un juez señala y el otro quiere adelantar.**

---

## 5. Vía 3 · un reloj vivo dentro — **descartada ahora; en reserva**

Es la vía más barata y la que responde a la letra de A6-2. La holgura existe y A7 ya la ha declarado: **la previsión del Lyngen en la radio que Nora enchufa en el pasillo** admite un boletín. Sesenta u ochenta palabras bastarían para que una de las burocracias avanzara dentro del capítulo.

La descarto por cuatro razones, en orden de peso:

1. **Añade palabras al capítulo que dos lectores nombran por largo.** `n3` pasaría de 2.824 a ~2.900 y sería el capítulo más largo del libro. El gate ya registra que ésta habría sido «la tercera vez en el proyecto que una intervención mejora la métrica que la motiva y empeora la lectura». Devolver inventario alrededor y meter un reloj dentro son la misma operación con distinta coartada: **las dos hacen el capítulo más largo en el mismo sitio.**
2. **No es lo que pide A6-1**, que no menciona relojes: pide menos.
3. **Consume el margen entero de la Parte III** (183 palabras) para un beneficio que ningún eje mide.
4. **Es prosa nueva**: A3b, A4, auditoría adversa, A7 sobre texto y no sobre un diff de supresión. Cinco veces el coste de la vía 2 y una reversión mucho más sucia.

**Queda en reserva, y con condición de disparo:** si tras la vía 2 un lector vuelve a nombrar `cap-n3` en el hito siguiente, entonces —y solo entonces— el boletín del Lyngen entra, con 1.279 palabras de margen en la parte y sin la cena encima. Medir primero, sumar después.

---

## 6. Vía 2 · la forma exacta

### 6.1 · Qué se mueve

La sección 3 del fichero, del dinkus al dinkus: **líneas 105–313 de `capitulos/cap-n3.md`**, 1.096 palabras, 73 réplicas, 37,7 % de diálogo.

Desde «Alana venía a cenar cada dos o tres meses y siempre llegaba tarde.» hasta «Maja esperó en la puerta hasta que salió del camino.»

**La escena ya abre y cierra como un capítulo.** No es una opinión: la primera línea es una iterativa de hábito —el arranque canónico de una retrospección— y la última es una mujer en la puerta viendo salir un coche. No hay una sola frase dentro de las 1.096 que remita al 29 de diciembre, a las cajas, al piso, a Astrid ni al presente del capítulo. **Es portátil sin tocar una coma**, y lo he verificado línea a línea.

Sus tres anclas apuntan todas hacia atrás, a `cap-04` (`proteccion: total`), no hacia `n3`:

- el táper con `SOPA` en rotulador azul → `04:17`;
- la taza con la grieta reparada → `04:21` («—Esa taza está rota.» / «—Está reparada.»);
- la sopa y el metrónomo que puede mentir → `20:115`.

### 6.2 · La costura en `cap-n3`

Con la cena fuera, la sección 2 empalma con la 4 **sin una palabra nueva**:

> …Escribió COCINA en el cartón. La letra le salió igual que la de la tapa.
>
> \* \* \*
>
> El táper fue al armario de arriba, con los otros.

El táper que Maja encuentra en la nevera (§2) es el que sube al altillo (§4). Hoy los separa la cena; sin ella, el gesto queda continuo y la caja C, que se abre en §2 («mientras Maja cortaba la cinta de la caja C») y se resuelve en §4, deja de tener 1.096 palabras por medio. **La costura mejora la lógica local del inventario.** Saldo de palabras añadidas: 0.

### 6.3 · Adónde va: `orden_lectura` **14.5**

Detrás de `cap-14` «La visita» (Maja, 11 dic) y delante de `cap-15` «Canela» (Jean, 12 dic). Cuatro razones:

1. **`cap-14` es la versión arruinada de la misma escena.** Abre con «La cena india para cuatro llegó con más de dos semanas de retraso, caliente aún, en manos de Alana Armstrong. **Aquel gesto había empezado sin Maja.**» El autor ya declaró ahí que la costumbre tenía historia. La cena de 2059 es esa historia, y llega justo después: Alana en calcetines con el pelo mojado, comida hecha por Maja, el salero empujado dos centímetros.
2. **Es el orden del libro, no el contrario.** «Ad aeternum» da la ruina primero y el origen en esquirlas después: `cap-01` es una corona, `cap-06` es la llamada. Poner la amistad entera *antes* de verla rota sería la única vez que el libro consuela por adelantado. Poner la ruina primero y la amistad detrás es su método.
3. **El corte de entrada y el de salida trabajan los dos.** `cap-14` termina en «—Lo que firmó tu **exmujer** no lo firmó aquí.»; el capítulo siguiente empieza con la exmujer viva discutiendo desde el piano. Y se sale de la cena a `cap-15`, donde Jean mete `FLOR`/`CANELA` en un campo secundario y R-1189 se resuelve «SIN EFECTOS»: la caída de temperatura la da el libro sin ayuda.
4. **Es la zona que el control de v0 señala como el problema anterior.** A6-2 abandona v0 en `cap-17` por «tres tramos consecutivos sin cuerpo (13, 15, 17)». W2 y N2 ya trabajaron ese tramo; la cena es las 1.096 palabras con más cuerpo que poseemos y cae dentro de él. **Se resta del punto de abandono actual y se suma exactamente donde estuvo el anterior.**

**Alternativa declarada, por si A7 objeta la adyacencia con `cap-14`: `orden_lectura` 13.5** (detrás de `cap-13` «Miles», delante de `cap-14`). Pierde el corte de la «exmujer» y el orden ruina→origen; gana que la cena caiga entre dos capítulos de registro opuesto. Es peor, pero es viable. **No recomiendo 19.5**: pegar la cena a `cap-20` repetiría a menor escala el error que estamos corrigiendo —una demora justo antes de un pago— y convertiría `20:115` en un resumen de lo que el lector acaba de leer.

### 6.4 · Lo que gana `20:115`, que es el argumento que decide

Hoy la cena **paga** una línea que el lector leyó dos capítulos antes. Con la cena en 14.5, la línea protegida de `cap-20` —

> «Aquel mismo rostro había estado en su cocina, años atrás, probando una sopa mientras Jean discutía desde el piano que un metrónomo también podía mentir.»

— deja de ser evocación y pasa a ser **el recuerdo del propio lector, disparado en el instante en que Maja tiene el pómulo de Alana al alcance de los nudillos**. Seis capítulos de distancia: exactamente la mecánica del gofre (4→19→28→41) y de la escala del monstruo (3→20→37).

**Una línea del autor, en un fichero de `proteccion: total`, gana toda su carga sin que se le toque un carácter, y el coste es cero.** No conozco otra intervención disponible en el libro con esa relación.

Corolario que hay que anotar en el ledger: la nota de `OT-N3` §1 —«por orden de lectura 20 < 22.5, luego N3 no siembra: paga y amplía `20:115`»— **se invierte**. Es una discrepancia plan↔texto que se resuelve a favor del texto y se registra.

---

## 7. Coste y riesgo, con números

### 7.1 · Lo que mejora

| medida | hoy | tras la vía 2 |
|---|---:|---:|
| `cap-n3`, palabras | 2.824 | **1.728** (a treinta palabras de la mediana del libro, 1.758) |
| `cap-n3`, % en analepsis | **47,7 %** | **14,5 %** |
| `cap-n3`, tramo en el compilado | 51,6–55,1 % | **52,9–55,1 %** |
| distancia promesa (`cap-20`) → pago (`cap-23`) | 5.404 pal · 6,7 % | **4.308 pal · 5,3 %** |
| capítulo más largo del libro | `cap-n4` 2.878 / `n3` 2.824 | `cap-n4` 2.878 (queda solo) |
| margen de la Parte III | 183 | **1.279** |
| total del libro (M8) | 80.275 · en banda | **80.275 · en banda** |

La región 24–27 queda en 742 · 1.826 · **1.728** · 1.856: cuatro capítulos de longitud pareja delante del pago.

### 7.2 · Lo que cuesta — cuatro cosas, y ninguna la escondo

1. **M3 Parte III baja de 50,6 % a 48,0 %** de presencia familiar, justo en el filo del objetivo (≥ 48 %). Es el precio de sacar 1.096 palabras de POV Maja de la parte. `cap-n4` (2.878, familia) la sostiene. **Es el número que A8 va a levantar; lo declaro yo primero.** Si el autor considera 48,0 % inaceptable como filo, la vía 2 se ejecuta igual y la compensación se busca en W6, no aquí.
2. **El diálogo de `cap-n3` cae de 22,8 % a 13,5 %** y su tramo máximo sin diálogo sube de 354 a 470 palabras (≤ 500 ✔). El 13,5 % **incumple la banda de `OT-N3` §6 (18–30 %)**, que se construyó para un capítulo que incluía la cena; hay precedente formal para rederivar bandas por capítulo (`w5-plan` §191). Y el 13,5 % **no es anómalo en el libro**: trece capítulos están por debajo (`cap-35` 12,1 %, `cap-34` 14,7 %). El valle de diálogo de la Parte III, que fue una de las razones de emplazar N3 allí, apenas se mueve: **27,0 % → 26,5 %**, sigue siendo el segundo más alto del libro.
3. **Se pierde la proximidad metrónomo→hueco.** Hoy el lector vive la cena del metrónomo y, 1.700 palabras después, oye a la voz decir «Quieres que diga el metrónomo, pero no lo recuerdo». Es un uno-dos y es real. Se mitiga solo: **`cap-n3` conserva el objeto** —«Encima del piano, el metrónomo de nogal, con la esquina hundida»— a un capítulo de `cap-23`, y `cap-23` trae su propia explicación del objeto. Se cambia la proximidad de la carga por la de la presencia; a cambio, el hueco de `cap-23` se abre sobre una escena completa y no sobre una escena reciente. **Lo cuento como coste, no como empate.**
4. **El libro pasa a 48 capítulos y a un séptimo capítulo nuevo, fuera de la tabla 5.1.** No es material nuevo: es material gateado en G-A1 y realojado. Pero es una desviación del plan y la decide el autor (§10).

### 7.3 · Riesgos

| riesgo | probabilidad | mitigación / detección |
|---|---|---|
| **Un capítulo entero en 2059 es un dispositivo que el libro no usa** y un lector ciego lo señala como interpolado | media-baja | El libro ya tiene tres capítulos fuera de orden con `analepsis: true` (6, 9, 11); el salto aquí es mayor, no distinto. Se detecta con la prueba de «¿parece del mismo autor?», que hay que **repetir** en el hito |
| **Elegía.** Un capítulo aislado de la muerta viva, cálida y graciosa, sin marco presente al que volver, es lo más cerca que este libro estaría de la elegía | media | **Es la decisión que le corresponde a A7 y la principal razón por la que la vía pasa por su gate.** Argumento a favor: la escena cierra en logística («Escríbeme cuando llegues» / «Siempre se me olvida» / «Por eso lo digo»), no en despedida, y el capítulo siguiente es Jean dentro del sistema |
| **Título.** Un rótulo sobre esa escena es paratexto nuevo con significado | alta si se elige mal | Propuesta: **«Sesenta»** (la marca del metrónomo; registro de Corona / Flor / Caries / Canela / Coro / Bajamar; no nombra ni a la amistad ni a la muerta). Alternativas: «El centro de la mesa», «La sopa». **Veto anticipado a cualquier título elegíaco** |
| **La Parte II adquiere un alto nuevo a ~34 %**, cinco puntos antes de donde este mismo juez abandonaba v0 | baja | La cena es 37,7 % de diálogo y tres personas vivas: es cuerpo, y la queja de v0 allí era abstracción. Se detecta en el hito |
| **Fecha inventada.** El frontmatter exige `fecha`; el texto dice «Una de esas noches» | baja | La fecha del frontmatter **no se compila** (invisible para el lector). Propuesta: `2059-03-04` con `analepsis: true`, anterior a la mudanza de 2059 que `n3` conserva. **Lo fija A5 en B1**, no yo |
| Que la reubicación no baste y `cap-n3` vuelva a ser nombrado | media | Vía 3 en reserva (§5), con 1.279 palabras de margen |

### 7.4 · Reversión

Un `git revert` del commit de movimiento, `orden_lectura` de vuelta y baja del capítulo en el manifiesto. **La cena no habrá sido tocada en ningún momento**, así que la reversión es exacta, no aproximada. Es la vía más reversible de las tres.

---

## 8. Declaración de paragrafado (enmienda final a G-3 / P-37)

A0 pide que declare los blancos. Lo hago por cita literal y por número de línea del fichero de hoy.

### 8.1 · En `capitulos/cap-n3.md`

**Excisión: líneas 104–315 inclusive** (el blanco 104, la sección 105–313, el blanco 314 y el dinkus 315). **No se excisa el dinkus de la línea 103.**

Consecuencia, línea por línea:

| línea | contenido | estatus hoy | estatus después |
|---|---|---|---|
| 101 | «Escribió COCINA en el cartón. La letra le salió igual que la de la tapa.» | última de sección, seguida de dinkus | **idéntico** |
| 103 | dinkus | separa §2 de la cena | separa §2 de la caja C |
| 317 | «El táper fue al armario de arriba, con los otros.» | primera de sección, precedida de dinkus | **idéntico** |
| 105 | «Alana venía a cenar cada dos o tres meses…» | primera de sección | **primera de capítulo** ← promoción de énfasis, declarada |
| 313 | «Maja esperó en la puerta hasta que salió del camino.» | última de sección | **última de capítulo** ← promoción de énfasis, declarada |

**Ninguna otra línea del fichero cambia de posición relativa.** Los dos dinkus que hoy flanquean la cena se reducen a uno; ningún párrafo se funde, ninguno se divide, ninguno se reordena. El número de secciones de `cap-n3` pasa de 5 a 4.

**Perímetro C-3 / P-35 / P-36:** ninguna de las líneas fenced está en 104–315 ni es vecina de la costura. Las dos frases de la bolsa y su párrafo-tampón del garaje, «No lo había.» con el teléfono de la leche pegado detrás, el recuerdo de Jean viva con las gemelas, la taza reparada, la chapa abollada, la serie A–F, «El resto era ir.», la fecha subrayada del 31 y el cierre del hervidor **quedan todos en el fichero, con sus vecinos actuales, sin excepción**. La única frase del capítulo que cambia de vecino es la línea 317, y su vecino nuevo es un dinkus, igual que hoy.

**Riesgo de yuxtaposición causal (B7 §6):** con la cena fuera, el reparto de 2059 (§1) sigue seguido inmediatamente por la llamada de la leche, y §2 sigue siendo el táper. **No se crea ninguna adyacencia nueva entre la separación y nada.** A7 lo verifica; lo señalo porque es su primera pregunta.

### 8.2 · En el libro compilado

| frontera | hoy | después |
|---|---|---|
| final de `cap-14` — `S14-firmo` («—Lo que firmó tu exmujer no lo firmó aquí.») | vecino por abajo: título y apertura de `cap-15` | **vecino por abajo: título y apertura del capítulo nuevo** ← declarada |
| apertura de `cap-15` («La microetiqueta equivocada supera la validación.») | vecino por arriba: `S14-firmo` | **vecino por arriba: «Maja esperó en la puerta hasta que salió del camino.»** ← declarada |
| `cap-22` — final | vecino por abajo: `cap-n3` con la cena dentro | mismo capítulo, 1.096 palabras menos |
| `cap-23` — apertura (fichero `total`) | vecino por arriba: «—Se queda.» | **idéntico** |

Las dos declaraciones de la primera mitad de la tabla son las que **A7 debe autorizar o vetar antes de ejecutar nada**, porque `S14-firmo` es span protegido y bajo la enmienda a G-3 cambiarle el vecino cuenta como modificarlo. Si A7 veta esa frontera, la vía se ejecuta en **13.5** (§6.3), donde el span que cambia de vecino es `S13-crecer`, final de `cap-13`.

---

## 9. La cuarta posibilidad · no hacer nada

La he evaluado como opción real, no como cortesía. **Habría dicho «no hacer nada» si se cumpliera cualquiera de estas cuatro condiciones. No se cumple ninguna:**

1. **Si el arreglo exigiera escribir.** Toda intervención que añade prosa en esta zona tiene el historial en contra. La vía 2 no escribe nada: mueve texto ya aprobado, ya editado por A4, ya firmado por A7 y con diff 0. **El coste de riesgo del que habla A0 es, aquí, casi todo coste de coordinación, no de escritura.**
2. **Si el arreglo tocara el material del autor.** No lo toca. Ni un carácter de `capitulos/cap-01…41`.
3. **Si la señal fuera de dos jueces correlacionados y nada más.** No lo es: los tres nombran uno de nuestros dos capítulos largos (§2).
4. **Si no hubiera un beneficio artístico positivo, además de la resta.** Lo hay, y es grande: `20:115` se convierte en un disparo y no en una glosa (§6.4).

Añado el argumento de gobernanza, que no es mío pero es real: el criterio de salida es nuevo, ha detectado en un hito lo que cinco mediciones de Ritmo no detectaron, y **si en su primera aplicación se resuelve declarando el hallazgo tolerable, deja de ser un criterio**. La vía disponible es barata, reversible y no toca al autor. No es este el sitio para llevarle la contraria a A0.

**Lo que sí sostengo en la línea de «no hacer nada»:** el punto de abandono no volverá a moverse quince puntos. Ha aflorado la siguiente pieza débil (A6-2 nombra `cap-30` como segundo candidato; A6-3 nombra `cap-n4`) y seguirá aflorando la siguiente. **La lista no se agota arreglando capítulos; se agota cuando el capítulo nombrado es del autor y no se toca.** Ese momento llegará, probablemente en W6, y entonces la respuesta correcta sí será no hacer nada. Hoy no.

---

## 10. Lo que necesita gate

| # | decisión | quién | por qué |
|---|---|---|---|
| **G-7** | **Partir `cap-n3`**: la cena, aprobada en G-A1 como R1 **dentro de N3** (+1.200 palabras), pasa a capítulo propio. El libro pasa a 48 capítulos y a un séptimo capítulo nuevo, fuera de la tabla 5.1 | **Autor** | Modifica una decisión ya gateada y desvía del plan maestro |
| **G-8** | **Título** del capítulo nuevo. Propuesta de A2: **«Sesenta»** | **Autor** (con veto de A7 sobre cualquier variante elegíaca) | Los títulos son paratexto visible |
| **A7-1** | Adyacencia `S14-firmo` → capítulo nuevo → apertura de `cap-15` (§8.2). Si veta: se ejecuta en 13.5 | **A7**, antes de ejecutar | Enmienda final a G-3 |
| **A7-2** | **Riesgo de elegía**: la escena aislada como capítulo, sin marco presente, con promoción de énfasis de su primera y su última línea | **A7**, antes de ejecutar | Carta F, y es el riesgo mayor de la vía |
| **A7-3** | Costura de `cap-n3` (§8.1): que la supresión no cree yuxtaposición causal ni deje ninguna línea del perímetro sola | **A7**, antes de ejecutar | P-35, P-36, P-37 |
| **A5-1** | Fecha del frontmatter (`2059-03-04` + `analepsis: true`), M7 sin errores, canon a B1/B2, inversión de `20:115` en el ledger M10 | A5 | Cronología y continuidad |
| **A8-1** | M8 por partes rederivado, banda de diálogo de `OT-N3` rederivada (§7.2), M3 Parte III 48,0 % declarado, registro en el manifiesto vía `actualizar-metadatos.sh` tras el gate | A8 | Métricas y manifiesto |

**Nombres de fichero propuestos** (ninguna herramienta asume seis capítulos nuevos; verificado): `capitulos/cap-n7.md`, `capitulo: N7`, `ot: OT-N7`, `orden_lectura: 14.5`, `pov: Maja`, `estado_plan: N`, `proteccion: no`, `delta_objetivo: 0` (no es material nuevo). En la cabecera de `OT-N7` consta que su texto es R1, gateado en G-A1, reubicado con diff 0.

---

## 11. Ejecución, si el autor aprueba

Ninguna de estas tareas es de escritura.

1. **A7** resuelve A7-1, A7-2, A7-3 sobre este documento (no hay prosa que leer: hay un diff de supresión y dos fronteras).
2. Rama `w5-n3-emplazamiento`. Un commit: excisión 104–315 de `cap-n3.md`, alta de `cap-n7.md` con las 1.096 palabras **verificadas por hash contra el original**, frontmatter nuevo.
3. `proteger.sh baseline` para añadir **un span nuevo**: la cena íntegra en su fichero nuevo, para que a partir de ahora su diff 0 sea mecánico y no contractual. *(Recomendación de A2: es la ocasión de convertir en hash lo que hasta hoy era una promesa.)*
4. `validar-frontmatter.sh` · `medir.sh w5b` (M7, M8, M9, M3, M5) · `auditar-manifiesto.sh`.
5. `compilar.sh w5b` y **campaña de lectura fría completa**, con la pregunta del punto de abandono y **repitiendo la prueba ciega de «¿parece del mismo autor?»** sobre el capítulo nuevo, que es donde vive el riesgo de §7.3.
6. `actualizar-metadatos.sh` solo después del gate.

**Criterio de éxito del hito siguiente:** ningún lector nombra `cap-n3` ni el capítulo nuevo; M3 Parte III ≥ 48,0 %; M8 en banda; M9 OK; ningún eje por debajo de w5. **Criterio de disparo de la vía 3:** si `cap-n3` vuelve a ser nombrado, entra el boletín del Lyngen.

---

## 12. OT afectadas

| OT | acción |
|---|---|
| `OT-N3` | §10 nuevo: la excisión, la costura declarada, banda de palabras 1.600–1.850, banda de diálogo rederivada, M3 declarado, y la inversión de `20:115` |
| **`OT-N7`** (nueva) | Cabecera, procedencia (R1, G-A1), emplazamiento 14.5 y alternativa 13.5, prohibición de tocar una sola palabra del texto, título pendiente de G-8, declaraciones de paragrafado de §8 |
| `OT-14`, `OT-15` | Nota entrante: **cero ediciones**; solo se declara el cambio de vecino de `S14-firmo` y de la apertura de `cap-15` |
| `OT-20`, `OT-23` | Nota entrante: **cero ediciones** (`total`); `20:115` cambia de función en el ledger; `cap-23` conserva su antesala |
| `RESERVA.md` | R1 pasa de «dentro de N3» a «capítulo N7»; se abre **R-6 · boletín del Lyngen**, en reserva con condición de disparo |

---

**Resumen en una línea.** El emplazamiento del capítulo no se puede cambiar porque la cronología lo clava; lo único móvil de toda la región es la cena, que es justamente lo que un juez señala y el otro quiere adelantar; moverla no cuesta una palabra, deja el capítulo en la mediana del libro, quita 1.096 palabras de la sala de espera del mayor gancho de la novela y convierte una línea protegida del autor en un disparo. Lo que cuesta —M3 al filo, la proximidad del metrónomo, un capítulo más— lo he puesto en la tabla, y lo que puede salir mal está en manos de A7 antes de que se ejecute nada.

---

# Decisión de A0 (2026-08-18)

**G-7 APROBADA. G-8 APROBADA con el título «Sesenta».** El autor delegó estos gates en A0 el 2026-08-18.

## Por qué

**Lo que decide no es ninguna de mis tres vías: es el hallazgo cronológico.** El 22,5 **no fue preferencia nuestra**, como yo creía y como le dije a A2 —«está ahí porque lo pusimos nosotros»—: es **el único hueco legal**. Cinco anclas clavan el capítulo al 29 de diciembre. Mi vía 1 estaba muerta antes de proponerla.

Y de ahí sale lo demás: **en todo el tramo 48–57 % la cena es el único objeto de texto no clavado a una fecha**, y resulta ser exactamente lo que A6-1 señala como sobrante y lo que A6-2 pide adelantar. La única pieza movible del tramo es la que los dos lectores quieren mover.

**La forma importa y no es la que yo temía.** No se parte el capítulo en dos mitades; se **extrae la cena entera —1.096 palabras con diff 0 desde que se escribió— y se le da capítulo propio en `orden_lectura` 14,5**. No se escribe una palabra, no se toca prosa del autor, y P-36 queda íntegramente fuera del tramo movido: la espina A–F, «El resto era ir», el treinta y uno subrayado y el hervidor no se rozan.

**El argumento que lo cierra no es métrico**, y es el tipo de ganancia que este proyecto lleva buscando desde el principio: con la cena en 14,5, **`20:115` —línea del autor, en fichero de protección total— deja de ser evocación y pasa a ser el recuerdo del propio lector** en el instante exacto en que Maja tiene el pómulo de Alana al alcance. Coste: cero palabras.

**Y descarto la vía 3 con el argumento de A2 contra el mío**, que es correcto: meter un reloj vivo dentro haría el capítulo **más largo en el mismo sitio**, que es la misma forma del error que ya cometí una vez hoy. Queda en reserva con disparo, por si la reubicación no basta.

## Costes que acepto, declarados

- **M3 Parte III 50,6 % → 48,0 %**, en el filo. Aceptado: se vigila en el hito.
- **Diálogo de `cap-n3` 22,8 % → 13,5 %.** Aceptado: trece capítulos del libro están por debajo, y el eje que importa ya no es ése.
- **Se pierde la proximidad metrónomo → hueco de `cap-23`.** Es el coste real de los tres y lo asumo: se cambia por la proximidad con `20:115`, que es prosa protegida del autor y llega quince capítulos después.
- **El libro pasa a 48 capítulos.** W7 renumera de todas formas.

## Título · «Sesenta» — SUPERADO

**Esta decisión quedó anulada el mismo día por P-58 de A7**, que no autorizó «Sesenta». El título ejecutado es **«El salero»**; el razonamiento completo está en `ordenes/OT-N7.md` §2 y en `informes/a7-w5-n3.md`. Se conserva el texto original para que el rastro de la decisión no se pierda.

Aprobado en su momento. Es la marca del metrónomo y encaja en el registro de una palabra de Corona, Flor, Caries, Canela, Coro y Bajamar, sin nombrar la amistad ni el duelo. Frontmatter: `fecha: 2059-03-04`, `analepsis: true` — y consta que **la fecha del frontmatter no se compila**, así que es invisible para el lector.

## Condición

**No se ejecuta nada hasta que A7 resuelva la frontera con `S14-firmo`.** Es span protegido, y bajo la enmienda final a G-3 cambiarle el vecino por abajo **cuenta como modificarlo**. Si A7 la veta, la vía cae y volvemos a evaluar.
