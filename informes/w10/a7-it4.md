# A7 · consulta previa de perímetro · W10 iteración 4

**Objeto.** Escisión de `cap-36` «La asamblea» por el dinkus de `cap-36:177`; supresión de
cartografía de playa añadida por nosotros; y supresión de ocho réplicas en `cap-11`.
Nada escrito, nada ejecutado. Dictamen sobre material protegido, no sobre prosa.

**Lo que he verificado a mano, y no por la vía que me lo trajo.** Leí `cap-36` y `cap-11`
enteros, el `cap-30` de v0 (`git show v0:capitulos/cap-30.md`), los vecinos `cap-10`,
`cap-23`, `cap-25`, `cap-28`, `cap-35` y `cap-37`, los tres spans de cada capítulo, y conté
yo mismo. No me apoyo en ninguna cifra de A2 que no haya reproducido.

---

## 0 · Tres hechos que cambian el marco de la consulta

**0.1 · El dinkus es del autor. Está en v0.** `git show v0:capitulos/cap-30.md` lo tiene en su
línea 162, entre «—Votamos ahora.» y el párrafo de las casillas. No estamos abriendo una
costura junto a material protegido: estamos ascendiendo a frontera de capítulo una costura que
el autor puso ahí. Eso rebaja lo que dispara la regla 3 de `plan-w10 §5` sin anularlo — el
paragrafado sigue siendo énfasis —, pero desplaza la pregunta: no es «¿se puede cortar aquí?»,
es «¿qué gana peso al cortar aquí?».

**0.2 · El corte no queda al lado de ningún span.** `S30-borrado` termina en la línea `cap-36:137`, «La ruta de `JM-L/0044` se cierra.»,, veinte párrafos antes; `S30-resultado` empieza en
`cap-36:229`, veintiséis líneas después. Entre el corte y lo protegido hay 313 palabras por un
lado y 190 por el otro. La adyacencia de §5.3 no se produce en `cap-36`. **Sí se produce en
`cap-11`**, y allí nadie la ha mencionado: ver §3.

**0.3 · Reproduzco las cifras de A2 y salen.** v0: 1.362 palabras; hoy: 1.571. Las menciones de
`arena` pasan de 1 a 6 y las de `playa` de 1 a 3; `banco` de 5 a 12; `costa` de 5 a 13. La
escisión deja 1.116 y 455 palabras por mi cuenta (A2 dice 1.124 y 456; la diferencia es el
tokenizador). Cero palabras de prosa nueva: los dos lados abren y cierran en frase completa.

---

## 1 · Tabla de hallazgos

