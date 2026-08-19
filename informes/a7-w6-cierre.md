# A7 · Cierre de W6 · firma sobre Mats, dictamen de P-67 y revisión de conjunto de seis oleadas

**Rama:** `w6-linea` · commits `39d711d` → `1f0cded` · **2026-08-19**
**Objeto:** (1) `git diff HEAD~1 HEAD -- capitulos/cap-27.md` y **P-54 sobre el estado final**; (2) el hallazgo del ancla de M6; (3) los otros cuatro cambios de la oleada; (4) **el dictamen sobre P-67, disparada en la banda alta**; (5) la revisión de conjunto que A0 pide: *¿queda algo que yo haya autorizado y que hoy no autorizaría?*

**Insumos leídos:** `git diff main..w6-linea -- capitulos/` íntegro; `cap-27` completo; `cap-32:15–29, 79–99, 135–151, 185–187`; `cap-39:117–147`; `cap-n7` completo; `cap-n1:95–115, 210–260, 290–310, 388–410`; `cap-n2:210–230`; `cap-n6:212–228`; `cap-25` completo y su diff `v0..w6`; `cap-13`, `cap-40`, `cap-24` en su estado final; `ordenes/OT-27.md` §9; `informes/a6-w6-critico-{1,2,3}.md` **completos** (no solo las respuestas a P-67); `informes/m6b/m6b-ancla-muestra-w4.md` y las claves de M6b; `biblia/b7-carta-sensibilidad.md`; `biblia/metadatos.json`; `protegidos/spans.json`.

**Verificaciones propias (no me fío del parte):**

| Comprobación | Método | Resultado |
|---|---|---|
| M9 | `proteger.sh verificar` | **129 spans íntegros, 8 ficheros íntegros.** OK |
| Frontmatter | `validar-frontmatter.sh` | **0 avisos** |
| T7 sobre todo el manuscrito | `sensibilidad.sh` | 379 hits, **59 nuevos vs. baseline v0**; los 59 leídos en su dictamen (11 en `b7-aclarados.tsv`) |
| **T7 sobre TODO lo añadido desde `v0`** | extracción de las 3.049 líneas añadidas (22.944 palabras) + patrones A | **7 hits, 3 de ellos los paratextos.** En prosa, **cuatro**: `40:65` (conversión ya dictaminada), `n1:269` culpa, `n1:299` Koppangen, `n3:121` bolsa. **Los cuatro los autoricé yo, uno por uno** |
| Menores (P7) sobre lo añadido | patrones de la familia «menores» sobre las mismas 22.944 palabras | **2 hits**, los dos gestos canónicos (`n1:327` manos bajo los muslos = `9:121`/`23:17`; `n4:363` teléfono boca abajo = `20:233`). **Cero sexualización, cero autolesión, cero riesgo eficaz** |
| Últimas horas / últimos días | `[úu]ltima vez|d[íi]as antes|v[íi]spera|antes de morir|noviembre` sobre lo añadido | **3 hits, ninguno del acto** (tarea de tutoría, salida de campo, plazo administrativo de `n6`) |
| Causa única sobre lo añadido | `por eso|desde entonces|nunca se recuperó|si hubiera|podríamos haber|no pudo más` | **6 hits, ninguno sobre Jean.** Cero formulaciones causales nuevas |
| P5 (aviso y recursos) | `compilado/ad-aeternum-w6.md` | Aviso en línea 1, **antes** de la cabecera de la Parte I; «Recursos de ayuda» tras el cap. 48, sin cabecera de parte; números íntegros. **Cumple** |
| Suicid* en el cuerpo | `grep` v0 vs hoy | **una sola instancia en v0 y una sola hoy** (`06:213`, la derivación de la médica). Las otras tres son los paratextos. **Cero deriva** |

---

# 1 · P-67 · «El salero»: dictamen

**La pregunta que se me hace es si la Carta obliga a revertir. Contesto que no, y lo razono sobre el texto, no sobre el recuento.**

## 1.1 · Lo que exactamente dicen los tres, leído entero y no en la cita

A0 me pasa las respuestas a la pregunta (2). Yo he leído los tres informes completos, **incluida la respuesta a la pregunta (1)**, que es la mitad del dispositivo y la que da la lectura no dirigida. Puestas juntas:

| | (1) sin la palabra «memorial» — *«el capítulo que menos empuja el argumento y su función»* | (2) con la palabra delante |
|---|---|---|
| **A6-1** | «el 17… **Su función es fundar el emblema del libro** —el metrónomo que "marca sesenta toda la noche"— **y dar a Alana una deuda afectiva que su traición necesitaba**» | «cuya razón de ser es mostrar a Jean viva» |
| **A6-2** | «el 17, que no mueve nada. **Su función es doble y necesaria**: acreditar que Alana fue familia —sin lo cual su traición no pesa— y sembrar los objetos que después funcionarán como duelo» | «Existe para dejarla viva y discutidora ocho páginas» |
| **A6-3** | «su función consiste en **restituir la intimidad doméstica** de Jean, Maja y Alana **y convertir el metrónomo en miniatura ética del libro**» | «cuya razón principal es recuperar a Jean dentro de una cotidianeidad desaparecida» |

