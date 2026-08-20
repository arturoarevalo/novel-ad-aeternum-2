# A7 · W11 · Consulta previa de nomenclatura

**Insumo:** consulta de A0 del 2026-08-20 · `ordenes/OT-W11-01.md` §5 · `plan-w11.md` §2·D
**Vinculante aplicado:** `biblia/b7-perimetro.md` (§1 Carta, §1 definiciones, R1, R3, R4, R6, R7·5, R7·7, R7·14, R9, §5·5, §6, §8b·W9-21, §8f·A7-it4-C8)
**Método:** censo `grep` de los cinco términos sobre los 48 capítulos; resolución de los 139 spans de `protegidos/spans.json` con `proteger.extraer_span` para buscar los términos **dentro** del cuerpo protegido y no solo en `inicio`/`fin`; recuento separado de ocurrencias en monoespaciado y en prosa; lectura a mano de cap-01, cap-02 (120-225), cap-13 (140-205), cap-18 (175-195), cap-22 (125-140), cap-26, cap-29 (65-120), cap-30 (55-215), cap-33 (140-210), cap-35, cap-40, cap-41, cap-43 (130-195), cap-45 (100-200); contraste de lexemas (`supervis-`, `incidencia`, `fondo`, `hoja`) en todo `capitulos/`.

**Convención de citas de este documento** (la de b7 §2): dentro de comillas angulares, verbatim; toda glosa va fuera; el literal manda y el número solo localiza. Las citas se dan en el orden canónico «literal» (`cap-NN:LL`) para que `verificar_b7.py` pueda leerlas — ver H-14.

---

## 0 · Lo primero, porque cambia la pregunta

**El libro ya hace lo que pide el editor, y lo hace con un mecanismo que esta pasada borraría.**

El método vigente es: **el código aparece en monoespaciado, como salida del sistema; la prosa se refiere después a la cosa con un nombre común.** No es una hipótesis. Está en el texto, en los cinco términos, y se verifica en un minuto:

| término | el ancla monoespaciada | la perífrasis que ya existe en prosa |
|---|---|---|
| INC-441 | cap-40, línea 263 | «asociaría su identidad, la incidencia, la hora y la puerta» (`cap-40:267`) |
| R-1189 | cap-01, línea 51 | «Jean reconoce el formulario.» (`cap-30:67`) |
| R-1189 | cap-30, línea 65 | «R-1189 acreditaba una revocación eficaz.» (`cap-35:49`) |
| Hvelv | cap-29, línea 71 | «El certificado conduce al proveedor de seguridad de la cadena de Kronfjord Kapital.» (`cap-29:93`) |
| Kronfjord | cap-29, línea 71 | «Conservaré el expediente de contratación del fondo y después consultaré su alcance.» (`cap-29:107`) |
| TKS | glosa de cap-22, línea 137 | «En 2054, un hombre llevó a la supervisión dos resoluciones de un mismo sistema certificado.» (`cap-26:173`) |

**La contrapropuesta de A2 no instaura esa práctica: le quita los anclajes.** Reduce el recuento de tokens y deja las perífrasis flotando sin el sitio donde el lector aprendió a qué se refieren. La densidad que incomoda al editor no viene de que los códigos se repitan: viene de que **hay veintiún nombres**. Quitarle tres ocurrencias a un nombre de siete no mueve esa cifra.

---

## 1 · Tabla de hallazgos

### H-1 · cap-30, líneas 65-69 — **VETO** · Carta 1 · R3 · §1 «Sugerir o reconstruir»

«Jean reconoce el formulario.» (`cap-30:67`) y «Lo presentó ella. Rechazó la sugerencia de añadir una causa.» (`cap-30:69`).

El token monoespaciado de la línea 65 no se sustituye. El bloque funciona porque el código llega opaco: primero el número, después el reconocimiento, después la memoria corporal de Jean, y **solo entonces** el sistema dice qué era, en las líneas 71 y 73. Nombrar el acto en la línea 65 pone esa memoria bajo un rótulo que nombra lo que ella hizo, deja «Jean reconoce el formulario.» sin antecedente y convierte la expansión del sistema en repetición. La línea 69 es el locus que R3 protege y es lo más cerca que este libro llega de sus últimos días.

### H-2 · cap-40 (261, 263, 305), cap-41 (185, 187, 245), cap-43 (137) — **VETO** · R7·5 · §1 definición de voz

`INC-441` es **7 de 7 en monoespaciado**. No hay una sola ocurrencia en prosa que colapsar: «6 de 7 colapsables» mide algo que no existe.

