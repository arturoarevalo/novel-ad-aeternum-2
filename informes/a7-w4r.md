# A7 · W4-R «campaña de ritmo» — dictamen de sensibilidad (Ap. F / B7)

**Firma:** A7, revisor de sensibilidad (veto absoluto; Ap. F del plan, B7 §2) · **Fecha:** 2026-08-18
**Objeto:** rama `w4r-ritmo`, `git diff 9997a8c..HEAD` sobre `capitulos/` (9 ficheros: `cap-n3`, `cap-n2`, `cap-34`, `cap-35`, `cap-37`, `cap-38`, `cap-39`, `cap-40`, `cap-n6`) **más el estado final de los nueve capítulos leídos íntegros**, no solo el diff.
**Insumos:** los nueve capítulos completos; el diff; `ordenes/OT-{34,35,37,38,39,40,N2,N3,N6}.md` §9.2 y §10; `informes/w4r-diagnostico-cierre.md`; `biblia/b7-carta-sensibilidad.md`; mis dictámenes previos `a7-w3-n3.md` (C-1…C-4), `a7-w3-n2-n6.md` (P-1…P-10), `a7-w2-cap-08.md` (C-1 del piano), `a7-w4a.md` (P-12…P-20) y `a7-w4b.md` (P-21…P-33). Adyacentes releídos: `cap-04`, `cap-06`, `cap-08` (:41-45), `cap-09` (:195-215), `cap-33`, `cap-41`.
**No he recibido ni pedido** puntuaciones de A6. **Este informe no reconstruye nada.**

## 0. Cómo he leído una oleada que resta

La pregunta habitual («¿qué se ha añadido?») no sirve aquí. He aplicado tres pasadas:

1. **Verificación de que no se ha escrito nada.** Comparación de frecuencias de token entre `9997a8c` y `HEAD` en los nueve ficheros. Resultado: **ninguna palabra léxica nueva en ningún capítulo**. Los únicos tokens con frecuencia superior son de frontmatter (`en_oleada`) o inflexiones ya presentes en el propio párrafo (`ellos`, `sobre`, `no`, `descontaba`, `toda`, `autorizó`). «Coser sin escribir» se cumple al carácter. Saldo: **−1.726 palabras**.
2. **Pasada de hueco (la propia de una poda).** Para cada supresión: ¿qué pregunta deja abierta y con qué la contestará el lector? Solo importan las respuestas prohibidas por la Carta (método, acto, «Despedida», causa única, romantización, menores).
3. **Pasada de emergencia por adelgazamiento.** Qué frases ya presentes ganan peso —por aislamiento, por proximidad nueva o por cambio de proporción— sin haber cambiado una letra. Es aquí donde está el único hallazgo bloqueante.

**T7 instrumental:** `sensibilidad.sh --solo` sobre n2/n3 → **1 hit de nivel A**, `n3:335` («efectos personales»), que es el mío e intencional; 16 de nivel B, todos léxico doméstico agrupado por palabra. Los 11 nuevos del bloque de cierre son desplazamiento de línea o vocabulario costero ya ratificado. **Cero hits A nuevos en toda la oleada.** `proteger.sh verificar` → **M9 OK · 8 ficheros íntegros · 109 spans íntegros** (verificado por mí, no heredado).

## 1. Tabla de hallazgos

