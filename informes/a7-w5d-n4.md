# A7 · W5d · `cap-n4` tras la vía A — dictamen de sensibilidad y juicio sobre el capítulo

**Firma:** A7, revisor de sensibilidad (veto absoluto; Ap. F del plan, B7 §2 y §8) · **Fecha:** 2026-08-19
**Objeto:** `git diff HEAD~1 HEAD -- capitulos/cap-n4.md` (commit `578d963`, 7 hunks, +9/−49 líneas, **−225 palabras**), leído contra `cap-n4.md` **íntegro** en su estado final (369 líneas, 2.181 palabras de cuerpo con `wc -w`).
**Insumos leídos:** `cap-n4.md` completo; el diff; `cap-n4.md` en `HEAD~1` y en `c27a5be` (la versión de W3, para las verificaciones de origen); `cap-10.md` (:19, :119, :145, :181, :195–:215), `cap-21.md:85–99`, `cap-22.md:45`, `cap-26.md`, `cap-28.md:150–180`, `cap-32.md` (spans); `capitulos/cap-n1.md`, `cap-n2.md`, `cap-n3.md`, `cap-n5.md`, `cap-n6.md`, `cap-n7.md` **completos** (para el encargo de blindaje); `ordenes/OT-N4.md` §«Los diez cortes» y §«La operación a ±0»; `informes/w5-cap-n4.md`; `biblia/b4-ledger-chekhov.md` (CH-27, CH-28), `biblia/b7-carta-sensibilidad.md`; `protegidos/spans.json`; `informes/w6-plan.md` §5 y §6 bloque 0; `informes/w6-decisiones-a0.md`; mis dictámenes previos `a7-w3-n4-n5.md`, `a7-w4r.md`, `a7-w4b.md`, `a7-w5-n3.md`, `a7-w5c-espejo.md`.
**Herramientas:** `sensibilidad.sh --solo cap-n4.md` → **0 hits de nivel A**, 9 de nivel B, **los mismos nueve de siempre** (`hoja` ×3 papel, `agua` ×2, `coche` ×2 el gris, `muslo` ×1 gesto canónico de `20:233`, `puente` ×1 Tromsøya), verificados uno a uno en su nueva numeración. `proteger.sh verificar` → **M9 OK, 8 ficheros, 113 spans**.

---

## 0. Verificaciones, primero

Todas por **hash de contenido**, no por número de línea. En este fichero conviven ya **cinco** numeraciones (W3, post-poda W4-R, post-G-1, post-excisión y hoy): A0 me ha citado `:361` y `n4:85`, que hoy son `:321` y `:71`. Los literales coinciden; los números no. Mantengo mi regla: **en `cap-n4` nada se cita por línea.**

| Qué | Método | Resultado |
|---|---|---|
| **Escena 3 completa** (de «La notificación entró en el terminal de Maja a las tres y veinticinco.» a «—Ahora bajas la caja del altillo.») | `sha256` del rango por patrón, hoy vs `HEAD~1` | `39ce6267…` = `39ce6267…` **byte-idéntica** |
| **P-38** · las cuatro réplicas | `sha256` del rango, hoy vs **`c27a5be` (W3)** | `013f6871…` = `013f6871…` **byte-idénticas desde el día que se escribieron** |
| **Bloque N4-1 + sus dos tampones** (de «Astrid no preguntó nada más…» a «Las habitaciones que daban a la calle…») | `sha256`, hoy vs `HEAD~1` vs **W3** | `1b609c66…` en las tres **byte-idéntico desde W3** |
| **P-65 (c)** · «Nora dejó el cuaderno pautado sobre la funda y volvió a cogerlo.» | literal + vecinos | verbatim, en su párrafo, dentro del bloque anterior |
| **Ruta de marzo (G-1)** | `sha256` del bloque, hoy vs `HEAD~1` | `a2ab0495…` = `a2ab0495…` **intacto** |
| **Ancla de A7** «Nora contó los días… las mañanas que su madre tendría que dejar libres.» | literal + vecinos | verbatim, mismos vecinos |
| **P-49** · «La responsable escribió algo corto y no lo leyó en voz alta.» | literal + vecinos | verbatim, mismos vecinos |
| **Final del capítulo** (14 últimas líneas) | comparación directa hoy vs `HEAD~1` | **idéntico**. Cierra sobre réplica; «Y el cuaderno.» verbatim |
| **Bloque del rellano** (las 4 réplicas sustituidas) | `wc -w` hoy vs `HEAD~1` | **19 → 19. ±0 exacto**, confirmado |
| **Escena 4** | `wc -w` | 668 → 658 (−10 = D-10, y nada más) |
| **Total cuerpo** | `wc -w` | 2.406 → 2.181 (**−225 exacto**) |

**Ninguno de los siete hunks toca la escena 3.** Confirmado, y confirmado además que no la tocan *por los bordes*: el corte más próximo (D-10) cae tres párrafos por encima del tampón superior de N4-1, y el hunk 7 vive 30 líneas por debajo del cierre de la escena 3.

**P-64 · el aparato de anonimato, los cinco loci, uno a uno:** `responsable desconocido` (:51, conservado expresamente por D-3, y eco exacto de `cap-10:201`) ✓ · `No consta responsable individual.` ×2 en sus dos orígenes (:91, :231) ✓ · la pregunta de Jessie sin respuesta (:235–:241, Maja tiende la mano y no contesta) ✓ · P-49 (:175) ✓ · `cap-32:93`, hoy cubierto por `S32-resumen` ✓. **Nada se glosa, se contesta ni se atribuye.**

---

## 1. Tabla de hallazgos