Y la sustitución pondría **tres referentes distintos** de «la incidencia» dentro de cap-40: la del coche de Gunnar en «Después de la incidencia del coche de Gunnar,» (`cap-40:15`); la genérica del protocolo en «asociaría su identidad, la incidencia, la hora y la puerta» (`cap-40:267`); y la de Tomas, que hoy solo existe con su código. Tomas es el único nombre presente en las dos primeras. **Fundir sus nombres es atribuir por nomenclatura lo que el auto deja en blanco.**

### H-3 · cap-01, líneas 51 y 69 — **VETO** · R9 · Carta 1 · fichero `proteccion: total`

Intocables. Además, A2 los cita como «cap-01:53»: la línea 53 es prosa sobre SPEIL. La lista de exclusiones se rompió antes de ejecutarse.

### H-4 · cap-18 línea 191 (`S15-r1189`) y **cap-43 línea 171 (`S37-acta`)** — **VETO** · R7·4 · hash de span

Hay **dos** spans con el código dentro, no uno. El segundo es `S37-acta`, el núcleo que contiene «No escribió *persona*. Tampoco *modelo*.» (`cap-43:195`). Nadie lo había contado. Y en esa misma frase la sustitución produciría una tautología, porque el texto ya dice «Fijaba la revocación eficaz y los permisos operativos durante la cola.» (`cap-43:171`).

### H-5 · cap-02 (123, 201), cap-30 (111), cap-33 (153, 163), cap-35 (49) — **corregir** · R3

«R-1189 seguía en cola.» (`cap-02:123`) · «R-1189 es la condición de procedencia de su candidatura.» (`cap-30:111`) · «R-1189 llevaba entonces más de cincuenta y tres horas vigente.» (`cap-33:153`) · «R-1189 acreditaba una revocación eficaz.» (`cap-35:49`).

En estas seis el código es **sujeto** de una predicación de vigencia, duración o consecuencia. Un número de expediente es inerte; «la revocación» con artículo es un acto de Jean que dura, que sigue en pie y que produce efectos. R3 prohíbe que la revocación del 24 de noviembre gane marcadores. Excluir las seis. La de cap-33 además cuenta horas sobre un intervalo que contiene el 26 de noviembre.

### H-6 · cap-45, líneas 107 y 117 — **corregir** · R7·5

«El paquete del vehículo de Gunnar documentaba un mecanismo probado que había usado una hoja de Hvelv dentro de la contratación de Kronfjord.» (`cap-45:107`) y «La jueza tuvo por acreditados el mecanismo deliberado, la cadena Hvelv–Kronfjord y el beneficio de Armstrong. El auto dejó en blanco al ejecutor y al ordenante individuales.» (`cap-45:117`).

La gramática de la escena es: **nombre propio para lo probado, nombre común para el hueco.** «El ejecutor» y «el ordenante» ya son nombres comunes con artículo. Si la cadena también lo es, desaparece la señal que distingue lo acreditado de lo no acreditado, y el auto pasa de «sabemos la cadena y aun así no podemos nombrar a la persona» a «no consta nada». Eso no resuelve la ambigüedad: **la disuelve, que es peor, porque invita al lector a rellenarla.** Los nombres se quedan.

### H-7 · cap-39 (135, 183, 217), cap-41 (27, 37, 47, 65, 71, 273) — **corregir** · R1 por acumulación · R4

«Si el fondo manda cortar, corto.» (`cap-39:183`) · «Si Aslak pierde fondo, él manda cortar.» (`cap-41:37`) · «la llevó al fondo de la barca» (`cap-41:273`).

«El fondo» ya es, en este libro, **el fondo del mar**, y lo es en los dos capítulos en que Maja y Jessie salen al agua — uno de ellos con literal protegido por R6. Generalizar «el fondo» como nombre de Kronfjord fabrica un homónimo entre el fondo que pagó el sabotaje y el fondo bajo la barca de las hijas. No lo enuncia nadie, y por eso no es R4 puro: es lo que §1 llama acumular. La instancia de cap-29 funciona porque es **una**. Denegada como perífrasis sistemática.

### H-8 · cap-26 (173), cap-45 (199), cap-28 (19), cap-35 (87) — **corregir** · R7·14 · R7·7 · R6 · R4