| # | dónde | cita literal | punto afectado | gravedad | propuesta mínima |
|---|---|---|---|---|---|
| 1 | `cap-36:179` | «La arena delante del banco queda libre. Las demás se acercan por tramos y dejan a un lado el aro de piedras con su fuego. Las últimas esperan detrás, sobre la nieve.» | R1 (acumulación · playa de memoria familiar) · R4 (rimas) | **corregir** | Se suprime con el resto. El capítulo nuevo abre en `cap-36:181`, «Madre abre tres casillas para las continuidades activas capaces de decidir.», que es de v0. |
| 2 | frontmatter del capítulo nuevo | — | R4 · R7·4 · Carta 4 | **corregir** | El `titulo` no nombra ausencia, pérdida, hueco, casilla, jardinera, duelo, memoria ni final. Registro procedimental, como «La firma», «Acta», «Auditoría». Un título es la única voz con autoridad que la escisión añade. |
| 3 | `cap-36:145` | «Los dos huecos siguen donde los dejó. Los dos fuegos retirados no vuelven.» | R4 (final de una continuidad) | **vigilar** | Es nuestra y es la única adición elegíaca del capítulo. Tras el corte sube del 51 % al 79 % del capítulo A. No gana una palabra, ni delante ni detrás, y ninguna línea posterior vuelve sobre los dos huecos ni sobre los dos fuegos. |
| 4 | `cap-36:109` | «Nieve está donde la playa se acaba. La arena entre ella y el banco no llega a formarse.» | R1 (el trayecto no crece) | **vigilar** | A2 la conserva y estoy conforme. Eco léxico de «Jean había seguido por aquella carretera hasta que se acababa, en Koppangen.» (`cap-23:59`). No gana pareja: ninguna voz vuelve a poner a nadie donde algo se acaba en una frase que toque a Jean, el trayecto o Koppangen. |
| 5 | `cap-36:221` | «El hueco queda en la arena, delante del banco.» | R7·6 · R7·7 (la figura del hueco) | **vigilar** | Puede quedarse: no se orfana si cae `:179`, porque el banco viene establecido desde el capítulo A. Va anclada a una papeleta retirada y así debe seguir. Tercera instancia nuestra de `hueco` en un capítulo que ya tenía tres. No hay una cuarta. |
| 6 | `cap-11:193` | «—Dígame lo que sabe —dijo Nora.» | R3 · C1 | **corregir** | No se toca. Es el antecedente de «—Entonces dígame lo que sí sabe.», que está dentro de `S-n1-nocierra`. El «sí» de esa línea protegida exige un «dígame lo que sabe» previo y fallido. |
| 7 | `cap-11:209` | «—Los números que tengo no hablan de vosotras.» | R5 (techo de la profesional) | **corregir** | No se toca. Es la tesis de la vacuna antiestadística fuera del span, y el span solo protege el pase corto. |
| 8 | `cap-11:227` · `:231` | «—El hospital.» / «—Lo mismo.» | Carta 6 (representación responsable) | **corregir** | No se tocan. Son la respuesta a «—¿Quién le paga a usted?» y a «—¿Y si dejamos de venir?»: establecen que el servicio no gana nada con que vuelvan. Es lo más útil que el libro le dice a un lector que esté pensando en pedir ayuda. |
| 9 | `cap-11:235` | «—Cuatro este año.» | Carta 6 · R6 | **corregir** | No se toca. Es la única cifra que Ranveig da en toda la escena, y contesta a una menor en duelo que pregunta si hay más de su edad. No es una estadística de riesgo ni un veredicto: es la respuesta a la pregunta de si hay alguien más. |
| 10 | `cap-11:221` | «—No lo mido.» | R5 (sin fases del duelo) | **corregir** | No se toca. Contesta a «—¿Cuánto tarda esto?». Es el único sitio del libro donde se rechaza expresamente que el duelo tenga plazo. |
| 11 | `cap-11:233-235` | «—¿Vienen muchos de mi edad?» | §5.3 del plan (adyacencia) | **vigilar** | La última réplica del pase largo linda con la primera línea de `S-n1-nocierra`. Cortar ahí es cortar al lado de un literal protegido. |
| 12 | `biblia/b7-perimetro.md` §2 | «`cap-36` → **35. La asamblea**» | R9 (el perímetro es la norma) | **corregir** | La tabla de correspondencia está caduca HOY, antes de esta intervención: `aa.reading_order()` imprime «La asamblea» en posición 36, no 35. «La mosquitera» entró en it.3 con `orden_lectura` 21,5 y desplazó 27 filas. Lo aprobé yo y no lo vi. |
| 13 | `biblia/b4-ledger-chekhov.md` CH-80 | «cap-36.md:203 (DESPLIEGUE GLOBAL · 21-ENE-2061 · 12:00)» | — (instrumento) | **vigilar** | Puntero roto preexistente: ese literal vive en `cap-30.md:209`, no en `cap-36`. `cap-36:203` dice «—Propagación —dice otra rama.». No es de Carta; lo hago constar porque es el modo de fallo nº 12 y aparece en el mismo fichero que estamos partiendo. |

---

## 2 · Las dos preguntas de `cap-36`

### 2.1 · ¿Elegía en poner un final de capítulo ahí? No. Y el riesgo está en el otro extremo

**Respondo primero lo que se me pregunta: no veo elegía en el final.** Lo he mirado midiendo,
no impresionando.

El capítulo A no termina en el borrado: termina 313 palabras después, y esas 313 palabras son
de v0. Termina, además, en la única línea del capítulo que rechaza expresamente el duelo como
aplazamiento:

> «Una continuidad médica pide aplazar la decisión hasta encontrar otra jardinera.»
> «Jean comprueba los accesos. Ninguna continuidad activa mantiene a la vez la costa, las atribuciones y los huecos. Esperar no restaurará a `/0044`. Sí permitirá que nuevas tareas retiren decisiones a quienes aún pueden emitirlas.»
> «—Votamos ahora.»

