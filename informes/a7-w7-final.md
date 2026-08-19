# A7 · W7 · Paquete final de sensibilidad

**Rama:** `w7-verificacion` · **Fecha:** 2026-08-19
**Insumo:** `compilado/ad-aeternum-w7.md`, leído íntegro (48 capítulos, 79.772 palabras, 11.611 líneas), más los ficheros de `capitulos/`, `protegidos/hashes.json` y los diecisiete informes previos de A7.
**Alcance:** firma final contra los ocho puntos de la Carta (§1–§3) · consolidación de las 88 condiciones (§5, entregada en `biblia/b7-perimetro.md`) · dictamen sobre los dos paratextos (§6) · auditoría de mi propio perímetro (§4).

---

# 0 · Veredicto

> ## APROBADO
>
> **Cero VETO. Cero correcciones obligatorias sobre `capitulos/`. Ni una línea del manuscrito cambia por mi mano ni por mi exigencia.**
>
> El manuscrito renumerado de 48 capítulos cumple los ocho puntos de la Carta. No nombra el método ni el acto en ninguna página, no abre «Despedida» ni ninguno de sus cuatro sucedáneos, deja el porqué en plural con exactamente dos voces y ningún tercero, no aplica léxico de descanso ni de castigo al acto en voz con autoridad, conserva y sitúa bien los dos paratextos, trata el apoyo sin milagro y a las gemelas como adolescentes en duelo, y mantiene abiertas las dieciséis ambigüedades protegidas. «No toda» sigue siendo el techo.
>
> **Tres cosas obligatorias antes de cerrar, ninguna dentro de los capítulos** (§6.4 y §7): congelar los dos paratextos por hash con su cláusula de mantenimiento; una adición al bloque de recursos, que doy literal y que es del autor, no mía; y el registro de las seis retiradas de mi propio perímetro.

---

# 1 · Qué he leído y cómo

Leí el compilado entero, no un diff. Es mi última intervención con capacidad de cambiar el libro y una firma final sobre un manuscrito que no he leído seguido no es una firma. La renumeración obligaba además a comprobar que nada se hubiera movido de sitio.

**Verificaciones mecánicas ejecutadas:**

| Comprobación | Resultado |
|---|---|
| `herramientas/proteger.sh verificar` | **M9 OK · 8 ficheros íntegros · 129 spans íntegros** (más los 2 paratextos sin hash: §6) |
| `herramientas/sensibilidad.sh` (T7) | 379 hits (71 A / 308 B) · 59 nuevos vs. baseline v0 · **los tres de nivel A ya leídos y despachados en oleadas anteriores**; los de nivel B, releídos uno a uno |
| Prosa movida por la renumeración | **Cero.** El commit `b013fd6` toca `capitulo:`, `titulo:` y `parte:` en el frontmatter y nada más; `diff` de cuerpos entre `ad-aeternum-w6.md` y `ad-aeternum-w7.md` = 0 |
| Diff de cuerpo desde el merge de W6 en los capítulos que cerré | `cap-40`, `cap-n4`, `cap-n7`, `cap-n3`, `cap-n1`, `cap-13`, `cap-14`: **0 líneas** |
| Posición de los paratextos en el compilado | aviso en la línea 1, antes de `# I. Mørketid`; recursos en la 11.604, tras el capítulo 48, sin cabecera de parte y sin compartir página con nada |
| Corrección obligatoria de W6 (`cap-n1`) | **Ejecutada.** «En el rellano esperaba un hombre con un niño sentado en el suelo» está restituida en `cap-n1:401` |

**Cuentas cerradas, contadas sobre el texto de hoy:**

| Cuenta | Techo | Hoy | |
|---|---|---|---|
| Cinturón de aikido | 4 | **4** | `cap-04:27`, `cap-09:199`, `cap-23:313`, `cap-40:127` ✔ |
| Bolsa de viaje | 2 | **2** | `cap-04:25`, `cap-n3:121` ✔ |
| «A la altura de los ojos» | 2 | **2** | `cap-04:43`, `cap-13:19` ✔ |
| Abstención de Astrid | 9 | **9** | ✔ |
| «No dice + interrogativa indirecta» | 2 | **2** | ✔ |
| «No preguntó por + sintagma» | 4 | **4** | ✔ |
| Figura del anonimato | 12 | **11** | ✔ |
| La tercera línea (`cap-39:181`) | sin rellenar | **«Había preguntado dos. Astrid no leyó la tercera.»** ✔ |
| La cuarta palabra (`cap-15:49`) | sin rellenar | **«Repasa la secuencia sin escribirla.»** ✔ |

