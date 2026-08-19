# a6-critico-1 · lectura · FRÍO REAL — 2026-08-19

> Ejecutado con `herramientas/critica-fria.sh` (claude -p desde `/tmp/aa-frio-w10/20260819-164437-a6-critico-1`, fuera del repositorio; system prompt = cuerpo de `.claude/agents/a6-critico-1.md`; sin herramientas, sin CLAUDE.md, sin memoria, sin MCP; entorno de la sesión padre eliminado). Insumo único inline: `compilado/ad-aeternum-vF.md` (sha256 2950755d49cc584e…, 80135 palabras). Instrucción previa: «Eres un crítico literario que puntúa un manuscrito inédito. Escribe en español.

RÚBRICA CON ANCLAS EXPLÍCITAS. Diez ejes, 1–10. Las anclas altas son lo que se te pide calibrar:

- **7** = competente con fallos visibles.
- **8** = notable; fallos menores y localizados.
- **9** = SOBRESALIENTE. Ninguna debilidad estructural en ese eje. Es el nivel de una novela que un editor publicaría sin pedir cambios en ese eje, y que un lector exigente citaría como ejemplo del oficio. **Un 9 NO exige perfección ni genialidad: exige que no haya nada que arreglar.**
- **10** = el eje no admite mejora concebible.

Ejes: (1) Premisa y originalidad conceptual; (2) Arquitectura y estructura; (3) Prosa y estilo; (4) Diálogo; (5) Personajes; (6) Construcción de mundo y verosimilitud; (7) Ritmo y legibilidad; (8) Trama, tensión y clímax; (9) Tratamiento del duelo y del suicidio; (10) Profundidad temática; y (G) NOTA GLOBAL, que es un juicio ponderado y no un promedio.

IMPORTANTE SOBRE LA CALIBRACIÓN: no reserves el 9 para obras maestras. Si un eje no tiene nada que arreglar, es un 9 aunque la obra no te entusiasme. Y si un eje sí tiene algo que arreglar, dilo y no lo pongas en 9 por cortesía.

Devuelve PRIMERO una línea JSON con las once cifras:
{"premisa":X,"estructura":X,"prosa":X,"dialogo":X,"personajes":X,"mundo":X,"ritmo":X,"trama":X,"duelo":X,"tema":X,"global":X}

Y DESPUÉS, obligatoriamente, responde a estas dos preguntas:
1. Para cada eje que hayas puntuado por debajo de 9: **¿qué habría que arreglar, exactamente, para que fuera un 9?** Sé concreto y cita el texto.
2. **¿Hay algún eje en el que creas que este libro no puede llegar a 9 por lo que es, y no por cómo está hecho?** Si lo hay, nómbralo y explícalo.».
> Modelo pedido `claude-opus-5` (esfuerzo max) · tokens por modelo: `claude-haiku-4-5-20251001`: in 162,071 / cache_w 0 / cache_r 0 / out 17; `claude-opus-5`: in 2 / cache_w 0 / cache_r 214,761 / out 16,614 (la llamada auxiliar de haiku es del harness, no del lector) · razonamiento 11078 · coste 0.6848965 USD · 263 s · turnos 1 · stop end_turn
{"premisa":8.5,"estructura":8.5,"prosa":8.5,"dialogo":8.5,"personajes":8.5,"mundo":9,"ritmo":7.5,"trama":8.5,"duelo":9.5,"tema":9,"global":8.5}

## Crítica

**Premisa (8,5).** La emulación póstuma explotada es territorio transitado —Egan, Chiang, *Age of Em*—, y la novela no finge lo contrario. Su originalidad está en el ángulo: no el rescate, sino la contabilidad. «CARGA FUNCIONAL EQUIVALENTE · 2.427,4 AÑOS-JM» (cap. 40) es la mejor idea del libro, un neologismo que convierte la esclavitud en unidad de facturación. Lo mismo la revocación R-1189 firmada horas antes de morir y resuelta «SIN EFECTOS · MOTIVO · INTERRUPCIÓN BIOLÓGICA»: un suicidio que la burocracia lee como fallo de disponibilidad. Resta originalidad la nomenclatura de las instancias —Cuchillo, Nieve, Madre, Coro—, un poco taxonómica, casi psicomaquia.