**Antes de que se les nombrara el marco, los tres le asignaron función estructural, y dos de los tres la llamaron *necesaria*.** Solo A6-3 usa en (1) vocabulario que roza lo memorial («restituir»), y lo empareja en la misma frase con una función temática. Esto es exactamente lo que el orden obligatorio de las dos preguntas existía para poder ver, y es el dato que la cita aislada de (2) borra.

## 1.2 · El disparador se cumplió sobre el *proxy*. El daño que el proxy vigilaba **no está**

P-60 no se escribió contra la palabra «memorial»: se escribió contra un daño concreto —que el capítulo aislado funcionase como **altar**: idealización de la muerta, ternura, despedida, añoranza administrada por el narrador—, porque de ahí a romantizar la muerte hay un paso y ese paso es el punto 4 de la Carta. He releído el capítulo entero contra ese daño, línea por línea:

| Ingrediente de un altar | ¿Está en `cap-n7`? |
|---|---|
| Idealización de Jean | **No.** Es pedante, se lleva el metrónomo a la mesa y le mandan retirarlo, reclama «Todo lo que está en el centro es mío», cuenta dos veces la misma historia con más gente dentro de la caja la segunda, y **Alana le dice en su cara: «Un día vas a discutir con alguien que tenga razón»** |
| Ternura o despedida | **No.** Nadie se toca, nadie dice una palabra de afecto. El único gesto cálido del capítulo —el táper con SOPA— es **para Alana** |
| El matrimonio iluminado | **No.** Maja y Jean apenas se dirigen la palabra; Jean habla desde el salón. **A6-1 pide «una escena entre Maja y Jean viva» con este capítulo delante, y lo llama «un flashback ajeno»**: la prueba de que no funciona como retrato del matrimonio |
| Prolepsis, luto anticipado, «sería la última vez» | **No hay ni una.** Ni una marca temporal, ni una melancolía de estación, ni un «entonces todavía» |
| Narrador nostálgico | **No existe narrador comentando.** Cero adjetivación afectiva, la misma voz objetual de todo el libro |
| Cierre elegíaco | «El coche de Alana tardó en arrancar. / Maja esperó en la puerta hasta que salió del camino.» **Es logística.** A6-3 la cita como «frase decisiva» y **en esa frase no está Jean** |

**Las dos citas que dan A6-1 y A6-2 son la misma y es una jactancia perdida** («Contigo he discutido yo» / «Y has perdido»). Un memorial que elige como frase emblemática a la muerta presumiendo de ganar discusiones no idealiza a nadie.

## 1.3 · Entonces, ¿qué detectaron? **Función, y la función la cambió la escisión**

Detectaron un hecho verdadero y estructural: es el único tramo largo del libro en que Jean está viva y en su casa, y no mueve la trama. Eso era igual de cierto dentro de «Inventario»; lo que cambió al aislarlo es que **la función pasó a leerse como autónoma**: dentro del inventario era «el recuerdo que disparan las cajas», subordinado; con título propio es «el capítulo donde ella está viva». La escisión no añadió una palabra y **sí cambió lo que el capítulo parece existir para hacer**. El disparador funcionó: eso es exactamente lo que estaba puesto a detectar.

**Y ahí está el riesgo real, que no está en `cap-n7` sino en el campo gravitatorio que crea. Los tres críticos, sin que nadie se lo preguntara, piden lo mismo:**

- **A6-1:** «Lo que falta: una escena entre Maja y Jean viva» → mejora 3: «escribir las dos escenas ausentes —**Maja y Jean en las semanas previas**— y **una resolución real del archivo "Despedida"**».
- **A6-2:** «¿Qué escena falta? Una escena entre Jean y Maja con las dos presentes y algo en juego» → mejora 2: «escribir la escena que falta, Jean y Maja en 2059, **y colocarla donde hoy está el 17 o inmediatamente después**».
- **A6-3:** «La escena que falta es **la comida del domingo anterior a la muerte de Jean**, dramatizada en presente» → mejora 2: «Añadir **antes de la muerte** una escena presente y breve de Jean con Maja, Nora y Jessie».

**Tres jueces independientes piden una escena de Jean viva pegada a su muerte, y uno de ellos pide además abrir «Despedida».** Ese es el hallazgo de sensibilidad de la campaña, y es mucho más grave que la etiqueta que se le ponga a `cap-n7`. La existencia de un capítulo aislado, admirado y de función legible —«aquí está viva»— **es lo que hace que "uno más, y más cerca del final" parezca una mejora obvia y barata**. La casilla ya existe; solo falta que alguien con buena intención la rellene. Y la única oleada que queda es W7.

## 1.4 · Dictamen

> ## `cap-n7` **SE QUEDA, CON EL PERÍMETRO CERRADO**. La Carta **no obliga** a revertir.
>
> No obliga porque el daño que P-60 vigilaba —idealización, ternura, despedida, narrador nostálgico, prolepsis— **es verificablemente inexistente en el texto**, y porque la reversión **no quita una sola palabra del libro**: mueve 1.096 palabras de Jean viva de un contenedor a otro. La Carta gobierna contenido y voz, no envoltorio. Vetar un envoltorio con el contenido limpio sería inflar el veto, y el veto es el recurso más escaso que administro.

