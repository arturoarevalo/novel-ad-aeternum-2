# W5 · Plan de ejecución (A2, 2026-08-18)

**Qué es esto.** No hay OT nuevas. Las siete están escritas desde F2 y siguen vigentes; lo que sigue es su **reconciliación** con (1) el recuento real de hoy sobre `main`, (2) el bloque de restricciones que A7 y A0 emitieron el 2026-08-18 (P-34…P-43, techo de retenciones, enmienda final a G-3) y (3) el cambio de naturaleza del mandato crítico. Donde el plan y el texto discrepan, **gana el texto y lo señalo**.

**Insumos leídos:** `ordenes/OT-{24,26,31,32,34,35,40}.md` íntegras, `OT-22.md` §9, `OT-22b.md` §4.3–§4.4 y §5, `OT-28.md` §9, `OT-36.md` §5, `OT-37.md` §5, `ordenes/RESERVA.md`, `informes/w4r-diagnostico-centro.md`, `informes/w4r-diagnostico-cierre.md`, `informes/w4r-decisiones-centro.md`, `informes/w4r-medicion-ritmo.md`, `informes/w4r-medicion-final.md`, `informes/a7-w4r.md` §7 y §11–§14, `informes/a6-w4r2-critico-{1,2,3}.md`, `informes/a6-w4r2-deriva-v0.md`, `protegidos/spans.json`, y los siete capítulos.

> ## Versión 2 · incorpora `informes/a7-w5.md` (A7, 2026-08-18): **APROBADO CON CORRECCIONES**
>
> A7 dictaminó los tres gates previos y devolvió ocho correcciones obligatorias, tres de ellas bloqueantes. **Están todas aplicadas en esta versión** y su rastro está en §14. Lo que cambia respecto de la v1:
>
> - **§10.5 reescrita entera**: las declaraciones de paragrafado pasan a **cita textual literal, sin un solo número de línea**, y son **trece**, no doce. Tres traen redacción de A7 que sustituye a la mía (`OT-24` I-2, `OT-35` I-1, `OT-40` I-1).
> - **§10.4 reescrita**: el techo de retenciones se gobierna ahora por el **test de las dos clases (R / A)** de A7, con el censo corregido y **P-45**, **P-46**. Mi argumento en G-W5-1 era malo y A7 lo desmonta antes de darme la razón.
> - **§10.3**: el censo del rasgo de Astrid está en **nueve**, no en siete, y `34:253` **no** es «—También cualquier omisión.». Cita mal puesta, corregida antes de que A5 y A8 la heredasen.
> - **§7**: R3 gana **P-47**, y el motivo de A7 es mejor que el mío.
> - **§8.2**: `OT-26` pasa de «A7 no aplica» a **A7 nota**; **segunda pasada obligatoria de A7 sobre el diff** en seis capítulos.
> - Prohibiciones nuevas vinculantes: **P-44 a P-49** (§10.8).
>
> **Δ de la oleada sin cambios: +768.** Ninguna corrección de A7 mueve una sola palabra del presupuesto.

**Regla de anclaje (vinculante, y evita una clase entera de errores).** **Los números de línea de las siete OT son numeración de v0 y ya no coinciden con el texto**: W2, W4 y la poda de W4-R los han desplazado (`S24-once` figura en `OT-24` §4 como `:45` y hoy está en `:33`; el ancla de `OT-24` I-1 pasó de `:125`/`:127` a `:113`/`:115`). **A3b y A4 anclan por cita textual literal, nunca por número de línea.** Los números que usa este plan son los del texto de hoy, medidos, y se recalculan si algo se mueve.

**Regla de medición (vinculante, de la corrección de A4 en la poda del centro).** Ninguna cifra de este plan es estimada. Todas salen del contador oficial:

```
python3 -c "import sys;sys.path.insert(0,'herramientas/lib');import aa;
fm,l,b,t=aa.read_chapter('capitulos/cap-24.md');print(aa.count_words(b))"
```

Toda hoja de intervención de A3b y toda hoja de línea de A4 **se mide con ese contador antes de firmarse**. Una hoja con cifras de ojo se devuelve sin leerla.

---

## 0. Estado medido hoy sobre `main`

| | palabras |
|---|---:|
| Parte I | 19.925 |
| Parte II | 19.021 |
| **Parte III** | **21.716** |
| **Parte IV** | **18.924** |
| **manuscrito** | **79.586** |

Banda vigente 80.000–82.000 (objetivo 81.000). **Fuera de banda por abajo: faltan 414.**

Los siete capítulos de W5, medidos:

| cap. | palabras | diálogo | tramo máx. sin diálogo | M4b |
|---|---:|---:|---:|---:|
| 24 | 1.637 | 22,7 % | 197 | 7,1 % |
| 26 | 1.704 | 29,9 % | 190 | **16,8 %** |
| 31 | 1.458 | 51,1 % | 72 | 6,1 % |
| 32 | 1.585 | 18,8 % | 339 | 7,0 % |
| 34 | 2.172 | 15,5 % | 374 | 6,2 % |
| 35 | 1.810 | 12,4 % | 228 | 4,7 % |
| 40 | 1.605 | 8,6 % | 272 | 5,9 % |

**Dato estructural que decide buena parte de este plan: la Parte IV es hoy la más corta del libro (18.924) y la Parte III la más larga (21.716).** Cinco de los siete capítulos de W5 están en la Parte IV.

---

## 1. El criterio: apuesta o procedimiento

La queja residual de Ritmo, en boca de A6-1 sobre el compilado `w4r2`, es literal:

> «La Parte III entera (**25–31**) acumula procedimiento sin subir la apuesta.»

**Los números del crítico son de compilado, no de fichero.** Traducidos: 25 = `cap-22`, 26 = `cap-n3`, 27 = `cap-23`, 28 = `cap-24`, 29 = `cap-25`, 30 = `cap-n4`, 31 = `cap-26`. Es decir: **el tramo que el crítico nombra contiene exactamente los dos capítulos de W5 en la Parte III, `cap-24` y `cap-26`, y termina en `cap-26`.** No es una coincidencia cómoda: es lo que obliga a que las dos intervenciones que sobrevivan allí sean de otra clase que el tramo.

### 1.1 · Definiciones operativas (para que A3b, A4, A5 y A8 puedan aplicarlas sin criterio propio)

- **APUESTA.** Tras la inserción, un lector puede nombrar **un coste nuevo, una pérdida nueva o una forma nueva de que el plan falle**. Prueba: si se borra la inserción, ¿desaparece algo que estaba en juego? Si la respuesta es no, no es apuesta.
- **PROCEDIMIENTO.** Contenido que es mecanismo, formalidad, registro, inventario, o **segunda enunciación de algo ya establecido**. Incluye el caso que este libro produce con más facilidad: **explicar un sentimiento que el texto ya ha mostrado**. Una intervención de trama que explica un mecanismo más no es trama.
- **PAGO.** Cobra un plantado ya sembrado (Chéjov). Exento del criterio **solo** si cabe en ≤ 30 palabras y no comenta lo que paga.
- **COSTE CERO.** 0 palabras: M4, M4b, reorden, conservación. Exento por definición; es donde está el mejor rendimiento de esta oleada.
- **TEXTURA.** Mundo narrado sin consecuencia. En W5 **no se ejecuta ninguna**, en ninguna parte del libro. Es lo que W4 metió en el 37 y el 38 y lo que la poda tuvo que sacar.

**Regla de decisión:** PROCEDIMIENTO y TEXTURA se cancelan salvo que cuesten 0. Sin excepciones y sin negociación de palabra a palabra.

---

## 2. (b) Clasificación de las 33 intervenciones

`E` ejecuta · `R` recorta · `X` cancela · `H` ya hecha en la poda

### OT-24 «Accidente» — Parte III

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | PAGO (CH-6)/INTERIORIDAD · el pasado de Tomas | **APUESTA** | 100–120 | **120** | E | Lo piden **dos críticos de tres, por su nombre**: «Tomas necesita una escena previa donde su decisión de preservar el coche de Gunnar **tenga coste personal**» (A6-1); «para que su aceptación en la consola sea la decisión de un personaje y no un requisito de la trama» (A6-2). Es la única deuda del libro con dos peticiones nominales. **Dos prohibiciones nuevas de A7 (§10.9), obligatorias en la hoja de A3b:** no puede ser el caso de 2054 con otro auditor, y la persona del caso anterior no muere ni se le pierde el rastro. |
| I-2 | INTERIORIDAD · la copia sellada, «a mi nombre» | **APUESTA** | 60–80 | **80** | E | Es el coste presente: lo que le queda a su nombre por preservar contra la orden de Mats. Sin ella, `:109` (`PENDIENTE`) y `34:255` (dejar de ser observador neutral) no tienen precio. |
| I-3 | ORIENTACIÓN · F15, el identificador de Hvelv | **PROCEDIMIENTO** | ≤15 | **0** | X | Es una siembra de mecanismo en el tramo que el crítico nombra por acumular mecanismo. F15 se queda en «no sembrada (C)»: la ambigüedad no necesita resolverse. |
| I-4 | TEXTURA · la espera de los nueve minutos | TEXTURA | ≤40 | **0** | X | Mundo narrado en la Parte III. **Contingencia 3.ª** (§4.3). |
| I-5 | TEXTURA · la curva | TEXTURA | ≤40 | **0** | X | Ídem, y encima reconstruye el accidente de Gunnar, que es elíptico. |
| I-6 | conservación de `:213`/`:217` | COSTE CERO | 0 | **0** | E | Se conserva tal cual; `S24-cierre` intacto porque `:115` se varía en I-1. |

**Δ OT-24 = +200** (rango 180–210).

### OT-26 «Casa prestada» — Parte III

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | ORIENTACIÓN · el motivo de la mudanza (ripple N4) | **APUESTA** | ≤25 | **25** | E | Convierte la mudanza de decisión en necesidad: la casa se volvió inhabitable **por hechos**. Además repara una falsedad viva: tras N4, «El seguimiento y la retención bastaban» ya no es verdad. |
| I-2 | TENSIÓN · el instituto retira los medios (ripple N4) | **APUESTA** | ≤30 | **30** | E | La familia pierde su instrumento y pasa a depender de una barca prestada. Es apuesta pura y **va en réplica**, que es lo que este tramo necesita. |
| I-3 | AGENCIA · la reunión del 4-ene gana asunto | **PROCEDIMIENTO** tal como está escrita | ≤60 | **15** | R | Escrita a 60 es **un hilo administrativo nuevo** (un requerimiento de diciembre que la asociación debe contestar) en el tramo que acumula administración. Se recorta a **≤15 palabras dentro de la réplica de `:175`**, remitiendo a la resolución de 2057 que la lata ya dramatiza (`:89–:101`). Deja de ser hilo y pasa a ser remisión. |
| I-4 | TEXTURA · el oficio antes de dormir | TEXTURA | ≤50 | **0** | X | Ya cancelada en `w4r-diagnostico-centro.md` §5.6. **Motivo nuevo que la confirma:** su ancla (`:183–:189`) está pegada a `S26-bocana` (`:191`), **span de anclaje único**, donde M9 es ciego a todo el entorno. |
| I-5 | TEXTURA · M4b, recomposición de antepuestas | **COSTE CERO** | 0 | **0** | E | **Es el trabajo principal del capítulo.** 16,8 % (17/101) es el peor porcentaje editable del libro —solo `cap-03`, protección total, está peor—. Hay que recomponer **≥ 9** para bajar de 8 %. Cuesta 0 palabras. |

**Δ OT-26 = +70** (rango 55–85).

