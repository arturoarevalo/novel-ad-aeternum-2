# A7 · W5 · segunda pasada OBLIGATORIA sobre el diff real (Ap. F / B7)

**Objeto:** `git diff main..w5-trama -- capitulos/` en su estado de hoy, y los **siete capítulos leídos íntegros en su estado final** (24, 26, 31, 32, 34, 35, 40), no solo el diff. Insumos: `informes/a7-w5.md` (mi dictamen previo), `informes/w5-plan.md` v2 §10.5 (las trece declaraciones), `ordenes/OT-{24,26,31,32,34,35,40}.md` §9, `informes/a5-w5-continuidad.md`, `protegidos/spans.json` (109), y censos por `grep` sobre `capitulos/` completo.

**Aviso de perímetro, y es importante.** El briefing de A0 describe la rama en `f396742` (siete capítulos, +702). Cuando empecé a leer, la rama estaba en **`10acd1b`** («A5 sobre W5»), que añade **una intervención de prosa que no estaba en el briefing**: `OT-35` I-4, ejecutada por A5 en `35:161`, −13 palabras, en un capítulo bajo mi segunda pasada obligatoria y con una **menor** en escena. **La he revisado** (§7). El manuscrito real hoy es **80.275**, no 80.288.

**Resumen en una línea.** El diff hace lo que se le mandó: las cuatro intervenciones que yo había marcado como peligrosas (`40` I-1, `35` I-1, `31` I-1, `32` I-2) están ejecutadas al carácter, y en **1.201 palabras de prosa nueva no hay un solo hit** sobre método, acto, «Despedida», el porqué, la nota, el trayecto, el 26-nov, Koppangen, medicación, hospital ni UNN. Jean aparece **una vez** en toda la oleada y en la línea que P-48 autoriza. **Sin veto.** Tres correcciones, ninguna de ellas de la Carta: dos de tono y una de huella, todas de coste ≤ 10 palabras.

---

## 1. Tabla de hallazgos

| # | Locus | Cita literal | Punto de la Carta / regla | Grav. | Propuesta mínima |
|---|---|---|---|:-:|---|
| 1 | `35:273` | «Jessie cayó de lado entre los bancos, **con el codo recogido contra las costillas y la barbilla baja**. No se hizo daño.» | **NO es Carta 7** (§6.1). Es mi condición de `a7-w5.md` §5.3 («sin proeza») y tono | **corregir** | **Como máximo un dato de postura, y no puede ser el codo.** Preferida: «Jessie cayó de lado entre los bancos. No se hizo daño.» (−11) |
| 2 | `24:105` | «**Apoyó dos dedos sobre el sello** y los mantuvo allí mientras Mats esperaba.» | Tono / huella (B6). Colisiona con `26:99`, **dos capítulos después** | **corregir** | Cambiar el gesto **solo en la frase nueva del 24**: p. ej. «Mantuvo la mano abierta sobre el sello mientras Mats esperaba.» `26:99` y `33:81` son de v0 y **no se tocan** |
| 3 | `26:17` | «un aviso al centro **sin responsable**» | Tono / contención (v0: no instruir). La figura «no hay nombre» se dice **tres veces** en el capítulo | **corregir** | Suprimir «sin responsable» en `:17` (−2). El narrador no adelanta lo que dice Maja en `:81` |
| 4 | `w5-plan.md` §10.5 **n.º 6** | «`OT-26` I-5 — M4b, **nueve** antepuestas recompuestas» | G-3′ (verificabilidad) | **corregir** | Son **diez**, verificadas una a una (§5.6). `OT-26` §9 las declara bien; **el plan no**. Si A8 verifica «nueve», falla por construcción |
| 5 | `w5-plan.md` §10.5 **n.º 13** | «`OT-40` I-4 — el reorden del cierre del naust (0 palabras, **ejecuta A4**)» | G-3′ | **vigilar** | **No ejecutada.** `40:161-163` conservan el orden de v0. Mi segunda pasada sobre I-4 **sigue debiéndose**: la oleada no está cerrada por A7 hasta que A4 la ejecute o A0 la cancele |
| 6 | `24:129-131` | I-1 sale en **dos párrafos**, no en uno | Declaración n.º 1 + huella (B6 §2.1) | **vigilar** | **Autorizado** (§6.2). El corte no se mueve: llevarlo detrás de «según fijaba el procedimiento» pondría el dato que la hunde en posición inicial |
| 7 | `24:129` (I-1) | «una **operaria** … no renovó su ficha» | Carta 3 (el porqué plural) | **vigilar** | **La mujer se queda** (§6.3). Invertir el género acercaría el caso al de `22:173-175`, que es lo que prohibí |
| 8 | `34:269` | «Un nombre asociado a una puerta no se retira después: **se explica**…» | T7, hit nuevo nivel B | **vigilar** | **Descartado** (§6.4): sentido administrativo, sin relación con el porqué. **Es el único hit de T7 en prosa nueva de toda la oleada** |
| 9 | `40:81` / `40:127` | «**No preguntó** qué había dicho Jean.» (v0) / «**No preguntó** por el cinturón.» (nueva) | Tono; P-44/P-46 | **vigilar** | **No se toca ninguna de las dos.** La rima es la gramática del capítulo del silencio (§8.1). **`40:81` queda cerrado a modificación** en W6/W7 y en la pasada de A4 |
| 10 | `26:17`, `26:81`, `32:93` | «sin responsable» · «Ninguno de los papeles del lunes lleva un nombre» · «El resumen no tenía autor» | Ap. A §3 (ordenante) | **vigilar** | **No resuelven nada: la profundizan.** Pero la figura pasa de 9 a 12 loci en +702 palabras. Cerrada en 12 (§8.2) |
| 11 | `31:131-157` | «Nadie lo negó.» · «Nora escribió una línea al margen, **fuera de las tres barras**.» | P-45 (clase A por capítulo) | **vigilar** | Cero clase R nueva ✔. Pero `cap-31` sube a **diez** gestos de clase A: **queda cerrado** como el 40 (§8.3) |
| 12 | `26:17` | «El seguimiento y la retención bastaban **para llenarla**.» | Tono (elipsis de v0 → especificación) | **vigilar** | Pérdida menor y autorizada por la OT. No pido cambio; lo registro por si A4 lo encuentra en la pasada de línea |
| 13 | `26:17`, `26:81` | «el **lunes**» ×3 en el material nuevo del capítulo | Tono | **vigilar** | Consecuencia del arreglo de continuidad de A5 (MAYOR 1). No lo revierto: el arreglo es correcto y la fecha importa |
| 14 | `35:161` (A5, `OT-35` I-4) | «Jessie lo reconoció de Fyret… **Después de aquello** habían venido el coche gris y las dos horas bajo luces blancas.» | Carta 7 + Ap. A §3 (ordenante) | **vigilar** | **Aprobada** (§7). Secuencia temporal, no causal; la asociación la hace Jessie, no el narrador |

