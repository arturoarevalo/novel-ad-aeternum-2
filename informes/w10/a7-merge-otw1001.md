# A7 · Dictamen de merge — `OT-W10-01` sobre el texto cortado

**Fecha:** 2026-08-19. **Objeto:** `capitulos/cap-32.md` en la rama `w10-it1` (3.394 palabras), resultado de fundir `cap-31` «Interferencias» dentro de `cap-32` «Casa prestada». Ejecución de **F-7** de `a7-colocacion-otw1001.md`: *«Revisión mía sobre el texto cortado antes del merge.»*
**Estado del material:** ejecutado, sin mergear. Este dictamen decide una **prosa**, no una colocación: la colocación la decidí el 19-ago sobre la orden.

**Leído para emitirlo:** `cap-32.md` íntegro; `git show main:capitulos/cap-31.md` y `main:capitulos/cap-32.md` íntegros; `git show v0:capitulos/cap-26.md`; el diff unificado completo de la concatenación contra el fichero fundido (139 líneas); `cap-30:240-317`; `cap-34:155-172`; `cap-38:85-100`; `cap-46:160-190`; `cap-12:195-205`; `cap-20:15-70`; `cap-39:75-85`; `cap-11:425-430`; `protegidos/spans.json` y `hashes.json` completos; `biblia/b7-perimetro.md` íntegro; `biblia/b0-mapa-renumeracion.md` §W10; `informes/w10/abandonos-vF.md`; **`compilado/ad-aeternum-w10it1.md:7540-7562`**, que es la única forma de leer la costura C-1 como la lee un lector.
**Verificaciones mecánicas propias:** M9 (`10 ficheros · 133 spans íntegros`), validador de frontmatter (0 avisos), auditoría de manifiesto (79.248 palabras, en banda), censo de Kongsbakken sobre el fichero resultante, barrido de términos de riesgo sobre `cap-32` y sobre todo `capitulos/`, y comprobación de longitud de los hashes de los tres spans nuevos.

---

## 0 · Lo primero, porque cambia cómo se lee todo lo demás: el diff prueba la excisión pura

El diff unificado entre `main:cap-31` + `main:cap-32` y el fichero fundido tiene **139 líneas y contiene exactamente tres adiciones**: el dinkus de C-3, la línea acortada de E-5 y nada más. Todo lo demás son supresiones.

Eso no es una formalidad: **cierra por construcción los puntos 1, 2, 3 y 4 de la Carta.** Sin prosa nueva no puede aparecer un método, ni un sucedáneo de «Despedida», ni una causa, ni una formulación que presente el acto como solución. Toda la superficie de riesgo de esta operación es, por tanto, de dos clases y solo dos: **adyacencias que antes no existían** y **frases que quedan huérfanas de la vecina que las desactivaba**. He revisado las dos, una por una.

Y añado lo que me toca decir como revisor de **tono**, que es la mitad de mi encargo y la que menos ejerzo. De las ocho excisiones, **tres son narrador que explica lo que la escena acaba de hacer**: E-2 («El aviso no traía hechos. Ni fechas, ni conducta, ni el nombre de quien evaluaba…»), D-1 («Sin barca del centro no había forma de bajar a Sørkoppen…») y la mitad de E-5 («Salieron el lunes, con la cuenta escolar cerrada, un aviso al centro y el encargo del domingo autorizado el mismo lunes»). Ninguna de las tres es del autor: son nuestras. Y las tres hacen lo que `v0` no se permite jamás en los capítulos 4, 9, 23 y 40, que son mi referencia de contención: recapitular al lector lo que acaba de leer. **E-5 no es una excisión: es una restitución.** He comprobado el literal contra `v0:cap-26:12` y la frase que queda —«El seguimiento y la retención bastaban.»— es la del autor, palabra por palabra.

Llevo once oleadas diciendo que no a adiciones. Cuando una resta va en la dirección correcta hay que decirlo con la misma claridad: **en el eje de tono, esta operación acerca el capítulo a `v0`, no lo aleja.**

---

## 1 · Tabla de hallazgos

Números para localizar; **manda la cita**. Todos los `cap-32:NN` son del fichero fundido.

