# Panel de jueces · W10 iteración 0 · JUEZ A

**Disposición declarada: conservador del libro.** La carga de la prueba recae íntegra sobre quien propone tocar. Un manuscrito que puntúa 8,5 tiene más que perder que que ganar, y seis oleadas sin mover cuatro ejes son evidencia de algo, no solo falta de puntería.

**Lo que hice antes de opinar.** Conté yo. Leí la Parte III entera (25–36) más los capítulos 1, 5, 42 y los tramos citados de 34, 35, 40. Y leí **una cosa que los seis ángulos tenían prohibida y que resulta decisiva: el registro de dónde dicen los lectores fríos que dejaron de leer.**

---

## 0 · Lo que verifiqué, y las siete correcciones que salieron

**Mi recuento** (cuerpo de `capitulos/cap-01…48.md`, sin frontmatter): **80.302 palabras, 48 capítulos.**
**Partes: 19.986 / 20.458 / 20.300 / 19.558** (24,9 / 25,5 / 25,3 / 24,4 %). Diferencia mayor–menor: **900 palabras, 1,1 %.**
**Capítulos: mín. 705 · máx. 2.312 · media 1.673 · mediana 1.748 · desviación 395 · coeficiente de variación 23,6 % · IQR 1.469–1.880.**

**El metrónomo es real y queda confirmado por tercera vez independiente.** Lo demás no sobrevivió igual de bien.

| # | Cifra de un ángulo | Lo que cuenta el texto | Consecuencia |
|---|---|---|---|
| **1** | Ángulo 5: «**441 palabras domésticas** en 31.800» | La apertura de `cap-34` (ferry + Co-op + coche, hasta «Koppangen desapareció de la pantalla») mide **619 palabras**, no 325. La ducha de `cap-32` mide **145**, no 116. Y `cap-28` entero (1.856) es una familia en su salón alrededor de un piano. Suelo honesto: **764 sin contar el 28; 2.620 contándolo.** | El **diagnóstico sobrevive** (el libro deja de ser novela familiar en el 55,7 %); **el titular que lo hace urgente es falso por un factor de 3 a 6.** P-1 se apoya en el titular. |
| **2** | Ángulo 3: «la letanía de los cuatro nombres tiene **solo dos instancias, y las dos están en 7 y 8**» | Cuatro loci: `cap-07:33` (la lista), `cap-08:55` (**la regla**: «Al final de cada serie repite cuatro nombres en el mismo orden»), `cap-08:281`, y **`cap-30:301`, que es su pago**: «Al terminar cada serie Jean repite cuatro nombres. Aquí no hay serie que terminar. / Los repite igual. No cierran nada.» | **C1 (suprimir el cap. 8) deja huérfano el mejor remate del cap. 30.** Un audit de corte que hace `grep` de sustantivos (zueco, andador, cuartilla) **nunca ve una regla**. |
| **3** | Ángulo 6: «el único personaje cuya función entera es el peligro **nunca hace daño donde se pueda ver**» | Falso, y la cadena está en `cap-42` literal: Jean sostiene apelaciones para contener a Cuchillo → «**Sola no basta.**» → Nieve abre su ruta para cubrirla → «`PÉRDIDA FUNCIONAL NUEVA · RECUPERACIÓN NO DISPONIBLE`» → `cap-44`: «Para mí, Nieve muere.» | **La amenaza de Cuchillo ya se cobra, y se cobra al personaje que el lector más quiere.** Lo verdadero es más estrecho: *ningún humano se entera nunca*, y eso es la tesis del libro. |
| **4** | Ángulo 6: «46 de 48 capítulos entre 938 y 2.312» | **45 de 48.** Tres por debajo: `cap-48` (705), `cap-25` (742), `cap-01` (752). | Trivial. Pero: **nadie ha medido el coeficiente de variación de una novela buena.** El metrónomo se declara defecto **sin control externo**, igual que el 8,5. |
| **5** | Ángulo 5: «`compilado/ad-aeternum-vF.md` está una revisión por detrás, 30 líneas divergentes» | Ya no. `vF` y `w10prep` tienen hoy **0 líneas divergentes**. `vF` fue **recompilado en su sitio** en el commit `4f18bc4`: **80.704 → 80.727 palabras.** El informe de la beta cita `sha256 2950755d…` y **80.135 palabras**. | **Tres artefactos distintos han llevado el nombre «vF».** Una línea base que se puede sobrescribir no es una línea base, y todo el método de §5.1 (medir con control pareado) descansa en que lo sea. |
| **6** | Cinco ángulos, cinco totales | 80.135 (beta) · 80.279 (á. 2) · 80.302 (mío) · 80.459 (á. 1 y 3) · 80.727 (á. 5 y hoy) | Dispersión del 0,7 %. No cambia ningún veredicto, pero **ninguna cifra de porcentaje de este expediente vale más allá de la primera decimal.** |
| **7** | Plan §4b.3: «Puntuar con la rúbrica **una novela publicada y reconocida**… Este experimento es barato y puede ahorrar la fase entera. **Va primero**» | `informes/w10/techo-experimento.md` ejecuta **solo el segundo bullet** (v0 y vF con rúbrica anclada). **El control externo no existe en el repositorio.** Grep sobre `informes/` y `herramientas/`: nada. | **La mitad del experimento que podía cerrar la fase se saltó.** Es mi entregable número uno. |

---

## 1 · El hecho que ningún ángulo podía ver, y que reordena el panel

Los seis ángulos razonan sobre «el punto de abandono está en el 62 %». **Eso no es lo que se midió.** Lo que se mide en este proyecto es **qué capítulo nombra cada lector frío como el sitio donde estuvo a punto de dejarlo**, y en vF hay cuatro nominaciones con nombre y apellido:

| lector | punto de abandono | motivo, literal |
|---|---|---|
| A6-1 (`a6-vF-critico-1.md:21`) | **cap. 31 «Interferencias»** | «Tres hostigamientos burocráticos paralelos con idéntico compás y la misma frase de cierre —"No consta responsable individual"— hacen tres veces un punto que ya estaba hecho». Segundos: **20 y 27**. |
| A6-2 (`a6-vF-critico-2.md:19`) | **cap. 27 «Inventario»** | «es donde el procedimiento deja de producir sentido y empieza a producir inventario literal; **el 20 y el 31**, alrededor, agravan la caída». |
| A6-3 (`a6-vF-critico-3.md:19`) | **cap. 31 «Interferencias»** | «encadena otra suspensión escolar, otra sanción laboral, otra resolución policial retroactiva… **La repetición es temática, pero no toda reiteración añade presión narrativa**». |
| beta-abandono (`a6b-beta-abandono-vF.md`) | **cap. 36 «La asamblea»** | «Estaba leyendo **un acta de junta de vecinos entre entidades que no puedo ver**». Y: «¿Qué escena sobra? El capítulo 44 ("Norna")… con una de las tres bastaba». |

Y A6-1, en prosa: «en el **11**, el **27** y el **31** la selección se afloja y la prosa se vuelve inventario».