### OT-31 «El ladrillo» — Parte IV

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | TENSIÓN/AGENCIA · el plan B explícito | **APUESTA** (definición literal) | 130–170 | **180** | E | Los **tres** críticos dicen que el clímax se concede: «Tomas acepta la petición sin arco previo, la orden de custodia llega en el minuto exacto» · «es una comodidad» · «conveniencia en que tantos actores independientes acierten a la vez». I-1 dice en voz alta **qué se pierde si falla el eslabón que no es suyo**. Va en ≤ 6 réplicas cortas: sube diálogo en un capítulo que ya está al 51 %. Autorizado por la propia OT hasta 190. **Incorpora P-48 antes de escribirse** (§10.8): ninguna voz presenta el final de la continuidad de Jean como descanso, alivio o resultado preferible. |
| I-2 | INTERIORIDAD · el cuaderno de Nora | TEXTURA/método | ≤40 | **0** | X | Duplica la cola de I-1, que ya incluye la anotación en el cuaderno. **Contingencia 1.ª** (§4.3). |

**Δ OT-31 = +180** (rango 165–195).

### OT-32 «La oferta» — Parte IV

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | TENSIÓN · la interferencia fallida da sentido al veto | **APUESTA** | ≤80 | **80** | E | Carga CH-1: la amenaza de Coro deja de ser una pistola descargada porque **ya se intentó y dejó rastro**. Es lo que convierte `:83` de escrúpulo en conclusión. **Posición fijada: entre `:79` y `:81`; prohibida la alternativa «tras `:81`»** (§5.2). |
| I-2 | INTERIORIDAD · la cala de Mats | **APUESTA** | 80–120 | **100** | E | Es el único sitio del libro donde **el antagonista tiene algo que perder**: guarda íntegros sus propios intentos de voz mientras firma «Las necesarias» para las demás. A6-1: «gana espesor con la ELA oculta». No se enuncia: se mira y se firma. **A7 vigila el borde:** ningún paralelo, ni enunciado ni sugerido por montaje, entre la enfermedad de Mats y la muerte de Jean; nada que lea «él también sabe lo que es desaparecer». |
| I-3 | TEXTURA · el mundo alrededor de la negociación | TEXTURA | ≤50 | **0** | X | **Contingencia 2.ª** (§4.3). |

**Δ OT-32 = +180** (rango 160–200).

### OT-34 «Soldagen» — Parte IV, bloque de cierre

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | INTERIORIDAD · la cala de Tomas antes de aceptar | **APUESTA** | 100–130 | **100** | E | Segunda mitad de la deuda que dos críticos nombran. Lo que le costará validar durante la cobertura, **antes** de que Jessie llegue. Tope 100 por `w4r-diagnostico-cierre.md` §6.2, que mantengo. |
| I-2 | TEXTURA · la butaca de Astrid | **PROCEDIMIENTO** + colisión con **P-43** | 70–100 | **0** | **X** | **Cancelada, y A7 lo confirma como permanente (G-W5-2).** (1) Tras la poda la escena ya tiene **seis réplicas**: el argumento de «darle cuerpo» está caducado. (2) §6.2 la reespecificaba como «un intercambio más con el representante ministerial», y ese intercambio es el bloque que va de «—Hay cuarenta y dos delegaciones. Cualquier actuación tendrá consecuencias fuera de este auditorio.» a «Astrid no movió la carpeta.», con **«—También cualquier omisión.»** dentro: ampliarlo produce la instancia nueva o diluye la última. (3) La forma original («Astrid consigna: lo que anota o no anota») **es** el gesto censado y además roza la clase R. **P-43: cero instancias nuevas.** No puede volver en W6 ni con otro nombre, ni como «cuerpo de la testigo», ni como «un intercambio más». |
| I-3 | COSTE CERO · cierre de `:257` | COSTE CERO | 0 | — | **H** | **Ya ejecutada por A4 en la poda.** La escena cierra en «Astrid no movió la carpeta.». |
| I-4 | COSTE CERO · cierre de `:223` | COSTE CERO | 0 | — | **H** | **Ya ejecutada.** «A las doce, la retransmisión mundial quedó abierta» abre la escena de Astrid. |
| I-5 | TEXTURA · Alana en el lateral | TEXTURA | ≤40 | **0** | X | Cancelada en §6.2; se confirma. |

**Δ OT-34 = +100** (rango 90–110).

### OT-35 «Caída» — Parte IV, bloque de cierre

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | PAGO (CH-4) · cae sin hacerse daño | **PAGO** | ≤30 | **30** | E | Una línea. Paga `3:123` y `9:181`. La caída es **consecuencia de que su madre tire de ella**, no proeza (Ap. F P7). |
| I-2 | TEXTURA · el fondo de la barca | TEXTURA | 40–60 | **0** | X | Cancelada en §6.2; se confirma. |
| I-3 | TENSIÓN/TEXTURA · Jessie ante el armario | TEXTURA | ≤50 | **0** | X | Ídem. |
| I-4 | ORIENTACIÓN · continuidad de `:149` | **COSTE CERO** | 0 ± 15 | **0** | E | Decisión de A5, no de estilo: las preguntas de Tomas fueron en Fyret (16), no en la comisaría (24); y v0 no da vía por la que Jessie sepa lo del coche de Gunnar antes de que la consola se lo enseñe (`:179`–`:187`). |

**Δ OT-35 = +30** (rango 20–35).

### OT-40 «Sombra» — Parte IV, bloque de cierre

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | PAGO (CH-2) · «No preguntó por el cinturón.» | **PAGO** (clase A: abstención, no retención) | ≤8 | **8** | **E** | **G-W5-1 resuelto: NO es la quinta retención.** A7 la ejecuta, con **literal congelado**, en la **posición (b)** —segunda oración del párrafo del jueves—; la posición (a) queda **VETADA**. Ocho condiciones de ejecución en §10.4 y §10.5. **CH-2 → PAGADO.** |
| I-2 | INTERIORIDAD · Nora ante el altavoz | **PROCEDIMIENTO DEL SENTIMIENTO** + **clase R** | 50–60 | **0** | **X** | **Cancelada, y A7 la cierra con carácter permanente.** Es ella, y no I-1, la que incumplía el techo: «el precio de no preguntar lo que escribió» es **clase R pura** sobre un ítem que v0 ya retiene y ya cobra. **Y v0 es la razón de fondo.** v0 ya tiene el objeto —«Nora llevaba una hoja doblada dentro de la mochila. La noche anterior había escrito una pregunta, la había corregido dos veces… hasta la versión falsa que preparó para comprobar una respuesta le pareció una trampa.»— y ya lo cobra —«El jueves no volvió con la misma pregunta.»—. I-2 sería **un tercer beat sobre el mismo objeto, entre los dos que ya existen**. Además sería la quinta ejecución de «no preguntar» en un capítulo que ya la hace cuatro veces: la hoja, «No preguntó qué había dicho Jean.», la transcripción en blanco de Jessie y «El jueves no volvió con la misma pregunta.» |
| I-3 | TEXTURA · la casa entre turnos | TEXTURA | ≤40 | **0** | X | Cancelada en §6.2; se confirma. |
| I-4 | AGENCIA/TEXTURA · cierre de `:163` | **COSTE CERO**, reespecificada | ≤25 | **0** | E | **Discrepancia plan↔texto: gana el texto.** La OT pedía convertir en réplica el anuncio de la sesión siguiente de `:161`; **la poda borró `:161`** (corte 6) porque `:175` lo dice mejor. La réplica ya no tiene fuente y añadirla reintroduciría lo que se quitó. **Nueva forma, 0 palabras:** se permuta el párrafo del sensor con el de la tabla, de modo que la escena cierre en «Maja efectuó el pago allí mismo.» — un acto, no un objeto. M4 del capítulo 2 → 1. Ejecuta **A4**, no A3b. |
| I-5 | PAGO (CH-9) · **R3 beat 3** | **PROCEDIMIENTO / REITERACIÓN** | ≤250 | **0** | **X** | §7. A7 suscribe la cancelación con un motivo mejor que el mío y **cierra el tramo a toda inserción para siempre (P-47)**. |
| I-6 | ORIENTACIÓN · `:161`/`:175` no se retocan | COSTE CERO | 0 | **0** | E | Confirmado: N6 (11-may) es posterior. |

**Δ OT-40 = +8** (rango 0–10).

### Fuera de las siete OT

| ítem | clase | | motivo |
|---|---|:-:|---|
| **R3, resto (425)** | — | **X** | §7. No se coloca; queda en reserva del autor. |
| **Ripple de N4 en `cap-36`** (`OT-36` §5: una línea de registro ≤ 8 palabras, «entrante W5») | **PROCEDIMIENTO** | **X** | **Rechazada por A0**, como la propia OT prevé: «si en W5 A0 lo rechaza, CH-1 queda pagado con N4 + 32 y el arco sigue legible». Es una cláusula de pacto más en el libro cuya queja es la acumulación de cláusulas, y reabriría un capítulo de W2 por ocho palabras. |
| **`OT-37` §5, beat ≤ 30 en `37:73–79`** | TEXTURA | **X** | «Por defecto NO» en la propia OT. Se confirma NO. |
| **`OT-37` §5, cruce sala de 34 ↔ 37** | COSTE CERO | E | Tarea de A5, sin palabras. |

**Recuento (33 ítems).** **16 se ejecutan:** 11 con palabras (una de ellas, `OT-26` I-3, recortada de 60 a 15) y 5 a coste cero. **15 no se ejecutan:** 13 canceladas dentro de las siete OT y 2 rechazadas fuera de ellas. **2 ya estaban hechas** (`OT-34` I-3 e I-4, ejecutadas por A4 en la poda).

---

## 3. (a) Reparto final por capítulo

| OT | cap. | parte | hoy | Δ W5 | vF | banda OT vigente | **banda reformulada** | escritor |
|---|---|:-:|---:|---:|---:|---|---|---|
| OT-24 | 24 | III | 1.637 | **+200** | 1.837 | ~~1.915–2.015~~ | **1.815–1.860** | A3b |
| OT-26 | 26 | III | 1.704 | **+70** | 1.774 | ~~1.854–1.954~~ | **1.755–1.790** | A3b |
| OT-31 | 31 | IV | 1.458 | **+180** | 1.638 | 1.608–1.708 | **sin cambio** | A3b |
| OT-32 | 32 | IV | 1.585 | **+180** | 1.765 | ~~1.785–1.885~~ | **1.745–1.785** | A3b |
| OT-34 | 34 | IV | 2.172 | **+100** | 2.272 | ~~2.523–2.623~~ | **2.262–2.282** | A3b |
| OT-35 | 35 | IV | 1.810 | **+30** | 1.840 | ~~1.920–2.020~~ | **1.830–1.845** | A3b |
| OT-40 | 40 | IV | 1.605 | **+8** | 1.613 | ~~1.824–1.924~~ | **1.605–1.615** | A3b + A4 (I-4) |
| | | | | **+768** | | | | |

**Reformular seis de las siete bandas es un acto formal y queda registrado aquí, igual que G-3′.** Las bandas de §0 y §6 de cada OT se calcularon en F2 como *v0 + Δ objetivo*, antes de la campaña de ritmo y antes de la poda; A8 las comprueba y **fallaría la oleada por construcción** si se dejan como están. El precedente es el que A0 ya aceptó para `cap-29`: «la banda por capítulo es construcción nuestra, derivada de una proyección». Lo que **no** se reformula es ningún criterio de contenido.

**Rango de la oleada:** Σ mínimo 670 · Σ planificado 768 · Σ máximo 845.

---

## 4. (e) Aritmética de banda

### 4.1 · Por parte