«En 2054, un hombre llevó a la supervisión dos resoluciones de un mismo sistema certificado.» (`cap-26:173`) · «El tribunal ordenó preparar una ventana supervisada de audio y texto para futuras visitas» (`cap-45:199`) · «Dos firmas y una hora autorizaban una sesión supervisada en un canal educativo aislado.» (`cap-28:19`) · «la ley de la TKS no sostenía la pretensión sobre las ejecuciones» (`cap-35:87`).

Tres cosas a la vez.

**(a)** «La supervisión» ya existe, **una vez**, y es el locus del hombre de 2054, que R7·14 protege. Después de la pasada, cap-26 diría «la supervisión» seis veces y el locus protegido perdería su singularidad.
**(b)** `supervis-` es en este libro el lexema de **la ventana supervisada del locutorio** y de **la sesión supervisada de una menor**. Hacerlo además el nombre corriente del órgano tiende un puente léxico entre quien no protege y el canal por el que una hija se encuentra con lo que puede ser su madre.
**(c)** «La ley de la supervisión» no dice lo que dice «la ley de la TKS».

Denegada.

### H-9 · cap-35, líneas 43 y 219 — **corregir** · oficio

«Astrid cogió la carpeta y entró en la TKS.» (`cap-35:43`) y «Astrid volvió a la TKS.» (`cap-35:219`). Aquí es un edificio. Ningún nombre abstracto entra ni se vuelve a él.

### H-10 · cap-35, líneas 55, 67, 73 y 87 — **corregir** · §5·5 · R7·4

«Prohibir todo el mantenimiento impondría un coste cierto frente a un daño que la TKS no puede individualizar.» (`cap-35:67`).

«La inspectora» queda **denegada** como sustituto del órgano. Convierte una institución en una persona: el fallo de cap-35 deja de ser institucional y pasa a ser de Astrid, y esa frase sería el décimo gesto de abstención suyo. «Una décima convierte una ética en un tic.»

### H-11 · `biblia/b7-perimetro.md`, línea 26 — **corregir** · §1 definición · §2

«las actas, autos y resoluciones (Astrid, la jueza, la TKS)».

A0 tiene razón y el problema es peor de lo que parece: la definición que hace aplicable la Carta está anclada a una **sigla**, es decir, al único tipo de dirección que una pasada de nomenclatura puede retirar. Si `TKS` cae a dos ocurrencias, quien grepee «TKS» concluirá que el inventario de voces con autoridad es pequeño. Fallo a la baja y en silencio, otra vez, y esta vez dentro del vinculante. Reescritura obligatoria en §3.

### H-12 · `herramientas/lib/verificar_b7.py` — **vigilar** · §2 · método

Su salida dice «b7-perimetro.md · 77 citas · OK 19 (+5 débiles) · MOVIDA 0 · PERDIDA 0 · sin literal 53». Es cierta y **no significa verificado**: 53 de 77 citas de b7 no llevan literal y el script no las comprueba. Entre ellas está la de cap-30 línea 69, el locus de la revocación del 24 de noviembre (H-1). Una pasada sobre cap-30, cap-33, cap-43 o cap-45 sería invisible para el único instrumento que guarda b7. El script lo enumera; el resumen que me llegó, no.

### H-13 · `biblia/b7-patrones-B.txt`, línea 5 — **vigilar** · Carta 1

El patrón de nivel B incluye `\bhoja\b`. Retirar `Hvelv` deja las frases apoyadas en «la hoja» sola, que es token vigilado. Correr `herramientas/sensibilidad.sh` después de cualquier pasada y comparar con la baseline.

### H-14 · `herramientas/lib/verificar_b7.py`, emparejamiento — **vigilar** · instrumento

Hallazgo lateral de escribir este informe. El script empareja una referencia con su literal buscando `»` en los catorce caracteres **anteriores** antes de mirar los posteriores. Consecuencia: en una enumeración escrita al revés del orden canónico —`` `ref` («literal») ``, repetida— **cada referencia roba el literal de la anterior**, y el script declara PERDIDA sobre citas exactas. Lo reproduje seis veces con la primera versión de este documento y lo verifiqué a mano: las veintinueve citas eran correctas. Hoy es latente, porque b7 usa el orden canónico en todas partes. Deja de serlo el día que alguien escriba una tabla. No pido cambiarlo: pido que conste, y por eso este documento usa el orden canónico.

---

## 2 · Las cuatro respuestas

### 1 · ¿`TKS` puede pasar a «la supervisión» en la prosa?

**Perder ocurrencias de `TKS`: sí. Llamarlas «la supervisión»: no. Llamarlas «la inspectora»: no.**