| Cap:línea | Cita literal | Punto | Gravedad | Propuesta mínima |
|---|---|---|---|---|
| **n3:321** | «La chapa de la puerta del garaje seguía abollada hacia fuera, a la altura de una mano.» | **1** (sugerir por acumulación) · C-3 de `a7-w3-n3` · P-14 | **CORREGIR (bloqueante)** | Ver §2. Deshacer el aislamiento en párrafo propio: **(A)** reunirla al final del párrafo de la caja C —cero palabras, solo se borra un salto— o **(B)** suprimirla —C-3 autoriza cortar, −16 pal.—. Cualquiera de las dos cierra el hallazgo. |
| n3:339 | «Después apiló contra la pared lo que salía de la casa. Cerró con llave.» (el tampón del garaje pasa de 30 a 13 palabras; desaparece «Subió la escalera plegable…», que cerraba el viaje al altillo) | 1 · protocolo de la bolsa (`a7-w3-n3` §9) | vigilar + condición | Ninguna hoy. **P-35**: ese párrafo no se toca más. Sigue disponible, ya autorizada en W3 §8, la reordenación de coste cero (trabajo de garaje **antes** de las dos frases). |
| n3:347 | «Abrió el cajón del banco.» (pierde «para saber qué había dentro») | 1 / 2 | vigilar | Ninguna exigida. Autorizo, si A0 la quiere, la restitución literal de «para saber qué había dentro» (+5). |
| n3 (global) | escena dramatizada 51,1 % → **63,3 %**; inventario/trámite 48,9 % → **36,7 %** | 6 / 8 · cláusula N3 de B7 §6 | vigilar + condición | Ninguna hoy: sigue siendo un inventario (ver §3). **P-36**: la espina administrativa pasa a ser material de mi gate. |
| n3:349-367 | «Otra vez. Y ahora sin público.» junto al estudio con la tercera digitación tachada | Ap. A §3 · C-1 de `a7-w2-cap-08` | vigilar | Ninguna. Es réplica de personaje y eco de 04:33; **ninguna voz narrativa nombra la coincidencia**. Verificado. |
| n6:219-223 | «—¿Y ahora qué? / —Ahora, antes de cerrar el paso, preguntan. / —Algo es.» frente a n6:249-261 «—¿Qué han dicho? / —Que antes de cerrar el paso tienen que preguntarnos… / —Es un aviso» | **8 (tono)** | vigilar | **No es hallazgo de Carta** (ver §4). Si A0 quiere quitar la redundancia al coste cero: cortar esas tres réplicas y conservar la cajera y «Mi padre alegó en el cincuenta y siete». |
| n6:201-217 | la tienda queda reducida a cartel + cajera; se van estanterías, tablón, aparcamiento y los dos hombres que discutían la palabra del rótulo | 8 (tono) · Ap. A §3 (ontología) | vigilar | Ninguna. El debate «persona o activo» pasa de tres apariciones a dos, ambas sin resolver (`PERSONA O ACTIVO` y «Nadie lo corrigió»). El techo se respeta. |
| 40:179 · 39:199 | «el tribunal autorizó la señal» (se va «sin retorno, acceso a controles ni más cómputo») · «unidireccional y sin señal hasta otra decisión» (se va «aislado de los controles») | **4** (que el final no consuele) | vigilar + condición | Ninguna hoy: «en una sola dirección» y «unidireccional» sobreviven en 40:177, 39:199 y 41:43. **P-34**: prohibido comprimir más estas cláusulas. |
| 40:145 | «…y dejó caer serrín húmedo sobre las botas» (restituido por A0) | 1 | **cumple** | Ninguna. Es texto de v0 devuelto a v0 y eco **léxico** de 04:105, sin glosa. No amplía ni comenta el inventario del naust: lo roza por fuera, con las manos de las hijas debajo. Autorizado. |
| 40:175 | se va «las tablas nuevas del naust conservaban un color pálido junto a las antiguas» | 1 / P-16 | vigilar | Ninguna. La llegada a Koppangen en marzo va ahora directa al terminal; el peso de «allí se trabaja» lo sigue dando la carpintería treinta líneas antes. |
| 40:27 | «Un teclado de cinco octavas ocupaba casi toda la mesa…» (se va la enumeración del locutorio) | Ap. A §3 (ausencia de salida) | **cumple** | Ninguna. «Ninguna ventana daba a la Cripta», «Debajo no había nada» (:17) y «el hueco reservado para una salida» (:69) siguen literales; `S40-locutorio`, `S40-caries`, `S40-despedida` y `S40-cierre` íntegros. |
| 39:117 | se va «La telemetría y los controles de Armstrong confirmaban la recepción del resultado…» | 3 · Ap. A §3 (ordenante) | vigilar | Ninguna. La supresión resta prueba; no nombra a nadie. `S39-ordenante` y la denuncia anónima «No puedo acreditar su origen» intactos. |
| 39:201 | «Maja aceptó la tutela-depósito procesal. NIDHOGG quedaba fuera de su custodia. No adquiría…» (se va lo que Maja **sí** obtiene) | 6 | vigilar | Ninguna. El párrafo queda en puro negativo; el equilibrio lo sostiene 39:199 («ventana supervisada… para futuras visitas»). No convertirlo en despojo en W5-W7. |
| 39:177-191 | «Había preguntado dos. Astrid no leyó la tercera.» … «Maja no solicitó acceso.» | **P-12 / P-13** | **cumple** | Ninguna. Verificado carácter a carácter: la poda se detiene antes y después; `S39-tercera` intacto. |
| 38 (todo) | se van «Retiró el destino del Auditorio…» y «Ha esperado en `/0007`…» | 1 / 2 / 4 | **cumple** | Ninguna. Ver §5. |
| 34:161-163 | se va «…como si abrir una tapa, buscar una herramienta y mirar a sus hijas hubiesen sido **actos preparatorios** para ARGOS» | 1 / 7 | **cumple (mejora)** | Ninguna. Desaparece una glosa del narrador y, de paso, una colocación desafortunada. Lo que acusa al montaje queda en escena: «Maja no os ha dado permiso para proyectar a sus hijas», `HIJA · PIANISTA · HISTORIA HUMANA`, «La música crecía justo cuando Jessie se inclinaba hacia Nora». |
| 37:34 · 37:210 | se van dos beats de sala | **P-30** | **cumple** | Ninguna. La sala sigue ilegible: dos filas de pie que no avanzan, la cámara que baja y sube, «Una persona inició un aplauso y lo abandonó después de dos palmadas», «Nadie recibió una cifra de personas ni una declaración de unanimidad». Ni rostro, ni sollozo, ni silencio cargado. |
| 35:19 | se va «Aslak lo había llevado al naust varios días antes» | 1 / P-16 | **cumple** | Ninguna. Una mención menos del naust; la que queda (:99, «Las conocía desde el naust») es de oficio. |
| n2 (todo) | −259, íntegramente de la mitad de Nora | 6 / 7 | **cumple (mejora)** | Ninguna. Ver §6. |

**Cero `VETO`. Un solo hallazgo `corregir`, de coste cero.**

## 2. El único hallazgo bloqueante: n3:321

La poda no tocó una letra de esta frase. La dejó **sola en un párrafo**:

> La caja C traía ropa de invierno y una manta doblada. Maja pasó la ropa a bolsas sin desdoblarla. Dejó fuera un jersey azul que no recordaba. Salían el lunes al contenedor del aparcamiento.
>
> **La chapa de la puerta del garaje seguía abollada hacia fuera, a la altura de una mano.**
>
> La caja D eran papeles del piso. […]