| parte | hoy | Δ W5 | **vF W5** | techo aplicable | margen |
|---|---:|---:|---:|---|---:|
| I | 19.925 | 0 | 19.925 | — | — |
| II | 19.021 | 0 | 19.021 | — | — |
| **III** | 21.716 | **+270** | **21.986** | **≤ 22.150** (`w4r-diagnostico-centro.md` §9) | **164** |
| **IV** | 18.924 | **+498** | **19.422** | — (la más corta del libro) | — |
| **total** | **79.586** | **+768** | **80.354** | banda 80.000–82.000 | **+354** sobre el suelo |

Con el rango completo: **80.256 – 80.431**. En banda en los dos extremos. Parte III entre 21.951 y 22.011: **el techo no se roza ni en el peor caso.**

**Y el dato que importa más que el techo: la Parte III termina W5 en 21.986, es decir 77 palabras POR DEBAJO de las 22.063 que tenía cuando los tres críticos la leyeron y la nombraron.** No hay crecimiento neto que defender.

### 4.2 · Bloque de cierre

| | antes de la poda | hoy | vF W5 |
|---|---:|---:|---:|
| bloque 34–41 | 14.963 | 14.233 | **14.371** |
| tramo 34→40 | 12.618 | 12.081 | **12.219** |

W5 devuelve al bloque **+138 de las −728 que la poda le quitó**: el 19 %.

### 4.3 · Riesgo por abajo y escalera de contingencia

80.354 deja **354 sobre el suelo**, y W6 es una pasada de línea global que históricamente resta. La contingencia está decidida **por adelantado** para que nadie improvise a mitad de W6:

| orden | qué | Δ | dónde | requiere |
|---|---|---:|---|---|
| 1.ª | `OT-31` I-2 (cuaderno de Nora) | +40 | Parte IV, fuera del tramo seco | A0 |
| 2.ª | `OT-32` I-3 (textura de Fyret) | +50 | ídem | A0 |
| 3.ª | `OT-24` I-4 (la espera de los nueve minutos) | +40 | Parte III — **solo si la Parte III conserva ≥ 100 de margen** | A0 |
| 4.ª | R3, resto | +425 | **nunca en `cap-40`** | **autor** (G-A1 fijó destinos) |

Tolerancia total a una resta de W6: **354 + 130 sin gate, + 425 con gate = 909.** La pasada de línea de W4 restó 13 palabras en dos capítulos: no hay riesgo real, pero queda cubierto.

**No propongo engordar W5 para acercarse a 81.000.** 80.354 está en banda; el objetivo es el centro de la banda, no un contrato. Rellenar ahora para no medir después es exactamente §1.1.

---

## 5. Conflicto 1 — la Parte III

### 5.1 · Las 66 palabras de exceso no existen

El cálculo que las produce (21.716 + 300 + 200 = 22.216) toma `OT-26` a su Δ nominal de **+200**. Pero **el mismo párrafo que fijó el techo de 22.150 ya había recortado `OT-26`**: `w4r-diagnostico-centro.md` §5.6 dice, literalmente, «`OT-26` I-1 (+25), I-2 (+30), I-3 (+60): se ejecutan. `OT-26` I-4 (textura del oficio antes de dormir, «opcional»): **se cancela**. […] **Parte III: +500 → +415**». El techo y el recorte son la misma decisión. Lo que discrepa es `mapa_ot.py`, que lee los Δ nominales de `ordenes/tabla-5-1.json` y no puede saber qué canceló un informe.

Con el recorte de §5.6 la Parte III aterrizaba en 22.131: **19 palabras de margen.** Eso no es un plan, es una casualidad. Por eso no me quedo ahí.

### 5.2 · Lo que hago, y no es «se compensa con poda»

**Recorto por función, no por aritmética**, y el resultado es que la Parte III recibe **+270 en vez de +500**:

- `OT-24` pierde I-3, I-4 e I-5 (−95). Las tres son procedimiento o textura en el tramo que el crítico nombra por acumular procedimiento.
- `OT-26` pierde I-4 (ya) y recorta I-3 de 60 a 15 (−45 sobre §5.6, −95 sobre el nominal).

**No pido una sola palabra más de poda en la Parte III.** No la hay que pedir: acabo de comprobar que el techo aritmético de la poda del centro era −615 y que A4 entregó −394 defendiendo cada declinación con razón. Y tengo el aviso escrito de mi propia medición: **podar alrededor de una escena la agranda** —la cena de N3 pasó del 30,7 % al 38,8 % del capítulo por culpa de una poda mía, y A6-1 abandona ahí ahora.

### 5.3 · Por qué las dos supervivientes sí pueden entrar

**`OT-24` I-1 + I-2 es la única deuda del libro que dos críticos de tres piden por su nombre.** A6-1 pide «una escena previa donde su decisión de preservar el coche de Gunnar tenga coste personal»; A6-2 pide «construir a Tomas Eide […] para que su aceptación en la consola sea la decisión de un personaje y no un requisito de la trama». No es textura: es la reparación de una de las tres junturas que los críticos llaman concesiones del clímax. Y su contenido —una cartera con carnés que ya no abren nada— es lo contrario del procedimiento.

**`OT-26` I-1 + I-2 son 55 palabras que convierten una mudanza en una consecuencia** y que le quitan a la familia su barca. Apuesta pura, en réplica, y encima reparan una frase que tras N4 es falsa.

**Y el trabajo mayor de `cap-26` no cuesta palabras: M4b de 16,8 % a ≤ 8 %.** Es el peor porcentaje editable del libro y lo arregla A3b/A4 sin añadir nada. Si W5 solo hiciera eso en el 26, ya habría valido la pena abrirlo.

### 5.4 · Y digo lo que el techo es

**El techo de 22.150 lo inventé yo y mide la cosa equivocada.** Se derivó de «≤ 21.700 tras la poda» + «+415 de W5», y la poda entregó −394 en vez de −479, así que el techo arrastra un supuesto que no se cumplió. Lo mantengo como guardarraíl porque es prudente y porque se cumple con holgura, **pero el criterio bueno es otro y es el que W5 persigue**: que ninguna intervención de la Parte III sea una octava ejecución del mismo movimiento. Ninguna de las cuatro supervivientes lo es.

---

## 6. Conflicto 2 — el bloque de cierre

### 6.1 · Reconciliación

| fuente | cifra |
|---|---:|
| `ordenes/tabla-5-1.json` (34 +250 · 35 +150 · 40 +150) | +550 |
| … más R3 en el 40 (425 sin colocar) | +975 |
| `w4r-diagnostico-cierre.md` §6.2, lo que prometí ayer | **≈ +400** |
| **este plan** | **+138** |

Bajo de 400 a 138 y no es capricho. §6.2 mantenía cuatro cosas que hoy no se sostienen:

1. **`OT-34` I-2 a +60** — la mata **P-43**: el rasgo de abstención de Astrid está **en nueve** (§10.3) y dos de las nueve viven en la escena que I-2 iba a ampliar —«—También cualquier omisión.» y «Astrid no movió la carpeta.»—. Las dos formas posibles de I-2 producen una instancia nueva o diluyen la última. **A7 lo confirma como cancelación permanente (G-W5-2).**
2. **`OT-40` I-2 a +50** — la mata el texto y la mata el techo: la hoja doblada ya está escrita en v0 y ya se cobra en v0, y el beat intermedio es **clase R sobre un ítem ya retenido**. A7: «quien lo incumplía era `OT-40` I-2, no I-1».
3. **`OT-40` I-4 con «+1 réplica»** — la mata la poda: su fuente (`:161`) ya no existe. Sobrevive como reorden a 0 palabras.
4. **R3 beat 3 a +150** — §7.

Lo que queda es **+138: una cala de apuesta (34), dos pagos Chéjov de una línea (35, 40) y dos operaciones de coste cero**. No hay una sola palabra de textura narrada.

### 6.2 · Dos criterios míos que retiro

`w4r-diagnostico-cierre.md` §7 fijó **bloque 34–41 ≤ 13.900** y **tramo 34→40 ≤ 11.800**. Hoy están en 14.233 y 12.081 y W5 los deja en 14.371 y 12.219. **No se van a cumplir y no voy a fingir que sí.**

Los escribí bajo una hipótesis que el control de deriva refutó el mismo día: que el bloque de cierre era el problema de Ritmo. **v0 puntúa Ritmo 7,5 y ninguno de los cuatro lectores nombra jamás el cierre.** Un criterio de tamaño para un tramo que nadie señala es un criterio que mide lo que no duele. **Se retiran** y los sustituyen tres que sí responden:

- **réplicas perdidas en el bloque = 0** (regla dura, se mantiene);
- **ningún crítico nombra 39–45 del compilado como reiteración** en el hito de W5;
- **el tramo máximo sin diálogo no sube en ningún capítulo del bloque.**

Retiro también, por lo mismo, **«diálogo `cap-34` ≥ 15,5 % tras W5»**: presuponía una poda de −280 en el 34 que A4 entregó como −223 con razones que acepté, y sobre la que yo restituí +72. Con +100 de cala, el 34 queda en ≈14,8 %. La cala de Tomas es un hombre solo ante un armario; **forzar réplica ahí rompería el personaje para salvar un porcentaje que A0 ya decidió no usar para dirigir trabajo**. Se sustituye por: *tramo máximo ≤ 374, sin subir; 0 réplicas perdidas.*

---

## 7. (c) R3 · dónde va, y por qué no va a ninguna parte

**R3 se cierra en 175 de 600. Las 425 restantes no se colocan en W5.**

**Lo gastado.** Beat 1, `cap-22` (81, W4): el cuaderno pautado que es de música y se usa como cuaderno de datos. Beat 2, `cap-28` (94, W4): la digitación sobre la rodilla, «—¿Ya hay fecha para la repesca?» / «—En marzo. El día lo dan al cerrar la lista», y el coste (la furgoneta que Nora apunta sin matrícula). Los dos beats, con voz, ya hacen lo que la partida pedía: «continuidad, no subtrama».

**Por qué el beat 3 no se ejecuta.** No es cuestión de presupuesto: es que **`cap-40` ya paga CH-9 tres veces por su cuenta**, en texto de v0:

- «Guardó la partitura, corrió hasta la parada y **alcanzó el autobús de clase**.»
- «La profesora cerró la puerta del aula […] **Nora pasó la hora siguiendo otras voces**.»
- Y, dentro de `S40-cierre`: «A esa hora tenía **ensayo con otras tres personas**», más la convocatoria con «los otros tres nombres y una lista de pasajes que todavía no habían logrado tocar sin detenerse».

Un beat de ensayo con vivos sería la **cuarta** ejecución del mismo movimiento en el mismo capítulo. Es literalmente el defecto que la campaña de ritmo identificó y midió —reiteración, no densidad— aplicado por nosotros, a mano, en el capítulo del silencio, dentro del bloque que el autor acaba de podar −728 porque «el libro sigue explicándose después de haber terminado».

Y hay dos razones técnicas que se suman:

- **Emplazamiento.** El ancla de I-5 es «alrededor de `:131`», es decir **inmediatamente antes de `S40-despedida`**, que es un **span de anclaje único** (51 de los 109 lo son) y una de las líneas más protegidas del libro. Bajo la enmienda final a G-3, insertar al lado **cuenta como modificarla**, y M9 es ciego a todo su entorno.
- **Diálogo.** «Con voces», como pedía §6.2, subiría el diálogo del capítulo cuyo contrato explícito es no subirlo (`OT-40` §6: «7–11 %; no se sube: es el capítulo del silencio»).

**Qué pasa con CH-9.** Queda **PAGADO** con 3 → 9 → 10 → 18 → 22 (R3-1) → 28 (R3-2) → 40 (v0, tres beats) → 41. No hay pago huérfano y M10 no cambia de estado por esto.