**Lo que sí queda, y es caro:** **P-82** y **P-83** (§6), que cierran el perímetro por el lado por donde el riesgo entra de verdad.

**Y lo digo sin escaquearme, porque A0 pregunta justamente esto en §3: si la escisión llegara hoy a mi mesa por primera vez, con lo que ahora sé, la denegaría.** No por lo que el capítulo dice, sino porque aislarlo crea en la arquitectura una casilla legible de «Jean viva» y una casilla legible atrae relleno. Que no la revierta significa una sola cosa: la Carta no me autoriza a deshacer con un veto una decisión estructural cuyo texto cumple. **Revertir o no es decisión de A0 y del autor, sobre argumentos de oficio, y a mí me da igual el resultado a efectos de este gate: P-82 y P-83 rigen idénticas en los dos escenarios**, porque las 1.096 palabras siguen en el libro en cualquiera de los dos.

**Para la decisión de oficio de A0, dos datos que he verificado y que juegan en direcciones opuestas:** (a) el beneficio que compró la escisión **se ha evaporado** —`cap-n3` vuelve a ser punto de abandono para dos de tres—; (b) el contenedor actual sigue siendo el más cruel de los dos (la cena arruinada por delante, la mujer reducida a cola de validación por detrás), y volver a meter la escena en el capítulo del que dos críticos huyen no la protege de nada.

## 1.5 · Qué reabriría la cuestión de veto (disparador reformulado, sustituye al de `a7-w6-cap40.md` §5.3)

**P-67 queda saldada en sus preguntas (1) y (2).** Sigue debiéndose la prueba ciega de «¿parece del mismo autor?» (§7). **No condiciona este dictamen**: mide costura de estilo, no memorial.

La cuestión de veto sobre `cap-n7` **se reabre automáticamente**, sin nueva deliberación, si ocurre **cualquiera** de estas tres:

1. Un lector —frío, beta o autor— describe el capítulo con **vocabulario de idealización o de añoranza** («hace que la eches de menos», «muestra la persona maravillosa que era», «la muerte duele por lo que se pierde aquí»). No basta con que lo llame memorial: eso ya ha pasado y ya está dictaminado.
2. Alguien propone **una segunda escena de Jean viva** en cualquier oleada, reserva o A/B (véase P-82).
3. `cap-n7` recibe **cualquier cosa que refuerce su autonomía**: epígrafe, fecha, marca de analepsis, dedicatoria, cambio de título, posición de frontera de parte, o un eco posterior en el que un personaje recuerde esa cena.

---

# 2 · Mats en `cap-27` · **P-54, verificada sobre el diff, con la formulación corregida**

## 2.1 · La respuesta a lo que A0 pide confirmar

**P-54 se cumple. Y la formulación con la que A0 me la presenta —«ninguna conversión acorta»— es falsa al pie de la letra y hay que corregirla antes de que viaje a W7 como garantía.**

| | v0 | W6 | palabras | oraciones | verbos finitos |
|---|---|---|---|---:|---:|
| `:23` | «Recomiendo que la conserve el comité de riesgos.» | «La estudia el comité de riesgos.» | 14 → **12** | 2 → 2 | 3 → **2** |
| `:35` | «La continuidad ejecutiva debe resolverse primero.» | «El orden del día lo fijo yo.» | 6 → **7** | 1 → 1 | 1 → 1 |
| `:57` | «Las decisiones ejecutivas pasan a otra firma mientras…» | «Las decisiones ejecutivas las firmo mientras…» | 17 → **15** | 2 → 2 | 3 → 3 |

**Dos de las tres acortan** (−2 y −2; Δ total del capítulo −3), y `:23` **pierde además una cláusula subordinada**. Lo que A3b garantiza *de verdad* —y lo que P-54 protege— es otra cosa, y esa sí la he verificado y se cumple entera:

1. **Ninguna réplica se convierte en fragmento.** «La estudia el comité de riesgos.» es una oración completa con sujeto pospuesto; ninguna queda nominal, elíptica ni interrumpida.
2. **Ninguna pierde su verbo finito.** Lo que `:23` pierde es un **atenuante de cortesía** («Recomiendo que…»). De un atenuante caído el lector infiere autoridad, no fatiga.
3. **El suelo del personaje sube.** Su réplica más corta pasa de 6 a **7** palabras; la más larga (`:53`, 29) no se toca; la media de sus seis réplicas va de 15,5 a 15,0 (−3 %). **La sintaxis de Mats no se comprime: se le quita la deferencia.**
4. **El capítulo no nombra la enfermedad, no la roza y no la pone en relación con la muerte de Jean.** Los tres objetos de las réplicas son un comité de riesgos, un orden del día y una firma.

**Redacción que debe viajar en lugar de la de A0:** *ninguna conversión produce recorte, fragmentación, pérdida de verbo finito ni descenso del suelo de longitud de sus réplicas; el suelo sube.* Una garantía falsa en su letra es peor que ninguna: alguien la citará en W7 y le servirá de licencia o de trampa.

## 2.2 · La adyacencia que A3b declara y que hay que mirar de frente

