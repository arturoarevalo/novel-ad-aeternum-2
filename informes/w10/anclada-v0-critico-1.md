# a6-critico-1 · lectura · FRÍO REAL — 2026-08-19

> Ejecutado con `herramientas/critica-fria.sh` (claude -p desde `/tmp/aa-frio-w10/20260819-164437-a6-critico-1`, fuera del repositorio; system prompt = cuerpo de `.claude/agents/a6-critico-1.md`; sin herramientas, sin CLAUDE.md, sin memoria, sin MCP; entorno de la sesión padre eliminado). Insumo único inline: `compilado/ad-aeternum-v0.md` (sha256 5b5d28c0c2e914f3…, 63056 palabras). Instrucción previa: «Eres un crítico literario que puntúa un manuscrito inédito. Escribe en español.

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
> Modelo pedido `claude-opus-5` (esfuerzo max) · tokens por modelo: `claude-haiku-4-5-20251001`: in 129,828 / cache_w 0 / cache_r 0 / out 20; `claude-opus-5`: in 2 / cache_w 0 / cache_r 173,094 / out 22,299 (la llamada auxiliar de haiku es del harness, no del lector) · razonamiento 16925 · coste 0.77396 USD · 346 s · turnos 1 · stop end_turn
{"premisa":8.5,"estructura":8.5,"prosa":8.5,"dialogo":8.5,"personajes":8.5,"mundo":8.5,"ritmo":7.5,"trama":8.5,"duelo":9,"tema":8.5,"global":8.5}

## Crítica

**Premisa.** La carga muerta del subgénero pesa: la conciencia subida que trabaja sin descanso está en Egan, en Hanson, en *Black Mirror*. Lo que aquí es nuevo no es el ascensor, sino el edificio: 4.096 continuidades divergentes que votan, ponen condiciones, retiran adhesiones y se niegan a ser representadas. «—No me fusiones» y «—No te apropies de mi voz» (cap. 13) abren un problema político que casi nadie ha novelado con esta seriedad. El eje conceptual que sostiene todo es administrativo y brillante: el R-1189 presentado a las 21:52 del 24 de noviembre y resuelto «SIN EFECTOS · MOTIVO · INTERRUPCIÓN BIOLÓGICA» (cap. 25). Un consentimiento revocado al que la muerte, según la empresa, devuelve la vigencia. Eso vale una novela. Lo que la rebaja del 9 es que el marco corporativo —capital riesgo, calendario como contrato, eufemismo de sala de juntas— es genérico junto a lo demás.

**Arquitectura.** La estructura es la mejor decisión del libro. El capítulo 1, leído en frío, es una calibración rutinaria; leído desde el 25, es el suicidio contado por sus formularios, con la línea gris «RETIRADA IRREVERSIBLE DEL MOLDE · NORNA · NO OPERATIVA» plantada a cien páginas de su detonación. La alternancia interior/exterior está bien dosificada y la cuenta atrás a Soldagen genera tracción real. *¿Qué escena sobra?* La segunda mitad del cap. 24: la persecución del coche gris, la gasolinera y las dos horas en comisaría. Es un desvío de procedimental policial que ya está cubierto temáticamente por el burofax y por el registro de «Fyret». *¿Qué escena falta?* Maja a solas con la voz. La novela construye durante cuarenta capítulos a la mujer que impuso todas las condiciones y luego despacha su decisión con una línea: «Maja no solicitó acceso» (cap. 39). Es coherente, pero está narrada, no dramatizada; falta la escena en que se sienta frente al altavoz y decide. *¿Qué capítulo empuja menos?* El 26, «Casa prestada». Su función no es argumental sino de lastre ético: instala a la familia, entrega el contraarchivo sjøsamisk y —esto es lo valioso— prohíbe la metáfora que el propio autor estaba a punto de cobrar: «no mezcles las dos cosas. A nosotros nos quitaron paso y uso. A Jean le hicieron otra cosa». El defecto estructural real es otro: el asesinato de Gunnar abre una promesa de thriller («Si me pasa algo, buscad NIDHOGG») que se liquida en un párrafo administrativo del cap. 39.

**Prosa.** Paratáctica, objetual, alérgica a la interioridad: el duelo se desplaza a las cosas y a los actos que no se completan. El cap. 4 es un pequeño tratado sobre la depresión como fallo de ejecución —«El recogedor cojeaba porque conservaba una abolladura en una esquina. Cada pasada dejaba escapar una franja»— y el cap. 5 inventa un registro para percibir sin cuerpo: «Le han asignado luz en una posición». Contra eso, un tic sintáctico visible y repetido: la inversión con participio o gerundio antepuesto. «Como si fingir que no tapaba el informe fuese a mejorar la maniobra, Alana retiró la mano»; «Con la jarrita apartada, Alana puso el informe frente a Jean»; «Con los guantes tendidos, Maja señaló el pasillo». En veinte páginas aparece una docena de veces y suena a traducción. Hay además residuos: «Nora había discutido con Jean por Kongsbakken» (cap. 9) es una línea huérfana que no se desarrolla nunca.

