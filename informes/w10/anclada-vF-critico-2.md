# a6-critico-2 · lectura · FRÍO REAL — 2026-08-19

> Ejecutado con `herramientas/critica-fria.sh` (claude -p desde `/tmp/aa-frio-w10/20260819-164437-a6-critico-2`, fuera del repositorio; system prompt = cuerpo de `.claude/agents/a6-critico-2.md`; sin herramientas, sin CLAUDE.md, sin memoria, sin MCP; entorno de la sesión padre eliminado). Insumo único inline: `compilado/ad-aeternum-vF.md` (sha256 2950755d49cc584e…, 80135 palabras). Instrucción previa: «Eres un crítico literario que puntúa un manuscrito inédito. Escribe en español.

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
> Modelo pedido `claude-opus-5` (esfuerzo max) · tokens por modelo: `claude-haiku-4-5-20251001`: in 162,071 / cache_w 0 / cache_r 0 / out 17; `claude-opus-5`: in 2 / cache_w 0 / cache_r 214,761 / out 24,528 (la llamada auxiliar de haiku es del harness, no del lector) · razonamiento 19740 · coste 0.8827465 USD · 366 s · turnos 1 · stop end_turn
{"premisa":8.5,"estructura":8,"prosa":8.5,"dialogo":8,"personajes":8.5,"mundo":9,"ritmo":7.5,"trama":8,"duelo":9.5,"tema":8.5,"global":8.5}

**Premisa (8,5).** El subgénero está saturado —Egan, Chiang, *Age of Em*, la televisión— y la novela lo sabe: no intenta que la idea de la mente compilada sorprenda. Su originalidad está en la contabilidad. La unidad «años-JM» (cap. 23: «CORTE 19-DIC · 979,7 AÑOS-JM», definida como «el tiempo mediano que Jean Marie habría necesitado para completar una dificultad equivalente») es una invención de primer orden: convierte la esclavitud en un renglón de coste trimestral. También lo son R-1189 —una revocación eficaz desde su recepción, resuelta «SIN EFECTOS · INTERRUPCIÓN BIOLÓGICA»— y NORNA como desenlace: no fuga ni rescate, sino esterilización del molde. Lo que baja la nota es el andamiaje heredado: consejo, fondo, fecha de lanzamiento, ingeniero asesinado.

**Estructura (8).** La cuenta atrás a Soldagen sostiene bien 48 capítulos, y el relevo de CARIES (cap. 3 → 12 → 18 → 28) y el de la cuarta nota (24) hasta la quinta (44) están cronometrados con precisión. Lo que sobra: la confrontación de la gasolinera en el cap. 29. Duplica exactamente la función de «Fyret» (cap. 19) —Jessie actúa, genera un registro contra sí misma, Maja administra el daño— y su único fruto, la notificación del 3 de enero, podía entregarse sin escenificarla. Lo que falta: una escena de Jean y Nora solas en el presente de la Parte I. La novela la instala y la esquiva («—Podrías llamarla esta tarde. —Podría.»); el resultado es que nuestra inversión en Jean como madre es enteramente prestada por las hijas. El capítulo que menos empuja el argumento es el 47, «Acta»: su función es dar cuerpo a la desposesión fuera de la familia Larsson y negarnos el veredicto —probar que la forma institucional que consumió a Jean es anterior a ella y la sobrevive.

**Prosa (8,5).** Hay una ética de estilo, no un adorno: el objeto hace el trabajo que la novela le prohíbe al adjetivo. «El recogedor cojeaba porque conservaba una abolladura en una esquina. Cada pasada dejaba escapar una franja» (cap. 4) es disociación sin nombrarla. Los capítulos interiores encuentran un idioma propio —«Le han asignado luz en una posición» (cap. 5)— que evita la metáfora corporal en un ser sin cuerpo. Contra: el método se vuelve manierismo hacia el cap. 39; hay deslices de foco («Alana soltó aire por la nariz, y el resoplido le hizo pensar en las gemelas», cap. 3, en capítulo de Jean); y tres veces el narrador enuncia la tesis que el resto del libro se niega a decir («Jean Marie Larsson reducida a una celda», cap. 13).