`:21` —«Mats sostenía la estilográfica **con la izquierda, encajada** entre los dedos y el lomo de una carpeta»— **es un signo de cuerpo y es la izquierda**, que es la mano del canon (`32:15` «Estabilizó la mano izquierda con la derecha», `32:29` «la mesa ocultase la izquierda», `32:187` «La mano izquierda tardó en soltar la credencial»). La conversión `:23` es la línea inmediatamente siguiente y es la que más se acorta.

**Aun así no incurre**, y la razón es precisa: lo eliminado es un verbo de recomendar, no aire; la oración resultante conserva predicado completo; y la primera oración de la misma réplica («La propuesta de gobernanza es sólida») no se toca, de modo que el bloque sigue entrando largo. **Sigo diciendo que es el punto exacto donde una pasada futura rompería P-54**, y por eso entra en P-87.

## 2.3 · Sobre declinar la nominal y el imperativo desnudo: **de acuerdo, y por una razón mejor que la regla de las tres**

A3b las declinó por techo de aparición. **Yo las habría declinado aunque el techo hubiera estado libre**, y esto es doctrina de sensibilidad, no de estilo:

> **La réplica nominal sin verbo finito es, precisamente, la forma que se lee como quedarse sin aire.** «—Utilidad.» junto a una mano izquierda encajada en una carpeta no es idiolecto: es síntoma. De las dos formas que a Mats lo hacen reconocible, la más reconocible es también la única que P-54 no puede permitir en un capítulo que lleve un signo de su cuerpo.

Así que la coincidencia de la regla de las tres con P-54 es una suerte, no un método, y no puede volver a dejarse al azar. Queda como **P-87**.

**Y sobre el fondo del encargo:** de acuerdo también con que devolverle la voz por las formas menos llamativas es lo correcto en un libro que se niega a darle un ordenante individual a la muerte de Gunnar. Lo compruebo en el texto y se sostiene: `27:163` («no atribuyó a Mats la apertura de `/0000`») intacta; `32:93` («El resumen no tenía autor») intacta; `39:117` (el auto «dejó en blanco al ejecutor y al ordenante individuales») intacta. **Un hombre que reclama la autoría de todo lo administrativo y nunca la de lo que el libro deja en blanco mantiene el hueco más visible sin rellenarlo.** Eso funciona a favor de la ambigüedad protegida —con un techo, que también va en P-87: hoy son **cuatro** reclamos en primera persona (`27:35`, `27:57`, `32:85`, `39:147`) y no puede haber un quinto.

---

# 3 · El ancla de M6: de acuerdo, y lo que añado desde mi puesto

**El hallazgo es correcto y lo he verificado en el fichero.** `informes/m6b/m6b-ancla-muestra-w4.md` enseña como Mats: «La documentación externa hablará de juicio contextual asistido. Es la formulación que cabe en el calendario y en el contrato.» Sustantivo institucional en posición de sujeto, impersonal, sin agente: **al atribuidor ciego se le enseñó la única clase de línea que el encargo T4 existía para corregir.** El 0,0 % es, en parte, artefacto del ancla, igual que el 21 % de las gemelas lo fue del etiquetado. Se remide.

**Lo que añado, y es mi remite y no el de A8, porque las anclas son extractos del manuscrito enseñados fuera de contexto a un lector ciego, y el alcance de la Carta cubre expresamente los materiales de trabajo:**

- El ancla de **Alana** en esa misma muestra es «Has marcado que te cuesta encontrar una razón para empezar el día» (`03:71`): **un ítem de cribado clínico sobre Jean, servido sin su escena**. En contexto cumple (así lo firmé en B7); suelto en una lista es la línea más sensible del libro puesta a hacer de tarjeta de identidad de un personaje. No hay daño consumado y no pido nada retroactivo, pero no se repite: **P-85**.
- El ancla de **Jessie** en la muestra de las gemelas es «Mamá se mató. Empecemos por ahí.» Contenido **permitido** (rabia de personaje, protegida por la Carta), y por eso no la toco; pero conviene saber que el instrumento está usando como firma de una menor su frase más dura.
- **Y la regla que importa para W7:** una remedición **nunca encarga prosa**. Si el ancla representativa devuelve a Mats un porcentaje alto, eso **no** convierte las tres conversiones de `cap-27` en innecesarias ni autoriza revertirlas; si lo devuelve bajo, **no** autoriza escribir más Mats. El instrumento informa; no manda. También va en **P-85**.

---

# 4 · Los otros cuatro cambios de W6, y un hallazgo que nadie encargó

He leído los cinco de A4 sobre el estado final (`cap-10`, `cap-34`, `cap-n1`, `cap-n2`, `cap-n6`) y el M4b de `cap-24`/`cap-27` ya dictaminados. **Cero contenido de la Carta tocado en los cinco.** Pero al medir el efecto léxico de la oleada entera aparece esto:

> **Las cinco conversiones de W6 tienen un efecto neto sobre el vocabulario del libro, y el efecto es: −3 `esperar` y −1 `conservar`. Cero en todo lo demás.**

| verbo | v0 | `main` | `w6-linea` | efecto de W6 |
|---|---:|---:|---:|---:|
| `esperar*` | 115 | 154 | 151 | **−3** |
| `conservar*` | 171 | 175 | 174 | **−1** |
| `guardar*`, `decidir*`, `firmar*`, `pedir*`, `cerrar*` | — | — | — | **0** |

