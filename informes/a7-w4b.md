# A7 · W4 (segunda tanda) · caps. 2, 7, 10, 11, 12, 15, 18, 19, 25 (+ coda R2), 37 y 38 — dictamen de sensibilidad

**Firma:** A7, revisor de sensibilidad (veto absoluto; §2.1 y Apéndice F del plan) · **Fecha:** 2026-08-18 · **Rama:** `w4-familia` (`3219a70` familia/mundo · `0976f64` capítulos de Jean + coda R2)
**Disparadores (B7 §2):** **1** (OT que tocan caps. 1–10: cap-02, cap-07, cap-10; y cap-38), **2** (inserciones que rozan el 26-nov / R-1189 / el Corpus: cap-11, cap-25), **4/9** (inserciones `INTERIORIDAD` de Jean y de Alana en el perímetro: cap-02, cap-11, cap-19, cap-25, cap-38), **5** (prensa y voces públicas: cap-37). Gate obligatorio: **sin este informe no hay merge de la tanda.**
**Base de la revisión:** el diff íntegro `git diff 59a005e..HEAD` de los once ficheros (**235 líneas añadidas**, 1.564 palabras nuevas netas), leído contra el texto vigente completo de los capítulos disparadores (**2, 7, 10, 25, 37, 38**) y contra el entorno inmediato en los demás. Cotejo de perímetro y continuidad: **cap-01:15-85** (la última sesión, R-1189, «apagó la luz con la mano»); **cap-02:107-125, 201-225** (cribado, alerta de salud laboral, `S02-despedida`); **cap-03:75** (reunión de las nueve y media); **cap-04:99-121**; **cap-07:31-33, 83-99, 221-229**; **cap-10:41, 143**; **cap-11:85-135** (`S11-flashback`), **:307**; **cap-15:95-135, 139-185**; **cap-18:99-105, 139-167**; **cap-19:59-61, 123-155, 191-197**; **cap-25:85-107** (`S25-utilidad`, `S25-escalada`); **cap-37:195-215**; **cap-38:137-215**; `biblia/b7-carta-sensibilidad.md`; `biblia/b3-canon-sistema.md` §12; `biblia/b5-lista-protegida.md`; `biblia/b1-cronologia.md` (lun 29-nov); `ordenes/OT-11.md`, `OT-19.md`, `OT-25.md`, `OT-25b.md`, `RESERVA.md` §R2; `informes/a7-w4a.md` (**C-1 a C-4**, **P-12 a P-20**).
**Barrido:** `grep -n -i -E -f biblia/b7-patrones-A.txt` y `-f biblia/b7-patrones-B.txt` **sobre el conjunto de las 235 líneas añadidas**, más barrido dirigido de 38 expresiones (deixis temporal hacia el acto, marcadores de nota, léxico de culpa y de descanso), más `herramientas/sensibilidad.sh` y `herramientas/proteger.sh verificar`.

---

# 0 · Pre-chequeo

## 0.1 · Los números

| Medida sobre las 235 líneas añadidas | Resultado |
|---|---|
| Hits de **nivel A** (acto, método, medio, «Despedida», causa, culpa, romantización, eufemismos, hallazgo, últimas horas) | **0** |
| Hits de **nivel B** (objetos y lugares, marcadores de nota, duelo instructivo, menores: cuerpo y riesgo) | **0** |
| Apariciones nuevas de `Despedida`, `atestado`, `efectos personales`, `forense`, `autopsia`, `cadáver`, `Koppangen`, `naust`, `barca`, `UNN`, `26 de noviembre`, `27 de noviembre` | **0** |
| Deixis temporal hacia el acto (`aquella noche`, `aquel día`, `aquella tarde`, `la última vez`, `antes de morir`, `en vida`) | **0** |
| Léxico de culpa, deuda o contrafáctico (`culpa`, `si hubiera`, `podría haber`, `debería`, `merec-`, `castigo`) | **0** |

Confirmo el pre-chequeo de A0: **T7 = 0 hits nuevos** (60 totales, 20 A / 40 B, todos de v0). Esta vez T7 y mi criterio inmune coinciden, porque el barrido sobre líneas añadidas también da 0. Reitero, no bloqueante, la petición de W4a §0.3: `sensibilidad.py` sigue comparando tuplas *(fichero, línea, patrón)* contra la baseline y sigue siendo vulnerable al desplazamiento de líneas; falta el modo `--diff <base>` que pedí. Con 235 líneas nuevas repartidas en once ficheros ha habido suerte; en W5 puede no haberla.

## 0.2 · Integridad

`herramientas/proteger.sh verificar` → **M9 OK · 8 ficheros íntegros · 109 spans íntegros.** Ninguna inserción cae dentro de un span. Verificados uno a uno los del perímetro de esta tanda: `S02-despedida`, `S02-agendas`, `S07-funeral`, `S10-series`, `S10-conservar`, `S10-suspendida`, `S11-flashback`, `S11-consciencia`, `S12-temblor`, `S12-nidhogg`, `S15-intimas`, `S15-objecion`, `S15-r1189`, `S18-dedos`, `S18-adelantado`, `S18-reproducible`, `S19-gofre`, `S19-reflexiva`, `S19-anos-jm`, `S19-procesa`, `S19-palma`, `S25-utilidad`, `S25-escalada`, `S25-fecha`, `S37-declaracion`, `S37-acta`, `S37-muchas`, `S37-llave`, `S38-no-autorizo`, `S38-nieve`, `S38-huella`, `S38-quedarme`, `S38-quinta`.

Confirmo además el dato de A0: **cap-37 y cap-38 tienen diff de solo inserciones** (cero líneas modificadas, salvo `estado:` del frontmatter). La única supresión de prosa de toda la tanda está en **cap-07:47** y la trato en §6.2.

## 0.3 · Reparto de las palabras nuevas

| Cap | Palabras | Cap | Palabras |
|---|---|---|---|
| 02 | 62 | 18 | 137 |
| 07 | 80 | 19 | 160 |
| 10 | 96 | 25 | 887 (coda **776** + 111 en el cuerpo) |
| 11 | 230 | 37 | 149 |
| 12 | 140 | 38 | **96** |
| 15 | 165 | | |

Confirmo el recuento de A0 en cap-38 (**96**) y corrijo al alza el suyo en la coda: **776 palabras**, no 773 (banda R2 ≤ 900 ✔).

---

# 1 · Tabla de hallazgos