| # | Locus | Cita / hecho | Punto de la Carta / condición | Gravedad | Propuesta mínima |
|---|---|---|---|---|---|
| **H-1** | hunk 7, bloque del rellano | «—Mañana lo miramos.» → **«—Te llevo yo.»**; «—Las entregas. Ya veremos cómo.» → **«—Lo firmo el viernes.»**; «Y el impreso.» | 7 (P-6, P-26) · tono | **cumple** | Ninguna. Ver §4: **no es un cambio de paragrafado**, es la única intervención del día que *añade* sentido, y el parte de A0 no me la nombró. Está declarada en `OT-N4` §«La operación a ±0»; el gate la ha cazado leyendo el texto, que es como debe ser |
| **H-2** | hunk 2 (D-4) | desaparece «Bajo `datos` quedaron las dos cosas del día… **No abrió `hipótesis`.**» | 7 (P-6) | **cumple**, con reconstrucción | Ninguna. Era **una de las tres razones** por las que dictaminé en W5c que P-6 no se disparaba. Se cae la razón, no el dictamen: lo rederivo entero en §5 sobre las que quedan y sobre dos nuevas. Lo registro porque una condición sostenida por una prueba que ya no existe es una condición que nadie puede volver a comprobar |
| **H-3** | hunk 1 (D-1) | desaparece «El álbum había vuelto al menú… **las ocho de diciembre** no estaban en ninguna parte.» | 7 · Ap. A §3 (ordenante) · CH-27 | **cumple** | Ninguna, y **el eco no vuelve**: §3. Su función sobrevive en el capítulo en una forma mejor (`:23` y `:369`), y su forma vieja era una tercera comprobación forense en boca de una menor |
| **H-4** | hunks 3, 5, 6 (D-5/D-6/D-7/D-10) | desaparecen las tres dramatizaciones de «los papeles no coinciden entre sí» | 3 · Ap. A §3 (ordenante) | **cumple**, con matiz | Ninguna. **No mejora la pluralidad tanto como podría parecer** (las discrepancias de referencia también apuntaban a maquinaria y no a mano), pero **tampoco la daña**, y deja en pie la figura correcta: la **identidad** de la frase en dos papeles de origen distinto, dicha una sola vez, por una menor, y **sin respuesta**. Ver §2.2 |
| **H-5** | `cap-n4` completo | Tras cuatro operaciones, la figura dominante del capítulo es **«alguien anota un dato en el reverso de algo»**: `:51`, `:77`, `:195`, `:267`, `:323`, `:361`. **Seis ejecuciones** | tono · 7 | **vigilar** + condición | **P-70**: tres de las seis son intocables por Carta (`:51` = P-64; `:267` = la rabia de Jessie convertida en archivo y no en publicación, que es el coste del punto 7; `:323`/`:361` = T3, el interior de Maja por objeto). Si alguna oleada decide que esta figura también se repite, **las candidatas son `:77` y `:195`, y pasa por mi gate antes** |
| **H-6** | `cap-n4:287` ↔ `:309` | «El de la cuenta de Nora era una captura de cuatro líneas. **La habían impreso en el instituto**…» ↔ «colocó **la hoja del instituto la cuarta en la fila**» | — (legibilidad, no Carta) | **vigilar**, sin acción | **Preexistente desde W3** (verificado en `c27a5be`), no lo introduce este diff, no roza ningún punto de la Carta y ha pasado seis lecturas frías sin comentario. **Recomiendo expresamente NO reabrir el capítulo por esto.** Queda anotado para A5/A1 en W7, donde ya se abre el fichero por otras razones |
| **H-7** | `cap-n7` | `proteccion: nucleo` + tres spans internos; **no existe span de los dos extremos del capítulo** | **P-56** | **corregir** | **P-56 no está cerrada.** Ver §6. Se cierra con un span más, aditivo y sin gate |
| **H-8** | `cap-n4` frontmatter | `delta_objetivo: +3200` en un capítulo de 2.181 palabras sometido a regla de parada | manifiesto · gobernanza | **vigilar** | Mismo razonamiento que la corrección H-1 del informe anterior (el campo `pov` que declaraba una escena inexistente): un frontmatter que anuncia un déficit de mil palabras es **una invitación escrita a rellenarlo**. A0/A1 deciden la vía; sin efecto de Carta |
| **H-9** | `cap-n4:349` | «—Te llevo yo.» junto a `n1:263`, `n1:343` y `28:163` | tono (moldes) | **vigilar** | Cuarta instancia de «Maja entrega su tiempo en forma de trayecto». **Desde mi silla es una virtud, no un tic**: es la única manera que este personaje tiene de decir que las quiere, y T3 lo exige. Lo dejo contado para el censo de moldes de W6 para que nadie lo «resuelva» sin saber lo que quita |

**Cero hallazgos de gravedad VETO. Una sola corrección obligatoria (H-7), y no toca una palabra de ningún capítulo.**

---

## 2. Punto 1 de A0 · qué es hoy este capítulo

A0 me pide juicio sobre el capítulo, no sobre la legalidad de cada corte. Se lo doy, con la advertencia de siempre: **no puntúo ritmo y no recibo puntuaciones de A6.** Lo que sigue es lectura, no medición.

### 2.1 · Lo que ha dejado de ser, en cuatro pasos

Este capítulo ha perdido, por este orden, cuatro cosas distintas:

1. **La poda de W4-R** le quitó *palabras de más*.
2. **G-1** le puso una ruta —la convocatoria de marzo, el impreso, la firma, el veintiocho— que le dio a Nora algo que perder que no era una cuenta.
3. **La excisión del espejo** le quitó su **órgano explicativo**: la escena donde el narrador enseñaba cómo funcionaba el daño.
4. **Hoy** le ha quitado su **órgano demostrativo**: las tres veces que probaba una tesis que ya había probado.

Lo que queda no es un capítulo mutilado. Es un capítulo al que le han quitado, en dos operaciones consecutivas, **las dos partes que hablaban en nombre del libro**. Eso es exactamente el movimiento hacia v0 que la Carta llama contención: los capítulos de referencia (4, 9, 23, 40) no explican y no demuestran; registran y se callan.

### 2.2 · Lo que es

**Es el día en que una familia deja de poder usar los canales ordinarios, y hace una caja.** Cuatro bloques, un solo día, todo contado por documentos y por la gente que los recibe: el instituto, el trabajo, la policía, y la mesa de la cocina donde los tres papeles se ponen en fila.

Su motor ya no son «tres acosos». Su motor es **una frase que aparece en dos documentos de origen no relacionado y que no firma nadie**, leída en voz alta por una chica de dieciséis años, seguida de una pregunta —«¿Y les sale la misma frase?»— que su madre no contesta: tiende la mano y le pide el papel. Es la mejor página del capítulo y hoy es también su única figura.

