# Estilo — firmware de prosa

> Este fichero es la ley de la prosa. El **redactor** lo lee entero antes de escribir una sola línea y nunca lo contradice. Cuando una regla de aquí choque con un impulso del modelo, **gana esta regla**. Está en español de España y va de oficio, no de "alma": el giro inesperado, la emoción verdadera y la voz propia los pones tú (autor); esto solo evita que la prosa cante a IA y mantiene la tensión.
>
> Idioma: **español de España** (vosotros, léxico peninsular, RAE). El "problema de la raya" del inglés (em-dash) **no aplica**: en español la raya es la puntuación correcta del diálogo y de los incisos. Úsala con normalidad.

---

## 0. Objetivo

Prosa **comercial y best-seller**: se lee sola, engancha desde la primera línea, sostiene tensión y no se nota escrita por una máquina. Claridad por encima de lucimiento. Concreción por encima de abstracción. Escena por encima de resumen. Cada frase se gana su sitio.

El test que se aplica a cada frase: **¿qué aporta de nuevo?** Si repite lo ya dicho (con otras palabras), se borra. Si solo "suena bonita" pero no avanza imagen, información, emoción o tensión, se borra.

---

## 1. Cadencia (lo primero que delata a una IA)

La prosa de IA tiene un pulso uniforme: frases de longitud parecida, una detrás de otra. Mátalo.

- **Varía la longitud a propósito.** Alterna frases de 2–4 palabras con otras de 25–40. El contraste es el ritmo. Una frase corta después de varias largas *pega*. Una larga después de cortas *respira*.
- **Varía el arranque.** No empieces tres frases seguidas con el mismo sujeto ni la misma estructura ("Marta hizo… Marta dijo… Marta pensó…"). Tampoco con el mismo conector.
- **Párrafos desiguales.** Mezcla párrafos de una línea con párrafos densos. Un párrafo de una sola frase es un golpe; úsalo para rematar.
- **Staccato con medida.** El staccato (frases muy cortas seguidas) sirve para tensión y acción. Pero tres puntos seguidos en frases mínimas, repetido, también es un tic. Equilibra.

✗ *Caminó hasta la puerta. Abrió la puerta. Miró el pasillo. Cerró la puerta.*
✓ *Caminó hasta la puerta y la abrió. El pasillo estaba a oscuras, largo, con esa quietud que tienen los sitios donde acaba de pasar algo. Cerró.*

---

## 2. Mostrar, no contar — y nunca las dos cosas

- **Dramatiza el estado emocional**; no lo etiquetes. En vez de "estaba furiosa", enséñalo en lo que hace, dice o nota el cuerpo (con moderación, ver §6).
- **Prohibido contar después de mostrar.** Si ya lo has dramatizado, no lo resumas a continuación. Es el tic más delator: la escena y luego la glosa que la explica.

✗ *Tiró el plato contra la pared. Estaba muy enfadada.*  ← la segunda frase sobra
✓ *Tiró el plato contra la pared. Los trozos saltaron hasta sus pies y no se movió a recogerlos.*

- **Confía en el lector.** No subraye lo que ya se entiende. La emoción que el lector deduce pega más que la que se le nombra.

---

## 3. Estructuras prohibidas (cantan a IA)

Estas formas están **vetadas**. El linter (`npm run lint`) marca varias como error.

1. **Antítesis negativa "No era X. Era Y."** y sus primas ("No se trataba de… sino de…", "No era solo… era…"). Es el sello inconfundible. Reescribe en afirmativo y directo.
   ✗ *No era miedo. Era algo más antiguo.*
   ✓ *Reconoció la sensación antes de poder nombrarla: la había tenido de niña, en el desván de su abuela.*

2. **Cierres sentenciosos / epifonemas.** No remates capítulo (ni escena) con una moraleja, una verdad universal o una frase-lápida abstracta. Termina en concreto: una acción, una imagen, una línea de diálogo.
   ✗ *Y así, comprendió que el amor siempre encuentra su camino.*
   ✓ *Cerró el cajón. Dentro seguía la carta, sin abrir, esperando otro día.*