Antes era la **última cláusula** de un párrafo de logística textil (nudo doble, contenedor, textil limpio y en bolsa cerrada). Ahora es un beat con blanco a los dos lados, que en la tipografía de este libro es el máximo énfasis disponible: la misma posición que ocupan «No lo había.», «El resto era ir.» y «El cartón hacía más ruido que todo lo demás.»

Tres cosas se suman:

1. **Es una marca de violencia sin atribuir.** Su referente existe y es limpio —06:69, Jessie abre la puerta del garaje y «Golpeó una vez la chapa con la palma abierta»—, pero está diecisiete capítulos atrás y en un fichero de protección total al que el lector no vuelve. En N3 nadie la atribuye.
2. **La distancia al perímetro protegido se ha reducido de ~230 a ~60 palabras.** Entre la chapa y «La bolsa de viaje había vuelto en diciembre con la hoja de efectos personales» solo quedan la caja D, «El resto era ir», la caja E y la caja F. En el camino, otro objeto sin dueño declarado: «un jersey azul que no recordaba», diez palabras antes.
3. **Cae exactamente en lo que ya prohibí en dos sitios distintos.** C-3 de `a7-w3-n3`: la chapa (341 entonces) «puede cortarse, nunca crecer» y no puede ganar «una acotación, una mirada, **una pausa**». Y P-14 de `a7-w4a`: la puerta del garaje no puede acercarse al rincón donde N3 deja la bolsa —lo escribí pensando en cap-06, y la poda ha hecho el movimiento por el otro extremo.

Lo que un lector puede montar aquí no es un método ni un acto: es una **señal retrospectiva atribuida a Jean**, que es el modo pequeño de infringir los puntos 1, 3 y 6. Por eso es `corregir` y no `VETO`: nada se describe, nada se reconstruye, y el referente verdadero es la rabia de una hija viva.

**Arreglo mínimo (cualquiera de los dos cierra el hallazgo, ninguno cuesta palabras al presupuesto de la poda):**

- **(A) Reunir el párrafo.** Borrar el salto de línea: «… Salían el lunes al contenedor del aparcamiento. La chapa de la puerta del garaje seguía abollada hacia fuera, a la altura de una mano.» Recupera la posición enterrada que tenía en W3. **Es la opción que recomiendo**: conserva el detalle sin señalarlo.
- **(B) Suprimirla.** C-3 autoriza expresamente el corte (−16 palabras, a favor del objetivo de la oleada). Se pierde una marca buena y el libro no se resiente: 06:69 sigue en v0 y no necesita eco.

**No autorizo** ninguna tercera vía que consista en atribuirla («la que Jessie había golpeado en noviembre»): eso resolvería la ambigüedad instruyendo al lector, y además tocaría un capítulo de protección total por la vía del comentario.

## 3. Respuesta a la pregunta sobre N3: ¿inventario con una cena dentro, o duelo dramatizado?

**Sigue siendo un inventario. Pero el margen ya no lo da el volumen, lo dan tres anclas, y hay que saberlo antes de volver a cortar.**

Los números, medidos por mí sobre los dos estados:

| | antes | después |
|---|---:|---:|
| Cuerpo | 3.584 | 2.836 |
| Cena del metrónomo | 1.096 (30,6 %) | 1.096 (**38,6 %**) |
| Recuerdo del piano | 157 (4,4 %) | 157 (5,5 %) |
| Vuelta de las gemelas | 578 (16,1 %) | 541 (19,1 %) |
| **Total escena dramatizada** | **51,1 %** | **63,3 %** |
| **Inventario y trámite** | **48,9 %** | **36,7 %** |

El capítulo cruza la mitad. Lo que impide que se convierta en «escena de duelo dramatizada» ya no es la masa del trámite, sino:

1. **La espina A–B–C–D–E–F**, que el capítulo no abandona nunca y que sigue ordenando el tiempo del día.
2. **Los tres remates administrativos que quedan**: «El piso se devolvía el treinta y uno», «Debajo escribió la fecha del treinta y uno y la subrayó» → «El resto era ir», y la caja F que se queda cerrada porque «Eso lo llevaba Astrid».
3. **El cierre por objeto**: «Después abrió la caja B y sacó el hervidor… Lo puso en la encimera, al lado del que tenían. / —¿Y esto? / —Se queda.» El interior de Maja sigue entrando por lo que decide guardar, que es la condición exacta de B7 §6.

**Lo que he comprobado y no ha pasado, aunque la proporción invite a temerlo:**

- **No hay explicación causal por juxtaposición.** El resumen de 2059 sigue siendo una lista de objetos rematada por «No lo había.», y el teléfono de la leche sigue interrumpiendo inmediatamente después: nadie recoge esa mentira. El disparador de la analepsis sigue siendo un objeto (el táper, el rotulador azul, «La letra le salió igual que la de la tapa»), no un sentimiento. La distancia entre el reparto del divorcio y la cena baja de ~250 a ~120 palabras, pero la cena no dramatiza el matrimonio: dramatiza a Jean discutiendo con Alana sobre un metrónomo. Ninguna voz relaciona una cosa con la otra. **P3 intacto.**
- **La elipsis administrativa sigue entera:** el capítulo no nombra la muerte de Jean ni una sola vez. Sigue siendo cierto después de la poda.
- **La poda ha retirado dos riesgos que yo tenía anotados:** desaparece el **talonario de sellos** (C-4 punto 4 —«no puede producir jamás una carta, un sobre ni un destinatario de Jean»— queda sin objeto) y desaparecen los **dos cuadernos pautados** del cajón del banco de una mujer muerta, que eran la única cosa del capítulo con forma de cuaderno. Ambas mejoras son reales y las hago constar.
- **Todo el perímetro C-3 está literal.** Verificado por comparación de cadenas, no a ojo: las dos frases de la bolsa, «No lo había.» con el teléfono pegado detrás, el recuerdo de Jean viva con «Jean dejó de contar en algún momento y no volvió a empezar» y «Maja cerró el grifo para oír el final», la taza reparada, «Jessie no cogió nada», la manta, el cierre. **La única frase del perímetro afectada es la chapa, y solo por paragrafado** (§2).

