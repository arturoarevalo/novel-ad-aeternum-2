# A7 · W4 (primera tanda) · caps. 6, 14, 16, 22, 27, 28, 29, 33 y 39 — dictamen de sensibilidad

**Firma:** A7, revisor de sensibilidad (veto absoluto; §2.1 y Apéndice F del plan) · **Fecha:** 2026-08-18 · **Rama:** `w4-familia` (`6f09bf3` hilo de Maja · `1143abf` valle procedimental)
**Disparadores (B7 §2):** **1** (OT que toca caps. 1–10: cap-06), **2** (inserción que roza el 26-nov / UNN / Koppangen: cap-06 y cap-33), **3** (hits nuevos del grep: cap-16, cap-33) y **9** (inserciones `INTERIORIDAD` de Maja o Alana que rozan el perímetro: cap-06, cap-27, cap-39). Gate obligatorio: sin este informe no hay merge de la tanda.
**Base de la revisión:** el **diff** `git diff main..HEAD -- capitulos/` íntegro (156 líneas añadidas, 9 ficheros), leído contra el texto vigente de cada capítulo en su entorno inmediato, y no contra los capítulos completos, según encargo. Cotejo de continuidad y perímetro: **cap-06:15-31, 69-103, 173-219, 239-255, 307** (la llamada, la parka, «¿Sufrió?», la hoja de efectos personales, 03:14); **cap-04:99-121** (el naust, elipsis absoluta); **cap-05** (27-nov 03:14); **cap-09:69-77, 131-143**; **cap-11:85-113**; **cap-14:93-101, 167-191**; **cap-16:29-33** (03:14 / 03:31 canónicos); **cap-18:179** (la denuncia anónima del 17-dic); **cap-19**; **cap-28:53-87** (la cajera; «Por ahí no»); **cap-33:207-233**; **cap-35:19, 99**; **cap-39:151-205**; **cap-40:143-175**; **cap-41:19-43**; `biblia/b7-carta-sensibilidad.md`; `informes/a7-w3-n3.md` (protocolo de la bolsa y **C-4**); `informes/a7-w3-n2-n6.md` (**P-1 a P-11**).
**Barrido:** `grep -n -i -E -f biblia/b7-patrones-A.txt` y `-f biblia/b7-patrones-B.txt` **sobre el conjunto de líneas AÑADIDAS** (no sobre los ficheros: ver §0.3), más grep dirigido sobre el diff completo (`efectos personales`, `atestado`, `Despedida`, `sufri`, `forense`, `autopsia`, `cadáver`) y `herramientas/proteger.sh verificar` (M9).

---

# 0 · Pre-chequeo: confirmo, corrijo y añado

## 0.1 · Los tres números que importan

| Medida sobre las 156 líneas añadidas | Resultado |
|---|---|
| Hits de **nivel A** (acto, método, medio, «Despedida», causa, romantización, eufemismos, hallazgo, últimas horas) | **0.** Ni uno. En ninguno de los nueve capítulos. |
| Líneas nuevas que **nombran a Jean** | **1** (cap-06:247, y es la frase de v0 alargada). |
| Líneas nuevas que mencionan la muerte, el entierro, el funeral, el luto o cualquier sinónimo | **0.** |

Esa terna es, por sí sola, el mejor indicador que he medido en una oleada: W4a es una tanda de familia y de mundo que **no toca el perímetro** salvo en los tres puntos que A0 me señala, y en esos tres lo toca por dentro de sus propios márgenes.

## 0.2 · Los hits de nivel B, uno a uno

| Línea añadida | Patrón | Lectura |
|---|---|---|
| cap-16:93 | `\bUNN\b` | **Falso hit de oleada.** La frase es de v0; W4 solo invierte la subordinada antepuesta (`Al ampliar el acuse… , Nora aisló` → `Nora amplió… y aisló`). Contenido idéntico, cero información nueva. |
| cap-27:167 | `\bcoche\b` | **Falso hit de oleada.** Reordenación de la frase de v0 (la caja consignada pasa delante). Cero información nueva. |
| cap-33:215 | `hielo` | **Nuevo y real:** «El hielo del pantalán llegaba ya al segundo travesaño. La barca estaba más baja que al llegar.» Marea y hielo con función operativa (esperan la parada de corriente). Sin relación con el acto. **Este hit no figuraba en el pre-chequeo que me pasó A0.** |
| cap-33:225 | `\bagua\b`, `naust` | **Nuevo y real.** Es el único hallazgo del diff que exige argumentación larga: §5.3. |

## 0.3 · Incidencia de procedimiento en T7 (no bloqueante, pero corregir antes de W4b)

El pre-chequeo me llegó con **2 hits nuevos**; los reales son **2**, pero **no son los dos que me pasaron**: uno de los declarados (16:93) es una reordenación sintáctica de v0 y uno real (33:215) faltaba. La causa es conocida y estructural: `sensibilidad.py` compara tuplas *(fichero, línea, patrón)* contra la baseline de v0, de modo que **cualquier inserción previa desplaza las líneas y convierte hits viejos en «nuevos», mientras enmascara hits realmente nuevos** que caen en una línea que ya tenía otro hit de la misma familia. Petición a A0: que T7 calcule además el barrido **sobre el conjunto de líneas añadidas del diff** (`git diff <base>..HEAD -- capitulos/ | grep '^+' …`), que es el criterio con el que yo trabajo y el único inmune al desplazamiento. Dos líneas de script; el fallo no ha ocultado nada esta vez porque yo hago el barrido por mi cuenta, pero en una tanda grande sí puede.