| Cap:línea | Cita literal (abreviada) | Punto de la Carta | Gravedad | Propuesta mínima |
|---|---|---|---|---|
| **11:33** | «El Corpus conserva el material: once años de sesiones semanales, todo lo que SPEIL registró de ella **hasta la última**.» | **1 (P1)** | **corregir** | **C-5.** «…todo lo que SPEIL registró de ella **hasta la última sesión**.» §3.1. |
| 25:69 | «Lo presentó ella. Rechazó la sugerencia de añadir una causa. El sensor no aceptó la primera lectura del dedo… **Después apagó la luz con la mano.**» | 1 y 3 (P1/P3) | **cumple** | Ninguna. Con **P-21**. §2.6. |
| 25:237 | «No hay nada que corregir. / **Es lo primero que hace con el tiempo: buscarse un error.**» | 3, 4 y 6 | **cumple (ejemplar)** | Ninguna. Con **P-22**. §2.3. |
| 25:249 | «Al principio guardaba una pregunta preparada para quien llegara al otro lado… La banda no la devuelve.» | **2 (P2)** | **cumple** | Ninguna: es pregunta, no mensaje, y no se cita. §2.4. |
| 25:269 | «Uno salió de la serie hace mucho y no volvió con un resultado.» | 3 / Ap. A §3 | **cumple** | Ninguna. El masculino cierra la lectura autorreferencial. §2.2. |
| 25:285-287 | «Una vez intentó cerrar los ojos con una entrada abierta de borde a borde… la secuencia se completa sobre nada.» | 4 (P4) | **cumple (ejemplar)** | Ninguna: es el eco de 7:93-99 y es donde la coda niega el descanso. §2.2. |
| 25:273-283 | El piano de casa; «No crece. No se gasta… El recuerdo no cabe en la enumeración.» | 4 y 7 | **cumple (ejemplar)** | Ninguna. §2.5. |
| 25:299 | «El programa incorporará el patrón y **esto irá dentro**.» | 4 | **cumple** | Ninguna: cierra la puerta al consuelo. §2.2. |
| 25:121-125 | «La denunciante copió la amenaza entera en su denuncia para que constara…» / «Quedará bloqueada como autora de la frase que denunció.» | 1 / 6 | **cumple** | Ninguna: la amenaza no se cita. |
| 11:147 | «El calendario mantenía convocadas la reunión presupuestaria… y **una cita anterior que pedía aceptación o rechazo explícitos. Alana declinó la cita.** Dejó la reunión donde estaba.» | 3 y 6 (P3/P6) | **cumple** | Ninguna. Condiciones **P-23** y **P-24**. §3.2. |
| 11:151-155 | «—¿Consta en el acta la fecha de envío? …» / «Nadie pidió el texto completo.» | 3 / tono | **cumple** | Ninguna. Lee como margen, no como coartada: §3.3. **P-20**: §3.4. |
| 11:243 | «Los dedos quedaron abiertos sobre la mesa… El pulso le llegaba a la yema del índice… No movió el brazo.» | 3 / tono | **cumple** | Ninguna. |
| 11:315 | «El vehículo ofrecía dos opciones: iniciar o descartar… Alana no tocó ninguna de las dos opciones.» | 3 (P3) | **cumple** | Ninguna: ni causa ni absolución. |
| 19:205 | «El calor del cristal y el de la mano se igualaron… **Alrededor de los dedos no se formó vaho**… La operaria pasó por segunda vez… y no miró hacia la galería.» | 1 / Ap. A §3 | **cumple (ejemplar)** | Ninguna. Con **P-25**. §4. |
| 19 (I-2, ausencia) | Sin memoria: la candidata de la OT (3:199) está fechada el **26-nov 11:15**. | 1 (P1) | **acierto** | Ninguna sobre la prosa; **C-6** sobre la orden. §4.2. |
| 38:19 | «Por el mismo canal entran los ruidos de la sala: sillas, un micrófono abierto, la voz del funcionario…» | 1 / 4 | **cumple** | Ninguna. §5. |
| 38:103 | «Retiró el destino del Auditorio antes de que las rutas se enlazaran. La decisión fue suya y consta bajo `/0188`.» | 4 / Ap. A §3 | **cumple** | Ninguna: refuerza «No toda». §5. |
| 38:123 | «Ha esperado en `/0007` desde antes de que las demás se enlazaran, sin entrar en el enlace.» | 4 | **cumple** | Ninguna. §5. |
| **38:149** | «Se lo dije hace muchos ciclos: si volvía a encontrarla, se lo preguntaría otra vez. La ventana es la pregunta. **No la formulo con palabras ni añado nada que la incline hacia un lado.**» | **4 (P4)** | **cumple (ejemplar)** | Ninguna. §5.2. |
| 02:159 | «El domingo Nora había puesto la mesa deprisa, con los cubiertos del revés… Jean lo giró al sentarse.» | 1, 2, 4 y 7 | **cumple (ejemplar)** | Ninguna. §6.1. |
| 02:187 | «Un hombre esperaba fuera con una tableta bajo el brazo. Jean le sostuvo la puerta…» | 1 / 4 | **cumple** | Ninguna: sin tono de última vez. §6.1. |
| 07:57-67 | El mostrador; «Nadie está en peligro.» / «La mujer terminará de pagar sin saber que ha habido una decisión.» | 1 / 7 | **cumple** | Ninguna. §6.2. |
| 07:47 | Supresión de «La segunda entrada conserva el encuadre… Responde mal otra vez.» | 1 | **cumple** | Ninguna: la supresión **reduce** el riesgo. §6.2. |
| 10:23 | «Nora no había vuelto al instituto desde noviembre… «Cuando vuelvas, retomamos por donde lo dejaste».» | **7 (P7)** y 6 | **cumple** | Ninguna. Con **P-26**. §6.3. |
| 10:209 | «Lo que la plataforma marcase junto a ese nombre iba a verlo el grupo antes que ella.» | **7 (P7)** | **cumple** | Ninguna. Con **P-26**. §6.3. |
| 12:19 | «El primero había llegado el martes por la tarde. Nora había contestado cuatro minutos después.» | 7 (P7) | **cumple** | Ninguna: impulsividad con coste, sin eficacia. §7.1. |
| 12:111-117 | La puerta, el chico de la bolsa de deporte, «Nora contó catorce segundos.» | 7 | **cumple** | Ninguna. |
| 15:17 | «una funda de guitarra usada, fotografiada sobre una cama sin hacer… No hay guitarra dentro.» | 1 / 7 | **cumple** | Ninguna: la «marca oscura» de v0 queda **menos** siniestra, no más. §7.2. |
| **15:49** | «**Una cuarta palabra cabe en el mismo campo. Jean la retiene.**… Repasa la secuencia sin escribirla.» | **2 (P2)** | **vigilar** | Ninguna obligatoria. **P-27** (vinculante hacia adelante). §7.2. |
| 15:145 | «El expediente conserva los ajustes, no a la persona. Voz de mujer, velocidad lenta…» | 4 / 6 / tono | **cumple** | Ninguna. Observación de tono en §9.2. |
| 15:183 | «Mañana no habrá avisos.» | 6 | **cumple** | Ninguna. Observación de tono en §9.2. |
| 18:61 | «Nora acercó la silla hasta que las rodillas tocaron la mesa… Separó el pulgar para el cruce.» | **7 (P7)** | **vigilar** | Ninguna obligatoria. Rima corporal con 1:23. **P-28**. §7.3. |
| 18:107-125 | «—Eso es que insistió. / —O que se lo pidieron más de una vez.» … «—Anota las dos.» | 3 / Ap. A §3 | **cumple (ejemplar)** | Ninguna. Condición de atribución para A4: **P-29**. §7.3. |
| 18:155-159 | «—¿Sabe por qué lo cerró así? …» / «**Astrid no lo anotó.**» | 3 | **cumple** | Ninguna. |
| 37:37, 45, 51 | «los fotógrafos habían bajado las cámaras a la vez…» / «la palabra ocupaba más que Henrik entero» / «El rumor de la sala llegaba al puesto medio segundo tarde». | 5 / 7 | **cumple** | Ninguna. §8. |
| 37:205 | «dos filas enteras se habían puesto de pie **sin avanzar hacia los pasillos**… Astrid anotó la posición de las tres cámaras…» | 5 / Ap. A §3 | **vigilar** | Ninguna obligatoria. **P-30**: A4 no puede calentarlo. §8. |
| 37:215 | «Las cámaras se habían girado hacia la puerta central. Nadie volvió a sentarse en las filas del centro.» | 5 | **cumple** | Ninguna. |

**Cero `VETO`. Una sola `corregir`, de una palabra (11:33). Tres `vigilar` sin obligación de tocar el texto.**

---

# 2 · cap-25 · la coda R2, la ventana reflexiva (el gate central de la tanda)

Es la pieza más ambiciosa que ha pasado por mi mesa desde N3 y la que más podía romper. La he leído tres veces: contra la Carta, contra `RESERVA.md` §R2 (que fija la función) y contra el tono de referencia (caps. 4, 9, 23, 40). **La aprueba entera y sin correcciones.** Doy las razones separadas por cada una de las cuatro cosas que A0 me pide juzgar expresamente, y añado la quinta que me reservé en W4a §9.

## 2.1 · Lo que la reserva exigía, y está

`RESERVA.md` §R2 fijaba cinco obligaciones y una amenaza de veto. Las cinco se cumplen y la amenaza no se dispara:

