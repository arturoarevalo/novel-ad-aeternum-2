# W5 · Plan de ejecución (A2, 2026-08-18)

**Qué es esto.** No hay OT nuevas. Las siete están escritas desde F2 y siguen vigentes; lo que sigue es su **reconciliación** con (1) el recuento real de hoy sobre `main`, (2) el bloque de restricciones que A7 y A0 emitieron el 2026-08-18 (P-34…P-43, techo de retenciones, enmienda final a G-3) y (3) el cambio de naturaleza del mandato crítico. Donde el plan y el texto discrepan, **gana el texto y lo señalo**.

**Insumos leídos:** `ordenes/OT-{24,26,31,32,34,35,40}.md` íntegras, `OT-22.md` §9, `OT-22b.md` §4.3–§4.4 y §5, `OT-28.md` §9, `OT-36.md` §5, `OT-37.md` §5, `ordenes/RESERVA.md`, `informes/w4r-diagnostico-centro.md`, `informes/w4r-diagnostico-cierre.md`, `informes/w4r-decisiones-centro.md`, `informes/w4r-medicion-ritmo.md`, `informes/w4r-medicion-final.md`, `informes/a7-w4r.md` §7 y §11–§14, `informes/a6-w4r2-critico-{1,2,3}.md`, `informes/a6-w4r2-deriva-v0.md`, `protegidos/spans.json`, y los siete capítulos.

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
| I-1 | PAGO (CH-6)/INTERIORIDAD · el pasado de Tomas | **APUESTA** | 100–120 | **120** | E | Lo piden **dos críticos de tres, por su nombre**: «Tomas necesita una escena previa donde su decisión de preservar el coche de Gunnar **tenga coste personal**» (A6-1); «para que su aceptación en la consola sea la decisión de un personaje y no un requisito de la trama» (A6-2). Es la única deuda del libro con dos peticiones nominales. |
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
| I-1 | TENSIÓN/AGENCIA · el plan B explícito | **APUESTA** (definición literal) | 130–170 | **180** | E | Los **tres** críticos dicen que el clímax se concede: «Tomas acepta la petición sin arco previo, la orden de custodia llega en el minuto exacto» · «es una comodidad» · «conveniencia en que tantos actores independientes acierten a la vez». I-1 dice en voz alta **qué se pierde si falla el eslabón que no es suyo**. Va en ≤ 6 réplicas cortas: sube diálogo en un capítulo que ya está al 51 %. Autorizado por la propia OT hasta 190. |
| I-2 | INTERIORIDAD · el cuaderno de Nora | TEXTURA/método | ≤40 | **0** | X | Duplica la cola de I-1, que ya incluye la anotación en el cuaderno. **Contingencia 1.ª** (§4.3). |

**Δ OT-31 = +180** (rango 165–195).

### OT-32 «La oferta» — Parte IV

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | TENSIÓN · la interferencia fallida da sentido al veto | **APUESTA** | ≤80 | **80** | E | Carga CH-1: la amenaza de Coro deja de ser una pistola descargada porque **ya se intentó y dejó rastro**. Es lo que convierte `:83` de escrúpulo en conclusión. **Posición fijada: entre `:79` y `:81`; prohibida la alternativa «tras `:81`»** (§5.2). |
| I-2 | INTERIORIDAD · la cala de Mats | **APUESTA** | 80–120 | **100** | E | Es el único sitio del libro donde **el antagonista tiene algo que perder**: guarda íntegros sus propios intentos de voz mientras firma «Las necesarias» para las demás. A6-1: «gana espesor con la ELA oculta». No se enuncia: se mira y se firma. |
| I-3 | TEXTURA · el mundo alrededor de la negociación | TEXTURA | ≤50 | **0** | X | **Contingencia 2.ª** (§4.3). |

**Δ OT-32 = +180** (rango 160–200).

### OT-34 «Soldagen» — Parte IV, bloque de cierre