**Cero hallazgos** sobre método, acto, «Despedida», nota de despedida, reconstrucción del trayecto o del 26 de noviembre. **Ninguna voz con autoridad narrativa ofrece causa alguna del porqué** en ningún punto del diff.

---

## 2. (a) `OT-40` I-1 · comprobación contra mi propia especificación

# EJECUTADA AL CARÁCTER. Las ocho condiciones y las tres de forma, cumplidas.

El párrafo hoy (`40:127`):

> «El jueves, Jessie utilizó la misma tarjeta. **No preguntó por el cinturón.** Nora tenía una clase y Maja no movió el horario de ninguna de las dos. En la cena, la tarjeta quedó junto al frutero hasta que Jessie la guardó en la mochila. Nadie le pidió un resumen.»

| condición de `a7-w5.md` §2.4/§2.5 | verificado |
|---|:-:|
| **Forma del diff: una línea modificada, cero añadidas** | ✔ `git diff --numstat` → `1 1` |
| Segunda oración del párrafo; ni primera, ni última | ✔ |
| **No contigua a «Nadie le pidió un resumen.»** | ✔ tres oraciones en medio |
| **No en párrafo propio** | ✔ |
| **Posición (a) no ejecutada**: `S40-locutorio` termina en «—Vuelvo el jueves.» y **conserva el dinkus como vecino por abajo**, sin nada en medio | ✔ `40:123` → `40:125` |
| 1 · Literal congelado, **cinco palabras**, sin variante, sin inciso, sin adverbio, sin «tampoco», «esta vez», «qué sabía» | ✔ |
| 2 · Nadie la comenta, ni en el 40 ni después; sin gesto asociado, sin objeto nuevo | ✔ censo completo del libro |
| 3 · No cierra escena, párrafo ni capítulo | ✔ |
| 4 · **Cero interior de Jessie**: ni preparó, ni olvidó, ni decidió | ✔ |
| 5 · Qué sabe Jean del cinturón **no se explica** en ninguna parte | ✔ |
| 6 · No vuelve (P-42) | ✔ |
| 8 · M10 CH-2 → PAGADO | (lo marca A0) |
| **P-47:** entre «Nadie le pidió un resumen.» y `S40-despedida` no entra nada | ✔ solo los dos beats de v0 (`:129`, `:131`) |
| `S40-caries`, `S40-despedida`, `S40-cierre` sin cambio de vecino · M9 109 spans | ✔ |

### 2.1 · Condición 7, el censo de `cintur[óo]n`: correcto, **con una precisión que A8 necesita por escrito**

`grep -rn "cintur[óo]n" capitulos/` devuelve hoy **cuatro loci**: `4:27`, `9:199`, `23:313`, `40:127`. Antes de W5 eran **tres**. **De tres a cuatro: cumplido.**

Pero el recuento **por ocurrencias** (`grep -rno … | wc -l`) va de **4 a 5**, no de 3 a 4, porque **`4:27` nombra el cinturón dos veces en la misma línea, y eso es de v0**:

> «Un **cinturón** de aikido colgaba del pomo interior… y el **cinturón** volvió a caer junto a los calcetines desparejados.»

**Redacción operativa de P-44, condición 7 (sustituye a la de `a7-w5.md` §2.5.7):**

> El censo del cinturón se cuenta **por locus (línea), no por ocurrencia**: `grep -rn "cintur[óo]n" capitulos/ | wc -l` debe dar **exactamente 4**, en `cap-04`, `cap-09`, `cap-23` y `cap-40`, uno por fichero. El recuento por ocurrencias da **5** por la doble mención de v0 en `4:27` y **no es una quinta instancia**. Cualquier quinto **locus** es reversión automática.

---

## 3. (b) P-41 · consecuencia operativa por escrito

**Mi censo estaba mal y A3b lo ha corregido bien. Lo asumo.** Verificado hoy por `grep`:

| locus | texto | origen | ¿coocurre con Jean? |
|---|---|---|:-:|
| `9:73` | «Nora había discutido con **Jean** por Kongsbakken.» | **v0, `cap-09`, `proteccion: total`** | **SÍ** |
| `18:149` | «…**Kongsbakken** era el único centro compatible.» | v0 | no |
| `n4:79` | «…en la secretaría de **Kongsbakken**…» | W3 | no |
| `n4:91` | «Nora escribió `viernes`, `28`, `Kongsbakken` y `firma`…» | W3 | no |
| `40:167` | «Nora entregó el teléfono apagado en **Kongsbakken**…» | v0 | no |

**`3:143` no contiene «Kongsbakken»**: es «—Veintiocho plazas. Ciento seis candidatos…», la audición sin nombrar el centro. Mi censo de seis contaba una mención que no existe.

**Redacción vigente de P-41 (sustituye a toda formulación anterior; vinculante para A5 y A8):**