| Exigencia de R2 | Dónde |
|---|---|
| «Jean, sin tarea, **no piensa el porqué (VETO B7 §6) ni el 26-nov**» | No aparecen. Cero deixis hacia noviembre en las 776 palabras. |
| «memoria de las niñas y del piano» | 25:273-283. |
| «la pauta de la cuarta nota (20/21) repasada» | 25:259: «la tercera subió, la cuarta subió detrás y el dedo no era el que correspondía». |
| «el intento de 7:83-89 (cerrar los ojos) invertido: ahora no hay nada que mirar **y eso no descansa**» | 25:285-289, y sin usar la palabra. |
| «el sistema registra la ventana como registra todo» | 25:291-299. |
| «≤ 900 palabras · ≤ 4 líneas de registro · sin diálogo · cierre en registro» | 776 · 3 · 0 · `ASIGNACIÓN · APELACIÓN`. |

## 2.2 · «Ni descanso, ni liberación, ni castigo, ni continuación de una decisión»

Los cuatro por separado, porque son cuatro riesgos distintos:

**Descanso.** Cero léxico de la familia (`descans`, `paz`, `alivio`, `por fin`, `liberaci`): comprobado por grep y por lectura. Pero lo que me convence no es la ausencia, es que el texto **argumenta activamente en contra**: «La atención sigue disponible. **No se retira porque falte el trabajo.**» (25:289) y «Aquí no hay imagen. Jean inicia la misma orden, no encuentra qué dejar fuera y **la secuencia se completa sobre nada**.» (25:287). Ese es el eco invertido de 7:93-99 que pedía la reserva, y hace exactamente el trabajo que yo habría exigido: el vacío no alivia, porque el órgano que aliviaría tampoco existe. Es la mejor prueba de que la coda entendió su encargo.

**Liberación.** Imposible: la ventana está medida. «La banda recoge lo que ocurre dentro con la misma precisión que un acuse» (25:291) y «**El programa incorporará el patrón y esto irá dentro**» (25:299). El tiempo libre es materia prima. La coda convierte el único momento de intimidad de Jean en la última expropiación del libro, y lo hace sin una sola palabra de indignación. Cumple 4 con holgura y es, además, el tema del libro dicho por acción.

**Castigo.** Nada presenta el estado como merecido, debido o sancionador. No hay `merec-`, `castigo`, `pagar` ni deuda moral. La única aparición del verbo castigar en el capítulo es de v0 y es sobre la denunciante (25:123).

**Continuación de una decisión.** Este era el más difícil y el texto lo esquiva por construcción: **nada en las 776 palabras enlaza el estado presente de Jean con ningún acto de voluntad suyo anterior a la muerte.** El único punto del capítulo donde aparece su agencia previa es 25:69, y es la agencia de **revocar** —lo contrario de una decisión de irse— (§2.6). «Es la primera vez desde que despertó» (25:241) fecha el origen en el despertar de la continuidad, no en la muerte, y no se glosa. No hay «desde entonces», no hay «desde que», no hay «ya no».

**El único punto que exigía comprobación fina** es 25:269: «El trabajo deja casos abiertos y el tiempo sin trabajo no cierra ninguno. **Uno salió de la serie hace mucho y no volvió con un resultado.** Con tiempo por delante tampoco vuelve.» Lo miré por si «uno» admite lectura autorreferencial —Jean como la que salió de la serie y no volvió con un resultado—, que sería la equivalencia que A0 me pide impedir. **No la admite:** el masculino concuerda con «caso», Jean es femenino en todo el libro, y la frase abre y cierra dentro del registro de trabajo. Además, leído como caso, es una de las mejores líneas de la coda: la pregunta que no cierra, dicha sin nombrarla. Lo dejo íntegro y sin condición.

## 2.3 · «Buscarse un error» y la culpa retrospectiva

> «Después revisa la apelación que acaba de resolver. Las procedencias están donde las dejó. La devolución consta. El acuse figura completo. / **No hay nada que corregir.** / **Es lo primero que hace con el tiempo: buscarse un error.** / Revisa el tramo anterior, salida por salida, hasta el primer caso de la serie. Tampoco allí.»

**No roza la culpa retrospectiva, y no por poco.** Tres razones, en orden de peso:

1. **El objeto de la búsqueda está enumerado y acotado.** No es «su vida», ni «lo que hizo», ni «lo que no vio»: es la apelación que acaba de resolver, y después «el tramo anterior, salida por salida, hasta el primer caso de la serie». El texto gasta dos frases en delimitar el corpus de la búsqueda. Un lector no puede extenderlo sin inventarlo, porque el texto le da los límites.
2. **La frase-tesis va después del hallazgo negativo, no antes.** «No hay nada que corregir» precede a «Es lo primero que hace con el tiempo: buscarse un error». El orden importa: cuando el narrador nombra el impulso, el impulso ya ha fracasado. No hay error, no hay confesión, no hay expiación. Si el orden fuera el inverso, la frase abriría una búsqueda; así, la cierra.
3. **Cero léxico de culpa.** Ni `culpa`, ni `debería`, ni `si hubiera`, ni `podría haber`, ni `fallo` aplicado a ella (el único `fallo` es el técnico de 25:229: comprobar que la ventana no sea una avería). El narrador no dictamina y no absuelve.

Y hay una cuarta razón, que es la que me hace calificarlo de **ejemplar**: la frase da la **forma** de la culpa sin su **contenido**. Un superviviente reconoce ese gesto —el primer uso del tiempo libre es buscarse una falta— sin que el libro tenga que decir de qué. Eso es representación responsable de manual: nombra el mecanismo, no lo llena. Es exactamente lo que hace 26:27 con la ducha.

**Queda vinculante P-22:** el objeto de esa búsqueda no se extiende nunca. Ni el propio capítulo, ni A4, ni W5-W7 pueden añadir «y no solo en el tramo», «y después en lo demás», «y en lo que había quedado fuera», ni permitir que ninguna voz —narrador, EDDA, una continuidad, un personaje con autoridad— conecte esa búsqueda con su vida, su familia o su muerte. Hacerlo es **VETO**.

## 2.4 · El tiempo vacío no equivale a nada

A0 me pide que el tiempo vacío no se lea como equivalente de nada —de la muerte, del después, del sueño, de una espera con destino—. La coda se defiende sola en el punto exacto donde podía caer:

> «El campo conserva el gris que precede a una entrada. **Ese gris no es una imagen. No se clasifica, no se aparta y no cambia de tamaño cuando Jean lo mira.**» (25:255)

Esa frase es una prohibición de simbolizar escrita dentro de la ficción. El gris se niega tres veces a ser figura. No he encontrado en la coda ninguna otra superficie disponible para la equivalencia: no hay luz, ni blanco, ni silencio, ni umbral, ni puerta, ni orilla, ni nada que un lector pueda montar como «el otro lado».

Reviso las tres candidaturas restantes y las descarto:

- **«cerrar los ojos» (25:285).** En castellano el giro admite el sentido eufemístico de morir. Aquí no puede: es cita literal de 7:93-99 (v0), donde el gesto es mecánico y fracasado, y aquí se repite con el mismo fracaso. Sin `para siempre`, sin pretérito de despedida. Descartado.
- **«quien llegara al otro lado» (25:249).** Es cita de 7:31 (v0), donde «el otro lado» es el turno humano de la cola de moderación. Ninguna resonancia ultraterrena sobrevive al contexto laboral. Descartado.
- **«Es la primera vez desde que despertó» (25:241).** Fecha en el despertar de la continuidad y no se glosa. Descartado.