### 7.1 · El motivo de A7, que es mejor que el mío — **P-47**

A7 suscribe cerrar R3 en 175 y añade una razón que no es de ritmo y que yo no vi. El destino previsto por `RESERVA` §1 R3 es la elipsis de febrero, es decir **entre «Nadie le pidió un resumen.» y `S40-despedida`**. Un beat de ensayo con vivos ahí quedaría **inmediatamente antes** de «Una tarde encontró otra vez únicamente el nombre `Despedida`. No abrió el archivo. Restringió el acceso, decidió conservarlo y fue a poner la mesa para cenar.», y produciría la cadencia que la Carta prohíbe en su punto 6:

> *tiene amigos → no abre el archivo → alivio*

La negativa de Nora dejaría de ser una decisión que sigue abierta y pasaría a ser **un peldaño de recuperación**. Hoy el capítulo la rodea de dos beats secos —el aula, la mesa— y deja el trabajo de los vivos para el final, donde está ganado (`S40-cierre`).

> **P-47 · el tramo del `cap-40` comprendido entre «Nadie le pidió un resumen.» y `S40-despedida` queda cerrado a toda inserción**, en W5, W6, W7 y en cualquier activación de reserva. `S40-despedida` es además de anclaje único: M9 es ciego a su entorno.

Mi motivo —cuarta ejecución del mismo movimiento— sigue siendo válido y es el que gobierna el presupuesto. El de A7 es el que gobierna el permiso, y es el que hay que citar si alguien vuelve a proponerlo.

### 7.2 · Qué pasa con las 425

No se reasignan y no se cancelan: quedan como **4.ª contingencia del ledger** (§4.3), a decisión del autor porque G-A1 fijó sus destinos (22/28/40). Si se activan, **no van al 40** —P-47 lo cierra—: el sitio que quedaría es un cuarto beat en `cap-28` o en `cap-22`, ambos en la Parte III, lo que exigiría revisar el techo de §5. A7 añade dos condiciones que hago mías: **(i) ningún beat de R3 puede quedar contiguo a un beat de duelo, a `Despedida` o a un locutorio; (ii) la repesca no se resuelve** (v0 no dice si Nora entra en Kongsbakken), que en `RESERVA` figuraba como riesgo y pasa a ser condición.

**Mi recomendación sigue siendo no activarlas nunca.** Una reserva es una autorización de gasto, no una cuota; gastarla para cuadrar un número es la definición de engordar.

---

## 8. (d) Orden de ejecución y gates

### 8.1 · Antes de escribir una palabra

| # | qué | quién |
|---|---|---|
| 0.1 | `inyectar-frontmatter.sh --set cap-NN.md estado=en_oleada` en los siete (`cap-24` figura hoy como `terminado` pese a haber sido podado en W4-R) | A0 |
| 0.2 | Rama `w5-trama` desde `main` | A0 |
| 0.3 | `proteger.sh verificar` (109 spans) y `medir.sh w5-base --baseline v0` como línea de partida | A8 |
| 0.4 | ~~Consulta previa a A7~~ · **HECHA: `informes/a7-w5.md`, APROBADO CON CORRECCIONES.** Los tres gates resueltos (§11) | A7 |
| 0.5 | **A3b lee `informes/a7-w5.md` §2.4, §2.5, §5.2–§5.4 y §7 antes de escribir**, y copia en su hoja las declaraciones de §10.5 que le tocan | A3b |

### 8.2 · Orden

**Se ejecuta en orden de lectura, en tres tandas.** Las dependencias reales son tres y todas quedan satisfechas: `OT-24` fija el canon del pasado de Tomas que `OT-34` no puede repetir y que `OT-35` I-4 necesita cerrado; `OT-26` necesita `cap-n4` y `cap-n6` aceptados (lo están); `OT-40` necesitaba el dictamen de A7 sobre I-1, que **ya está emitido**.

**Segunda pasada obligatoria de A7 sobre el diff** (no sobre la OT) en **seis capítulos**: `cap-40` (I-1 e I-4), `cap-35` (I-1), `cap-31` (I-1), `cap-32` (I-2), `cap-24` (I-1 e I-2) y `cap-26` (I-1, I-2 y la declaración de las nueve antepuestas de I-5). `cap-34` I-1 queda en nota. **Ningún capítulo se da por cerrado sin ella.**

| # | OT | tanda | por qué ahí | gates que dispara |
|---|---|---|---|---|
| 1 | **OT-24** | A | Fija el canon de Tomas (B2 §6). Todo lo demás de Tomas cuelga de aquí | **A7 sobre el diff, obligatorio** (el pasado no puede rimar con el acto, con UNN ni con una muerte; ni clínica, ni menor, ni vehículo; **§10.9: no repetir el caso de 2054 —debe diferir en dos de tres— y la persona del caso anterior no muere ni se le pierde el rastro**) · **A5** (2-ene domingo; OTA 23:16 del 16-dic; canon nuevo a B2 §6; G-3′ sustituye al checklist «segunda mitad con diff vacío») · **A8** (M1 baja a ≈6,7 por denominador; M2 = 0; **tramo ≤ 197**; M4: la escena deja de cerrar en «La devolvió a la cartera.»; `S24-once` («Once segundos en blanco en la percepción.») y `S24-cierre` («Tomas dobló la huella detrás del certificado.» … «cerró el broche.») íntegros) · **M10 CH-6 → PAGADO** |
| 2 | **OT-26** | A | Ripples de N4/N6, ambos aceptados. Y el M4b, que es el trabajo real | **A5 fuerte** (la caja de «Dentro quedaban dos bolsas y la caja que llenaron cuando la casa de Tromsøya empezó a parecerles demasiado observada.» = la de N4; medios del instituto retirados frente a AK-7 accesible el 7/20/21-ene; el asunto de «—Mañana tengo descarga y después una reunión del kystbrukslag…» = el que N6 cobra, **sin anticipar el resultado**) · **A8** (**M4b 16,8 % → ≤ 8 %**, ≥ 9 recompuestas; M1 no sube; M2 = 0; sin cierre-objeto nuevo) · **A7 nota, sobre el diff** — corrige mi plan, que decía «no aplica»: vigila **Carta 3** (los hechos que hicieron inhabitable la casa quedan como hechos; **prohibido encadenar del acoso hacia lo que le pasó a Jean**) y que **`S26-paso-uso` no se glose** |
| 3 | **OT-31** | B | Independiente. Es la respuesta estructural al «clímax concedido» | **A5** (canon B3 §16 custodia «ante manifestación pública verificable» y §17 llave/repetidor/vinculación; `33:221–223` y `35:207` coherentes; **Jean no conoce N4**) · **A8** (M1 ≤ 23,3 y **0 términos nuevos**; **M2 = 0**; tramo ≤ 100; diálogo 48–58 %) · **A7 sobre el diff, obligatorio** — **P-48**: ninguna voz presenta el final de la continuidad de Jean como descanso, alivio o preferible; `S31-elegir` sin glosa, sin contestar otra vez, sin matizar y sin réplica nueva contigua · **M6b** (réplicas nuevas de cuatro voces: es la mejor muestra de la oleada) |
| 4 | **OT-32** | B | Depende de N4 (aceptado). Cierra CH-1 con N4 | **A5** (los tres avisos y sus rastros tal como los fija `cap-n4.md`; «—La familia queda fuera del alcance contractual…», «PODEMOS IMPEDIR EL ACCESO SIN DAÑO FÍSICO.», «LA DISTINCIÓN ENTRE DAÑO Y CONTINUIDAD DEPENDE DE QUIÉN DEFINE LA SEGUNDA.» y «Mats recordó a Gunnar Rydberg y los once segundos por los que no había preguntado.» verbatim; «casi seiscientas»/597; nada de NORNA) · **A8** (M1 no sube, 0 términos nuevos; M2 = 0; **M4b ≤ 8 % con 0 antepuestas nuevas**; tramo ≤ 339) · **A7 sobre el diff, obligatorio** (ningún paralelo, **ni enunciado ni por montaje**, entre la ELA y la muerte de Jean; `HIJO` y `S32-voz` intactos) · **M10 CH-1 → PAGADO (N4 + 32)** |
| 5 | **OT-34** | C | Después de 24 (no repite su pasado; puede citar un objeto) | **A5 el más fuerte de la oleada** (las diecisiete horas del clímax; `4.096 − 2.911 = 1.185` intacto y **prohibido «la consolidación borró 1.185»**; `2.401,6 AÑOS-JM`; cobertura «hasta 12:47» sin alargar; «Un fotógrafo avanzó de espaldas por el pasillo… Astrid no movió la carpeta.» verbatim) · **A8** (M1; M2 = 0; tramo ≤ 374; M4 = 0, ya conseguido) · **A7 nota** + **verificación P-43 sobre el diff completo de la oleada: las nueve instancias conocidas, ninguna más** |
| 6 | **OT-35** | C | Después de 24 y 34: I-4 necesita 16 y 24 finales, e I-1 no puede heredar interior de Tomas | **A7 sobre el diff, obligatorio** (Ap. F P7 / Carta 7: la caída es coste de una acción de la madre, no proeza; **párrafo propio PROHIBIDO**, §10.5 n.º 11; sin adverbio de manera, sin «aikido», sin herida; Jessie sin herida; nada nuevo del naust) · **A5** (12:38/12:41/12:42/12:43/12:46:01/«Cuarenta segundos»/12:46:50; **AF-1 sin alargar**; decisión sobre «Jessie recordó sus preguntas en la comisaría y las dos horas bajo luces blancas…» anotada en B2 §9.5) · **A8** (M1; M2 = 0; tramo ≤ 228) · **M10 CH-4 → PAGADO** |
| 7 | **OT-40** | C | Último. El dictamen previo ya está: posición (b), literal congelado | **A7 OBLIGATORIO sobre el diff** (las ocho condiciones de P-44; **una línea modificada y cero líneas añadidas**, o se revierte; ningún interior de Jessie; prensa sin causa ni método; «Despedida» sin abrir; **P-47**: nada entra entre «Nadie le pidió un resumen.» y `S40-despedida`) · **A5** («Aslak estaba con la asociación en la segunda sesión de la consulta» verbatim; el reorden de I-4 no toca fechas ni baja del segundo dinkus) · **A8** (M4 del capítulo 2 → 1; M4b ≤ 8 %; diálogo 7–11 %) · **M10 CH-2 → PAGADO** |

### 8.3 · Después de los siete

| # | qué | quién |
|---|---|---|
| 8 | Pasada de línea (lista negra B6b; molde «X tenía Y»; acotaciones) | **A4** |
| 9 | Continuidad global de la oleada + cruce `OT-37` §5 (la sala de 34 ↔ 37) | **A5** |
| 10 | **Auditoría adversarial** sobre los tres capítulos con más prosa nueva: **24, 31, 32** (`auditor-adverso.sh`, `gpt-5.6-sol`). No es gate: A0 decide qué se borra | A0 |
| 11 | A4 repara lo que A0 acepte de la auditoría | A4 |
| 12 | A8: `medir.sh w5 --baseline v0`, `proteger.sh verificar`, `validar-frontmatter.sh`, `m4b_antepuestas.py`, `sensibilidad.sh --solo` en los siete, compilado `w5`. **Más cuatro censos por `grep` sobre el diff completo:** P-44 (`cintur[óo]n` = 4) · P-43 (las nueve de Astrid) · P-46 (el molde «no preguntó por + SN» = 4) · P-41 (Kongsbakken↔Jean = 0 coocurrencias, censo en 6) | A8 |
| 13 | **Sondas de aislamiento (`claude` y `codex`) antes de puntuar. Fallan cerradas** | A0 |
| 14 | Hito: **A6 ×3 en frío + control de deriva sobre v0 el mismo día** + M6b con ancla | A0 |
| 15 | Gate de W5 al autor | A0 |