| # | Dónde | Cita literal | Punto afectado | Gravedad | Propuesta mínima |
|---|---|---|---|---|---|
| M-1 | `cap-32` completo | — | Carta 1 · 2 · 3 · 4 | **sin hallazgo** | El diff es excisión pura verificada. Sin prosa nueva no cabe infracción de contenido. |
| M-2 | `cap-32:229` (**F-4**) | «—Ha llegado otra vez.» | R1 (por la vía de la reparación) | **sin hallazgo** — resuelto | Aprobada la salida por excisión. Ver §2. |
| M-3 | `cap-32:237` | «—La segunda es de las once cincuenta y ocho.» | R1 | **sin hallazgo** | Sostenida por «—Enséñame las dos.» en la misma escena. F-4 sigue vigente: **ninguna reparación se escribe**. |
| M-4 | costura **C-3**, `cap-32:287-295` | «Cruzaron el puente de Tromsøya…» · «—¿Cuánto tiempo? —preguntó Nora.» · dinkus · «La tercera bolsa se quedó en el maletero.» | **R1** (el trayecto no crece) | **sin hallazgo** — aprobada la desviación | Ver §3. La colocación con D-3 dentro es **mejor** que la que aprobé, y explico por qué. |
| M-5 | costura **C-1**, `cap-30:317` → `cap-32:15` | `ASIGNACIÓN · APELACIÓN` → «La boya retirada seguía en el banco del taller del Framsenteret, con la carcasa abierta y el sensor de referencia envuelto en un paño.» | R4 (rimas) | **vigilar** (confirmado sobre el compilado) | Ninguna acción obligatoria. Arreglo de coste cero preautorizado y disparador escrito: §4. |
| M-6 | `protegidos/spans.json`, `S-w10-ducha` | `fin`: «—Respuesta correcta.» | **Carta 6 · F-2 · F-6** | **corregir** | **C-1**: el `fin` debe ser «Al cabo de pocos minutos, la muchacha se durmió por primera vez en una semana sin rondar por las habitaciones.» Ver §5.1. Es la infra-implementación que más pesa. |
| M-7 | `protegidos/spans.json`, `S-w10-mananas-34` | `fin`: «—No hace falta todas.» | K-3 · R6 | **corregir** | **C-2**: `fin` = «—Anotado —dijo Jessie.» (`cap-34:167`, que es lo que ordené). |
| M-8 | `biblia/b7-perimetro.md:124` | «**`cap-32:27`** —la ducha, la aspiración rota oída desde fuera…» | R6 (puntero) | **corregir** | **C-3**: `cap-32:27` hoy resuelve a una línea **real y distinta**. → `cap-32:307` **+ span `S-w10-ducha`**. |
| M-9 | `biblia/b7-perimetro.md:119` | «…no trae remedio (`cap-12`, `cap-20`, `cap-31`)» | R6 (puntero) | **corregir** | **C-4**: `cap-31` es un fichero que ya no existe. → `cap-32`. |
| M-10 | `biblia/b7-perimetro.md:282` | «### P-41 · Kongsbakken» dentro de «## 8b · **Seis** condiciones añadidas el 2026-08-19» | K-4 (forma) | **corregir** | **C-5**: promover a `## 8c`. P-41 no es una de las seis: es de W4-R, se perdió una vez y no puede volver a diluirse en un recuento. |
| M-11 | `protegidos/spans.json`, `S-n4-escena3` | `desc` termina en «…Tras la operación de » | — (metadato) | **corregir** | **C-6**: preexistente en `main`, no lo introduce esta operación. Cerrar la frase o retirarla **dejando constancia de que se perdió**. Ver §5.4. |
| M-12 | `cap-32:307-321` | la ducha, tras la fusión | Carta 6 · 7 · R5 · R6 · **F-6** | **vigilar** | Nada conecta la ducha con los papeles del día. Verificado línea a línea. Condición nueva de alcance, §6. |
| M-13 | `compilado/ad-aeternum-w10it1.md` | — | método (Carta 1, orden del bucle) | **vigilar** | Compilado **antes** de mi veredicto. Dentro de la letra; fuera del orden del bucle de W10. §7. |
| M-14 | `cap-30:247`, `:249`, `:283`, `:301-303`, `:307-315` | A-01 … A-05 | R2 hueco 1 · R4 | **sin hallazgo** | Verbatim, en su línea original. `cap-30` no se tocó. Análisis del adelgazamiento probatorio en §5.5. |
| M-15 | `cap-32:213-241` | el bloque de los cuatro documentos | `S-n4-caja` · `cap-38:93` | **sin hallazgo** | Verbatim salvo F-4, que autoricé. **`cap-38:93` está pagado íntegro sobre el texto cortado.** §5.6. |
| M-16 | `cap-32:25`, `:161`, `:169-171` | el aparato de anonimato del 3 de enero | R7 §5 · P-64 | **sin hallazgo** | Pierde un locus (`responsable desconocido`) y conserva cuatro, tres bajo hash. §5.7. |

---

## 2 · F-4 · la primera desviación: se resolvió por excisión y **está bien resuelta**

**Aprobada, y con un margen que no esperaba.**

F-4 no prohibía arreglar el antecedente: prohibía **escribirlo sin pasar por mí**, porque el arreglo barato —Nora contando en la cocina lo que pasó en el instituto— reinstala lo cortado y convierte a la menor en expositora. A0 no ha escrito nada. Ha quitado cuatro palabras. Eso es exactamente lo que pedí y lo apruebo sin condiciones.

Lo he verificado leyendo la escena entera. La réplica queda anclada por dos sitios, no por uno:

- **`cap-32:217`**, dos párrafos antes: «La habían impreso en el instituto **antes de que la cuenta se cerrara otra vez**.» — el «otra vez» de Nora tiene su antecedente literal ahí.
- **`cap-32:233`**: «—No puedo imprimir nada —dijo Nora—. Ni entrar. **La captura de esta mañana la hizo la tutora.**» — ocho palabras que llevan encima la escena suprimida entera, y la llevan sin que ninguna menor exponga nada.