**De los capítulos que los lectores de vF señalan como defecto —31 (×3), 27 (×3), 20 (×2), 11 (×1)— los cuatro son capítulos que este proceso añadió.** Origen `REVISIÓN 10`: 8, 11, 17, 20, 27, 31, 47. Son el 14,6 % de los capítulos y el 15,0 % de las palabras, y concentran el 100 % de las quejas de capítulo de la última campaña.

**Y la otra mitad del hecho, que es obligatorio decir:** esos mismos capítulos concentran también los elogios. Un crítico anclado llama al **cap. 8** «la cima del libro»; al **cap. 11**, «el mejor personaje episódico del libro»; del **cap. 27** dice que «hace más duelo que veinte páginas de introspección». **No son capítulos malos. Son capítulos sin trama.**

Cinco de los siete no avanzan la trama (8, 11, 17, 27, 47). **Seis oleadas añadieron 17.552 palabras, 12.016 de ellas en siete capítulos nuevos, y unas nueve mil de esas son desaceleración pura, en un libro cuyos ejes estancados son ritmo, trama, estructura y global.**

> **Ésta es mi respuesta a por qué seis oleadas no movieron los cuatro ejes: cada oleada añadió freno a un libro diagnosticado de lento, y lo hizo bien, capítulo a capítulo.** No es un fallo de puntería. Es la propiedad emergente de un proceso que solo sabe sumar — exactamente lo que el ángulo 6 predice en abstracto sin saber que ya había pasado.

**Corolario duro, y es el que gobierna mi tabla:** en la iteración 1, **la carga de la prueba de toda propuesta que añada palabras es la séptima repetición del movimiento que produjo el atasco.** No es prohibitiva. Es mucho más alta de lo que ninguno de los seis ángulos supone.

**Y un criterio de aceptación vivo que el libro incumple hoy.** El autor, el 2026-08-18 (`informes/registro-gates-autor.md:18`), sustituyó «Ritmo ≥ 8,0» por: **«ningún capítulo nombrado como punto de abandono por dos o más lectores en el mismo hito»**. vF lo **incumple**: `cap-31` lo nombran dos de tres. Plan W10 §5.7 lo refrenda («el criterio final no es la métrica: es dónde deja de leer la gente»). **Nadie lo ha registrado como incumplido, y es el único criterio de este proyecto que ha respondido al trabajo.**

---

## 2 · Tabla de puntuación

*P = probabilidad de mover un eje estancado (0–10). R = riesgo para lo que ya funciona (0–10). Solo se puntúa lo que trae hoja.*

| Prop. | Qué | P | Coste | R | Veredicto |
|---|---|--:|---|--:|---|
| **A1** | Capítulo nuevo «Lote de prueba» entre 29 y 30; saca la muerte de `/0044` del cap. 36 | 3 | +2.700/3.200 · 1 oleada A3a + **A7 previo** | **9** | **NO** |
| **A2-A** | Sustrato de casos a los caps. 36 y 44 | 2 | 2.995 reescritas, +250 · 1 oleada + A7 | 8 | **NO** |
| **A2-B** | Reinstaurar el recuento (4 inserciones, ≈350) | 2 | 0,5 oleada | 4 | injerto parcial (solo la del 44) |
| **A2-C** | 71-K vuelve una vez (≈80) | 1 | mínimo | 5 | **NO** (el propio ángulo pide denegarla) |
| **A3-C1** | Suprimir el cap. 8 con trasplante al 7 (−1.589) | 2 | 0,5 oleada | **9** | **NO** |
| **A3-C2** | Cap. 34, mirador y regreso (−971) | 3 | 0,5 oleada | 5 → **8** | **NO** — revocado en §4bis: es resto |
| **A3-C3** | Cap. 19, las tres columnas (−312) | 1 | mínimo | 2 | **injerto** |
| **A3-C4** | Fusión 37+39 (−839) | 3 | 1 oleada | 6 | **NO** — la cubre P-2 a un sexto del riesgo |
| **A3-C5** | Cap. 18, Madre y Cuchillo (−414) | 1 | mínimo | 3 | **injerto** |
| **A3-C6** | Cap. 40, Henrik a la mitad (−215) | 1 | mínimo | 4 (**W9-20**) | **injerto**, fundido con P-3 |
| **A3-C7** | Cap. 25, primera mitad (−180) | 1 | mínimo | 2 | **injerto** |
| **A3-C8** | Cap. 11, logística de Maja (−177) | 1 | mínimo | 4 (**R5**) | **NO** — 177 palabras no valen una discusión con el perímetro |
| **A3-H3** | Partir los cuatro capítulos más largos de la IV. **Cero palabras** | **4** | 0 palabras · 1 campaña | 3 | **SÍ**, fundida en mi síntesis |
| **F-1** | Cuenta atrás desde la Parte II; la I fecha la noche polar | 2 | 1 cadena de metadatos | 4 | **sí, pero jamás medida sola** |
| **F-2** | Frontera II/III al cap. 26. **Cero palabras** | 3 | 2 campos | 2 | **SÍ** |
| **F-3** | Corte asimétrico: **−4.500/5.000 solo en la Parte III** | 2 | 2–3 oleadas + **A7 en once capítulos** | **10** | **NO. Aritméticamente imposible sin amputar el clímax** |
| **F-4** | Frontera III/IV al cap. 35. **Cero palabras** | **4** | 3 campos | 3 | **SÍ — y anulo la declinación de su propio autor** |
| **F-6a** | «Mørketid» absorbida en el subtítulo | 1 | incluida en F-1 | 1 | injerto |
| **P-1** | Capítulo nuevo de duelo por La Jardinera al abrir la IV | 3 → **5** | +1.300/1.700 · 1 oleada + **A7** | 7 | **NO para la it. 1** · **reserva ascendida en §4bis** |
| **P-2** | Comprimir el protocolo de aborto (−250/400) | 2 | mínimo | 2 | **injerto — el mejor anclado del expediente** |
| **P-3** | Comprimir cap. 40 Alana/Henrik (−300/350) | 1 | mínimo | 4 (**W9-20**) | **injerto** |
| **E-1** | Tres capítulos a 3.500–4.000 y tres a 700–900 | **5 → 8** | +4.000/6.000 · 2 oleadas | 8 → **5** | **SÍ. Revocado al alza en §4bis: es la mejor apuesta del expediente** |
| **E-2a** | Partir el cap. 15; una voz por capítulo con ancla exterior | 4 | +600/1.000 · 1–2 oleadas | 7 | **NO** — ver §3, nota |
| **E-2b** | 200 palabras en el cap. 42 desde una butaca del Auditorio | 3 | mínimo | 6 | **NO** (ver §0, corrección 3) |
| **E-3** | «Flor» como capítulo 1, «Corona» como 2 | 3 | reordenación + suturas | **9** | **NO** |
| **E-5** | Una costumbre mental propia por adulto con POV | 2 | 0,5 oleada, ±0 palabras | 3 | **injerto** |
| **E-4** | Título, sinopsis, lectura noruega y sjøsamisk | 0 | fuera de rúbrica | 1 | **injerto — la única propuesta que reduce un riesgo real** |
| **F-5, D-1…D-5, E-1(b)** | declinadas por sus propios autores | — | — | — | **confirmo las declinaciones** |