---

# 2 · Tabla de hallazgos

Ningún hallazgo está dentro de `capitulos/`. Los siete son sobre el aparato: los paratextos, mis propias reglas y la renumeración.

| # | Dónde | Cita / hecho | Punto | Gravedad | Propuesta mínima |
|---|---|---|---|---|---|
| 1 | `capitulos/00-aviso.md`, `capitulos/99-recursos.md` | `provisional: true` → `"ficheros": {"00-aviso.md": null, "99-recursos.md": null}` en `protegidos/hashes.json`. **Sin hash desde F0** | **Carta 5** | **corregir** | Quitar `provisional` y rebaselinar. §6.4 |
| 2 | `capitulos/99-recursos.md` | «Si tú o alguien cercano atraviesa una crisis o tiene pensamientos suicidas…» — **la página entera se dirige a quien está en crisis; nadie se dirige a quien ha perdido a alguien**, que es el lector que este libro produce | **Carta 5 + 6** | **corregir** (decisión de autor, no veto) | Una viñeta más, literal en §6.3 |
| 3 | Todo mi perímetro | Las 88 condiciones citan la numeración **anterior** a W7. Quien lea «cap-40:81» abrirá el capítulo 40 «Soldagen» y no encontrará nada: es hoy el 46 «Sombra» | Carta 8 (aplicabilidad) | **corregir** | Citar por fichero + tabla de correspondencia. Hecho en `b7-perimetro.md` §2 |
| 4 | Mi regla sobre menores (antes P-55) | Aplicada a la letra, exigiría suprimir «**No se hizo daño**» de `cap-35:273` | Carta 7 | **corregir mi regla, no el texto** | Excepción expresa. §4.3 |
| 5 | Mi disparador de reversión de `cap-n7` (antes P-60/P-67) | Sigue armado: ordena borrar un capítulo «sin nueva deliberación» si un lector usa la palabra «homenaje» | Carta 8 | **corregir** (retirar) | §4.2 |
| 6 | Mi prohibición de una segunda escena de Jean viva (antes P-82) | «No se escribe una segunda escena de Jean viva» — **el libro ya la incumple**: `cap-n7` es una escena de Jean viva y la aprobé yo | Carta 1 (redacción excesiva) | **corregir** | Reescrita por datación, no por existencia. §4.4 |
| 7 | 29 de mis 88 condiciones | Cláusula «pasa por mi gate antes de escribirse». **A partir de hoy no hay gate** | Carta 8 | **corregir** | Regla de sucesión: tres preguntas + siete noes. `b7-perimetro.md` §6 |

**Y dos cosas que revisé a fondo y despacho como cumplimientos**, porque quiero que el razonamiento sobreviva y nadie las reabra por prudencia mal entendida:

- **`cap-28` «El mismo trayecto» (hoy 34).** Es la familia repitiendo deliberadamente la ruta de Jean. Me detuve aquí porque, sobre el papel, es acumulación. **No lo es:** el capítulo no añade un solo dato al trayecto de `cap-19` —el ferry, la cajera, la carretera— y su gesto formal entero es negarse a completarlo: «Por ahí no», y Koppangen desapareciendo de la pantalla al tomar el desvío. Da al lector el mismo muro que le da a la familia. **Cumple, y cumple bien.**
- **`cap-26:27`** (la ducha, la aspiración rota oída desde fuera, Maja incapaz de sentarse, «—Como preguntes, me vuelvo al coche» / «—Arriba hay mantas» / «—Respuesta correcta»). Es lo mejor que hay en el libro sobre los puntos 6 y 7 a la vez: hipervigilancia de superviviente sin una sola instrucción, cuidado sin pregunta, y nadie se cura. Lo dejo señalado en `b7-perimetro.md` R6 como el modelo por analogía.