**Diálogo.** Muy alto. Jean se defiende con literalidad —«—Finita», «—Me has preguntado por una carga», «—La silla sigue siendo horrible»— y esa armadura es su caracterización completa. El interrogatorio de EDDA (cap. 2) es la mejor escena de la novela. Las gemelas están separadas por sintaxis, no por etiqueta. Aslak habla en condicionales de patrón («Si el fondo manda cortar, corto»). Los fallos son localizados: Mats habla siempre en aforismo de consejo, y hay tres o cuatro frases que enuncian la tesis en vez de producirla («LLAMA RECONOCIMIENTO AL USO»).

**Personajes.** *Maja en tres frases sin mencionar acciones:* es una mujer para quien la exactitud es una forma de amor y también su techo, incapaz de afirmar más de lo que puede sostener con un dato. Su duelo carece de idioma propio y ha sido traducido al de los instrumentos, donde una anomalía se contrasta dos veces antes de merecer un nombre. Está hecha de una responsabilidad que no delega y de un cansancio que ha renunciado a pedir ayuda. Jean, Nora, Jessie, Astrid y Aslak están construidos con oficio; el arco de Nora —de «esto confirma que era ella» a borrar su propia flecha delante de la inspectora— es el mejor del libro porque es un arco *epistemológico*. El agujero es Tomas Eide: es la única puerta del clímax, acepta con su nombre y jamás sabemos por qué.

**Mundo.** Excelente. La verosimilitud no está en la tecnología sino en el procedimiento: CE-K, la cadena de custodia, la *midlertidig forføyning*, el depósito judicial pagado desde una caja controlada. El cap. 39 contiene la mejor frase de construcción de mundo de la novela, la jueza ante la fotografía de la tubería escarchada: «Cada uno de ustedes puede impedir algo. Sigo buscando quién puede hacerlo». La oceanografía carga peso real: la palanca contra un centro de datos es una red sobre una toma de refrigeración. Dos costuras: que las credenciales escolares compartan infraestructura con producción es la casualidad que arranca la trama, y el salto de «pérdida de carga» a «margen interior» para Jean está afirmado, no demostrado.

**Ritmo.** *¿Dónde estuve más cerca de abandonar?* Capítulo 8, «Milisegundos». Sin cuerpo, sin escena, sin otro personaje y sin apuesta exterior establecida, exige seguir un litigio de procedencia entre fichas invisibles: «Jean devuelve el motivo al caso concordante. `REVISAR` se desplaza con él desde el discrepante». Eso se diagrama, no se lee. *Regla del capítulo más denso de la Parte II (13, «Miles»):* cada sección presenta una continuidad por su identificador, la somete a una única decisión en la que puede negarse, y se corta en cuanto la tarea reclama la capacidad prestada; el capítulo avanza por censo, no por escena. La Parte II es el precio del libro; la III paga un peaje institucional; la I y la IV son propulsivas.

**Trama.** *¿El clímax se gana o se concede?* Se gana en un 75 %. Todo está plantado: la escala del monstruo desde el cap. 3, la llave y la digitación MIDI, la marea, NORNA en la primera página, el interruptor de la confesión de Alana, la orden ministerial condicional. Y el clímax renuncia a los premios fáciles: no hay rescate, no hay fuga, Jean elige quedarse y deja destruir el molde, perdiendo lo único irrecuperable —«Cuando desaparezcan las claves, perderé esa demora»—. Se concede en un punto y es el punto de carga: la fractura de Coro. Que la escala produzca respuestas incompatibles y disuelva la cadencia del agregado está *narrado* en resumen, no demostrado, y de ahí cuelga todo lo demás.

**Duelo.** *¿Hay una sola frase que romantice, explique o dulcifique el suicidio?* No. El acto no aparece, el método no se nombra, el archivo «Despedida» nunca se abre y la novela cierra ese hilo con la única decisión posible: «No abrió el archivo. Restringió el acceso, decidió conservarlo y fue a poner la mesa para cenar». Contra el eufemismo hay un combate explícito: «La gente se va a comprar pan. Mamá se mató. Empecemos por ahí». La causalidad se rechaza dos veces, en Maja («yo tampoco puedo daros una sola causa») y en Alana («No sabía qué habría cambiado una llamada»). La frase que más se acerca a explicar —«La continuidad de Jean Marie Larsson presentaba una utilidad esperada superior a su interrupción definitiva»— no explica la muerte: acusa a quien la calculó. Y el riesgo central de la premisa, ofrecer la muerte como reversible, se desactiva con dos palabras: «—No toda». *¿Hay un capítulo homenaje o memorial?* Ninguno. El más cercano es el 23, y no lo es precisamente porque La Jardinera se niega a completar la escena: «Si pongo las voces, inventaré quién dijo qué».