**Las tres puntuaciones que hay que justificar:**

**F-3, riesgo 10.** La Parte III mide 20.300. Los cuatro capítulos que *los propios ángulos 3, 4, 5 y 6 protegen expresamente* —27 (1.737), 28 (1.856, `proteccion: total`), 30 (1.765), 32 (1.773, modelo del perímetro para R6)— suman 7.131. **Quedan 13.169 palabras disponibles, y F-3 pide 4.500: el 34,2 % de ellas.** Ese 34 % hay que sacarlo de la auditoría de Astrid, la forense de Tomas, la confesión de Alana + el ladrillo + la siembra de NORNA, el trayecto (con «—Por ahí no», techo de R1), la poda + la cautelar denegada, y la asamblea. Son **cinco de los cinco hilos** que el ángulo 3 demuestra que convergen en 12:46:50. Y once de los doce capítulos llevan ancla de perímetro. **F-3 no nombra una sola frase para cortar** —dice expresamente «la zona, no las frases»—: es un objetivo sin origen. La cifra 4.500 no sale de leer la Parte III; sale de una ecuación de forma.

**A1 y A3-C1, riesgo 9, por la misma razón: las dos vacían un capítulo para llenar otro.** A1 saca de `cap-36` las 380 palabras que van de «—Para la convergencia bastan los fragmentos con origen. Los demás convie—» a «Nadie propone una casilla para ella», y deja el capítulo como procedimiento de votación puro. **`cap-36` es el punto de abandono declarado del único lector beta**, y su motivo es exactamente ése: «un acta de junta de vecinos entre entidades que no puedo ver». A1 le quita lo único que hoy lo hace soportable. C1 hace lo mismo con la regla de `cap-08:55` y su pago en `cap-30:301`.

**E-3, riesgo 9.** Dos de tres críticos de vF citan espontáneamente la última línea del cap. 1 —«La corona se balanceó una sola vez en el gancho y quedó quieta»— como ejemplo de la mejor prosa del libro, y el crítico anclado de v0 fundamenta en ese capítulo su juicio de que «**la estructura es la mejor decisión del libro**»: «El capítulo 1, leído en frío, es una calibración rutinaria; leído desde el 25, es el suicidio contado por sus formularios». **Cero lectores en 48 lecturas se han quejado del arranque.** Y hay un argumento que el ángulo 6 no ve: **`premisa` es el eje que dos críticos declaran acotado por el campo.** Abrir con «Fije la vista en el centro de la imagen» pone en la página uno exactamente la premisa que el jurado descuenta; abrir con «Corona» pone lo que el jurado elogia sin excepción — el ángulo administrativo, un formulario, un campo vacío. **E-3 propone empezar por lo que no puntúa.**

---

## 3 · Veredictos de los cuatro conflictos

### C-1 · ¿Se corta la Parte III, y de dónde salen las palabras?

> **Las dos cifras se excluyen, y el ángulo 3 tiene razón. F-3 queda denegada por aritmética, no por gusto. La forma que F-3 persigue se compra gratis con F-2 + F-4, y por eso el conflicto no hay que arbitrarlo: hay que disolverlo por el otro lado.**

**Los 4.697 del ángulo 3, repartidos por partes:** I = 1.766 (C1 + C8) · II = 726 (C3 + C5) · III = **1.151** (C2 + C7) · IV = 1.054 (C4 + C6). **Solo 1.151 palabras de corte defendible caen en la Parte III: el 5,7 % de ella y el 24 % de lo que F-3 pide.** No se solapan: se excluyen. El ángulo 3 leyó la Parte III buscando qué se puede quitar y encontró mil ciento cincuenta y una palabras. El ángulo 4 no la leyó buscando eso; derivó 4.500 de una ecuación de forma y entregó la zona, no las frases.

**Y aquí está lo que ninguno de los dos vio, porque el ángulo 4 lo escribió y lo descartó:** su propia hoja **F-4** produce la forma objetivo **sin cortar una sola palabra**. Verificado por mí:

| | hoy | con F-2 + F-4 |
|---|---|---|
| I (1–12) | 19.986 | 19.986 |
| II (13–24 → **13–25**) | 20.458 | **21.200** |
| III (25–36 → **26–34**) | 20.300 | **16.547** |
| IV (37–48 → **35–48**) | 19.558 | **22.569** |

**Eso es 20 / 21 / 16,5 / 22,5.** Rompe la igualdad con más filo que el objetivo de F-3 (20 / 20,5 / 15,5 / 19,5), hace del tercer movimiento el más corto y del cuarto el más largo, y cuesta **cinco campos del manifiesto y tres subtítulos** (III pasaría a *27 de diciembre de 2060 · Faltan 25 días*; IV, a *9 de enero de 2061 · Faltan 12 días*; ambos aritméticamente exactos, comprobados).

**Anulo la declinación de F-4 por su propio autor.** Su objeción es que saca «La asamblea» de la posición de clímax de movimiento. Es una pérdida real y es la única. **Pero F-4 no cambia una sola adyacencia del texto**: 35 y 36 siguen consecutivos, y la secuencia «La poda» → «La asamblea» —la orden de consolidación y la cautelar denegada, e inmediatamente los reducidos constituyéndose y votando— queda intacta. Lo único que cambia es de qué lado del telón cae. A cambio, la Parte III cierra en **«…20…23:00…no lleguéis tarde…»** (`cap-34`, última línea: el plazo llegando como transmisión rota) y la Parte IV abre en «La poda» con *Faltan 12 días* y catorce capítulos de aceleración detrás. **Vender la cumbre por la silueta**, dice el ángulo 4. Yo digo: la cumbre no se mueve un metro; se mueve el rótulo.

**Coste de F-2 + F-4 que sí hay que decir:** una Parte III de 16.547 palabras y nueve capítulos puede leerse como diseño o como que el libro se quedó sin material. No hay forma de saberlo sin medir. Es reversible en un commit.

**Qué se pierde si se hace F-3 en vez de esto:** el desgaste. La tesis del tercer movimiento es que las instituciones muelen despacio y muchas veces, y su prueba interna es el caso de 2054 de Astrid —«El hombre volvió cuatro veces con capturas distintas y ninguna dio el mismo resultado… Archivó el caso y bajó la carpeta al cajón inferior del armario». **Repetir sin resultado *es* el asunto.** Un tercer movimiento corto por amputación convierte el desgaste en resumen. Un tercer movimiento corto **por frontera** conserva cada palabra del desgaste y solo cambia cuándo el lector siente que ha terminado.

---

### C-2 · ¿Qué entra en el hueco que deja el corte?

> **Son una sola cosa vista desde tres lados, y la formulación no es la de ninguno de los tres. Y de las tres intervenciones, ninguna se paga: dos están contraindicadas por el lector que las validaría, y la tercera parte de un hecho falso.**

**La frase única:** *después del 55,7 %, todo lo que ocurre en este libro —dentro y fuera— se tramita a través de un documento, y no queda nadie visible a quien pueda pasarle algo.*