| # | etiqueta OT | clase | Δ OT | Δ W5 | | motivo |
|---|---|---|---:|---:|:-:|---|
| I-1 | INTERIORIDAD · la cala de Tomas antes de aceptar | **APUESTA** | 100–130 | **100** | E | Segunda mitad de la deuda que dos críticos nombran. Lo que le costará validar durante la cobertura, **antes** de que Jessie llegue. Tope 100 por `w4r-diagnostico-cierre.md` §6.2, que mantengo. |
| I-2 | TEXTURA · la butaca de Astrid | **PROCEDIMIENTO** + colisión con **P-43** | 70–100 | **0** | **X** | **Cancelada, y el motivo es de hoy.** (1) Tras la poda la escena tiene **seis réplicas** (`:213`–`:219`, `:233`, `:237`): el argumento de «darle cuerpo» está caducado. (2) §6.2 la reespecificaba como «un intercambio más con el representante ministerial», y **ese intercambio es exactamente donde vive `—También cualquier omisión.`**, que A7 censa como la **séptima y última** instancia del gesto de abstención de Astrid. **P-43: la octava y la ética se vuelve tic.** (3) La versión original («Astrid consigna: lo que anota o no anota») **es** el gesto de abstención. Las dos formas caen bajo P-43. |
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
| I-1 | PAGO (CH-2) · «No preguntó por el cinturón.» | **PAGO** | ≤8 | **8** | E* | Paga `23:313` («Si volvemos, pregúntale qué sabe del cinturón»), que está en un fichero de **protección total**. B7 §6 la autoriza literalmente. **Condicionada a A7** por dos motivos nuevos: el techo de retenciones y el paragrafado (§5.4, G-W5-1). |
| I-2 | INTERIORIDAD · Nora ante el altavoz | **PROCEDIMIENTO DEL SENTIMIENTO** | 50–60 | **0** | **X** | **Cancelada, y v0 es la razón.** `40:19` ya tiene la hoja doblada, la pregunta escrita, corregida dos veces, y la versión falsa que «le pareció una trampa»; `40:117` ya la cobra («El jueves no volvió con la misma pregunta»). I-2 sería **un tercer beat sobre el mismo objeto, entre los dos que ya existen**, y explicaría lo que el texto muestra. Además sería la **quinta** ejecución de «no preguntar» en un capítulo que ya la hace cuatro veces (`:19`, `:69`, `:101`, `:117`). |
| I-3 | TEXTURA · la casa entre turnos | TEXTURA | ≤40 | **0** | X | Cancelada en §6.2; se confirma. |
| I-4 | AGENCIA/TEXTURA · cierre de `:163` | **COSTE CERO**, reespecificada | ≤25 | **0** | E | **Discrepancia plan↔texto: gana el texto.** La OT pedía convertir en réplica el anuncio de la sesión siguiente de `:161`; **la poda borró `:161`** (corte 6) porque `:175` lo dice mejor. La réplica ya no tiene fuente y añadirla reintroduciría lo que se quitó. **Nueva forma, 0 palabras:** se permuta el párrafo del sensor con el de la tabla, de modo que la escena cierre en «Maja efectuó el pago allí mismo.» — un acto, no un objeto. M4 del capítulo 2 → 1. Ejecuta **A4**, no A3b. |
| I-5 | PAGO (CH-9) · **R3 beat 3** | **PROCEDIMIENTO / REITERACIÓN** | ≤250 | **0** | **X** | §7. |
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

1. **`OT-34` I-2 a +60** — la mata **P-43**, emitida ayer por A7: el censo del gesto de abstención de Astrid está en siete y `—También cualquier omisión.` es la séptima, dentro de la escena que I-2 iba a ampliar. Las dos formas posibles de I-2 producen la octava.
2. **`OT-40` I-2 a +50** — la mata el texto: `40:19` y `40:117` ya hacen su trabajo, y el capítulo ya ejecuta «no preguntar» cuatro veces.
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

- `:117` «Guardó la partitura, corrió hasta la parada y **alcanzó el autobús de clase**.»
- `:119` «La profesora cerró la puerta del aula […] **Nora pasó la hora siguiendo otras voces**.»
- `:181`–`:185` (`S40-cierre`) «A esa hora tenía **ensayo con otras tres personas**» + la convocatoria con «los otros tres nombres y una lista de pasajes que todavía no habían logrado tocar sin detenerse».