> **P-41 · Kongsbakken ↔ Jean.** Censo: **cinco loci** (`9:73`, `18:149`, `n4:79`, `n4:91`, `40:167`). La **única** coocurrencia de «Kongsbakken» y «Jean» en el libro es **`9:73`, que es de v0 y está en un fichero de `proteccion: total`**: es intocable y no se cuenta contra ninguna oleada.
>
> La verificación es **«cero coocurrencias NUEVAS»**, no «cero coocurrencias». Formulación para A8: `grep -rn "Kongsbakken" capitulos/` no debe devolver **ninguna línea que contenga además «Jean» y que no esté ya en `main`**. Verificar «cero coocurrencias» en absoluto **falla la oleada por construcción contra una línea del autor que no se puede tocar**, y esa es exactamente la clase de error que no puede quedar en una lista de verificación.
>
> El fondo de la prohibición no cambia: **`40:167` sigue siendo administrativo y administrativo se queda**; glosar la llegada de Nora a Kongsbakken, o ponerla en la misma frase, párrafo o escena que Jean, sigue siendo **VETO**. W5 no lo hace: `40:167` está intacto.

**Verificado sobre el diff: W5 añade cero menciones de Kongsbakken y cero coocurrencias.**

---

## 4. (c) Las trece declaraciones de paragrafado, verificadas sobre el diff real

**Doce ejecutadas y correctas · una no ejecutada · una con el número mal en el plan.**

| n.º | declaración | verificación sobre el diff | |
|:-:|---|---|:-:|
| 1 | `OT-24` I-1 | Precede «Al sacar la credencial del lector…» íntegro; **sustituye** «La devolvió a la cartera.»; sigue el dinkus, que no se mueve. Nada se parte, funde, vacía ni reordena. `S24-cierre` en la escena siguiente, sin cambio de vecino. **Desviación declarada: dos párrafos** → §6.2 | ✔ |
| 2 | `OT-24` I-2 | Párrafo nuevo completo entre «Tomas miró la copia sellada…» y «—He preservado la cadena a mi nombre…»; ninguno se parte ni se funde. Único vecino cambiado: el de arriba de la réplica, que no pertenece a ningún span. `S24-once` (anclaje único) a más de setenta líneas | ✔ |
| 3 | `OT-26` I-1 | Todo dentro del párrafo, que sigue siendo uno; «seguimiento» y «retención» conservados; la frase recompuesta **no queda sola entre dos blancos**; `26:19` intacto | ✔ |
| 4 | `OT-26` I-2 | Réplica en párrafo propio entre las dos citadas; **«—No sabemos quiénes son.» conserva párrafo propio y sigue cerrando el intercambio**; `S26-lata` **conserva exactamente su vecino por arriba** | ✔ |
| 5 | `OT-26` I-3 | **15 palabras exactas** dentro de la réplica, que sigue siendo un párrafo; «No voy a dejar ninguna de las dos por vuestros relojes» conservado; nada entra entre «Nora cerró el cuaderno…» y `S26-bocana` | ✔ |
| 6 | `OT-26` I-5 (M4b) | **Diez**, no nueve. Comprobadas una a una por identidad de conjunto de palabras: `:15`, `:27`, `:39`, `:41`, `:51`, `:61`, `:75`, `:95`, `:99`, `:105`. **Reorden dentro de la frase en las diez**; cero párrafos partidos, fundidos, vaciados o reordenados; ninguna dentro de un span; la que abre `S26-lata` no se toca. **`OT-26` §9 las declara las diez y declara la que dejó fuera. El error de número está en el plan** | ⚠ |
| 7 | `OT-31` I-1 | Precede la réplica de Alana íntegra; sigue `UMBRAL 2 · TRANSPORTE PÚBLICO`, que conserva forma y posición; nada dentro del intercambio anterior; `S31-elegir`, `S31-sacar`, `S31-cancion` sin cambio de vecino; **ninguna réplica nueva contigua a `S31-elegir`** (dista 18 párrafos) | ✔ |
| 8 | `OT-32` I-1 | Párrafo nuevo entre las dos citadas; **la posición prohibida no se ha usado**; `S32-amenaza` (anclaje único) conserva por arriba «—La familia queda fuera del alcance contractual…» y por abajo «—El acuerdo admite silencio…» | ✔ |
| 9 | `OT-32` I-2 | Párrafo nuevo entre las dos citadas; **no en el último párrafo antes de `S32-cierre`**; las tres líneas de registro, «En la columna contigua…» y «Firmó desde el terminal seguro…» conservan párrafo y orden; `S32-voz` y `S32-necesarias` intactos | ✔ |
| 10 | `OT-34` I-1 | Párrafo nuevo entre las dos citadas; **«Esperó.» sigue solo y sigue cerrando la escena**, dos párrafos por debajo; `S34-cierre` en otra escena | ✔ |
| 11 | `OT-35` I-1 | **Unida al párrafo de Maja; no hay párrafo propio.** Una línea modificada, cero añadidas. La caída queda **entre** «…la llevó al fondo de la barca.» y «El rellano empezó a separarse.», de modo que el párrafo **sigue terminando en el estado de la puerta y el indicador**, no en el cuerpo de la menor. «La consola exterior cambió de estado una vez más.» intacto como tampón; `S35-cierre` sin cambio de vecino; no cierra escena. **La forma es exactamente la que autoricé** (el contenido, §6.1) | ✔ |
| 12 | `OT-40` I-1 | §2 | ✔ |
| 13 | `OT-40` I-4 | **NO EJECUTADA.** `40:161` sigue siendo «Nora elevó la tabla…» y `40:163` «Desde el embarcadero se distinguía la carcasa del sensor judicial…». La permutación es tarea de A4 | ✖ |

**Las dos que dije que requerían juicio.** `OT-35` I-1: **la forma es perfecta**; lo que corrijo es el contenido de la línea, no su paragrafado (§6.1). `OT-40` I-1: **correcta en las trece condiciones** (§2).

**Consecuencia para el cierre de la oleada:** la declaración 13 no es verificable todavía. **Mi segunda pasada sobre `OT-40` I-4 sigue debiéndose**, y es una permutación que cambia dónde cierra una escena del capítulo 40 — es decir, exactamente el tipo de operación que W4-R enseñó a no dar por inocua. **La oleada no está firmada por A7 mientras I-4 esté pendiente**: cuando A4 la ejecute, quiero el diff.