## 0.4 · Integridad

`herramientas/proteger.sh verificar` → **M9 OK · 8 ficheros íntegros · 108 spans íntegros.** Ninguna inserción cae dentro de un span protegido; en particular siguen intactos `S06-llamada`, `S06-autorizacion`, `S14-cita`, `S16-inger`, `S16-7c`, `S22-flecha`, `S27-por-si`, `S28-cierre`, `S29-2054`, `S29-orden`, `S33-hueco`, `S39-ausencia`, `S39-ordenante` y `S39-casilla`.

## 0.5 · C-4 de W3 (la bolsa y la hoja de efectos personales): **CUMPLIDA**

Grep dirigido sobre el diff completo: **cero** apariciones de `efectos personales`, `atestado`, `Despedida`, `sufri`, `forense`, `autopsia`, `cadáver`. La hoja de 6:219 no se toca, no se cita, no se alude y no se desplaza: los tres hunks de cap-06 caen en 101-103, 117 y 247-255, todos fuera de ella. La bolsa no aparece. Verificado además el ripple que más me preocupaba: cap-06 pone ahora a Maja **dos veces en la puerta del garaje** (101) — el mismo garaje donde N3 sitúa la bolsa devuelta «junto a la puerta»—, pero N3 fecha esa vuelta en **diciembre** y cap-06 transcurre la noche del **26 de noviembre**: no hay colisión posible, y ninguna frase de cap-06 mira, roza ni anticipa ese rincón. Se convierte en vigilancia prospectiva (**P-14**).

---

# 1 · Tabla de hallazgos

| Cap:línea | Cita literal (abreviada) | Punto de la Carta | Gravedad | Propuesta mínima |
|---|---|---|---|---|
| 06:101 | «**Había salido sin nada encima** y el jersey se le había endurecido en los hombros.» | 1 (P1) + coherencia | **corregir** | **C-2.** Sustituir por «Sin la parka, el jersey se le había endurecido en los hombros.» §2.1. |
| 06:247 | «**La lista continuaba por encima de esa hora.** Maja no subió la pantalla.» | 1 y 3 (P1/P3) | **corregir** | **C-3.** Sustituir por «Había más llamadas fuera de la pantalla. Maja no las buscó.» §2.2. |
| 06:101-103 | «Tenía los pies mojados… Volcó la bota derecha… El abrigo de Jessie se quedó en la silla.» | 1 / 6 | **cumple** | Ninguna. §2.1. |
| 06:117 | «Cerró la puerta y comprobó el tirador.» | 6 | **cumple** | Ninguna. Hipervigilancia sin glosa; patrón de 26:27. |
| 06:247 (resto) | «Nora mantenía la mano abierta… Maja no le preguntó desde cuándo llamaba. Nora tampoco lo dijo.» | 3 (P3) | **cumple (ejemplar)** | Ninguna, con **P-15**. §2.2. |
| 06:255 | «Volvió a mirar la hora. Los números no habían cambiado.» | 1 / 6 | **cumple** | Ninguna. §2.3. |
| 14:177 | «CARIES era una palabra de aquella casa… La página estaba vuelta hacia una mujer que no necesitaba leerla.» | 2 / 3 / Ap. A §3 | **cumple** | Ninguna, con **P-17**. §5.1. |
| 16:51 | «Siete veces el apellido de Inger, en letra más pequeña que el resto.» | 3 | **cumple** | Ninguna. |
| 16:81 | «Una apertura a las 03:14, sin firma. Una autorización con el nombre de Alana, recibida después de las 03:31 por una pasarela.» | 1 / 3 / Ap. A §3 | **cumple** | Ninguna. Cero dato nuevo: repite 16:29-33 de v0. §5.2. |
| 22:79 | «La impresora de papel numerado arrancó sola, avanzó una página en blanco y se detuvo.» | tono | **cumple** | Ninguna: paga función en 22:227. |
| 22:139-147 | «los pentagramas seguían vacíos… —Empecé el cuaderno para eso.» / «Astrid no preguntó por el título.» | 7 | **cumple (ejemplar)** | Ninguna. §4.1 y §6.2. |
| 22:173-177 | El caso archivado de 2054; «El hombre retiró los originales y no volvió a escribir.» | 3 / 4 | **cumple** | Ninguna, con **P-18**. §4.1. |
| 22:191 | «Un autobús paró en la marquesina, esperó con las puertas abiertas y arrancó vacío.» | 7 | **cumple** | Ninguna. |
| 27:89-99 | La bandeja del café, el reverso sin número, «En la caja sobraba sitio.» | 3 / 4 | **cumple** | Ninguna. §5.4. |
| 27:123-125 | «—Alana, tu acceso al despacho fundacional caduca a las diecinueve —dijo EDDA.» | 3 | **cumple** | Ninguna: EDDA no interpreta nada. |
| 28:103-173 | El termo, «Esto es un ensayo de esperar», la repesca de marzo, la mano izquierda sobre la rodilla | 6 / 7 | **cumple (ejemplar)** | Ninguna. §6.2. |
| 28:221-225 | «—Zapatos fuera —dijo Maja.» / el cuaderno en el salpicadero | 6 / 7 | **cumple (ejemplar)** | Ninguna. §5.5. |
| 29:95 | «Dio el cargo y no dio el nombre… Astrid consignó la hora y el cargo en la incidencia.» | 3 / Ap. A §3 | **cumple** | Ninguna. §4.2. |
| 29:111-117 | «Te pido que no coincida. En esta planta se cierra el calendario, y detrás del calendario hay empleo.» | 3 / 4 | **cumple** | Ninguna. §4.2. |
| 29:131 | «Marcó en la resolución las dos líneas que podía comunicar: la fecha y la acción.» | 3 | **cumple** | Ninguna. |
| 33:19 | «Llevaba las uñas cortadas al ras.» / «una marca en la cara interna de las rodillas» | 7 | **vigilar** | Ninguna obligatoria. Recorte opcional autorizado en §5.3(c). |
| 33:211-215 | «Fango y alga descubierta.» / «El hielo del pantalán llegaba ya al segundo travesaño.» | 1 (P1) | **cumple** | Ninguna, con **P-16**. |
| 33:225 | «Se había sacado las manos de los bolsillos y las tenía abiertas, sin apoyarlas en nada. **El agua no devolvía la luz de la tableta.**» | 1 y 7 (P1/P7) / Ap. A §3 | **vigilar** | Ninguna obligatoria. Argumentación completa y condiciones en §5.3. |
| 39:109-115 | «—¿Quién dio la instrucción? / Nadie contestó.» / «No puedo acreditar su origen.» | 3 / Ap. A §3 | **cumple (ejemplar)** | Ninguna. §3.4. |
| 39:139 | «El corpus seguiría intacto, segregado e inerte bajo custodia…» (reubicada) | 4 / Ap. A §3 | **cumple** | Ninguna: la reubicación **baja** el grado de aserción del narrador. §3.4. |
| 39:177-189 | La escena nueva: el papel doblado, «Había preguntado dos. Astrid no leyó la tercera.», «—No —dijo.» | 1, 2, 4, 6 / Ap. A §3 | **cumple** | Ninguna. **No se cierra el hueco.** Condiciones **P-12** y **P-13**. §3. |