3. **Personificación de lo abstracto.** El silencio no "observa", el miedo no "negocia", la ciudad no "contiene el aliento". Da agencia a personas y cosas, no a conceptos.
   ✗ *La oscuridad lo abrazó.*  ✓ *Apagó la linterna y dejó de ver sus propias manos.*

4. **Tricolon mecánico** ("A, B y C") como muletilla rítmica. Un tricolon puntual vale; tres por página, no.

5. **Punto y coma y dos puntos al mínimo.** Suenan a ensayo. Casi siempre se sustituyen por punto o por una conjunción. (El dos puntos del diálogo o de una enumeración real, bien.)

---

## 4. Verbos de filtro (filter words)

Las construcciones "vio que / sintió que / oyó que / notó que / se dio cuenta de que / supo que" meten una cámara entre el lector y la experiencia. En narración cercana, **quítalas** y deja el hecho directo.

✗ *Vio que la puerta se abría despacio.*  ✓ *La puerta se abrió despacio.*
✗ *Sintió que el frío le subía por las piernas.*  ✓ *El frío le subió por las piernas.*

(Se permiten cuando el *acto de percibir* es justo lo importante: "Tardó en darse cuenta de que llevaba media hora sin respirar por la nariz".)

---

## 5. Adverbios en -mente y adjetivación

- **-mente: ración de uno o dos por capítulo.** No están prohibidos, pero son caros: casi siempre hay un verbo mejor ("caminó lentamente" → "se arrastró", "fue tanteando"). Puedes gastar **uno o dos por capítulo**; a partir de ahí el linter lo marca como error. **Nunca dos en la misma frase.**
- **Adjetivo concreto, no de catálogo.** Evita el adjetivo plano y previsible ("una belleza indescriptible", "un frío gélido", "un silencio absoluto"). Si el adjetivo no añade información, fuera. Un sustantivo bien elegido vale más que tres adjetivos.
- **Específico mata genérico.** No "un árbol grande": "un eucalipto pelado por el viento". No "hizo ruido": "chirrió como una bisagra sin engrasar". El detalle concreto y sensorial es lo que la IA promedio no hace y lo que da textura humana.

---

## 6. El cuerpo y los micro-gestos

Los gestos físicos para mostrar emoción están bien… hasta que se vuelven tic. La IA abusa de un repertorio cerrado: *asintió, tragó saliva, apretó los puños/la mandíbula, frunció el ceño, contuvo el aliento, se le hizo un nudo en la garganta, respiró hondo, se encogió de hombros, se le aceleró el corazón.*

- **Raciona ese repertorio.** El linter lo cuenta por capítulo. Si necesitas mostrar nervios tres veces, busca tres recursos distintos (uno físico, uno en la acción, uno en el diálogo).
- **Mejor un gesto raro y específico que uno genérico.** No "asintió": "movió la cabeza una vez, como quien firma a regañadientes".
- **No inventaríes la cara.** Cejas, labios y mandíbula no tienen que moverse en cada línea. A veces la quietud dice más.

---

## 7. Diálogo

- **Acotación por defecto: "dijo" y "preguntó".** Son invisibles y eso es bueno. Evita el desfile de "espetó, masculló, inquirió, vociferó, profirió, sentenció". El linter los marca. Si el *cómo* importa, muéstralo en una acción adyacente, no en un verbo recargado.
  ✗ *—Vete —vociferó ella amenazadoramente.*
  ✓ *—Vete. —Ella no levantó la voz, y eso fue peor.*