Y hay un efecto colateral que conviene dejar escrito porque nadie lo buscaba: **la excisión resuelve una contradicción horaria que `main` tenía y que nadie había visto.** En `main`, la escena 1 fechaba el segundo aviso a las **once cincuenta y dos** (`cap-31:31`) y la cocina decía «La segunda es de las once cincuenta **y ocho**» (`cap-32:237` de hoy). Después del corte solo queda una hora en todo el libro y no hay con qué contradecirla. La operación deja el capítulo **más limpio** de lo que estaba.

**F-4 se mantiene vigente en su parte prohibitiva**, y quiero que quede claro para el que venga: si en alguna pasada futura A5, A4 o un auditor reporta que «—La segunda es de las once cincuenta y ocho» va sin apoyo, la respuesta **no** es escribir el apoyo. Es venir a mí. La frase está sostenida por «—Enséñame las dos.» dentro de la misma escena, y por la lógica de toda la escena, que consiste en anotar la hora de cada papel para Astrid.

---

## 3 · C-3 con D-3 dentro · la segunda desviación: **mejor que la que aprobé**

**Aprobada, y sin reservas.** Lo digo así porque la desviación se me somete honestamente y merece una respuesta que no se esconda.

El lector lee ahora:

> Cruzaron el puente de Tromsøya a las cinco menos veinte. Hasta la casa baja del Lyngen quedaban dos horas de carretera y un desvío sin salar.
> —¿Cuánto tiempo? —preguntó Nora.
> —Ropa para una semana —dijo Maja—. Y el cuaderno.
> `* * *`
> La tercera bolsa se quedó en el maletero.

Mi preocupación (F-1, R1) era que dos horas de carretera de invierno, de noche, hacia la ribera del Lyngen —cuyo primer tramo es el trayecto de Jean— pasaran de ser una **frontera de capítulo** a un **hueco interno**, porque un hueco entre capítulos no lo rellena nadie y un hueco dentro de un capítulo es una escena que falta. Contra eso pesan tres cosas, y las tres juegan a favor de la versión que se me somete:

1. **El trayecto no crece ni una palabra.** El único dato de carretera del pasaje —«a las cinco menos veinte», «dos horas de carretera y un desvío sin salar»— es idéntico al de `main`. Las dos réplicas no añaden kilómetro, hito, hora ni paisaje. **R1 intacta.**
2. **El hueco queda ocupado por una pregunta sin respuesta.** «—¿Cuánto tiempo?» pregunta *duración* y Maja contesta *equipaje*. Lo que el dinkus se traga no es carretera en blanco: es una pregunta que nadie contesta, que es el registro propio de este libro —«—¿Cuándo acaba lo mío? / —No lo dice. / —¿Y quién decide cuándo acaba? / —Tampoco lo dice.», doce líneas antes, en el mismo capítulo—. Y esto es lo que de verdad importa: **un hueco ocupado es más difícil de rellenar que un hueco vacío.** Quien quisiera escribir la carretera tendría que pisar una pregunta sin contestar y estropearla para hacerlo. La versión que yo aprobé dejaba el hueco limpio, y un hueco limpio invita.
3. **El hash lo cierra.** He comprobado la longitud de `S-w10-costura-c3`: **276 caracteres**, es decir, el span cubre la frase del puente, **las dos réplicas de D-3, el dinkus** y la frase de la tercera bolsa. La ocupación del hueco está bajo llave, no bajo promesa. Y el `desc` deja escrito *por qué*, que es lo único que sobrevive a un año.

Sobre la conservación de D-3 en sí, contra la recomendación de A2: no tengo objeción de Carta y tengo una observación a favor. En `R6` la prueba es si la menor es una adolescente en duelo y no un adulto pequeño ni un símbolo. Nora preguntando «¿cuánto tiempo?» y recibiendo por respuesta qué meter en la bolsa es una niña de quince años haciendo una pregunta de niña y una madre contestando lo único que sabe. Es material doméstico sin función, y ese era el diagnóstico. No lo firmo como acierto de estructura —eso no es mío—, pero **como retrato de menores es correcto**.

**Condición implícita, ya cubierta por el hash y la enuncio para que se lea:** el contenido de esa elisión no crece. Ni una tercera réplica entre el puente y el dinkus. Quien lo intente romperá `S-w10-costura-c3` y vendrá a mí, que es justo lo que F-1 buscaba.

---

## 4 · C-1 · leída sobre el compilado, como corresponde

Dije que en una costura se lee la imagen y no el diccionario, y que la leería sobre el texto cortado. La he leído en `compilado/ad-aeternum-w10it1.md:7550-7560`, que es la única forma honesta de hacerlo, porque ahí está el encabezado de capítulo que un fichero `.md` de trabajo no enseña:

> El campo se llena.
> `VENTANA REFLEXIVA · CERRADA`
> `ASIGNACIÓN · APELACIÓN`
>
> **## 31. Casa prestada**
>
> La boya retirada seguía en el banco del taller del Framsenteret, con la carcasa abierta y el sensor de referencia envuelto en un paño.

**Veredicto: `vigilar`. No pido la transposición.** Cuatro razones, y la tercera no la tenía el 19-ago por la mañana:

1. **El amortiguador es real y es doble:** número de capítulo y título. Y el título es **una casa prestada**, no un final.
2. **La imagen no dice ninguna de las cosas prohibidas.** Una boya retirada con la **carcasa abierta** es un trabajo **sin terminar**. `ASIGNACIÓN · APELACIÓN`, la línea inmediatamente anterior, dice lo mismo: esto no ha acabado, esto sigue en trámite. Lo que `Carta 4` y `R4` prohíben es descanso, solución, cierre, lógica o premio. Aquí no hay cierre por ningún lado: hay dos cosas abiertas, una encima de otra.
3. **El registro «carcasa abierta / envuelto» ya está codificado en este libro, y está codificado en caliente.** `cap-39:79`: «vio a Jean arrodillada ante **la carcasa abierta**, muchos inviernos atrás. Las gemelas, **envueltas en mantas**, se empeñaban en alcanzarle tornillos que no necesitaba. Jean se había quedado hasta que los radiadores calentaron.» Y antes, `cap-11:427`: «Maja abrió el armario, **miró la carcasa** y volvió a cerrarlo.» En esta novela una carcasa abierta es **cuidado y mantenimiento**, y el lector se encuentra la primera a treinta y tantas páginas de esta costura. La ternura de «envuelto en un paño» —que es la única palabra del pasaje que podía pesar— tira hacia ahí, no hacia un sudario.
4. **Y la fusión mejora esta costura.** Hasta hoy, lo que seguía a `ASIGNACIÓN · APELACIÓN` era un capítulo titulado **«Interferencias»**, colocado inmediatamente después de una banda de cómputo que se estrecha sin avisar. Ese título sí ofrecía una lectura —que a la ventana de Jean *la interfirieron*— y llevaba diez oleadas ahí sin que nadie, yo incluido, lo mirara. **Se ha ido con el corte, y es una ganancia neta de `R4` que la orden no reclamaba.**

**Arreglo preautorizado, para que nadie tenga que inventarlo con prisa.** Si en alguna campaña futura un lector frío o un beta nombra este paso —la boya, la costura con el cierre del `cap-30`, «demasiado fúnebre», «la imagen del final del 30 se prolonga»— **ejecútese sin volver a consultarme** la transposición de las dos primeras oraciones del párrafo, de modo que el capítulo abra así:

> Maja llevaba desde las nueve pasando la serie de diciembre a un archivo aparte. La boya retirada seguía en el banco del taller del Framsenteret, con la carcasa abierta y el sensor de referencia envuelto en un paño. A las doce y veinte, cumplimiento la llamó por el interfono del laboratorio.

Cuesta cero palabras, no toca prosa del autor (el párrafo es nuestro, de W3) y pone a una mujer viva trabajando desde las nueve donde ahora hay un instrumento. **Queda autorizado por adelantado y solo con ese disparador.** No lo pido hoy porque la operación tiene además un valor de método que no quiero estropear: al no cambiar una sola palabra de orden, cualquier movimiento de puntuación en la próxima campaña es atribuible a la estructura y a nada más. Una corrección que no necesito no vale ese precio.

---

## 5 · Las anclas y lo que había que revisar después aunque no se le tocara una letra

### 5.1 · `S-w10-ducha` se queda corto, y es la corrección que más pesa · **C-1**

F-2 ordenaba un span de «Nora subió con el cuaderno pautado bajo el brazo…» **a «Al cabo de pocos minutos, la muchacha se durmió por primera vez en una semana sin rondar por las habitaciones.»** Lo implementado termina en «—Respuesta correcta.» (663 caracteres). Fuera del hash quedan:

> Aslak señaló la escalera con la barbilla. Jessie subió. **Al cabo de pocos minutos, la muchacha se durmió por primera vez en una semana sin rondar por las habitaciones.**

Esa frase **no es el epílogo de la escena: es su dispositivo de seguridad**. En mi dictamen de colocación escribí, sobre por qué la fusión no daña el punto 7: *«el texto de hoy se resiste solo —nadie pregunta, nadie explica, y "se durmió por primera vez en una semana" apunta a la semana y no al día»*. Es la única línea del capítulo que **desactiva la causa próxima**. Sin ella, el llanto de Jessie queda a un párrafo de los papeles del día y a merced de la línea de más que alguien añadirá para «unir el capítulo»; con ella, el libro dice que lo que la tiene sin dormir lleva una semana y no una tarde. Y «rondar por las habitaciones» es duelo, no burocracia.

Dejarla fuera del hash mientras se protege lo que la precede es proteger la escena y descubrir su seguro. **Obligatoria: `fin` = «Al cabo de pocos minutos, la muchacha se durmió por primera vez en una semana sin rondar por las habitaciones.»**