Un beat de ensayo con vivos sería la **cuarta** ejecución del mismo movimiento en el mismo capítulo. Es literalmente el defecto que la campaña de ritmo identificó y midió —reiteración, no densidad— aplicado por nosotros, a mano, en el capítulo del silencio, dentro del bloque que el autor acaba de podar −728 porque «el libro sigue explicándose después de haber terminado».

Y hay dos razones técnicas que se suman:

- **Emplazamiento.** El ancla de I-5 es «alrededor de `:131`», es decir **inmediatamente antes de `S40-despedida`**, que es un **span de anclaje único** (51 de los 109 lo son) y una de las líneas más protegidas del libro. Bajo la enmienda final a G-3, insertar al lado **cuenta como modificarla**, y M9 es ciego a todo su entorno.
- **Diálogo.** «Con voces», como pedía §6.2, subiría el diálogo del capítulo cuyo contrato explícito es no subirlo (`OT-40` §6: «7–11 %; no se sube: es el capítulo del silencio»).

**Qué pasa con CH-9.** Queda **PAGADO** con 3 → 9 → 10 → 18 → 22 (R3-1) → 28 (R3-2) → 40 (v0, tres beats) → 41. No hay pago huérfano y M10 no cambia de estado por esto.

**Qué pasa con las 425.** No se reasignan y no se cancelan: quedan como **4.ª contingencia del ledger** (§4.3), a decisión del autor porque G-A1 fijó sus destinos (22/28/40). Si se activan, **no van al 40**: el sitio que quedaría es un cuarto beat en `cap-28` o en `cap-22`, ambos en la Parte III, lo que exigiría revisar el techo de §5. **Mi recomendación es no activarlas nunca.** Una reserva es una autorización de gasto, no una cuota; gastarla para cuadrar un número es la definición de engordar.

---

## 8. (d) Orden de ejecución y gates

### 8.1 · Antes de escribir una palabra

| # | qué | quién |
|---|---|---|
| 0.1 | `inyectar-frontmatter.sh --set cap-NN.md estado=en_oleada` en los siete (`cap-24` figura hoy como `terminado` pese a haber sido podado en W4-R) | A0 |
| 0.2 | Rama `w5-trama` desde `main` | A0 |
| 0.3 | `proteger.sh verificar` (109 spans) y `medir.sh w5-base --baseline v0` como línea de partida | A8 |
| 0.4 | **Consulta previa a A7 (G-W5-1, G-W5-2, G-W5-3 de §11).** Se lanza el día 1 y no bloquea las tandas A y B | A7 |

### 8.2 · Orden

**Se ejecuta en orden de lectura, en tres tandas.** Las dependencias reales son tres y todas quedan satisfechas: `OT-24` fija el canon del pasado de Tomas que `OT-34` no puede repetir y que `OT-35` I-4 necesita cerrado; `OT-26` necesita `cap-n4` y `cap-n6` aceptados (lo están); `OT-40` necesita el dictamen de A7 sobre I-1.

