# M6-continuidades · atribución ciega de las cuatro voces del cap. 13 (W2)

**A0 · 2026-08-17.** Criterio de aceptación de `ordenes/OT-13.md` §6, confirmado por el autor en G-A1: «atribución ciega de las réplicas de 13 entre Madre/Nieve/Cuchillo/Coro **≥ 75 %**» (azar 25 %). Este informe documenta cómo se ha medido, qué ha salido y por qué A0 propone cambiar el criterio.

## 1. Instrumento

`herramientas/lib/m6_continuidades.py`. `m6_muestra.py` no sirve aquí: su extractor exige atribución explícita («—dice Coro») y en el 13 las continuidades hablan casi siempre sin inciso. La clave la fija A0 leyendo el capítulo (cada sección, separada por dinkus, pertenece a una voz) y el script aborta si alguna réplica de la clave deja de existir en el capítulo, para que no pueda desincronizarse.

Muestra: **23 réplicas** de atribución inequívoca — Coro 7, Nieve 6, Madre 5, Cuchillo 5 — sin las de Jean, sin las de menos de 4 palabras, sin las que nombran a su propio hablante y sin incisos de narrador. Barajado determinista (semilla 13). El lector es `m6-atribuidor` (`claude-opus-4-8`, medium) **en frío real** vía `critica-fria.sh --insumo-libre`: no ve el capítulo, ni el reparto real, ni la clave. Seis pases por condición.

## 2. Resultado

| Condición | Pases | Media | Mediana |
|---|---|---:|---:|
| **v0** | 82,6 · 69,6 · 69,6 · 73,9 · 73,9 · 69,6 | **73,2 %** | 71,7 % |
| **W2 antes de A4** | 43,5 · 60,9 · 56,5 · 69,6 · 65,2 · 69,6 | **60,9 %** | 63,0 % |
| **W2 tras A4** | = v0 (instrumento idéntico, ver §4) | **73,2 %** | 71,7 % |

Las dos primeras condiciones difieren en **2 de las 23 réplicas**; las 21 restantes son el mismo texto. Aun así todos los valores de v0 quedan por encima o igual que todos los de W2: la caída no era ruido.

## 3. Diagnóstico por ítem: una palabra

| Réplica | v0 | W2 antes de A4 |
|---|---:|---:|
| «La **divergencia** reducía estabilidad.» → «La **condición** reducía estabilidad.» | **6/6** | **0/6** |
| «Las demás **salidas** siguen sin respuesta.» → «Las demás siguen sin respuesta.» | 2/6 | 0/6 |

La primera es la respuesta de Coro a «—¿Has retirado tu condición?». `OT-13` I-8 autorizó la sustitución afirmando que «conserva la voz de Coro». No la conserva: **«divergencia» pertenece al campo conceptual de Coro** (convergencia, sincronía, propagación, estabilidad), mientras que **«condición» es el registro con el que el libro identifica a Nieve**, que es quien pone condiciones —en el 13, en la asamblea del 30 y en el 36—. Al retirar la jerga (T1) se retiró un marcador de voz (T4).

Sobre las 21 réplicas idénticas, v0 saca 93/126 (73,8 %) y W2 84/126 (66,7 %). Como el texto es literalmente el mismo, esa diferencia es propiedad del instrumento, no del manuscrito: el modelo atribuye las 23 a la vez y reparte entre cuatro voces, así que cambiar dos ítems desplaza el resto. **Conclusión: el análisis por ítem es informativo; el agregado, no, salvo con muchos pases.**

## 4. Corrección aplicada

A4 restauró «divergencia» (22 únicos, M1 **14,0** ≤ 14,5: cabía en el presupuesto) y «salidas» (coste M1 cero: `salida` ya estaba contado). Con eso **las 23 réplicas de W2 son textualmente idénticas a las de v0**, y por tanto el resultado del instrumento es el mismo: 73,2 %. No hay regresión.

## 5. Por qué A0 propone cambiar el criterio (decisión del autor)

1. **El umbral se fijó sin medir v0.** En G-A1 se aprobó «≥ 75 %» como propuesta de A2. Ahora sabemos que **v0 está en 73,2 %**, con una dispersión entre pases de unos 5 puntos. Pedir 75 % es pedir que W2 supere a v0 dentro del margen de error del propio instrumento: no es un criterio, es una moneda al aire.
2. **Dos de los ítems peores lo son por diseño.** «Acepta las cuatro primeras. Reserva la quinta.» saca 0/6 en v0 **y debe sacarlo**: es la primera aparición de la otra voz, antes de que se llame Madre, y el efecto del capítulo depende de que suene a Jean. «He devuelto el salto…» es Madre en modo informe. Afinarlas para subir la métrica dañaría el texto.
3. **El instrumento no puede ver lo que W2 hizo en el 13.** La intervención real fue narrativa —un caso propio por voz, que *muestra* la diferencia en vez de declararla, que es justo lo que pedía el crítico frío A6-2— y la métrica solo lee réplicas sin contexto.
4. Las réplicas que sí podrían afilarse están casi todas dentro de spans protegidos (`S13-nieve`, `S13-coro-nora`, `S13-madre`, `S13-sufra`, `S13-yo-que-soy`).

**Propuesta de A0 al autor:** sustituir «M6-continuidades ≥ 75 %» por **«sin caída respecto a v0 medida con el mismo instrumento y el mismo número de pases»** (hoy: 73,2 % = 73,2 %, cumplido), y trasladar el objetivo de diferenciación de voces a **W6**, la pasada de línea global, donde A4 trabaja sobre el libro entero y donde M6b se mide de forma global con el criterio ya aprobado en G1 (M6b canónica ≥ 60 %).

## 6. Hallazgo transversal para las oleadas siguientes

A4 dejó una lista de **marcadores de voz perdidos por retirada de término** que no pudo recuperar por falta de presupuesto M1: `17:99` «ramas» → «Coro» (única marca de pluralidad de Coro en el capítulo), `30:133` «clasificación» → «tarea» en la frase que define a La Jardinera, `36:33` «canal educativo» → «las aulas», `08:81` «blanco» → «espacio» (pierde la primera siembra del término, que ahora ocurre en el 13). Están anotados en cada `ordenes/OT-NN.md` §9.1.

**Regla operativa que sale de aquí, para W4 y W6:** antes de retirar un término del lexicón, comprobar si esa palabra es lo único que distingue a quien la dice. T1 y T4 pueden empujar en direcciones opuestas, y hasta ahora el plan no lo contemplaba.