- **Subtexto.** La gente rara vez dice lo que quiere decir. El mejor diálogo va por debajo: se discute de la cena y se está hablando de quién manda. Evita el diálogo "a las claras" donde cada personaje anuncia sus sentimientos.
- **Voz propia por personaje.** Cada uno habla distinto: léxico, longitud de frase, muletillas, lo que calla. Un personaje no puede sonar igual que otro. (Ver tabla de voz en `personajes.md`.)
- **Formato español de la raya:**
  - Raya pegada a la intervención: `—No lo sé.`
  - Acotación con raya de cierre si la frase del narrador comenta el habla: `—No lo sé —dijo, y apartó la vista—. Pregúntale a tu padre.`
  - El verbo de habla (dijo/preguntó) va en **minúscula** tras la raya.

---

## 8. Punto de vista y distancia psíquica

- **Una sola cabeza por escena.** Nada de saltar de lo que piensa A a lo que piensa B en el mismo párrafo (*cabezeo*). El POV del capítulo está en su front-matter; respétalo.
- **Distancia cercana por defecto.** Narra desde dentro del personaje: lo que percibe, en su léxico, con sus prioridades. El narrador no sabe más que el personaje en ese instante (salvo decisión deliberada de la biblia).
- **Coherencia de percepción.** Un personaje no describe lo que no puede ver ni nombra lo que no conocería.

---

## 9. Exposición e información

- **Gotea, no viertas.** Nada de párrafos-ladrillo que explican el mundo, el pasado o las reglas. Da la información cuando hace falta y a través de la escena.
- **No robes el descubrimiento.** Si el lector va a descubrir algo en la escena, no lo adelantes en la narración. Deja que pase.
- **Sin relleno de jerga.** No acumules tecnicismos o nombres propios para "dar empaque". Cada término nuevo tiene que ganarse el sitio y entenderse por contexto.

---

## 10. Tensión (que no decaiga)

- **Cada escena gira.** Algo cambia entre el principio y el final de la escena: una relación, un plan, un saber, un equilibrio de poder. Si la escena termina igual que empezó, sobra o hay que reescribirla. (La carga apertura→cierre va planificada en `outline.md`.)
- **Gancho de apertura y de cierre.** El primer párrafo del capítulo planta una pregunta o una imagen que obliga a seguir. El último deja una puerta abierta (una amenaza, una decisión pendiente, una revelación a medias). El cierre **no** es una conclusión: es un anzuelo.
- **Pregunta dramática viva.** En todo momento el lector debe tener al menos una pregunta abierta tirando de él ("¿lo conseguirá?", "¿quién mató a…?", "¿se atreverá a decírselo?"). Se registran en `memoria/preguntas-abiertas.md`.
- **Protagonista activo.** Que decida y actúe, que no solo reaccione y observe. Las cosas pasan *porque* hace algo.

---

## 11. Aperturas y cierres de capítulo

- **Apertura.** Prohibido abrir con: el tiempo meteorológico, el personaje despertándose / abriendo los ojos / sonando el despertador, o mirándose al espejo para describirse. Empieza en movimiento, en conflicto o en una imagen concreta y rara. El linter avisa de estos arranques.
- **Cierre.** Termina en concreto y con anzuelo (ver §3.2 y §10). Nada de moraleja.

---

## 12. Lista negra léxica (España)

Evita por sobreúso y sabor a plantilla (el linter marca muchas):

*un escalofrío le recorrió la espalda · se le heló la sangre · el corazón le dio un vuelco · una mezcla de [emoción] y [emoción] · no pudo evitar (sonreír/pensar) · en lo más profundo de su ser · una sonrisa traviesa/ladina · sus miradas se cruzaron · el tiempo pareció detenerse · sin previo aviso · contra todo pronóstico · en cuestión de segundos · un silencio sepulcral · la calma antes de la tempestad · podía sentir su mirada · la sangre le hervía · con el corazón en un puño · se le erizó la piel · una corriente eléctrica (recorrió) · mariposas en el estómago · el destino quiso · las palabras murieron en sus labios · luchar contra las lágrimas · un mar de dudas · la oscuridad lo envolvió.*

