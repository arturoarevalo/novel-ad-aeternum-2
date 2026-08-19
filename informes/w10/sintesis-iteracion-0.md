# W10 · Síntesis de la iteración 0

**A0 · 2026-08-19.** Seis ángulos divergentes, cuatro lecturas frías con pregunta abierta
(dos familias de modelos), un experimento de techo y un panel de tres jueces. Esto es lo
que se concluye antes de tocar una palabra.

---

## 1. El hallazgo

Cuatro lecturas independientes —dos modelos distintos, dos preguntas distintas, ninguna
coordinada— dan la misma respuesta, y ninguna de las 48 lecturas anteriores la había dado
porque **ninguna preguntó esto**: las 48 eran de rúbrica y preguntaban qué está mal.

> «En este libro no hay ni una sola escena que la trama no necesite. Todos los capítulos
> están justificados. Todos hacen algo. **Y esa es exactamente la carencia.**»
> — abierta-10, opus-5

> «Sobrecontrol hermenéutico. […] Casi nada queda fuera de la economía significante de la
> novela. […] La emoción no está ausente: **está notarizada**.»
> — abierta-global, gpt-5.6-sol

> «La global no se mueve porque el libro no me ha pedido nada que no pudiera verificar;
> **y por eso mismo no me ha pedido nada.**»
> — abierta-global, opus-5

> «No necesita necesariamente menos páginas. **Necesita páginas con menos funciones
> simultáneas.** […] Un resto que la inteligencia total del libro no consiga utilizar ni
> delimitar.»
> — abierta-global, gpt-5.6-sol

Las dos familias de modelos, por separado, nombran la misma novela de contraste
(*Nunca me abandones*) y el mismo capítulo del libro como prueba de que el libro **sabe**
hacerlo: el 17, «El salero», donde no ocurre nada y tres mujeres cenan.

> «*Nunca me abandones* dedica media novela a Hailsham, a los celos, a un estuche, a una
> cinta de casete. Nada de eso demuestra nada. Es precisamente lo que hace insoportable el
> final. Aquí, «El salero» es ese exceso, **y es el único**. La novela sabe hacerlo y
> decide hacerlo una vez.»

## 2. Lo que esto le hace al proyecto

**El método de las seis oleadas fabricaba el defecto que intentaba curar.**

La regla M2 dice: «toda inserción lleva etiqueta de función; sin etiqueta, se borra».
`herramientas/auditor-adverso.sh` existe para una sola pregunta: «¿paga cada inserción su
etiqueta de función?». Durante seis oleadas, **todo lo que no pagaba se borró**.

Y la respuesta de cuatro lectores fríos a «¿qué le falta para ser un 10?» es: páginas que
no paguen. El proyecto optimizó exactamente la variable equivocada, con rigor, durante
seis oleadas, y por eso el trabajo salió impecable y la nota no se movió.

No es una crítica retrospectiva barata: la regla era correcta **contra la hinchazón**, que
era el riesgo real de una expansión de 62.750 a 80.000 palabras. Lo que estaba mal era
aplicarla sin excepción, y no tener ninguna categoría para la página deliberadamente
inútil.

## 3. Lo verificado a mano (no se toma de ningún informe)

| afirmación | comprobación | resultado |
|---|---|---|
| Jean está viva en pocos capítulos | frontmatter `fecha` < 27-nov-2060 | **cinco**: caps. 1–4 (sus dos últimos días) y el 17, analepsis de 2059 |
| «El salero» es el único donde solo *es* | lectura | confirmado: los otros cuatro son la auditoría, la revocación, el ferry y la muerte |
| CARIES no se dramatiza nunca | 26 apariciones en el compilado | confirmado: **todas referidas**; la escena fundacional (Nora, cuatro años, las teclas negras) se cuenta dos veces de oídas y no se escribe |
| las cuatro partes pesan lo mismo | `compilar.sh` | 19.925 / 20.337 / 20.158 / 19.374 — **4,7 % entre la mayor y la menor** |

**Corrección de cifras:** los pesos de parte circulan en los informes con tres valores
distintos (20.002/20.461/20.316/19.545 y 20.002/20.461/20.316/19.680). Los buenos son los
de arriba, medidos sobre el compilado de hoy tras recompilar. La conclusión no cambia: el
libro está repartido con un metrónomo.