| # | OT | tanda | por qué ahí | gates que dispara |
|---|---|---|---|---|
| 1 | **OT-24** | A | Fija el canon de Tomas (B2 §6). Todo lo demás de Tomas cuelga de aquí | **A7 informativo** (el pasado no puede rimar con el acto, con UNN ni con una muerte; ni clínica, ni menor, ni vehículo) · **A5** (2-ene domingo; OTA 23:16 del 16-dic; canon nuevo a B2 §6; G-3′ sustituye al checklist «segunda mitad con diff vacío») · **A8** (M1 baja a ≈6,7 por denominador; M2 = 0; **tramo ≤ 197**; M4 `:115` variado; `S24-once` y `S24-cierre` íntegros) · **M10 CH-6 → PAGADO** |
| 2 | **OT-26** | A | Ripples de N4/N6, ambos aceptados. Y el M4b, que es el trabajo real | **A5 fuerte** (caja de `:17` = caja de N4; medios del instituto retirados vs. AK-7 accesible el 7/20/21-ene; el asunto de `:175` = el que N6 cobra, **sin anticipar el resultado**) · **A8** (**M4b 16,8 % → ≤ 8 %**, ≥ 9 recompuestas; M1 no sube; M2 = 0; sin cierre-objeto nuevo) · A7 no aplica |
| 3 | **OT-31** | B | Independiente. Es la respuesta estructural al «clímax concedido» | **A5** (canon B3 §16 custodia «ante manifestación pública verificable» y §17 llave/repetidor/vinculación; `33:221–223` y `35:207` coherentes; **Jean no conoce N4**) · **A8** (M1 ≤ 23,3 y **0 términos nuevos**; **M2 = 0**; tramo ≤ 100; diálogo 48–58 %) · **A7 nota** (`S31-elegir` sin glosa) · **M6b** (réplicas nuevas de cuatro voces: es la mejor muestra de la oleada) |
| 4 | **OT-32** | B | Depende de N4 (aceptado). Cierra CH-1 con N4 | **A5** (los tres avisos y sus rastros tal como los fija `cap-n4.md`; `:83`/`:85`/`:87`/`:91`/`:93` verbatim; «casi seiscientas»/597; nada de NORNA) · **A8** (M1 no sube, 0 términos nuevos; M2 = 0; **M4b ≤ 8 % con 0 antepuestas nuevas**; tramo ≤ 339) · **A7 nota** (la ELA sin paralelo enunciado; `HIJO` intacto) · **M10 CH-1 → PAGADO (N4 + 32)** |
| 5 | **OT-34** | C | Después de 24 (no repite su pasado; puede citar un objeto) | **A5 el más fuerte de la oleada** (las diecisiete horas del clímax; `4.096 − 2.911 = 1.185` intacto y **prohibido «la consolidación borró 1.185»**; `2.401,6 AÑOS-JM`; cobertura «hasta 12:47» sin alargar; `:257` verbatim) · **A8** (M1; M2 = 0; tramo ≤ 374; M4 = 0, ya conseguido) · **A7 nota** + **verificación P-43 explícita: 0 instancias nuevas del gesto de abstención** |
| 6 | **OT-35** | C | Después de 24 y 34: I-4 necesita 16 y 24 finales, e I-1 no puede heredar interior de Tomas | **A7 informativo** (Ap. F P7: la caída es coste de una acción de la madre, no proeza; Jessie sin herida; nada nuevo del naust) · **A5** (12:38/12:41/12:42/12:43/12:46:01/«Cuarenta segundos»/12:46:50; **AF-1 sin alargar**; decisión sobre `:149` anotada en B2 §9.5) · **A8** (M1; M2 = 0; tramo ≤ 228) · **M10 CH-4 → PAGADO** |
| 7 | **OT-40** | C | Último: necesita el dictamen previo de A7 y la Parte IV ya cerrada | **A7 OBLIGATORIO, previo al borrador y de nuevo sobre el diff** (posición y literal de CH-2; techo de retenciones; paragrafado en las dos direcciones; ningún interior de Jessie; prensa sin causa ni método; «Despedida» sin abrir) · **A5** (`:161` y `:175` verbatim; el reorden de I-4 no toca fechas) · **A8** (M4 del capítulo 2 → 1; M4b ≤ 8 %; diálogo 7–11 %) · **M10 CH-2 → PAGADO** |

### 8.3 · Después de los siete

| # | qué | quién |
|---|---|---|
| 8 | Pasada de línea (lista negra B6b; molde «X tenía Y»; acotaciones) | **A4** |
| 9 | Continuidad global de la oleada + cruce `OT-37` §5 (la sala de 34 ↔ 37) | **A5** |
| 10 | **Auditoría adversarial** sobre los tres capítulos con más prosa nueva: **24, 31, 32** (`auditor-adverso.sh`, `gpt-5.6-sol`). No es gate: A0 decide qué se borra | A0 |
| 11 | A4 repara lo que A0 acepte de la auditoría | A4 |
| 12 | A8: `medir.sh w5 --baseline v0`, `proteger.sh verificar`, `validar-frontmatter.sh`, `m4b_antepuestas.py`, `sensibilidad.sh --solo` en los siete, compilado `w5` | A8 |
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
- **Verificación obligatoria (A8, `grep`):** censo en seis, **0 coocurrencias** Kongsbakken↔Jean en capítulos, borradores, hojas de intervención y prompts. Nadie —tampoco Nora en interioridad— recuerda la discusión donde Kongsbakken aparece.