`TKS` es 17 de 17 en prosa, no aparece en ningún span, no es literal protegido en ningún capítulo y no es rótulo de sistema. Como término es el más disponible de los cinco. **La perífrasis propuesta es el problema, no la sustitución.** Razones en H-8, H-9 y H-10.

**Restricción, en negativo y sin ejemplo** (§8f: un ejemplo dentro de una condición se lee como parte de la condición). Toda perífrasis candidata cumple las cuatro:

1. **No comparte lexema** con `supervis-`, `vigil-`, `control-` ni con ningún término que el libro aplique ya a un canal por el que pase una menor.
2. **No es ya la designación de otra cosa.** Comprobación mecánica: `grep` del candidato en `capitulos/` antes de decidir. Si sale con ocurrencias, se descarta, o se cuenta qué se les quita a esas.
3. **No es una persona.** El órgano falla como órgano.
4. **Sobrevive a la sustitución escrita en estos cuatro literales**, y la prueba es escribirlos: «Astrid cogió la carpeta y entró en la TKS.» (`cap-35:43`), «Astrid volvió a la TKS.» (`cap-35:219`), «la ley de la TKS no sostenía la pretensión sobre las ejecuciones» (`cap-35:87`) y «El hombre miró la insignia de la TKS en su chaqueta y se apartó.» (`cap-40:233`). Si alguno queda raro, el candidato está mal. Los cuatro conservan el nombre propio en cualquier caso.

Techo: **cap-22 línea 137 conserva la glosa íntegra** y cap-26 línea 213 conserva la sigla, porque ahí la institución se nombra a sí misma.

### 1b · ¿Hay que reescribir `b7:26`?

**Sí, y no basta con la glosa única.** Pero la reescritura correcta **no** es cambiar «la TKS» por la perífrasis nueva: eso reproduce el fallo un escalón más allá. La definición tiene que dejar de depender de cómo se llame nada.

**Texto de sustitución para el primer guion de `b7-perimetro.md` §1:**

> - **Voz con autoridad narrativa** = el narrador en cualquier persona, incluida la primera de `cap-44`; **toda acta, auto, resolución o consignación de un órgano** —la inspectora, la jueza y la autoridad de supervisión de sistemas cognitivos, se las nombre por sigla, por perífrasis o por su nombre completo—; **todo texto en monoespaciado**, que en este libro es la salida de un sistema presentada como hecho (EDDA, consolas, sellos, acuses, auditados); la profesional de apoyo de `cap-11`; y el autor en los paratextos. Un personaje en diálogo puede decir lo que la rabia le dicte —Jessie: «Mamá se mató»; Maja: «Jean ya pagó tu forma de protegerla»— y el narrador ni lo ratifica ni lo desmiente. Esa asimetría es el motor moral del libro entero.

**Y una definición tercera, que faltaba y aparece por esta consulta.** Entra como §8g:

> **A7-W11-C1 · El monoespaciado es una frontera de voz, no un adorno.** Un sistema no dice «la incidencia» ni «la revocación»: emite un identificador. **Todo token en monoespaciado es voz del sistema y, por tanto, voz con autoridad narrativa.** Ninguna pasada de estilo, nomenclatura, poda o traducción convierte un token monoespaciado en prosa corriente, ni prosa corriente en token. Mover un término a través de esa frontera cambia quién habla, y quién habla es materia de Carta, no de estilo. **La frontera se verifica con una expresión regular y no envejece.**

A7-W11-C1 entra en `b7-perimetro.md` **ocurra o no la pasada**, porque no depende de ella. La reescritura de §1 entra **en el mismo commit** que el primer cambio de prosa que reduzca `TKS`; no en el siguiente, no en un informe. Ese es el modo de fallo de P-41 y no lo repito.

### 2 · `R-1189`: el criterio, no la lista

Tres pruebas, en orden. El resultado no es 15 de 21: es **7**.

**Prueba 1 — tipográfica. Mecánica, y no envejece.** *Donde el token va en monoespaciado, se queda.* Es la salida de un sistema, y un sistema no parafrasea (A7-W11-C1). Son **8**: cap-01 (51, 69), cap-18 (191), cap-30 (65, 181), cap-33 (145), cap-43 (171), cap-45 (17). Se comprueba con una regex, no con una lista.

**Prueba 2 — gramatical, sobre las 13 de prosa.** *El código se queda donde el nombre común sería sujeto de una predicación de vigencia, duración, fuerza o consecuencia; puede ceder donde el expediente es objeto del procedimiento de otro.* Como objeto, «la revocación» nombra un papel que alguien maneja; como sujeto, nombra **un acto de Jean que sigue en pie y produce efectos**, y R3 prohíbe que la revocación del 24 de noviembre gane marcadores. Se quedan **6**: las de H-5.