## 4. La ponderación real del jurado

Dato operativo de primer orden, que reordena qué trabajo merece la pena (abierta-global,
sol; opus-5 coincide en lo esencial y difiere en prosa):

| eje | peso marginal en la global |
|---|---:|
| Estructura | 25 % |
| Personajes | 25 % |
| Tema | 20 % |
| Ritmo macro | 15 % |
| Trama | **7 %** |
| Prosa | 6 % |
| Diálogo | **2 %** |

> «La prosa y el diálogo ya superan ampliamente el umbral necesario, pero tienen poco
> margen de influencia sobre la global. […] Otra clave, otra persecución o una capa
> conspirativa adicional **no eleva mi global**.»

Consecuencia inmediata: **W6 (línea) y buena parte de W9 no podían mover la global aunque
se hubieran hecho perfectamente.** Y la trama, que es donde el libro más creció, pesa 7.

## 5. La intervención de la iteración 1

Un solo movimiento con dos mitades, que se compensan en palabras y **invierten la política
del libro**:

**(a) Se corta la capa probatoria de la Parte III** — entre 4.500 y 5.000 palabras, el
corte asimétrico que pide el ángulo 4 («la igualdad es el defecto») y que los dos lectores
abiertos nombran por su cuenta: la fontanería de género. Gunnar, la parka gris, la fuga por
el restaurante indio, el burofax, el seguimiento; y las explicaciones posteriores a
revelaciones que ya se sostienen solas.

> «Haría que la muerte de Gunnar siguiera siendo altamente sospechosa, pero no demostraría
> con tanta precisión el sabotaje técnico. […] **Menos pruebas culminadas, más decisiones
> de no saber.**»

**(b) Ese presupuesto se gasta en páginas sin función.** Candidatas, por orden de defensa
en los informes:

1. **La habitación encendida.** Las tres —Jean, Nora, Jessie— una tarde entera, dentro de
   la `VENTANA REFLEXIVA` del cap. 30, el único lugar de la arquitectura donde una memoria
   puede sostenerse sin que una tarea la recorte. El libro construye el hueco («El recuerdo
   no cabe en la enumeración») y entrega cuatro líneas.
2. **CARIES, escrita.** Dos páginas. La niña de cuatro años, el teclado, «esas teclas hacen
   morder a la canción».
3. **La pregunta de Jessie en el locutorio.** No una respuesta: una pregunta que ningún
   sistema pueda clasificar. «Tú dices que eres Jean. ¿Qué parte de eso es tuya?»
4. **La noche de Alana**, entre los caps. 4 y 5, en presente y en su sitio cronológico.
5. **71-K vuelve.** Alguien cuyas mañanas se pararon. Que se entere el lector, no Jean.
6. **Nora tocando por gusto. Jessie cayendo.** Las dos hijas tienen un objeto y no una
   práctica — que es exactamente lo que Armstrong le hace a Jean.

**La regla que gobierna (b), y que es la inversión exacta de M2:** ningún objeto, frase ni
gesto de estas páginas puede reaparecer después como contraseña, prueba, motivo ni señal.
Si se reutiliza, se ha vuelto funcional y **no sirve**. Se etiquetan `SIN FUNCIÓN` y el
auditor adverso tiene prohibido tocarlas.

## 6. Criterio de falsación

Se compila, se mide con control de deriva sobre v0 el mismo día y jurado de dos familias.
**Si la global y la estructura no se mueven más de ±0,5, toda la familia «resto» se cierra
y se anota el callejón.** No se reintenta con otra escena: la hipótesis es la categoría
entera, no la escena concreta.

## 7. Perímetro — pendiente de A7 ANTES de escribir

Cuatro de las seis candidatas rozan el perímetro y **no se escribe ni una línea hasta que
A7 se pronuncie sobre el brief**: la noche de Alana cae dentro del perímetro sin discusión;
CARIES y la habitación encendida son Jean viva con sus hijas; la pregunta de Jessie es la
frontera misma. El ángulo 4 sostiene además que una segunda escena de Jean viva está
vedada por la regla de sucesión.