### 10.2 · P-42 (el cuarto ítem de `22:203`)

`cap-22` no está en W5, pero la prohibición alcanza a **todo material del proyecto**. Este plan **no especifica el cuarto ítem**, no se refiere a «la cuarta» ni a «lo que no dijo», y **ninguna intervención de W5 puede recoger, recordar, completar, corregir ni cobrar ese beat**. Se anota expresamente en el handoff de A3b y en el checklist de A5.

### 10.3 · P-43 (gesto de abstención de Astrid: censo en siete)

Censo: `18:157`, `22:147`, `22:203`, `29:147`, `n4:423`, `39:181`, `34:253`. **Techo alcanzado.**

- **Mata `OT-34` I-2** en sus dos formas (§2, §6.1).
- Astrid no aparece en ninguna otra intervención de W5. **A5 y A7 verifican 0 instancias nuevas** sobre el diff completo de la oleada, no solo del 34.

### 10.4 · Techo de cuatro retenciones (`OT-22b` §4.3)

Las cuatro registradas: `22:147` (un título de música) · la escena del canal en `23` (una pregunta elegida en lugar de otra) · `39:179-181` (tres líneas escritas, dos dichas) · el beat de CH-48 en `22` (una resta hablada). **La quinta es rechazo automático; si dos comparten registro, la nueva se revierte.**

Dos consecuencias en W5:

1. **`OT-40` I-2 queda cancelada también por aquí**, y de la peor manera posible: «el precio de no preguntar lo que escribió» comparte registro con `39:179-181` —una pregunta **escrita** y no formulada— y lo hace en el capítulo siguiente y en boca de la hija de quien lo hace en el 39. Comparten registro: se revertiría aunque la otra sea anterior.
2. **`OT-40` I-1 («No preguntó por el cinturón») va a A7 antes de escribirse** (G-W5-1). No la doy por buena yo: B7 §6 la autoriza literalmente y es el pago de una línea dicha en un fichero de protección total, pero el techo de retenciones se emitió después que B7 y la colisión es real. Si A7 dictamina que es una quinta, **CH-2 pasa a SIN-PAGO-INTENCIONAL** —el silencio de Jessie lo paga— y W5 cierra con +760. El libro ya trata así CH-44 y CH-76.

### 10.5 · Enmienda final a G-3 · declaración de paragrafado

> El paragrafado es énfasis. **Vaciar, partir, fundir, reordenar o insertar al lado** de una línea protegida cuenta como modificarla. **51 de los 109 spans son de anclaje único** y M9 es ciego a todo su entorno.

**Cada intervención de W5 declara cómo queda paragrafado lo de al lado, por adelantado.** Sin la declaración, A7 devuelve el borrador sin leerlo y A4 no ejecuta.