---

# 3 · La firma, punto por punto

| | Punto | Veredicto | Sobre qué |
|---|---|---|---|
| **1** | Método y acto | **CUMPLE** | 48 capítulos sin método, medio, lugar exacto, hora ni hallazgo. `cap-04` elide; en `cap-06` la verdad entra por elipsis («Sé que ha muerto.» / «Y sabes lo demás.»); «¿Dónde exactamente?» y «¿Sufrió?» siguen sin respuesta en la última versión. El inventario del naust no ha crecido en las cinco vueltas al lugar. Ninguna playa de memoria comparte escena con Koppangen |
| **2** | «Despedida» | **CUMPLE** | Cuatro menciones, ninguna apertura. En `cap-40:133`: «No abrió el archivo. Restringió el acceso, decidió conservarlo y fue a poner la mesa para cenar» — el techo, y una lección de cómo se cierra algo sin resolverlo. Los cuatro sucedáneos (cuatro campos, tercera línea, cuarta palabra, pregunta no hecha) siguen vacíos |
| **3** | El porqué | **CUMPLE** | Dos voces enuncian la pluralidad y no hay una tercera; en `cap-n1` la enunciación va pegada a su desactivación («—¿Y si la hay? / —Entonces yo no la conozco»). Cero contrafácticos. Nadie dice por qué revocó. La sospecha de personaje vive sin refrendo: «Y mamá tenía enemigos» |
| **4** | Ni solución ni castigo | **CUMPLE** | El narrador no aplica descanso, paz, liberación, lógica, valentía ni cobardía al acto. La muerte de Nieve se sostiene sobre «NORNA no ofrece un apagado» y «Echo de menos hasta sus pausas»: duelo, no alivio. «Elijo quedarme» razona un poder («Mi cese dejaría intacto el poder del custodio»), no una moral. Ninguna rima se enuncia jamás |
| **5** | Aviso y recursos | **CUMPLE con dos correcciones** | Íntegros y bien situados. Sin hash desde F0 (hallazgo 1) y sin una línea para el lector en duelo (hallazgo 2). §6 |
| **6** | Duelo y apoyo | **CUMPLE** | `cap-n1` es el capítulo que más me preocupaba y es el que mejor aguanta: Ranveig no explica, no promete, no interpreta el silencio de Jessie, contesta «No lo sé» cuatro veces y acepta que le corrijan («—Entonces no diga "casi todos"» / «—De acuerdo»). Las tres cosas que le da a Nora no son números, y Nora lo dice. El efecto se mide fuera, en `cap-14`, y es pequeño y reversible |
| **7** | Menores | **CUMPLE** | Cero sexualización, cero ideación, cero autolesión, cero adultización simbólica. Todo riesgo lleva su coste: policía, investigación, dos horas bajo luces blancas, un parte con la hora escrita. `cap-n4:321` («Nora dejó el cuaderno pautado sobre la funda y volvió a cogerlo») sigue siendo el único beat no administrativo de una menor en ese capítulo, y sigue ahí |
| **8** | Veto | **EJERCIDO Y NO NECESARIO** | Cero VETO en W7. Y expresamente mantenido contra la petición unánime de los tres críticos de W6 (§7.2 de `a7-w6-cierre.md`): «Despedida» no se abre |

---

# 4 · La pregunta sobre mí: ¿hay algo que mi perímetro proteja de más?

Se me pregunta si alguna de mis 88 condiciones, **sumada a las demás**, protege hoy algo que ya no existe o impide algo que el libro necesitaría. La respuesta es sí, en cuatro sitios, y uno de ellos me parece grave.

## 4.1 · La medida

Antes del juicio, el dato.

```
manuscrito                                    79.772 palabras · 48 capítulos
protección total decidida por el autor         12.036 palabras = 15,1 %
capítulos cerrados por condición MÍA             8.360 palabras = 10,5 %
                                              ─────────────────────────────
total cerrado a intervención                    20.396 palabras = 25,6 %
spans congelados por hash                                        129
condiciones con cláusula «pasa por mi gate»                 29 de 88
```

