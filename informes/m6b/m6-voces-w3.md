# M6b en W3 · y un fallo del instrumento que revisa el diagnóstico del proyecto

**A0 · 2026-08-17.** Tres mediciones de atribución ciega sobre la oleada W3, todas en frío real con `m6-atribuidor` (`claude-opus-4-8`, medium) vía `critica-fria.sh --insumo-libre`, tres pases por condición.

---

## 1. M6b global: sin regresión

Muestra regenerada con `m6_muestra.py generar w3` (54 réplicas, 9 hablantes) frente a la muestra de v0 de F1 (56 réplicas, 8 hablantes), medidas **el mismo día y con el mismo modelo**:

| | pases | media | azar |
|---|---|---:|---:|
| v0 | 21,4 · 28,6 · 30,4 | **26,8 %** | 12,5 % |
| w3 | 18,5 · 31,5 · 35,2 | **28,4 %** | 11,1 % |

W3 queda ligeramente por encima **con un hablante más en el reparto** (Aslak entra porque N6 le da réplicas atribuidas: más confusiones posibles y menos azar). No hay regresión.

**Dato que obliga a desconfiar del número:** en F1 este mismo instrumento, sobre **esta misma muestra de v0**, dio 39,3 %. Hoy da 26,8 %. Doce puntos y medio sobre un insumo idéntico. Es la tercera medición de hoy que confirma que esta métrica no discrimina umbrales (ver también `m6-continuidades-w2.md`).

En las tres pasadas, EDDA acierta 100 % y Aslak 50 %; los humanos quedan muy por debajo. Coincide con el patrón que ya describía F1.

---

## 2. El fallo del instrumento: etiquetas, no voces

Criterio de aceptación de `OT-N2` §6: las gemelas tenían que separarse. Se construyó una muestra ciega de 24 réplicas nuevas de N2 (12 de Nora, 12 de Jessie), sin acotación, con el azar en el 50 %:

| pase | acierto | Nora | Jessie |
|---|---:|---:|---:|
| 1 | 20,8 % | 2/12 | 3/12 |
| 2 | 62,5 % | 8/12 | 7/12 |
| 3 | 20,8 % | 3/12 | 2/12 |

**Dos de tres pases por debajo del azar.** En una tarea binaria eso no puede significar «no se distinguen»: un atribuidor que no distinguiera rondaría el 50 %. Sacar 20,8 % exige acertar *sistemáticamente al revés*, y en efecto el fallo es una inversión casi total (diez de las doce de Nora van a Jessie, nueve de las doce de Jessie van a Nora).

Es decir: **el modelo agrupa las réplicas en dos voces coherentes y después decide al azar cuál de las dos se llama Nora**. Nada en las réplicas, despojadas de contexto, dice quién es quién. La puntuación resultante es bimodal (≈21 % o ≈62 %) según caiga la moneda de las etiquetas, y no mide lo que dice medir.

### Comprobación

Se repitió la misma muestra, sin cambiar una sola réplica, añadiendo un **ancla de dos líneas**: una réplica identificada de cada gemela, tomada de otros capítulos y ausente de la lista.

| | pases | media |
|---|---|---:|
| N2 sin ancla | 20,8 · 62,5 · 20,8 | 34,7 % |
| **N2 con ancla** | 75,0 · 87,5 · 95,8 | **86,1 %** |

Confirmado: las voces estaban separadas desde el principio; lo que faltaba era el mapa entre grupos y nombres.

---

## 3. El control de v0, y lo que revisa

Misma prueba, mismo ancla, con las réplicas de las gemelas de la muestra de v0 (14 réplicas):

| | pases | media | azar |
|---|---|---:|---:|
| v0 | 64,3 · 64,3 · 64,3 | **64,3 %** | 50 % |
| **N2 (W3)** | 75,0 · 87,5 · 95,8 | **86,1 %** | 50 % |

**Dos conclusiones, y la segunda importa más que la primera.**

1. **N2 mejora la diferenciación de las gemelas en +21,8 puntos** sobre v0, medido con el mismo instrumento, el mismo ancla y el mismo día. El criterio de G1 (Nora/Jessie ≥ 60 %) se cumple con holgura. Era el criterio principal del capítulo.
2. **v0 ya estaba en 64,3 %, no en 21 %.** El diagnóstico de D1 —«las voces no son distinguibles en frío»— estaba sustancialmente inflado por el fallo de etiquetado. Las gemelas de v0 se distinguen bastante mejor de lo que el proyecto creía.

---

## 4. Consecuencias operativas

- **El instrumento M6b se usa con ancla a partir de ahora.** Sin ella confunde «voces indiferenciadas» con «voces diferenciadas y etiquetas cambiadas», y el error es tanto mayor cuantos menos hablantes tenga la muestra. En la variante global de 8–9 nombres el efecto es más sutil (permutaciones parciales) pero opera igual: **M6b sin ancla infravalora sistemáticamente la diferenciación de voces**.
- **El umbral de G1 (M6b canónica ≥ 60 %) se fijó contra un número producido por el instrumento defectuoso.** A0 propone al autor recalibrarlo cuando se rehaga la medición con ancla, junto con la propuesta D-2 del gate de W2 (anti-regresión en vez de umbral absoluto).
- **Efecto sobre W4 y W6:** T4 (diferenciación de voces) es el objetivo declarado de esas dos oleadas y su prioridad se justificaba con el 39–42 % de v0. Antes de dimensionar ese trabajo hay que rehacer la medición global con ancla por personaje: puede que el problema real sea bastante menor de lo que el plan supone, y que el presupuesto de W4/W6 deba ir a otra parte.
- Ninguna de estas mediciones cambia una palabra del manuscrito.