**Diálogo (8).** Ranveig (cap. 11) es el mejor personaje episódico del libro por lo que no dice: «—¿Casi todos son cuántos? —No lo he contado. —Entonces no diga “casi todos”. —De acuerdo». Jessie tiene voz propia y sostenida («Como si hubiera perdido un puto autobús»). El problema es el registro único: Ranveig, Astrid, Aslak, la tutora, Tomas y la funcionaria comparten la misma sintaxis de frase corta y negativa seca. Mats habla solo en aforismos («El calendario es el contrato»), lo que lo vuelve gerente de tesis.

**Personajes (8,5).** Jean está construida con exactitud desde dentro y desde antes: el instante en que disfruta de un acierto y calcula el daño que habría causado su ausencia —«Se avergüenza» (cap. 7)— vale más que veinte páginas de introspección. Nora invalidando su propia flecha ante Astrid (cap. 26) es el mejor gesto de carácter de la novela. Maja, en cambio, sostiene el libro y es la menos interior: su duelo está delegado íntegramente a objetos. Mats es delgado. *Maja en tres frases sin acciones:* Es una mujer para quien el mundo se ordena en instrumentos, series y responsabilidades, y a quien la pena le llega siempre con retraso, cuando ya no queda nada práctico donde ponerla. Su lealtad es administrativa antes que efusiva: la clase de amor que consiste en no perder un plazo, no mentirle a una hija y no reclamar para sí un duelo que cree ajeno. Bajo el orgullo profesional de quien firma sus datos hay una vergüenza sorda por el matrimonio que se estaba disolviendo en formularios cuando llegó la llamada.

**Mundo (9).** No encuentro nada que arreglar. La geografía de Tromsø y Lyngen está vivida, no consultada; el aparato jurídico noruego se usa con corrección y sin turismo; el membrete trilingüe del cap. 47 y Aslak tachando «ASISTENTE» para exigir «PATRÓN / COLABORADOR DE CAMPO» (cap. 19) valen por un capítulo de contexto. La oceanografía —CTD, ADCP, la pluma pegada al relieve, el traslado de 400 m que descarta el sensor— es rigurosa, y el sabotaje del cap. 41 produce exactamente lo que la física permite: «Ni humo, ni oscuridad, ni la clase de ruido que en una película habría permitido saber que algo importante acababa de ocurrir».

**Ritmo (7,5).** *¿Dónde estuve más cerca de abandonar?* En el cap. 36, «La asamblea». Llega en la presión máxima de la Parte III y gasta su extensión en el reglamento de una votación —quórum, deduplicación, papeletas incompletas— entre entidades cuya individuación el lector aún no consigue sostener. Segundo candidato: el cap. 9, tras un cap. 8 igualmente interior. *Regla del capítulo más denso de la Parte II (15, «Miles»):* ninguna continuidad puede hablar con otra salvo en el borde de una tarea compartida y a costa del margen que necesitaría para trabajar, de modo que cada conversación se paga con una salida y termina cuando la tarea la reclama.

**Trama (8).** *¿El clímax se gana o se concede?* Se gana en lo que importa y se concede en lo que lo hace posible. La red sobre la toma está sembrada en 22, 32 y 39 y rinde exactamente lo poco que debe rendir; la escala de Nora se gana desde el cap. 3. Pero el acceso físico depende de que Tomas Eide, presentado en el cap. 29, acepte a las 12:46:01 con una cobertura que caduca a las 12:47, y de que un repetidor local entre en la mezcla pública de un lanzamiento mundial. Eso es coreografía, no consecuencia.

**Duelo (9,5).** No hay una sola frase que romantice, explique o dulcifique el suicidio; la busqué. El acto no se describe, el lugar no se lirifica, el «¿Sufrió?» de Maja queda sin respuesta —«No podemos determinarlo con la información de la que disponemos» (cap. 6)—, Ranveig repite «No lo sé» sin ablandarlo, y el archivo «Despedida» nunca se abre: «No abrió el archivo» (cap. 46). Las líneas que podrían acusarse —la de EDDA sobre la «utilidad esperada» (cap. 30)— explican el cálculo de la empresa, no la muerte. *¿Hay capítulo-homenaje?* Sí: el 17, «El salero». Su razón de ser es enseñarnos a Jean viva; la frase que me lo hace pensar es «—He tocado sesenta veces tarde. Es distinto». (No puntúa.)