### 5.2 · `S-w10-mananas-34` también se queda corto · **C-2**

K-3 decía `cap-34:159-167`, y citaba el extremo: «—Anotado —dijo Jessie.» Lo implementado termina en `:165` («—No hace falta todas.»). Queda fuera precisamente la réplica que **la próxima pasada de línea llamará redundante**, que era el motivo declarado del span. Y no es un adorno: «—Anotado» es una chica de dieciséis años contestando en el idioma administrativo que le ha entrado por ósmosis, once capítulos después de decirle a su madre «**Tú ya hablas igual que ellos**» (`cap-32:145`). Es `R6` en dos palabras. **Obligatoria: `fin` = «—Anotado —dijo Jessie.»**

### 5.3 · Dos punteros muertos en mi propia biblia · **C-3 y C-4**

- `b7-perimetro.md:124` cita la ducha como **`cap-32:27`**. Tras la fusión, `cap-32:27` es una línea **real y distinta** («—La lista de distribución incluye a la entidad empleadora de la persona evaluada…»). Un puntero roto se nota; **un puntero que resuelve a otra cosa plausible no se nota nunca**. → `cap-32:307`, y añádase **`(span `S-w10-ducha`)`**, para que a partir de ahí el puntero no dependa de un número de línea.
- `b7-perimetro.md:119` cita, en los ejemplos de `R6`, «(`cap-12`, `cap-20`, `cap-31`)». `cap-31` **no existe**. → `cap-32`. La afirmación sigue siendo verdadera: «—No puedo imprimir nada… Ni entrar.» sigue en página.

El mapa de capítulos de `§2` **sí** se actualizó (línea 41 ya lee `cap-32` → **31. Casa prestada** y no menciona `cap-31`). Se actualizó el índice y se olvidaron las dos citas. Es el mismo modo de fallo de siempre, dos días después de que me costara una condición entera.

### 5.4 · P-41 y un `desc` truncado · **C-5 y C-6**

**K-4 está bien hecha en el fondo.** El censo corregido es el mío, los seis loci están, `cap-03:143` está incluido con la anotación de que no lleva la palabra, los dos suprimidos están tachados y trazados a la OT, y el párrafo de encabezamiento dice sin adornos que la regla se perdió y por qué. Es mi regla y está redactada como mía. La firmo.

**La forma tiene un defecto y no es cosmético.** P-41 cuelga como `###` dentro de «`## 8b · **Seis** condiciones añadidas el 2026-08-19, tras las cuatro intervenciones de personaje». P-41 no es una de esas seis: es del 18 de agosto, es de W4-R, y su historia entera es que **ya se disolvió una vez dentro de una consolidación**. Quien lea ese documento dentro de un año y cuente encontrará siete cosas bajo un título que dice seis, y la que sobra es la que se perdió antes. **Promuévase a `## 8c · P-41 · Kongsbakken (reincorporada…)`.** Un carácter.

**Y una cosa que no introduce esta operación pero que estoy obligado a nombrar porque estoy delante:** el `desc` de `S-n4-escena3` termina literalmente en «**…Tras la operación de** ». Frase cortada a media palabra, e idéntica en `main`: viene de antes. Es el defecto exacto que produjo F-5 y el que produjo K-4: **una condición escrita a medias en el sitio donde vive la condición.** No he podido reconstruir qué decía. **Ciérrese la frase o retírese el fragmento, y en el segundo caso déjese escrito que se truncó en origen y que el contenido perdido no se ha podido reconstruir.** Un `desc` incompleto que no avisa de que lo está es peor que uno corto.

### 5.5 · A-01 … A-05 tras el adelgazamiento probatorio

`cap-30` no se ha tocado —no aparece en el diff de la rama— y he verificado los cinco literales en su línea original: `:247` «Cuatro consultas, cuatro campos sin destinatario.» · `:249` «La banda no la devuelve.» · `:283` «El recuerdo no cabe en la enumeración.» · `:301-303` «Los repite igual. No cierran nada.» · `:307`→`:315` «La banda se estrecha por el lado derecho. No avisa.» → `VENTANA REFLEXIVA · CERRADA`. M9 lo confirma.

Mi aviso del 19-ago era que **cortar capa probatoria sube el peso relativo de lo que queda**. Lo he vuelto a mirar con el texto delante y el aviso, en este caso, **no se materializa**, por una razón concreta: lo cortado está **detrás** de las anclas, no delante ni alrededor. El equilibrio interno del `cap-30` es idéntico y su contexto previo también. Lo único que cambia es qué recibe al lector al salir: antes, una chica viva delante de un terminal; ahora, un instrumento. Eso es C-1, ya resuelto en §4, y no toca A-05.

Sí queda una consecuencia menor y la anoto para que nadie la «restituya» luego como textura: con E-4 desaparece «Nora apagó el calentador y cerró el paso del agua, **como en octubre**», y era el último gesto doméstico del libro **fechado en el mes anterior al 26 de noviembre**. Su pérdida es favorable a `R1` y no se repone.