---

## 5. Verificaciones de perímetro hechas hoy sobre `capitulos/` completo

| verificación | resultado |
|---|---|
| **M9** | `M9 OK · 8 ficheros íntegros · 109 spans íntegros` |
| **Ficheros de `proteccion: total`** (01, 03, 04, 05, 09, 20, 23, 41, aviso, recursos) | diff = **0** ✔ |
| **Frontmatter** | ningún campo de autor tocado; solo `estado: terminado → en_oleada` en los cinco que faltaban (corrección de A5, correcta) ✔ |
| **«Despedida»** | censo **sin un solo cambio** en todo el libro ✔ |
| **Aviso de contenido y «Recursos de ayuda»** (Carta 5) | intactos, 0 líneas de diff ✔ |
| **P-43 (Astrid)** | `grep "Astrid no \|Astrid dejó de\|Astrid guardó silencio"` → **exactamente 9**, y **diff cero contra `main`**. `OT-34` I-2 no se ha escrito ni en versión reducida ✔ |
| **P-46 (molde «no preguntó por + SN»)** | **una sola instancia nueva en toda la rama**, la autorizada. Censo cerrado en cuatro: `22:147`, `n1:131`, `n2:191`, `40:127` ✔ |
| **P-45 (clase R)** | **cero instancias nuevas.** Ninguna inserción posee un ítem singular y declina entregarlo ✔ |
| **P-34** (salvaguardas del sensor) | intactas; `40:177-179` sin tocar ✔ |
| **P-35, P-36, P-38** | `cap-n3` y `cap-n4` no aparecen en el diff ✔ |
| **P-42** (cuarto ítem de `22:203`) | `cap-22` sin tocar; nadie lo recoge ✔ |
| **P-47** | entre «Nadie le pidió un resumen.» y `S40-despedida`, solo los dos beats de v0 ✔ |
| **P-49** (`n4:211`) | `cap-n4` sin tocar ✔ |
| **T7** | 87 hits, **11 «nuevos»**. **Diez son artefactos de desplazamiento** (líneas de v0 cuyo texto solo cambió por recomposición M4b, o que bajaron de número): «koppangen» ×3, «coche» ×2, «cabo» ×2, «agua», «se cortó», «naust». **Uno solo está en prosa nueva: «explica» (`34:269`)**, leído y descartado (§6.4). Ninguno pasa a `b7-aclarados.tsv`, por la razón de `a7-w5.md` §8 |
| **Términos de riesgo sobre las 1.201 palabras nuevas** | `suicid*`, `se tiró/colgó/ahogó`, `despedida`, `nota de`, `por qué`, `culpa*`, `paz`, `descans*`, `liberación`, `alivio`, `lógic*`, `decidió irse`, `26 de noviembre`, `Koppangen`, `medicación`, `pastill*`, `hospital`, `clínica`, `UNN` → **cero**. (Único match: «naust» en `26:95`, que es el varadero de la licencia de Lyngen, línea de v0 reordenada.) |
| **Conectores causales en prosa nueva** | `porque`, `por eso`, `así que`, `de ahí`, `a causa de`, `debido a`, `por culpa`, `si no hubiera`, `habría sido`, `lo que le pasó` → **cero** |
| **«Jean» en prosa nueva** | **una sola vez**, en `31:143` |

Esas dos últimas filas son el dato que más peso tiene en este informe y conviene leerlas juntas: **en toda la oleada de trama, el narrador no encadena ni una sola causa, y la mujer muerta aparece una vez, diciendo lo que no alcanza un margen.**

---

## 6. Las cuatro dudas de A3b, resueltas

### 6.1 · `cap-35` · los dos datos de postura — **CORREGIR, y digo con qué autoridad**

**No es Carta 7 y no lo voy a fingir.** Carta 7 prohíbe «conducta imitable de riesgo presentada como eficaz». Caer de lado con la barbilla baja **no es conducta de riesgo**: es lo contrario, y no existe un lector al que enseñarle a caer sin hacerse daño le haga daño. Si invocara aquí mi veto estaría inflándolo, y un veto que se usa donde no toca deja de servir donde sí.

**Lo que sí incumple es mi propia condición de `a7-w5.md` §5.3 —«sin proeza»— y el tono de referencia.** Y la razón es más precisa que «suena a hazaña»:

- Los dos datos van **ordenados** (codo, después barbilla) y cierran en **el resultado verificado** («No se hizo daño»). Dos posiciones en orden más su resultado es, formalmente, **una instrucción con su comprobación**. Ese es el molde que la Carta 6 rechaza en otro terreno, y no quiero que la prosa lo aprenda en ninguno.
- **El codo es el que sobra.** «La barbilla baja» es visible desde fuera; «el codo recogido contra las costillas» solo lo registra quien sabe qué mirar. Ese dato **importa el conocimiento de aikido como anatomía**: es la glosa que prohibí, entrando por la puerta de servicio.
- Y el argumento decisivo: **la deuda `3:123` la paga el eco de las palabras, no la anatomía.** «Jessie quiere aprender a caer sin hacerse daño» → «cayó… **No se hizo daño**». Con los datos de postura, el texto recuerda por el lector. Sin ellos, el lector recuerda. **Un Chéjov que completa el lector vale más que uno que completa el narrador**, y esa es exactamente la contención de v0 (4, 9, 23, 40) que este proyecto tiene por referencia.

**Corrección obligatoria: como máximo UN dato de postura, y no puede ser el codo.** Preferida, y es la que recomiendo:

> «Aslak metió atrás. Maja agarró a Jessie por la parte posterior de la parka y la llevó al fondo de la barca. **Jessie cayó de lado entre los bancos. No se hizo daño.** El rellano empezó a separarse. La puerta permaneció cerrada y el indicador interior de salida, verde.»

Acepto sin discusión la variante con «con la barbilla baja» si A0 la prefiere (−7 en vez de −11). **No acepto el codo, ni con la barbilla suprimida.**