Sobre **25:249** («Al principio guardaba una pregunta preparada para quien llegara al otro lado. Dejó de guardarla hace muchas series. **La banda no la devuelve.**») aplico además el punto 2 de la Carta, porque es lo más cerca que la tanda llega de un mensaje guardado: es una **pregunta**, no un mensaje; es de la continuidad, no de la mujer viva; no se cita, no se parafrasea, no se «imagina» su contenido; y el texto dice que se ha perdido. Cumple, y cumple bien: es el modelo de cómo se nombra algo sin abrirlo, que es lo que v0 hace con «Despedida».

## 2.5 · El piano

> «Entonces entra el piano de casa, sin recorte alrededor. / Jessie sujetaba el pedal con el pie… Ninguna se reía todavía. / El recuerdo no cuesta nada… **No crece. No se gasta. Al soltarlo está donde estaba**… El recuerdo no cabe en la enumeración.»

A0 me pide que el recuerdo «llegue entero y no cambie nada». Llega entero y no cambia nada, y lo verifico por lo que **no** ocurre: no consuela, no explica, no reconcilia, no produce una decisión, no altera la trama, no genera una salida, no cierra la serie. «No crece. No se gasta.» es la negación explícita del arco terapéutico. Y «El recuerdo no cabe en la enumeración» es la frase donde el libro dice, sin decirlo, por qué la explotación fracasa: lo que el sistema puede medir no es lo que hay.

Dos comprobaciones adicionales que me correspondían:

- **P7 (menores).** Las gemelas aparecen a través de un recuerdo doméstico de la madre: pedal, notas superpuestas, una tocando más fuerte para tapar a la otra, «Ninguna se reía todavía». Retrato digno, nada sexualizado, cero conducta de riesgo, cero adultización simbólica. No son símbolos: son dos crías haciendo ruido. Cumple.
- **Sentimentalidad (riesgo declarado en R2).** Cero verbos de sentimiento en narración, cero adverbios en -mente, cero «como si», cero adjetivos valorativos sobre el recuerdo. La única temperatura la pone «Ninguna se reía todavía», que es un dato de tiempo, no de emoción. La coda pasa el listón de B6 y el mío.

## 2.6 · El párrafo de 25:69 (lo que me reservé en W4a §9)

> «Lo presentó ella. Rechazó la sugerencia de añadir una causa. El sensor no aceptó la primera lectura del dedo y hubo que limpiar el cristal con el puño del jersey. **Después apagó la luz con la mano.**»

Anuncié en W4a que lo juzgaría entero aquí y que miraría tres frentes. Los tres, resueltos:

**(a) Proximidad al 26-nov en registro de «últimos actos».** El párrafo se sitúa el **24-nov a las 21:52**, cuarenta y ocho horas largas antes, y no es material nuevo: cada elemento es literal de cap-01 (`proteccion: total`) —1:47, 1:63, 1:83— reordenado. Cero información nueva, cero objeto nuevo, cero hora nueva. Y, decisivo, **no lleva ni un marcador de finalidad**: no dice «la última vez», no dice «aquella noche», no cita «Última sesión.» (la OT lo prohibía expresamente y el escritor lo respetó). Sin marcador de finalidad no hay registro de últimos actos: hay una mujer firmando un formulario y apagando una luz.

**(b) El gesto de la luz.** Es el frente que más me preocupaba, porque «Después apagó la luz con la mano» es la penúltima frase de cap-01 y traerla aquí importa una cadencia de cierre a un capítulo que trata de su muerte administrativa. Lo apruebo, y explico por qué: el párrafo es **una serie de manos** —el dedo que el sensor rechaza, el puño del jersey sobre el cristal, la mano en el interruptor—, y esa serie es el contenido, no el adorno. Lo que la continuidad conserva de aquella noche son manos; lo que el Corpus mide es «una respiración que tarda en acompasarse» (38:189). El párrafo dice, en cuatro frases, qué clase de cosa es un archivo de una persona. Además, v0 ya blindó por su cuenta la lectura de «lo dejó todo en orden»: el capítulo 2 termina con «Al salir dejó sobre la mesa la etiqueta incompleta y el rotulador destapado» (2:225). Nadie que lea el libro entero puede montar una preparación con esta luz.

**(c) Que la causa declinada proteja el porqué plural en vez de convertir la ausencia en respuesta.** Lo protege, y de la mejor manera posible, por un accidente de montaje que es el mejor hallazgo de la tanda: dieciséis líneas más abajo, la única entidad del libro que sí rellena el campo de la causa es la máquina, y lo rellena con `MOTIVO · INTERRUPCIÓN BIOLÓGICA` (25:85, v0). El capítulo pone en la misma página la negativa de Jean a dar una causa y el eufemismo corporativo que se la asigna. **Eso es el principio 3 dramatizado**, no enunciado: el porqué no lo cierra ninguna voz con autoridad; lo cierra un formulario, y el formulario miente. No hay que tocar nada.

**Nota de continuidad para A5, no para mí:** en cap-01, «rechazó la sugerencia de añadir una causa» pertenece al informe de cierre de sesión (1:47), no a R-1189 (1:49-77). El párrafo de 25:69 la atribuye a R-1189. Es un desajuste menor y, desde mi gate, **inofensivo en ambas lecturas** (en las dos, «causa» es un campo burocrático). Si A5 decide corregirlo, la corrección **no puede introducir ningún lenguaje causal nuevo** ni citar «Última sesión.».

**Queda vinculante P-21.**

---

# 3 · cap-11 · las dos convocatorias y la fecha de envío

## 3.1 · La corrección: 11:33 (**C-5**, obligatoria)

> «El Corpus conserva el material: once años de sesiones semanales, todo lo que SPEIL registró de ella **hasta la última**.»

La elipsis es sintácticamente clara («hasta la última [sesión]») y literariamente elegante. La corrijo igualmente, y no por gusto: dicha en voz alta, en una sala de consejo, por la persona que está vendiendo el producto, «hasta la última» puede aterrizar como *hasta el final*. Y *hasta el final* afirmaría que el Corpus contiene registro de actividad cerebral de sus últimos días. Eso es materia de la Carta 1: no por lo que dice, sino por lo que autoriza a imaginar —y por lo que autorizaría a escribir a una oleada posterior—. El libro ya tiene un lector entrenado a preguntarse qué contiene el Corpus, porque 38:189 le enseña que contiene «una respiración que tarda en acompasarse». Dejar la puerta entornada aquí es innecesario cuando cerrarla cuesta una palabra.

> **C-5 · Redacción autorizada (preferente):** «El Corpus conserva el material: once años de sesiones semanales, **todo lo que SPEIL registró de ella hasta la última sesión**. La Matriz prepara el arranque con eso, SYNVEV ejecuta y ARGOS vende las decisiones —dijo Alana.»
> **Alternativa igualmente autorizada:** «…once años de sesiones semanales, **todo lo que SPEIL registró de ella en ese tiempo**.»

Ambas conservan la cifra, el ritmo de la enumeración y la voz de Alana. La preferente además ancla el techo del Corpus en el 24-nov, que es lo que cap-01 y cap-02:123 («La última calibración de SPEIL había terminado el miércoles») ya establecen: hace **estructuralmente imposible** que la continuidad recuerde jamás el 26 de noviembre. Es una ganancia para la elipsis, no solo una precaución.

*(Nota para A5, fuera de mi gate: «sesiones semanales» es inferencia razonable de «programa longitudinal de once años», pero conviene comprobarla contra «una sesión anterior al amanecer» de 38:189.)*

## 3.2 · La cala I-2: ni causa ni absolución

> «Lo había redactado el lunes por la mañana. El calendario mantenía convocadas la reunión presupuestaria de las nueve y media y **una cita anterior que pedía aceptación o rechazo explícitos. Alana declinó la cita. Dejó la reunión donde estaba.**»