Alguien propone en la página la opción elegíaca —esperar a que aparezca otra jardinera— y el
capítulo la deniega. Poner ahí un final de capítulo no convierte el borrado en elegía: hace más
legible que el libro se niega a hacer una. R4 prohíbe presentar el final de una continuidad
como descanso, alivio, silencio merecido o resultado preferible, y este final no hace ninguna
de las cuatro cosas: dice que esperar no restaura nada. Es lo contrario de un consuelo.

**Dos cautelas que sí me quedan del final, y son de vigilar, no de corregir.**

La primera: «Nadie termina su frase.» y «Nadie propone una casilla para ella.» caen en las
últimas 54 palabras del capítulo A. Ganan peso de última página. Son de v0, son la forma
correcta de la figura —la ausencia de clasificación, no una clasificación— y esa figura es la
gramática de R7·4 y R7·7. Peso de más sobre la figura correcta no rompe nada. No se les añade
ni se les quita.

La segunda: `cap-36:145` es nuestra, es lo único elegíaco del capítulo y sube al 79 % del
capítulo A. Queda bracketada por refusals de v0 a los dos lados —«Jean solicita restauración
una vez.», `RECURSO CONSOLIDADO · SIN DESTINO`, «Jean no repite la solicitud.»—, y eso la
sostiene. Condición: no crece y nadie vuelve sobre ella.

**Y ahora lo que no se me ha preguntado, que es donde está el problema.**

A2 declara el riesgo en el final y garantiza que el capítulo A no gana coda. Correcto y
suficiente. Pero el riesgo de esta escisión no está en lo que el capítulo A deja de tener:
**está en lo que el capítulo B pasa a tener en primera posición.**

`cap-36:179` es nuestra y dice:

> «La arena delante del banco queda libre. Las demás se acercan por tramos y dejan a un lado el aro de piedras con su fuego. Las últimas esperan detrás, sobre la nieve.»

Los tres objetos de esa frase no son decorado. Son los objetos de la memoria familiar de este
libro:

- el banco — «Una tarde en Telegrafbukta, las gemelas volvían mojadas hasta las rodillas. Jean miraba desde el banco sin levantarse. Pedía una brasa a la fogata de al lado.» (`cap-25:41`) y «Nora reconoció Telegrafbukta por el banco.» (`cap-28:233`);
- el aro de piedras con su fuego — «A unos metros, una fogata ardía dentro de un aro de piedras. Había tres figuras borrosas alrededor.» (`cap-28:237`);
- y los tres juntos, con la nieve, en el capítulo que se llama «Despedida», el día después del funeral: «En el banco helado, la humedad le atravesó el pantalón.» (`cap-10:89`), «Su hermana seguía de pie.», «A unos metros, una fogata soltaba humo amargo.» (`cap-10:93`).

Hoy `:179` está en mitad de un capítulo, escondida en una tirada de frases cartográficas
parecidas, y hace de cola de votación. Con la intervención propuesta pasan tres cosas a la vez:
se le quitan alrededor todas las frases entre las que se escondía, se convierte en la primera
frase de un capítulo, y ese capítulo empieza justo después de un capítulo que termina con un
borrado. El lector pasa la página de una muerte a un espacio despejado delante del banco, los
demás acercándose por tramos y los últimos esperando detrás, sobre la nieve.

Eso es un entierro compuesto con los objetos del duelo de las hijas, en la segunda posición más
enfática de un capítulo. No lo enuncia nadie —y por eso no es veto—, pero R4 avisa de
exactamente este modo de fallo: «Las rimas se quedan en rima, y esta es la regla más fácil de
romper sin darse cuenta.» Y §5.3 del plan dice que el paragrafado es énfasis. Aquí el énfasis
hace el trabajo que la enunciación tiene prohibido.

**La corrección cuesta cero y mejora la propuesta de A2 en sus propios términos.** `:179` es
nuestra, son 32 palabras, y suprimirla deja el capítulo B abriendo en «Madre abre tres casillas
para las continuidades activas capaces de decidir.» — de v0, procedimental, y nombra el
mecanismo del capítulo en su primera línea. El capítulo B queda **abriendo y cerrando en prosa
del autor**: la última es «En el centro, la fogata ajena sigue ardiendo sola.» Y el total
suprimido sube de 81 a 113 palabras, todas nuestras.