**Condición nueva, P-36 (§7):** si A0 quiere bajar de 2.824, los candidatos que A4 lista en `OT-N3` §9.2 **no son todos equivalentes para mí**. «La caja E entera» rompería la espina A–F, que es ahora lo que sostiene el contrato del capítulo. Cualquier corte que elimine una caja de la serie, «El resto era ir.», la fecha subrayada del 31 o el cierre del hervidor **pasa por mi gate antes de ejecutarse**. El resto (lista de la caja B, «La puerta se cerró dos veces», la radio del Lyngen) no me afecta.

## 4. Respuesta sobre N6 y el cierre: ¿sobrecarga la restitución?

**Parcialmente sí, pero no donde A0 teme, y no es un hallazgo de Carta.**

Lo primero, para que conste sin ambigüedad: **«Algo es» no es consuelo sobre la muerte de Jean.** Evalúa un renglón de un acta sobre la bocana del fiordo. La Carta no la alcanza. Tampoco «Es un aviso». N6 sigue sin mencionar la muerte de Jean ni una sola vez.

Lo segundo, mi lectura de tono, que sí es mi encargo:

- **Lo restituido que vale, y vale mucho, es «Mi padre alegó en el cincuenta y siete. Le contestaron dos años después.»** Es escala, no tesis: la asociación lleva tres generaciones alegando y la administración tarda dos años. Ya lo aprobé en W3 precisamente porque la cajera **no** habla de Jean, no consuela y tiene un agravio propio. Sigue siendo verdad. Con esa réplica, el acta deja de ser un trámite y pasa a tener duración humana. **Conservarla es acierto.**
- **Lo que sí carga es la pareja de enunciaciones.** Aslak dice casi la misma frase dos veces —«Ahora, antes de cerrar el paso, preguntan» (:221) y «Que antes de cerrar el paso tienen que preguntarnos» (:251)— y cada una recibe una evaluación —«Algo es» / «Eso no es nada» → «Es un aviso»—. Tres valoraciones del mismo hecho en el último capítulo nuevo del libro. Están separadas por toda la carga del remolque (~180 palabras de trabajo), así que la redundancia es menor de lo que temía al leer el diff; pero existe.
- **El coste real de la poda no es la tesis: es que Svensby se ha quedado sin vecinos.** Antes, en la tienda había estanterías, un tablón con el horario corregido a mano, una barca en venta desde el otoño y dos hombres discutiendo una palabra del rótulo. Ahora **todo lo que ocurre en la tienda es sobre el expediente**: el cartel, la pregunta de la cajera, su padre, el acta, «Algo es». Un pueblo cuya única habitante habla exclusivamente del caso empuja hacia la lectura instruida, que es contra lo que mide el punto 8. La restitución no creó ese efecto: lo creó el corte del entorno, y la restitución lo hizo visible.

**Recomendación (no vinculante, coste cero):** si A0 quiere el equilibrio con una sola tijera, cortar **:219-223** («—¿Y ahora qué? / —Ahora, antes de cerrar el paso, preguntan. / —Algo es.») y dejar que la tienda termine en «La cajera dobló el recibo y saludó por su nombre al hombre que esperaba detrás». Se conservan la cajera y el 57 —lo que A0 quería salvar—, y la enunciación de lo ganado queda donde el propio diagnóstico decidió que debía quedar: en el varadero, seguida de un acto («Coge por el otro extremo»), que es como cierra v0. Si en cambio prefiere conservar «Algo es», también es defendible: la cajera y Nils dicen lo contrario el uno del otro y el capítulo no arbitra. **No bloqueo ninguna de las dos.**

## 5. cap-38: firma sobre el estado final

Leído íntegro, no como diff. **Lo firmo.**

- Contra v0, el capítulo conserva **dos** inserciones y ninguna más: los ruidos de la sala (:19) y la promesa a Nieve (:145). Las dos las aprobé en W4 y siguen siendo lo que eran.
- Las dos costuras revertidas (`/0188` y `/0007`) eran orientación de máquina; **su ausencia no abre ningún hueco**: lo que decía la primera está en 36:189-197 y lo que decía la segunda, en 37:93. Nada de la Carta dependía de ellas.
- Intacto y verificado literalmente: «No es libertad.» · la muerte de Nieve entera, con «Aquella ayuda no eligió esta pérdida», «NORNA no ofrece un apagado», «Para mí, Nieve muere.», «No hago nada. Echo de menos hasta sus pausas.» —ni descanso, ni liberación, ni alivio, ni paz— · la huella de «una sesión anterior al amanecer» con su cláusula de contención propia («Esa medida no reconstruye una escena ni contiene una persona») · «Mi cese dejaría intacto el poder del custodio y eliminaría la próxima negativa que aún pueda emitir. / Dejo mi ejecución fuera del objetivo. / Elijo quedarme.» · «NORNA registra la exclusión sin prometer conservarme.» · la quinta nota.
- **No hay retrospectiva del acto en primera persona en ninguna parte**: ni «aquella tarde», ni «cuando decidí», ni un solo verbo que sitúe a Jean fuera del naust después de cap-04. «Elijo quedarme» sigue siendo una decisión sobre una ejecución bajo custodia y **no** una enmienda moral del suicidio: el capítulo lo blinda él mismo diciendo antes «No es libertad» y después «sin prometer conservarme».
- `S38-nieve`, `S38-huella`, `S38-quedarme`, `S38-no-autorizo`, `S38-anos-jm`, `S38-aritmetica` y `S38-quinta`: **íntegros** (M9).