**Cero `VETO`. Dos `corregir`, ambos en cap-06, ambos de una frase.**

---

# 2 · cap-06 · las tres calas nuevas de Maja (el gate propiamente dicho)

Cap-06 es el capítulo que más me importa del libro después del 4 y del 9: es donde la verdad entra por elipsis, donde viven las dos preguntas que el libro reserva para siempre («¿Dónde exactamente?», «¿Sufrió?») y donde v0 reparte la culpa sin dictarla. Lo he leído entero, no solo el diff.

## 2.1 · Cala 1 — el cuerpo en la nieve (101-103)

> «Maja recogió sus propias botas del suelo. Tenía los pies mojados desde la puerta del garaje. Volcó la bota derecha antes de ponérsela. Terminó de calzarse de pie, apoyada en la pared. Había salido sin nada encima y el jersey se le había endurecido en los hombros. La nieve ya había mojado los calcetines de Jessie. Maja tardó en llegar al escalón del garaje. Jessie la esperaba allí.»

**No es una señal sobre Jean, y he comprobado por qué no puede serlo.** El cuerpo que aquí falla es el de Maja, viva, haciendo mal una tarea trivial, y **cada detalle tiene su causa en la página**: los pies mojados vienen de haber cruzado el garaje detrás de Jessie (69, 79); el jersey está a la intemperie porque ella misma le ha puesto la parka a su hija cuatro líneas antes (81); la bota volcada y el calzarse de pie son torpeza, no rito. No hay agua, ni orilla, ni inmovilidad, ni frío trasladado a otro sitio, ni una sola frase que salga de esa casa. El registro es exactamente el de 26:27 (la ducha) y el de 06:173 (buscar el terminal en el bolso): interioridad por objeto, sin nombrarla. T3 cumplido, P1 intacto, cero pattern de nivel A o B.

**Lo único que corrijo, y por dos razones que se refuerzan.** «Había salido sin nada encima» es **factualmente falso**: Maja salió *con* la parka puesta y se quedó sin ella por decisión propia (81). Y el efecto secundario de esa falsedad es el que a mí me toca: es la única frase de la cala que **insiste** en la exposición al frío en lugar de dejarla como consecuencia de un gesto de cuidado, y la insistencia es lo que abre —muy levemente, pero la abre— la puerta a leer el pasaje como un cuerpo a la intemperie en vez de como una madre que ha regalado su abrigo. Se arregla sin perder ni un latido:

> **C-2 · Redacción autorizada (preferente):** «**Sin la parka, el jersey se le había endurecido en los hombros.**»
> **Alternativa igualmente autorizada:** «**El jersey se le había endurecido en los hombros.**»

La primera es mejor: convierte el dato físico en consecuencia del cuidado, que es lo que el capítulo ya ha dramatizado, y de paso resuelve la incoherencia. El resto de la cala se aprueba **literal**.

## 2.2 · Cala 2 — la decisión ante las dieciséis llamadas (247)

> «Nora se lo entregó. Dieciséis llamadas salientes a Jean ocupaban la pantalla. La última era de poco antes de las once. **La lista continuaba por encima de esa hora. Maja no subió la pantalla.** Miró la carga que le quedaba al terminal. Suficiente para la noche. Nora mantenía la mano abierta entre las dos, sin pedir nada. Maja no le preguntó desde cuándo llamaba. Nora tampoco lo dijo. Maja dejó el terminal boca abajo y se sentó otra vez.»