**Prueba 3 — de protección. Absoluta.** Nada dentro de fichero `total` ni dentro de span con hash. Añade cap-43 línea 171 (`S37-acta`), que no estaba en ninguna lista.

**Quedan disponibles siete:** cap-30 (127, 175, 183, 211), cap-33 (207), cap-35 (89, 179). Cuatro están en cap-30, que es donde R3 tiene su locus: **si se ejecutan, no se ejecutan las cuatro**, y ninguna cae en la misma sección que el bloque de H-1.

El criterio que A0 propone —«el código vive donde el documento se cita como documento»— es correcto en el sentido y **no es operable**: en cap-43 línea 171 y cap-45 línea 17 el expediente aparece en un terminal, que es y no es citarse como documento. La prueba tipográfica resuelve esos dos sin discusión y sin depender del juicio de quien ejecute.

### 3 · `Hvelv` y `Kronfjord`: sí, debilita, y sé dónde

**Sí.** Detalle en H-6. La acreditación de cap-45 está construida con precisión nominal máxima **alrededor de dos huecos**: una hoja, un contratante, una instrucción, un centro de coste, un cliente — y después «—¿Quién dio la instrucción? —preguntó la jueza.» (`cap-45:109`) y «Nadie contestó.» (`cap-45:111`). Los dos huecos se leen como huecos porque todo lo que los rodea tiene nombre. Lo mismo hace, dos réplicas después, «No puedo acreditar su origen» (`cap-45:115`).

**Criterio:** *los nombres propios viven donde la cadena se acredita; la perífrasis vive donde alguien se refiere a ella.* Acreditan cuatro loci: cap-29 línea 71 (donde se establece), cap-35 línea 37 (donde «la incidencia Hvelv» es la designación propia del expediente) y cap-45 líneas 107 y 117. El resto puede parafrasearse, **y el libro ya lo hace**: «Solo compartían la autoridad intermedia del proveedor de seguridad y la cadena contractual de Kronfjord Kapital.» (`cap-40:21`), más las dos de cap-29 citadas en §0.

**Y una recomendación que no lleva veto.** `Hvelv` tiene **siete** ocurrencias y cuatro son estructurales: el neto son tres. No merece el riesgo, y el editor no se quejaba de `Hvelv` — se quejaba de que hay veintiún nombres. Sobre `Kronfjord`: siete de sus dieciocho están en el consejo de cap-13, donde identifican a los dos únicos consejeros que el libro nombra por su empleador, que es como sabe el lector que el dinero está en la sala. Ese capítulo está además bajo condición permanente (§8b·W9-21). Si se toca, se toca con A5 delante.

### 4 · Dramatis personae: **denegado**

No por el motivo de A0, que es bueno y no es el que ata. Los que atan son tres:

1. **§6, pregunta 1.** «¿Qué punto de la Carta mejora esta página?» Ninguno: responde a un editor. Cuando la respuesta es ésa, la respuesta es no, y no hay cuarta pregunta ni apelación a un experto ausente.
2. **Es voz con autoridad narrativa obligada a clasificar.** Un reparto tiene que decir qué es cada entrada. Tiene que describir a Jean Marie Larsson en una línea firmada por el autor —la frase de mayor riesgo que este libro podría contener— y tiene que **separar personas de no-personas** para ordenar a `JM-L/0000`, AK-7, Madre, Nieve, Coro, NORNA y Cuchillo. Esa separación es exactamente la pregunta que R7·4 deja abierta para siempre, y «No toda» es el techo. Ya lo dictaminé para el índice en §8f·A7-it4-C8, punto 2: **no se responde desde la tabla de contenidos.** Un reparto es el índice de las personas: el argumento vale más allí, no menos.
3. **R9.** El aviso es la promesa, va solo, antes del capítulo 1, y no comparte página con ninguna nota de autor. Un aparato nuevo entre el aviso y el primer capítulo interpone algo entre la promesa y el libro.

**No propongo sustituto**, y es deliberado: en el dictamen del título puse tres títulos vivos como ejemplo de registro y A0 leyó uno como propuesta. Cuando restrinjo, restrinjo en negativo. Si alguien quiere aparato de apoyo, pasa por las tres preguntas de §6 **por escrito y antes de redactar una línea**, y la primera ya está contestada arriba.

---