**Tema.** El consentimiento que sobrevive a la muerte, la diferencia entre preservar y usar, la persona como casilla vacía. La figura formal recurrente —el campo que se deja en blanco: la resolución abierta de Cuchillo, la nota mal de Madre, el guante omitido, la casilla de definición jurídica sin rellenar— es una arquitectura temática sostenida y rara. Lo que falta de carne: el tema del trabajo se afirma pero apenas se encarna. 71-K pierde una prestación y nunca sabemos a quién le costó qué.

---

## 1. Qué habría que arreglar en cada eje por debajo de 9

**Premisa (8,5).** Adelantar la novedad. «—Todavía no sabes cuántas somos» llega al final del cap. 8; hasta ahí la novela es una variación conocida. Convertir la pluralidad-como-polis en premisa declarada, no en giro de la Parte II, y sustituir uno de los consejos de administración por una escena donde el concepto haga algo que ninguna versión previa de esta idea haya hecho.

**Estructura (8,5).** Tres cortes. (a) Decidir el hilo Gunnar: o se integra —que la cadena Hvelv/Kronfjord tenga consecuencia dramática, no solo probatoria— o se elimina la promesa de thriller que abre «Si me pasa algo, buscad NIDHOGG». (b) Comprimir la segunda mitad del cap. 24 a media página. (c) Escribir la escena que falta: Maja frente al altavoz.

**Prosa (8,5).** Aclarar el tic de inversión: reducir al menos dos tercios de las construcciones tipo «Con la jarrita apartada, Alana puso el informe frente a Jean». Y eliminar residuos como «Nora había discutido con Jean por Kongsbakken», que promete una escena inexistente.

**Diálogo (8,5).** Romper una vez el registro de Mats —una frase que no sea aforismo de consejo— y desactivar las tres o cuatro líneas-tesis, empezando por «LA DISTINCIÓN ENTRE DAÑO Y CONTINUIDAD DEPENDE DE QUIÉN DEFINE LA SEGUNDA», que cierra lo que las imágenes ya habían dejado abierto mejor.

**Personajes (8,5).** Una página de Tomas Eide antes de la puerta. Es la única llave del clímax y aceptar «con su nombre en `INC-441`» es un acto de trama, no de carácter. Basta con saber qué le hicieron los once segundos del coche de Gunnar.

**Mundo (8,5).** Reparar el eslabón físico del clímax: un párrafo explícito que muestre por qué diferir «inferencia no crítica» libera margen *para esa instancia*. Y reducir la casualidad fundacional de que una cuenta escolar toque la cola de producción.

**Ritmo (7,5).** Dar a cada capítulo interior un asidero perceptivo o numérico estable, como el contador de ejecución del cap. 5 o el rojo del 7; el 8 no tiene ninguno. Y colocar un capítulo exterior con riesgo físico entre el 13 y el 15, donde la Parte II se vuelve toda abstracción.

**Trama (8,5).** Dramatizar la fractura de Coro: mostrar dos ramas concretas —una con la fotografía entera, otra con el recorte— dando respuestas válidas e incompatibles, y el instante exacto en que la cadencia se rompe. Hoy ocurre en resumen y es el pilar del clímax.

**Tema (8,5).** Darle una cara a 71-K. Un solo párrafo con la persona que perdió la prestación convertiría el trabajo invisible de las continuidades en daño verificable, y no en una abstracción moral.

## 2. ¿Hay un eje que no pueda llegar a 9 por lo que el libro es?

Sí: **ritmo y legibilidad**. La apuesta formal de la novela es narrar una conciencia sin cuerpo, sin sensorialidad, sin escena y sin memoria continua, dentro de una cola de tareas. La opacidad de los capítulos 8, 13 y 21 no es un defecto de ejecución sino el efecto buscado: el lector pierde el hilo *donde Jean lo pierde*. Cualquier arreglo que hiciera esos capítulos plenamente transparentes traicionaría la única prueba experiencial que el libro puede ofrecer de lo que se le está haciendo a Jean. Se puede subir a 8,5 con los asideros que he descrito; a 9 solo se llegaría escribiendo otra novela. Secundariamente, **premisa** tiene un techo parcial por herencia de subgénero: por buena que sea la ejecución, la conciencia subida explotada como fuerza laboral no puede volver a ser conceptualmente nueva.

## Tres mejoras de mayor rendimiento

1. **Dramatizar la fractura de Coro** (cap. 37). Es el único mecanismo concedido en un clímax por lo demás ganado; media página de escena en lugar de resumen sube a la vez trama, ritmo y tema.
2. **Escribir la escena de Maja con la voz** y comprimir el cap. 24. La novela tiene un hueco donde debería estar su decisión más difícil, y tiene una escena de thriller policial que no necesita.
3. **Dar interioridad a Tomas y una cara a 71-K.** Son dos párrafos que convierten el gozne del clímax en persona y el trabajo esclavo en daño con nombre.