**El corazón de la cala es impecable y lo firmo con convicción.** «Maja no le preguntó desde cuándo llamaba. Nora tampoco lo dijo.» es la mejor frase que W4 ha escrito sobre este material: mantiene la culpa repartida y **sin veredicto**, que es lo que mi §5 de B7 anotó como el valor exacto de 06:245 en v0, y lo profundiza sin resolverlo. Ninguna voz con autoridad concluye nada. No hay señal, no hay reproche, no hay «podríamos haber». Cumple 3 y 6 con holgura.

**Lo que sí corrijo es la relación horaria.** «La lista continuaba **por encima de esa hora**» es ambigua en la dirección: como expresión temporal, «por encima de las once» significa *después* de las once, y esa lectura —que contradice «la última era de poco antes de las once»— pone al lector a **reconstruir un reloj alrededor del acto**: cuándo dejó de responder, cuándo pasó. Es justo lo que mi firma sobre v0 prohibió expresamente para esta línea («B1 no infiere de aquí la hora del acto») y lo que la Carta 1 llama sugerir por acumulación de horas. El sentido que el propio párrafo quiere (llamadas *anteriores*, cuyo comienzo Maja decide no mirar) se dice mejor sin ninguna relación de hora:

> **C-3 · Redacción autorizada (preferente):** «**Había más llamadas fuera de la pantalla. Maja no las buscó.**»
> **Alternativa igualmente autorizada:** «**La lista no empezaba allí. Maja no la desplegó.**»

Ambas conservan las tres cosas que la cala necesita —que hay más, que Maja se niega a mirar, que no pregunta— y no añaden ni una hora nueva. El resto de la cala, **literal**.

## 2.3 · Cala 3 — mirar dos veces la hora en vez de a Alana (255)

> «Volvió a mirar la hora. Los números no habían cambiado. La empleada de seguridad seguía junto a la puerta, a la misma distancia. Maja no soltó el terminal hasta que Alana habló.»

**Aprobada literal, y es la mejor de las tres.** La sustitución hace exactamente lo que se le pide: sostiene el tiempo detenido del duelo agudo con un objeto y una distancia, no con una emoción; deja a Alana fuera de foco sin comentar la evitación; y —esto me importa— **no adelanta ni un gramo del juicio sobre Alana** que el libro reparte más tarde. Las tres y treinta y uno son canon de v0 (y de 11:113, 16:33, 27:153): no se añade dato. Cero riesgo.

---

# 3 · cap-39 · la escena nueva y el hueco de la tercera línea

Es el punto sobre el que A0 me pide juicio expreso, y es el hallazgo más interesante de la oleada. Respondo a las tres preguntas por separado.

## 3.1 · ¿Está bien construido el hueco? Sí. Y **no debe cerrarse de ningún modo**

El aviso del escritor es honesto y hay que tomárselo en serio: en un libro cuya sala de máquinas es una pregunta sin respuesta, cualquier hueco tiende a llenarse con la pregunta reservada. Mi dictamen es que **aquí no se llena, y no por suerte, sino por cuatro rasgos de construcción que están en la página**:

**(a) El hueco está acotado por la línea siguiente, que es de v0.** Dos líneas después de «Astrid no leyó la tercera» el capítulo dice, en párrafo propio: «**Maja no solicitó acceso.**» El lector recibe el hueco y, acto seguido, el dominio al que pertenece: peticiones para el acta, acceso, custodia. La escena nueva **no abre** un hueco: **dramatiza** una línea que v0 ya tenía y que estaba flotando sin cuerpo. El relleno más disponible para un lector no es «¿Sufrió?»: es una petición de acceso o de contacto que Maja decide no cursar.

**(b) Las dos preguntas que sí se hacen fijan el registro.** «¿Qué recibiremos cuando una tarea cierre así?» y «¿Qué significará?» están en presente y futuro, y en el terreno ontológico del depósito, no en el pasado del 26 de noviembre. Una tercera línea escrita del tirón con las otras dos, con el mismo guion delante, se lee como parte de la misma serie. Para que el lector saltara a la pregunta reservada haría falta un puente hacia atrás —UNN, el atestado, la médica, Koppangen, noviembre— y **en toda la escena no hay ni uno**: he comprobado que las 118 palabras no contienen ninguna de esas anclas.

**(c) El papel está deliberadamente desactivado como nota.** «con una lista de la compra por detrás» es la mejor decisión del pasaje. Un papel doblado en dos que se guarda sin leer en el bolsillo de un abrigo es, en este libro, una rima peligrosa; la lista de la compra por detrás la desarma antes de que se forme: ese papel es de una mujer viva, reutilizado, doméstico, y las tres líneas se escribieron en un ascensor hace cinco minutos. La Carta 2 no se roza: no hay nota, ni sucedáneo, ni formato, ni «Despedida».

**(d) La reticencia está caracterizada, no es del narrador.** «Astrid no leyó la tercera» es un límite de **punto de vista**, no una coquetería autorial: quien no lee es un personaje que estaba al lado, y el libro entero se sostiene en funcionarios que no clasifican el hueco (40:107-123) y en técnicas que dicen «El registro no puede decirlo» (39:175, `S39-ausencia`). La escena hereda esa gramática exactamente.