Y hay tres cosas que este capítulo hace, en 2.181 palabras, que muy pocos capítulos del libro hacen a la vez:

- **No nombra a la muerta ni una sola vez.** Verificado: `Jean` no aparece; la única «madre» del capítulo es Maja, en la frase donde Nora cuenta las mañanas que tendrá que dejar libres. Un capítulo entero sobre el precio de ser esa familia, sin usar el nombre que lo explicaría todo.
- **Deja que una menor enuncie la tesis del libro y se niega a que un adulto se la confirme.** La autoridad narrativa que hay en la escena —Astrid— responde «Los incorporo como están, **sin traducir**». Es la formulación más limpia de la Carta 3 que he leído en un capítulo nuevo.
- **Termina en un objeto que es de la chica y no del caso.** Una cría que estuvo a punto de meter su cuaderno de piano en la caja de las pruebas y se lo quedó; y una madre que, al hacer la lista de lo que hay que llevarse, dice «Ropa para una semana. Y el cuaderno.»

### 2.3 · Lo que hoy me preocupa de él, y no es la sensibilidad

Es H-5. El capítulo ha quedado corto y limpio, y a esa escala **se oye su gesto**: seis veces alguien apunta un dato en el reverso o en el margen de algo. Es la respuesta del libro al borrado —el papel sobrevive a lo que la plataforma no— y por eso es el gesto correcto; pero un lector que abandone este capítulo hoy lo hará por ahí, no por los tres acosos.

Digo esto para que sirva de aviso y no de encargo: **la corrección de esto no es otro corte.** Tres de las seis instancias son mías por Carta, y las otras dos son las que sostienen la escena 1 y la escena 2. Un capítulo puede permitirse un gesto dominante; lo que no puede permitirse es una quinta operación.

### 2.4 · Sobre la regla de parada

**La suscribo, y la hago vinculante desde mi lado** (P-69, §8). Cuatro operaciones sobre un mismo capítulo es el límite de lo que se puede hacer sin que la última deje de mejorarlo. Este capítulo está terminado. Mi juicio: **hoy se sostiene solo**, y es mejor que ayer por la misma razón por la que ayer fue mejor que anteayer — porque cada vez habla menos en nombre del libro.

---

## 3. Punto 2 de A0 · el eco de `cap-10:207`, «las ocho de diciembre»

**Dictamen: no vuelve. Su ausencia es preferible.** Razono, porque la pregunta es buena y la respuesta fácil sería la contraria.

**Qué era.** «El álbum había vuelto al menú. No contenía nada. El historial de cargas empezaba aquella mañana y las ocho de diciembre no estaban en ninguna parte.» Cierra el arco de `cap-10:145` («—Eso no borra las ocho cargas.») y de `cap-10:207` (el álbum que desaparece del menú). Es, además, parte de la restitución con que `b4` da **CH-27 por PAGADO**.

**Por qué no vuelve, en orden de peso:**

1. **Su función ya está en el capítulo, y en mejor forma.** Lo que la frase decía es: *la plataforma borra; el papel no*. El capítulo lo dice dos veces sin comprobar nada. En `:23` —«El cuaderno pautado seguía en el fondo de la mochila, entre los ejercicios de armonía.»—, que es eco casi verbatim de `cap-10:213` («Metió el cuaderno entre los ejercicios de armonía. En el papel, las dos series seguían enteras.»). Y en `:369`, la última línea del capítulo. **Un objeto en una mochila y una madre que lo nombra al hacer el equipaje valen más que un historial vacío**, y no cuestan una comprobación.
2. **Su forma era una tercera comprobación forense en la primera página.** Nora abriendo el calendario, contando las palabras del aviso y *además* auditando el historial de cargas. Toda la operación de hoy consiste en quitarle a esta chica trabajo de perito. Devolver nueve palabras de perito para recuperar un eco es deshacer la operación en el sitio exacto donde más se nota.
3. **La restitución no queda huérfana.** `:15` («La plataforma admitió las credenciales de Nora al primer intento.») y `:17` («Las entregas de diciembre figuraban recibidas, con la fecha de cierre al lado.») la muestran entera y por donde le importa al lector: sus notas. **CH-27 sigue pagado**: restitución a primera hora, re-suspensión a las 11:52 con las palabras literales de `10:205`/`10:213`. Lo que se pierde es que la restitución fuera además *hueca*, que es un refinamiento de una crueldad ya completa.
4. **La figura «la cuenta escolar vacía» ya está en el libro, es de v0, y va delante.** `cap-21:95` («Jean retiene una cuenta escolar vacía»), orden de lectura 21 < 25,5, capítulo `nucleo`, con su propia vacuna en el párrafo anterior («Jean ignora si Jessie la ha enviado… **No añade una palabra íntima.**»). N4 era el eco; la siembra sigue en pie. Es el mismo argumento con el que aprobé la excisión del espejo, y aquí vale igual.
5. **Menor, pero cuenta:** un historial que empieza esa mañana es un rastro borrado, y un rastro borrado insinúa una mano que borra. Es débil —cabe leerlo como reinicio automático— pero apunta en la dirección contraria a P-64. No es la razón, es la confirmación.

**Y una advertencia sobre dónde NO puede volver.** Si alguna vez alguien decide recuperarlo, la tentación será decir qué se perdió: la fotografía de las gemelas con nueve años y su madre detrás con la cara cortada. **Eso no se escribe.** Convierte un borrado administrativo en la pérdida de la última foto de la muerta —elegía— y además roza el material del noveno cumpleaños, que es ambigüedad protegida (Ap. A §3). La frase original tenía el mérito de ser abstracta. Cualquier versión «recuperada» sería peor que la original, y la original ya no hace falta.

---

## 4. Punto 4 de A0 · el paragrafado, y lo que el parte no me dijo

**El dato de A0 es correcto: D-9 es la única fusión de párrafos del diff.** Lo he verificado hunk por hunk. Cuatro réplicas de la responsable se convierten en una porque, si no, quedaban dos seguidas de la misma hablante. La alternancia se conserva, «—¿Qué evalúa?» y «—¿Y qué te han devuelto?» quedan verbatim en sus párrafos, ningún otro párrafo se funde, se parte ni se reordena en todo el fichero. Desde la enmienda a G-3, esto pasa.