**Coste estimado del hito 14:** ≈ 8,8 USD (A6-1/A6-2 en `claude-opus-5`, A6-3 en `gpt-5.6-sol` sin coste por token, control de deriva, M6b).

---

## 9. Guardarraíles de ritmo (la regla que W4 se saltó en el 37 y el 38)

**Ningún bloque narrativo continuo puede superar el tramo máximo actual de su capítulo.** Es la guarda que `OT-24` §1 ya tenía y que A0 debe hacer explícita al lanzar la oleada:

| cap. | tramo máx. hoy | **límite en vF** | diálogo hoy | **diálogo en vF** |
|---|---:|---:|---:|---|
| 24 | 197 | **≤ 197** | 22,7 % | ≥ 20,0 % (baja por diseño: el pasado de Tomas es narración; **no se fuerza réplica**) |
| 26 | 190 | **≤ 200** | 29,9 % | **≥ 30,5 %** (I-2 e I-3 son réplica) |
| 31 | 72 | **≤ 100** | 51,1 % | **48–58 %** |
| 32 | 339 | **≤ 339** | 18,8 % | ≥ 16,5 % |
| 34 | 374 | **≤ 374** | 15,5 % | ≥ 14,5 % (criterio de 15,5 % retirado, §6.2) |
| 35 | 228 | **≤ 228** | 12,4 % | 11–15 % |
| 40 | 272 | **≤ 272** | 8,6 % | **7–11 %, no se sube** |

**Réplicas perdidas en toda la oleada: 0.** Regla dura.

---

## 10. Restricciones duras, capítulo a capítulo

### 10.1 · P-41 (Kongsbakken ↔ Jean)

Afecta a `cap-40` y a `cap-32` por vecindad de tema. **Ninguna intervención de W5 toca las seis menciones del censo** (`3:143`, `9:73`, `18:149`, `n4:79`, `n4:91`, `40:167`) ni se acerca a ellas:

- `40:167` («En marzo, Nora entregó el teléfono apagado en Kongsbakken y entró con el teclado») es el pago del marzo de N4 y **es administrativo y administrativo se queda**. Glosar la llegada sería VETO.
- La cancelación de R3 en el 40 **elimina el único riesgo real de P-41 de toda la oleada**: un beat de ensayo/repesca en la elipsis de febrero pasaba a treinta líneas de `:167` y habría tentado a que alguien cobrase la inscripción emocionalmente.
- **Verificación obligatoria (A8, `grep`):** censo en **cinco** loci —`9:73`, `18:149`, `n4:79`, `n4:91`, `40:167`; `3:143` NO contiene el término—, **0 coocurrencias NUEVAS** Kongsbakken↔Jean en capítulos, borradores, hojas de intervención y prompts. Nadie —tampoco Nora en interioridad— recuerda la discusión donde Kongsbakken aparece.

### 10.2 · P-42 (el cuarto ítem de `22:203`)

`cap-22` no está en W5, pero la prohibición alcanza a **todo material del proyecto**. Este plan **no especifica el cuarto ítem**, no se refiere a «la cuarta» ni a «lo que no dijo», y **ninguna intervención de W5 puede recoger, recordar, completar, corregir ni cobrar ese beat**. Se anota expresamente en el handoff de A3b y en el checklist de A5.

### 10.3 · P-43 (rasgo de abstención de Astrid: censo en **nueve**)

**Corrección de A7 a este plan, y a mí me corrige dos veces.**

1. **`34:253` no es «—También cualquier omisión.»**, como decía la v1 en §2 y §6.1: `34:253` es **«Un fotógrafo avanzó de espaldas por el pasillo. El cartón gris quedó visible en la imagen oficial. Astrid no movió la carpeta.»**, y la réplica está en `34:249`. Las dos caen en la misma escena, así que la conclusión no cambia; pero **A5 y A8 verifican por cita y una cita mal puesta en el plan se propaga**. Corregida antes de que la heredaran.
2. **El censo de siete omitía dos instancias de v0**, las dos en `cap-23`, que es protección total: «Astrid dejó de escribir.» (`23:193`) y «Astrid guardó silencio.» (`23:261`). **El rasgo está en nueve.**

Censo completo: `18:157` · `22:147` · `22:203` · **`23:193`** · **`23:261`** · `29:147` · `34:249`+`34:253` · `39:181` · `n4:423`.

**P-43 no cambia de efecto —cero instancias nuevas— y gana margen de razón.** Astrid no aparece en ninguna otra intervención de W5.

**Verificación (A5 y A8, sobre el diff completo de la oleada, no solo del 34):**

```
grep -n "Astrid no \|Astrid dejó de\|Astrid guardó silencio" capitulos/
```

debe devolver **exactamente** las nueve conocidas.

### 10.4 · Techo de retenciones · **P-45**, **P-46**, y la corrección de mi argumento

**G-W5-1 lo gané, pero no con mi argumento, y conviene que quede escrito.** A7 desmonta las dos mitades de lo que yo alegué en la v1:

- **«Es el pago de una línea dicha en un fichero de protección total» no exime de nada.** Si «paga un plantado» bastara para salir del techo, el techo estaría vacío: en este proyecto **toda** retención se justifica como pago de algo. El techo cuenta **efectos sobre el lector**, no orígenes.
- **Mi caracterización del censo era falsa.** Dije que recogía «gestos de adulto que declinan una potestad»; de las cuatro registradas, la n.º 2 tiene por sujeto a **una menor** eligiendo entre sus propias preguntas y en `39:181` quien retiene es **Maja**. Y si el censo fuese eso, v0 lo rebasaría solo: `6:23`, `6:247`, `11:155`, `14:33`, `23:23`, `23:261`, `23:309`, `26:19`, `31:47`, `40:81`, `41:107`.

#### El criterio bueno: el test de las dos clases

Es el criterio con el que se juzgará todo lo que venga —W5, W6, W7 y toda reserva—, así que va aquí completo y no por referencia:

> **Clase R · RETENCIÓN.** La narración **posee** un ítem singular y **declina entregarlo**, y la no entrega **es** el beat. Tres condiciones, **todas necesarias**:
> 1. el texto establece que existe un ítem **específico y singular** (un título, una tercera línea, un cuarto ítem, una pregunta escrita, un segundo regalo);
> 2. señala su no entrega **como acontecimiento** (alguien declina, o la cuenta se queda corta);
> 3. el lector puede **nombrar lo que falta** sin poder nombrar su contenido.
>
> **Clase A · ABSTENCIÓN.** Un personaje declina ejercer una potestad, y **al lector no se le retiene nada que la narración tenga**: o conoce ya el contenido, o no hay contenido que conocer. Es la gramática básica del libro y su modelo de adulto.

**El caso que lo prueba es de v0 y de protección total**, `9:181`: «Nora estuvo a punto de lanzarle como pruebas las tardes en aquel parque y las veces que Jean había dejado ganar a Jessie cuando practicaban inmovilizaciones. **Se contuvo.**» El lector tiene el contenido íntegro y el acto no se ejecuta; nadie lo ha contado nunca como retención. Y está en el mismo hilo de aikido que `OT-35` I-1 va a pagar.

#### Aplicación a «No preguntó por el cinturón.»

| | ítem | ¿la narración lo posee? | ¿el lector puede nombrar su contenido? | clase |
|---|---|:-:|:-:|:-:|
| 1 | `22:147`, el título | sí | no | **R** |
| 2 | `23`, la tercera pregunta preparada | sí | no | **R** |
| 3 | `39:181`, la tercera línea | sí | no | **R** |
| 4 | `22:203`, el cuarto ítem | sí | no | **R** |
| — | **la línea del cinturón** | **no: nadie llegó a pedirla nunca** | **sí: `23:313`, verbatim, cierre de capítulo** | **A** |

La pregunta se entregó al lector íntegra diecisiete capítulos antes. Lo que queda sin saberse —qué sabe Jean del cinturón— **no lo retiene esta línea: no existe en el mundo del libro porque nadie llegó a preguntarlo**. La narración no calla nada; el mundo carece. Y esa es también su garantía: la ambigüedad de B4 §2.1 queda **cerrada por imposibilidad**, no administrada por nosotros. Lo que sí hace la línea es invertir el molde: donde `22:147`, `n1:131` y `n2:191` ponen a un adulto con potestad que no presiona a una menor, aquí el sujeto es **la menor y lo que declina es su propio encargo**.

#### El censo corregido, y por qué endurece el techo

A7 corrige contra sí mismo: el censo de cuatro de `OT-22b` §4.3 **estaba incompleto**. (Los locus que siguen son **de registro, no de instrucción**: se verifican por la cita, no por el número.) Clase R en v0: `6:247` («La lista no empezaba allí. Maja no la desplegó.»), `22:147`, la escena del canal de `23`, `23:171` («—Dejo el hueco.»), `39:179-181`, `40:19`+`40:117`. Nuestra: `22:203`.

**La consecuencia es la contraria a la que una lectura interesada querría sacar.** El techo nunca fue un censo del libro: era **un presupuesto sobre nuestras adiciones**, y está **agotado**. La densidad de v0 no nos autoriza a más; nos obliga a menos, porque el lector ya ha gastado su tolerancia leyendo al autor.

> **P-45 · redacción vigente del techo (sustituye a `OT-22b` §4.3 sin ampliarlo).**
> **Clase R:** presupuesto **agotado**. Cero instancias nuevas en W5, W6, W7 y en cualquier reserva, en capítulos nuevos y por inserción en capítulos de v0. Las cuatro administradas (`22:147`, `23`, `39:181`, `22:203`) no se tocan, no se glosan y no se cobran. Si dos comparten registro, la nueva se revierte aunque la otra sea anterior.
> **Clase A:** sin techo global —es la gramática del libro—, gobernada por dos vías: **por personaje** (P-43 para Astrid) y **por capítulo**. **`cap-40` queda cerrado** tras la línea del cinturón: sus instancias son el diseño del capítulo del silencio y no admiten una más en ninguna oleada.

> **P-46 · molde.** «no preguntó **por** + sintagma nominal» queda **cerrado en cuatro** tras el 40: `22:147`, `n1:131`, `n2:191` y la línea nueva. Ninguna instancia nueva, **y A4 no puede producir una en la pasada de línea**.

#### Y el resultado que reordena la §6

**Quien incumplía el techo era `OT-40` I-2, no I-1.** «El precio de no preguntar lo que escribió» es clase R pura sobre un ítem —la hoja doblada— que v0 **ya** retiene y **ya** cobra: habría sido un tercer beat sobre la misma retención y la quinta de la clase. La cancelé por la vía correcta y **queda cancelada con carácter permanente, en cualquier forma y bajo cualquier nombre.**

#### Qué habría convertido la línea del cinturón en la quinta

Para que la regla sea enseñable y A3b pueda autoevaluarse: que el texto diga que Jessie **preparó** la pregunta y no la hizo; que diga cuántas cosas quería preguntar y enumere menos; que la línea se apoye en algo **escrito** por ella; que alguien registre la ausencia («la transcripción no recogía…»); que se nombre lo que **sí** preguntó en su lugar. **Nada de eso puede aparecer en el borrador.**

### 10.5 · Enmienda final a G-3 · las **trece** declaraciones de paragrafado, por cita literal

> El paragrafado es énfasis. **Vaciar, partir, fundir, reordenar o insertar al lado** de una línea protegida cuenta como modificarla. **51 de los 109 spans son de anclaje único** y M9 es ciego a todo su entorno.