| intervención | span más próximo | anclaje | **declaración obligatoria** |
|---|---|---|---|
| `OT-24` I-1 (`:113`→`:115`) | `S24-cierre` (`:205`) | con fin | Lejos. `:115` se **sustituye** por el gesto nuevo; `:113` conserva su párrafo; ningún límite de párrafo nuevo entre `:109` y `:117`. |
| `OT-24` I-2 (entre `:91` y `:93`) | `S24-once` (`:33`) | **ÚNICO** | Lejos. `:93` (réplica de Tomas) **conserva su párrafo propio y su vecino por arriba**; la inserción entra como párrafo nuevo antes, no partiendo `:91`. |
| `OT-26` I-1 (`:17`) | — | — | La frase «El seguimiento y la retención bastaban.» puede recomponerse pero **no puede quedar sola entre dos blancos**; el párrafo sigue siendo uno. |
| `OT-26` I-2 (`:77`–`:81`) | — | — | `:81` («—No sabemos quiénes son.») **conserva su párrafo y sigue cerrando el intercambio**. |
| `OT-26` I-3 (`:175`) | `S26-bocana` (`:191`) | **ÚNICO** | **La ampliación va DENTRO de la réplica de `:175`**, que sigue siendo un solo párrafo. Nada nuevo entre `:183` y `:191`. `S26-bocana` no cambia de vecino por arriba ni por abajo. |
| `OT-26` I-5 (M4b) | los cuatro spans | 3 únicos | Recomponer una antepuesta **no puede** partir, fundir ni reordenar párrafos: se reordena **dentro de la frase**. Ninguna de las 17 está dentro de un span salvo la de `S26-lata`, que **no se toca**. |
| `OT-31` I-1 (entre `:117` y `:119`) | `S31-sacar` (`:97`), `S31-cancion` (`:233`) | **ÚNICOS** | Lejos de los dos. `:119` (`UMBRAL 2 · TRANSPORTE PÚBLICO`) **conserva su forma de registro y su posición**; las réplicas nuevas entran como párrafos propios entre `:117` y `:119`. |
| `OT-32` I-1 (**entre `:79` y `:81`**) | `S32-amenaza` (`:85`) | **ÚNICO** | **Posición fijada y la alternativa prohibida:** insertar «tras `:81`» dejaría la inserción a un párrafo de `:83` y a dos de un span de anclaje único. Con la posición fijada, `:81`, `:83` y `:85` conservan sus párrafos y su orden, y `S32-amenaza` no cambia de vecino. |
| `OT-32` I-2 (`:171`/`:181` zona SYNVEV-2) | `S32-cierre` (`:195`) | **ÚNICO** | La cala **no se coloca en el último párrafo antes de `S32-cierre`**; los tres registros y `:195` conservan párrafo y orden. |
| `OT-34` I-1 (entre `:255` y `:257`) | `S34-cierre` | con fin | Lejos. **`Esperó.` sigue solo en su párrafo y sigue cerrando la escena 6**; `:257` conserva su párrafo íntegro. |
| `OT-35` I-1 (`:261`) | `S35-cierre` (`:265`) | con fin, **adyacente** | La línea nueva **se une al párrafo `:261` o forma párrafo antes de `:263`**; **`:263` sigue siendo el párrafo tampón** entre la caída y el span. Prohibido dejar la línea de la caída sola inmediatamente antes de `S35-cierre`: sería el énfasis máximo para lo que debe pasar desapercibido. |
| `OT-40` I-1 | `S40-locutorio` (fin: «—Vuelvo el jueves.») | con fin | **Decide A7.** La posición (a) —entre «—Vuelvo el jueves.» y el dinkus— **le quita a esa réplica la posición de énfasis máximo del libro** y se la da a la línea del cinturón, que es lo contrario de lo que B7 §6 pide. **A2 recomienda la posición (b)**: dentro del párrafo del jueves (`:115`), antes de «Nadie le pidió un resumen.», que conserva su lugar final. Es el mismo principio que `OT-22b` §3.1: **el remate va en el hecho administrativo, no en lo que duele.** |
| `OT-40` I-4 (reorden) | `S40-despedida`, `S40-caries` | **ÚNICOS** | Permutan **dos párrafos completos** (el del sensor y el de la tabla) dentro de la escena del naust: ninguno se parte, se funde ni se vacía; ninguna línea queda aislada de nuevo; ningún span cambia de entorno. Ejecuta **A4** con la declaración sobre el diff. |

### 10.6 · P-34, P-35, P-36, P-38

- **P-34:** las salvaguardas del sensor —«en una sola dirección», «unidireccional», «sin señal hasta otra decisión», «autorización posterior»— **no se comprimen más**. Afecta a `cap-40` `:177`–`:179`, que W5 **no toca** (el reorden de I-4 se detiene en el párrafo del sensor de `:163` y no baja al segundo dinkus).
- **P-35, P-36:** `cap-n3` **no entra en W5**, ni para podar ni para añadir. La espina A–F, «El resto era ir.», el 31 subrayado y el hervidor disparan el gate de A7. Sobre el hallazgo de que mi poda agrandó la cena: **no se corrige en W5** —la Parte III no tiene sitio y P-36 cierra el capítulo—; se mide en el hito y se decide en W6, con una lectura más, no con una.
- **P-38:** las cuatro réplicas de `n4:271–277` son la única enunciación viva del coste de Jessie. `cap-n4` no se toca en W5.