**Estructura (8,5).** La alternancia interior/exterior está calculada con precisión: el cap. 5 («Flor») llega antes de que sepamos que Jean ha muerto, y el 6 lo confirma retroactivamente. La cuenta atrás a Soldagen sostiene 48 capítulos. Los costes: la Parte IV acumula tres capítulos de preparación logística (37-39) donde bastaban dos, y la trama Gunnar/Hvelv/Kronfjord se abre como thriller y se cierra con un auto que «dejó en blanco al ejecutor». Coherente con la poética del libro; narrativamente, algo desinflado.

**Prosa (8,5).** Disciplina conductista sostenida: emoción producida por objetos, nunca declarada. «La P se había ido lavando hasta quedar en una raya» (cap. 27) hace más duelo que veinte páginas de introspección. El cap. 8 («Turno») —la mano fotografiada sobre el canto de la mesa, la cuartilla con dos nombres tachados— es la cima del libro. El coste: cuando la novela se va al registro jurídico-administrativo (26, 31, 33, 45), la prosa se vuelve informe y pierde el detalle sensorial que la sostiene. Hay algún resbalón sintáctico: «Alana soltó aire por la nariz, y el resoplido le hizo pensar en las gemelas» (cap. 3) descoloca el sujeto.

**Diálogo (8,5).** Idiolectos nítidos. Jean evade por literalidad («—¿Cómo describirías tu carga de trabajo? —Finita»); Alana confiesa su deformación profesional («Lo intentaba. Me ha salido gestión»); Jessie ataca de frente; Nora encadena preguntas. El cap. 11, la sesión con Ranveig, avanza casi entero por negativas —«No lo he contado.» «Entonces no diga "casi todos".»— y es un tour de force. Debilidad: en los capítulos corporativos el diálogo transporta política («El documento contempla explotación bajo supervisión»), y hacia el final el tic de la réplica seca —«Ya.» «Sí.» «No.»— iguala voces que antes eran distintas.

**Personajes (8,5).** Jean mantiene continuidad de carácter viva y muerta: el rigor, la incapacidad de pedir, la negativa a inventar un dato. Mats es el hallazgo: su ELA oculta y la orden de retener los intentos fallidos del banco de voz («Incorpórelos a la retención») lo convierte en alguien que hace a otro exactamente lo que teme para sí. Tomas se define con un objeto —el carné caducado de la operaria a la que hundió cumpliendo el procedimiento—. Contra: Henrik Dahl es un títere sin dimensión, y las instancias interiores funcionan como posiciones éticas más que como personas (Nieve es la excepción; su muerte conmueve).

**Mundo (9).** No encuentro nada que arreglar. La oceanografía es funcional, no decorativa: el residual térmico de AK-7 corregido por fase de marea es *la prueba*. El aparato jurídico noruego (rekonstruksjonsforhandling, midlertidig forføyning, el trilingüe Lyngen/Ivgu/Yykeän) es específico y creíble. Y la mejor escena institucional del libro es el cap. 45: la jueza reduce la ontología de un ser digital a «¿Y quién cambia la bomba?». El daño ocurre siempre en el hueco entre competencias; eso está construido, no afirmado.

**Ritmo (7,5).** El eje más débil. **Dónde estuve más cerca de abandonar: capítulo 15, «Miles».** Introduce cuatro continuidades nuevas en un espacio sin cuerpo, sin lugar y sin tiempo, con el lector aún sin brújula sobre qué está en juego dentro; el efecto es de catálogo, no de escena. Los caps. 30 y 44 exigen relectura. Además, el primer contacto real llega en el 24, pasada la mitad, y la cola tras el clímax ocupa cinco capítulos.

**Trama (8,5). ¿El clímax se gana o se concede?** Se gana. Todo lo que converge en Soldagen está plantado: la digitación de Gunnar, la anomalía de AK-7, la custodia nominal de Tomas, la acreditación de Nora, y la escala del monstruo mencionada como anécdota doméstica en el cap. 3, cientos de páginas antes. Hay una concesión: Tomas acepta con solo tres apariciones previas, y la novela lo sabe (por eso escribe «EL SEGUNDO LO ACEPTA UN DESCONOCIDO»). Lo admirable es que el clímax no resuelve: decir tu nombre activa una custodia estratégica, no te convierte en persona.

