# El techo era la vara · veredicto de §4b.3 y cambio de rumbo de W10

**A0 · 2026-08-19.** Este informe cierra el experimento de techo y replantea el objetivo de
la fase, que es lo que `plan-w10.md` §4b.3 ordena hacer si el resultado sale así:

> «Si también sale 8,5, el techo es del instrumento y **el objetivo de la fase hay que
> replantearlo, no perseguirlo**. Este experimento es barato y puede ahorrar la fase entera.»

## 1. El dato

Cuatro lecturas en frío real, dos versiones, dos familias de modelos, el mismo día, con una
rúbrica cuyas tres reglas correctoras **las escribió el propio jurado** al auditar su
historial sin manuscrito delante:

| | estructura | ritmo | trama | **global** |
|---|---:|---:|---:|---:|
| **v0** · opus-5 | 9,5 | 9 | 9,5 | **9,5** |
| **v0** · gpt-5.6-sol | 8,5 | 8,5 | 9,5 | **9,5** |
| **vF** · opus-5 | 9 | 9 | 9,5 | **9,5** |
| **vF** · gpt-5.6-sol | 8,5 | 8,5 | 9,5 | **9,5** |

**v0 —el manuscrito intacto, 41 capítulos, 62.750 palabras, sin una sola intervención del
proyecto— saca 9,5 de global en las dos familias.** El eje que llevaba 48 lecturas clavado
en 8,5 sube un punto entero sin que cambie una coma del libro.

En un eje, v0 puntúa **por encima** de vF (estructura 9,5 frente a 9).

## 2. Por qué esto no es inflar la nota con el prompt

Es la objeción obvia y hay que contestarla, porque si no se contesta el dato no vale nada.

- **Las tres reglas no las puse yo.** Salieron de `w10-calibracion`, una sonda que no
  recibe manuscrito y solo pregunta al jurado por su propia escala. opus-5 respondió que
  reservaba la banda 9–10 como «vitrina» para libros «que ya no necesitan mi nota», que su
  distribución real da **1 nueve y 0 nueve-y-medios por cada cien novelas**, y que descontar
  por falta de eco «no es un defecto: es una laguna mía». Las reglas son su corrección.
- **La regla es simétrica y obliga a acusar.** «Para puntuar 8,5 tienes que escribir, en una
  frase, qué habría que reconstruir.» No premia: exige cargo escrito por cada décima.
- **No se comportó como un inflador.** Ninguna lectura dio 10. opus-5 presentó tres cargos
  concretos contra v0 y los nombró. sol mantuvo estructura y ritmo en 8,5 en las dos
  versiones, y solo movió la global.
- **Y el control funciona:** si fuera inflación ciega, vF habría subido igual que v0. Subió
  igual que v0. **Eso es exactamente el resultado**: la vara no distingue las dos versiones
  ni en 8,5 ni en 9,5. Lo que cambió de sitio es el nivel, no la discriminación.

## 3. Lo que se concluye, y lo que NO

**Se concluye:** el objetivo «9,0 en los diez ejes y en la global» no era una propiedad del
libro. Era una propiedad de la vara. Con la vara vieja es inalcanzable para v0 y para vF por
igual; con la vara corregida ya está alcanzado por v0 y por vF por igual. Un objetivo que
cambia de cumplido a incumplido según qué regla sostenga el juez, sin que el texto cambie,
no puede dirigir una fase de trabajo.

**No se concluye** que el libro sea un 9,5, ni que las seis oleadas fueran inútiles, ni que
no haya nada que mejorar. La vara sigue sin distinguir v0 de vF, que es el mismo problema
que teníamos. Lo que distingue a vF de v0 sigue siendo lo que ya sabíamos y no viene de la
rúbrica: **la A/B ciega da 5 de 5 a vF**, el punto de abandono pasó del 40 % al 62 %, y el
lector beta que abandonaba en el capítulo 15 llega al final.

## 4. El instrumento que iba a destruir la fase

El juez C encontró tres defectos en `herramientas/lib/w10_scores.py`, el marcador de W10.
Verificado por A0 con un banco de pruebas A/B, código viejo contra código nuevo, mismo
insumo y mismo estado inicial:

Insumo: `estructura` y `global` suben **exactamente +0,5** — que es, literalmente y en
exclusiva, el resultado que W10 existe para producir.

```
VIEJO:  estructura 9.0 ← 8.5 · global 9.0 ← 8.5 · «Sin cambios fuera del ruido (±0.5)»
NUEVO:  estructura 9.0 ← 8.5  +0.50  SUBE · global 9.0 ← 8.5  +0.50  SUBE
```

Y `plan-w10.md` §4 ordena: «si el eje objetivo no sube fuera del ruido, **se revierte**».

**El marcador de la fase estaba garantizado para ordenar la reversión de su propio éxito**,
de forma determinista, no probabilística. Los tres defectos, todos fallando a la baja y en
silencio como los once anteriores: comparación estricta `>` donde el paso de la escala es
justo el umbral; el control de deriva del mismo día se imprimía y no entraba en ninguna
comparación; y `mejor_conocido` era un trinquete que subía con el ruido y no bajaba nunca.
Corregidos: `>=`, diferencias emparejadas contra el control de v0 del mismo día, y
comparación por suma de medianas reversible.

Es el **duodécimo** instrumento del proyecto que mide algo distinto de lo que dice su
nombre, y el primero que se caza **antes** de gastar una oleada con él.

## 5. El rumbo nuevo

El autor delegó expresamente los cambios de rumbo: «si tienes que hacer algún cambio en la
dirección o rumbo, hazlo con tu criterio». Lo ejerzo aquí.

**W10 deja de perseguir «9,0 en los once ejes».** El número no discrimina y ya está
cumplido o incumplido a voluntad del que sostenga la vara.

**W10 pasa a perseguir el criterio que puso el autor a mano el 18 de agosto**, que es
medible, discrimina, responde al trabajo y **hoy está fallando**:

> «Ningún capítulo nombrado como punto de abandono por dos o más lectores en el mismo hito.»

Hoy fallan tres: `cap-31` (×3), `cap-27` (×3), `cap-20` (×2). Y los cuatro capítulos que
aparecen en esa lista son capítulos que añadió este proceso.

Ese criterio y el hallazgo de la iteración 0 son la misma cosa vista dos veces, y la unión
la formuló el juez A: esos capítulos **fueron** el intento de añadir resto al libro, y
fracasan porque M2 les obligó a llevar etiqueta de función. **Se les ve el recibo.**

La iteración 1 no escribe seis escenas nuevas. Hace que los capítulos que ya existen para
esto dejen de enseñar el recibo, con M2 y el auditor adverso suspendidos por escrito para
ese material (`ordenes/SUSPENSION-M2.md`). Se mide contra el criterio del autor, no contra
la rúbrica; y en paralelo se sigue puntuando con las dos varas, la vieja y la corregida,
sobre v0 y sobre el candidato el mismo día, porque ahora sabemos que sin eso no se compara
nada.