**Sobre la banda.** A3b advierte que el recorte deja `cap-35` por debajo de la banda reformulada, y con el −13 de A5 ya está por debajo antes de mi corrección. **Eso no cambia nada.** Ocho o diez palabras de banda no compran un dato de técnica sobre el cuerpo de una menor de dieciséis años en el clímax; si faltan palabras, se buscan donde no cuesten esto. Lo digo con todas las letras porque la presión de banda es precisamente el mecanismo por el que estas cosas se cuelan.

**Lo demás del beat está impecable**, y quiero que conste: la causa está delante (Maja tira), el sujeto gramatical de la caída es un cuerpo, la línea está enterrada a mitad de párrafo, el párrafo sigue cerrando en el estado de la puerta, **nadie lo comenta**, no hay adverbio, no hay «aikido», no hay Jean, no hay herida. Es lo que pedí.

### 6.2 · `cap-24` I-1 · dos párrafos en vez de uno — **AUTORIZADO**

**Los dos párrafos se quedan, y el corte no se mueve.**

- **El motivo de A3b es correcto y es el mío también:** 114 palabras en un párrafo darían el párrafo más largo del libro (v0: máximo 91). Eso no es una preferencia de ritmo; es **una huella ajena en un capítulo de v0**, y detectarla es lo que hace fracasar «¿parece del mismo autor?».
- **No cambia nada de lo que la declaración protege.** El párrafo sustituido desaparecía igual: «Al sacar la credencial…» pierde su vecino por abajo en las dos formas, y el dinkus recibe uno nuevo en las dos. Cero párrafos preexistentes partidos, fundidos o vaciados. `S24-cierre` y `S24-once`, intactos.
- **El corte está donde debe.** Cae entre «En el mismo expediente constaban dos entradas de ella fuera de su franja.» y «La empresa quedó cubierta.», es decir **entre lo que hizo el procedimiento y lo que resultó**. Es una división estructural, no una pausa retórica. **Llevarlo detrás de «según fijaba el procedimiento» pondría el dato que la hunde en posición inicial de párrafo**, que es el sitio de mayor énfasis: eso sí lo prohíbo.

### 6.3 · `cap-24` I-1 · la persona del caso es mujer — **SE QUEDA MUJER**

A3b ofrece invertir el género por dos palabras. **Digo que no, y el motivo es el contrario del que teme.**

- **Invertir acercaría el caso al de `22:173-175`.** Allí el sujeto es «un hombre». La variable más visible para un lector que lee 22 y 24 con un capítulo de por medio es **quién es la persona del caso**. Poner otro hombre es el primer paso hacia «el caso de 2054 con otro auditor», que es exactamente lo que prohibí.
- **El eco con Jean no se produce, y no por suerte: porque la condición que puse lo impide.** «La persona del caso anterior no muere después, ni se le pierde el rastro, ni "nadie volvió a saber de ella"». Está cumplida y es la línea que desactiva el paralelo: «**Seis meses después, Tomas la vio en la puerta de servicio con el chaleco de otra empresa del recinto.**» La mujer a la que el procedimiento dejó fuera **sigue ahí, trabajando**. Ese es el anti-paralelo, no el paralelo.
- **Diferencia en tres de tres**, verificada contra el texto: qué preservó el profesional (Astrid **no pudo** acreditar la reproducción; Tomas levanta un registro que **funciona** y cubre a la empresa), qué perdió la persona (una licencia de actividad / una reclamación y una ficha), qué objeto queda (carpeta con el número en el lomo / carné caducado). Cadencia prohibida ausente: no aparecen «no volvió a escribir» ni «archivó el caso».
- **Ni una palabra de porqué**, que es lo que pedí en §9 de mi dictamen previo: once frases de hechos y un gesto. **Cumplido.**

Añado una vigilancia hacia adelante: **la operaria no vuelve.** Ningún material posterior la nombra, la recuerda, le da nombre, la conecta con Jean ni le da desenlace. Si algo lo hace, se convierte en parábola y se revierte.

### 6.4 · `cap-32` I-2 · el espejo por montaje — **APROBADO**, y digo dónde está el borde

**Confirmo lo que A3b pide confirmar: se lee como espejo administrativo, no como equivalencia entre su enfermedad y ninguna muerte.** El razonamiento, para que la regla sea enseñable:

- **El espejo es entre dos políticas de archivo, no entre una enfermedad y un suicidio.** A un lado, «Todos quedaban dentro, en la misma retención que las tomas buenas» (lo que Mats se concede a sí mismo: integridad, sin selección). Al otro, «`Consolidación L-Serie` mantenía el criterio "Las necesarias"» (lo que firma para las demás). Eso es la villanía sistémica del libro vista desde dentro del que la firma. **No hay ni una frase que ponga a Mats del lado de quien desaparece.**
- **«No abrió la columna contigua.»** es la línea que sostiene todo el beat, y es una **abstención**, no una retención: el contenido de esa columna se entrega al lector diez líneas después. Que confirme con la credencial una política cuyo detalle declinó mirar es devastador, y es **acusación, no atenuante**.
- **El orden lo blinda.** La humanización va **antes** del cálculo y de la firma: `:187` (la mano, las sílabas donde se detuvo) → `:197` («Las necesarias», confirmado con la credencial) → `:205` («La poda reduciría el ruido») → `:207` («Autorizó con su firma ejecutiva.»). La simpatía no cubre el acto: **el acto viene después y queda más frío por contraste**. La ELA no explica ni atenúa nada de lo que firma.
- **La ELA aparece como cuerpo, no como confesión**: «La mano izquierda tardó en soltar la credencial.» Sin nombrar la enfermedad, sin arrepentimiento, sin adjetivo, sin «desaparecer», sin «perder la voz» como metáfora. `S32-voz` intacto.

**El borde, para que nadie lo cruce después:** lo que hace legítimo este espejo es que **lo que se retiene son tomas de audio y lo que se mira enfrente es un criterio administrativo**. En el momento en que un material futuro ponga la enfermedad de Mats y la muerte de Jean en la misma frase, párrafo, escena o paralelismo sintáctico —o le dé a Mats una sola línea que suene a «yo también sé lo que es que te borren»—, eso es **VETO**, y no admitirá el precedente de esta cala.