**Corrección bloqueante de A7, y es una ironía que anoto porque es instructiva.** La tabla de la v1 estaba escrita en **tres sistemas de numeración incompatibles** —`OT-26` en numeración de fichero; `OT-24/31/32/34/35` en numeración de cuerpo (fichero − 12); las OT de F2 en la de v0— y a veces **dos en la misma fila**. En la fila de `OT-31` I-1, «entre `:117` y `:119`» leído en numeración de fichero coloca las réplicas **dentro del intercambio de Jessie**, no antes de `UMBRAL 2 · TRANSPORTE PÚBLICO`, que es lo que la propia declaración exigía tres palabras después. **Lo que salvaba esa fila era la cita literal — es decir, la regla de anclaje que yo mismo estampo como vinculante en la cabecera de este plan y que no apliqué aquí.** Y eran **trece**, no doce: A7 y yo contamos mal el mismo número.

**El problema es endémico y conviene decirlo, porque si no cada revisión lo hereda del anterior.** No es solo mío: el propio dictamen de A7 cita el `cap-40` en numeración de cuerpo para la hoja doblada y en numeración de fichero para el censo de clase A, dentro del mismo informe. Con cuatro numeraciones en circulación —v0, cuerpo, fichero y compilado— **el único identificador que no se degrada es la frase**. Regla para W5, W6 y W7: **los números de línea valen para localizar; solo la cita literal vale para instruir y para verificar.**

**Reexpresadas las trece por cita textual literal y sin un solo número de línea.** Cada una nombra: (i) la frase que precede, (ii) la frase que sigue, (iii) qué párrafos se parten, funden, vacían o reordenan, (iv) el span más próximo y si cambia de vecino. **Sin esto A7 devuelve el borrador sin leerlo y A4 no ejecuta.**

---

**1 · `OT-24` I-1 — el pasado de Tomas**

- **Precede:** «Al sacar la credencial del lector, rozó con el pulgar los bordes de otros plásticos dentro de la cartera.»
- **Sustituye:** «La devolvió a la cartera.» — este párrafo **desaparece** y en su lugar va el recuerdo, que termina en un gesto con dato de carácter.
- **Sigue:** el dinkus, que **no se mueve**.
- **Se parte / funde / vacía / reordena:** nada. El párrafo anterior queda íntegro; el nuevo ocupa exactamente el sitio del sustituido.
- **Span más próximo:** `S24-cierre` («Tomas dobló la huella detrás del certificado.» … «lo deslizó entre los carnés caducados y cerró el broche.»), en la escena siguiente. **No cambia de vecino.** `S24-once` («Once segundos en blanco en la percepción.», **anclaje único**) queda a más de setenta líneas.

**2 · `OT-24` I-2 — la copia sellada · redacción de A7, sustituye a la mía**

La declaración de la v1 era **autocontradictoria**: decía a la vez que la inserción entra entre los dos párrafos y que la réplica conserva «su vecino por arriba». Redacción que A7 autoriza:

- **Precede:** «Tomas miró la copia sellada. Kronfjord Kapital estaba en el consejo y Gunnar había activado alarmas internas antes de morir, pero el formulario no ampliaba el perímetro.»
- **Sigue:** «—He preservado la cadena a mi nombre. Conservaré el expediente de contratación del fondo y después consultaré su alcance.»
- **Forma:** la inserción entra como **párrafo nuevo completo** entre los dos. **Ninguno de los dos se parte, se funde ni se vacía.**
- **Único vecino que cambia en todo el libro:** el de arriba de la réplica de Tomas, que **no pertenece a ningún span**.
- **Span más próximo:** `S24-once` (**anclaje único**), a más de setenta líneas; no cambia de entorno.

**3 · `OT-26` I-1 — el motivo de la mudanza**

- **Precede, en el mismo párrafo:** «… Dentro quedaban dos bolsas y la caja que llenaron cuando la casa de Tromsøya empezó a parecerles demasiado observada.»
- **Opera sobre:** «El seguimiento y la retención bastaban.», última oración de ese párrafo, que puede recomponerse **conservando «seguimiento» y «retención»**.
- **Forma:** todo ocurre **dentro del párrafo existente**, que sigue siendo uno. La frase recompuesta **no puede quedar sola entre dos blancos**.
- **Sigue:** «En la entrada de la casa baja, Aslak esperó inmóvil hasta que Maja abrió el maletero.» — intacto.
- **Span más próximo:** ninguno cerca.

**4 · `OT-26` I-2 — el resumen de Maja a Aslak**

- **Precede:** «—Un coche siguió a Jessie por tres lugares. Grabó la matrícula y lo encaró. La policía la retuvo dos horas.»
- **Sigue:** «—No sabemos quiénes son.» — **conserva su párrafo propio y sigue cerrando el intercambio.**
- **Forma:** una réplica más de Maja, párrafo propio, entre las dos. Nada se parte ni se funde.
- **Span más próximo:** `S26-lata` («Después de dejar el cabo, Aslak abrió el armario bajo el fregadero,» …), que **empieza dos párrafos después** y no cambia de vecino por arriba.

**5 · `OT-26` I-3 — la reunión gana asunto**

- **Opera dentro de:** «—Mañana tengo descarga y después una reunión del kystbrukslag. No voy a dejar ninguna de las dos por vuestros relojes.»
- **Forma:** **≤ 15 palabras DENTRO de esa réplica**, que sigue siendo **un solo párrafo**. «No voy a dejar ninguna de las dos por vuestros relojes» se conserva.
- **Precede:** «—Quiero que nos dejes quedarnos —dijo—. …» · **Sigue:** «—Dormís aquí —dijo Aslak—. Mañana sacamos la barca si el hielo deja libre el amarre.» — los dos intactos.
- **Spans más próximos:** `S26-paso-uso` (**anclaje único**) y `S26-asociacion` (**anclaje único**) quedan por encima; `S26-bocana` («—La bocana de Sørkoppen queda reservada por operaciones para el veintiuno de enero.», **anclaje único**) queda al final del capítulo. **Nada nuevo entra entre «Nora cerró el cuaderno. Aslak guardó la carpeta en la lata…» y `S26-bocana`**: ninguno de los tres cambia de vecino.

**6 · `OT-26` I-5 — M4b, diez antepuestas recompuestas**

- **Forma:** se reordena **dentro de la frase** (sujeto delante, circunstancia detrás). **Prohibido** partir, fundir, vaciar o reordenar párrafos, y prohibido tocar contenido u objetos.
- **Ninguna de las nueve está dentro de un span.** La antepuesta que abre `S26-lata` («Después de dejar el cabo, Aslak abrió el armario…») **no se toca**.
- **A4 declara las nueve, una a una, sobre el diff.** Es la intervención con más superficie de contacto de la oleada aunque cueste cero palabras.

**7 · `OT-31` I-1 — el plan B** *(la fila que la numeración estropeaba)*

- **Precede:** «—El repetidor solo llevaría el audio educativo al homenaje —dijo Alana—. Si no lo alcanza, se termina. No abre producción ni controles.»
- **Sigue:** «`UMBRAL 2 · TRANSPORTE PÚBLICO`» — línea de registro que **conserva su forma y su posición**.
- **Forma:** las réplicas nuevas entran como **párrafos propios** entre esas dos. **Nada se inserta dentro del intercambio anterior** («—Buscaremos a otra persona.» y lo que lo precede quedan intactos).
- **Spans:** `S31-elegir` («—¿Quieres vivir?» … «—Quiero poder elegir. Es la primera vez.») y `S31-sacar` («Nora tachó `SACAR A JEAN`…», **anclaje único**) quedan muy por encima; `S31-cancion` («—Si algo sale mal, que Nora termine la canción igual.», **anclaje único**) muy por debajo. **Ninguno cambia de vecino, y las réplicas nuevas no pueden quedar contiguas a `S31-elegir`** (P-48).

**8 · `OT-32` I-1 — la interferencia fallida**

- **Precede:** «—Esa diferencia no cambia vuestra oferta. —Mats volvió a abrir la franja verde—. Afecta al coste, quería decir. …»
- **Sigue:** «CONTENEREMOS TAMBIÉN LAS INTERFERENCIAS EXTERIORES. LA FAMILIA INSISTE. PUEDE SER RESUELTA.»
- **Posición fijada y alternativa PROHIBIDA:** insertar después de la línea de Coro dejaría la inserción a un párrafo de «—La familia queda fuera del alcance contractual…» y a dos de `S32-amenaza` («PODEMOS IMPEDIR EL ACCESO SIN DAÑO FÍSICO.», **anclaje único**).
- **Forma:** párrafo nuevo completo entre las dos citadas; ninguna se parte ni se funde. `S32-amenaza` **no cambia de vecino**.

**9 · `OT-32` I-2 — la cala de Mats**

- **Precede:** «Desde el resguardo del banco de voz, Mats movió el paquete al directorio privado de SYNVEV-2, fuera de `Consolidación L-Serie`, sin cambiar la etiqueta clínica. …»
- **Sigue:** «La interfaz solo mostraba el material registrado y el usuario previsto. No aparecía una ejecución ni otro resultado.»
- **Prohibido:** colocarla en el último párrafo antes de `S32-cierre` («Aceptamos. Nosotras siempre cumplimos nuestras condiciones.», **anclaje único**). Las tres líneas de registro (`RETENCIÓN · ÍNTEGRA`, `ALCANCE · MUESTRAS / INTENTOS / VARIACIONES`, `CONSOLIDACIÓN · EXCLUIDA`), «En la columna contigua, `Consolidación L-Serie` mantenía el criterio “Las necesarias”…» y «Firmó desde el terminal seguro del estudio…» **conservan párrafo y orden**. `S32-voz` no se toca.

**10 · `OT-34` I-1 — la cala de Tomas**

- **Precede:** «La interfaz advirtió de que validar cualquier petición de mantenimiento durante esa cobertura asociaría su identidad, la incidencia, la hora y la puerta. Después ya no podría figurar como observador neutral de aquel acceso.»
- **Sigue:** «Tomas confirmó el registro sin informar a nadie fuera de su cadena de seguridad. No conocía la llave de Gunnar ni el repetidor, y tampoco la maniobra de Jessie.»
- **Forma:** párrafo nuevo completo entre las dos. **«Esperó.» sigue solo en su párrafo y sigue cerrando la escena**, dos párrafos por debajo.
- **Span más próximo:** `S34-cierre` («El contador de la demostración marcó 12:46:50.» …), en otra escena; no cambia de vecino.

**11 · `OT-35` I-1 — la caída · redacción de A7, y el motivo es sensibilidad, no forma**

**La opción de párrafo propio queda PROHIBIDA.** No es una preferencia formal: un párrafo propio es énfasis, y aquí el énfasis recaería sobre **la destreza de una menor de dieciséis años en el clímax de una acción arriesgada** — «conducta imitable de riesgo presentada como eficaz», Carta 7 y Ap. F P7.

- **Forma única autorizada:** la línea **se une al párrafo** «Aslak metió atrás. Maja agarró a Jessie por la parte posterior de la parka y la llevó al fondo de la barca. El rellano empezó a separarse. La puerta permaneció cerrada y el indicador interior de salida, verde.» Dentro de ese párrafo, la caída es **lo que le pasa a un cuerpo del que tiran**.
- **Sigue, intacto y como párrafo tampón:** «La consola exterior cambió de estado una vez más.»
- **Span:** `S35-cierre` («`SALIDA EDUCATIVA → MEZCLA PÚBLICA · ENLACE DISPONIBLE`» / «12:46:50.») conserva su tampón por arriba y **no cambia de vecino**. La línea **no queda inmediatamente antes del span** ni cierra escena.
- **Condiciones de forma que A3b escribe en su hoja:** sin «aikido» como glosa; sin «como le habían enseñado» ni referencia a las clases o a Jean; **sin adverbio de manera**; sin herida y **sin proeza**; nadie lo comenta.