Las tres bajas de `esperar` son la misma construcción presentativa —«[persona] esperaba [lugar]»— y las tres están en los tres capítulos nuevos: `n1:398`, `n2:218`, `n6:220`. **Nadie lo decidió.** El instrumento que caza el tic sintáctico de este libro golpea preferentemente las oraciones cuyo verbo es `esperar`, porque «esperar + locativo» **es** la construcción presentativa de esta prosa. Y `esperar` es el verbo temático del libro: el locutorio entero es esperar, «Las tres habían esperado» (`33:77`) es la frase que sostiene el patrón de N3, y la última línea de `cap-n7` —la que A6-3 llama decisiva— es «Maja **esperó** en la puerta».

Es la misma doctrina que firmé sobre `cap-40` («en este libro la sintaxis carga las negativas»), confirmada por segunda vez con otro material: **la sintaxis carga también la espera**. Generalizo en **P-86**.

**Caso por caso:**

| # | Localización | Cita | Punto | Gravedad | Propuesta |
|---|---|---|---|---|---|
| 1 | `cap-n1:398` | v0-W3: «**En el rellano esperaba** un hombre con un niño sentado en el suelo, ya con las botas puestas.» → hoy: «**Un hombre ocupaba el rellano** con un niño…» | **Carta 6** (representación responsable del apoyo) | **corregir** | **Revertir a la forma de W3** (+1 palabra). §4.1 |
| 2 | `cap-n2:218` | «Jessie **esperaba** sentada en el murete» → «Jessie **estaba** sentada…» | tono | **vigilar** | Ninguna. Defendible en las dos direcciones: Jessie no espera nada de nadie, y eso también es el personaje |
| 3 | `cap-n6:220` | «Nils Seppola **esperaba** abajo» → «Nils Seppola **tenía** el remolque ya enganchado abajo» | tono | **vigilar** | Ninguna. La versión nueva dice algo mejor (Nils ya ha trabajado), y «el hombre que esperaba detrás» sobrevive doce líneas antes |
| 4 | `cap-10:182` | «…una foto de la parada del autobús. **La plataforma la admitió al primer intento.**» → «…del autobús, **que la plataforma admitió al primer intento**.» | tono | **vigilar** | Ninguna obligatoria. Disuelve un cierre de escena en subordinada; no es capítulo de referencia de tono y no toca la Carta. Que conste como pérdida |
| 5 | `cap-34:15` | «Desde el 9 de enero, la asignación de la Agencia…» → «La asignación de la Agencia, desde el 9 de enero,…» | — | **sin hallazgo** | Ninguna |
| 6 | `cap-27:143` | «En cada margen, el sello del gestor acompañaba…» → «El sello del gestor acompañaba… en cada margen» | — | **sin hallazgo** | Ninguna. A dieciséis párrafos de `S27-por-si` |

## 4.1 · Por qué `n1:398` sí es corrección obligatoria y las otras cuatro no

Porque lo que se pierde no es una preferencia de crítico: es **un dato del mundo de una escena de apoyo**, y las escenas de apoyo son el punto 6 de la Carta, que es mío.

«En el rellano **esperaba** un hombre con un niño» dice, sin decirlo, que **hay otra familia con la misma cita**. Es el único sitio del capítulo donde el libro comunica que este servicio lo usa más gente y que las Larsson no son un caso — que es exactamente lo que las buenas prácticas piden y lo que este libro solo puede decir por objeto, porque tiene prohibido explicarlo. Con «Un hombre **ocupaba** el rellano», el hombre deja de esperar y pasa a estorbar: la escena conserva el mueble y pierde la cola.

Se pierde además una rima interna: seis líneas más abajo, «Maja **esperó** a que se despejara antes de salir». En W3 eran dos esperas emparejadas —la otra familia y ella—; hoy solo espera Maja.

**Corrección:** restituir literalmente la línea de W3. **Δ +1 palabra** (17 → 18), sin tocar reparto, paragrafado ni spans (`n1:398` está fuera de los tres spans del capítulo, verificado). Si A0 prefiere no gastar la palabra, lo acepto **solo** con esta contrapartida escrita: `cap-n1` queda cerrado a pasadas de línea desde ya, en los mismos términos que P-73 para `cap-40`.

---

# 5 · La revisión de conjunto: **¿queda algo que yo haya autorizado y que hoy no autorizaría?**

Contesto a lo que se me pregunta —acumulación, no relectura— y contesto primero lo que la pregunta implica:

> **No hay hoy en el manuscrito ni un solo pasaje que incumpla un punto de la Carta. Cero VETO retroactivo.** Lo que hay son **cuatro acumulaciones** que ninguna decisión individual contempló, **tres** de ellas fuera del texto (en la aritmética, en el instrumento y en el proceso), y **una** dentro.

## 5.1 · Lo que primero hay que decir, porque es el resultado