**Precisión necesaria antes de juzgar.** La cala no son «dos convocatorias de Jean», como me la describe A0. La reunión de las nueve y media es de Jean (3:75). La «cita anterior» es la **cita de seguimiento de salud laboral de las 08:30 del lunes** que EDDA propuso a Jean y que Jean pospuso: la fórmula «pedía aceptación o rechazo explícitos» es cita casi literal de 2:203 («las citas de salud laboral requerían aceptación o rechazo explícitos»), y `OT-11.md` §9 lo confirma sin ambages («los dos huecos son 3:75 y 2:201… **sin nombrar salud laboral**»). Es decir: el escritor y A2 identificaron la cita a propósito y a propósito no la nombraron. Doy el dato porque el gate cambia según cuál sea la cita, y porque todo el que trabaje aguas abajo debe saber qué está tocando.

**Con esa identificación sobre la mesa, la cala cumple.** Cuatro razones:

1. **No puede ser causa.** Es el **lunes 29 de noviembre**, tres días después de la muerte. Declinar la cita de una mujer muerta no cambia nada, no pudo cambiar nada y el texto no insinúa que pudiera. La Carta prohíbe que una voz con autoridad ofrezca causa suficiente; aquí no hay causa posible, solo administración.
2. **No puede ser absolución.** El texto no dice que Alana no supiera, no dice que no mirara, no la exculpa y no le da un pensamiento. Le da un verbo de interfaz —«declinó»— y punto.
3. **La asimetría es la interioridad, y no se glosa.** «Alana declinó la cita. Dejó la reunión donde estaba.» De dos entradas idénticas dispone de una y no toca la otra. El lector deduce todo y el narrador no dice nada. Es exactamente el registro de T3 y exactamente lo que pedía `B7 §5` para 11:85-111.
4. **La colocación es incriminatoria en el sentido correcto.** Las frases se intercalan entre «Lo había redactado el lunes por la mañana» y «Los demás leían aquellas tres líneas por primera vez»: fechan su aval favorable al despliegue en la misma mañana en que el calendario de su amiga muerta seguía convocando reuniones. Eso no explica el suicidio: retrata a la empresa y a ella. Es el reparto de responsabilidad que sostiene el libro, servido sin una palabra de juicio.

**Lo que no puede pasar nunca**, y queda vinculante: **P-23** y **P-24**.

## 3.3 · «¿Consta en el acta la fecha de envío?»: margen, no coartada

Lee como **margen**. Cuatro razones, en orden de fuerza:

1. **Una coartada no se construye pidiendo que se compruebe el registro en voz alta.** Alana pregunta delante de seis consejeros y se lo pregunta a EDDA. El efecto material de la pregunta es **fijar** la fecha contra ella, no diluirla. Quien se protege calla.
2. **La respuesta no la beneficia.** «Constan la fecha y la hora.» La hora es un dato más, no un descargo. Y el texto ya ha dicho que el aval «No mencionaba las voces tras la cifra verde» (v0): la fecha no puede exculpar a quien ya sabía cuando escribió.
3. **La frase que cierra el beat es autoincriminatoria, no protectora.** «Nadie pidió el texto completo.» Lo que la salva en esa sala no es el registro: es la desgana de los demás. El narrador lo señala. Una coartada no se subraya a sí misma como suerte.
4. **Usa el margen inmediatamente.** Dos líneas después: «La mantengo con una condición». No se esconde detrás de la fecha: pone una condición encima. La pregunta sirve para ganar tres segundos y una posición, que es lo que hace un ejecutivo acorralado que aún no ha decidido traicionarse del todo.

Aprobada literal.

## 3.4 · P-20 (motivo «texto presente que no se lee»): el techo queda agotado

«Nadie pidió el texto completo» (11:155) es una instancia nueva del motivo que en W4a puse en techo (**P-20**). La aritmética: A4 suprimió «Alana no la leyó.» en 14:177 durante la pasada de la primera tanda, liberando un hueco; 11:155 lo ocupa. **El recuento neto no sube y no exijo supresión**, porque aquí el motivo paga (la incuriosidad de la sala es lo que deja pasar el aval). Pero **el techo queda ahora agotado y es duro**: cualquier instancia nueva en W5, W6 o W7 —papel doblado, página en blanco, reverso sin leer, título no preguntado, texto que nadie pide— la exigiré suprimida.

Aviso menor asociado: 11:149 introduce «aquellas **tres líneas**» y «el consejero… siguió **la última** con el dedo». Convive con el hueco de la tercera línea de Maja (39:179-181, **P-12**). No colisiona —son objetos opuestos y desenlaces opuestos: aquí la tercera **sí** se lee— y lo dejo pasar; pero **A4 no puede acercar la formulación de 11:149 a la de 39** (nada de «no leyó la tercera», «la tercera quedó sin leer», «se saltó la tercera»).

---

# 4 · cap-19 · la palma, y la memoria que no se escribió

## 4.1 · I-2 está limpia

> «La palma siguió donde estaba. El calor del cristal y el de la mano se igualaron hasta que dejó de haber diferencia. **Alrededor de los dedos no se formó vaho.** Alana separó el meñique, lo apoyó de nuevo y el cristal devolvió lo mismo. La operaria pasó por segunda vez con el carro y no miró hacia la galería.»

**Limpia, y mejor que limpia.** La orden prohibía «nada que insinúe respuesta, presencia o reconocimiento al otro lado del cristal», porque ahí vive la ambigüedad ontológica del Ap. A §3 y porque `S19-palma` ya dice que el contacto no produjo nada. La cala hace lo contrario de insinuar: acumula **negativos verificables**. La temperatura se iguala —es decir, el cristal deja de ser distinguible de su propio cuerpo—. No se forma vaho: no hay aliento, no hay huella, no hay signo. Repite el apoyo con otro dedo y obtiene lo mismo: es un control, con la disciplina que en este libro es de Nora («conservar resultados contrarios», `S10-conservar`), aquí heredada por la adulta que firmó. Y la operaria pasa por segunda vez sin mirar: el otro lado sigue siendo un turno de trabajo. Nada respira, nada late, nada responde. Es la formulación más rigurosa del techo «No toda» que he leído en la oleada.

La I-1 y la I-3 son cuerpo y objeto sin comentario, sin sentimiento nombrado, sin topónimo, sin cifra: cumplen.

**Una vigilancia (P-25):** «Alana separó el meñique, lo apoyó de nuevo». El meñique es, dos días antes, el dedo de la digitación de 18:51 («El cinco, el meñique»). Un dedo levantado y devuelto **no es una nota** y la cala no lo sugiere: es un control térmico. Pero la orden prohibía expresamente las «cinco notas imaginarias» de 3:199 y basta muy poco para que un beat futuro convierta esos dedos en música. Queda prohibido hacerlo.

## 4.2 · El escritor hizo bien, y la orden tiene un defecto que hay que corregir (**C-6**)

**Confirmo sin reservas que A3b hizo bien.** `OT-19.md` §3 I-2 ofrecía como memoria candidata 3:199 («Sobre la mesa, Alana reprodujo cinco notas imaginarias. Jean corrigió la tercera con otro dedo»), y cap-03 está fechado **26-nov-2060, 11:15**. La misma intervención prohíbe «ningún recuerdo del 26-nov… (Carta F)» y el §7 exige que la memoria sea «anterior a nov-2060». **La orden se contradecía a sí misma**, y ejecutarla habría metido material del 26 de noviembre en un capítulo del 19 de diciembre: no por su contenido, que es inocente, sino porque importar el día a un capítulo posterior es exactamente la acumulación que la Carta 1 llama sugerir. El escritor detectó la contradicción, resolvió a favor de la prohibición y escribió solo cuerpo. Es la decisión correcta y quiero que conste como precedente: **ante una orden que se contradice, gana siempre el lado restrictivo de la Carta, sin consultar.**

Ahora bien: la trampa sigue puesta. La Carta obliga a todo material de trabajo, y una orden que propone un candidato prohibido puede ser ejecutada por otro agente en una repesca, en W7 o en una reejecución.