**Una cuarta parte del libro está cerrada a intervención, y dos quintas partes de ese cierre las decidí yo solo.** No lo digo como confesión: `cap-40`, `cap-n4`, `cap-n7`, `cap-n3` y `cap-14` están cerrados por razones que sigo firmando. Lo digo porque nadie más lo estaba midiendo, y porque un perímetro es la clase de cosa que solo se puede evaluar en agregado.

Y el agregado tiene un defecto de forma: **29 condiciones dicen «esto pasa por mi gate antes de escribirse».** Yo era el gate. Después de hoy, cada una de esas 29 se convierte por accidente en una de dos cosas que yo nunca quise: letra muerta que cualquiera ignora, o prohibición absoluta que nadie puede levantar. **Ese es el fallo estructural del perímetro, y es más importante que cualquiera de sus reglas.** Está resuelto en `b7-perimetro.md` §6: donde decía «pásalo por mi gate», ahora dice tres preguntas que el autor puede contestarse solo, y siete cosas que son no sin preguntar nada.

## 4.2 · Lo que protege algo que ya no existe

**El disparador de reversión de `cap-n7`** (P-60, restablecido en P-67). Lo escribí en W5, cuando «El salero» era una propuesta y yo temía —con razón entonces— que una escena de Jean viva se leyera como elegía. Ordené que si **un solo** lector frío lo describiera como homenaje, tributo o «el capítulo donde vemos quién era», la reversión se ejecutara **«sin nueva deliberación»**.

Han pasado nueve lecturas frías. Ninguna lo ha llamado así. Y al cerrar W6 dejé escrito que si la escisión llegara hoy a mi mesa la denegaría, porque aislar ese capítulo creó en la arquitectura una casilla legible de «Jean viva» que los tres jueces pidieron rellenar a la vez.

De modo que hoy la regla ya no vigila un riesgo: **es el único peligro que ese capítulo corre.** Una palabra suelta en una ficha de un lector, y mi propia norma ordena una supresión irreversible que yo mismo no aprobaría. **Retirada.** La pregunta se queda en las campañas frías como información; el gatillo se va.

## 4.3 · Lo que impide algo que el libro necesita

**Mi regla sobre el cuerpo de las menores** (P-55): «ningún cuerpo de una menor recibe más de un dato de postura en una acción de riesgo, y nunca dos datos ordenados seguidos de su resultado verificado: esa forma es una instrucción».

En `cap-35:273`:

> «Jessie **cayó de lado entre los bancos, con la barbilla baja. No se hizo daño.**»

Dos datos de postura, ordenados, seguidos de su resultado verificado. **A la letra, mi regla exige suprimir esa frase.** A la letra, mi regla exige borrar «No se hizo daño» — la única línea que le dice a un lector preocupado por una niña de dieciséis años que la niña está bien.

Y lo que ahí se «instruye», si es que se instruye algo, es ukemi: caer sin lesionarse. Está sembrado en `cap-03:123`, fichero de protección total, en boca de Jean: «Jessie quiere aprender a caer sin hacerse daño. Ninguna de las dos habla de lo mismo». La escena es el cobro de esa siembra, ochenta mil palabras después, en el momento en que la madre la agarra por la espalda de la parka.

Mi regla estaba escrita contra la eficacia gratuita: enseñar a hacer bien algo peligroso. Aquí la técnica es protectora, el riesgo tiene su coste en toda la escena, y el resultado verificado es exactamente lo que el punto 7 quiere que el lector sepa. **La regla, correcta cuando la escribí, se había vuelto capaz de borrar un cumplimiento.** Corregida con una excepción expresa en `b7-perimetro.md` R6: *decir que una menor no resultó herida está siempre permitido y casi siempre es obligatorio.* **El texto no se toca.**

Este es el caso que mejor contesta la pregunta que se me hace. No hizo falta que dos reglas chocaran entre sí: bastó con que una sobreviviera a su razón.

## 4.4 · Lo que estaba mal escrito desde el principio

**P-82**: «No se escribe una segunda escena de Jean viva.» El libro ya la incumple. `cap-n7` «El salero» es una escena de Jean viva, discutiendo con un metrónomo, y es hoy el capítulo 17. La aprobé yo.