Los tres ángulos han medido tres sombras del mismo objeto: el ángulo 2 la mide en los capítulos interiores (desconocidos con cara 4,2 → 0,4), el ángulo 5 en los exteriores (la familia), el ángulo 6 en la trama (la amenaza que no cae sobre nadie). **Un solo diagnóstico, tres instrumentos, y ninguno se solapa con otro: por eso convergen.** El ángulo 4 lo mide una cuarta vez y le pone número: **siete capítulos consecutivos (29→35) cuyo objeto central es un papel, 12.556 palabras, 15,6 % del libro** — verificado por mí.

**Pero de las tres intervenciones que salen de ahí, ninguna sobrevive al lector:**

- **A2-A (sustrato a los caps. 36 y 44).** El propio ángulo 2 declara el riesgo: «puede subir la carga cognitiva justo en el capítulo que ya es el segundo más denso del hilo. **Este es el riesgo real de la propuesta**». **Está realizado.** El único lector que informa de dónde estuvo a punto de dejarlo lo dejó **en el 36**, y por carga: «un acta de junta de vecinos entre entidades que no puedo ver». Y del 44 dice que **sobra**: «repite una asamblea/votación que ya vivimos en el 36 y en el 42… Con una de las tres bastaba». **A2-A añade materia a los dos únicos capítulos que un lector ha nombrado por exceso.** Denegada.
- **P-1 (capítulo de duelo por La Jardinera).** Su justificación descansa en «441 palabras domésticas en 31.800», que es entre tres y seis veces menor que la cuenta real (§0.1). Corregida la cifra, la propuesta sigue siendo defendible pero deja de ser urgente — y sigue costando **+1.300/1.700 palabras de desaceleración pura colocadas entre el 75 % y el 82 %**, que es el séptimo ejercicio del movimiento que produjo el atasco (§1). Y su propio autor concede: «Se añade material a la franja que ya es lenta… es una apuesta y puede perderse». Denegada **para la iteración 1**; no cerrada.
- **E-2b (200 palabras en el cap. 42 desde una butaca).** Parte de un hecho falso (§0.3). Y toca lo único que sostiene el capítulo: **«La interfaz no muestra nombres ni plano.»** Jean se niega *porque no sabe a quién golpearía* —«—No sabes a quién vas a golpear.» / «—Ellos tampoco preguntaron.»—. Enseñarle la sala al lector no rompe el perímetro, pero convierte una pregunta moral epistémica en un dispositivo de suspense, y `cap-42` es el capítulo de la factura, no el del susto. Denegada.

**Lo que sí concedo del ángulo 2, y es lo único de C-2 que compraría:** su **Pieza B reducida a una sola inserción**, la del `cap-44` junto a `4.096 − 1.185 = 2.911`. La contabilidad de Jean al lado de la de Armstrong, sin comentario y sin que ninguna gane. Es 40–120 palabras, no es mecánica nueva (M2 = 0), y paga la única promesa del libro que el ángulo 2 demuestra impagada con número de línea: `cap-08:53`, «Jean cuenta las que llevan a alguien». **Condición de A7 (R4): el narrador no enuncia jamás el parentesco entre las dos aritméticas.**

---

### C-3 · ¿Se dramatiza la poda?

> **La pregunta está mal planteada y por eso el conflicto es aparente. El ángulo 5 tiene razón sobre la poda; el ángulo 1 no propone dramatizar la poda; y el ángulo 1 pierde igualmente, por otra razón.**

**No hay conflicto sobre la poda.** El ángulo 5 prohíbe poner en escena las 1.185 («que el mayor recuento de muertes del libro llegue como una línea de contabilidad es la tesis del libro dicha en forma»). El ángulo 1 **coincide**: «El capítulo no da cifra total. Da una parcial y sin denominador». Los dos protegen lo mismo. **El D-4 del ángulo 5 debe anotarse como acierto permanente y cerrarse a futuras oleadas**, con su literal: «`SEGMENTO 5 · RESERVA DE RESPUESTA REMOTA`» / «En la tableta, el quinto hueco no volvió a abrirse».

**Lo que el ángulo 1 propone es otra cosa: trasladar y expandir la muerte de La Jardinera.** Y ahí gana el ángulo 5 por un motivo que el ángulo 1 escribe él mismo y minimiza: **la muerte de `/0044` dentro de la votación demuestra en acto lo que la votación discute** — que se puede desaparecer a mitad de palabra. «Los demás convie—» / «La ruta de `JM-L/0044` se cierra.» Eso no se traslada: se destruye al trasladarlo. Y `cap-36` se queda con el reglamento —«Abstenciones, silencios, falta de margen y papeletas incompletas quedan fuera»— que es literalmente la frase que el lector beta cita al explicar por qué casi lo deja.

**El argumento del ángulo 4 (D-4, la regla de sucesión) no aplica** y hay que decirlo para que no se use mal: el capítulo del ángulo 1 no es una escena de Jean viva. La regla de sucesión sí aplica, pero por su pregunta 1, no por su punto 4: *«¿Qué punto de la Carta mejora esta página?»* — ninguno; mejora el ritmo. **Denegada en el gate y también en el mérito.**

---

### C-4 · La cuenta atrás (F-1)

> **El diagnóstico es correcto y verificado. El remedio propuesto no lo cura, porque conserva el dato que produce el defecto. Y por su tamaño no puede medirse sola sin quemar una de las tres oportunidades del §6.**

**Lo verificado:** `grep` sobre `capitulos/`: **«Mørketid» aparece cero veces en la prosa del libro** — solo existe como título de parte en `biblia/metadatos.json`. Y **«Soldagen» aparece por primera vez en `cap-13`**, al 27,5 %, en la escena donde la fecha *se decide*: «una fecha en blanco sobre el arco dorado del logotipo. **21 de enero de 2061**». Los dos cargos son ciertos: durante veinte mil palabras el paratexto sabe algo que la novela todavía no sabe.

**Por qué el remedio no cura.** El subtítulo propuesto —*«Tromsø · 24 de noviembre de 2060 · el sol no saldrá hasta el 21 de enero»*— **vuelve a imprimir el 21 de enero en la página 2**. Conserva íntegra la presciencia del paratexto y pierde el tictac, que es la única señal de destino que el primer cuarto tiene. Se paga el precio sin comprar la mercancía. Si se hace, la única versión que cumple su propio argumento es la que **no da fecha ninguna**: *«Tromsø · 24 de noviembre de 2060 · la noche polar»*, y que el 21 de enero nazca en el cap. 13, donde nace.

**Mérito literario, sin adornos.** La lectura que salva la cuenta atrás es soberbia y es del propio ángulo 4: **la cuenta atrás de los subtítulos es el calendario de Armstrong impreso sobre las páginas del libro** — «—El calendario es el contrato» (`cap-13`). Si la Parte I no cuenta y las tres siguientes sí, la apropiación del paratexto se dramatiza. Eso es un argumento literario de primer orden y lo suscribo.

**Y aun así:** **cero lectores en 48 lecturas han mencionado la cuenta atrás como defecto**; el crítico anclado de v0 dice lo contrario —«la cuenta atrás a Soldagen genera tracción real»—. La única objeción viene del ángulo 6, que es agente nuestro, no lector. **Es un cambio de dos cadenas, reversible en un commit, que no puede mover medio punto en ningún eje.** Mi veredicto: **hacerse puede; medirse sola, jamás.**