## 3 · Condiciones obligatorias antes de cualquier merge de nomenclatura

1. **A7-W11-C1** (texto en §2·1b) entra en `b7-perimetro.md` como §8g. Independiente de la pasada.
2. **Reescritura de la definición de voz con autoridad** (texto en §2·1b) en `b7-perimetro.md` §1, **en el mismo commit** que el primer cambio de prosa que reduzca `TKS`. `biblia/b7-carta-sensibilidad.md` no se toca: su cabecera ya lo declara registro histórico y no norma vigente.
3. **A7-W11-C2 · La cadena se acredita con nombres propios.** Ni `Hvelv` ni `Kronfjord` pierden el nombre en los cuatro loci de acreditación (§2·3). Rige para toda oleada futura y rige aunque alguien vuelva a contar tokens: el auto que deja al ordenante en blanco necesita que lo probado tenga nombre.
4. **A7-W11-C3 · Test de homonimia.** Ninguna perífrasis sustituye sistemáticamente a un nombre propio sin `grep` previo del candidato en `capitulos/`. Si ya existe, o comparte lexema con un canal por el que pasa una menor, o con el mar, o con un locus protegido, se descarta. Vale para «el fondo», para «la supervisión» y para lo que venga.
5. **A7-W11-C4 · Ningún paratexto nuevo antes del capítulo 1.** El aviso va solo.
6. **Nada se ejecuta con `sed`.** Los cinco términos suman 70 ocurrencias y los veintiún nombres, 372. Se editan a mano, locus a locus, con la prueba tipográfica delante.
7. **Antes de tocar cap-30, cap-33, cap-43 o cap-45: darles literal a las citas de b7 que apuntan a ellos** (H-12), empezando por la de cap-30 línea 69. Si no, el cambio es invisible para el único guardián de b7.
8. **Después:** `verificar_b7`, `proteger.sh verificar`, `sensibilidad.sh` contra baseline y A5. Y `biblia/b3-canon-sistema.md` y `b3-lexicon.json` en el mismo commit, como ya advierte A2.

---

## 4 · Veredicto

**APROBADO CON CORRECCIONES**, con dos vetos parciales dentro.

- **`TKS`** — la reducción de ocurrencias se aprueba. **«La supervisión» y «la inspectora» quedan denegadas** como perífrasis. Cuatro loci conservan el nombre propio (cap-22:137, cap-26:213, cap-35:43, cap-35:219) y dos más hay que escribirlos con el candidato delante antes de decidir (cap-35:87, cap-40:233). Máximo real: **11 de 17**, no 16.
- **`R-1189`** — **VETO** sobre cap-01 (51, 69), cap-18 (191), cap-30 (65, 181), cap-33 (145), cap-43 (171) y cap-45 (17). Aprobadas **siete**, no quince. La de cap-30 línea 65 es veto de Carta, no de oficio.
- **`INC-441`** — **VETO íntegro.** Cero loci disponibles. El item se retira de la orden.
- **`Hvelv` / `Kronfjord`** — aprobado solo fuera de los cuatro loci de acreditación; **«el fondo» denegado** como perífrasis sistemática; `Hvelv` no compensa; cap-13 no se toca sin A5.
- **Dramatis personae** — **DENEGADO.** Sin sustituto y sin apelación en el mérito.

**Balance de la operación tal como estaba escrita:** de las ≈40 ocurrencias que prometía quedan **como mucho 18**, y ninguna de ellas mejora un punto de la Carta. No lo digo para bloquearla. Lo digo porque si el objetivo era aliviar al lector de veintiún nombres, dieciocho tokens no lo consiguen y el trabajo está en otro sitio. **Eso no es mío y no lo decido yo.** Lo mío es que ninguno de esos dieciocho salga de donde no puede salir.

---

**Firmado, A7 · 2026-08-20 · sobre `capitulos/` en `main`, 48 capítulos.**

*Nota de método. Esta consulta encontró tres cosas que ninguna lista tenía: un span con el código dentro que nadie había contado (`S37-acta`), un término que era 7 de 7 monoespaciado cuando la orden lo daba por 6 de 7 colapsable, y una frontera de voz —el monoespaciado— que llevaba cuarenta y ocho capítulos funcionando sin estar escrita en ninguna parte. Las tres aparecieron por resolver los spans y contar los backticks, no por leer la propuesta. A0 tenía razón en pedir criterio y no lista. El criterio que faltaba estaba en la tipografía, que es lo único de este proyecto que no ha cambiado de esquema cinco veces.*