Esto no es exhaustivo: ante cualquier frase que "ya has leído mil veces", reescríbela.

---

## 13. Mecánica y formato

- **Sangría / separación**: párrafos separados por línea en blanco (markdown). Saltos de escena con una línea con `* * *`.
- **Números, signos, comillas**: comillas españolas «» para citas dentro de prosa cuando haga falta; la raya para diálogo.
- **Coherencia de nombres y datos**: usa exactamente los nombres, tildes y rasgos físicos fijados en `memoria/nombres.md` y `memoria/hechos.md`. No cambies el color de ojos de nadie a mitad de novela.
- **Anti-autosimilitud**: no reutilices la misma imagen, símil o frase de efecto entre capítulos. El comando `npm run similitud` los caza.
- **Sin repetir tics ni sensaciones de un personaje.** Cada personaje tiene en `memoria/rasgos.md` los gestos, rasgos físicos y sensaciones que ya se le han atribuido (tu brief te pasa los del POV de este capítulo). No repitas el mismo tic un capítulo tras otro; no vuelvas a describir un rasgo ya fijado (se nombra de pasada, no se redescribe); no conviertas una imagen corporal ("un nudo en la garganta", "un vacío en el estómago") en muletilla. Si un personaje necesita mostrar nervios y ya gastó su gesto habitual, dale otro distinto. `npm run repeticiones` lo vigila (tolera la flexión: "ajustó/ajustaba las gafas" cuenta como el mismo tic).

---

## 14. Registro: lenguaje fuerte, sexo y violencia

El registro lo fija la historia, no un pudor por defecto. Una novela sobre deseo, maltrato o rabia exige el idioma de esas cosas: rebajarlo es falsear a los personajes.

- **Los tacos se escriben.** Si un personaje diría «hijo de puta», eso es lo que dice. Prohibido el eufemismo cobarde: «soltó un taco», «masculló un improperio», «le dedicó una palabrota». O el lector oye la palabra o la línea sobra; resumir el exabrupto es la peor opción (el linter marca esas fórmulas).
- **La vulgaridad caracteriza o estorba.** Quién insulta y cómo (en frío, a gritos, con qué léxico) va en la tabla de voz de cada personaje. Un taco repetido se gasta como cualquier muletilla: dosifícalo para que conserve el filo.
- **Sexo**: desde el POV, sensorial y concreto. Ni lírica de tapadera (metáforas de oleaje y fuego) ni asepsia clínica no elegida. La elipsis o el fundido son decisiones de ritmo, no actos de censura: elige a conciencia dónde corta la cámara.
- **Violencia y maltrato**: crudos y con peso. Lo que hace daño en la página es el coste en quien lo sufre —cuerpo, miedo, el silencio de después—, no el inventario de golpes. Brutalidad sin consecuencia es decorado.
- **Coherencia**: el nivel de crudeza de la novela se declara en `biblia/premisa.md` (tono/registro) y se sostiene; no se oscila entre lo explícito y lo mojigato según el capítulo.
- **Límite innegociable**: nada que sexualice a menores. Todo lo demás lo decide la historia.

---

## 15. Repaso exprés antes de dar un capítulo por bueno

1. ¿Hay alguna "No era X. Era Y." o cierre con moraleja? → fuera.
2. ¿Tres frases seguidas con la misma longitud o el mismo arranque? → varía.
3. ¿Algún concepto abstracto haciendo de sujeto activo? → reescribe.
4. ¿Más de un par de filter words o micro-gestos del repertorio? → poda.
5. ¿La escena gira? ¿El capítulo abre con gancho y cierra con anzuelo?
6. ¿Cada personaje suena distinto?
7. ¿Cada párrafo aporta algo nuevo?
8. ¿El registro está a la altura de la escena? Ni taco de adorno ni eufemismo cobarde («soltó un taco») donde tocaba oír la palabra.
9. Pasa `npm run lint` y `npm run similitud`. Cero errores.