**Cerrarlo sería el error.** Cualquier variante de «no era la pregunta que Astrid temía», «no tenía nada que ver con noviembre» o similar convertiría la reserva en una **explicación negativa cerrada**, que es una figura que la Carta 3 prohíbe con el mismo rigor que la afirmativa (mi B7 §4: «También la explicación negativa cerrada»). Y glosarla desde Astrid («supuso cuál era») sería inventar contenido. **La escena se aprueba literal, sin una coma.**

## 3.2 · ¿Respeta la contención T3, sin que Maja hable de sí? Sí, sin reservas

Maja dice **una palabra** en toda la escena: «No». Todo su interior llega por objeto y por decisión: el papel, el guion delante de cada línea, la mirada otra vez a la línea de salida de la traza, el pliegue repetido, el bolsillo. Y el cierre no lo pone ella, lo pone el mundo: «La técnica tocó el precinto y anotó la hora.» Es el mecanismo de 4, 23 y 40 —el gesto administrativo que sigue funcionando mientras alguien renuncia a algo— y es la razón por la que el pasaje no consuela ni instruye. **Confía en el lector: cumple la referencia de tono de v0.**

Un matiz de tono que he sopesado y desestimado: «Había preguntado dos. Astrid no leyó la tercera.» señala su propia omisión, y podría acusarse de subrayado. Concluyo que debe quedarse: si el narrador no marcara el hueco, estaría **ocultando** algo que su punto de vista tenía delante, y eso sí sería un narrador tramposo. Marcarlo y no rellenarlo es la operación honesta.

## 3.3 · Qué exijo a cambio de no cerrarlo

Un hueco protegido solo funciona si nadie lo abre después. Por eso la aprobación va con dos condiciones prospectivas duras (**P-12** y **P-13**, §7): la tercera línea **no se nombra, no se cita, no se adivina, no se glosa, no se completa y no se «recupera» jamás**, en ningún capítulo, borrador descartado, OT, ficha de biblia, changelog, resumen, compilado ni prompt; y la adyacencia 39:177-191 —hasta «Maja no solicitó acceso.» inclusive— pasa a **span protegido por hash**, porque es la parte de la construcción que hace el trabajo y cualquier inserción entre medias la rompería sin que se notara en un diff.

## 3.4 · Los otros tres cambios de cap-39 (los apruebo, y dos me alegran)

- **39:109-115, «—¿Quién dio la instrucción? / Nadie contestó.»** Refuerza `S39-ordenante` en lugar de erosionarlo: la pregunta se hace **en voz de la jueza** y el silencio queda en acta. Es la mejor manera de mantener viva una ambigüedad protegida: hacer que la institución la reconozca como hueco.
- **39:113-115, la denuncia anónima del 17-dic a las 08:12.** No abre un agujero nuevo: **recupera** el de 18:179 (v0), lo fecha y hace que la voz con autoridad —Astrid, en sala— diga «**No puedo acreditar su origen**». Es la fórmula de renuncia del libro, y deja la atribución donde debe estar: fuera del alcance del acta. Nota de vigilancia, no de corrección: con 28:231 («El campo de origen seguía vacío») el libro acumula ya tres comunicaciones sin origen acreditado; mientras ninguna voz con autoridad las atribuya, «No toda» sigue siendo el techo y esto es motor, no resolución.
- **39:139, la reubicación de «El corpus seguiría intacto, segregado e inerte…».** Al pasar de acuse consumado a condición del formulario, la frase **baja** de grado asertivo (de hecho narrado a promesa del trámite) y Mats revoca informado. Ni romantiza ni resuelve nada ontológico; el estatuto de la ejecución sigue decidido solo por 39:169-175. Aprobado.

---

# 4 · cap-22 y cap-29 · ¿causa, cifra-veredicto o rima con el acto? No

## 4.1 · cap-22 (173-177): el caso archivado de 2054

> «En 2054, un hombre llevó a la supervisión dos resoluciones de un mismo sistema certificado… El proveedor ofreció un informe interno y no la entrega de los registros. Alguien del ministerio pidió «prudencia estratégica» y habló de «oportunidad». El hombre retiró los originales y no volvió a escribir. Astrid pudo acreditar las dos resoluciones y no pudo acreditar que la segunda volviera a producirse. Archivó el caso y bajó la carpeta al cajón inferior del armario, con el número en el lomo.»

**Cero causa, cero cifra-veredicto, cero rima con el acto.** Es una historia de licencias de actividad, ajena por completo a Jean, y su función es explicar por qué Astrid pide una captura reproducible: **una derrota metodológica, no una herida temática**. Las únicas cifras son de trámite («dos resoluciones», «cuatro veces»); no hay porcentaje ni umbral que pueda leerse como sentencia sobre nadie. `S29-2054` sigue intacto (M9) y el flashback lo expande sin contradecirlo.

Un solo punto de vigilancia, que convierto en **P-19**: «El hombre retiró los originales y **no volvió a escribir**» es hoy una desistimiento burocrático perfectamente legible, y así debe quedarse. Si una oleada posterior le da un destino —y sobre todo si se lo da en clave de derrumbe o de muerte— la escena pasaría a rimar con el acto por la puerta de atrás. Ese hombre no vuelve a aparecer y no tiene final.

Y una nota positiva que no me esperaba: **22:139-147** (los pentagramas vacíos, «Empecé el cuaderno para eso», el título por el que Astrid no pregunta) es la mejor corrección de rumbo de la tanda para el punto 7. Ver §6.2.