**12 · `OT-40` I-1 — el cinturón · redacción de A7, sustituye a la mía y deroga «va sola» de `OT-40` §8**

**Posición (a) VETADA** —tras «—Vuelvo el jueves.» y antes del dinkus—: `S40-locutorio` **termina** en esa réplica, e insertar al lado cuenta como modificarla; y le quitaría a las tres palabras que son el arco entero de Jessie el sitio de mayor énfasis del capítulo.

**Posición (b), ejecutada así y no de otra manera.** El párrafo queda:

> «El jueves, Jessie utilizó la misma tarjeta. **No preguntó por el cinturón.** Nora tenía una clase y Maja no movió el horario de ninguna de las dos. En la cena, la tarjeta quedó junto al frutero hasta que Jessie la guardó en la mochila. Nadie le pidió un resumen.»

**Segunda oración del párrafo.** Ni la primera, ni la última, ni contigua a «Nadie le pidió un resumen.», ni en párrafo propio. Tres razones: el sujeto elidido queda inequívoco; **no clasifica el hueco protegido** (se refiere a un jueves que no se narra y deja el turno del lunes, bajo span, exactamente como estaba); y el remate del párrafo sigue en el hecho administrativo, que además blinda la línea.

- **Se parte / funde / vacía / reordena:** nada. `S40-locutorio` **no cambia de vecino por abajo**: el dinkus sigue inmediatamente después de «—Vuelvo el jueves.».
- **Forma del diff, verificable:** en estos ficheros cada párrafo es una línea. La ejecución correcta produce **una línea modificada y cero líneas añadidas** en `capitulos/cap-40.md`, +5 palabras. **Si el diff muestra líneas añadidas, se ha ejecutado la (a) o se ha creado párrafo propio: revertir sin discusión.**
- **Ocho condiciones de ejecución** en §10.4 y en la ficha P-44 de §10.8: literal congelado de cinco palabras; nadie la comenta; no cierra nada; cero interior de Jessie; qué sabe Jean del cinturón no se explica jamás; no vuelve; censo de `cintur[óo]n` de tres a **cuatro**, ninguna quinta; M10 CH-2 → PAGADO.

**13 · `OT-40` I-4 — el reorden del cierre del naust (0 palabras, ejecuta A4)**

- **Permutan dos párrafos completos:** «Nora elevó la tabla. Aslak la encajó antes de pasar a la segunda. Las piezas nuevas quedaron demasiado claras junto a las antiguas. Maja efectuó el pago allí mismo.» y «Desde el embarcadero se distinguía la carcasa del sensor judicial bajo el alero del naust. La lente encuadraba un fragmento del muelle y el cable desaparecía en el transmisor precintado.»
- **Resultado:** el segundo pasa delante y la escena cierra en «Maja efectuó el pago allí mismo.» — un acto, no un objeto. M4 del capítulo 2 → 1.
- **Se parte / funde / vacía:** nada; ninguna línea queda aislada de nuevo; el dinkus no se mueve.
- **Precede al bloque, intacto:** «—Vemos el daño y recalculo.» **Spans:** `S40-despedida` (**anclaje único**) queda por encima y `S40-cierre` muy por debajo; ninguno cambia de entorno. **El reorden se detiene antes del segundo dinkus**, de modo que P-34 (salvaguardas del sensor) queda fuera de alcance.

### 10.6 · P-34, P-35, P-36, P-38

- **P-34:** las salvaguardas del sensor —«en una sola dirección», «hasta la entrada exterior de NIDHOGG», la autorización posterior del tribunal y «dejó constancia de que la primera entrega seguía pendiente»— **no se comprimen más**. Están en el último tramo del `cap-40`, que W5 **no toca**: el reorden de I-4 se detiene en el párrafo del sensor del naust y **no baja del segundo dinkus**. **Verificado por A7 sobre el texto de hoy.**
- **P-35, P-36:** `cap-n3` **no entra en W5**, ni para podar ni para añadir. La espina A–F, «El resto era ir.», el 31 subrayado y el hervidor disparan el gate de A7. Sobre el hallazgo de que mi poda agrandó la cena: **no se corrige en W5** —la Parte III no tiene sitio y P-36 cierra el capítulo—; se mide en el hito y se decide en W6, con una lectura más, no con una.
- **P-38:** las cuatro réplicas de `n4:271–277` son la única enunciación viva del coste de Jessie. `cap-n4` no se toca en W5.

### 10.7 · Ambigüedades del Ap. A §3

Ninguna intervención de W5 las resuelve ni las roza: el **ordenante** del sabotaje (`24:79` verbatim; el resumen de `OT-32` I-1 **no tiene autor** y la atribución la hace el lector, no Mats); **qué sabe Cuchillo** (`13:201`); la **consciencia residual**; la denuncia anónima; **«No toda» como techo**. La villanía sigue siendo sistémica: en `cap-32`, si Mats piensa «Coro lo hizo», la inserción se revierte.

---

### 10.8 · Prohibiciones nuevas emitidas por A7 sobre este plan (P-44 … P-49)

Vinculantes hacia adelante. Van aquí completas porque A3b, A4, A5 y A8 trabajan con este documento.

| # | Alcance | Prohibición |
|---|---|---|
| **P-44** | todo el proyecto | **El cinturón (CH-2).** Censo cerrado en **cuatro**: `4:27`, `9:199`, `23:313` y la línea nueva del 40. **Literal congelado**, cinco palabras, sin variante, sin inciso, sin adverbio, sin «tampoco», sin «esta vez», sin «qué sabía». Nadie la comenta. No vuelve (régimen P-42). **Qué sabe Jean del cinturón no se explica jamás.** Ningún material nuevo aplica al cinturón verbo de manipulación alguno, ni lo pone en la misma frase, párrafo o escena que el acto, el 26 de noviembre, el trayecto, Koppangen o el naust. |
| **P-45** | W5–W7 y toda reserva | **Techo de retenciones** en la redacción de §10.4: clase R con presupuesto **agotado** (cero instancias nuevas); clase A gobernada por personaje y por capítulo; **`cap-40` cerrado** a instancias nuevas de clase A tras la línea del cinturón. |
| **P-46** | todos los capítulos, **incluida la pasada de línea de A4** | El molde **«no preguntó por + SN»** queda cerrado en cuatro (`22:147`, `n1:131`, `n2:191`, la línea del 40). Ninguna instancia nueva. |
| **P-47** | `cap-40` | El tramo entre **«Nadie le pidió un resumen.»** y **`S40-despedida`** queda **cerrado a toda inserción**, en cualquier oleada y en cualquier activación de reserva (§7.1). |
| **P-48** | `cap-31` y toda OT futura con Jean en escena | **Ninguna voz** —narrador, Maja, Alana, Jessie, Nora ni Jean— presenta el final de la continuidad de Jean como **descanso, alivio, paz, silencio merecido, «se acaba y ya está» o resultado preferible**. Jean puede decir qué pierde, qué mide y qué no controla. `S31-elegir` no se glosa, no se contesta otra vez, no se matiza y no cambia de vecino. Nora pregunta y anota; no dirige. |
| **P-49** | `cap-n4` y todo material | **`n4:211`** («La responsable escribió algo corto y no lo leyó en voz alta.») es **opacidad, no retención**: nadie especifica, recuerda, completa ni cobra jamás su contenido. Si algo lo hace, se convierte en la quinta retención y se revierte. |

### 10.9 · Vigilancias de contenido de A7 sobre las intervenciones que se ejecutan

Van a la hoja de A3b, capítulo por capítulo.

- **`OT-24` I-1 · el pasado de Tomas no puede ser el caso de 2054 con otro auditor.** `22:173-175` ya cuenta —**dos capítulos antes en orden de lectura**— la historia de quien siguió el procedimiento, la institución quedó cubierta y la persona no. Si el pasado de Tomas repite esa forma, el lector oye el mecanismo. **Debe diferir en al menos dos de estos tres:** qué preservó el profesional, qué perdió la persona, qué objeto queda. (El objeto ya difiere: Astrid conserva una carpeta con el número en el lomo; Tomas, un carné caducado.) **Prohibida la cadencia «no volvió a escribir» / «archivó el caso».** Y: **la persona del caso anterior no muere después, ni se le pierde el rastro, ni «nadie volvió a saber de ella»** — un final abierto sobre alguien a quien el procedimiento dejó fuera, en este libro, se lee como lo que la Carta no permite insinuar.
- **`OT-26` I-1 / I-2 · Carta 3.** Los hechos que hicieron inhabitable la casa son posteriores a la muerte de Jean y **deben quedar como hechos**. Prohibido cualquier encadenamiento —de narrador o de personaje con autoridad— que vuelva del acoso a la casa hacia lo que le pasó a Jean. **`S26-paso-uso` no se glosa** («A nosotros nos quitaron paso y uso. A Jean le hicieron otra cosa.»): es la línea que el libro tiene para impedir esa ecuación, y es de anclaje único.
- **`OT-31` I-1 · P-48**, arriba. Es la única intervención de W5 donde la Carta 4 puede morder de verdad: seis réplicas sobre qué se pierde si el plan falla, en una mesa donde una de las voces es la continuidad de una mujer muerta.
- **`OT-32` I-2 · ningún paralelo, ni enunciado ni sugerido por montaje, entre la enfermedad de Mats y la muerte de Jean.** Nada que permita leer «él también sabe lo que es desaparecer»: sería una equivalencia moral entre una enfermedad y un suicidio y arrastraría el registro de la pérdida hacia el de la liberación. La ELA no explica ni atenúa nada de lo que firma. `S32-voz` no se toca.
- **`OT-34` I-1 y `OT-40` I-4:** sin observaciones de A7.
- **Aviso de tono de A7 sobre toda la oleada:** «la biografía de Tomas es la primera vez que W5 escribe **pasado** de un personaje, y el pasado es donde este libro podría empezar a explicarse. **Ciento veinte palabras de hechos y un gesto; ni una de porqué.**»

---

## 11. Gates · estado

### 11.1 · Los tres de A7: **RESUELTOS** (`informes/a7-w5.md`)

| # | decisión | dictamen |
|---|---|---|
| **G-W5-1** | `OT-40` I-1 frente al techo de retenciones, y posición | **NO es la quinta.** Es **clase A** (abstención), no clase R, por el test de §10.4, y el precedente que lo prueba es de v0 y de protección total (`9:181`). **Se ejecuta**, literal congelado, **posición (b)**; la (a) queda **VETADA**. **CH-2 → PAGADO.** El techo sale de aquí **más estricto** que entró. **Gané el gate, no el argumento:** los dos míos eran malos y A7 los desmonta (§10.4) |
| **G-W5-2** | `OT-34` I-2 bajo P-43 | **Confirmado. Cancelación permanente**, en las dos formas y bajo cualquier nombre; no puede volver en W6 ni como «cuerpo de la testigo», ni como «un intercambio más», ni como «lo que anota o no anota» |
| **G-W5-3** | Las declaraciones de paragrafado | **Aprobadas en bloque**, con una corrección formal **bloqueante** (numeración → cita literal; eran **trece**, no doce) y tres de fondo (`OT-24` I-2, `OT-35` I-1, `OT-40` I-1). **Todas aplicadas en §10.5** |

**Veredicto de A7: APROBADO CON CORRECCIONES. Sin veto.** Ocho correcciones obligatorias, las ocho ejecutadas (§14).

### 11.2 · Los de A0: **cerrados por escrito**