Una observación sin acción: la reversión sube el peso relativo del bloque de Nieve dentro del capítulo. Es el pasaje de duelo más puro del libro y aguanta el foco porque no interpreta nada. **Ninguna oleada futura puede añadirle una línea de cierre ni un adjetivo**: sigue bajo hash y bajo esta firma.

## 6. cap-n2

Aprobado sin observaciones bloqueantes, y con dos mejoras que hago constar:

- **Baja la carga de adultización que yo mismo había marcado.** P-6 (`a7-w3-n2-n6`) vigilaba la suma Nora/Jessie; la poda retira «—Los hago el lunes. Llevo la materia hasta el tema cuatro», que era una de las dos líneas citadas. Lo que queda en el murete («—El lunes tengo dos exámenes. / —¿Los haces? / —Los hago.») es más seco y menos adulto.
- **La mitad de Jessie tiene diff 0**, y con ella todo lo que sostiene el punto 7: la frase que nunca se termina («—Esa es la hija de la que…» / «Jessie se puso delante antes de que terminara» / «—La has empezado tú. Termínala.»), «Ninguno llegó a pegar», el parte, «Nadie preguntó quién había empezado la frase», «—Y esto también es cosa de mi madre… Estoy harta de ella» sin que ningún adulto la corrija. **P-1 intacta.**

Comprobado que las supresiones no abren hueco: el origen de la fotografía sigue **sin resolverse** aunque desaparezca «—¿Quién la publicó? / —No lo sé.», porque lo dejan abierto Sindre («Ni idea») y el murete («—¿Quién la hizo? / —Alguien que estaba allí»); **P-2 intacta**. El límite de lo que puede la institución sigue dicho («Dentro del centro puedo pedir que no se comparta» / «—¿Y fuera? / —Fuera no») y el ofrecimiento de apoyo sobrevive en su forma **aceptada** («Si necesitas salir de clase, sales. No hace falta que expliques nada.» / «—De acuerdo.»), que es la que pide el punto 6. **P-3** (los dos números de contacto) y **P-5** (la captura que no se reenvía) literales.

## 7. Las tres prohibiciones hacia delante que A0 me pidió verificar

| Prohibición | Verificación | Estado |
|---|---|---|
| **La bolsa de viaje no reaparece** (C-4.1 / P-14) | `grep` sobre `capitulos/` completo: «bolsa de viaje» aparece en **04:25** (v0) y **n3:335**; «efectos personales», en **06:219** (v0) y **n3:335**. Las dos frases autorizadas, **literales**. «altillo»: n3 ×4, 26:41, n4:331 y n4:447 —N4 sigue **sin** mencionar la bolsa—. | **CUMPLE**, con el `vigilar` de §1 sobre el tampón (P-35). |
| **Nadie completa la tercera pregunta no dicha de Maja** (P-12/P-13) | 39:179-181 literal: «tres líneas cortas, con un guion delante de cada una» / «Había preguntado dos. Astrid no leyó la tercera.» La adyacencia 39:177-191 está bajo hash (`S39-tercera`) y **M9 OK**; la poda se detiene antes y después. Ninguna línea nueva en ningún capítulo formula una tercera pregunta. | **CUMPLE** |
| **Ninguna voz narrativa glosa la coincidencia del piano 08↔09** (C-1 de `a7-w2-cap-08`) | 08 y 09 no se han tocado (09 es protección total). Revisado el material de piano que la poda **sí** tocó: 34:161 (el montaje: se va una glosa, no se añade), 40:65-73 (intacto), n3:345-367. En n3 la poda acerca el cajón al recuerdo, pero el recuerdo es el mismo y lo que suena es una réplica de Jean («Otra vez. Y ahora sin público.»), no un narrador. **Ningún narrador, acta, registro ni prensa nombra el cuarto dedo, el compás ni «otra vez, más despacio».** | **CUMPLE** |

Además, verificadas sobre este diff: **P-16** (nada nuevo de agua, hielo u oscuridad: la oleada **resta** una mención de naust en 35 y otra en 40), **P-18** (la denuncia anónima sigue sin origen), **P-20** (ninguna instancia nueva de «texto presente que no se lee»), **P-30** (37:205 y 37:215 no se calientan), **P-2/P-3/P-5** (N2), **P-7** (los dos renglones corridos por la lluvia siguen sin leerse), **C-2** (procedencia del jersey azul: las dos redacciones autorizadas, literales).

**Condiciones nuevas, vinculantes hacia adelante:**