**Duelo (9,5). ¿Hay una sola frase que romantice, explique o dulcifique el suicidio?** No. La novela ataca activamente el eufemismo: «No digas que se fue. La gente se va a comprar pan. Mamá se mató. Empecemos por ahí» (cap. 10). Ranveig se niega a dar causa, cifra o significado. El riesgo mayor —que la existencia póstuma funcionara como consuelo— se desarma con «No toda» (cap. 28), con que Nora nunca la llame madre, y con el archivo «Despedida» que se conserva sin abrir. **¿Hay algún capítulo que funcione como homenaje o elegía?** Sí: el 17, «El salero». La frase: «Maja esperó en la puerta hasta que salió del camino.» Matizo que no es puro memorial —el metrónomo que «se calla mientras te equivocas, eso también es participar» es la tesis moral del libro sobre EDDA—, pero su razón de ser primera es dar a Jean viva una escena de amor doméstico.

**Tema (9).** Consentimiento caducado, testimonio y prueba, responsabilidad difusa. El hallazgo político: «No consta responsable individual» aparece el mismo día en dos documentos de instituciones distintas (cap. 31). Y el paralelo con la licencia de 2057, que «evaluó los perjuicios por separado y no sumó la pérdida común», es exacto respecto a la evaluación instancia por instancia. Nunca se subraya.

**Estructura — ¿qué sobra y qué falta?** Sobra la persecución callejera del cap. 14 (parka oscura, restaurante indio, salida lateral): género prestado que la propia novela desactiva cuando el hombre sale de un portal sin reconocerlas. Falta una escena a solas entre Maja y Alana después del depósito: el libro cierra su conflicto con un «Fuera» y luego con cooperación funcional, pero nunca les da la escena de dos mujeres que quisieron a la misma muerta.

**Capítulo que menos empuja el argumento:** el 17, «El salero». Su función: recargar el capital afectivo antes de la Parte III y sembrar los objetos (metrónomo, taza reparada, táper de sopa) que después funcionarán como reliquias en el inventario del cap. 27.

**Maja en tres frases, sin acciones.** Es una mujer cuyo amor tiene forma de logística y cuya ternura solo cabe en el imperativo. Su duelo no ocupa un lugar en la casa porque es la casa entera, sostenida por horarios, recibos y latas de galletas. Ante el Estado sigue siendo esposa por un trámite sin resolver, y esa ironía administrativa es lo más parecido a una herida que permite que se le vea.

**Legibilidad — la regla del capítulo más denso de la Parte II (cap. 15, «Miles»):** todo contacto entre continuidades dura exactamente lo que dure el solapamiento de dos tareas asignadas y se corta sin aviso cuando una de ellas cierra.

---

## 1. Qué habría que arreglar en cada eje por debajo de 9

**Premisa (8,5 → 9).** Sustituir la nomenclatura alegórica de las instancias. «Cuchillo», «Nieve», «Coro» las fija como posiciones morales antes de que actúen; el lector sabe qué son antes de conocerlas. La novela demuestra que puede hacerlo mejor con «La Jardinera» —un nombre elegido por ella, justificado en la tarea que le asignaron («Me asignaron catálogos botánicos y médicos») y que produce sentido en vez de anunciarlo. Con dos o tres nombres derivados así de su asignación productiva, la pluralidad dejaría de leerse como psicomaquia.

**Estructura (8,5 → 9).** Dos cosas. Primera: fundir los caps. 37-39; hay tres capítulos donde uno y medio bastaría, y la enumeración de «UMBRAL 1 / 2 / 3» en el cuaderno de Nora convierte la planificación en checklist. Segunda: la trama Gunnar necesita un cierre que no sea administrativo. «El auto dejó en blanco al ejecutor y al ordenante individuales» es temáticamente correcto, pero el lector ha invertido tres capítulos en once segundos de telemetría y un certificado Hvelv; hace falta una escena —no un párrafo— donde alguien mire a Tomas y decida no responder.

**Prosa (8,5 → 9).** Reducir en un tercio la densidad de bloques monoespaciados en los caps. 30, 42 y 44. Cuando la página se llena de `SIN ASIGNACIÓN`, `RECURSO CONSOLIDADO · SIN DESTINO`, `CERRAR · APRENDIZAJE LOCAL`, el recurso deja de ser textura y pasa a ser sustituto de escritura. Compárese con el cap. 8, donde la misma materia se narra en prosa —«La cinta ha levantado la pintura de la puerta al pegarse dos veces»— y funciona el doble. Corregir además los tres o cuatro sujetos descolocados que señalé.