### 10.7 · Ambigüedades del Ap. A §3

Ninguna intervención de W5 las resuelve ni las roza: el **ordenante** del sabotaje (`24:79` verbatim; el resumen de `OT-32` I-1 **no tiene autor** y la atribución la hace el lector, no Mats); **qué sabe Cuchillo** (`13:201`); la **consciencia residual**; la denuncia anónima; **«No toda» como techo**. La villanía sigue siendo sistémica: en `cap-32`, si Mats piensa «Coro lo hizo», la inserción se revierte.

---

## 11. Decisiones que necesitan gate

| # | decisión | quién | recomendación de A2 |
|---|---|---|---|
| **G-W5-1** | **`OT-40` I-1 («No preguntó por el cinturón») frente al techo de cuatro retenciones**, y elección de posición con declaración de paragrafado. B7 §6 la autoriza; el techo se emitió después | **A7**, previo al borrador | **Ejecutarla, en la posición (b)**. Es el pago de una línea dicha en un fichero de protección total y no es un gesto de adulto que declina una potestad, que es la clase que el censo recoge. Si A7 dice que es la quinta: **CH-2 → SIN-PAGO-INTENCIONAL**, sin sustituto |
| **G-W5-2** | **Confirmación de que `OT-34` I-2 cae bajo P-43** en sus dos formas | **A7**, informativo | Cancelarla. A2 ya la ha cancelado en este plan; se pide la confirmación para que no vuelva en W6 |
| **G-W5-3** | **Las doce declaraciones de paragrafado de §10.5**, por adelantado y verificables sobre el diff | **A7** | Aprobarlas en bloque; las dos que requieren juicio son `OT-35` I-1 y `OT-40` I-1 |
| **G-W5-4** | **Reformulación de seis bandas por capítulo** (§3). Sin esto A8 falla la oleada por construcción | **A0**, por escrito | Hecho aquí. Precedente: `cap-29` |
| **G-W5-5** | **Retirada de tres criterios míos**: bloque 34–41 ≤ 13.900, tramo 34→40 ≤ 11.800, diálogo `cap-34` ≥ 15,5 % | **A0**, por escrito | Hecho aquí (§6.2). Los tres se apoyaban en una hipótesis que el control de deriva refutó |
| **G-W5-6** | **R3: cerrarla en 175 y no colocar las 425**, o activarlas fuera del `cap-40` | **autor** (G-A1 fijó los tres destinos) | **Cerrarla.** Es la única de las seis que es del autor |
| **G-W5-7** | **Criterio de salida de W5 en el eje Ritmo.** «Ritmo ≥ 8,0» lleva cinco mediciones sin moverse, y v0 puntúa igual | **autor** | Sustituirlo por el que sí responde y ya está propuesto en `w4r-medicion-final.md` §3: **ningún capítulo nombrado como punto de abandono por dos o más lectores en el mismo hito**. Hoy no lo incumple ninguno |
| **G-W5-8** | **Rechazo del ripple de N4 en `cap-36`** (≤ 8 palabras) | **A0** | Rechazado aquí; la propia `OT-36` §5 lo prevé y CH-1 queda pagado con N4 + 32 |

---

## 12. Lo que creo que no debe hacerse

Ocho cosas. Las tres primeras están en el alcance vigente de W5 y las quito yo; las cinco siguientes vienen de fuera y las rechazo.

1. **R3 beat 3 en el `cap-40`.** Sería la cuarta ejecución del tirón de los vivos en el mismo capítulo, pegada a un span de anclaje único, subiendo el diálogo del capítulo del silencio, dentro del bloque que se acaba de podar por explicarse de más. §7.
2. **`OT-40` I-2.** v0 ya tiene el objeto (`:19`) y su pago (`:117`); el beat intermedio explica lo que el texto muestra y comparte registro con `39:179-181`. §2, §10.4.
3. **`OT-34` I-2.** P-43. §6.1.
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
| gates | 3 a A7 (uno previo y bloqueante), 3 a A0 por escrito, 2 al autor |

**A2 · 2026-08-18**