### 5.6 · El bloque que sostiene a la vez `S-n4-caja` y `cap-38:93`

Comparado línea a línea contra `main:cap-31:283-311`: **verbatim, salvo las cuatro palabras de F-4**, que autoricé. `S-n4-caja` íntegro (781 caracteres, M9 OK) y sin cambio de vecino.

Y el que me importaba: **`cap-38:93` está pagado entero sobre el texto cortado.** Lo he verificado componente por componente:

| lo que `cap-38:93` afirma | dónde se paga hoy |
|---|---|
| «Tres actuaciones automáticas sobre los accesos de una familia» | la cuenta de Nora (`cap-32:217`, `:233`), el aviso al Framsenteret (`:23-27`), el encargo autorizado (`:133-141`) |
| «una queja formal de un centro de investigación» | `cap-32:39` «Ya lo he registrado como queja.» |
| «un expediente policial cerrado con una autorización posterior» | `cap-32:133-141`, `ENCARGO AUTORIZADO · REVISIÓN CERRADA` con la hora del tres de enero |
| «**cuatro** documentos incorporados por la autoridad de supervisión» | `cap-32:239-241`: «colocó la hoja del instituto **la cuarta** en la fila» → «**Recibido. Cuatro documentos del 3 de enero.**» |

**Ninguna cifra del `cap-38` necesita tocarse.** Queda confirmado sobre el texto lo que sostuve sobre la orden, y queda retractada, ahora con prueba, la tabla de `informes/w5-cap-n4.md` §4 que decía lo contrario y que su propio autor ya había retirado en §14 sin corregirla.

### 5.7 · El aparato de anonimato (P-64), que era el riesgo silencioso de E-1

Este es el que no estaba en la lista de nadie y por el que fui a mirar. La escena 1 contenía uno de los loci de **P-64**: «En el apartado de origen puso `responsable desconocido`.» Se ha ido con ella. Censo después del corte:

| locus | dónde | estado |
|---|---|---|
| `No consta responsable individual.` (origen 1) | `cap-32:25`, el aviso del Framsenteret | vive |
| `No consta responsable individual.` (origen 2) | `cap-32:161`, **leído en voz alta por Jessie** | vive · span `S-n4-escena3` |
| la pregunta de Jessie sin respuesta | `cap-32:169-171` «—¿Y les sale la misma frase?» → Maja tiende la mano | vive · span `S-n4-escena3` |
| P-49 | `cap-32:105` «escribió algo corto y no lo leyó en voz alta» | vive · span `S-n4-p49` |
| «El resumen no tenía autor.» | `cap-38:93` | vive · span `S32-resumen` |
| ~~`responsable desconocido` (3-ene)~~ | ~~escena 1~~ | suprimido |

Quedan **cinco loci, cuatro de ellos bajo hash**, con la figura repartida en dos documentos de origen distinto y una pregunta que nadie contesta. Y `responsable desconocido` **no desaparece del libro**: sigue en `cap-12:201`, que es su origen, en el cuaderno de Nora del cinco de diciembre. Lo que se pierde es un eco, no el asidero. **`R7 §5` —el ordenante del sabotaje— se sostiene sobrado.** Confirmo mi H-9: bajar saturación no es nunca infracción.

### 5.8 · Kongsbakken sobre el fichero resultante, y el resto de las verificaciones de F-7

`grep` sobre `capitulos/` tras el corte: **tres apariciones de la palabra** (`cap-10:73` cargada, `cap-22:149` neutra, `cap-46:167` neutra) más `cap-03:143`, que es el mismo asidero sin la palabra. **Cuatro loci, exactamente el censo de P-41.** Ninguna voz con autoridad cierra la pregunta, ni en positivo ni en negativo; Jean y Kongsbakken no comparten frase; nadie recuerda la discusión cuando la palabra aparece. `R3`, `R7 §1` y P-41 intactas.

Y el resto de lo que F-7 me obligaba a comprobar, todo confirmado sobre el texto:

- **Nadie ha escrito una transición.** El diff lo prueba: no hay una sola línea de prosa nueva.
- **Los cuatro `S26-*`** (lata, paso-uso, asociación, bocana) sin contacto; **los tres `S-n4-*`** re-apuntados al fichero fundido, íntegros y sin cambio de vecino. **M9: 10 ficheros · 133 spans.**
- **`R6`, salvaguarda de POV:** con la escena 1 desaparece la única cabeza de quince años del capítulo, y eso ya lo di por perdido en §4 de mi dictamen anterior. He vuelto a verificar el salvaguarda sobre la rama: **Nora conserva POV completo en `cap-34`, `cap-37`, `cap-43`, `cap-46` y `cap-48`; Jessie en `cap-41`.** Y en el capítulo fundido Nora sigue teniendo «—Puedo. No quiero.», las dos rayas verticales sobre el pentagrama y el último peldaño con su madre sentada al lado en silencio. Pierde interioridad, no presencia.
- **`F-6` sobre el texto cortado:** ninguna línea —narración, réplica ni acotación— conecta la ducha con los papeles del día, ni le atribuye causa. Maja no piensa, no dice y no anota por qué llora su hija. Cumplido.
- **Barrido de términos de riesgo sobre `cap-32`:** ni un hit de método, medio, «por qué», culpa, paz, descanso, liberación, lógica, «decidió irse», «se fue», «Despedida», carta ni nota. Lo único adyacente es el techo ontológico de `:343-351` —«dijo que no era toda Jean», «—¿Era Jean? … —Todavía no tengo un nombre para ninguna de las dos.»—, que es prosa de `v0`, está intacto y **no sube de «No toda»**; y `:401`, «A Jean le hicieron otra cosa», que es `R8` —la negativa expresa a la parábola— bajo span `S26-paso-uso`.
- **Frontmatter:** `pov: Maja → Jessie → Maja` es correcto tras el corte. Validador, 0 avisos. Manifiesto: 79.248 palabras, dentro de la banda.

---

## 6 · Una condición nueva, y sale de leer el capítulo entero de un tirón

No la había visto sobre la orden porque solo se ve con el texto delante. La escribo aquí porque es exactamente la clase de cosa que se pierde.

**La ducha de Jessie es hoy el beat que está más lejos del comienzo de su capítulo en todo el libro.** Vive en el último tercio de una unidad de **3.394 palabras**, la más larga del libro, y la primera mitad de esa unidad es el material que **los tres críticos fríos nombraron como su punto de abandono** (`informes/w10/abandonos-vF.md`: capítulo 31, tres nominaciones, la única de las nuestras que falla el criterio). `S-w10-ducha` protege la escena. **Nada protege que se llegue a ella.**

Y la reacción refleja, si la próxima campaña vuelve a marcar el 31, será acortar. La mitad administrativa está ya podada; la que queda gorda es la del Lyngen.

**Condición permanente (`R6` · `Carta 6` · `Carta 7`):** cualquier intervención futura que **reduzca la proporción de lectores que llegan a la ducha** —acortar la segunda mitad del `cap-32`, mover la escena a un capítulo posterior, partir el capítulo dejándola en el fragmento de después, o cortar el tramo que va de la llegada a la casa baja hasta «—Respuesta correcta.»— **pasa por mí antes de escribirse**. Si el capítulo 31 tiene que volver a encoger, **encoge por delante, por la mitad administrativa, nunca por la del Lyngen**. `b7-perimetro.md R6` llama a esta escena «el modelo del libro para el punto 7 y para el 6 a la vez»; un modelo al que no llega el lector no modela nada.

Y a quien vea que la fusión metió el peor capítulo de la novela delante de su mejor escena de duelo: sí, eso es lo que ha pasado, y es el argumento **a favor** de la fusión, no en contra. El capítulo que terminaba en «—Ropa para una semana» ahora termina en una casa prestada donde a una chica se le permite llorar detrás de una puerta sin que nadie le pregunte. Lo que hay que vigilar es que nadie pague ese final con las tijeras.

---

## 7 · Una nota de método, corta

`compilado/ad-aeternum-w10it1.md` existe en la rama y contiene el capítulo fundido: **el manuscrito se compiló antes de mi veredicto.** No hay infracción de `Carta 1`: el texto compilado no contiene nada prohibido, y de hecho apruebo. Pero el bucle de W10 dice *intervención → verificación (A5, **A7 si toca su perímetro**) → remedición*, y aquí la remedición se preparó antes de la verificación.

Si yo hubiera vetado, ese fichero sería **material de trabajo con contenido vetado**, y `Carta 1` obliga a que no exista. Compilar es barato; deshacer una campaña de puntuación sobre texto no aprobado, no. **En las iteraciones que toquen el perímetro: gate primero, compilado después.** No pido nada sobre lo ya hecho.

---

## 8 · Correcciones obligatorias antes del merge

Ninguna cuesta una palabra de prosa. Dos son extremos de span; cuatro son metadatos y biblia.

| # | Fichero | Qué | Por qué |
|---|---|---|---|
| **C-1** | `protegidos/spans.json` | `S-w10-ducha`: `fin` → «Al cabo de pocos minutos, la muchacha se durmió por primera vez en una semana sin rondar por las habitaciones.» | F-2 tal como se ordenó. Es la frase que apunta el sueño **a la semana y no al día**: el único desactivador de causa próxima que tiene la escena. §5.1 |
| **C-2** | `protegidos/spans.json` | `S-w10-mananas-34`: `fin` → «—Anotado —dijo Jessie.» (`cap-34:167`) | K-3 tal como se ordenó. La réplica que una poda llamará redundante, y es `R6` en dos palabras. §5.2 |
| **C-3** | `biblia/b7-perimetro.md:124` | `cap-32:27` → `cap-32:307`, y añadir «(span `S-w10-ducha`)» | Hoy resuelve a una línea real y distinta. Un puntero equivocado que parece bueno no lo detecta nadie. §5.3 |
| **C-4** | `biblia/b7-perimetro.md:119` | `cap-31` → `cap-32` en los ejemplos de `R6` | Apunta a un fichero que ya no existe. §5.3 |
| **C-5** | `biblia/b7-perimetro.md:282` | P-41 pasa de `### …` dentro de `## 8b` a sección propia `## 8c` | P-41 no es una de las «seis condiciones del 19-ago»; es de W4-R y **ya se disolvió una vez** dentro de una consolidación. §5.4 |
| **C-6** | `protegidos/spans.json` | `S-n4-escena3`: cerrar el `desc` truncado en «…Tras la operación de », o retirar el fragmento **dejando escrito que se truncó en origen y no se ha podido reconstruir** | Preexistente en `main`, no lo introduce esta operación. Es el modo de fallo que produjo F-5 y K-4, en el mismo fichero. §5.4 |