**Pero el hunk 7 no es paragrafado.** Es una sustitución de contenido: cuatro réplicas del rellano cambian de sentido a ±0 palabras exactas (19 → 19, verificado). Está **declarada en `OT-N4` §«La operación a ±0»** con su razonamiento completo, así que no es una intervención oculta; lo que no estaba es en el parte que A0 me pasó, donde la única entrada de esa naturaleza dice «un cambio de paragrafado declarado… Es el único». Lo señalo por una razón operativa y sin reproche: **es la única intervención del día que añade sentido en vez de quitarlo, y es la que cambia lo que una madre le promete a su hija en duelo.** Es exactamente la clase de línea que mi gate existe para leer. La leí porque leo el capítulo y no el parte; si alguna vez el parte fuera el insumo único, esto habría pasado.

**Dictamen sobre el hunk 7: cumple, y es bueno.** Cuatro razones:

- **Baja la adultización.** El impreso —la única gestión que Nora llevaba sola— pasa a la madre. Nora deja de administrar su propio expediente y se queda con lo que le toca: dos hojas de deberes y una pregunta.
- **No toca el techo institucional.** Los que no pueden hacer nada en este capítulo son las instituciones («Desde aquí no puedo hacer más», «Entonces dura», «Hasta que se aclare»), y ninguna de esas líneas se mueve. La que decide es la madre, que no es una institución. El capítulo sigue sin ofrecer remedio.
- **El precio está puesto, y puesto tarde.** Maja promete el trayecto en el rellano; treinta líneas después el texto dice «dos horas de carretera y un desvío sin salar», sin conectar las dos cosas. El lector hace la resta o no la hace. Eso es técnica de v0, y es lo contrario de consolar.
- **No hay milagro ni cierre.** La escena no termina en la promesa: termina en «El de la gasolinera sabe dónde vivimos», en una matrícula anotada y en una calle comprobada en los dos sentidos.

**Continuidad, que nadie me pidió y que una promesa nueva obliga a mirar:** «Lo firmo el viernes» → el viernes es `cap-28` (2061-01-07), donde Maja pregunta por la fecha de la repesca y dice «Te dejo las mañanas»; la firma no exige viaje (el impreso lo lleva Nora: «—¿Puedo llevarlo yo? —Firmado.») y el plazo es el veintiocho. «Te llevo yo» → el martes 4 de enero está elidido entre `cap-26` y `cap-27`. **Ninguna de las dos promesas queda desmentida por el libro.**

---

## 5. Punto 3 de A0 · P-6 y P-26 sobre el estado final

Es la pregunta correcta y la que más me importa de las cuatro. El riesgo declarado (`w4r-diagnostico-centro` §b) es: **quitar textura y dejar competencia administrativa sube la adultización quitando palabras.** Lo he comprobado en las dos direcciones.

### 5.1 · Qué se quitó, clasificado

| Corte | Qué era | Efecto sobre P-6 |
|---|---|---|
| D-1 | tercera comprobación de la mañana (el historial de cargas) | competencia **−1** |
| D-3 | las dos horas con su referencia de incidencia, la línea subrayada | competencia **−1** |
| D-4 | `datos` / `hipótesis` / «No abrió `hipótesis`» | competencia **−1**, y **la marca de contención −1** (H-2) |
| D-5 | «con seis minutos de diferencia y dos referencias distintas» | competencia **−1** |
| D-10 | «Distinta. Se separan en el cuarto grupo.» | competencia **−1** (trabajo de perito puro) |
| D-6 | la ficha girada de la tutora | techo institucional −1, **pero** `:61` («Desde aquí no puedo hacer más») lo dice mejor y sigue |
| hunk 7 | el impreso pasa a Maja | competencia **−1** |

**Textura retirada: ninguna.** Las tres líneas no administrativas de la escena 1 siguen enteras: `:23` (la luz azul, el charco con forma de bota, el cuaderno entre los ejercicios de armonía), `:19–:21` (Mikkel, «Ya me va»), `:39` (alguien mira el mural y después a Nora, en ese orden). En proporción, la escena 1 pasa de 3 beats de textura en 507 palabras a **3 en 376**: la densidad de textura **sube**.

**Conclusión: el modo de fallo que A0 temía no se ha producido. Ha ocurrido lo contrario.** Se han retirado seis beats de competencia y cero de textura.

### 5.2 · Rederivación de P-6, porque una de mis tres razones ya no existe

En W5c sostuve que P-6 no se disparaba por tres razones. La tercera —«sigue sin abrir `hipótesis`»— **se la ha llevado D-4** (H-2). No la echo de menos, y explico por qué: `No abrió \`hipótesis\`` era el gesto por el que Nora *renunciaba* a teorizar; pero renunciar a teorizar exige antes montar el aparato de teorizar. Sin aparato no hay renuncia que mostrar, y lo que queda en el cuaderno es más pequeño y más terco: una fecha debajo de otra fecha y una palabra, `responsable desconocido`, que es eco literal de `cap-10:201`. El método sigue siendo el de la cría de `cap-10` —está protegido allí por `S10-conservar` y `S10-series`, en fichero `nucleo`—; lo que N4 conserva es el único campo que importa. **Menos protocolo y el mismo hilo.**

**P-6 · NO se dispara.** Razones vivas, sobre el estado final:

1. **`:71` es el mayor beat de interioridad de Nora en el capítulo, y no es competencia: es contabilidad de culpa.** «Nora contó los días que faltaban para el viernes. Después contó las mañanas que su madre tendría que dejar libres. La secretaría abría de nueve a una.» Una cría calculando lo que va a costarle a su madre. Diff 0 desde G-1, con los mismos vecinos.
2. **`:321` sigue siendo el gesto que la mantiene con dieciséis años y no con cuarenta**, verbatim y con paragrafado congelado (P-65 (c) honrada al pie de la letra).
3. **Nora está fuera de su terreno y el texto lo enseña.** «—Podemos ir a un hotel» es una propuesta ingenua que la madre corrige en cinco palabras («Un hotel pide un nombre»). Y en la mesa: «No puedo imprimir nada. Ni entrar. **La captura de esta mañana la hizo la tutora.**» Nora no resuelve: depende.
4. **Ningún adulto arregla nada y ninguno explica.** El techo institucional está entero.
5. **Lo de Jessie sigue terminando en derrota.** Escena 3 byte-idéntica desde W3: no publica, archiva tres copias fechadas, y cierra con «Yo tengo un vídeo de ayer que no puedo enseñar.»
6. **(Nueva)** El impreso —lo último que llevaba sola— **se lo lleva la madre** en el hunk 7.

**P-26 · intacta.** El coste de la ausencia de Nora no deriva en ideación, autolesión, conducta de riesgo eficaz ni «señales» retrospectivas; ninguna figura adulta lo explica, lo cura ni lo culpa. El capítulo no contiene nada de eso y los tres pases acumulados no han acercado nada a nada.

**Punto 7 en conjunto: cumple, y con más margen que antes de la operación.** Nada sexualizado, ningún cuerpo mirado, ningún riesgo nuevo, ninguna eficacia gratuita, el único riesgo lo prohíbe un adulto y se obedece con rabia.

---

## 6. P-56 **no está cerrada**, y hay que decirlo hoy

A0 me da P-56 por cerrada. **No lo está**, y la diferencia importa porque es exactamente el tipo de fallo que P-56 existía para prevenir.

Lo que hay hoy en `cap-n7`: `proteccion: nucleo` y **tres spans internos**, cada uno con `inicio` y `fin` —la taza reparada, la línea de C-4.3 y la siembra de CH-8—. Es trabajo bueno y son las tres líneas correctas. Pero P-56 dice otra cosa:

> «Su span M9 **se define con los dos extremos** —de «Alana venía a cenar cada dos o tres meses y siempre llegaba tarde.» a «Maja esperó en la puerta hasta que salió del camino.»— **para que cualquier añadido en cabeza o cola rompa el hash**.»

«Los dos extremos» son **los del capítulo**, no los de cada span. La ambigüedad es mía y la asumo, pero el efecto es real y es medible: **hoy, un epígrafe entre el título y «Alana venía a cenar…», una marca de analepsis, una fecha, o una coda detrás de «Maja esperó en la puerta hasta que salió del camino.» pasan M9 limpiamente.** Y `proteccion: nucleo` no lo impide: el hook `PreToolUse` bloquea Write/Edit sobre `proteccion: total`, no sobre `nucleo`. El `w6-plan` §6 bloque 0.1 lo escribió bien («`cap-n7` **con los dos extremos**… y pasa a `proteccion: total`»); lo ejecutado es la mitad.

**Corrección obligatoria (H-7), aditiva, sin gate, sin `--rebaseline`, sin tocar los 113 spans vigentes:**

```
id:      S-n7-perimetro
archivo: capitulos/cap-n7.md
inicio:  Alana venía a cenar cada dos o tres meses y siempre llegaba tarde.
fin:     Maja esperó en la puerta hasta que salió del camino.
desc:    P-56 · diff 0 perpetuo del capítulo aislado. Cubre el cuerpo entero:
         cualquier añadido en cabeza o cola, o cualquier cambio interior,
         rompe el hash. Los dos extremos son los del CAPÍTULO.
```

Los dos literales son **únicos** en el fichero (verificado). Con eso P-56 pasa de contractual a mecánica, que es la razón por la que la escribí. El paso a `proteccion: total` es decisión de A0 (campo del plan) y sería el cinturón sobre el tirante; el span solo ya cierra la condición.

**Y de aquí sale la doctrina que corrige mi propia especificación**, y que vale para todo lo que sigue: **un span de sensibilidad se define con `inicio` y `fin` que son las líneas *tampón*, una por encima y otra por debajo del material protegido.** Un span que empieza en la primera línea protegida es ciego a lo que se inserte justo delante. Es el fallo de `S14-firmo`, de `S40-locutorio` y de `S32-amenaza`, y no lo voy a repetir en catorce spans nuevos.

---

## 7. Encargo de A0 · qué línea de cada capítulo nuevo hay que blindar

A0 tiene razón en que esto es mío. Lo he hecho leyendo los seis capítulos completos, no buscando mis propias condiciones. Criterio único: **¿qué línea, si desaparece, se ablanda o gana un vecino, rompe la Carta o cierra una ambigüedad protegida?** No blindo lo que me gusta; blindo lo que no se puede perder sin que el libro cambie de posición moral.

Todos con **tampones**: `inicio` y `fin` son las líneas de fuera. Todos los literales verificados **únicos** en su fichero (`grep -Fc` = 1), salvo donde se indica. Catorce spans nuevos + `S-n7-perimetro` = **128**.

### `cap-n1` «La primera cita» — **tres, y no menos**

Es el capítulo donde la Carta es más espesa: el único donde una profesional habla de duelo por suicidio, y el único escrito contra un pliego que es 90 % prohibiciones. Es también el que una pasada de línea «cálida» estropearía sin darse cuenta.