**Tema (8,5).** La rima entre la desposesión sjøsamisk y la de Jean —una licencia que evaluó los perjuicios por separado «y no sumó la pérdida común»— es el mejor movimiento del libro, y Aslak la protege de la alegoría fácil: «A nosotros nos quitaron paso y uso. A Jean le hicieron otra cosa» (cap. 32). Igual de sólido es el problema del cap. 9: «lo que vuelve sin el acto de elegirlo no se distingue de lo propio». Resta que tres veces la novela entrega la interpretación ya masticada, y que el paralelo Mats/ELA se presenta en columnas contiguas de la misma pantalla.

**Tres mejoras de mayor rendimiento.** (1) Resolver la puerta: o Tomas se siembra desde el lado de la familia con veinte páginas de antelación, o se elimina el acceso físico y el canal se abre desde dentro, para que el clímax no dependa del minuto de un desconocido. (2) Comprimir la Parte III interior: fundir 30 y 36 y dramatizar la asamblea a través de la decisión de una sola continuidad, no de su reglamento. (3) Darle a Maja un capítulo de interioridad que no esté delegado a objetos; la semilla está en el cap. 27 y la novela la abandona en dos líneas: «Maja dijo que había otro en el altillo. / No lo había».

---

**1. Qué habría que arreglar en cada eje por debajo de 9**

*Premisa (8,5).* Retirar el andamiaje de thriller heredado, en concreto la muerte de Gunnar. La originalidad del libro es burocrática; el coche saboteado importa un reflejo de género que el resto de la novela no necesita. Si a Gunnar lo silencia un procedimiento —una pérdida de acceso, una reasignación, una incidencia derivada a Seguridad— en vez de un certificado hoja de Hvelv, la premisa deja de pedir prestado.

*Estructura (8).* Tres cortes: suprimir la gasolinera (cap. 29) y entregar la notificación del 3 de enero sin escenificarla; escribir la escena ausente de Jean y una hija en la Parte I; y fundir el coda de cuatro capítulos (45–48) en dos, absorbiendo el 47 dentro del 45.

*Prosa (8,5).* Corregir los deslices de foco (cap. 3, «le hizo pensar»), eliminar las tres tesis narradas («reducida a una celda», cap. 13) y romper la cadencia una vez por capítulo en la segunda mitad: a partir del 39 el lector predice el ritmo de cualquier párrafo antes de leerlo.

*Diálogo (8).* Diferenciar registros. Ahora mismo Ranveig, Astrid, Aslak, la tutora y la funcionaria comparten longitud de frase y relación con la pregunta. Bastaría con dar a dos de ellos una sintaxis distinta y quitarle a Mats el aforismo: que argumente mal una vez.

*Personajes (8,5).* Maja necesita una escena de conciencia propia, no de gestión; y Mats necesita un momento en el que no controle la sala —hoy sale del libro sin perder la compostura una sola vez.

*Ritmo (7,5).* Cuatro atascos (9, 30, 36, 47), una carga de siglas y códigos que ningún lector puede sostener sin releer, y seis capítulos de la Parte III en los que la familia desaparece. Comprimir los interiores y devolver a Nora o Jessie al menos un capítulo entre el 26 y el 33.

*Trama (8).* La puerta y el repetidor. Mientras el canal público dependa de un enlace local no autenticado en una empresa que acaba de exhibir cadenas CE-K y procedimiento *break-glass*, el clímax se sostiene por permiso del autor.

*Tema (8,5).* Cortar las tres formulaciones explícitas y separar el paralelo Mats/ELA: que las dos columnas no compartan pantalla.

*Global (8,5).* Consecuencia de lo anterior; con esas correcciones el libro subiría de golpe.

**2. ¿Hay un eje que no pueda llegar a 9 por lo que el libro es?**

Sí: **premisa y originalidad conceptual**. Su techo lo fija el campo, no el manuscrito. En 2026, «una conciencia compilada y puesta a trabajar» no es una idea que pueda puntuar 9 por más impecable que sea su ejecución; Egan, Chiang y una década de televisión ya la ocuparon. Esta novela hace lo único honesto que se puede hacer con una premisa gastada —administrarla mejor que nadie, con la unidad «años-JM», R-1189 y NORNA— pero eso es originalidad de segundo orden. Todos los demás ejes son alcanzables por revisión.

Matiz sobre **ritmo**: parte de su problema también es constitutivo. Un libro que se niega a darle a la continuidad un cuerpo, una habitación o una metáfora no puede hacer propulsivo el cap. 9 sin mentir sobre lo que describe. Pero ahí sí hay salida: la aridez es defendible; la *reiteración* de la aridez no lo es. Ese eje sube a 9 por compresión, no por traición.