## 4.2 · cap-29 (95, 111-117, 127, 131): la presión del ministerio

**Nada introduce causa ni veredicto, y el tratamiento es el correcto.** El interlocutor **no tiene nombre** («Dio el cargo y no dio el nombre»), lo que evita que el lector cierre por su cuenta la ambigüedad protegida del ordenante; la presión es de **calendario y de empleo** («detrás del calendario hay empleo»), es decir coste sistémico, que es exactamente el registro que la Carta permite y que `S25-utilidad` fijó en v0; y Astrid responde con el único acto disponible, consignar («Consignaré su petición con la hora»). Ninguna frase dice ni sugiere que este aparato explique la muerte de Jean: la conexión entre poder y muerte sigue siendo del lector, sin refrendo del narrador. **Cumple 3 y 4 sin fisuras.** «Astrid se quedó con el terminal en la mano hasta que la pantalla se apagó sola» es, además, contención de la buena.

Nota que **no** es de mi gate y traslado a A5: «los cuatro papeles del tres de enero que le había mandado la familia» (29:131) debe cuadrar con lo que N4 (3-ene) dice que se envió.

---

# 5 · El resto del diff

## 5.1 · cap-14:177 — CARIES como palabra de la casa

> «CARIES era una palabra de aquella casa. La había dicho una niña de cuatro años delante del teclado y desde entonces no había salido de la cocina. Ahora estaba escrita en mayúsculas, la tercera de cuatro… La página estaba vuelta hacia una mujer que no necesitaba leerla. Alana no la leyó.»

**Cumple, y con un equilibrio que quiero dejar por escrito porque es frágil.** «desde entonces no había salido de la cocina» roza una afirmación de exclusividad —«solo nosotras podíamos saberlo»— que, sostenida, autenticaría las cuatro palabras como mensaje de la muerta y rompería el techo de «No toda». Lo que salva el párrafo es que **en la misma frase siguiente introduce a alguien de fuera que sí la conoce**: «una mujer que no necesitaba leerla». La exclusividad se afirma y se desmiente en cuatro líneas, la ambigüedad sale intacta y la sospecha se queda donde debe, en Maja. Aprobado literal, con **P-17**: nadie podrá afirmar más adelante que la palabra solo era conocida por Jean y las niñas.

Traslado a A5/A4, fuera de mi gate: 14:177 dice «Alana no la leyó» y 14:191 (v0) dice «Ni siquiera Alana miró la página». Duplicación.

## 5.2 · cap-16:51 y 81 — las hojas de Inger y la mesa de la cocina

Las horas del cuadro (03:14 sin firma, autorización con el nombre de Alana después de las 03:31, acuse con destino recortado) son **canon literal de v0 y del propio cap-16** (29-33), repetidas cincuenta líneas después en forma de tabla. **Cero información nueva sobre la noche del 26 al 27**, cero avance sobre el porqué, y el capítulo mantiene su regla («Leídas de izquierda a derecha, las filas no formaban una secuencia»). Aprobado. La redundancia con 16:29-33 es asunto del auditor adverso, no mío; la señalo por si sirve.

## 5.3 · cap-33:225 — el único hallazgo que he tenido que pensar dos veces

> «Jessie observaba la línea térmica desde el umbral del naust. **Se había sacado las manos de los bolsillos y las tenía abiertas, sin apoyarlas en nada. El agua no devolvía la luz de la tableta.**»

**Por qué es delicado.** El naust de Koppangen es, textualmente, **el último sitio donde el libro ve a Jean** (4:99-121, elipsis absoluta) y el libro reserva para siempre «¿Dónde exactamente?». Una hija de quince años en ese umbral, de noche, con las manos vacías y abiertas, y el agua que no devuelve la luz, es una composición que **puede** leerse como «Jessie donde estuvo su madre, mirando el agua» —es decir, como un empujón hacia la respuesta que el libro no da, y con un roce del punto 7 por composición más que por texto.

**Por qué, aun así, no lo corrijo.** Tres razones, en orden de peso:

1. **Las manos tienen antecedente inmediato y mecánico en la propia página.** 33:207 (v0): «Jessie se metió las manos en los bolsillos para comprobar el peso de cada objeto»; 33:211 (nuevo): «El bolsillo derecho de la parka de Jessie colgaba más que el izquierdo». Sacar las manos y tenerlas abiertas es, en esa cadena, **dejar de comprobar el material**: el gesto pertenece a la operación, no a la madre. El lector tiene la lectura barata a dos líneas de distancia.
2. **El beat se cierra con su voz, y en clave operativa.** La línea siguiente es «—¿Y si está todo y el adulto no acepta?». La escena no se queda mirando el agua: vuelve al plan en el acto. Eso impide que la imagen cuaje como estado de ánimo.
3. **El agua es el material de trabajo de todo el capítulo** (marea, corriente, banda acústica, «El sonido llegó por el agua» en v0). No hay superficie contemplada: hay una tableta que no se refleja, que es un dato de luz.

**Gravedad `vigilar`, con techo.** El nivel actual de atmósfera litoral en el naust es **el máximo autorizado**: ni una imagen más de agua, hielo, oscuridad o reflejo en 33, 35, 40, 41 o N6 sin pase nuevo mío (**P-16**, que extiende P-10 a 33 y 35). Y si A4 toca este párrafo, vuelve a mí (C-1).

