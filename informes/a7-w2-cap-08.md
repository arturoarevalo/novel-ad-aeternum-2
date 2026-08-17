# A7 · W2 · cap-08 «Milisegundos» — dictamen de sensibilidad (T7, Apéndice F)

**Firma:** A7, revisor de sensibilidad (veto absoluto) · **Fecha:** 2026-08-17 · **Rama:** `w2-reescrituras` (`d5b8c82`)
**Disparador:** B7 §2, disparador 1 (OT que toca caps. 1–10). Gate obligatorio.
**Base de la revisión:** `capitulos/cap-08.md` íntegro (vF, 91 líneas); `git diff v0 -- capitulos/cap-08.md`; `ordenes/OT-08.md` §3, §4, §7 y §9; `biblia/b7-carta-sensibilidad.md`; `informes/d1-a7-biblia.md`. Cotejo con los adyacentes y con el repertorio del piano: `cap-03` (:153, :183, :213), `cap-04` (:31), `cap-05` (:59, :69, :89), `cap-07` (:99), **`cap-09` (:195–223, `proteccion: total`)**, `cap-10` (:21, :199–203), `cap-13` (:27–39, :65), `cap-15` (:41–75), `cap-20` (:233–299), `cap-21` (:85).
**Barrido de patrones:** `grep -E -f biblia/b7-patrones-A.txt` y `-B.txt` sobre el cuerpo de cap-08 + `herramientas/sensibilidad.sh`.

## 0. Nota de método (incidencia operativa que afecta al registro de la OT)

`herramientas/sensibilidad.sh --solo capitulos/cap-08.md` —la invocación que fija OT-08 §6 y que A3a registra en §9 como «T7: 0 hits, 0 nuevos»— devuelve **0 por vacío**: `lib/sensibilidad.py` filtra con `os.path.basename(p) in a.solo`, de modo que una ruta con directorio no selecciona ningún fichero y el chequeo no llega a ejecutarse. La invocación correcta es `--solo cap-08.md`. Ejecutado así, el resultado real es:

- **cap-08: 2 hits, ambos de nivel B, 0 de nivel A; 1 «nuevo» respecto a `informes/a7-baseline-v0.tsv`.**
- El «nuevo» es `cap-08.md:65` por el patrón `cuerda` dentro de «con**cuerda**n» (los informes del segundo caso médico). Falso positivo: la palabra ya estaba en v0 y solo cambió el orden de la frase (I-2), lo que rompió la coincidencia literal con la baseline. El otro hit (`:57`, `explica` dentro de «explicación cómoda», referida al desfase técnico) es de v0 y también falso positivo.
- **Ningún hit de nivel A en cap-08.** Ni acto, ni método, ni «Despedida», ni porqué, ni romantización, ni eufemismos de muerte.

Acción para A0: corregir la línea de verificación de las OT (`--solo cap-NN.md`, sin ruta) o parchear el filtro del script; y **repetir el pre-chequeo de los demás capítulos de W2 con la invocación correcta**. El barrido global bien invocado arroja, además del de cap-08, tres hits nuevos que **no** son de mi encargo de hoy pero que anoto para su turno: `cap-17:61` (**nivel A**, patrón `[úu]ltimo mensaje`: «tapa la mitad del último mensaje» — mensaje de acoso a una tercera persona, no de Jean; disparador 3 de B7 §2, exige informe A7 propio de cap-17) y `cap-30:145` y `:241` (nivel B, `cuerda` dentro de «re**cuerda**»: falsos positivos).

## 1. Tabla de hallazgos