**Diálogo (8,5 → 9).** Diferenciar la economía de las réplicas por personaje en el último tercio. Ahora mismo Maja, Aslak, Tomas y Astrid comparten el mismo monosílabo. Aslak tiene un modo propio —«Y no mezcles las dos cosas», el conteo en sami, «Si salimos, salimos con la corriente medida, no con vuestros relojes»— que debería contaminar más su presencia en los caps. 39 y 41, donde suena igual que Maja. Y quitar la exposición negociada del cap. 13: Alana explicando SPEIL→CORPUS→MATRIZ→SYNVEV→ARGOS a un consejo que aprobó esa cadena.

**Personajes (8,5 → 9).** Henrik Dahl. Es el único que existe para producir frases infames («Propongo "lanzamiento dedicado a la memoria de Jean Marie Larsson"») y recibir el desprecio del lector. Con dos gestos —el hombre que en el cap. 43 tarda dos indicaciones en entregar el auricular ya apunta a algo— sería un profesional de comunicación aterrorizado, no un maniquí. Igualmente, Ranveig merece una segunda aparición: es el mejor personaje episódico del libro y desaparece tras el cap. 11 sin que la novela vuelva a la cita de «cada quince días» que ella misma establece.

**Ritmo (7,5 → 9).** El arreglo es quirúrgico y conocido: mover material. El cap. 15 debe llegar más tarde y en dos piezas, con Madre y Nieve introducidas en escenas separadas por capítulos exteriores; ahora se presentan cuatro continuidades de golpe en un espacio sin coordenadas. Recortar el cap. 26 (auditoría) a la mitad quedándose con la escena Haldorsen–Vik y el banco de Nora. Y comprimir la cola: los caps. 45, 46, 47 y 48 hacen tres cosas distintas —resolución jurídica, duelo continuado, política costera, epílogo— y podrían hacerlas en tres capítulos. El 47 («Acta») es admirable en su terquedad, pero llegar a una lectura íntegra de acta municipal a cuarenta páginas del final exige del lector una fe que la novela ya no necesita pedir.

**Trama (8,5 → 9).** Plantar a Tomas antes. Aparece en el cap. 19 como voz de Seguridad, en el 29 como investigador y en el 41 como la bisagra de todo el clímax. Basta una aparición más en la Parte II —verlo, por ejemplo, en el momento en que se autoriza el seguimiento del coche gris, y verlo dudar— para que su «ACEPTAR» del cap. 41 sea inevitable en vez de oportuno. Y el mismo trabajo para la fractura de Coro: si la escala del monstruo va a partir a seiscientas ramas, la novela debe mostrar antes al menos una rama que ya venía discrepando por la fotografía familiar, no descubrirla en el momento del efecto.

---

## 2. ¿Hay algún eje que no pueda llegar a 9 por lo que es y no por cómo está hecho?

Sí: **ritmo y legibilidad**. Y hay que decirlo con cuidado, porque no es una excusa para la novela.

Esta obra ha elegido que sus capítulos interiores no tengan cuerpo, lugar, tiempo ni interlocutor estable. Es la decisión correcta —una emulación sin cuerpo no puede narrarse con las herramientas del cuerpo— y produce el mejor material del libro: «Recuerda el peso del gesto, la oscuridad irregular bajo los párpados, la posibilidad infantil de apretar más para hacer desaparecer una habitación. La operación está completa en su memoria, pero falta el órgano que la ejecute.» Pero esa misma decisión priva al lector de las tres anclas con las que gestiona el ritmo: dónde estoy, cuánto llevo, quién habla. Un capítulo puede reordenarse y aligerarse —y he indicado cómo—, pero la fricción residual es constitutiva. La novela pide, estructuralmente, un lector dispuesto a orientarse por identificadores alfanuméricos durante veinte páginas seguidas. Se puede reducir el peaje. No se puede eliminar sin dejar de ser este libro.

Los otros ejes bajos son reparables sin tocar el proyecto. El ritmo lo es solo en parte.