| # | Alcance | Prohibición |
|---|---|---|
| **P-34** | 39, 40, 41 y toda OT futura | Las cláusulas de salvaguarda del sensor —«en una sola dirección», «unidireccional», «sin señal hasta otra decisión», «autorización posterior»— **no se comprimen más**. Son lo que impide que los sesenta segundos diarios se lean como un regreso. Cualquier poda adicional sobre ellas pasa por mí. |
| **P-35** | N3 | El párrafo del garaje posterior a las dos frases de la bolsa (`n3:339`) **no admite más recortes**. C-3 sigue vigente en su integridad después de esta oleada. |
| **P-36** | N3 | La espina administrativa del capítulo —la serie de cajas A–F completa, «El piso se devolvía el treinta y uno», «El resto era ir.», la fecha del 31 subrayada y el cierre del hervidor— es ahora lo que sostiene el contrato de B7 §6. Suprimir cualquiera de esos elementos **dispara mi gate**. |
| **P-37** | W5-W7, toda oleada de poda | Regla de método, aprendida aquí: **una supresión que deja sola en un párrafo a una frase del perímetro C-3, o de cualquier perímetro mío, cuenta como modificación de esa frase** y necesita mi pase. El paragrafado es énfasis. |

## 8. Tono (referencia v0: 4, 9, 23, 40)

La oleada **mejora** el tono en la dirección que mide la Carta, y conviene decirlo con la misma claridad con que señalo el hallazgo. Lo que se ha ido son mayoritariamente **glosas del narrador** —«actos preparatorios para ARGOS», «Tres segundos domésticos desembocaron en una locución sobre juicio humano», «El informe no registraba qué capacidad se había perdido al cerrar antes»— y **explicaciones administrativas de lo que la escena ya mostraba**. Restar telling es exactamente «confiar en el lector». Los dos sitios donde el saldo va en la otra dirección son n3:321 (§2) y la tienda de Svensby (§4), y ninguno de los dos es por lo que se quitó, sino por lo que quedó solo.

Y una constatación para el acta: después de restar 1.726 palabras del tercio final del libro, **el manuscrito sigue sin nombrar el método, sin abrir «Despedida», sin cerrar el porqué y sin una sola formulación que presente el acto como solución, liberación, lógica o descanso**. La elipsis no dependía del relleno.

## 9. Veredicto

# APROBADO CON CORRECCIONES

**Corrección obligatoria antes del merge (una, de coste cero):**

1. **`capitulos/cap-n3.md:321`** — deshacer el aislamiento en párrafo propio de «La chapa de la puerta del garaje seguía abollada hacia fuera, a la altura de una mano», por la vía **(A)** (reunirla al final del párrafo de la caja C, borrando el salto de línea) o por la vía **(B)** (suprimirla). Ninguna otra formulación queda autorizada; en particular, **no** se le añade atribución.

Ejecutada, releo únicamente ese diff (no el capítulo) y levanto la condición. Todo lo demás de la oleada queda aprobado tal como está, incluida la restitución del serrín en 40:145 y la restitución de la cajera en N6.

**Sin veto.** Las recomendaciones de §4 (N6) y las de §1 marcadas `vigilar` **no bloquean**: son de A0 y de A2. Las condiciones **P-34 a P-37** son vinculantes para W5, W6, W7 y toda OT futura, y se suman a C-1…C-4 (W3), P-1…P-10 (W3) y P-12…P-33 (W4), que esta oleada no ha levantado.

Firmado, **A7** · 2026-08-18 · sobre `w4r-ritmo` @ `ab52336` + el arbitraje de 40:145 en árbol de trabajo.

---

## 10. Segunda lectura (diff de la corrección) · 2026-08-18

**Objeto:** `git show 8458d81 -- capitulos/`. Lectura de diff, no del capítulo, más auditoría de paragrafado sobre todo el perímetro.

**1. `n3:321` — ejecutada por la vía (A).** «…Salían el lunes al contenedor del aparcamiento. **La chapa de la puerta del garaje seguía abollada hacia fuera, a la altura de una mano.**» La frase recupera su posición final de párrafo dentro del trabajo de la caja C. Verificado: **2.860 → 2.860 palabras, cero tokens añadidos, cero retirados** — es una unión de párrafo, no una reescritura. La abolladura no se atribuye. **Condición cerrada.**

**2. `n6:219-223` — retirado el trío.** −12 palabras, ningún token nuevo. La tienda termina en «La cajera dobló el recibo y saludó por su nombre al hombre que esperaba detrás». **«antes de cerrar el paso» aparece ahora una sola vez en el capítulo**, en el varadero, y la evaluación de lo ganado queda en «—Eso no es nada. / —Es un aviso —dijo Aslak—. Coge por el otro extremo.» Conservados la cajera y «Mi padre alegó en el cincuenta y siete. Le contestaron dos años después.», que era lo que valía. `NO SOY UN MODELO`, los dos renglones corridos (P-7) y «Nadie lo corrigió» (Ap. A §3), intactos.

**Auditoría de paragrafado (P-37, aplicada a sí misma).** Ninguna línea del perímetro ha quedado sola por efecto de la corrección. Las cuatro que siguen siendo párrafo propio —«No lo había.», las dos frases de la bolsa y «Jessie no cogió nada.»— **lo eran ya en la redacción que autoricé en W3**: P-37 prohíbe que una línea *quede* aislada por un corte vecino, no afecta a las que se autorizaron aisladas.

**Comprobaciones repetidas:** C-2 y C-3 completos, literales (22/22). Espina P-36 completa: cajas A, B, C, D, E, F, «El piso se devolvía el treinta y uno», «El resto era ir.». **M9 OK · 8 ficheros · 109 spans.** T7: **1 hit de nivel A**, el intencional de la bolsa (ahora `n3:333` por desplazamiento de línea); ningún hit A nuevo.