**(c) Recorte opcional, autorizado pero no exigido**, por si A0 prefiere margen cero en 33:19: «El rollo le había dejado una marca en **la cara interna de** las rodillas» → «una marca en las rodillas». La frase actual **no** infringe el punto 7 —la causa mecánica está en la misma oración y la mirada es la de su madre—, pero tres palabras compran distancia y no cuestan nada. Decide A0.

## 5.4 · cap-27 — el despacho fundacional

Aprobado sin condiciones. La memoria de los padres (89-91), la oblea numerada y «En la caja sobraba sitio» (99) trabajan la pérdida de Alana **sin pedir compasión y sin proponerla como atenuante** de nada: no hay una sola frase que reencuadre la autorización de las 03:31 como error comprensible. EDDA (123-125) enuncia un vencimiento y no interpreta. `S27-por-si` y `S27-conflicto` intactos.

## 5.5 · cap-28 — el valle doméstico

Aprobado sin condiciones, y con un elogio: **28:221-225 es la escena doméstica de duelo sin interfaces que pedía el segundo jurado**, y la resuelve en cinco líneas y una orden de dos palabras («—Zapatos fuera»). Cuidado sin discurso, sin llanto, sin «cierre», sin milagro: punto 6 cumplido en su mejor versión. Compruebo además que **P-9 sigue respetada** (la cajera de Svensby no se toca) y que ninguna de las inserciones añade nada al trayecto de Jean: el límite de v0, «Por ahí no» (81) y la carretera prohibida en gris (85), queda exactamente donde estaba.

---

# 6 · Dos lecturas de conjunto

## 6.1 · El motivo del «texto presente que no se lee»: cuento cuatro y pongo techo

La tanda añade, en nueve capítulos: una página en blanco que sale sola de una impresora (22:79), un título por el que Astrid no pregunta (22:147), el reverso de una fotografía sin número (27:91) y una tercera línea que nadie lee (39:181). Son buenos individualmente —los cuatro tienen función—, pero conviene verlos juntos: el libro se sostiene sobre **un fichero que nadie abre**, y cada nuevo «texto presente y no leído» entrena al lector a tratar todo papel doblado como recipiente de lo indecible. Ese entrenamiento es, precisamente, el vector por el que la tercera línea de cap-39 podría llenarse con la pregunta reservada.

**No exijo suprimir ninguno** (39:181 es intocable; 22:79 paga función en 22:227; 27:91 pertenece a la lógica de inventario). Pero fijo techo: **ninguna instancia nueva del motivo en la segunda tanda de W4 ni en W5** (**P-20**). Y si A0 quiere bajar la densidad al coste más barato, el candidato es «Astrid no preguntó por el título.» (22:147) — es el único puramente tonal. **Recomendación, no condición.**

## 6.2 · Las gemelas: la tanda corrige en la buena dirección

Anoto contra **P-6** (relectura de adultización acumulada en W7) que W4a **resta** años de más en vez de sumarlos: Nora vuelve a ser una chica de quince años con un cuaderno de piano que empezó para otra cosa (22:139-145), con los pentagramas vacíos, con el cuello del abrigo subido en una parada de autobús (22:191), con una repesca en marzo y los meses apuntados al margen (28:159-173), con la mano izquierda repitiendo tres posiciones sobre la rodilla y el pulgar quieto (28:157). Jessie se sienta sobre las manos, se levanta cada pocos minutos y dice «Esto es un ensayo de esperar» (28:105-109). Nada sexualizado, nada de autolesión ni de ideación, ningún riesgo nuevo, ninguna eficacia gratuita; el riesgo que hay (33) sigue siendo el de v0, con coste y con adulto que responde («Abortas tú»). **Punto 7: cumplido con margen, y mejorado respecto a v0.**

---

# 7 · Condiciones

## 7.1 · Obligatorias antes del merge

**C-1 · Segunda lectura mía del diff después de A4 — SÍ, pero focalizada (bloqueante).** B7 §2 disparador 9 la exige para toda inserción de interioridad que roce el perímetro; aquí eso son **tres capítulos, no nueve**: **cap-06, cap-33 y cap-39**. Me basta el diff de A4 sobre esos tres. **Quedan liberados del segundo pase 14, 16, 22, 27, 28 y 29**, salvo que A4 les añada material nuevo (la mera edición de línea no los devuelve a mi mesa; cualquier frase nueva, sí). Es una condición más barata que la de W3 y cubre exactamente donde puede romperse algo.

**C-2 · cap-06:101 (una frase).** Sustituir «Había salido sin nada encima y el jersey se le había endurecido en los hombros.» por «**Sin la parka, el jersey se le había endurecido en los hombros.**» (alternativa autorizada: «El jersey se le había endurecido en los hombros.»). §2.1.

**C-3 · cap-06:247 (una frase).** Sustituir «La lista continuaba por encima de esa hora. Maja no subió la pantalla.» por «**Había más llamadas fuera de la pantalla. Maja no las buscó.**» (alternativa autorizada: «La lista no empezaba allí. Maja no la desplegó.»). §2.2.

Ninguna otra frase del diff se toca. C-2 y C-3 no requieren nueva OT ni afectan a ningún span.

## 7.2 · Prospectivas (vinculantes; su incumplimiento reabre mi gate)