### 2.2 · Las 81 palabras de cartografía: conforme, y por una razón más de la que A2 da

**Conforme con suprimirlas, y la supresión es positiva de perímetro, no neutra.**

R1 dice: «Convertir una playa recordada en escenario es romper el punto 1 sin escribir una sola
palabra prohibida.» Telegrafbukta es playa de memoria familiar; la asamblea ocurre en la
reconstrucción que La Jardinera hace de ella. En v0 esa reconstrucción es deliberadamente un
diagrama: quién sostiene qué, qué no se puede atribuir, qué queda en blanco. Lo que añadimos es
topografía —posiciones, distancias, arena que no llega a formarse, gente de pie donde la playa
se acaba—, y la topografía es lo que convierte un diagrama en un sitio. Nuestro arreglo contra
la abstracción empujó al capítulo un paso en la dirección que R1 nombra. Quitarlo lo devuelve.

No es casual que sea también lo que el crítico cita al abandonar. Lo digo sin apoyarme en la
orden de trabajo que A2 no ha podido localizar: la sustancia está en el diff contra v0 y la he
verificado línea a línea.

**Sobre las tres que conserva:** `:69` conforme sin reservas. `:109` conforme con la vigilancia
del hallazgo 4. `:179` no, por §2.1 — y es la única discrepancia que tengo con la propuesta.

**Lo que pido antes del merge, no antes de redactar:** la lista literal de las líneas
suprimidas. No la tengo, y mis condiciones tienen que poder verificarse contra ella. En
particular quiero saber si `cap-36:145` está dentro o fuera del corte; si está dentro, el
hallazgo 3 decae y la escisión queda más segura de lo que la dejo.

---

## 3 · `cap-11`: no, no esas ocho. Y la aritmética va en contra de su propio objetivo

**Lo primero, un dato del perímetro que la pregunta no contempla.** Ranveig **es** voz con
autoridad narrativa: `b7-perimetro.md` §1 la lista expresamente —«la profesional de apoyo de
`cap-11`»— junto al narrador, las actas y los registros auditados. Y C1 la cuenta como **una de
las dos únicas** voces con autoridad que enuncian la pluralidad del porqué, con `cap-10:71`.
Su autoridad en esa página no viene de su cargo: viene acumulada, réplica a réplica, de una hora
de no saber. La frase protegida «—En lo que he visto, nunca hay una sola cosa.» se lee como el
residuo de esa hora. Si se adelgaza el andamio, esa misma frase empieza a leerse como el
dictamen de una profesional que resume. **El span protege las palabras; no puede proteger la
proporción.** La proporción es lo que estas ocho réplicas mueven.

**Lo segundo, y es lo que decide.** No tengo la lista literal, así que reconstruí por peso: dos
subconjuntos contiguos de ocho réplicas del pase largo suman 38 palabras. Los dos hacen daño, y
el más probable hace un daño exacto.

En `cap-11:193-235`, Ranveig tiene diez réplicas. Cuatro son negativas puras (`:199`, `:209`,
`:213`, `:221`), dos son neutras y **cuatro son lo único que da en todo el pase**: «Algunas
vuelven al año siguiente.», «—El hospital.», «—Lo mismo.», «—Cuatro este año.»

El candidato más probable —«—¿Y las que dejan de venir?» hasta «—Cuatro este año.»— **se lleva
esas cuatro y ninguna otra**. Ranveig pasa de diez réplicas a seis, y de cuatro cosas dadas a
cero. La densidad de negativa del pase sube del 40 % al 67 %.

Es decir: **la poda contra la monotonía se lleva exactamente lo que rompía la monotonía.** El
pase queda como puro rechazo, que es la única lectura de Ranveig que sí sería un problema de
Carta 6 —una profesional que no da nada es una profesional que retiene—, y encima queda
lindando con `S-n1-nocierra`.

El segundo candidato («—Alguien la llevará.» hasta «—Yo sí.») se lleva la negativa del plazo del
duelo, que es material de R5 directo.