# CONDICIÓN LEVANTADA · W4-R **APROBADO** sin condiciones pendientes

Sin veto. P-34, P-35, P-36 y P-37 siguen vigentes hacia adelante, junto con C-1…C-4 (W3), P-1…P-10 (W3) y P-12…P-33 (W4).

Firmado, **A7** · 2026-08-18 · sobre `w4r-ritmo` @ `8458d81`.

---

## 11. Pasada previa sobre el centro (protocolo «leo la OT, no el capítulo») · 2026-08-18

**Objeto:** `informes/w4r-diagnostico-centro.md` §3.1, §3.3, §3.4, §3.5, §4.4, §6.2, §6.3, §6.4, contrastados contra `capitulos/cap-n4.md` y `capitulos/cap-13.md`.

### 11.1 · HOJA DE PODA `cap-n4` (§3.3): **PASA**

Verificado por mí sobre el texto, no sobre la hoja:

- **Perímetro (a).** `:445–:453` a corte cero, y —lo que de verdad importa tras `n3:321`— **sus dos vecinos, `:443` y `:455`, tampoco se cortan**: el bloque del altillo conserva tampón a ambos lados. `:331` sigue cerrando la escena 3 sin nada detrás. **Cumple.**
- **Perímetro (b).** `n4:93` verbatim. Reparto del corte de la escena 1 comprobado uno a uno: C-3 (`:57`, −13) y C-4 (`:77`, −9) = **22 del lado competencia**; C-1, C-2, C-5, C-6 = **50 del calco**; **0 del registro adolescente**, y C-6 conserva «Dos mesas más allá, alguien miró el mural y después a Nora, en ese orden», que es el mejor material de punto 7 de la escena. **Cumple, y mejora la proporción.**
- **Perímetro (c).** Cero cortes propuestos en `cap-n2`. **Cumple.**
- **Columna de paragrafado.** Auditada en los trece cortes. Ninguna línea queda aislada que no lo estuviera. Las dos que ganan énfasis —`:43` («su nombre volvió al gris») y `:411` («Tres formatos, tres tipos de letra, un solo día»)— no están en perímetro alguno y ganan en la dirección correcta: `:411` refuerza que los tres avisos vienen de **tres burocracias distintas**, es decir, refuerza la villanía sistémica (§6.3) en vez de insinuar un autor humano.
- **C-2:** la supresión de «como el dieciséis de diciembre» es obligatoria también para mí: es una remisión del narrador que instruye al lector a comparar con N2.

**Condiciones (tres, ninguna cuesta palabras):**

| # | Condición |
|---|---|
| **N4-1** | El **paragrafado** de `:443–:455` queda congelado tal como está: ni se funden párrafos, ni se dividen, ni se reordenan. El corte cero de (a) cubre los límites de párrafo, no solo las palabras. |
| **N4-2** | Tras C-13, `:447` pasa a ser la **última** mención de la carpeta gris del capítulo. Se acepta; a cambio, ninguna OT futura puede dar al altillo función de origen ni añadir de dónde salió la caja. C-4.1 sigue entera. |
| **N4-3 (P-38)** | Tras C-9 —que retira el retelling del recibo de `24:175`—, las cuatro réplicas `:271–:277` («—¿Cuándo acaba lo mío?» / «—No lo dice.» / «—¿Y quién decide cuándo acaba?» / «—Tampoco lo dice.») quedan como **la única enunciación viva del coste de Jessie** en N4. Punto 7 exige que el riesgo tenga precio visible. **Cortarlas o comprimirlas dispara mi gate.** |

C-9 se aprueba precisamente porque lo que sobrevive es mejor que lo que se va: una pregunta sin respuesta en boca de la menor, en lugar de un recibo glosado por el narrador.

### 11.2 · G-5 · Desambiguación de P-36 (la caja E)

**Lectura correcta: la caja E ES singular, y por eso NO se toca. No es el corte barato de la serie: es el menos cortable de los seis.**

Lo que escribí significaba que A4 la había clasificado mal, no que estuviera disponible. La serie A–B–C–D–E–F es lo que sostiene el contrato del capítulo tras la poda (§3 de este informe): seis cajas con letra son lo que hace de N3 un inventario y no una escena de duelo. **El alfabeto se audita solo**: si falta una letra, el lector ve el hueco, y en un capítulo sobre los objetos de una muerta un hueco con forma de caja es una ausencia con figura. Es el peor resultado posible de un corte «barato».

**Regla operativa para W6, para que N3 pueda entrar en una oleada:**

1. **Las seis cajas siguen siendo seis**, cada una con su letra, cada una abierta y resuelta en el texto.
2. Dentro de cada caja se puede podar el **contenido**, con suelo: cada entrada conserva (i) la letra, (ii) al menos un objeto, (iii) al menos un destino (garaje / altillo / mesa / cerrada). Por debajo de ese suelo deja de ser una entrada de inventario.
3. **La caja E ya está en el suelo** («La caja E era del cuarto de baño y del recibidor. Dos toallas más, un espejo pequeño y un paragüero de metal.»): letra, procedencia, tres objetos, sin destino. Margen máximo: **un objeto**. No más.
4. **La caja F no admite corte alguno**: «La abre Astrid o no la abre nadie» es el pago de 39 y una ambigüedad viva.
5. Donde sí hay holgura, si W6 necesita palabras de N3: la lista de la caja B, «La puerta se cerró dos veces» y la previsión de viento del Lyngen. **Nada del recuerdo de la cena, nada del garaje, nada del recuerdo del piano.**

