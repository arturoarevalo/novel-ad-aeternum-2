# W4-R · medición de ritmo sobre el manuscrito podado

**A0 · 2026-08-18.** Tres críticos fríos sobre `compilado/ad-aeternum-w4r.md` (79.844 palabras) más **control de deriva sobre v0** leído el mismo día por el mismo juez. Todos en frío real vía `critica-fria.sh`, con sondas de aislamiento LIMPIAS previas (`claude` y `codex`).

## 1. Puntuaciones

| eje | A6-1 | A6-2 | A6-3 | **mediana w4r** | **control v0** | baseline W3 |
|---|---:|---:|---:|---:|---:|---:|
| premisa | 8,5 | 8,5 | 9,0 | 8,5 | 8,5 | 8,5 |
| estructura | 8,5 | 8,5 | 8,5 | 8,5 | 8,5 | 8,5 |
| prosa | 8,5 | 8,5 | 9,0 | 8,5 | 8,5 | 8,5 |
| diálogo | 8,0 | 8,0 | 9,0 | 8,0 | 8,5 | 8,5 |
| personajes | 8,5 | 8,5 | 9,0 | **8,5** | 8,5 | 8,5 |
| mundo | 8,5 | 9,0 | 8,5 | 8,5 | 9,0 | 8,5 |
| **ritmo** | 7,5 | **8,0** | 7,5 | **7,5** | **7,5** | 7,5 |
| trama | 8,0 | 8,5 | 8,5 | 8,5 | 8,5 | 8,5 |
| duelo | 9,5 | 9,0 | 9,5 | 9,5 | 9,5 | 9,5 |
| tema | 9,0 | 9,0 | 9,5 | 9,0 | 9,0 | 9,0 |
| **global** | 8,5 | 8,5 | 8,5 | **8,5** | 8,5 | 8,5 |

**Criterio de salida de W4 fijado por el autor: «Ritmo ≥ 8,0 y Personajes sin caída».**
- Personajes **8,5, sin caída: CUMPLE**.
- Ritmo **7,5: NO CUMPLE**. Es la quinta medición consecutiva en 7,5.

## 2. El dato que decide: el control de deriva

**v0 también puntúa Ritmo 7,5**, leído hoy, por el mismo juez, en la misma sesión. Es decir: **la poda del bloque de cierre no movió el eje, y el eje tampoco se había movido nunca**. Cuatro oleadas de trabajo y una campaña de poda entera no han tocado el número.

Esto no significa que la poda estuviera mal hecha —A2 diagnosticó bien y A4 ejecutó bien— sino que **estaba aplicada al tercio equivocado del libro**. Sin el control de v0 habría concluido que podar no sirve. Lo que dice el control es que podamos donde no dolía.

## 3. Dónde duele, según los cuatro

Los cuatro lectores coinciden con una unanimidad que no habíamos visto en ningún hito anterior, y **ninguno nombra el bloque de cierre**:

| lector | punto de abandono | fichero |
|---|---|---|
| A6-1 | compilado 30 «Interferencias» | **cap-n4** |
| A6-2 | compilado 15 «Miles» | **cap-13** |
| A6-3 | compilado 15 «Miles» | **cap-13** |
| control v0 | 30 «La asamblea»; «el primer aviso llega en el 13» | cap-30 / **cap-13** |

Y las razones son la misma razón:

- A6-1 sobre cap-n4: «tres acosos administrativos paralelos… todos construidos sobre la misma demostración (“No consta responsable individual”), **que ya se había hecho cuatro veces**».
- A6-3 sobre cap-n4: «la segunda suspensión escolar de Nora…, **casi calcada en gestos y formularios** a la del [cap-n2], **es la escena que sobra como escena completa**». Y: «**el centro necesita poda**».
- Control v0 sobre la Parte III: «**22, 27 y 29 ejecutan el mismo movimiento** (una institución mide el daño y no puede detenerlo)».
- A6-2 sobre cap-13: «Introduce a Nieve, Cuchillo y Coro en sucesión rápida, **sin ancla exterior**… **pide crédito antes de haberlo ganado**».

**Reiteración, no densidad.** Es exactamente lo que predijo el instrumento de repetición léxica (`w4r-instrumentos-ritmo.md` §3) y lo que A2 encontró leyendo el cierre. La hipótesis queda confirmada por cuatro lecturas independientes, dos familias de modelos y un control sobre texto no modificado.

## 4. Dos hipótesis mías, refutadas por la evidencia

Conviene dejarlas escritas, porque las dos parecían sólidas y las dos eran falsas:

1. **«cap-08 es el problema de ritmo»** (0,9 % de diálogo, mancha de 1.008 palabras por M5). A6-1, sin que nadie le preguntara: «el 8, “Turno”, **es monótono a propósito y lo justifica** con tres imágenes memorables». *(Nota: compilado 8 = cap-n5; el argumento vale igual para cap-08, al que ningún crítico menciona.)*
2. **«la adyacencia 07 → n5 → 08 repite el ritual tres veces»**, que deduje de la repetición léxica (cap-07 en 7,23 repeticiones por término, cap-n5 en 6,50, contra una mediana de 2,40). Ningún lector la nota, y uno exculpa a n5 expresamente. **El instrumento sobredispara donde el ritual ES el contenido.** Se retira la propuesta de mover N5: no se toca su `orden_lectura`.

La lección operativa es la de siempre en este proyecto y van cuatro: **medir antes de actuar, y con control**. Las dos hipótesis eran mías, estaban bien argumentadas y habrían costado una oleada.

## 5. Y una que probablemente es culpa nuestra

B4 asignó **CH-27** (la cuenta escolar suspendida de Nora) a **dos capítulos nuevos a la vez**: «N2 (estigma de la cuenta suspendida) **y** N4 (re-suspensión “casual” de la cuenta restituida)». Dos críticos dicen ahora que N4 repite la escena de N2 «casi calcada en gestos y formularios». Si se confirma, **pagamos un Chéjov dos veces con dos escenas completas**, y el punto de abandono n.º 1 del libro lo escribimos nosotros en W3. A2 lo está verificando, junto con el resto de la Parte III.

## 6. Lo que no cae

Contra el control de v0, el mismo juez baja 0,5 en diálogo, mundo y trama. Contra la baseline de W3, **la mediana de los tres no cae en ningún eje** y global se mantiene en 8,5. Dado que este proyecto ha confundido tres veces varianza de juez con señal, se registra el dato y no se deduce nada de él: un solo juez, medio punto, sin réplica.