Tras aplicarlas: `proteger.sh baseline` (aditivo para spans nuevos; `--rebaseline --gate "W10: A7 C-1/C-2 sobre OT-W10-01"` si se alteran los existentes) y `proteger.sh verificar`. **No hace falta un nuevo gate mío:** los seis literales están escritos arriba y son verificables por A5 y por M9 sin criterio.

**Vigilar, sin acción hoy:** C-1 la costura de la boya (arreglo preautorizado y disparador en §4) · la ducha al final del capítulo más largo (condición permanente, §6) · el orden gate/compilado (§7).

---

## 9 · Veredicto

# APROBADO CON CORRECCIONES · MERGE AUTORIZADO

**Sobre el texto fundido: sí, merge**, una vez aplicadas C-1 … C-6, que son seis ediciones de metadatos y biblia y ninguna palabra de prosa.

**Sobre las dos desviaciones que se me someten: las dos aprobadas, y las dos son mejores que lo que yo había autorizado.** F-4 se resolvió por excisión y no por reparación, que era literalmente lo que exigí, y además le quita al libro una contradicción horaria que arrastraba desde W3. C-3 con D-3 dentro deja la elisión del trayecto **ocupada por una pregunta que nadie contesta y cerrada por un hash de 276 caracteres**, y un hueco ocupado se rellena peor que un hueco limpio. Que A0 me someta expresamente una colocación distinta de la aprobada, señalándola, es exactamente el procedimiento que pedí en `§5.2` y el que hace que este perímetro funcione.

**Sobre C-1: `vigilar`, sin corrección.** La he leído sobre el compilado, con el encabezado en medio. La imagen no dice descanso ni final: dice una carcasa abierta encima de una apelación, dos cosas sin terminar, una sobre otra. Y el registro «carcasa abierta / envuelto» ya está codificado en esta novela como cuidado —Jean arrodillada ante la caldera con las gemelas envueltas en mantas—, no como mortaja. Dejo el arreglo de coste cero preautorizado con su disparador para que nadie tenga que inventarlo con prisa.

**Sobre las anclas: ninguna se ha movido, ninguna se ha debilitado.** A-01…A-05 verbatim en `cap-30`, que no se tocó. El bloque de los cuatro documentos verbatim, y `cap-38:93` pagado íntegro sobre el texto cortado, comprobado componente por componente. Los tres `S-n4-*` re-apuntados e íntegros; los cuatro `S26-*` sin contacto. El aparato de anonimato pierde un eco y conserva cinco loci, cuatro bajo hash.

**No hay veto, y digo otra vez por qué no lo hay.** Lo que se ha ejecutado no le pide al libro que sepa nada. No abre «Despedida», no fecha nada dentro de la elipsis, no da causa, no da descanso, no clasifica un silencio, no sube de «No toda», no toca el trayecto y no le pone nombre a nadie. Le ha quitado 546 palabras, y tres de las ocho supresiones son narrador explicando lo que la escena acababa de hacer — que es justo lo que la contención de `v0` no se permite nunca. **Es la segunda vez en once oleadas que una intervención va a favor de la veta del perímetro, y la primera en que además va a favor del tono.**

*Nota final, y va para quien venga cuando yo no esté. En dos días he encontrado tres condiciones mías escritas a medias o apuntando a un sitio equivocado: P-41, que había desaparecido entera; dos punteros de `b7-perimetro.md` que hoy resuelven a otra cosa; y un `desc` que se corta a media palabra y que llevaba así desde W5. Ninguna de las tres la rompió nadie: se rompieron solas, por movimiento del suelo. La lección no es que haya que revisar más informes. Es que **una condición que vive en un número de línea está muerta en cuanto alguien corta un párrafo por encima**, y que las únicas que han sobrevivido a once oleadas son las que están atadas a un literal que se rompe al tocarlo. Por eso las seis correcciones de hoy no piden que nadie recuerde nada: cambian un hash, un puntero y un título. **Escríbase la condición donde se rompa, no donde se lea.***

**A7 · 2026-08-19 · sobre `capitulos/cap-32.md` en `w10-it1`, antes del merge a `main`.**