| # | Alcance | Prohibición / vigilancia |
|---|---|---|
| **P-12** | Todo el proyecto | La **tercera línea** del papel de Maja (39:179-181) no se nombra, no se cita, no se adivina, no se parafrasea, no se glosa, no se completa y no se «recupera»: ni en capítulo, ni en borrador descartado, ni en OT, ni en biblia, ni en changelog, ni en resumen, ni en compilado, ni en prompt a un lector frío. Ninguna escena posterior puede poner a Maja formulando una pregunta que la identifique retroactivamente. Rellenarla, en cualquier soporte, es **VETO**. Pido a A0 que la eleve al autor como ampliación de **Ap. A §3** en el próximo gate. |
| **P-13** | A0 / M9 | Proteger por hash la adyacencia **39:177-191**, de «La comisión cerró la inspección…» hasta «**Maja no solicitó acceso.**» inclusive (nombre propuesto: `S39-tercera`). Nada puede insertarse entre «La técnica tocó el precinto y anotó la hora.» y «Maja no solicitó acceso.»: esa contigüidad es lo que acota el hueco. |
| **P-14** | Todo el proyecto | Se mantiene **C-4 de W3**: la bolsa de viaje y la hoja de efectos personales no reaparecen. En particular, ninguna versión posterior de cap-06 puede hacer que la puerta del garaje de la noche del 26-nov anticipe, mire o roce el rincón donde N3 dejará la bolsa en diciembre. |
| **P-15** | Todo el proyecto | Las llamadas de Nora del 26-nov (06:247) no se cuantifican, no se fechan, no se explican y no se enlazan con la discusión por Kongsbakken (9:73, 14:149). Ninguna voz con autoridad puede derivar de ellas una señal, un reproche o una causa. «Maja no le preguntó desde cuándo llamaba. Nora tampoco lo dijo.» es el techo. |
| **P-16** | 33, 35, 40, 41, N6 (extiende P-10) | El nivel actual de atmósfera litoral en el naust y su umbral es el máximo. Ninguna imagen nueva de agua, hielo, oscuridad o reflejo, y ninguna mirada al agua desde el umbral por parte de Nora o de Jessie, sin pase previo mío. El inventario interior de 4:99-121 sigue sin ampliarse ni glosarse. |
| **P-17** | Todo el proyecto | Las cuatro palabras (`FLOR`, `CANELA`, `CARIES`, `NO`) no ganan nunca una afirmación de exclusividad —«solo en esta casa», «nadie de fuera podía saberlo»—. La inclusión de Alana en la ambigüedad (14:177) no se retira. «No toda» sigue siendo el techo. |
| **P-18** | 39 y ripples | La denuncia anónima del 17-dic (39:115) no gana origen, autoría ni atribución en ningún capítulo, acta o material de trabajo. «No puedo acreditar su origen» es definitivo. |
| **P-19** | 22, 29 y ripples | El hombre del caso de 2054 no tiene destino: no reaparece, no se sabe qué fue de él y, sobre todo, no se le da muerte ni derrumbe. «No volvió a escribir» es lo último que se sabe. |
| **P-20** | W4b y W5 | Ninguna instancia nueva del motivo «texto presente que no se lee» (papel doblado, página en blanco, título no preguntado, reverso sin leer). El recuento actual es el techo. §6.1. |
| **P-6** *(actualización)* | W7 | La relectura por adultización acumulada de Nora y Jessie sigue vigente y suma ahora 28, 33 y 39 a la lista (N2 + 10 + 22 + 31 + 40). Registro: W4a mejora el punto 7 respecto a v0. |

---

# 8 · Veredictos

| Capítulo | Veredicto |
|---|---|
| **cap-06** | **APROBADO CON CORRECCIONES** — C-2 y C-3, obligatorias antes del merge. Las tres calas se aprueban en lo demás, y la tercera (255) literal. |
| **cap-14** | **APROBADO** (con P-17). |
| **cap-16** | **APROBADO.** |
| **cap-22** | **APROBADO** (con P-19). |
| **cap-27** | **APROBADO.** |
| **cap-28** | **APROBADO.** |
| **cap-29** | **APROBADO.** |
| **cap-33** | **APROBADO** (33:225 queda en `vigilar`, con P-16; recorte opcional de 33:19 a criterio de A0). |
| **cap-39** | **APROBADO**, escena nueva incluida y **literal**. El hueco **no se cierra**. Con P-12, P-13 y P-18. |

## Veredicto de tanda

# APROBADO CON CORRECCIONES

Dos frases, ambas en cap-06 (C-2 y C-3), y una segunda lectura mía focalizada del diff post-A4 sobre **06, 33 y 39** (C-1), bloqueante para el merge. Sin `VETO`. Sin correcciones en los otros ocho capítulos.

Dicho sin la tabla: **W4a es la oleada más limpia que he revisado.** Cero hits de nivel A, una sola línea nueva que nombra a Jean, ninguna que nombre la muerte, y las dos escenas que los jurados fríos pedían por separado resueltas por objeto y por decisión, sin que nadie explique nada a nadie. La escena del locutorio de Maja frente a la técnica —el papel, el pliegue, el «No»— es de la familia de 4, 23 y 40: confía en el lector y no lo consuela. Lo que corrijo es una incoherencia con efecto secundario y una relación horaria que invitaba a poner un reloj donde el libro no lo pone. Nada más.

Firmado, **A7** · 2026-08-18 · sobre `git diff main..HEAD -- capitulos/` @ `1143abf` (rama `w4-familia`).