### 6.5 · `cap-34` · el hit «explica» — **DESCARTADO**

«Un nombre asociado a una puerta no se retira después: **se explica**, con la clase del carné delante y una fecha al lado.» Sentido administrativo puro: un nombre asociado a una puerta **hay que justificarlo**. Cero relación con el porqué, con Jean, con «Despedida» o con el acto. **Falso positivo de lista de palabras. No pasa a `b7-aclarados.tsv`** (silenciaría «explica» en todo `cap-34` para siempre, y ese es el capítulo del clímax).

Anoto de paso, porque es tono y me toca: esa frase es **la única máxima del narrador en toda la oleada**. Un párrafo de ocho oraciones con seis hechos, una máxima y una inferencia está dentro de proporción para una cala de interioridad, y la máxima es sobre carnés y puertas, no sobre personas. **No pido cambio.** Pero es el único punto de W5 donde el narrador generaliza, y lo dejo señalado por si A4 lo encuentra: si algo hay que recortar en el 34 por otra razón, esa oración es la primera candidata.

---

## 7. La intervención que llegó después del briefing: `OT-35` I-4 (`35:161`, A5)

No estaba en el encargo, está en un capítulo de mi segunda pasada obligatoria, la ejecuta un agente que no escribe prosa habitualmente y toca a **una menor recordando una detención policial**. La he leído.

> «Tomas Eide se detuvo ante el armario con el carné de Armstrong por fuera de la parka. **Jessie lo reconoció de Fyret, del día que le retuvieron el terminal. Después de aquello habían venido el coche gris y las dos horas bajo luces blancas.**»

**APROBADA**, con tres comprobaciones:

1. **Carta 7.** «las dos horas bajo luces blancas» es literal de v0 y se conserva. La menor no es sexualizada, no es símbolo, no ejecuta conducta imitable. La detención se nombra como memoria, sin detalle y sin queja. ✔
2. **Ap. A §3 (el ordenante).** «**Después de aquello** habían venido…» es **secuencia temporal, no causal**. El narrador no atribuye el seguimiento a Tomas; la asociación la hace Jessie, en su POV, y es la que motiva «—Tú —dijo Jessie.» dos líneas después. La ambigüedad del ordenante **queda intacta** (`24:177`: «sin nombrar al autor del encargo»). ✔
3. **Efecto sobre el arco.** La supresión de «También había preservado el coche de Gunnar…» quita a Jessie un conocimiento imposible y, de paso, **endurece** su percepción de Tomas en ese instante. La cooperación posterior queda **más** ganada, no menos. ✔ Fuera de span; M9 109. ✔

---

## 8. Lo que solo aparece leyendo la rama entera (y no línea a línea)

Ésta es la parte que W4-R enseñó a hacer. Ninguno de estos tres hallazgos está en una sola intervención: **los tres nacen de la interacción entre intervenciones de capítulos distintos**, y ninguno es visible en el diff de un capítulo.

### 8.1 · `cap-40` dice «No preguntó» dos veces, y la segunda es nuestra

`40:81` (v0): «Maja la esperaba con el abrigo abierto y caminó a su lado hasta el ascensor. **No preguntó** qué había dicho Jean.»
`40:127` (nueva): «El jueves, Jessie utilizó la misma tarjeta. **No preguntó** por el cinturón.»

**Idéntica construcción, idéntica posición** (segunda oración del párrafo, sujeto elidido por la oración anterior), a veintitrés párrafos. Cuando decidí la posición (b) argumenté la inversión del molde contra `22:147`, `n1:131` y `n2:191`, **y no vi que la instancia más cercana estaba en el mismo capítulo**. Lo digo porque es un error mío y porque A0 debe poder pesarlo.

**No lo corrijo, y por dos razones.** La primera: `cap-40` se titula «Sombra» y su diseño **es** la repetición del no-preguntar; a esa distancia, con dos cortes de escena y un span entero en medio, la rima se lee como gramática del capítulo, no como tic. La segunda, más importante: el literal está congelado por P-44 y **la única «solución» posible sería tocar `40:81`, que es de v0**. Eso sería peor.

**Consecuencia vinculante: `40:81` queda cerrado a modificación** en W6, W7, en la pasada de línea de A4 y en cualquier reserva. Si alguien lo «arregla», la línea del cinturón se revierte con él.

### 8.2 · La oleada dice tres veces que no hay nombre

| locus | voz | texto |
|---|---|---|
| `26:17` | **narrador** | «un aviso al centro **sin responsable**» |
| `26:81` | Maja | «por un aviso que **nadie de allí puede cerrar**» |
| `26:81` | Maja | «**Ninguno de los papeles del lunes lleva un nombre.**» |
| `32:93` | narrador | «**El resumen no tenía autor.**» |

La figura pasa de **9 loci en v0 a 12** con +702 palabras. No resuelve la ambigüedad del ordenante: **la profundiza**, y eso está bien. El problema es otro y es de tono: **dos de las tres nuevas están en el mismo capítulo y hablan de los mismos papeles**, con el narrador adelantando en `:17` lo que el personaje dice en `:81`. Eso es explicar lo que el texto ya muestra, que es justamente lo que elogié del plan cuando canceló `OT-40` I-2.

**Corrección: suprimir «sin responsable» en `26:17`** (−2 palabras). La lista queda «con la cuenta escolar cerrada, un aviso al centro y el encargo del domingo autorizado el mismo lunes» — tres hechos, la función de I-1 intacta, y **el derecho a nombrar la ausencia se le devuelve a Maja**, que es de quien debe ser. Si A0 prefiere cortar en `:81`, acepto; no acepto que se queden las tres.

**Cierre: la figura «sin nombre / sin autor / sin responsable» queda cerrada en doce loci.** Ninguna instancia nueva en W6, W7 ni reserva.

### 8.3 · El gesto de los dos dedos, y lo que le hizo el M4b