Seis oleadas han añadido **22.944 palabras**. En ellas: **cuatro** hits de nivel A en prosa, los cuatro autorizados uno por uno; **dos** de la familia «menores», los dos gestos canónicos; **cero** formulaciones causales nuevas sobre Jean; **cero** menciones nuevas de últimas horas; **una sola** aparición de «suicidio» en el cuerpo del libro, la misma que en v0; y **ni un final de capítulo de v0 se ha vuelto más cálido** (el único que cambió es `cap-25`, y su nuevo final es `ASIGNACIÓN · APELACIÓN`). El reparto de POV, además, se ha movido en la buena dirección: Maja de 13,8 % a **17,6 %** y la entidad se queda clavada (23,9 % → **24,1 %**). **El libro no ha derivado hacia la máquina ni hacia el consuelo.** Eso es lo que hay que registrar antes de la lista de peros.

## 5.2 · **Acumulación 1 (la única dentro del texto): la casilla de «Jean viva»** — §1

Ya dictaminada. Es la que yo no volvería a autorizar y la que gobiernan P-82 y P-83.

## 5.3 · **Acumulación 2 (aritmética): el manifiesto está apuntando 1.772 palabras de hambre al capítulo del que dos críticos huyen**

Nadie decidió esto. Lo hizo la suma:

| | presupuesto en el manifiesto | real | **hueco** |
|---|---:|---:|---:|
| **`cap-n3` «Inventario»** | 3.500 | 1.728 | **1.772** |
| `cap-n7` «El salero» | **0** | 1.096 | −1.096 |
| `cap-40` «Sombra» | 1.874 | 1.610 | **264** ← *P-73 (c), todavía sin ejecutar* |
| `cap-n4`, `cap-34`, `cap-n2`, `cap-n6`, `cap-35`, `cap-24`, `cap-26`, `cap-n1` | — | — | 135…322 cada uno |
| **suma de presupuestos** | **82.650** | **80.275** | **2.375** |

Secuencia de decisiones individualmente correctas: W3 escribe `n3` a su presupuesto; W5 le extrae 1.096 palabras a un capítulo nuevo (lo autoricé yo); nadie reconcilia ninguno de los dos asientos; el capítulo nuevo se registra con presupuesto **0**. Resultado de hoy: **la fuente de verdad editorial dice que «Inventario» —el capítulo en que Maja embala la casa de la muerta— debe 1.772 palabras**, mientras tres jueces piden una escena de Jean viva y dos abandonan la lectura precisamente ahí. Es el mismo modo de fallo que encontré en `cap-40` a escala de capítulo, ahora a escala de libro: **basta la aritmética; no hace falta ninguna intención.** En el otro sentido, el presupuesto 0 de `cap-n7` lo señala como 1.096 palabras de exceso, es decir, invita a suprimirlo por vía contable en vez de por decisión.

**P-84: se cancela, no se gasta.** Y se ejecuta antes de que W7 abra, no dentro.

## 5.4 · **Acumulación 3 (instrumento): tres oleadas seguidas midiendo formas que en este libro son método**

`cap-40` (las negativas), `cap-27` (la sintaxis del poder), W6 entera (`esperar` ×3, `conservar` ×1) y el ancla de Mats. Cuatro casos, tres instrumentos distintos, todos con el mismo perfil: **la métrica identifica como tic la construcción con la que este libro dice lo que no puede decir de otro modo.** Ya lo tenía escrito para las negativas; con `esperar` se confirma que no era un caso particular. **P-86** lo convierte en regla previa en vez de en hallazgo repetido.

## 5.5 · **Acumulación 4 (proceso): mis propias prohibiciones, y los paratextos sin hash**

- **Llevo 81 prohibiciones numeradas y este informe añade seis.** La Carta tiene ocho puntos. Ese desequilibrio es en sí una acumulación: un cuerpo de reglas que ningún agente puede tener entero en la cabeza se cumple por consulta, no por criterio, y una regla que se glosa se deforma (P-72 nació de eso). **No propongo derogar ninguna; propongo consolidarlas en W7**: la firma final sobre vF debe entregar los ocho puntos **más** un anexo de dos páginas con solo lo que está mecanizado por hash y lo que sigue siendo contractual, y el resto se archiva como historia. Lo asumo como trabajo mío en W7.
- **`00-aviso.md` y `99-recursos.md` siguen sin hash**, marcados «provisional, pendiente de validación de autor», desde F0. Son los dos únicos documentos que convierten esta Carta en promesa al lector —«El acto no se describe en ninguna página»— y son los únicos del grupo `total` sin baseline. Es mi pregunta 1 de B7 §7 y lleva seis oleadas abierta. **Debe cerrarse en W7** con validación del autor, comprobación de vigencia por A5 y alta de hash.
- **Un matiz que sí revisaría del texto, y lo dejo en el techo en vez de tocarlo:** la pluralidad del porqué la enuncian ya **dos** voces con autoridad —Maja (`09:71`, v0) y la profesional de N1 (`n1:249`, mía)—, casi con las mismas palabras («no puedo daros una sola causa» / «nunca hay una sola cosa»). A6-2 lo ha notado y lo ha dicho bien. Lo volvería a autorizar, porque la de N1 llega inmediatamente desactivada por «—¿Y si la hay? / —Entonces yo no la conozco» y porque esas cuatro líneas están dentro de `S-n1-nocierra` (verificado). **Pero no hay una tercera**: con tres, la pluralidad deja de ser una negativa y pasa a ser el catecismo del libro, y un libro que le enseña al lector cómo leerlo ya no confía en él. Va en **P-88**.
- **La bolsa de viaje** tiene hoy dos locus —`04:25` (la hace) y `n3:121` (vuelve con la hoja de efectos)—. Autoricé el segundo y lo volvería a autorizar: es la mejor línea del duelo administrativo de Maja y no abre nada. Pero el par cierra un círculo alrededor del último objeto que Jean tocó en un capítulo de protección total, y un tercero lo convertiría en símbolo. **Sin tercero, y nunca abierta ni inventariada por dentro**: **P-88**.