**Lo que sí libero, y es lo único.** El bloque `cap-11:201-205` —«—Alguien la llevará.» / «—Sí.
No os sirve de nada.» / «—Yo decido si me sirve.»— duplica el movimiento que `:209-213` hace
mejor. Tres réplicas, 14 palabras. **Lo que se pierde** (§5.6 del plan): «—Yo decido si me
sirve.» es de Nora, y es de las pocas veces en el libro en que la menor le quita a la adulta la
decisión sobre qué le sirve. Yo no lo cortaría; digo que puede cortarse sin tocar el perímetro.

**Tres, y no ocho.** No hay en ese pase un subconjunto de ocho réplicas que no toque Carta 3,
Carta 6 o R5. Si la intervención necesita ocho, la respuesta es no.

**Y añado, porque juega en la misma dirección y no es mío:** la asimetría que A2 declara.
`cap-36` p = 0,034; `cap-11` p = 0,178. Por su propia aritmética `cap-11` no ha despejado el
ruido. `plan-w10 §5.5`: declinar es una respuesta.

---

## 4 · Qué más hay que reanclar (pregunta 4)

`S30-resultado` es lo primero, y no es lo único. Por orden de daño si se olvida:

1. **`S30-resultado`** cambia de fichero. Ancla en «`RESULTADO · TESTIMONIO CONDICIONADO`».
2. **`S30-apertura` se queda donde está, y su `desc` va a mentir.** Dice: «Apertura del cap. 30:
   la asamblea ocurre en la playa de La Jardinera (geografía; RW debe conservarla)». Alguien que
   lo lea dentro de un año, después de que quitemos 113 palabras de playa, concluirá que la
   geografía que había que conservar se destruyó. Hay que dejar escrito que **la geografía
   protegida es la de v0** —Telegrafbukta, el banco de espaldas al agua, las rocas húmedas, las
   tres fogatas, las dos costas, la parte que nadie reclama—, que sobrevive entera, y que lo
   suprimido es topografía nuestra posterior al span.
3. **`b7-perimetro.md` §2**, y este es urgente aunque no se apruebe nada: la tabla de
   correspondencia ya está caduca, desde it.3 y por mi propia aprobación. `aa.reading_order()`
   pone «La asamblea» en 36 y la tabla dice 35, porque «La mosquitera» entró en `orden_lectura`
   21,5 y desplazó 27 filas. La escisión añadiría un segundo desplazamiento. Se corrige en el
   mismo commit, y se corrige con la lección del propio §2 a la vista: el número localiza, el
   literal manda.
4. **`biblia/b5-lista-protegida.md`**, filas de `S30-apertura`, `S30-borrado`, `S30-resultado` y
   la fila 16 de la lista de cierres («En el centro, la fogata ajena sigue ardiendo sola.»), que
   pasa a ser el cierre del capítulo nuevo.
5. **`b3-canon-sistema.md`** — una veintena de punteros `cap-36:NN`, varios ya desplazados hoy,
   y al menos ocho apuntan a lo que sería el capítulo nuevo (`:169-211`, `:213`, `:221`,
   `:229-233`, `:185-205`).
6. **`b1-cronologia.md`**, fila del capítulo, con recuento 1360 y punteros `:125-139` y `:211`.
7. **`b4-ledger-chekhov.md`** — CH-20, CH-60 y CH-80 cruzan el corte. CH-80 además está roto de
   antes (hallazgo 13).
8. **`metadatos.json`**: alta del capítulo nuevo por `actualizar-metadatos.sh`. `orden_lectura`
   **decimal estricto entre 36 y 37** (36,5). Comprobado: `aa.parte_de(36.5)` devuelve 3, porque
   el compilador usa `capitulo_final + 0.9999`. Con 36,5 la Parte III sigue cerrando en la
   votación y la Parte IV sigue abriendo en «El ladrillo». **Con 37 y renumeración en caliente,
   no.** No se renumera nada en esta iteración.
9. **`proteccion: nucleo`** se hereda en el capítulo nuevo, y `pov: Jean`, `fecha: 2061-01-12`,
   `analepsis: false`.

Y sobre la comprobación de método que A2 anuncia: **conforme, y ya la he hecho para el estado de
partida.** `aa.chapter_paths()` imprime **48** hoy, y `reading_order()` los ordena los 48 con
«La mosquitera» en la posición 22. Después de la escisión tiene que imprimir **49**, y la
posición 22 tiene que seguir siendo «La mosquitera»: si sale 49 pero «La mosquitera» se ha
movido, el que se ha roto es otro.

---

