# W10 · Informe final

*Documento vivo. Se cierra cuando se cierre la fase.*

---

## 1. Qué se pidió y qué se encontró

El encargo fue llegar a **9,0 en los once ejes**, con estructura y prosa desbloqueadas por
primera vez, de forma autónoma y sin intervención humana.

**El objetivo no era una propiedad del libro. Era una propiedad de la vara**, y comprobarlo
costó una tarde. Con una rúbrica corregida —cuyas tres reglas escribió el propio jurado al
auditar su escala **sin manuscrito delante**— el manuscrito intacto de v0 saca **9,5 de
global** en las dos familias de modelos, y en estructura puntúa **por encima** de vF.

| | estructura | ritmo | trama | global |
|---|---:|---:|---:|---:|
| v0 · opus-5 | 9,5 | 9 | 9,5 | **9,5** |
| v0 · gpt-5.6-sol | 8,5 | 8,5 | 9,5 | **9,5** |
| vF · opus-5 | 9 | 9 | 9,5 | **9,5** |
| vF · gpt-5.6-sol | 8,5 | 8,5 | 9,5 | **9,5** |

Un objetivo que pasa de incumplido a cumplido según qué regla sostenga el juez, sin que el
texto cambie, no puede dirigir una fase. **El plan preveía este resultado y ordenaba
replantear, no perseguir** (`plan-w10.md` §4b.3). Se replanteó.

**El objetivo pasó a ser el criterio que el autor puso a mano el 18 de agosto:** «ningún
capítulo nombrado como punto de abandono por dos o más lectores en el mismo hito». Discrimina
donde la rúbrica no, responde al trabajo, y estaba fallando.

## 2. El hallazgo de la fase

Cuatro lecturas frías independientes —dos familias de modelos, dos preguntas distintas,
ninguna coordinada— convergen en algo que 48 lecturas anteriores no habían dicho **porque
ninguna lo preguntó**: las 48 eran de rúbrica y preguntaban qué está mal.

> «En este libro no hay ni una sola escena que la trama no necesite. Todos los capítulos están
> justificados. **Y esa es exactamente la carencia.**»
>
> «Sobrecontrol hermenéutico. Casi nada queda fuera de la economía significante de la novela.
> **La emoción no está ausente: está notarizada.**»
>
> «La global no se mueve porque el libro no me ha pedido nada que no pudiera verificar; **y por
> eso mismo no me ha pedido nada.**»

**Y el método del proyecto fabricaba el defecto.** M2 exigía etiqueta de función a toda
inserción; `auditor-adverso.sh` existía para borrar lo que no la pagaba. Durante seis oleadas
se borró sistemáticamente lo único que cuatro lectores fríos piden ahora. La regla era
correcta contra la hinchazón; lo que faltaba era una categoría para la página deliberadamente
inútil. Se creó: `ordenes/SUSPENSION-M2.md`.

## 3. Lo que se hizo, iteración por iteración

### Iteración 0 — divergente

Seis ángulos independientes, un panel de tres jueces con disposiciones opuestas a propósito,
cuatro lecturas abiertas y una sonda de calibración de la escala. Resultado en §1 y §2.

### Iteración 1 — la fusión · **hipótesis falsada**

Se suprimió un tercio de `cap-31` y se fundió el resto en `cap-32`. Excisión pura, cero prosa
nueva, −546 palabras. **Ratio de amplitud de capítulo 1,36 → 2,01**, sin añadir una palabra:
la primera intervención de la fase que atacó el metrónomo.

**Y el muro no se movió: se mudó de capítulo.** vF abandonaba en el 64,0 %; después de borrar
al inquilino, el abandono cayó en el 65,2 % — el capítulo siguiente. A2 lo había preregistrado
antes de medir: *«el muro es posicional y no autoral, y desmiente la hipótesis de la fase;
vale más que el punto de rúbrica».*

**Callejón cerrado:** cortar el capítulo repetitivo que ocupa el muro.

### Iteración 2 — el acto · **criterio superado**

Diagnóstico nuevo, de A2 y no del encargo: *«diez veces, entre el 58,4 % y el 71,7 %, un
personaje con POV tiene delante una transgresión que el propio texto nombra — y las diez veces
la declina»*. El último acto no autorizado está en el 59,5 %; el siguiente, solo planeado, en
el 76,4 %. **El muro entero cae en ese hueco.** No es que todos anoten: es que nadie hace nada
malo durante trece puntos de libro.

Se escribieron cuatro piezas: una tarde muda de Jean con sus hijas dentro de la continuidad;
el acto —Jessie sube el vídeo que su madre le prohibió, sola y en frío—; el hueco del reloj de
Nora, escrito **por ausencia**; y el precio, que llega como persona y no como documento.

**Resultado:** nadie nombra el capítulo tratado, que era el criterio preregistrado. Diálogo
+0,5 y personajes +0,5 —exactamente lo que la intervención tocaba—; estructura y prosa −0,5.

### Iteración 3 — declinada dos veces, y las dos veces con razón

Se encargó cortar el hilo forense de Gunnar. **A2 declinó desmontando la premisa del encargo**,
que era mía y era falsa: los dos críticos que bajaron estructura no son los que nombran ese
hilo, y las cifras que le atribuyen están mal por un factor de dos a cuatro. El argumento
decisivo: *«el auto en blanco sólo está en blanco porque el mecanismo está probado; quitar la
prueba no lo ablanda, lo hace desaparecer»*. Y el clímax de la novela es un hombre leyendo una
cadena de certificados: no admite «menos precisión».