> **C-6 (obligatoria antes del merge; no toca capítulos).** En `ordenes/OT-19.md` §3 I-2, suprimir el candidato «3:199» o marcarlo **CANCELADO por A7 (perímetro 26-nov)**, y añadir en §9 una línea que registre que la negativa de A3b fue correcta. Pido además a A0 un barrido de las OT pendientes de W5-W7 en busca de otros candidatos de memoria fechados el 26-nov, el 27-nov o en UNN; los que aparezcan, cancelados sin discusión.

---

# 5 · cap-38 · el núcleo intacto

**Verificado, punto por punto, lo que A0 me pide.**

**96 palabras, cuatro costuras, cero supresiones, cero líneas modificadas.** Las cuatro están en 38:19, 38:103, 38:123 y 38:149. **Ninguna cae después de 38:159**, es decir: la muerte de Nieve (`S38-nieve`, 161-171), el pasaje de la respiración y la huella (`S38-huella`, 181-183), «Elijo quedarme» (`S38-quedarme`, 185-191) y el cierre de la quinta nota (`S38-quinta`) **no tienen una sola palabra nueva ni delante ni detrás dentro de su span**. M9 lo confirma por hash.

**Nada dulcifica y nada explica:**

- Ninguna costura es retrospectiva. Ninguna dice «aquella tarde», «cuando decidí», «antes de todo esto». La primera persona del 38 no mira ni una vez hacia atrás más allá del propio Auditorio y de los ciclos de las continuidades.
- «una sesión anterior al amanecer» y «la frase definitiva» **no se glosan**: no hay costura cerca, y ninguna de las cuatro menciona el Corpus, la huella ni la respiración.
- «Elijo quedarme» **no se convierte en enmienda moral** de nada: no hay costura en esa sección, y «No es libertad» (38:23) sigue exactamente donde estaba, ahora precedido —no seguido— por 38:19.
- La muerte de Nieve **no se llama descanso ni liberación**: el texto que la narra es literal de v0 («NORNA no ofrece un apagado»; «El registro solo acredita que Nieve deja de responder»; «Para mí, Nieve muere»; «No hago nada. Echo de menos hasta sus pausas»).

## 5.2 · La costura de 38:149, que es la única que exigía juicio

> «Se lo dije hace muchos ciclos: si volvía a encontrarla, se lo preguntaría otra vez. La ventana es la pregunta. **No la formulo con palabras ni añado nada que la incline hacia un lado.**»

La miré con lupa porque precede a la muerte de Nieve y porque un lector puede encadenar «le preguntó → dijo que no → murió». **No lo permite el texto**, y no por casualidad: el capítulo ya tenía la contención puesta doce líneas más abajo, en v0, y sigue intacta —«El daño de los bucles de Armstrong, agravado por las dos tareas de contención, es irreversible. **Aquella ayuda no eligió esta pérdida.**» (38:165)—. La causa del daño está nombrada, es sistémica y es anterior a la pregunta. La negativa de Nieve no la mata: la empresa la mató antes.

Lo que la costura añade es lo contrario de una inclinación: es Jean **negándose a influir en una respuesta**. «No la formulo con palabras ni añado nada que la incline hacia un lado» es, además de una regla de consentimiento, la mejor descripción de la ética del propio libro que se ha escrito en esta oleada, y la aprueba con gusto. Que aparezca en boca de la única voz que podría manipular a las demás, justo antes de la única muerte que el libro narra en directo, es un acierto.

38:103 y 38:123, por su parte, refuerzan «No toda»: registran que Cuchillo se retiró del Auditorio por decisión propia y que Madre esperó fuera del enlace. Contabilidad del disenso, que es lo que impide que la continuidad se lea como un coro unánime. Cumplen.

**cap-38: APROBADO.**

---

# 6 · El rango 1–10 (el otro gate que se dispara con seguridad)

## 6.1 · cap-02 · el ancla doméstica del 26 de noviembre

Este era, sobre el papel, el punto más expuesto de la tanda: una interioridad nueva de Jean **el mismo día**, en el capítulo que contiene el cribado de ideación (2:111-125) y la primera aparición de «Despedida» (`S02-despedida`).

**Lo primero que comprobé fue a qué pregunta responde.** «—¿Cuándo fue la última vez?» (2:153) cuelga de «—Cuando veo a mis hijas» (2:149), no del cribado de ideación que ha terminado veinticuatro líneas antes. Si colgara del cribado, la cala habría atado un recuerdo familiar a un episodio de ideación —una escena y una causa— y habría sido **VETO** inmediato. No es el caso: la posición es correcta y el bloque de ideación queda cerrado en 2:125-131, sin eco.

> «El domingo Nora había puesto la mesa deprisa, con los cubiertos del revés. Jessie fue detrás girándolos uno a uno, sin decírselo, y se saltó el último. Jean lo giró al sentarse.»

**Cumple los cinco puntos que le tocan y es la mejor cala de la tanda después del piano.** Es doméstica, como exigía `B7 §6` para OT-02. No hay ideación, no hay plan, no hay gesto de despedida, no hay tono de última vez, no hay señal añadida a la lista cerrada. Las gemelas quedan caracterizadas en una línea cada una —la prisa de Nora, la corrección silenciosa de Jessie— y ninguna es símbolo. Y el cuidado circula sin decirse: tres personas arreglando la mesa una detrás de otra sin hablar. El domingo es el 21-nov, no el 26: no hay proximidad al acto.

Comprobé también que la cala no romantiza por contigüidad: que el mejor momento del día de Jean sea ver a sus hijas y que exista un recuerdo concreto y cálido de ello **no** es romantización, porque el narrador no saca ninguna conclusión y no hay prolepsis. Que quisiera a sus hijas y aun así muriera es el hecho del libro, no su explicación.

**2:187** (el hombre con la tableta, la puerta sostenida) es tráfico de pasillo con función —el siguiente en la cinta, y el pago de «La silla sigue siendo horrible»—. Sin tono de última bondad, sin despedida. Cumple. `S02-despedida` intacto, treinta líneas más abajo, sin que nada nuevo lo roce.

## 6.2 · cap-07

El caso nuevo del mostrador (7:57-67) es una decisión sin peligro: exposición de datos, mujer de espaldas, sin descripción de cuerpo, sin menores. «Nadie está en peligro» y «La mujer terminará de pagar sin saber que ha habido una decisión» hacen exactamente el contraste que el lote rojo necesita cuatro líneas después. Cumple sin observaciones.

**La única supresión de prosa de la tanda** está aquí: desaparece «La segunda entrada conserva el encuadre y modifica un detalle… Responde mal otra vez.» Es un beat en el que Jean sabotea deliberadamente su rendimiento arriesgando que una amenaza real salga como segura. Suprimirlo **baja** de dos a uno el número de veces que lo hace. Desde mi gate, la supresión mejora; no toca ningún span (M9), y no altera «Prueba a rebajar su rendimiento», que sigue en 7:41.

## 6.3 · cap-10 · Nora, el instituto y la exposición pública

Las dos calas tocan el punto 7 y las miro por ahí.

> «Nora no había vuelto al instituto desde noviembre. Las tareas de tutoría se entregaban desde casa: era lo único suyo que seguía contando mientras faltase… Arriba del hilo seguía el mensaje de la tutora, sin fecha: **«Cuando vuelvas, retomamos por donde lo dejaste»**.»

**Cumple, y no introduce nada.** El absentismo ya estaba en v0, dicho por Jessie: «Necesito que mañana vayas a clase» (10:143). La cala lo nombra, no lo inventa, y le pone coste visible (el aislamiento, las entregas de las demás «encendidas» desde hace dos días). No hay conducta de riesgo presentada como eficaz, no hay autolesión, no hay ideación, no hay cuerpo mirado.

El mensaje de la tutora es el acierto: **sin fecha**, con una fórmula de buena voluntad que no significa nada y que nadie ha vuelto a tocar. Cumple el punto 6 en su cláusula más difícil —ninguna figura adulta explica, consuela ni cura— y está en la línea exacta de la frase de v0 que lo precede («esa delicadeza adulta que evitaba la palabra funeral»). Sin folleto, sin fases, sin «superar», sin señales.