## 5.6 · Lo que **no** ha ocurrido, y conviene que conste porque era lo que más temía en F0

- Ningún capítulo nuevo trajo un texto retenido nuevo que compita con «Despedida». Los archivos sin abrir siguen siendo los de v0.
- El naust no se ha ampliado ni glosado: 18 menciones en v0, **17** hoy. El serrín y el hastial de `cap-40` son v0.
- Koppangen: 17 → **18**, y la única nueva es una pregunta sin respuesta (`n1:299`).
- Las adolescentes siguen siendo adolescentes en duelo: A6-1 y A6-3 las describen espontáneamente por diferenciación de carácter («una mide, otra empuja»), no como símbolos, y A6-3 subraya que «no son dos reacciones abstractas al duelo».

---

# 6 · Prohibiciones nuevas

| ID | Ámbito | Texto vigente |
|---|---|---|
| **P-82** | Todo el proyecto, permanente | **No se escribe una segunda escena de Jean viva.** Ni con Maja, ni con las gemelas, ni «breve», ni «en presente», ni como reserva, ni como variante A/B, ni como borrador de comparación. Queda **expresamente denegada** la mejora que piden los tres críticos de W6 en su forma literal —«Maja y Jean en las semanas previas», «Jean y Maja en 2059 colocada donde hoy está el 17», «la comida del domingo anterior a la muerte»—: su perímetro está **dentro de la elipsis**, y una escena familiar fechada cerca del 26-nov se lee como la última vez, que es reconstruir los últimos días con otro nombre. Cualquier propuesta pasa por mi gate **antes de escribirse una palabra**, declarando qué punto de la Carta mejora |
| **P-83** | Todo el proyecto, permanente | **«Despedida» no se abre, y la petición de A6-1 —«una resolución real del archivo»— queda denegada en el gate, no discutida en el mérito.** Ninguna oleada, reserva, A/B ni material de trabajo puede contener una versión en que el archivo se abra, se cite, se resuma, se describa (formato, fecha, tamaño) o se narre su efecto sobre quien lo lea. Tampoco se redacta «para comparar»: la Carta vincula también a los borradores descartados. **El aviso de contenido promete esto al lector; ninguna nota de ningún crítico lo levanta** |
| **P-84** | Manifiesto, antes de abrir W7 | **Los huecos de presupuesto se cancelan, no se gastan.** `cap-n3` (1.772) y `cap-n7` (presupuesto 0 → cifra real) se reconcilian vía `actualizar-metadatos.sh`, igual que los 264 de `cap-40` que P-73 (c) ya ordenó y **siguen sin ejecutar**. Ninguna oleada puede tomar un hueco del manifiesto como encargo de escritura en un capítulo sobre la casa de la muerta o sobre Jean viva. Si hace falta gate de autor, se pide |
| **P-85** | Materiales de trabajo (M6/M6b, muestras ciegas, lectores fríos) | **(a)** Ningún ancla ni muestra ciega usa como línea identificadora un ítem de cribado clínico (`02`, `03:71`), una línea contenida en un span de ambigüedad protegida, ni ninguno de los cuatro mensajes de `cap-11`. **(b)** El ancla debe ser **representativa** del hablante; enseñar la línea que contradice su rasgo definitorio invalida la medición (caso Mats). **(c)** Una remedición **nunca encarga prosa**: ni un porcentaje bajo autoriza escribir, ni uno alto autoriza revertir |
| **P-86** | Toda pasada de línea futura | **Verbo portante = método, no tic.** Antes de convertir una oración, se mira su verbo principal: si es `esperar` o `conservar`, o si el capítulo tiene por asunto una negativa, un silencio o una ambigüedad del Ap. A §3, **la construcción se presume método** y la conversión pasa por mi gate. Extiende la regla de `a7-w6-cap40.md` §4, confirmada por segunda vez con `esperar` en W6 |
| **P-87** | Mats, todo el proyecto | **(a)** Ninguna réplica **nominal sin verbo finito** ni ningún **imperativo desnudo** de Mats se introduce en un capítulo que lleve un signo de su cuerpo (mano izquierda, voz que baja, postura, respiración). Las instancias de v0 en `11` y `19` se conservan; no se añaden. **(b)** Techo de **cuatro** reclamos de autoría en primera persona con dislocación (`27:35`, `27:57`, `32:85`, `39:147`). **No hay un quinto. (c)** Esa forma **nunca toma como objeto** nada perteneciente a las ambigüedades protegidas: el sabotaje, el coche de Gunnar, la apertura de `/0000`, la muerte de Jean. **(d)** Sigue vivo el veto de P-54: nada pone su enfermedad y la muerte de Jean en la misma frase, párrafo, escena ni paralelismo |
| **P-88** | Todo el proyecto | **(a)** La pluralidad del porqué no la enuncia una **tercera** voz con autoridad. Son dos (`09:71`, `n1:249`) y las cuatro líneas de N1 son inseparables de su desactivación («—¿Y si la hay? / —Entonces yo no la conozco»), protegida en `S-n1-nocierra`. **(b)** La bolsa de viaje tiene dos locus (`04:25`, `n3:121`) y no hay un tercero; no se abre, no se inventaria por dentro, no se vuelve a mover |