Se reorientó entonces a la escena que cuatro nominaciones pedían —**Jean y Maja vivas y juntas
en presente**— y A2 declinó otra vez, con el hallazgo que produjo el instrumento nº 20: **A7 ya
la había denegado en W5**, y su denegación llevaba cinco oleadas cortada a mitad de palabra.
La escena pedida es, literalmente, la «frase delante o detrás» que aquella denegación prohibía.
No es que no hubiera anfitrión: **el anfitrión sería la causa.**

## 4. La trayectoria del criterio del autor

| campaña | lectores | por nominación principal | capítulos que incumplen |
|---|---:|---|---|
| vF | **7** | **INCUMPLE** | **cuatro**: 31, 20, 27, 15 |
| it1 | 3 | CUMPLE | uno: 15 |
| it2 | 3 | CUMPLE | uno: 15 |
| it3 | 3 | CUMPLE | **ninguno** |

**Y la advertencia que hay que leer antes que la tabla.** Las tres iteraciones se midieron con
**tres** lectores y vF con **siete**. A n=3 el criterio **pasa por azar** entre el 69 % y el
94 % de las veces; a n=7 baja al 3,8 %. Poner las cuatro filas en la misma columna y leer la
diferencia como progreso es **mezclar dos instrumentos de potencia distinta**, y lo encontró
A2 revisando un titular mío. Lo que sobrevive: el fallo de vF a n=7 es señal; los tres
capítulos nuestros que incumplían llevan tres campañas sin ser nombrados; y la evidencia
independiente —A/B ciega 5 de 5, abandono del 40 % al 62 %— no depende de esto.

**Los tres capítulos nuestros que incumplían han salido del censo.** El que queda, «Miles», es
del autor, existe igual en v0 y ninguna oleada lo ha tocado nunca.

## 5. Instrumentos rotos encontrados en esta fase

El proyecto llevaba once. W10 añadió estos:

| # | instrumento | fallo |
|---|---|---|
| 12 | `w10_scores.py` | Comparación estricta donde el paso de la escala **es** el umbral: ante una mejora de exactamente +0,5 —el único resultado que W10 existía para producir— imprimía «sin cambios» y el plan ordenaba revertir. **Determinista, no probabilístico.** Más: el control de deriva se imprimía y no entraba en ninguna comparación, y `mejor_conocido` era un trinquete. |
| 13 | `informes/w5-cap-n4.md` | Contiene una tabla y, doscientas líneas más abajo, su propia retractación firmada. La tabla nunca se actualizó, y su argumento falso denegó un corte correcto en W5. **Una corrección que no borra lo corregido no es una corrección: es una segunda fuente.** |
| 14 | `b1-cronologia.md` | Daba «Interferencias» como `cap-37.md`, que es «El ladrillo»: doble sustitución superviviente del renombrado de W7. |
| 15 | `CLAUDE.md` | Nombraba los ficheros protegidos por sus números **anteriores** a la renumeración. Lo hereda cada agente del proyecto en su contexto. |
| 16 | el censo del verbo de A7 | Falló **al alza**. A7 lo declaró sobre sí mismo y dijo por qué es peor: «un recuento inflado hace que una prohibición mía parezca mejor justificada de lo que está, y nadie discute a la baja una regla de A7». |
| 17 | `spans.json` · cuatro `desc` truncados | Cortados a media palabra desde W5. Uno lo encontró A7 a mano; los otros tres, el verificador nuevo. |
| 18 | `b7-perimetro.md` | Cinco punteros a línea equivocada en cuatro días, y uno de un tipo nuevo: **una paráfrasis entrecomillada**. Regla añadida: dentro de ese documento las comillas significan verbatim. |
| 19 | el extractor de abandonos | Devolvía cadena vacía en dos de tres campañas. El criterio de salida del autor llevaba tres campañas sin poder leerse. |
| 20 | `spans.json` · seis `desc` **amputados en 300 caracteres exactos** | Y falla de una clase que no se había visto: **no a la baja ni al alza, sino por el final, que es donde va la conclusión**. Los 300 que sobreviven parecen una nota completa. Uno de ellos guardaba una **denegación de A7 cortada a mitad de palabra desde W5** — y decidía la iteración 3. |

### El nº 20 merece su párrafo, porque cambia cómo hay que buscar

Mi verificador encontró cuatro de los seis con una heurística: «el `desc` acaba en
preposición». **Se le escaparon los dos que el corte dejó terminando en punto**, y uno de esos
dos es el span que A7 llama «el más importante de todo el encargo».

El detector correcto no es una heurística: es **la longitud exacta**. Un `desc` de 300
caracteres clavados no es una coincidencia, es una amputación. Está en el hook, y se probó
inyectando una amputación real para comprobar que la caza — porque en este proyecto ya hubo un
parche que se ejecutó, no hizo nada, y casi hace concluir que un escritor se había equivocado.

Y el truncador **no está en `herramientas/`**. No hay ningún `[:300]` que quitar: se produjo al
escribir, puede repetirse, y por eso la comprobación vive en el hook y no en la memoria de
nadie.

**Y ninguno de estos lo detectó una métrica.** Todos salieron de que alguien leyera.

## 6. Lo que queda dicho para quien venga después

De A7, y es la mejor frase operativa que ha producido el proyecto:

> «Una condición que vive en un número de línea **está muerta** en cuanto alguien corta un
> párrafo por encima. **Escríbase la condición donde se rompa, no donde se lea.**»

Y su corolario, después de que el verificador nuevo cerrara una clase entera de fallo:

> «El verificador habría fallado en las tres correcciones de hoy: un eco sintáctico, una frase
> parecida y un sinónimo. **Cierra una clase entera de fallo y no toca la que importa.**»