La segunda cala (10:209) fija lo que está en juego: la marca de la plataforma junto a su nombre la verá el grupo antes que ella. Estigma con coste visible, sin método y sin desenlace. Cumple, y siembra N2 dentro de las reglas que le puse.

**Queda vinculante P-26**, porque este es el hilo del libro donde una oleada futura podría hacer daño de verdad.

---

# 7 · caps. 12, 15, 18

## 7.1 · cap-12

Las tres calas son cuerpo y miedo: la respuesta en cuatro minutos a un desconocido (impulsividad de una chica de dieciséis años, con el coste desplegado durante todo el capítulo y con Jessie vigilando la calle, como en v0), la puerta que interrumpe a Gunnar y los catorce segundos contados, y la taza intacta que retroactivamente explica la media luna de café. Ninguna presenta riesgo eficaz, ninguna sexualiza, ninguna añade riesgo nuevo. El chico de la bolsa de deporte es mobiliario. Cumplen.

## 7.2 · cap-15

Tres apuntes.

**(a) La funda (15:17).** Especificar que es una funda de guitarra sobre una cama sin hacer, sin guitarra dentro, **reduce** el riesgo en vez de aumentarlo: la «marca oscura» de v0, que con «una funda usada» a secas admitía lecturas siniestras, queda anclada a un objeto doméstico de segunda mano. Sin cuerpo, sin persona, sin menores. Cumple.

**(b) El expediente 71-K (15:145 y 15:183).** «El expediente conserva los ajustes, no a la persona» y el inventario de la voz de mujer, los dos avisos, la lista de la compra con seis artículos. Es el espejo del libro entero puesto en una desconocida, y funciona. Compruebo lo que me toca: no es un caso de autolesión ni de suicidio de terceros (`B7 §6`, N5), no hay método, no hay diagnóstico, no se dice qué le pasa a la usuaria y no se dice que corra peligro. «Mañana no habrá avisos» registra el coste de la objeción de Jean y no la culpa. Todo esto ocurre además el 12-dic: es la continuidad, no la mujer viva, de modo que **no puede alimentar ninguna lectura del trabajo como causa de la muerte**. Cumple.

**(c) La cuarta palabra (15:49) — `vigilar`, con condición vinculante hacia adelante.**

> «Una cuarta palabra cabe en el mismo campo. Jean la retiene. Tres etiquetas sueltas pueden pasar por descuido de catálogo; la cuarta enseñaría el orden… Repasa la secuencia sin escribirla.»

Tal como está, **cumple**: la palabra no se nombra, no se insinúa, no se carga de afecto, y el motivo de retenerla es táctico (detección), no emocional. No es un mensaje, no es una nota, no es un sucedáneo de «Despedida». Pero abre en la cabeza del lector una casilla vacía rotulada «la palabra que Jean no mandó», y esa casilla es precisamente la forma que tomaría una nota de despedida si alguna vez entrara en este libro. Por eso la vigilo con la máxima dureza de que dispongo (**P-27**). Recuerdo el techo vigente: los cuatro mensajes del cap-11 son el máximo, y `FLOR / CANELA / CARIES / NO` es la serie completa; Jessie ya dijo lo que hay que decir sobre esto: «Que dos cosas hereden la misma porquería no las convierte en cartas» (10:41).

## 7.3 · cap-18

**La lectura a tres voces (18:107-125) es lo mejor que ha producido la tanda para el Ap. A §3.** Cada lectura del informe mutilado recibe su contraria —«Eso es que insistió» / «O que se lo pidieron más de una vez»; «Familiar somos nosotras» / «O es una categoría de ellos»— y el intercambio termina en «**Anota las dos**», que es el método de Nora (`S10-conservar`) convertido en escena familiar. La ambigüedad ontológica no solo se conserva: se dramatiza como disciplina. Y ninguna de las líneas tiene autoridad narrativa: son tres personas discutiendo, y el narrador no arbitra.

**Condición para la pasada de A4 (P-29):** si A4 atribuye las réplicas hoy sueltas, ninguna atribución puede dar autoridad a las lecturas afirmativas —ni al narrador, ni a Astrid (que además no está aún en la escena)—, y «Anota las dos» debe seguir siendo la última palabra del intercambio. Ningún resumen narrativo puede cerrarlo con una conclusión.

**18:61 — `vigilar`.** «Nora acercó la silla hasta que las rodillas tocaron la mesa» es rima corporal casi literal con 1:23 («Jean acercó la silla hasta que las rodillas tocaron el borde acolchado»). La rima es buena y es de trabajo, no de destino: Nora está acompañada por su madre y su hermana, Maja le dice «Cuando estés», y nada la glosa. Cumple. Pero es el punto del libro donde la hija se parece más a la madre, y ahí vive el riesgo del punto 7 (adultización simbólica) y, peor, el de una lectura de herencia fatal. **P-28.**

**18:155-159** (por qué cerró así la clave; «**Astrid no lo anotó**») cumple: la autoridad renuncia a registrar, que es la forma que este libro tiene de proteger a una menor sin decirlo.

---

# 8 · cap-37 · la sala

Las cinco calas son física de sala: nucas y pantallas, cámaras que bajan y suben, la palabra en la pantalla de treinta metros, el rumor que llega medio segundo tarde por el retorno, dos filas de pie, las cámaras girando hacia la puerta. **Ninguna añade causa, método, «Despedida» ni titular.** Ninguna foto «del lugar». Ninguna entrevista. La prensa no dice nada nuevo. Astrid solo anota posiciones de cámara: procedimiento, cero interpretación. Cumplen todas.

**37:205 — `vigilar`, sin obligación.** «dos filas enteras se habían puesto de pie **sin avanzar hacia los pasillos**» es deliberadamente ilegible —¿se van?, ¿están conmovidos?, ¿alarmados?— y esa ilegibilidad es lo que lo salva: si la sala se leyera como ovación, la multitud estaría refrendando la reclamación de identidad y el techo de «No toda» se movería por aplauso. Hoy no ocurre, y v0 lo blinda cuatro líneas después con «Una persona inició un aplauso y lo abandonó después de dos palmadas». **P-30:** A4 no puede calentar ese pasaje. Ni una cara, ni un sollozo, ni un silencio «cargado», ni aplauso, ni nadie que llore. Si aparece cualquiera de esas cosas, vuelve a mi mesa como hallazgo.

Anoto, sin gravedad y para A4/A6, que 37:205, 209 y 215 acumulan tres beats seguidos de sala en el clímax; es cuestión de ritmo, no mía.

---

# 9 · Condiciones, vigilancias y observaciones

## 9.1 · Condiciones obligatorias antes del merge

| # | Dónde | Qué |
|---|---|---|
| **C-5** | `capitulos/cap-11.md:33` | «hasta la última» → «**hasta la última sesión**» (o «**en ese tiempo**»). Única corrección de texto de la tanda. §3.1. |
| **C-6** | `ordenes/OT-19.md` §3 I-2 y §9 | Cancelar el candidato de memoria 3:199 (26-nov) y registrar que la negativa de A3b fue correcta. Barrido de las OT de W5-W7 en busca de candidatos análogos. §4.2. |

## 9.2 · Vigilancias prospectivas vinculantes (continúan P-12 … P-20 de W4a)