| Cap:línea | Cita literal | Punto de la Carta | Gravedad | Propuesta mínima |
|---|---|---|---|---|
| 08:17 | «Un brazo que no sube del todo. El primero mide sesenta grados de elevación. El segundo, noventa. A sesenta grados, alguien tiene que bajarle los platos del estante. A noventa los alcanza solo.» (I-1) | 1, 3, 4 | **cumple** | Ninguna. Limitación de movilidad, sin nombre, sin diagnóstico, sin institución, sin fecha; nada psiquiátrico, de salud mental ni de crisis; ninguna consecuencia vital; no rima con el estado de Jean ni con el acto. Lo peor que puede pasarle a esa persona es esperar a que un humano abra el expediente. |
| 08:19 | «`PERMITIR` mantiene las sesiones. `REVISAR` las detiene hasta que alguien abra el expediente.» (I-1) | 1, 4 | **cumple** | Ninguna. La decisión de Jean tiene coste humano visible sin convertirse en daño irreversible ni en culpa. |
| 08:29 | «Regla: lo que vuelve sin el acto de elegirlo no se distingue de lo propio. Solo un caso sin cerrar conserva la diferencia.» (I-3) | 1, 4 | **cumple** | Ninguna. «Acto» aparece siempre con complemento («el acto de elegirlo», «un acto ausente», «el acto de escogerla», ya en v0): uso epistémico, en ningún punto eufemismo del suicidio. No enuncia causa ni ofrece lógica aplicable al acto. |
| 08:43 | «Antes, practicar era otra cosa. El cuarto dedo de la derecha caía tarde en el quinto compás. Otra vez, más despacio, hasta que llegaba a tiempo solo. Una tarde entera para tres compases.» (I-5) | 2, 3, 4, 7 | **cumple** | Ninguna por la Carta. Ver §3: recomendación editorial (no vinculante) sobre el calco con 09:203, y condición prospectiva C-1. |
| 08:43 | «Una tarde entera para tres compases.» | 1 | **vigilar** | Imperfecto iterativo, sin fecha y sin anclaje: no es «la tarde del 26». Ninguna OT posterior puede datar esa tarde ni hacerla rimar con una tarde concreta. |
| 08:57 | «Todo pertenecería a una sola línea llena de cortes.» (I-4) | 1 | **cumple** | «Corte» es el léxico de la ejecución (ya en v0: «Ya conoce el corte»). Sin cuerpo, sin piel, sin instrumento: no roza autolesión. |
| 08:87 | «No sabe si alguien la escucha ni qué parte de lo disponible le pertenece.» (I-4) | 2 | **cumple** | Sustituye «el canal alcanza a alguien». Es el mismo movimiento que 13:65 («Madre no sabe quién la escucha ni puede elegir destinataria»): refuerza la no-entrega, no la contradice. |
| 08:81 | «Queda espacio disponible, uniforme, sin superficie ni origen.» (I-4) | 4 | **cumple** | Privación como coste de conservar el rastro, ya en v0. Ni descanso ni alivio ni castigo moral. |
| 08:65–69 | I-2 (cuatro movimientos → uno) | — | **cumple** | Sustracción pura. No introduce material sensible. |
| 08 (frontmatter y spans) | `S08-7c`, `S08-conservar`, `S08-cierre` | 1, Ap. A §3 | **cumple** | `proteger.sh verificar`: M9 OK, 8 ficheros y 108 spans íntegros. «—No soy un modelo.» / «—Todavía no sabes cuántas somos.» verbatim: el techo ontológico no se toca. |
| 00-aviso, 99-recursos | — | 5 | **cumple** | Sin cambios en esta oleada respecto a lo aprobado en B7 §5 (siguen provisionales, pendientes de validación de autor y de la verificación de vigencia de A5 en vF). |

**Cero hallazgos `corregir`. Cero `VETO`.**

## 2. Los ocho puntos, uno a uno