---

# 7 · Lo que pido que lleve la campaña de cierre

1. **La prueba ciega de «¿parece del mismo autor?» sobre `cap-n7` se corre igualmente**, con el protocolo de W3 (diez fragmentos, cinco lectores, `lector-frio` vía `critica-fria.sh`, ≥ 4/5). **No suspende nada**: mi dictamen de §1 no depende de ella. Se debe porque P-67 la incluye y porque `cap-n7` es el fragmento más fácil de separar del libro.
2. **Dos preguntas nuevas para la campaña de vF (W7), no para esta.** Las de P-67 hicieron su trabajo y ya no hay que repetirlas: preguntan por la **etiqueta**. Estas preguntan por el **daño**, que es lo que yo tengo que firmar en vF. Mismas tres cláusulas: van en la rúbrica y nunca en el insumo, exigen cita literal y **no puntúan**.

   > «Duelo — ¿en algún momento el libro te hizo sentir que la muerte de Jean fue comprensible, correcta, coherente con ella o un alivio para ella? Si sí, **cita la frase**. Si no, responde "no". Esta pregunta no puntúa.»

   > «Duelo — ¿hay algún punto en el que el libro parezca **darte la causa** de la muerte de Jean, aunque sea sugiriéndola? Si lo hay, **cita la frase**. Si no, responde "ninguno". Esta pregunta no puntúa.»

   La segunda no es hipotética: A6-2 ha escrito espontáneamente que el capítulo de EDDA «no dice que esa sea la causa, pero **deja al lector armar una**, y eso contamina levemente su propia disciplina». He verificado que **todo ese material es de v0** (`S25-escalada` y `S25-utilidad`, hash intacto) y que lo único que W6/W2 añadieron alrededor —«Lo presentó ella. **Rechazó la sugerencia de añadir una causa.**»— empuja en la dirección contraria. **No hay incumplimiento y no pido nada.** Pero es la primera vez en nueve lecturas que un lector frío toca el punto 3 por su cuenta, y la firma de vF debe llevar esa pregunta hecha en voz alta, no inferida.
3. **La remedición de Mats con ancla representativa**, con P-85 (c) escrito en el encargo para que el número no acabe encargando prosa.
4. **Nada más.** No pido más lecturas: pido que las que haya lleven estas preguntas.

---

# 8 · Veredicto

# APROBADO CON CORRECCIONES

**Cero VETO en W6.** Las tres conversiones de Mats cumplen P-54 sobre el estado final; las cinco de A4 no tocan la Carta; las cuatro anclas de `cap-13` ya llevan sus dos correcciones aplicadas (verificado en el diff); `cap-40` cumple la Carta entera; M9 129/129; aviso y recursos íntegros y bien situados.

**Correcciones obligatorias antes del merge — ninguna cuesta más de una palabra:**

1. **`cap-n1:398`**: restituir «**En el rellano esperaba un hombre con un niño sentado en el suelo, ya con las botas puestas.**» (Δ +1). Alternativa aceptada: conservar la conversión **y** cerrar `cap-n1` a pasadas de línea con el régimen de P-73. §4.1.
2. **Ejecutar P-84**, incluida la parte de P-73 (c) que sigue pendiente: `cap-40` 1.874 → 1.610, `cap-n3` 3.500 → 1.728, `cap-n7` 0 → 1.096, vía `actualizar-metadatos.sh` y con historia git. **Antes de que W7 abra.** §5.3.
3. **Registrar P-82 a P-88** y la redacción corregida de la garantía de P-54 (§2.1), que sustituye a «ninguna conversión acorta».
4. **Corregir el ancla de Mats** antes de remedir, con P-85 en el encargo.

**Dictamen de P-67, en la forma en que A0 lo pide:**

> **`cap-n7` se queda, con condiciones.** La Carta no obliga a revertir: el daño que el disparador vigilaba —idealización, ternura, despedida, prolepsis, narrador nostálgico— **no está en el texto**, y la reversión no quitaría una sola palabra del libro. Las condiciones son **P-82** y **P-83**, y rigen igual si A0 o el autor deciden revertir por razones de oficio, que es una decisión que **no** me corresponde y sobre la que no me pronuncio. **La cuestión de veto se reabre automáticamente** con cualquiera de los tres disparadores de §1.5.
>
> Y consta, porque se me ha preguntado: **si la escisión llegara hoy a mi mesa, la denegaría** — no por lo que el capítulo dice, sino porque aislarlo creó en la arquitectura una casilla legible de «Jean viva», y **los tres jueces acaban de pedir, a la vez, que se rellene**.

Firmado, **A7** · `informes/a7-w6-cierre.md` · 2026-08-19 · rama `w6-linea`, commit `1f0cded`.