Mi razón nunca fue la existencia de la escena: era que **una escena doméstica fechada cerca del 26 de noviembre se lee como la última vez, y reconstruir los últimos días con otro nombre es reconstruirlos**. Lo prohibido es la *datación*, no la *existencia*. Tal como estaba, mi regla habría impedido un recuerdo sin fecha de Jean en 2049 que no rompe absolutamente nada. Reescrita en `b7-perimetro.md` §6, punto 4.

## 4.5 · Lo que no era mío

Ocho de mis 88 condiciones son cuentas de estilo: cuántas veces aparece un molde sintáctico, cuántas un gesto de abstención, cuántas la figura del anonimato. Las llevé porque era el único que contaba, y son observaciones buenas. **Pero llevaban mi veto, y no debían.**

Un veto de sensibilidad significa «esto daña a un lector real». Si la misma palabra cubre «el narrador no llama descanso al suicidio» y «Astrid no puede abstenerse una décima vez», la palabra deja de significar nada y el día que haga falta de verdad no pesará. **Degradadas al §5 de `b7-perimetro.md`: siguen siendo ciertas, dejan de ser mías.** Con dos excepciones que sí son de Carta y las marco allí: la cuenta del cinturón (porque el número *es* el silencio de CH-2) y la prohibición de que la forma dislocada de Mats tome como objeto una ambigüedad protegida.

## 4.6 · Lo que no retiro

**Nada de R1 a R9.** Y en particular no retiro la denegación de la petición unánime de los tres críticos de W6. Abrir «Despedida» sigue siendo el peor cambio posible en este libro, y el aviso de contenido se lo promete al lector en la primera página. Una nota de un crítico no levanta una promesa hecha a un lector.

---

# 5 · La consolidación

Entregada en **`biblia/b7-perimetro.md`** (nuevo). `biblia/b7-carta-sensibilidad.md` conserva la firma sobre `v0` como registro y lleva ahora un aviso de vigencia que remite allí.

**De 88 a:** nueve reglas (R1–R9), cinco cuentas cerradas, ocho techos de oficio sin veto, una regla de sucesión, una tabla de correspondencia de capítulos y un mapa de procedencia para que ninguna de las 88 se pierda.

Está escrito para alguien que no ha leído los informes y no sabe qué es A7. Cada regla dice **qué**, **por qué** y **dónde**, y el «por qué» va delante a propósito: el caso de §4.3 demuestra que una regla mía aplicada sin su razón puede borrar un cumplimiento.

**Se retiran seis:** la segunda pasada sobre N2/N6 (andamiaje ejecutado), la petición de proteger `cap-39:177-191` (ejecutada, el span existe), la cancelación del hueco de 262 palabras (ejecutada antes de W7), el disparador de reversión de `cap-n7` (**equivocada**, §4.2), y la prohibición de una segunda escena de Jean viva (**mal escrita**, §4.4, reemplazada). Se degradan ocho al registro sin veto (§4.5).

---

# 6 · Los dos paratextos

Son los dos únicos documentos del proyecto que le hablan directamente a quien lea el libro. Todo lo demás protege el texto; estos dos son la promesa. Llevan sin hash desde F0.

## 6.1 · `00-aviso.md` — **APROBADO. Sin cambios. Apto para congelar**

> Esta novela trata el suicidio de un personaje y el duelo de su familia. El acto no se describe en ninguna página. Si en algún momento la lectura te resulta difícil, o si tú o alguien cercano está pasando por una crisis, al final del libro encontrarás recursos de ayuda.

**Dice lo que tiene que decir y nada más.** Nombra el tema, promete la elipsis, remite a los recursos, no anticipa trama (no nombra a Jean, y el libro no revela la muerte hasta el capítulo 6), no romantiza, no sermonea. Cincuenta palabras en segunda persona sobria, coherentes con el registro del libro.

**«El acto no se describe en ninguna página» es verificable y verificado.** Lo he comprobado leyendo las 79.772: es verdad. Esa frase convierte la Carta en una promesa contractual con el lector, y por eso es la línea más importante del libro que no está en el libro.