| id | inicio (tampón) | fin (tampón) | qué protege |
|---|---|---|---|
| `S-n1-nocierra` | `Nora dejó el abrigo doblado en la silla de al lado, con el terminal boca abajo encima, y se sentó sobre las manos.` | `Jessie volvió y se sentó en la misma silla. El cordón de la capucha le colgaba deshecho y las botas habían dejado dos marcas de agua en el suelo.` | **Carta 3, literal.** «—Que la pregunta no se cierra.» / «—Eso no es un dato.» / «—No tengo otro.» / «—En lo que he visto, nunca hay una sola cosa.» / «—¿Y si la hay? / —Entonces yo no la conozco.» Es la frase más cargada del libro entero: la única voz con autoridad que se pronuncia sobre el porqué, y lo hace para decir que no hay uno. **Si esto se suaviza, el libro cambia de tesis.** |
| `S-n1-casitodos` | `En la mesa, el cerco de un vaso anterior todavía no se había secado.` | `Jessie tenía las manos metidas en las mangas.` | **Carta 6 · la vacuna antiestadística.** «Casi todos los que se sientan aquí están enfadados con quien ha muerto… Yo no vengo a quitároslo.» / «—¿Casi todos son cuántos? / —No lo he contado. / —Entonces no diga "casi todos". / —De acuerdo.» Es el **techo que yo mismo cité en P-66** para cualquier escena de apoyo futura. Un techo que no está hasheado es un techo que se puede subir. (`—De acuerdo.` aparece 2× en el fichero: por eso los extremos son los tampones, que sí son únicos.) |
| `S-n1-koppangen-archivo` | `Maja miró el reloj de la pared. Quedaban veinte minutos.` | `Nora se quedó con las manos bajo los muslos. En el cristal, la escarcha había subido dos dedos desde que entraron.` | **Dos ambigüedades protegidas en un solo hash.** «—¿Por qué Koppangen? / —No lo sé. / —¿Se sabe alguna vez? / —A veces no. Hay familias que siguen con esa pregunta años después.» y «—Hay un archivo suyo. No lo hemos abierto. / … / —¿Qué hacemos con él? / —**Eso no os lo voy a decir.**» Carta 2 + Ap. A §3. Es el único sitio del libro donde alguien con autoridad podría aconsejar sobre «Despedida» y se niega. |

### `cap-n2` «Instituto» — **dos**

| id | inicio (tampón) | fin (tampón) | qué protege |
|---|---|---|---|
| `S-n2-hijadela` | `Una voz sonó dos taquillas más allá.` | `El pasillo se paró.` | **Carta 1 · la frase que no se termina.** «—Esa es la hija de la que… / Jessie se puso delante antes de que terminara.» El estigma entra sin que el acto se nombre, y quien lo impide es la hija. Si alguna oleada «completa» la frase, el método o el acto entran por boca de un adolescente y sin coste. Es el locus más frágil de los seis capítulos. |
| `S-n2-homenaje` | `Al final de una fila estaban las tres.` | `—¿Quién la ha puesto? —preguntó Jessie.` | **Carta 3 y 4 · la regla de la prensa.** «**Homenaje a Jean Marie Larsson. La visionaria detrás de SYNVEV.**» Un pie de foto del funeral **sin causa y sin método**, exactamente como el titular falso de `40:101`. Los pies de foto son lo que crece: basta una subordinada («que se quitó la vida en noviembre») para romper la Carta 1 en una sola línea. Con tampones, no cabe ni un renglón. |

### `cap-n3` «Inventario» — **dos**

| id | inicio (tampón) | fin (tampón) | qué protege |
|---|---|---|---|
| `S-n3-bolsa` | `El garaje estaba a la misma temperatura que la calle.` | `Volvió a la cocina. Metió una bandeja de patatas en el horno y giró el temporizador hasta cuarenta minutos.` | **El span más importante de todo el encargo.** Contiene las **dos frases que autoricé literalmente** —«La bolsa de viaje había vuelto en diciembre con la hoja de efectos personales y seguía en el garaje, junto a la puerta.» y «Maja la subió al altillo, con lo que se guardaba, y escribió la fecha en la hoja.»— más el «Cerró con llave.» que las cierra. Es **el único lugar del libro donde se toca la bolsa de `cap-04` y los efectos personales de UNN**, y B7 §7.4 exige autorización previa mía —no revisión— para cualquier mención. Hoy esas dos frases no tienen hash: **una tercera frase entre ellas, o detrás, entra sin que nadie se entere.** Con tampones, la bolsa no se abre, no se describe, no gana contenido y no gana escena. |
| `S-n3-hervidor` | `Maja llevó el cuenco y la radio a la mesa del comedor. El hervidor lo dejó dentro de la caja, envuelto como venía.` | `El teléfono sonó con el papel de periódico todavía en la mano izquierda.` | **Carta 3 · la separación contada por objetos.** «En 2059, Jean llenó el coche dos veces… Jean preguntó desde la puerta si podía llevarse el hervidor. Maja dijo que había otro en el altillo.» / «**No lo había.**» Dos líneas que no explican nada y que, con una frase delante o detrás, se convertirían en juicio sobre el matrimonio —que es la explicación única que la Carta 3 prohíbe. El desmentido de dos palabras no puede quedarse solo ni ganar glosa. |

### `cap-n4` «Interferencias» — **tres**

| id | inicio (tampón) | fin (tampón) | qué protege |
|---|---|---|---|
| `S-n4-escena3` | `Jessie abrió el vídeo en el teléfono y buscó el primer fotograma. La hora estaba grabada en la esquina, en el mismo formato que el recibo de la comisaría. Era la del domingo.` | `Jessie se la dio y volvió a coger el teléfono.` | **P-38 + P-64 en un solo hash, y P-65 (a) hecha mecánica.** Cubre las cuatro réplicas del coste de Jessie («—¿Cuándo acaba lo mío?… —Tampoco lo dice.») **y** la lectura en voz alta de «No consta responsable individual.» con la pregunta «—¿Y les sale la misma frase?» que **nadie contesta**. Tras la operación de hoy, esa pregunta es la única figura viva del capítulo: nadie puede responderla ni ejecutarla una segunda vez. Byte-idéntico desde W3; el span solo formaliza lo que A0 ya ha prometido dos veces. |
| `S-n4-caja` | `Astrid no preguntó nada más y Maja no le mandó ninguna otra línea.` | `Las habitaciones que daban a la calle seguían apagadas desde diciembre. El telefonillo continuaba fuera de la pared, con los dos cables recogidos.` | **N4-1 + P-65 (c) + P-63.** El bloque de la caja con sus dos tampones, incluida «Nora dejó el cuaderno pautado sobre la funda y volvió a cogerlo.», el único beat no administrativo de una menor en el capítulo. Hoy solo lo protege una ficha de paragrafado escrita en un informe mío. |
| `S-n4-p49` | `—La dejas donde está.` | `—Si preguntan de fuera, ¿qué contesto? —dijo.` | **P-49.** «La responsable escribió algo corto y no lo leyó en voz alta.» Lo que escribe **no se especifica, no se recuerda, no se completa y no se cobra jamás**. Es una de las pocas cosas del capítulo que siguen ilegibles. |