Lo cual me lleva a un hallazgo de método que vale más que F-1:

> **Plan §6 detiene la fase tras «tres iteraciones consecutivas sin una sola mejora fuera del ruido». Cada intervención barata medida por separado gasta una de esas tres. Con el suelo de ruido en ±0,5 y el jurado variando hasta un punto entero sobre texto idéntico, medir F-1 sola es contratar un resultado nulo y pagarlo con un tercio de la fase.** Las intervenciones se agrupan **por hipótesis**, no por baratura.

---

### Dos conflictos que el encargo no nombra y que hay que resolver igual

**C-5 · Ángulo 3 (H-3) y ángulo 6 (E-1) diagnostican la misma enfermedad y prescriben el signo contrario.** Los dos miden la uniformidad —yo la confirmo: CV 23,6 %, IQR 1.469–1.880—. El ángulo 6 quiere **amplitud por crecimiento** (tres capítulos a 3.500–4.000, tres a 700–900: ≈ +4.000/6.000 palabras). El ángulo 3 quiere **amplitud por división** (partir los cuatro más largos de la Parte IV: **cero palabras**). **Veredicto: se prueba primero el de coste cero, y no porque sea el más probable —lo es menos— sino porque un nulo en H-3 cierra la familia entera y un nulo en E-1 solo dice que esas seis mil palabras no eran las buenas.** Y porque E-1 es, otra vez, sumar. El ángulo 6 tiene el mejor argumento del expediente («en todo el manuscrito no hay ni un solo capítulo al que se le haya permitido crecer») y el peor momento para usarlo.

**C-6 · Ángulo 2 y ángulo 3 se contradicen sobre las mismas 1.835 palabras.** Para el ángulo 3, el `cap-08` es el mayor corte defendible del libro. Para el ángulo 2, contiene «la promesa central» —`cap-08:53`— y es lo único que sostiene la premisa. **Gana el ángulo 2, y la demostración es de texto:** el ángulo 3 verificó que el capítulo no siembra objetos (zueco, andador, cuartilla, escurridor: cero fuera del 8) y **no verificó que siembra una regla**, cuyo pago es el mejor remate del `cap-30`. Un audit de corte que hace `grep` de sustantivos no puede ver una regla moral. **C1 denegada, y el método que la produjo queda anotado.**

---

## 4 · Mi síntesis para la iteración 1

**Antes de la iteración 1, y no cuenta como iteración: ejecutar la mitad que falta de §4b.3.**

> Puntuar con la rúbrica anclada, en frío real y con el mismo jurado del mismo día, **una novela publicada y reconocida del mismo género** (y, si cabe presupuesto, una segunda competente pero no memorable). **Es lo único de todo este expediente que puede terminar la fase, el plan ordenó que fuera primero, y no se hizo.** Si la novela canónica también sale 8,5 de global, el objetivo «9 en las once» está muerto por construcción y W10 entrega su diagnóstico. Si sale 9,5, sabemos por primera vez cuánta distancia hay y de qué está hecha. Coste: una campaña fría. No toca el manuscrito, no gasta una de las tres oportunidades de §6.

**Y después, una sola intervención, con una sola hipótesis: *el centro no se alarga ni se amputa; se redistribuye.***

Tres movimientos que apuntan en la misma dirección y **ninguno de los cuales añade una palabra**:

**(a) Las dos fronteras de parte, F-2 + F-4.** `partes[1].capitulo_final: 24→25`, `partes[2]: 25→26 / 36→34`, `partes[3].capitulo_inicial: 37→35`, y tres subtítulos. Forma resultante **19.986 / 21.200 / 16.547 / 22.569**. Cero palabras, cero perímetro, cero A5. La Parte II cierra en «—Ser inevitables.»; la III, en «…20…23:00…no lleguéis tarde…»; la IV es el movimiento más largo y el único que corre.

**(b) Romper la cadena documental por su eslabón medido, no por su longitud.** La cadena 29→35 son **12.556 palabras, 15,6 % del libro, siete capítulos seguidos con una mano sobre un papel**. Su cuarto eslabón, `cap-31`, es **el capítulo que dos de tres lectores nombran como punto de abandono**, y su defecto está diagnosticado con precisión quirúrgica por los dos: **tres hostigamientos institucionales idénticos en un solo capítulo, el tercero de los cuales repite lo que el `cap-29` ya dramatizó**. La intervención es **reubicar uno de los tres tramos fuera del capítulo y fuera de la cadena, sin cortarlo**: el bloque de Nora que va de «La plataforma admitió las credenciales de Nora al primer intento» a «Nora escribió `viernes`, `28`, `Kongsbakken` y `firma` debajo de las dos horas de la mañana» (**≈ 620 palabras**), cuyo hilo —la repesca de marzo, las mañanas de Maja— ya tiene su continuación literal en `cap-34` («—¿Ya hay fecha para la repesca? —En marzo… —Te dejo las mañanas»). Resultado: `cap-31` baja de 2.181 a ≈1.560, pasa de tres hostigamientos a dos, la cadena baja de siete capítulos consecutivos a seis con una interrupción, y **no se pierde una sola palabra del libro**. Lo que hay que verificar con A5: que la suspensión de la cuenta no sea condición de nada entre el 31 y el 34 (mi lectura dice que no: ni el 32 ni el 33 la usan).

**(c) H-3, la amplitud por división, cero palabras.** Partir `cap-40` (2.312, ocho escenas, el capítulo más largo del libro) y `cap-43` (2.244, tres bloques de ~750) por sus dinkus. Nada más. **Cero prosa nueva, cero prosa borrada, `git revert` limpio.**

**Neto del paquete: ±0 palabras.** Una campaña. Sin A7 (nada toca el perímetro: se mueven fronteras de parte, se traslada un bloque de instituto y se parten dos capítulos por sus separadores existentes). A5 obligatorio en (b). `actualizar-metadatos.sh` y `proteger.sh --rebaseline --gate` en (a) y (c).

### Criterio de falsación, declarado antes de medir

**Doble, porque el instrumento está bajo sospecha y porque el proyecto tiene un criterio mejor que la rúbrica.**

1. **Primario, de lector — el criterio ratificado por el autor.** Campaña fría con la pregunta del punto de abandono. **Si algún capítulo vuelve a ser nombrado punto de abandono por dos o más lectores en el mismo hito, la intervención ha fracasado en su objetivo declarado y se revierte entera.** Si `cap-31` sale de la lista y no entra otro con dos nominaciones, la intervención **paga**, aunque no se mueva un solo eje — y ese resultado hay que escribirlo así de claro en el informe final.
2. **Secundario, de rúbrica, con control de deriva de v0 del mismo día.** **Si `estructura` no sube ≥ +0,5 sobre la mediana corregida por deriva, la familia entera «uniformidad de unidad y de movimiento» se cierra para W10** y se anota en `callejones_sin_salida` con esta redacción:

> «La igualdad de las cuatro partes (1,1 %) y la estrechez de la banda de longitud de capítulo (CV 23,6 %) son propiedades reales y medidas del texto. Se corrigieron a coste cero moviendo dos fronteras y partiendo dos capítulos, sin quitar ni añadir una palabra. Mover esa propiedad no mueve `estructura`. La uniformidad no es lo que el jurado puntúa como arquitectura.»