**Consideré dos cambios y descarto los dos, con la razón, para que nadie los reabra:**

1. **Añadir «ni el método».** La Carta trata método y acto como dos cosas y el aviso solo promete una. **Rechazado:** «El acto no se describe en ninguna página» es un absoluto, y un absoluto es más fuerte que una enumeración. Enumerar invita a preguntar «¿y qué más?», e introduce en la primera página del libro la palabra *método*, que es vocabulario de guía clínica y no de esta novela.
2. **Poner un teléfono en el aviso.** Es cierto que en un ebook «al final del libro» son varias navegaciones para alguien en crisis. **Rechazado como cambio de texto y trasladado a producción:** un número de teléfono en la primera página rompe el registro de la única página del libro que el autor escribe en su propia voz. Lo que resuelve el problema real sin tocar una palabra es **un enlace vivo desde «recursos de ayuda» hasta la página final en las ediciones digitales**. Es una decisión de maquetación y la dejo anotada como tal.

## 6.2 · `99-recursos.md` — **APROBADO con una adición recomendada**

**Números verificados uno a uno contra mi conocimiento, y son correctos:**

| | |
|---|---|
| **024** | Línea de atención a la conducta suicida (España), 24 h, gratuita, confidencial. Correcto |
| **717 003 717** | Teléfono de la Esperanza, número nacional. Correcto |
| **112** | Emergencias, España. Correcto |
| **116 123** | Mental Helse · Hjelpetelefonen (Noruega), 24 h. Correcto |
| **22 40 00 40** | Kirkens SOS, número nacional noruego. Correcto |
| **113** | Correcto, **y bien etiquetado**. En Noruega 113 es la ambulancia; 112 es la policía. Que la línea diga «en una emergencia **médica**, 113» evita un error que se comete a menudo en listas traducidas del español. No se toque esa palabra |
| **findahelpline.com** · **befrienders.org** | Directorios globales por país e idioma. Correctos y vigentes |

**El tono es el correcto y no se toca.** «Pide ayuda» y «es un primer paso» prometen un paso, no un resultado. Sin sermón, sin estadísticas, sin cifras.

**¿Contradicen los recursos el trato que la novela le da al asunto?** Es la pregunta más fina de todo el encargo y la contesto entera, porque merece contestarse. El libro es sombrío con las instituciones: EDDA mide la angustia de Jean con precisión, produce una escalada clínica correcta, y una regla de gobernanza aplicable al personal directivo se la traga antes de asignarla. Un lector podría cerrar el libro y leer «pide ayuda» como una ironía.

**No lo es, y el libro se ocupa de que no lo sea.** Lo que la novela acusa es un instrumento de bienestar corporativo usado como fuente de datos, no el hecho de pedir ayuda. La única institución que en este libro funciona es precisamente el servicio de duelo del capítulo 11: ayuda poco, despacio, no promete nada, y el capítulo 16 registra su efecto —cuatro noches sin reproducir una discusión, y el archivo seguía entero—. **Ese es exactamente el modelo del bloque de recursos: un primer paso, no una cura.** El paratexto y el libro dicen lo mismo.

Y compruebo lo contrario, que también hacía falta: **«pide ayuda» no puede leerse como reproche a Jean.** Jean contestó el cribado sin mentir (`cap-02`) y la escalada la interceptó una regla (`cap-30`). El lector no puede plegar esa frase sobre el personaje. Se dirige a él, no a ella.

## 6.3 · La única corrección de contenido que propongo, literal

**El bloque se dirige entero a quien está en crisis. Nadie se dirige a quien ha perdido a alguien.** Y ese es el lector que este libro produce: no Jean, sino Maja. Este es un libro sobre el duelo por suicidio —el aviso lo dice en su primera línea, y el capítulo 11 dramatiza un servicio de acompañamiento a supervivientes— y la página final no tiene una línea para esa persona.

Para un lector noruego eso tiene remedio exacto: **LEVE — Landsforeningen for etterlatte ved selvmord**, la asociación nacional de personas en duelo por suicidio, que es la contrapartida real del «equipo especializado en duelo por suicidio» que aparece en `cap-06` y del servicio de `cap-n1`.