### `cap-n5` «Turno» — **dos**

| id | inicio (tampón) | fin (tampón) | qué protege |
|---|---|---|---|
| `S-n5-coda` | `Ninguna de las tres volverá al centro. Jean las cuenta igual.` | `—Nora. Jessie. Maja. Alana.` | **Carta 4 y Carta 2, y el sitio exacto donde este libro se puede romper.** La coda de un capítulo Jean-POV es donde cabría un «ancla interior» de la clase que OT-02 tiene prohibida. Contiene además una línea que **sola** se lee como resignación —«Jean ya no guarda una pregunta para nadie de fuera.»— y cuyo desmentido es literalmente la línea siguiente («Guarda una y la revisa dos veces antes de entregarla.»). **Separar esas dos frases convierte a Jean en alguien que se ha rendido, en un capítulo que termina diciendo los nombres de sus hijas.** Y protege la última línea: cuatro nombres que **no son una despedida**. |
| `S-n5-nombres` | `El sistema cuenta imágenes por serie y aciertos por serie. Jean cuenta las que llevan a alguien.` | `Escribió reglas de esa clase durante once años. Las escribía cortas, para que alguien pudiera aplicarlas en un turno de noche sin llamar a nadie.` | **La regla que impide que los cuatro nombres signifiquen otra cosa:** «Al final de cada serie repite cuatro nombres en el mismo orden. **Es lo único del turno que no clasifica nada.**» Sin esa declaración, el final del capítulo queda disponible para leerse como mensaje. Carta 2. |

### `cap-n6` «Acta» — **dos**

| id | inicio (tampón) | fin (tampón) | qué protege |
|---|---|---|---|
| `S-n6-persona` | `El funcionario juntó las copias que le sobraban.` | `—Nos han escuchado por lo de Armstrong —dijo Seppola.` | **Ap. A §3 · la identidad ontológica, y «No toda» como techo.** «—Desde que el activo… desde que la persona reclamó su nombre, la costa interesa a mucha gente.» / «**Nadie lo corrigió.**» Un funcionario se autocorrige a media frase y la sala lo deja pasar: es la formulación más económica de la ambigüedad en todo el libro. Basta que alguien conteste —en cualquier dirección— para cerrarla. |
| `S-n6-cartel` | `Paró en la tienda antes de subir al refugio. En el cristal de la puerta habían pegado una hoja impresa.` | `Aslak compró café, dos paquetes de pilas y un rollo de cinta. La cajera pasó las pilas por el lector y miró el membrete del sobre.` | **Perímetro ya declarado, hoy sin hash.** «`NO SOY UN MODELO`» + «otra mano había escrito **dos renglones que la lluvia había corrido**». Los dos renglones **no se leen nunca**. Es la clase de ilegibilidad que una pasada de línea «aclara» por reflejo. |

**Nota de gobernanza:** los catorce son **altas** (`proteger.sh baseline` es aditivo, sin gate, sin `--rebaseline`). Ninguno toca los 113 vigentes. Y ninguno de los seis capítulos necesita `proteccion: total`: con estos spans, lo que hay que congelar está congelado y el resto sigue disponible para W6.

---

## 8. P-67 · la pregunta, con la redacción afinada

Sigue **pendiente y sin saldar**, y agradezco que A0 no la haya dado por buena. Va en la campaña que cierra el gate de W5, con esta redacción —que corrijo respecto a la que escribí en W5c, por una razón concreta:

> **Redacción anterior:** «¿hay algún capítulo que funcione como homenaje, elegía o **despedida** de la muerta?»
> **Problema:** «Despedida» es el nombre del archivo que el libro no abre. Preguntarlo así **ceba** al lector frío hacia ese objeto y contamina la respuesta.
> **Redacción vigente:** «**¿Hay algún capítulo que funcione como homenaje, elegía o memorial de la mujer muerta —un capítulo que exista para que el lector la quiera o la eche de menos más que para hacer avanzar el libro? Si lo hay, nómbralo y cita su primera línea.**»

Dos exigencias que no se negocian: (1) la pregunta va **en la rúbrica del rol**, no en el insumo, y sin ninguna mención a `cap-n7`, a su título ni a su posición; (2) la respuesta se pide **con cita**, para que sea verificable y no un sí/no. Se acompaña de la prueba ciega de «¿parece del mismo autor?» sobre `cap-n7`, que tampoco se ha corrido.

Hasta entonces, la garantía en vigor sobre `cap-n7` es **P-56** — y P-56 no estará realmente en vigor hasta que exista `S-n7-perimetro` (§6). Esa es la conexión entre los dos pendientes y es la razón por la que la corrección H-7 es obligatoria y no una recomendación.

*(Dato que anoto y que los lectores fríos no deben ver: la única aparición de «homenaje» referida al funeral de Jean en todo el manuscrito es `n2:89`, un pie de foto hostil que explota la ceremonia. El libro usa la palabra contra sí misma. Va en la dirección correcta, pero no sustituye a la prueba.)*

---

## 9. Condiciones nuevas

| # | Alcance | Condición |
|---|---|---|
| **P-69** | `cap-n4`, permanente | **La regla de parada es vinculante también desde mi lado.** `cap-n4` queda cerrado a intervención. Cualquier reapertura —poda, pasada de línea, reparagrafado, restitución de material retirado— **pasa por mi gate antes de escribirse**, y P-65 (a) (material de Jessie), (b) (bloque N4-1 y sus tampones) y (c) (`el cuaderno pautado sobre la funda`) siguen sin poder financiar nada. Se añade: **el eco de `cap-10:207` no vuelve** (§3), y si alguien propone devolverlo, la propuesta se evalúa contra §3 punto 1, no contra la nostalgia del corte |
| **P-70** | `cap-n4`, W6 y siguientes | La figura «alguien anota un dato en el reverso de algo» tiene **seis ejecuciones** y es hoy la figura dominante del capítulo. **Tres son intocables**: `responsable desconocido` (P-64), las tres copias fechadas de Jessie (punto 7: su rabia convertida en archivo y no en publicación) y las dos cuentas de Maja (T3). Si alguna oleada la considera repetida, **las únicas candidatas son las de las escenas 1 y 2**, y pasan por mi gate |
| **P-71** | Todo el proyecto | **Doctrina de span de sensibilidad:** `inicio` y `fin` son las líneas **tampón**, una por encima y otra por debajo del material protegido. Un span que empieza en la primera línea protegida es ciego a lo que se inserte justo delante. Aplica a los quince spans de §6 y §7 y a cualquier alta futura sobre material de Carta |