**Mi predicción, registrada por adelantado y contra mi propia propuesta:** `estructura` **0 a +0,5** · `ritmo` **0** · `trama` **0** · `global` **0** · `duelo`/`tema` **0**. **Espero que la rúbrica no se mueva.** El valor de esta iteración es (i) reparar el único criterio de aceptación vivo que el libro incumple y (ii) cerrar una familia entera de intervenciones por el precio de cero palabras. Si además sube algo, mejor; pero he dicho antes de medir que no lo creo, para que el resultado signifique algo.

**Qué se pierde con mi propia propuesta, y lo digo yo:**
- La asamblea deja de ser telón de movimiento (F-4).
- `cap-31` pierde su cierre de tres papeles alineados como culminación de tres hostigamientos; el «Tres formatos, tres tipos de letra, un solo día» queda apoyado en dos.
- Partir el `cap-40` rompe la única meseta continua de ocho escenas que el libro tiene antes del clímax, y esa meseta puede ser justamente lo que hace que el 41 corra. **Éste es el punto de mi paquete que más probablemente empeore algo**, y si el nulo llega acompañado de una caída en `trama`, es lo primero que hay que mirar.
- Y el riesgo global: los tres movimientos son a coste cero, lo que los hace **exactamente el tipo de cambio tímido contra el que avisa §4b.4**. Lo asumo a sabiendas y digo por qué: la evidencia de §1 dice que en este libro las apuestas grandes han sido siempre apuestas de suma, y las de suma son las que produjeron el atasco. **La apuesta grande de W10, si mi lectura es correcta, es restar y redistribuir; y por primera vez hay una forma de restar que no cuesta una palabra.**

---

## 4bis · Adenda: reviso mi síntesis a la baja, y digo por qué

**Esto se escribe después de haber puntuado la tabla.** Mientras cerraba, `informes/w10/estado.json` incorporó el hallazgo de la iteración 0, que yo no tenía al juzgar y que **cambia dos de mis veredictos y el orden de mi síntesis**. Lo dejo en una sección aparte en vez de reescribir lo anterior, porque el orden en que llegó la evidencia es parte del dato.

**El hallazgo, resumido:** cuatro lecturas frías independientes, de dos familias de modelos y con dos preguntas distintas, convergen en que **el libro no tiene resto**: todas sus escenas son necesarias para la trama, y *esa* es la carencia. «Sobrecontrol hermenéutico: la emoción está notarizada.» Y el método del proyecto lo fabricaba — **M2 exige etiqueta de función a toda inserción y `auditor-adverso.sh` borraba lo que no la pagaba, durante seis oleadas**. Más la ponderación real de la global: **estructura 25 · personajes 25 · tema 20 · ritmo 15 · trama 7 · prosa 6 · diálogo 2.**

### Lo que esto le hace a mi §1

**No lo contradice: lo completa, y la versión completa es mejor que la mía.**

Yo concluí que seis oleadas añadieron freno y que por eso la carga de la prueba de toda adición es altísima. Eso, tal cual, **es un error mío y lo retiro.** La versión correcta es más fina y explica más:

> Los cinco capítulos nuestros que no avanzan la trama —8, 11, 17, 27, 47— fueron **exactamente el intento del proceso de añadir resto**. Y no lo son, porque **M2 obligaba a que cada uno llevara etiqueta de función**. El `cap-27` no es una familia siendo una familia: es la escena que paga la deuda de duelo de la Parte III, y A6-2 lo nota con esas palabras — «es donde el procedimiento deja de producir sentido y **empieza a producir inventario literal**». El `cap-11` paga R5. El `cap-47` paga R8. **Nada en este libro es gratis, y los lectores lo sienten justamente en las páginas que este proceso escribió para que no se notara.**

Por eso los cuatro capítulos señalados son los nuestros: no por ser adiciones, sino **por ser adiciones justificadas**. Se les ve el recibo.

**Mi regla («la iteración 1 no debe sumar») queda mal formulada y la sustituyo por esta:**

> **La próxima adición tiene que ser la primera de todo el proyecto que no pague por nada.** Y la carga de la prueba se invierte: **una adición que traiga etiqueta de función es sospechosa por traerla.**

### Las tres consecuencias operativas, en orden de importancia

**1 · El aparato de verificación se comerá la intervención antes de que llegue a medirse, y hay que desarmarlo por escrito.** M2 («Máximo 1 mecánica nueva por capítulo de Jean… Toda inserción lleva etiqueta de función; **sin etiqueta, se borra**») y `auditor-adverso.sh` («¿paga cada una su etiqueta de función?») **están construidos para destruir resto**, y llevan seis oleadas haciéndolo bien. Si la iteración 1 escribe páginas sin función y luego pasa por A5, por el auditor adverso y por la hoja de A2 —que exige «qué función cumple» en cada bloque—, **el material sale borrado del pipeline y el resultado se anotará como "la intervención no movió nada"**. Sería el duodécimo instrumento que falla a la baja y en silencio, y esta vez sabiendo por adelantado que iba a fallar.
> **Acto operativo previo, sin el cual no merece la pena intentarlo: suspender M2 y `auditor-adverso.sh` para el material de esa intervención, y dejarlo escrito en la orden.** Es la aportación más concreta que tengo y no la hace nadie más del panel.

**2 · Revoco al alza E-1, del ángulo 6, y pasa a ser la mejor apuesta del expediente.** «En todo el manuscrito **no hay ni un solo capítulo al que se le haya permitido crecer**» y «el libro no tiene resto» son la misma frase dicha con dos instrumentos. Dejar que el `cap-30` corra hasta 3.500 **sin añadirle una función** —Jean con tiempo y sin nada que hacer con él, que es la única página del libro donde el resto sería literalmente el asunto— es la operacionalización exacta del hallazgo. Su riesgo baja de 8 a 5 por un motivo verificable: **el `cap-30` es el único capítulo del libro del que un lector escribe «ni una coma; si un corrector lo aligera, despido al corrector»**, y no hay una sola queja sobre él en 48 lecturas. Crecer ahí es el sitio más protegido que existe para probar la hipótesis. Y cumple §4b.4: es la apuesta de 5.000 palabras, no la de 200.

**3 · Revoco a la baja mi propio injerto de compresión, en un caso.** **A3-C2 (cap. 34, mirador y regreso, −971) pasa a NO.** «Esto es un ensayo de esperar», el termo que da la vuelta entera y vuelve vacío, Jessie sentada sobre las manos, «Ellas también formaban parte del tráfico que alguien podía aprenderse»: **eso es resto, y es de lo poco que hay.** El propio ángulo 3 lo cuenta como pérdida neta irrecuperable. En un libro cuyo diagnóstico es que no le sobra nada, cortar novecientas palabras de gente esperando sin que pase nada es cortar la muestra. **P-2, P-3, C3, C5 y C7 sobreviven** porque lo que quitan no es resto: es **exposición procedimental repetida tres veces**, y el texto contesta a la tercera con «—Ya lo sé».