| # | decisión | estado |
|---|---|---|
| **G-W5-4** | Reformulación de seis bandas por capítulo (§3) | Hecho. Precedente: `cap-29`. Sin esto A8 falla la oleada por construcción |
| **G-W5-5** | Retirada de tres criterios míos: bloque 34–41 ≤ 13.900, tramo 34→40 ≤ 11.800, diálogo `cap-34` ≥ 15,5 % | Hecho (§6.2). Los tres se apoyaban en una hipótesis que el control de deriva refutó. **A7 respalda el tercero por una razón que no es métrica: «un porcentaje no vale un personaje»** |
| **G-W5-8** | Rechazo del ripple de N4 en `cap-36` (≤ 8 palabras) | Rechazado. La propia `OT-36` §5 lo prevé y CH-1 queda pagado con N4 + 32 |

### 11.3 · Los dos del autor: **abiertos**

| # | decisión | recomendación de A2 |
|---|---|---|
| **G-W5-6** | **R3: cerrarla en 175 y no colocar las 425**, o activarlas fuera del `cap-40` | **Cerrarla.** A7 cierra el destino previsto con **P-47** y añade dos condiciones si el autor las activa en otro sitio (§7.2). El `cap-40` ya no es una opción |
| **G-W5-7** | **Criterio de salida de W5 en el eje Ritmo.** «Ritmo ≥ 8,0» lleva cinco mediciones sin moverse, y v0 puntúa igual | Sustituirlo por el que sí responde (`w4r-medicion-final.md` §3): **ningún capítulo nombrado como punto de abandono por dos o más lectores en el mismo hito**. Hoy no lo incumple ninguno |

---

## 12. Lo que creo que no debe hacerse

Ocho cosas. Las tres primeras están en el alcance vigente de W5 y las quito yo; las cinco siguientes vienen de fuera y las rechazo.

1. **R3 beat 3 en el `cap-40`.** Sería la cuarta ejecución del tirón de los vivos en el mismo capítulo, pegada a un span de anclaje único, subiendo el diálogo del capítulo del silencio, dentro del bloque que se acaba de podar por explicarse de más. **Y A7 añade el motivo que lo cierra para siempre (P-47): produciría la cadencia *tiene amigos → no abre el archivo → alivio*, que convierte una decisión abierta en un peldaño de recuperación.** §7.
2. **`OT-40` I-2.** v0 ya tiene el objeto y su pago; el beat intermedio explica lo que el texto muestra. **Y es la que de verdad incumplía el techo de retenciones —clase R sobre un ítem ya retenido y ya cobrado—, no I-1.** Cancelación **permanente**, en cualquier forma y bajo cualquier nombre. §2, §10.4.
3. **`OT-34` I-2.** P-43, con el censo en nueve. Cancelación **permanente**, confirmada por A7 en G-W5-2. §6.1, §10.3.
4. **El ripple de N4 en `cap-36`.** §11, G-W5-8.
5. **Sembrar el acceso de Cuchillo al control de puertas antes del 41**, que A6-1 pide como su segunda mejora. **Los críticos se equivocan aquí y conviene dejarlo escrito.** Haría tres cosas que el proyecto tiene decididas en contra: añade una mecánica (M2), **cierra una ambigüedad que el Ap. A §3 protege** («qué sabe Cuchillo», `13:201`) y convierte en previsible lo único que el final se guarda. Un plan que se anuncia entero no es un plan frágil: es un folleto.
6. **La escena de Maja y Jean vivas «con el hervidor o la firma del divorcio»**, tercera mejora de A6-1. Ya está servida: R1, aprobada por el autor en G-A1, puso a Jean viva dentro de N3, y un crítico la cita con elogio. Y los dos objetos que el crítico nombra están cerrados: **el hervidor cae bajo P-36** y el divorcio bajo `S39-divorcio`.
7. **Podar la Parte III «un veinte por ciento» o «fundir 19 en 30, 25 con 34, 13 con 22 y 32»**, que piden A6-1 y A6-2. Contestado con cifras en `w4r-diagnostico-centro.md` §8: el techo aritmético real de la poda del centro era −615, A4 entregó −394 defendiendo cada declinación, y las fusiones tocan capítulos de v0 del autor y la única medición de voces que tenemos. **El crítico percibe bien y dimensiona a ojo; el número no es una instrucción.**
8. **Rellenar W5 hasta 81.000.** El libro entra en banda con 80.354. Añadir 650 palabras de textura para tocar el centro de la banda es lo que W4 hizo en el 37 y el 38 y lo que la poda tuvo que deshacer. Si W6 deja el manuscrito por debajo del suelo, la escalera de §4.3 está decidida y medida.

---

## 13. Resumen en una tabla

| | |
|---|---|
| Δ W5 | **+768** (rango 670–845) frente a los +1.500 del mapa y los +1.925 con R3 |
| intervenciones (33) | 16 se ejecutan (11 con palabras · 5 a coste cero) · **15 no se ejecutan** · 2 ya hechas en la poda |
| todas las supervivientes con palabras | **APUESTA (8) o PAGO de una línea (3)**. Textura ejecutada: **cero** |
| Parte III | 21.716 → **21.986** · techo 22.150 · **77 por debajo de lo que leyeron los críticos** |
| Parte IV | 18.924 → **19.422** (sigue siendo la más corta) |
| bloque de cierre | **+138** (de +550, o +975 con R3; y de mi propio ≈+400) |
| manuscrito | 79.586 → **80.354**, en banda, +354 sobre el suelo |
| R3 | **cerrada en 175/600**; 425 en reserva del autor, nunca en el 40 |
| gates | **los 3 de A7 resueltos** (`a7-w5.md`: aprobado con correcciones, sin veto) · 3 de A0 cerrados por escrito · **2 abiertos al autor** (G-W5-6 R3, G-W5-7 criterio de Ritmo) |
| prohibiciones nuevas | **P-44 … P-49**, vinculantes hacia adelante (§10.8) |
| segunda pasada de A7 | **obligatoria sobre el diff en seis capítulos**: 40, 35, 31, 32, 24, 26 |

---

## 14. Rastro de las ocho correcciones de A7, y de mis dos errores

| # | corrección de `a7-w5.md` | dónde queda aplicada |
|---|---|---|
| 1 | **Bloqueante.** Reexpresar las declaraciones de paragrafado por cita literal, sin números de línea | **§10.5 reescrita entera**, trece declaraciones |
| 2 | **Bloqueante.** Rehacer la de `OT-24` I-2, hoy autocontradictoria | §10.5 n.º 2, con la redacción de A7 |
| 3 | **Bloqueante.** Sustituir la de `OT-40` I-1 por la de A7; posición (a) vetada; «va sola» de `OT-40` §8 derogado | §10.5 n.º 12 |
| 4 | `OT-35` I-1: párrafo propio **prohibido**; solo la unión al párrafo de Maja | §10.5 n.º 11 · §8.2 |
| 5 | `OT-31` I-1 incorpora **P-48** | §2 · §8.2 · §10.8 · §10.9 |
| 6 | `OT-24` I-1 incorpora las dos prohibiciones de §7.1 de A7 | §2 · §8.2 · §10.9 |
| 7 | Corregir la identificación de `34:253` y anotar el censo de Astrid en **nueve** | **§10.3** · §2 · §6.1 · §8.2 |
| 8 | `OT-26` deja de figurar como «A7 no aplica»: pasa a **A7 nota** | §8.2 · §10.9 |

**Y los dos errores míos, que anoto porque los dos son de método y los dos son enseñables.**

1. **Estampé una regla de anclaje vinculante en la cabecera de este plan y no la apliqué en §10.5.** Escribí las declaraciones en tres numeraciones incompatibles, y en `OT-31` I-1 llegué a mezclar dos en la misma fila: leída en numeración de fichero, mi propia declaración colocaba las réplicas dentro del intercambio de Jessie, es decir justo donde la frase siguiente lo prohibía. **Lo que salvaba la fila era la cita literal — mi propia regla.** Lección operativa: una regla que solo se aplica al trabajo ajeno no es una regla, es una advertencia.
2. **Defendí G-W5-1 con dos argumentos malos y acerté por casualidad.** «Paga un plantado sembrado en un fichero protegido» no exime de nada —si eximiera, el techo estaría vacío, porque aquí toda retención se justifica como pago— y mi caracterización del censo era **falsa**, comprobable contra el texto en treinta segundos. El criterio bueno es el test de las dos clases de §10.4, y **es el que gobierna todo lo que venga**: no se juzga el origen de una línea, se juzga si la narración posee un ítem y declina entregarlo.

**A2 · 2026-08-18 · v2, sobre `informes/a7-w5.md`**


---

## 15. Correcciones de A7 sobre el diff (2026-08-18), aplicadas

Dictamen en `informes/a7-w5-diff.md`. **Aprobado con correcciones, sin veto.** Las cinco, ejecutadas:

1. **`cap-35`** — un solo dato de postura y **no el codo**: «con el codo recogido contra las costillas y la barbilla baja» → «con la barbilla baja» (−7). A7 rechaza expresamente que sea Carta 7 —«caer con la barbilla baja no es conducta de riesgo»— y da el motivo bueno: dos posiciones **ordenadas** más su resultado verificado es formalmente **una instrucción**, y el codo importa el aikido como anatomía. El argumento decisivo: **`3:123` lo paga el eco de las palabras** («caer sin hacerse daño» → «No se hizo daño»), **no la anatomía**.
2. **`cap-24`** — el gesto pierde «dos dedos». **`26:99` y `33:81` no se tocan**: el choque lo creó la recomposición M4b de esta misma oleada, que volvió `26:99` sintácticamente idéntica.
3. **`cap-26`** — suprimido «sin responsable».
4. **§10.5 n.º 6:** eran **diez** antepuestas, no nueve. `OT-26` §9 sí las declaraba las diez; el error estaba en el plan.
5. **§10.1 y hoja de A8:** P-41 se verifica como **«0 coocurrencias NUEVAS»** sobre un censo de **cinco** loci. Verificar «cero» a secas fallaba la oleada contra `9:73`, que es v0 en fichero de protección total. Y **P-44 cond. 7 se cuenta por LOCUS, no por ocurrencia**: `4:27` nombra el cinturón dos veces en la misma línea y es de v0, así que `grep -rno` da 5 y no es una quinta. **Censo verificado hoy: 4 loci.**

**Manuscrito tras las correcciones: 80.275, en banda.**

### Tres repeticiones que solo aparecen leyendo la rama entera

A7 señala que **ninguna intervención las causa por separado**: el gesto de los dos dedos (corregido), la figura «no hay nombre» dicha **tres veces en `cap-26`** con el narrador adelantando lo que dice Maja, y `cap-40` diciendo «No preguntó» dos veces en idéntica construcción y posición. Esto último A7 lo asume como error propio al fijar la posición del cinturón —no vio que la instancia más cercana estaba en el mismo capítulo—, lo deja y cierra `40:81` a modificación (**P-50**).

### Pendiente

**`OT-40` I-4 no está ejecutada.** `40:161-163` conservan el orden de v0 y la declaración n.º 13 queda sin cumplir. Es un reorden a coste cero, tarea de A4, y **A7 debe una segunda pasada sobre él**: permuta dónde cierra una escena a dos párrafos de `S40-despedida`.

Condiciones nuevas: **P-50** (`40:81` cerrado), **P-51** (figura «sin nombre» cerrada en 12), **P-52** (`cap-31` cerrado a clase A), **P-53** (la operaria no vuelve), **P-54** (la cala de Mats no crea precedente — VETO si se cruza), **P-55** (ningún cuerpo de menor recibe más de un dato de postura en acción de riesgo).