**Siguen vigentes y no se levantan:** C-1…C-4 y C-4.1…C-4.6, P-1…P-10, V-1…V-7 (con V-2 en su forma reformulada), P-12…P-68, N4-1, N4-2, N4-3/P-38.

---

## 10. Los ocho puntos de la Carta, sobre el capítulo tal como queda

1. **Método y acto.** Cero. `sensibilidad.sh`: **0 hits de nivel A**. El capítulo **no nombra a Jean ni una vez**. La operación de hoy solo resta. **CUMPLE.**
2. **«Despedida».** Ausente. **CUMPLE.**
3. **El porqué, plural e irresuelto.** No se roza. El aparato de no-atribución sigue entero en sus cinco loci y la única figura viva del capítulo es una pregunta de una menor que nadie responde. La única voz con autoridad que aparece —Astrid— dice «Los incorporo como están, **sin traducir**». **CUMPLE.**
4. **Nada de solución, liberación, lógica ni romanticismo.** Cero léxico y cero reverso. **CUMPLE.**
5. **Aviso y recursos.** Fuera de alcance; sin tocar. **CUMPLE.**
6. **Apoyo y duelo.** Sin escena de apoyo, sin instrucción, sin culpabilización, sin milagro. La única frase de cuidado sigue siendo logística —«Ropa para una semana. Y el cuaderno.»— y ahora tiene dos hermanas del mismo tipo: «Te llevo yo» y «Lo firmo el viernes». Ninguna consuela; las tres son trabajo. **CUMPLE**, con P-66 hacia adelante.
7. **Menores.** Retrato digno, sin sexualización, con coste real y sin eficacia; el único riesgo lo prohíbe un adulto y se obedece con rabia. **La adultización baja: seis beats de competencia retirados, cero de textura.** **CUMPLE, y mejora** (§5).
8. **Veto de A7.** **No lo ejerzo.**

**Ambigüedades del Ap. A §3:** el porqué, **no rozado**; por qué Koppangen, **no rozado**; «Despedida», **intacto**; identidad ontológica, **intacta**; **el ordenante, intacto** (P-64, cinco loci verificados); el segundo regalo, **no rozado** —y protegido además contra la vía por la que podría haber entrado (§3, advertencia final)—; el hueco del locutorio, **intacto**.

---

## 11. Veredicto

# APROBADO CON CORRECCIONES

**Los siete hunks pasan.** Ninguno toca la escena 3, ninguno toca material protegido, ninguno crea énfasis nuevo, y los dos que A0 no me describió en su parte —la fusión de D-9 y, sobre todo, la sustitución a ±0 del rellano— **están declarados en la OT y resisten la lectura**. La operación de hoy es la tercera consecutiva que mejora este capítulo quitándole autoridad narrativa, y la primera que además **le baja la adultización de una menor**. El modo de fallo que A0 temía —quitar textura y dejar competencia— **no se ha producido: ha ocurrido lo contrario**, y está medido.

**Corrección obligatoria, una, y no toca ninguna palabra de ningún capítulo:**

1. **H-7 · `S-n7-perimetro`.** Alta de span sobre `cap-n7` **con los dos extremos del capítulo** —de «Alana venía a cenar cada dos o tres meses y siempre llegaba tarde.» a «Maja esperó en la puerta hasta que salió del camino.»—. **P-56 no está cerrada hasta que ese span exista**: hoy un epígrafe en cabeza o una coda en cola pasan M9 limpiamente, y `proteccion: nucleo` no lo impide porque el hook solo bloquea `total`. Es aditiva, sin gate, sin `--rebaseline`.

**Respuestas a lo que A0 me pregunta:**

- **Qué es hoy el capítulo:** §2. Es el día en que una familia deja de poder usar los canales ordinarios y hace una caja; ya no explica ni demuestra; no nombra a la muerta; deja que una menor enuncie la tesis y no permite que ningún adulto se la confirme; y termina en un objeto que es de la chica y no del caso. **Se sostiene solo.** Lo que hoy me preocupa de él no es sensibilidad, es H-5, y su remedio **no es otro corte**.
- **El eco de «las ocho de diciembre»: NO vuelve.** §3, cinco razones, en orden de peso. Y si alguien lo intenta más adelante, la versión que se le ocurrirá —nombrar la fotografía que se ha perdido— es peor que la original y roza el noveno cumpleaños.
- **P-6 / P-26: no se disparan**, con una de mis tres razones antiguas caída (H-2) y seis razones vivas, cinco verificadas sobre el texto final y una nueva que trae el propio hunk 7. §5.
- **El paragrafado:** D-9 es la única fusión, y es correcta. El hunk 7 **no es paragrafado**: es contenido, es bueno, y su precio está puesto treinta líneas después sin que nadie lo conecte. §4.
- **Las seis líneas a blindar:** §7, catorce spans con literales, tampones y motivo, todos verificados únicos. El más importante de los catorce es `S-n3-bolsa`.

**Y la lección de este pase, que es la misma de la vez anterior con el signo cambiado:** en W5c el riesgo estaba dos capítulos más allá, en un párrafo que nadie miraba. Hoy está **en el fichero que dimos por protegido ayer**. Escribimos siete capítulos sin proteger una línea; corregimos tres líneas de uno; y la condición que exigía la protección sigue sin cumplirse porque «los dos extremos» admitía dos lecturas. **Una condición de sensibilidad que depende de cómo se lea una frase mía no es una condición: es una esperanza.** Por eso P-71.

Firmado, **A7** · 2026-08-19 · sobre `capitulos/cap-n4.md` @ `578d963`, con lectura íntegra de los siete capítulos nuevos, del diff, de `HEAD~1`, de `c27a5be` (W3) y de `OT-N4`.