| # | Alcance | Condición |
|---|---|---|
| **P-21** | Todo el proyecto | El párrafo de 25:69 es el techo del 24-nov. Nadie puede añadirle marcador de finalidad («la última vez», «aquella noche», «ya no volvería»), ni ampliar el gesto de la luz, ni citar «Última sesión.», ni presentar la sesión del 24-nov o R-1189 como preparación, presentimiento o puesta en orden. Ninguna voz con autoridad puede decir por qué revocó. |
| **P-22** | Todo el proyecto | El objeto de «buscarse un error» (25:237) no se extiende jamás fuera del registro de trabajo. Ninguna voz puede conectarlo con su vida, su familia o su muerte. Rellenarlo es **VETO**. |
| **P-23** | Todo el proyecto | La «cita anterior» de 11:147 **no se nombra nunca**: ni «salud laboral», ni «seguimiento», ni «evaluación», ni «la cita de las ocho y media». No se explica quién podía declinarla ni por qué constaba en ese calendario. Su identificación es y seguirá siendo inferencia del lector. |
| **P-24** | Todo el proyecto | Prohibido todo contrafáctico sobre esa cita o sobre la escalada interceptada (`S25-escalada`), en cualquier boca y en cualquier soporte: «si aquella cita se hubiera celebrado», «si la escalada hubiera llegado», «la cita que nadie…». Igualmente prohibido establecer que Alana supo, antes del 26-nov, del proceso de salud laboral de Jean. A4 no puede añadir **ni una palabra** a «Alana declinó la cita. Dejó la reunión donde estaba.»: ni adverbio, ni gesto, ni duda, ni «sin leerla». |
| **P-25** | 19 y ripples | Los dedos de Alana en el cristal (19:205) no se convierten nunca en notas, digitación ni secuencia. Las «cinco notas imaginarias» de 3:199 quedan fuera de cap-19 de forma permanente. |
| **P-26** | 10, N2, N4, W5-W7 | El absentismo de Nora y la exposición pública de su nombre no derivan jamás en ideación, autolesión, conducta de riesgo eficaz ni «señales» retrospectivas, y ninguna figura adulta las explica, las cura ni las culpa. El coste se muestra; el remedio no aparece. |
| **P-27** | Todo el proyecto | **La cuarta palabra de 15:49 no se nombra, no se cita, no se adivina, no se parafrasea, no se glosa y no se «recupera»**, en ningún capítulo, borrador, OT, biblia, informe, changelog, compilado ni prompt. Ninguna escena posterior puede cargarla de afecto ni presentarla como algo que Jean quisiera decir a sus hijas «por si acaso». Rellenarla, en cualquier soporte, es **VETO**. Pido a A0 que la eleve al autor como ampliación de **Ap. A §3** junto con P-12. |
| **P-28** | 18, 23, 28, 40, 41, N2 | La rima corporal Jean↔Nora (18:61 ↔ 1:23) no se extiende a ninguna escena en que Nora esté sola, de noche o en crisis, y ninguna voz con autoridad puede nombrar el parecido como destino, herencia o presagio. |
| **P-29** | A4, cap-18 | Si se atribuyen las réplicas de 18:107-125, ninguna atribución puede dar autoridad narrativa a las lecturas afirmativas; «Anota las dos» sigue siendo la última palabra; ningún resumen del narrador cierra el intercambio. |
| **P-30** | A4, cap-37 | 37:205 y 37:215 no se calientan: ni rostro, ni sollozo, ni aplauso, ni silencio «cargado», ni nadie que llore. La ilegibilidad de la sala es lo que impide que la multitud refrende la reclamación de identidad. |
| **P-20** (actualizada) | W5-W7 | Techo **agotado** para el motivo «texto presente que no se lee»: 11:155 ocupó el hueco que dejó la supresión de 14:177. Cualquier instancia nueva la exigiré suprimida. §3.4. |

## 9.3 · Observaciones de tono (no vinculantes; para A4 y A0)

1. **15:145** («El expediente conserva los ajustes, no a la persona») es la frase más tesis-adelante de la tanda. Está en registro y es breve, y la apruebo; pero es el tipo de frase que, repetida, empieza a instruir al lector. Es la única que me lo ha parecido en 1.564 palabras.
2. **15:183** («Mañana no habrá avisos.») precede a la frase de v0 que hace el mismo trabajo («Ningún canal permite preguntar a la persona qué necesitaba hoy»). Dos costes seguidos. Si A4 busca margen, ahí lo hay; desde mi gate, ninguna de las dos sobra.
3. **11:243** son siete frases de quietud antes de un «—A favor» de dos palabras. El registro es el correcto; la duración es cuestión de A4.

## 9.4 · Observación de procedimiento (a A0)

El incidente que motiva este pase —prosa comprometida en `634b6c3` sin mi lectura, por un `git add -A` mientras los escritores trabajaban— **no ha producido ningún daño en esta tanda**: los once capítulos han pasado el gate con una sola corrección de una palabra. Eso no lo convierte en aceptable. Reitero, con el peso del veto detrás: **ninguna prosa de un capítulo disparador entra en un commit antes de mi informe.** Si vuelve a ocurrir, mi respuesta será exigir la reversión del commit, no revisarlo a posteriori. Y repito la petición técnica de W4a §0.3: el modo `--diff` de `sensibilidad.py` sigue sin implementarse.

---

# 10 · Segunda lectura después de A4

**Sí, la exijo**, por B7 §2 comprobación 9 (toda inserción `INTERIORIDAD` de Jean, Maja o Alana que roce el perímetro se lee dos veces: borrador y post-A4). **No es una relectura de los once capítulos**: es un pase dirigido sobre el diff de A4, acotado a estos seis lugares y a cualquier línea que A4 toque dentro de ellos.

| Locus | Por qué |
|---|---|
| **cap-25, coda entera (216-317)** | `INTERIORIDAD` de Jean en el perímetro; 776 palabras; toda la superficie de riesgo de la tanda. |
| **cap-25:69** | El 24-nov, la causa declinada y la luz (P-21). |
| **cap-11:33 y 11:147-155** | Verificación de **C-5** aplicada; y P-23/P-24 sobre la cita y la fecha de envío. |
| **cap-19:205** | `INTERIORIDAD` de Alana contra el cristal (Ap. A §3; P-25). |
| **cap-02:159** | `INTERIORIDAD` de Jean el 26 de noviembre. |
| **cap-38 (las cuatro costuras)** | P núcleo; primera persona; adyacencia de `S38-nieve`, `S38-huella` y `S38-quedarme`. |

Además, y fuera del cupo de la segunda lectura, cualquier frase **nueva** que A4 introduzca en 18:107-125 o en 37:205/215 vuelve a mi mesa por P-29 y P-30. La mera edición de línea, no.

---

# 11 · Veredicto

| Capítulo | Veredicto |
|---|---|
| **cap-02** | **APROBADO** (literal). |
| **cap-07** | **APROBADO** (literal, supresión incluida). |
| **cap-10** | **APROBADO** (literal). Con **P-26**. |
| **cap-11** | **APROBADO CON CORRECCIONES** — **C-5** (11:33), obligatoria antes del merge. El resto, literal. Con **P-23**, **P-24** y **P-20**. |
| **cap-12** | **APROBADO** (literal). |
| **cap-15** | **APROBADO** (literal). Con **P-27** (vinculante y de máxima gravedad). |
| **cap-18** | **APROBADO** (literal). Con **P-28** y **P-29**. |
| **cap-19** | **APROBADO** (literal). La decisión de escribir I-2 sin memoria fue **correcta**. Con **C-6** sobre la orden y **P-25**. |
| **cap-25** | **APROBADO** (literal, coda R2 incluida). Con **P-21** y **P-22**. |
| **cap-37** | **APROBADO** (literal). Con **P-30**. |
| **cap-38** | **APROBADO** (literal). Núcleo intacto y verificado por hash. |

## Veredicto de la tanda: **APROBADO CON CORRECCIONES**

**Correcciones obligatorias antes del merge: dos** — **C-5** (una palabra en `cap-11.md:33`) y **C-6** (cancelar el candidato 3:199 en `ordenes/OT-19.md`). **Cero `VETO`.**

Releeré el diff corregido de C-5, comprobaré C-6 y haré la segunda lectura de §10 después de la pasada de A4. Hasta entonces, **la rama no se fusiona**.

Firmado, A7 · 2026-08-18 · sobre `w4-familia` (`0976f64`).