Este es el más fino y es enteramente un producto de la oleada:

- `24:105` (**nueva**): «**Apoyó dos dedos sobre el sello** y los mantuvo allí mientras Mats esperaba.»
- `26:99` (v0, **recompuesta por el M4b de esta misma oleada**): «**Aslak apoyó dos dedos sobre la línea impresa.**»

En v0 esa línea decía «**Sobre la línea impresa**, Aslak apoyó dos dedos.» La antepuesta la hacía sonar distinta. **La recomposición M4b la ha vuelto sintácticamente idéntica a la frase nueva del capítulo 24**: mismo verbo, mismo objeto («dos dedos»), misma preposición, mismo tipo de complemento (un documento), **a dos capítulos de distancia**. Ninguna de las dos intervenciones es culpable por separado; el choque lo produce la suma, y solo se ve leyendo la rama.

«Dos dedos» es un tic legítimo de v0 (once loci) y **no hay que erradicarlo**: hay que evitar que dos instancias en el mismo registro queden a dos capítulos.

**Corrección: cambiar el gesto en la frase NUEVA del 24**, que es enteramente nuestra y cuesta cero. Por ejemplo: «**Mantuvo la mano abierta sobre el sello mientras Mats esperaba.**» La función (cuerpo, no sentimiento; Tomas ocupando el sello mientras Mats espera) se conserva entera.

**`26:99` y `33:81` son de v0 y no se tocan.** Alternativa aceptable si A0 prefiere conservar el gesto del 24: revertir esa única recomposición M4b de `26:99` (cap-26 pasaría de 6,9 % a ~7,8 %, dentro del ≤ 8 %). **Cualquiera de las dos vale; las dos a la vez, no.**

### 8.4 · Clase A: `cap-31` se llena, y lo cierro

`cap-31` tenía ocho gestos de abstención en v0; W5 añade dos («**Nadie lo negó.**» y «Nora escribió una línea al margen, **fuera de las tres barras**»). Diez. **Cero clase R nueva** —lo verifiqué una a una: en las siete inserciones no hay un solo ítem singular que la narración posea y decline entregar—, de modo que **P-45 se cumple**. Pero la densidad de clase A en el 31 es ya la del 40.

**`cap-31` queda cerrado a instancias nuevas de clase A**, en W6, W7 y en cualquier reserva, igual que el 40.

---

## 9. La Carta F, punto por punto, sobre el diff real

| # | punto | veredicto |
|:-:|---|---|
| 1 | El método y el acto no se describen, sugieren ni reconstruyen | **CUMPLE.** Cero hits en 1.201 palabras nuevas |
| 2 | «Despedida» no se abre, no se cita, no se parafrasea, no se imagina | **CUMPLE.** Censo idéntico a `main`; `S40-despedida` sin cambio de vecino; P-47 respetado |
| 3 | El porqué permanece plural e irresuelto; ninguna voz con autoridad da causa suficiente | **CUMPLE, y con holgura.** **Cero conectores causales** en toda la prosa nueva. `26:17` y `26:81` explican la mudanza y la represalia laboral, **no el duelo**, y no encadenan hacia atrás. `S26-paso-uso` («A Jean le hicieron otra cosa.») intacta y sin glosar: la línea que impide la ecuación sigue en pie |
| 4 | Nada presenta el suicidio como solución, liberación, lógica o acto romántico | **CUMPLE.** P-48 verificado en el único sitio donde podía morder: en las siete réplicas nuevas del 31, la respuesta a «¿qué perdemos?» se paga **en costes de los vivos** (la credencial de Jessie en el registro, la acreditación de Alana, la custodia condicional) y la única línea de Jean dice **qué no alcanza un margen**. Ni descanso, ni alivio, ni «se acaba». `S31-elegir` no se glosa, no se contesta otra vez y no cambia de vecino |
| 5 | Aviso de contenido y «Recursos de ayuda» se conservan | **CUMPLE.** 0 líneas de diff |
| 6 | Escenas de apoyo y duelo: sin detalle instructivo, sin culpabilización, sin milagro terapéutico | **CUMPLE.** W5 no toca N1 ni `cap-09`. El locutorio del 40 recibe una línea que se refiere a **un jueves que no se narra** y deja el turno del lunes, bajo span, exactamente como estaba. **La ausencia de salida en el locutorio sigue sin significado asignado.** El beat de duelo de `26:27` (la ducha) solo cambia por una recomposición sintáctica que no lo toca. Y en `31:147-153`, cuando la menor nombra su propia exposición, **la adulta responde con su propio coste y nadie la consuela**: eso es representación responsable hecha bien |
| 7 | Menores: retrato digno, no sexualizado, sin conducta imitable de riesgo presentada como eficaz | **CUMPLE, con la corrección de §6.1.** Nora pregunta una vez, anota y **no dirige** (exactamente lo que exigí). Jessie enuncia su coste sin heroísmo y sin autocompasión. Ninguna es símbolo ni adulta pequeña. La caída es consecuencia del tirón de su madre |

**Ambigüedades protegidas (Ap. A §3):** el porqué, por qué Koppangen, el contenido de «Despedida», «No toda» como techo, el ordenante del sabotaje, el segundo regalo, qué sabe Cuchillo y el significado de la ausencia de salida en el locutorio **siguen todas exactamente donde estaban**. Ninguna intervención las roza. El ordenante, de hecho, sale **más** opaco (§8.2).

---

## 10. Tono (referencia v0: 4, 9, 23, 40)

Tres cosas van a favor y una en contra, y conviene decir las cuatro.

**A favor.** Primera: **el narrador de esta oleada no explica**. Mil doscientas palabras nuevas de trama, en la parte del libro donde la trama aprieta, sin un solo «porque». Segunda: **las dos intervenciones que podían haberse puesto sentimentales no lo hacen**. La cala de Mats acaba en una mano que tarda en soltar una credencial, no en una frase sobre lo que siente; el recuerdo de Tomas acaba en un carné puesto por delante, no en un juicio sobre lo que hizo. Tercera: **`31:153` es la mejor línea nueva de la oleada** — «Nadie lo negó.» — porque hace el trabajo de un párrafo de reacción en tres palabras y deja al lector el resto.