### Y lo que la ponderación real hace con mi síntesis

Con **estructura al 25 %** y `personajes` y `tema` ya en 9, mi paquete apunta al mayor coeficiente disponible de la global. Pero mi propia predicción registrada es `estructura` **0 a +0,5**, lo que da a la global **0 a +0,125**: **nada.** Es honesto decirlo: **mi síntesis de §4 no puede mover la global aunque salga perfecta.**

**Por eso la revoco como intervención principal de la iteración 1 y la degrado a acompañante.** El orden correcto queda así:

| orden | qué | por qué |
|---|---|---|
| **0** | **El control externo de §4b.3** | Sin él no sabemos si el 9 de global es emisible. Sigue siendo lo primero y sigue sin hacerse. |
| **1** | **La primera adición sin función del proyecto** — E-1 sobre el `cap-30`, y como candidata mayor la escena de CARIES (ver abajo) | Es lo único del expediente respaldado por cuatro lecturas convergentes, y ataca la global por donde el hallazgo dice que se pierde. **Con M2 y el auditor adverso suspendidos por escrito.** |
| **2** | **Mi paquete de §4** (F-2 + F-4 + reubicación del bloque de Nora + H-3), cero palabras | Repara el único criterio de aceptación vivo que el libro incumple, ataca el 25 % de estructura y **cierra una familia entera si sale nulo**. Puede correr en la misma campaña **solo si se acepta que un nulo cierra las dos hipótesis**; si no, va detrás. |
| **3** | **P-1** (el duelo por La Jardinera), ascendida de 3 a 5 | Es la adición del expediente que más se parece a resto. Si la iteración 1 confirma la hipótesis, ésta es la iteración 2. |

### La candidata que el hallazgo nombra, y mi cautela sobre ella

El hallazgo dice: «**CARIES aparece 26 veces, todas referidas: la escena fundacional del libro no está escrita.**» Es cierto y es notable — la palabra que sostiene el eje emocional entero del libro nace en una escena que el lector nunca ve.

**Mi lectura del perímetro, que no sustituye a A7 y que A7 debe emitir antes de que se escriba una línea:** una escena de infancia de las gemelas al piano **no está en los siete noes del §6** — el punto 4 prohíbe la escena de Jean viva *que el lector pueda situar en las semanas anteriores al 26 de noviembre*, y §7.6 corrige expresamente P-82 para dejar claro que «**la prohibición es la datación, no la existencia**». Una tarde sin fecha, con dos niñas de nueve años, no se sitúa en la elipsis.

**Y aquí está mi cautela, que es de las tres preguntas y es seria.** La regla de sucesión pregunta primero: *«¿Qué punto de la Carta mejora esta página?* Si la respuesta es "ninguno: mejora el ritmo, la extensión, o responde a la nota de un crítico", la respuesta es **no**». La respuesta honesta para una escena de CARIES es **ninguno**. **El ángulo 4 ya usó ese argumento para denegar una segunda escena de Jean viva (su D-4) y tiene razón en el razonamiento.**

> **Y aquí es donde declino declinar.** La regla de sucesión se escribió para impedir que alguien reconstruyera la elipsis con la excusa del ritmo. Aplicada a la escena que el libro invoca veintiséis veces y nunca muestra, hace algo que A7 dice expresamente que no quiso: convertir una cláusula de gate en «una prohibición absoluta que yo nunca quise». **A7 ya retiró una regla suya por exactamente este error** —el disparador de reversión del `cap-17`, retirado «por equivocado, no por gastado»— y dejó escrito el criterio: una regla que ordena borrar por el uso de una palabra suelta es «lo único que ese capítulo tiene que temer». **Ésta es la misma situación y hay que ponérsela delante a A7 con esas palabras.** No decido yo. Pero el panel no debe darla por denegada de oficio: **debe pedir el pronunciamiento.**

**Qué se pierde si la escena se escribe y sale bien.** Se gasta la única cosa que este libro invoca sin mostrar y que **sí** puede mostrarse. Después de escribirla, todo lo que quede sin mostrar será material del perímetro, y no habrá una segunda vez. Y hay un riesgo mayor, que es el que de verdad vigilaría: **`CARIES` funciona hoy porque el lector la reconstruye 26 veces y nunca la comprueba.** «Era fea, pequeña y nuestra» (`cap-28`) es más fuerte que cualquier tarde que se pueda escribir. **Escribir la escena puede ser exactamente el error que este libro no comete nunca: ayudar al lector a saber.** Ese es el único argumento contra que me parece de peso, y no es de perímetro: es de oficio, y va en la orden.

---

## 5 · Lo que injertaría de las que no ganan

1. **La compresión por duplicación verificada, toda junta, en el mismo commit** (≈1.100–1.400 palabras, ninguna en la Parte III, ninguna sobre span protegido ni cuenta cerrada):
   - **P-2 (ángulo 5), el mejor anclado del expediente.** El protocolo de aborto de la barca se enuncia tres veces (`cap-37:103`, `cap-39:135`, `cap-41:37`) y el de Jessie cuatro, **y el propio texto contesta a su exposición**: «—Eso he dicho.» / «—Me acuerdo.» / «—Ya lo sé.» Suprimir las preguntas y dejar las réplicas: pasan de acuse de recibo a tensión entre madre e hija. Condición de A5: «Si Aslak pierde fondo, él manda cortar» **debe conservarse en el 39** porque se ejecuta en `cap-41:129`.
   - **P-3 + A3-C6 fundidas** (cap. 40, escena Alana/Henrik, −300). **Por eliminación de réplicas, jamás por resumen narrativizado**, y `cap-40:193` («`CEDIDA POR LA FAMILIA` pasó al montaje definitivo») **es innegociable**. **W9-20 rige: al comprimir es tentador darle a Henrik una línea que lo explique. Prohibido.**
   - **A3-C3** (cap. 19, las tres columnas, −312), **A3-C5** (cap. 18, Madre y Cuchillo, −414), **A3-C7** (cap. 25, primera mitad, −180). Duplicación funcional verificada por `grep` en las tres.
   - **Fuera del injerto: A3-C8** (cap. 11, −177). R5 declara ese capítulo el modelo del libro. **177 palabras no valen una discusión con el perímetro.**
   - **Fuera del injerto, y revocado en §4bis: A3-C2** (cap. 34, −971). Lo que corta es resto, y de resto va escaso este libro.