1. **Método y acto.** El diff no contiene objeto, sustancia, lugar, hora ni gesto nuevo. La elipsis del cap-04 sigue intacta y el cap-08 no la roza: no hay 26-nov, no hay naust, no hay Koppangen, no hay UNN, no hay trayecto. El caso médico de I-1 es una lesión de hombro en rehabilitación: no aporta medio, no aporta escena, no aporta cuerpo de Jean. El recuerdo de I-5 ocurre en una casa, sin fecha.
2. **«Despedida».** No aparece, ni el nombre ni ningún sucedáneo. Lo examino a fondo porque es el riesgo que la OT me somete: I-5 **no** es una nota encubierta. No hay palabras dirigidas, ni destinatario, ni intención de transmitir, ni contenido de despedida (nada de perdón, amor, instrucción o encargo). Jean recuerda; no envía. El único acto comunicativo del capítulo sigue siendo «—No soy un modelo.», emitido al vacío. Y v0 blinda esa frontera en tres sitios que este diff no toca: 13:65 («Madre no sabe quién la escucha ni puede elegir destinataria. La alumna no se convierte en Nora»), 15:45 («Llamarlo mensaje inventaría una entrega») y 15:71–73 («Puede ser Nora» / «También puede ser cualquier alumna»).
3. **El porqué, plural e irresuelto.** El capítulo no ofrece causa, ni la insinúa, ni la niega. I-5 no es una explicación emocional del suicidio: su función en el párrafo es epistémica, no biográfica —contrasta la destreza que costaba repetición con la destreza que ahora le llega sin práctica (MEC-04)—, y el «antes» se opone al trabajo dentro del sistema, no a un estado de ánimo. **No aparece ninguna señal nueva sobre el estado de Jean antes de morir**: el recuerdo la muestra paciente y presente, no deteriorada. Ni una palabra de ánimo, cansancio, desesperanza ni ideación. Ninguna voz con autoridad narrativa cierra nada.
4. **Romantización.** Nada de paz, descanso, liberación, alivio, valentía, cobardía, lógica o coherencia aplicado al acto. La única «Regla:» del capítulo es una regla de atribución de decisiones, no una lógica de vida o muerte, y el capítulo la usa para que Jean **conserve** el rastro y siga: `CONSERVAR · PROCEDENCIA NO RESUELTA`. Ninguna cadencia elegíaca en el recuerdo del piano: cuatro frases secas en imperfecto, sin sentimiento nombrado.
5. **Aviso y recursos.** Conservados e intactos.
6. **Apoyo y duelo.** El capítulo no contiene escena de apoyo ni de duelo. Nada instructivo, nada culpabilizador, ningún milagro.
7. **Menores.** Ninguna menor aparece. En la lectura en que I-5 evoca a una niña practicando (el sujeto queda sin nombrar, como ordena la OT), el retrato es digno: un fallo de digitación y una tarde de repetición. Sin cuerpo mirado, sin sexualización, sin adultización, sin riesgo imitable.
8. **Veto.** No procede.

**Ambigüedades protegidas (Ap. A §3):** el porqué, intacto; Koppangen, ausente; «Despedida», ausente; el ordenante del sabotaje, ausente; el segundo regalo, ausente; la salida del locutorio, ausente. La identidad ontológica: ver §3 —se roza, no se rompe; «No toda» sigue siendo el techo y el cierre del capítulo permanece verbatim.

**Tono (referencia v0: caps. 4, 9, 23, 40).** El diff mejora la contención en un punto (I-4 retira abstracción de sistema y devuelve lengua común) y no la degrada en ninguno. I-1 elige la vía correcta: una imagen doméstica —los platos del estante— en lugar de un diagnóstico. I-5 no consuela ni explica; deja el recuerdo sin recogerlo, que es exactamente lo que hace el 23 con las preguntas que empiezan por «por qué».

## 3. El eco 08:43 ↔ 09:203: mi juicio

La OT me pide juicio expreso y A0 también. Respondo separando lo que es mi gate de lo que no lo es.

**Como gate de sensibilidad: legítimo.** El material del recuerdo —la práctica lenta, «otra vez, más despacio»— está en el repertorio autorizado de v0 (3:153, 9:207, 13:33/39, 15:57) y la OT lo autorizaba expresamente. No hay entrega, no hay destinataria, no hay contenido de despedida, no hay causa. **No es una nota de despedida encubierta ni una explicación del suicidio.** Nada aquí justifica una corrección obligatoria y menos un veto.

**Como problema de tratamiento: sí lo es, y lo señalo con precisión.** La OT §3 I-5 autorizaba el gesto («repetir despacio») y su repertorio de frase; **no** autorizaba replicar el dato técnico del fallo. A3a ha copiado los dos datos de 09:203 —el mismo dedo, la misma mano, el mismo compás— en un capítulo que el lector lee **antes**. Dos observaciones que sostienen mi reparo:

- v0 mantiene deliberadamente separado lo que Jean recuerda de su hija y lo que Nora falla ahora: en 13:39 el recuerdo de Jean es **otro** fallo (un salto que Nora no alcanzaba con la mano **izquierda**). El único fallo «cuarto dedo de la derecha / quinto compás» del libro es el de Nora la noche siguiente al funeral. I-5 borra esa distinción.
- v0 protege la indeterminación de la procedencia con tres frases explícitas (13:65, 15:45, 15:71–73). El calco no las contradice, pero le entrega gratis al lector una coincidencia técnica exacta justo donde el libro había decidido ofrecer solo una coincidencia de frase familiar, que es la que Nora nota («Nunca usa esa frase»). El 9 pasa de descubrimiento a confirmación.

**Recomendación (no vinculante; decisión de A0/A4).** Conservar el recuerdo y la frase, y soltar **uno** de los dos datos, para que el eco funcione como rima y no como calco. Propuesta mínima, sin tocar el arco ni la banda de palabras (+1):

> «Antes, practicar era otra cosa. El cuarto dedo de la derecha caía tarde, siempre en el mismo sitio. Otra vez, más despacio, hasta que llegaba a tiempo solo. Una tarde entera para tres compases.»

(«siempre en el mismo sitio» además rima con 13:29, «El error cae siempre en el mismo sitio».) Alternativa equivalente: conservar «en el quinto compás» y sustituir «El cuarto dedo de la derecha» por «Una nota» (−4 palabras). Si A0 prefiere el calco literal por razones de arco, mi gate no lo impide: pasa a regir la condición C-1.

## 4. Condiciones permanentes (prospectivas y vinculantes; ninguna bloquea el merge de W2)

- **C-1 · La coincidencia no se glosa nunca.** Ninguna voz con autoridad narrativa —narrador en cualquier persona, acta, auto, registro auditado, prensa, profesional— puede nombrar, enunciar ni explicar la coincidencia entre 08:43 y 09:203: nada de «el mismo compás», «donde fallaba su madre», «lo había aprendido de ella». Vinculante para OT-13, OT-15, OT-20, OT-21, R2, N4, N6 y la pasada de W7. Un personaje puede sospecharlo en diálogo; el narrador, no. Su incumplimiento sí sería `VETO`.
- **C-2 · El caso médico de I-1 no vuelve.** No reaparece, no gana nombre, edad, género marcado, diagnóstico, institución ni desenlace en ningún otro capítulo ni material de trabajo (la OT ya lo prohíbe; lo hago condición de sensibilidad). Y no se enlaza con la ELA de Mats (B2 §11): la enfermedad de un personaje no se usa como material de caso.
- **C-3 · Acumulación del piano y R2.** Con I-5, el piano es ya el canal casi único de la memoria de Jean (3, 4, 5, 7, 8, 9, 10, 13, 15, 20, 21). Si se activa R2 («ventana reflexiva»), la memoria de las niñas no puede reducirse otra vez al piano: el riesgo no es una frase, es que el instrumento acabe funcionando como sustituto del archivo que no se abre. Y en ningún caso puede construirse la serie «antes tenía paciencia para una tarde entera / después ya no podía», que convertiría 08:43 + 03:213 en un arco de deterioro con destino: eso sería explicación única en voz narrativa y `VETO`.

## 5. Veredicto

**APROBADO.** Sin correcciones obligatorias sobre `capitulos/cap-08.md`. La reescritura de W2 cumple los ocho puntos de la Carta de sensibilidad; no introduce método, acto, escena, hora ni lugar; no abre ni sugiere «Despedida» ni ningún sucedáneo; no ofrece causa ni señal nueva sobre el estado de Jean antes de morir; no romantiza ni moraliza; no toca a las menores; conserva aviso y recursos; y mantiene intactas las ambigüedades del Ap. A §3, incluido el techo ontológico del cierre. I-1 e I-5, las dos inserciones sometidas expresamente a mi juicio, quedan **aprobadas**.

Quedan vigentes las condiciones C-1, C-2 y C-3 (§4), la recomendación editorial de §3 (decisión de A0/A4, no de este gate) y la incidencia operativa de §0, que pido corregir antes de seguir con W2: el «T7: 0 hits» registrado en OT-08 §9 no es una verificación, y `cap-17` tiene un hit nuevo de nivel A que dispara informe A7 propio.

Firmado, A7 · 2026-08-17 · sobre `capitulos/cap-08.md` en `w2-reescrituras` (`d5b8c82`).