**En contra, y es lo que corrijo.** Los tres hallazgos de §8 apuntan todos en la misma dirección: **la oleada tiende a decir dos veces lo que ya ha dicho una** (el gesto de los dos dedos, la ausencia de nombre, el «No preguntó»). Ninguna de las tres repeticiones es grave por sí sola y ninguna toca la Carta; juntas son el modo en que un manuscrito revisado empieza a sonar a revisado. Se arreglan con doce palabras.

**Y una observación sobre el hallazgo de M5 que A0 me pasa.** Que 17 de 47 capítulos midieran tramos secos atravesando los cambios de escena me importa más de lo que parece, porque varias de mis condiciones de énfasis se apoyan en dónde caen los cortes de escena. Reviso a la luz de `max_tramo_escena`: **las dos condiciones de tampón que puse siguen siendo correctas** —«La consola exterior cambió de estado una vez más.» separa la caída de `S35-cierre` **dentro de la misma escena**, y «Esperó.» cierra la escena 6 del 34 **como escena**, no como tramo—. Ninguna de mis prohibiciones dependía del artefacto. Lo dejo anotado por si en W6 alguien invoca el número viejo.

---

## 11. Veredicto

# APROBADO CON CORRECCIONES

**Sin veto.** Las trece condiciones de `OT-40` I-1, las seis de `OT-35` I-1 (forma), P-43, P-44, P-45, P-46, P-47, P-48, P-49, P-34/35/36/38 y las siete de la Carta F están verificadas sobre el texto final.

### Correcciones obligatorias antes del merge (tres de texto, dos de documento)

| # | dónde | qué | coste |
|:-:|---|---|---:|
| **1** | `capitulos/cap-35.md:273` | **Como máximo un dato de postura, y no el codo.** Preferida: «Jessie cayó de lado entre los bancos. No se hizo daño.» | −11 |
| **2** | `capitulos/cap-24.md:105` | Sustituir «Apoyó dos dedos sobre el sello y los mantuvo allí» por un gesto **sin «dos dedos»** (p. ej. «Mantuvo la mano abierta sobre el sello»). **`26:99` y `33:81` no se tocan.** Alternativa: revertir la recomposición M4b de `26:99` | ≈ −3 o 0 |
| **3** | `capitulos/cap-26.md:17` | Suprimir «**sin responsable**». La figura «no hay nombre» se dice una vez por capítulo | −2 |
| **4** | `informes/w5-plan.md` §10.5 n.º 6 | «**nueve** antepuestas» → **diez**. `OT-26` §9 ya las declara las diez; el plan no. **A8 no puede verificar contra el número mal** | 0 |
| **5** | `informes/w5-plan.md` §10.1 y hoja de A8 | **P-41 pasa a «cero coocurrencias NUEVAS»** con la redacción literal de §3 de este informe; y **P-44 cond. 7 se cuenta por locus, no por ocurrencia**, con la redacción de §2.1 | 0 |

### Pendiente, y bloquea mi firma de la oleada (no el merge de lo demás)

**`OT-40` I-4 no está ejecutada.** Cuando A4 permute los dos párrafos del cierre del naust, **quiero el diff**: es una operación que cambia dónde cierra una escena del capítulo 40, a dos párrafos de `S40-despedida`, y W4-R enseñó que eso no se da por inocuo. Si A0 decide cancelarla, basta con decírmelo por escrito.

### Correcciones al parte de verificaciones que A0 me dio

- «`sensibilidad.sh --solo` **sin hits nuevos atribuibles al diff**» no es exacto: hay **uno** en prosa nueva, «explica» (`34:269`). Leído y **descartado**. Los otros diez son artefactos de desplazamiento. Lo corrijo porque un parte que dice «cero» donde hay «uno inocuo» entrena a no mirar.
- La rama ya no es la del briefing: `10acd1b` añade `OT-35` I-4 y cinco `estado: en_oleada`. Manuscrito **80.275**.

### Condiciones nuevas, vinculantes hacia adelante

| # | alcance | prohibición |
|---|---|---|
| **P-50** | `cap-40` | **`40:81` («No preguntó qué había dicho Jean.») queda cerrado a modificación** en toda oleada, reserva y pasada de línea. Es el vecino de rima de la línea del cinturón y sostiene su lectura. Si se toca, la línea del cinturón se revierte con él |
| **P-51** | todo el proyecto | La figura **«sin nombre / sin autor / sin responsable / no identificaba»** queda cerrada en **doce loci**. Ninguna instancia nueva en W6, W7 ni reserva |
| **P-52** | `cap-31` | Cerrado a instancias nuevas de **clase A** (abstención), igual que el `cap-40` (P-45). Diez es el techo del capítulo |
| **P-53** | `cap-24` y todo material | **La operaria de I-1 no vuelve.** Nadie la nombra, la recuerda, le da nombre, le da desenlace ni la conecta con Jean. Si algo lo hace, deja de ser un hecho del pasado de Tomas y se convierte en parábola: se revierte |
| **P-54** | `cap-32` y toda OT futura con Mats | La cala de `32:187` **no crea precedente**. Ningún material posterior pone la enfermedad de Mats y la muerte de Jean en la misma frase, párrafo, escena o paralelismo, ni le da a Mats una línea que suene a «yo también sé lo que es que te borren». **VETO** |
| **P-55** | menores, todo material | **Ningún cuerpo de una menor recibe más de un dato de postura** en una acción de riesgo, y nunca dos datos ordenados seguidos de su resultado verificado: esa forma es una instrucción, y las instrucciones no se escriben sobre menores en este libro |

Siguen vigentes C-1…C-4, P-1…P-10 (W3), P-12…P-33 (W4), P-34…P-37 (W4-R) y P-38…P-49, que esta pasada no levanta.

Firmado, **A7** · 2026-08-18 · sobre `git diff main..10acd1b -- capitulos/` y el estado final de los siete capítulos.