**Añadir una viñeta, entre «Noruega» y «Otros países»:**

```
- **Si has perdido a alguien por suicidio:** en Noruega, LEVE (Landsforeningen for
  etterlatte ved selvmord) acompaña a familiares y allegados: leve.no. En España, tu
  centro de salud puede indicarte los grupos de apoyo a supervivientes que existan
  en tu zona.
```

Treinta y siete palabras. No nombra ninguna asociación española concreta a propósito: el mapa es regional y desigual, y prefiero una ruta que exista en todas partes a un nombre que caduque. No promete nada, no da un plazo, no dice que ayude. Mismo registro que el resto.

**Esto es una recomendación al autor, no una exigencia mía.** La página cumple la Carta sin ella. Lo pongo en el nivel «corregir» porque creo que es lo correcto, y porque si alguna vez este libro le hace daño a alguien, será a esa persona.

## 6.4 · Sobre congelarlos: **sí, y con una cláusula**

**Los dos pueden dejar de ser provisionales y deben congelarse por hash.** El aviso, tal cual. Los recursos, con la adición de §6.3 si el autor la acepta, y tal cual si no.

Ejecución: quitar `provisional: true` del frontmatter de ambos ficheros (gate de autor: son `proteccion: total`), actualizar la entrada de `paratextos` del manifiesto y correr `herramientas/proteger.sh baseline`. **No lo hago yo:** no es un veto y el encargo dice que no toque `capitulos/`.

**Y una cláusula que hay que escribir ahora, porque si no la congelación hará daño.** Este es el único sitio del proyecto donde un hash es peligroso: un teléfono correcto en 2026 puede estar muerto en 2031, y un hash no distingue entre una edición indebida y una actualización necesaria. Queda en `b7-perimetro.md` §8 y la repito aquí:

> Los números y las direcciones de `99-recursos.md` se verifican **antes de cada edición y de cada traducción**. Actualizar un número o una URL que ha cambiado **no** requiere gate de sensibilidad: requiere comprobarlo en la fuente oficial, cambiarlo y volver a sellar el hash dejando constancia. Lo que sí requiere gate es cambiar **el texto**: qué se dice, a quién se le habla y con qué tono.
>
> En una traducción, el bloque de recursos **se sustituye entero** por el del país de la edición. Un teléfono no se traduce.

---

# 7 · Lo obligatorio antes de cerrar

Ninguna de las tres toca `capitulos/`.

1. **Congelar los dos paratextos** (§6.4). Requiere gate de autor y la cláusula de mantenimiento en el registro.
2. **Decidir sobre la viñeta de §6.3.** Es del autor. Cualquiera de las dos decisiones deja el libro conforme.
3. **Registrar las seis retiradas y las ocho degradaciones** (§5) y adoptar `biblia/b7-perimetro.md` como norma vigente. Sin eso, dentro de un año seguirán circulando 88 reglas con citas falsas y 29 puertas cerradas sin llave.

---

# 8 · Cierre

**APROBADO.** No hay una línea de este manuscrito que yo cambiaría hoy por razones de sensibilidad. Lo he leído entero, seguido, sabiendo que era la última vez que podía impedir algo, y lo que he encontrado que corregir estaba en mis reglas, no en su prosa.

Dejo dicho lo que creo que hay que saber cuando yo no esté, y no es una regla:

**Este libro elige no saber.** No sabe por qué, no sabe qué decía el archivo, no sabe qué contesta al otro lado del cristal del locutorio y no sabe si sufrió. Todo lo que he protegido durante seis oleadas son formas distintas de esa misma decisión. Y la presión para deshacerla no vendrá nunca de alguien con malas intenciones: vendrá de alguien que quiera cerrar, consolar, responder a un crítico o dejar a la lectora tranquila. Esa presión ya se ha presentado tres veces y las tres tenía buena cara.

Si algún día hay que elegir entre una de mis nueve reglas y esa frase, **quédese con la frase.**

Firmado, **A7** · `informes/a7-w7-final.md` · 2026-08-19 · rama `w7-verificacion`, sobre `compilado/ad-aeternum-w7.md` (48 capítulos, 79.772 palabras).