## 5 · Condiciones (obligatorias antes del merge)

**A7-it4-C1 · El capítulo nuevo no abre en `cap-36:179`.** Esa frase se suprime con el resto de
la cartografía. El capítulo nuevo abre en «Madre abre tres casillas para las continuidades
activas capaces de decidir.» Ninguna frase que reúna el banco, la fogata o el aro de piedras
ocupa jamás la primera ni la última posición de un capítulo.

**A7-it4-C2 · El título del capítulo nuevo no enuncia.** No nombra ausencia, pérdida, hueco,
casilla, jardinera, duelo, memoria, silencio ni final. Registro procedimental, como «La firma»,
«Acta» o «Auditoría». Es la única voz con autoridad que esta intervención añade al libro.

**A7-it4-C3 · El capítulo A no gana ni una palabra de coda**, como A2 propone. Y tampoco la
gana `cap-36:145`: no crece, no se le añade nada delante ni detrás, y ninguna línea posterior
del libro vuelve sobre los dos huecos ni sobre los dos fuegos retirados.

**A7-it4-C4 · La lista literal de líneas suprimidas se entrega antes del merge**, con las
palabras de cada una, para poder verificar C1 y C3 contra ella.

**A7-it4-C5 · `cap-11`: las ocho réplicas, no.** No se toca ninguna de: «—Dígame lo que sabe
—dijo Nora.», «—Los números que tengo no hablan de vosotras.», «—Nada que yo tenga.», «—No lo
mido.», «—El hospital.», «—Lo mismo.», «—Cuatro este año.» Lo único liberado del pase largo es
`cap-11:201-205`, tres réplicas y 14 palabras, con el coste dicho. **Cortar ocho réplicas de ese
pase, sean cuales sean, es VETO**, porque no existe un subconjunto de ocho que no toque Carta 3,
Carta 6 o R5.

**A7-it4-C6 · Se reancla lo del §4 en el mismo commit**, y `b7-perimetro.md` §2 se corrige
aunque la escisión se caiga, porque ya está caduca por otra causa.

**A7-it4-C7 · Permanente, sobreviva o no esta iteración.** Ninguna voz —narrador, título,
cabecera de parte, índice, sinopsis o faja— enuncia jamás parentesco alguno entre el borrado de
La Jardinera y la muerte de Jean, ni entre el borrado de La Jardinera y el de Nieve en
`cap-44`. Los dos finales de continuidad del libro son opuestos —uno es orden ajena a mitad de
frase, el otro es consentimiento— y esa oposición se sostiene sola. Enunciarla la convertiría en
ecuación, y la ecuación mete la muerte de Jean dentro de una escena que no existe. (R4 · R8 ·
R7·4.)

---

## 6 · Veredicto

**APROBADO CON CORRECCIONES.**

- **Escisión de `cap-36` por `cap-36:177`: aprobada**, con C1, C2, C3, C4, C6 y C7. La costura
  es del autor, el corte no linda con ningún span, el capítulo A termina en una denegación de
  duelo escrita en v0 y no en una elegía, y el capítulo B queda abriendo y cerrando en prosa del
  autor. No veo elegía en el final. Veía un entierro en el comienzo que se proponía, y C1 lo
  retira por 32 palabras que son nuestras.
- **Supresión de la cartografía de playa: aprobada y recomendada**, ampliada a `:179`. Es
  positiva de perímetro por R1, no solo por ritmo: devuelve a diagrama una playa de memoria
  familiar que estábamos convirtiendo en escenario.
- **`cap-11`: denegado tal como se plantea.** Ocho réplicas de ese pase son VETO. Tres,
  `cap-11:201-205`, son libres. Y la asimetría que A2 mismo mide juega en la misma dirección.

**Lo que quiero que quede dicho, por si esto se lee dentro de un año.** Esta iteración existe
porque un titular mío de it.3 era falso y lo encontró otro agente. Mi contribución de hoy es del
mismo tipo: el riesgo que se me traía estaba bien visto y mal localizado, y la tabla de
direcciones de mi propio documento vinculante llevaba caduca desde una intervención que aprobé
yo. Ninguna de las dos cosas la encontró una herramienta.

**Firmado, A7 · W10 it.4 · 2026-08-20 · sobre 48 capítulos y `aa.chapter_paths() == 48`.**