2. **Del ángulo 2: la inserción única del `cap-44`**, la contabilidad de Jean junto a `4.096 − 1.185 = 2.911`. Sin veredicto, sin comentario, sin que el narrador enuncie la rima (R4). Y su regla explícita: si al medirla por separado el resultado es plano, se conserva solo ésa y se descartan las otras tres.
3. **Del ángulo 4: F-6a**, «Mørketid» absorbida en el subtítulo, si F-1 llega a hacerse. Coste adicional nulo, y arregla que la primera palabra que el lector ve del libro sea una palabra que el libro no dice nunca.
4. **Del ángulo 6: E-5**, una costumbre mental propia por cada adulto con POV. Cero palabras netas, y responde a un defecto que un lector frío nombra: «Los cuatro adultos con punto de vista suenan igual… si tapas los nombres, no sabes quién piensa». **No moverá un eje estancado** —`personajes` y `prosa` ya llegan a 9— pero es barato y no rompe nada.
5. **Del ángulo 6: E-4, la lectura de exactitud noruega y sjøsamisk antes de vender.** No puntúa en ninguna rúbrica y es **la única propuesta de todo el expediente que reduce un riesgo real sobre personas reales**. El `cap-47` y la condición sjøsamisk de Aslak tienen que poder resistir esa lectura, y es mejor que la resistan con nosotros delante.
6. **Del ángulo 5: sus tres declinaciones, como registro permanente.** D-4 (la poda no se dramatiza jamás), D-3 (no se intercambian 46 y 47: rompe la cronología feb-mar/mayo y desarma la viga), D-2 (el `cap-42` no se adelanta: es la factura, y cobrarla antes de comprar destruye el mecanismo por el que el clímax se gana). Y su tabla de **diez anclas de perímetro en la cola 45–48**, que convierte «los capítulos 45 a 48 pueden ser tres» en una decisión de sensibilidad y no de ritmo. **Esa tabla debe pegarse en el informe final:** es la respuesta permanente a una petición que va a volver.

---

## 6 · Lo que hay que declarar techo y dejar de intentar

**Declarados por evidencia suficiente. Se cierran, se escriben en el informe final y no se vuelven a trabajar:**

1. **`premisa`.** Dos críticos, por separado y sin coordinarse, la declaran acotada por el campo y no por el manuscrito: «En 2026, "una conciencia compilada y puesta a trabajar" no es una idea que pueda puntuar 9 por más impecable que sea su ejecución». Diecisiete lecturas la ponen en 8,5 y ninguna intervención la ha movido. **Cerrada.** Y consecuencia operativa: **cualquier propuesta que ponga la premisa más adelante en el libro está trabajando contra el único eje que sabemos que no puede subir** (por eso muere E-3).
2. **`ritmo`.** Misma fuente: «la opacidad de esos capítulos no es un defecto de ejecución sino el efecto buscado… a 9 solo se llegaría escribiendo otra novela». **Y añado el dato que refuerza la declaración desde el otro lado:** la razón que dan es la de los capítulos **interiores**, y las quejas de los lectores son de la cadena **exterior** de documentos. Es decir: aunque se arreglara entero lo que los lectores señalan, **el techo declarado seguiría donde está, porque lo pone otra cosa.** Banda realista 7,5–8,5. **Cerrado como objetivo; abierto como criterio de abandono, que es lo que sí responde.**
3. **La escena de Kongsbakken.** Es literalmente lo que el único lector beta contesta a «¿qué escena falta?»: «La última discusión de Nora con Jean por Kongsbakken… Una sola escena presente, madre e hija peleándose de verdad, me habría dado el peso que el resto del duelo pide prestado». **Y es la escena que el perímetro prohíbe (R3, §6.4, §6.7).** Cerrada para siempre, y **escrita así en el informe final**: la petición más razonada que ha hecho un lector real de este libro es exactamente lo que el libro se ha comprometido a no escribir. Eso no es un defecto pendiente: es el precio que el libro paga a propósito, y hay que decirlo con esas palabras.
4. **«Despedida».** Ya declarado por A7 («queda denegada en el gate y no discutida en el mérito»). Lo repito porque va a volver, y el ángulo 6 predice de dónde: «Va a llegar de marketing, de un editor extranjero y de algún crítico».
5. **La planitud de Henrik Dahl.** W9-20 la declara dispositivo. La nombran el beta y varios críticos, y la seguirán nombrando siempre. **Deja de contar como defecto pendiente.** «Preferencia sí; razón, herida, precio, duda o cansancio, nunca.»
6. **La unanimidad.** «Este libro no va a gustar unánimemente y no debe… Ese descontento es el precio de la columna vertebral del libro, y no es un defecto reparable.» Una parte de los lectores va a experimentar las negativas del libro como evasión. **Cualquier oleada futura que intente arreglar eso estará desmontando «No toda».**

**Y el que NO se puede declarar todavía, que es el importante:**

7. **`global` y `estructura`.** **No pueden declararse techo hoy, y tampoco perseguirse, porque falta el único dato que distinguiría una cosa de otra: el control externo de §4b.3.** 48 lecturas sin pasar de 8,5 sobre todas las versiones prueban que el número no distingue vF de v0; **no prueban que el número pueda emitirse.** Nadie ha comprobado nunca si este jurado, con esta rúbrica, le pone un 9 de global a algo. **Ese experimento vale más que las veintisiete propuestas de esta tabla juntas, cuesta una campaña fría, el plan ordenó que fuera primero y se hizo a medias.** Hasta que se ejecute, «8,5 es el techo del libro» es una hipótesis sin control, exactamente igual que «la uniformidad de capítulo es un defecto» — y este proyecto lleva **once instrumentos** que resultaron medir algo distinto de lo que decía su nombre, todos fallando a la baja y en silencio.

---

## 7 · Si el panel se queda con una sola cosa

> **La forma es correcta, el clímax está donde debe, la cola está ganada y el arranque es de lo mejor que tiene el libro: cuatro de los seis ángulos lo demuestran y yo lo confirmo leyendo. Lo que está mal es más pequeño y más incómodo de lo que ninguno propone: los cuatro capítulos que los lectores de vF señalan son los cuatro que este proceso añadió, cinco de los siete capítulos nuevos no avanzan la trama, y seis oleadas de mejoras han ido añadiendo freno a un libro cuyos ejes atascados son ritmo, trama, estructura y global.**
>
> **Y por eso la iteración 1 no debe sumar *como ha sumado hasta ahora*. Puede comprarse la forma que el ángulo 4 quiere por cero palabras moviendo dos fronteras, reparar por reubicación el único criterio de aceptación vivo que el libro incumple, y cerrar de paso una familia entera de hipótesis. Y antes de nada, ejecutar la mitad del experimento del techo que el plan mandó hacer primero y que no se hizo: es lo único aquí dentro que puede decirnos si el objetivo de la fase existe.**
>
> **Corrección propia, §4bis:** el hallazgo de la fase —el libro no tiene resto, y el propio método lo fabricaba borrando todo lo que no pagaba— **retira mi regla de "no sumar" y la sustituye por otra**: la próxima adición tiene que ser **la primera del proyecto que no pague por nada**, y una adición que traiga etiqueta de función es sospechosa por traerla. Eso convierte E-1 en la apuesta principal y mi paquete de cero palabras en su acompañante. **Y obliga a un acto previo que nadie más ha nombrado: suspender M2 y `auditor-adverso.sh` por escrito para ese material, porque el aparato de verificación de este proyecto está construido para borrarlo y lleva seis oleadas haciéndolo bien.**

---

*Juez A · panel de la iteración 0 · sobre `capitulos/cap-01…48.md` (80.302 palabras, recuento propio), los seis informes de ángulo, `plan-w10.md`, `biblia/b7-perimetro.md`, `informes/w10/estado.json`, el registro de gates del autor y las cuatro lecturas frías de vF · 2026-08-19 · ningún capítulo tocado.*