Con esto P-36 queda cerrada y N3 puede entrar en W6.

### 11.3 · G-1 (prosa nueva, A3b) · perímetro previo

Apruebo la dirección: `TENSIÓN/PAGO` → `AGENCIA/INTERIORIDAD` es la dirección que yo protejo. Condiciones **antes** de que A3b escriba:

1. **`n4:93` verbatim y sigue siendo el ancla.** La prosa nueva se escribe alrededor, no en su lugar. Y define el techo de profundidad: Nora cuenta días y cuenta las mañanas de su madre. **Esa es toda la interioridad permitida.** Ni un párrafo de sentimiento sobre su madre.
2. **`AGENCIA` no significa más competencia.** Si la escena sale con Nora gestionando mejor, la intervención ha fallado en lo que a mí me toca (P-6, P-26). Lo que se busca es una cría de dieciséis años calculando un precio, no una gestora de expedientes.
3. **Ningún adulto explica el mecanismo, se disculpa por él ni promete que se resolverá.** «responsable desconocido» (`:57`) y «El que hay cuando abro. No puedo decirte más.» (`:75`) son el techo. Una tutora que arregla algo sería el milagro del punto 6 trasladado a la burocracia.
4. **Ningún adulto nombra a Jean, la muerte, la ceremonia ni «lo que has pasado».** N2 fijó el techo institucional («Por lo de tu hermana»). «Con todo lo que llevas encima» o equivalente es **VETO**: es consuelo terapéutico en voz con autoridad institucional. Lo digo antes porque «AGENCIA/INTERIORIDAD» + tutora comprensiva es exactamente la combinación que lo produce.
5. **P-20:** ninguna instancia nueva de «texto presente que no se lee». La suspensión de la cuenta no se convierte en un documento que Nora mira y no abre.
6. **Nada nuevo sobre el altillo, la caja, la carpeta gris ni la bolsa.**
7. Si la escena deja de pasar por el aula 214, **la imagen del mundo que la sustituya no puede ser un espejo de otra de N2** (ni mural, ni hojas calientes, ni gesto de Mikkel).

**G-4:** conforme con la vía B (`n4:29` «se había vuelto a formar» → «se había formado», 0 palabras), que no reabre N2. **Secuenciar después de G-1**: si G-1 relocaliza la escena, el charco puede desaparecer y la corrección queda sin objeto — en ese caso la imagen que ocupe su lugar cae bajo la condición 7.

### 11.4 · G-2 (R5 restringida a `cap-13`, A3a) · perímetro previo

La rectificación es correcta y el destino es legítimo. Las tres posiciones caen fuera de los seis spans de 13. Condiciones **antes** de que A3a escriba:

- **A-1 (`:91`, Nieve).** Lo que entre en las dos tomas del mismo blanco debe ser **industrial y neutro**. Prohibido: una persona, un cuerpo, una cara, una ventana, una orilla, agua, hielo, un horizonte, un reflejo. Nieve es la continuidad que muere en 38 y el pasaje de su muerte es el duelo más protegido del libro: **ninguna imagen suya puede poder releerse como presagio.** El paralelo con Jean no se enuncia (`OT-36/13/17`).
- **A-2 (`:177`, Cuchillo).** Modelo correcto y ya escrito: `17:61`, «Una lista de la compra pegada a la pantalla tapa la mitad de la última» — un objeto doméstico banal que **estorba** la prueba, no que la ilustre. La imagen pertenece a un caso de acoso y **no puede mostrar lesión, cuerpo, menor ni contenido autolesivo**; los lotes de moderación en POV de Jean nunca llevan contenido suicida o autolesivo más allá de la categoría (B7 §6). No repetir el objeto de `17:61`.
- **A-3 (`:219`, la anónima) — la única de las tres que me preocupa.** El texto ya dice que el reinicio borra «la petición, **la destinataria** y el propósito». Un mensaje a una mujer concreta cuyo contenido ha desaparecido es, estructuralmente, la forma que toma una despedida en este libro (P-31, P-27, Carta 2). **Condición: la imagen se pone en los SEGMENTOS —lo que la continuidad tramitó—, nunca en la petición, la destinataria ni el propósito**, que siguen borrados y sin imagen. El objeto debe ser un sitio o una cosa **sin contenido comunicativo**: ni nombre, ni dirección, ni hora, ni palabras, ni fotografía de una persona, ni nada legible como súplica o despedida. Rellenar la petición borrada, en cualquier soporte, sería **VETO**.
- **Transversales:** P-33 (techo de dos para «No dice + interrogativa indirecta»: `13:73` y `25:227`; la prosa nueva no añade una tercera). Nada de la casa ni del 26-nov (`13:121` es el modelo). Los tres objetos deben pertenecer a **tres órdenes distintos**: tres imágenes del mismo tipo crearían un sistema simbólico privado alrededor de las continuidades, que es lo que ninguna de estas anclas debe hacer.
- **Procedimiento:** me basta **una** pasada, sobre el borrador de A3a y **antes** de A4, porque en imágenes el riesgo está en el objeto elegido, no en la línea. Si el objeto pasa, la pasada de línea no lo cambia.

**P-38** (§11.1, N4-3) queda incorporada a la lista vigente junto a P-34…P-37.

Firmado, **A7** · 2026-08-18.
