# W4-R · Diagnóstico estructural del centro (Partes II–III)

**A2 · 2026-08-18 · rama `w4r-ritmo`.** Encargo de A0: diagnóstico, no redacción. **No se ha editado ningún capítulo.** Gemelo de `informes/w4r-diagnostico-cierre.md`. Este informe localiza texto, lo cuantifica y lo somete a decisión; no propone prosa de sustitución ni la escribe.

**Insumos leídos íntegros:** `capitulos/cap-11 … cap-30`, `cap-n2`, `cap-n3`, `cap-n4`, y `cap-n5` (como contraste); `ordenes/OT-13`, `OT-19`, `OT-22`, `OT-24`, `OT-26`, `OT-27`, `OT-28`, `OT-29`, `OT-30`, `OT-N2`, `OT-N4`, `RESERVA.md`, `tabla-5-1.json`; `informes/a6-w4r-critico-{1,2,3}.md`, `a6-w4r-deriva-v0.md`, `w4r-medicion-ritmo.md`, `w4r-instrumentos-ritmo.md`, `w4r-diagnostico-cierre.md`, `a5-w4r-continuidad.md`, `g-a2-gate.md`, `registro-gates-autor.md`, `m6b/m6-continuidades-w2.md`, `m8-w4r.json`; los informes A6 de **W2, W3 y W4** (para la §1); `protegidos/spans.json`; `biblia/b4-ledger.json`; `biblia/metadatos.json`. Perímetro vinculante de A7 recibido de A0 durante la redacción: incorporado en §3.1, §3.3, §5.5 y §6.4.

**Numeración.** Los críticos leen el compilado de 47 capítulos; el control de deriva lee v0 (41, numeración = fichero). Equivalencia en este bloque: **13=cap-11 · 14=12 · 15=cap-13 · 16=14 · 17=cap-15 · 18=16 · 19=cap-n2 · 20=cap-17 · 21=18 · 22=cap-19 · 23=20 · 24=cap-21 · 25=cap-22 · 26=cap-n3 · 27=cap-23 · 28=cap-24 · 29=cap-25 · 30=cap-n4 · 31=cap-26 · 32=cap-27 · 33=28 · 34=cap-29 · 35=cap-30.** Verificada contra once citas literales (la cadena `SPEIL → CORPUS JM` = 13; «No me fusiones» = 15; «Canela» = 17; el mural de 1STA = 19; «979,7 AÑOS-JM» = 22; «El cartón hacía más ruido» = 26; «No toda» = 27; el coche gris = 28; `RESUELTA SIN EFECTOS` = 29; «No consta responsable individual» = 30; «paso y uso» = 31).

**Recuentos.** Tokenizador canónico de `herramientas/lib/aa.py` (el mismo de M8) para todas las cifras; los desgloses por escena y por locus son exactos, no aproximados.

---

## 0. Confirmación de las cifras de A0, y la cifra que explica el centro

Las cuatro citas de A0 son exactas y los cuatro lectores apuntan al centro. Añado la medición que ninguna oleada ha hecho: **cuánto ha crecido cada parte.**

| parte | v0 | caps | hoy | caps | Δ | Δ % | media v0 | media hoy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| I · Mørketid | 15.599 | 10 | 19.925 | 12 | +4.326 | +28 % | 1.560 | 1.660 |
| II · Fije la vista | 15.855 | 10 | 18.928 | 11 | +3.073 | +19 % | 1.586 | 1.721 |
| **III · Propiedad intelectual** | **14.089** | 10 | **22.063** | 12 | **+7.974** | **+57 %** | **1.409** | **1.839** |
| IV · Soldagen | 17.207 | 11 | 18.936 | 12 | +1.729 | +10 % | 1.564 | 1.578 |
| **total** | **62.750** | 41 | **79.852** | 47 | +17.102 | +27 % | | |

**La Parte III era la más corta del libro y hoy es la más larga.** Creció el 57 %, dos veces la media del proyecto y casi seis veces lo que creció el bloque de cierre que acabamos de podar. El control de deriva —que lee v0, donde la Parte III mide 14.089— **ya decía que la Parte III se sienta**. Después le añadimos 7.974 palabras.

De ese crecimiento, **el 86 % son tres intervenciones nuestras y las tres caen en seis capítulos consecutivos**:

| | | Δ |
|---|---|---:|
| cap-n3 «Inventario» (orden 22,5) | capítulo nuevo, W3 | +2.824 |
| cap-25 «EDDA», coda R2 | reserva, W4 | +851 |
| cap-n4 «Interferencias» (orden 25,5) | capítulo nuevo, W3 | +3.156 |
| | **subtotal** | **+6.831** |
| los otros ocho capítulos de la Parte III | W2 + W4 | +1.143 |

El tramo de lectura **22 → N3 → 23 → 24 → 25 → N4 → 26** mide hoy **14.728 palabras**. En v0 el mismo tramo (22-23-24-25-26) medía **7.555**. Lo hemos duplicado, y es exactamente donde el crítico 1 abandona y donde el crítico 3 dice que «la reiteración probatoria prolonga demasiado el centro».

Dos cifras más que conviene tener delante:

- **cap-n4 (3.156) y cap-n3 (2.824) son los dos capítulos más largos del libro.** El tercero es cap-37 (2.234), a 590 palabras del segundo. Los dos primeros son nuestros y los dos están en la Parte III.
- **El manuscrito está hoy FUERA DE BANDA por abajo:** M8 79.844 contra una banda de 80.000–82.000 (`informes/m8-w4r.json`, `en_banda: false`). La poda del cierre lo sacó. Esto restringe el techo de cualquier poda del centro (§7.3) y obliga a gastar lo podado en algo; §4.4 dice en qué.

---

## 1. El dato que nadie ha tabulado: el historial de puntos de abandono

Cada hito pregunta a los tres críticos dónde estuvieron más cerca de abandonar. Nadie ha puesto las cuatro respuestas juntas. Puestas juntas dicen tres cosas, y una de ellas es un control positivo que el proyecto tiene y no ha usado.

| hito | A6-1 | A6-2 | A6-3 |
|---|---|---|---|
| **W2** (41 caps) | cap-24 «Accidente», primera mitad | cap-16 «La firma» | cap-30 «La asamblea» |
| **W3** (47) | cap-08 «Milisegundos» | **cap-n4** «Interferencias» | **cap-13** «Miles» |
| **W4** (47) | **cap-n3** «Inventario» | **cap-n3** «Inventario» | **cap-13** «Miles» |
| **W4-R** (47) | **cap-n4** «Interferencias» | **cap-13** «Miles» | **cap-13** «Miles» |
| **control v0** (41) | cap-30 «La asamblea»; «el primer aviso llega en el 13» | — | — |

**Uno.** De las trece nominaciones, **doce caen en Partes II–III**. La única que no (cap-08) está en la Parte I. **Ninguna, en ningún hito, en ningún crítico, en ninguna familia de modelos, ha caído nunca en el bloque de cierre.** Podamos 728 palabras de un bloque del que nadie se ha quejado jamás.

**Dos.** De las trece, **cuatro son capítulos que no existían en v0** (N4 ×2, N3 ×2). Cuatro de trece: casi un tercio de todos los puntos de abandono del proyecto los escribimos nosotros.

**Tres, y es lo que hay que usar: hay dos controles positivos.**

- **cap-30 «La asamblea»** fue el punto de abandono de A6-3 en W2 y **lo sigue siendo del control de v0 hoy**. Entre medias se reescribió en W2 (`OT-30`, +218 y −71 de recortes documentados). Desde entonces **ningún crítico del manuscrito vivo lo ha vuelto a nombrar**. El control de deriva, que lee la versión no reescrita, sí. Es una prueba pareada limpia: la reescritura de W2 sacó al 30 de la lista.
- **cap-n3 «Inventario»** fue el punto de abandono de **dos de tres** críticos en W4. Entre W4 y W4-R se podó −748 (commit `62d4d61`). En W4-R **nadie lo nombra**. A0 lo había archivado «para W6»; la poda ya lo resolvió sin que nadie lo registrara.

**Conclusión operativa: podar funciona, pero solo donde el lector se para.** El cierre no movió Ritmo porque allí no se paraba nadie. N3 salió de la lista en cuanto se podó. Y **cap-13 lleva tres hitos consecutivos siendo nombrado, y cap-n4 dos de cuatro**. Ahí es donde hay que trabajar, y son los dos casos que A0 pregunta.

**Un fallo de proceso que este historial destapa.** `OT-13` §6 fijó como criterio cualitativo: «A6 re-lectura W2: el 13 deja de ser "más cerca de abandonar"». En W2 pareció cumplirse (los tres nombraron 24, 16 y 30). En W3, W4 y W4-R el 13 vuelve, y ya lo nombran dos de tres. **El criterio ha fallado en tres mediciones seguidas y el proyecto no lo ha marcado como fallado en ningún gate.** Lo que ocurrió en W2 no fue una mejora del 13: fue que aquel jurado nombró otros capítulos.

---

## 2. El mapa de la reiteración probatoria (pregunta 1)

**Definición del movimiento**, para que se pueda contar: (a) la familia o un aliado sufre un daño concreto; (b) una institución lo mide, lo registra y lo consigna bien; (c) declara que no puede actuar —no es su competencia, no consta responsable, no hay umbral superado, no lo lleva el centro—; (d) nada cambia.

### 2.1 · Las catorce ejecuciones, en orden de lectura

| # | cap. | fecha | institución | ¿qué escala nueva? | veredicto |
|---:|---|---|---|---|---|
| 1 | **11** | 6-dic | EDDA / consejo de Armstrong | primera vez: la familia entra en el registro corporativo; la moratoria bilateral | **necesaria** |
| 2 | **16** a | 13-dic | UNN (Inger) | «UNN registra una actuación. No la origina.» | **necesaria** |
| 3 | **16** b | 15-dic | Seguridad de Fyret + policía | Jessie detenida; la advertencia notificada a la tutora legal | **necesaria** |
| 4 | **16** c | 15-dic | burofax de Armstrong | «Propiedad intelectual. Así la llaman» (título de la Parte III) | **necesaria** |
| 5 | **N2** | 16-dic | instituto | la única institución donde las hijas son sujeto y no objeto | **necesaria** |
| 6 | **18** | 17-dic | TKS (Astrid) | el regulador mide y no puede atribuir; y encarga («Tráigame algo reproducible») | **necesaria: convierte en misión** |
| 7 | **19** | 19-dic | NIDHOGG / contrato | «Ningún umbral acordado se ha superado» + 979,7 AÑOS-JM | **necesaria: es el horror** |
| 8 | **22** | 27-dic | la propia TKS (su director) | la institución del regulador bloquea al regulador | **necesaria** |
| 9 | **24** | 2-ene | policía | «O sea, que él se va y a mí me investigan» | **necesaria** |
| 10 | **N4** a | 3-ene | instituto (otra vez) | ninguna: reejecución de #5 con los mismos actores y los mismos objetos | **SOBRA COMO ESCENA DE ESE TIPO** (§3) |
| 11 | **N4** b | 3-ene | Framsenteret | sí: el aviso sin autor alcanza al empleador; única mecánica nueva del capítulo | **necesaria** |
| 12 | **N4** c | 3-ene | policía (otra vez) | la autorización llega **después** del hecho | **necesaria, y es la mejor de las tres** |
| 13 | **27** | 5-ene | consejo de Armstrong | apartamiento formal; y **gira a agencia** en la segunda escena | **necesaria** |
| 14 | **29** | 9-ene | tribunal + ministerio | el techo: la judicatura dice que no; y llega la cuenta atrás | **necesaria** |

(cap-30 «La asamblea» ejecuta el mismo movimiento **dentro**, con La Jardinera consolidada a mitad de frase. No lo cuento con los demás: cambia de registro, de sujeto y de mundo, y es lo que hace que el motivo signifique.)

### 2.2 · Lo que dice el mapa

**Catorce ejecuciones, y ninguna sobra por sí sola. Lo que sobra es la concentración.**

- **En v0 la Parte III ejecutaba el movimiento cuatro veces** (22, 24, 27, 29) repartidas en diez capítulos, con 23, 25, 26, 28 y 30 entre medias.
- **Hoy lo ejecuta siete veces en doce capítulos, y tres de las siete están dentro del mismo capítulo, N4.** La secuencia real que lee el lector es: **24 (policía, 2-ene) → N4 (instituto + trabajo + policía, 3-ene) → 27 (consejo, 5-ene) → 29 (tribunal, 9-ene)**. Cuatro derrotas institucionales consecutivas en siete días de tiempo narrativo, con solo tres capítulos que no lo son entre ellas.
- **El pico está en N4 y lo pusimos nosotros.** El control de deriva ya se quejaba de la versión con cuatro; lo hemos llevado a siete.

### 2.3 · Y el Chéjov pagado dos veces: sí, es culpa nuestra, y está por escrito

A0 sospecha bien. **`biblia/b4-ledger.json`, entrada CH-27, campo `resolucion`, literal:**

> `"resolucion": "N2«Instituto» (estigma de la cuenta suspendida) y N4 (re-suspensión «casual» de la cuenta restituida)"`

**Un plantado, dos capítulos nuevos, dos escenas completas.** Es la única entrada del ledger con dos capítulos nuevos en su resolución (verificado sobre las 83 entradas). Y el resultado es lo que dos críticos describen como «casi calcada en gestos y formularios»:

| beat | cap-n2 (16-dic) | cap-n4 (3-ene) |
|---|---|---|
| el mural | `:19` «En el mural del aula 214… El nombre de Nora se quedó gris entre veintisiete nombres blancos.» | `:17` «En el mural del aula 214, su nombre pasó de gris a blanco entre los otros veintisiete.» → `:43` «En el mural, su nombre volvió al gris.» |
| Mikkel | `:23` «Mikkel giró su terminal hacia el compañero de al lado.» | `:23` «Mikkel giró el terminal hacia el compañero de al lado.» → `:99` «Mikkel ya había vuelto a girar el terminal.» |
| **la tutora y las hojas** | `:31` «**La tutora apagó el mural desde el panel de la puerta**… **Salió al pasillo y volvió con dos hojas impresas, calientes todavía**…» | `:45` «**La tutora apagó el mural desde el panel de la puerta. Salió al pasillo y volvió con dos hojas impresas, todavía calientes**, como el dieciséis de diciembre.» |
| quién registra | `:37` «—La registro yo.» | `:47` «—La entrega la registro yo.» |
| el papel | `:59` «—En papel, mientras dure la revisión, **que no depende del centro**.» | `:79` «—Mientras dure, entregas en papel… **La revisión no la lleva el centro**.» |

**Veinte palabras consecutivas idénticas** entre `n2:31` y `n4:45`, y el propio texto lo señala con «como el dieciséis de diciembre». Cuando el capítulo tiene que decirle al lector que está repitiendo, el lector ya lo sabía.

**No hay un segundo caso de doble pago en W3.** He revisado las 83 entradas del ledger: CH-27 es la única con dos capítulos nuevos. Pero hay **dos ecos menores del mismo patrón**, y los dejo anotados porque nacen de la misma causa (asignar la misma deuda a dos sitios):

1. **CH-9 (la repesca) se paga en N4 y en 28 con el mismo beat.** `n4:93` «contó las mañanas que su madre tendría que dejar libres» ↔ `28:163` «—Te dejo las mañanas.» Cuatro días de distancia. `OT-28` §9 declara «Sin repetir la inscripción de N4» y aun así el gesto de las mañanas está en los dos. **No propongo tocarlo**: la línea de N4 está protegida por A7 (§3.1 b) y la de 28 es una réplica de Maja. Queda como constancia.
2. **La comprobación de cola** de `24:205` («Maja había revisado el aparcamiento… sin decir lo que buscaba») ↔ `n4:495` («Comprobó la calle en los dos sentidos antes de arrancar y no dijo lo que buscaba»). Casi verbatim. La versión de N4 es mejor (lleva el cartón de aparcamiento y la matrícula anotada). Se poda en 24, no en N4 (§5.4).

---

## 3. cap-n4 «Interferencias» (pregunta 2)

### 3.1 · Perímetro vinculante de A7 (recibido 2026-08-18, incorporado sin cambios)

Se transcribe aquí porque gobierna toda la hoja de poda de §3.3.

- **(a) El altillo.** `n4:331` («—Ahora bajas la caja del altillo.») y `n4:447-451` son el único otro sitio del libro donde alguien sube al altillo donde N3 dejó la bolsa, tres días de tiempo narrativo después; **C-4.1 está viva**. La escena **puede cortarse entera**; el inventario de la caja **puede comprimirse, pero no hasta que «Jessie la había bajado del altillo» encabece un párrafo o quede sola**. Nada nuevo sobre el altillo; ninguna réplica de respuesta a «—Ahora bajas la caja del altillo».
  → **Consecuencia en §3.3: `:445–:453` quedan a corte cero.** Ni una palabra. Y `:331` sigue cerrando la escena 3 sin nada detrás.
- **(b) Proporción es contenido.** En una poda cuyo criterio es «esto ya lo hizo N2», lo primero que parece redundante es la textura escolar-administrativa y lo que queda en pie es Nora resolviendo. **`n4:93` («Nora contó los días que faltaban para el viernes. Después contó las mañanas que su madre tendría que dejar libres») no se toca**: cortar eso y conservar la competencia administrativa **sube la adultización quitando palabras** (P-6, P-26).
  → **Consecuencia en §3.3:** la hoja de poda lleva una columna de lado. **De las 72 palabras que se cortan en la escena 1, 22 salen del lado de la competencia (`:57`, `:77`) y 50 del calco; ninguna del registro adolescente.** La proporción mejora, no empeora. Es un requisito de aceptación, no una nota.
- **(c) Si la desduplicación acaba cortando por el lado de N2, vuelve al gate de A7.** La mitad de Jessie de N2 tiene diff 0 y ahí vive el punto 7 del capítulo.
  → **Consecuencia: A2 no propone ni una palabra de corte en cap-n2**, y coincide con el fundamento (§8.1).
- **(P-36, sobre N3)** cortar una caja de la serie A–F, «El resto era ir», el treinta y uno subrayado o el hervidor dispara su gate; «la caja E entera» no es equivalente a los demás cortes.
  → **Consecuencia: N3 queda fuera del alcance de este diagnóstico** (§8.4). Se registra P-36 para que nadie lo toque en W6 sin pasar por A7. **La frase «la caja E entera no es equivalente» admite dos lecturas** (que ese corte esté permitido y sea distinto, o que esté prohibido por serlo): A0 debe pedir a A7 la desambiguación antes de que N3 entre en ninguna oleada. No la resuelvo por mi cuenta.

### 3.2 · Qué es lo que realmente falla en N4, y no es lo que dicen los críticos

El crítico 1 dice «tres acosos administrativos paralelos… todos construidos sobre la misma demostración». Tiene razón en el síntoma y se queda corto en la causa. La causa es medible:

**N4 descubre lo mismo entre siete y ocho veces en cinco secciones.**

| # | locus | quién lo descubre | qué |
|---:|---|---|---|
| 1 | `:57` | Nora | dos horas, dos referencias, «se separaban en el cuarto» |
| 2 | `:67` | Nora, en voz alta | «Han llegado los dos. Con seis minutos de diferencia y dos referencias distintas.» |
| 3 | `:187–:195` | Maja | la copia lleva otra referencia que la pantalla |
| 4 | `:279–:281` | Jessie, en voz alta | **la frase idéntica en dos expedientes** ← el pago |
| 5 | `:413` | el narrador | «En dos de ellos aparecía la misma frase. Cuatro palabras, en el mismo orden…» |
| 6 | `:433–:437` | Nora otra vez | «—Distinta. Se separan en el cuarto grupo.» (verbatim de #1) |
| 7 | `:457` | el narrador | la cámara y la autorización «no se contradecían» (cuarta vez tras `:251`, `:257`, `:259`) |

Y en paralelo, la fórmula «el documento no dice quién» se enuncia **ocho veces**: `:121`, `:125`, `:129`, `:133`, `:137`, `:201`, `:273`, `:277`.

**Esto no es un defecto de escritura de A3b: es lo que pedía la OT.** `OT-N4` §3 encargó **cuatro costuras** (I-1R, I-2R, I-3R, I-4R) y una quinta sección (I-4R b) para alinearlas. A3b las escribió las cuatro y las alineó. El diseño produce necesariamente que el mismo hallazgo se haga cuatro veces y se recapitule una quinta. **La responsable es la OT, y la firmé yo.**

**Y una cosa que hay que decir contra el crítico 3: la escena escolar de N4 no sobra como escena completa.** De sus 592 palabras, **unas 340 son contenido que no está en ninguna otra parte del libro**: la restitución con el álbum vacío (`:19`), las palabras idénticas a las del 5-dic (`:35`), la notificación doble con una línea de menos (`:55–:59`), «—El que hay cuando abro. No puedo decirte más.» (`:75`) y **la inscripción de marzo entera** (`:81–:101`), que paga CH-9 y prepara 28 y 40. El calco vale, medido, **unas 50 palabras**. Cortarlo no quita la sensación de calco, porque el calco no está en el número de palabras: **está en los objetos y en el orden.** El lector vuelve a entrar en el aula 214, con Mikkel, con la tutora, con el mural y con las dos hojas calientes. Eso solo se arregla cambiando el decorado, y eso ya no es poda (§3.4, G-1).

### 3.3 · HOJA DE PODA · cap-n4 — bloque para A7, léase suelto

> **Fichero:** `capitulos/cap-n4.md` · **estado_plan** N · **proteccion** no · **spans:** ninguno.
> **Recuento hoy:** 3.156. **Objetivo tras poda:** 2.857 (**−299**). **Techo:** −360.
> **Escena 4 (el espejo de Jean, `:335–:401`, 483 palabras): CORTE CERO.** Decisión D-1 del autor en G-A2 («se conserva y se vuelve a medir en W5»). Ningún crítico de esta ronda lo nombra. No se toca ni una coma, ni se reordena, ni se le cambia el paragrafado.
> **Rango `:445–:453`: CORTE CERO** por perímetro A7 (a). Incluye «Jessie la había bajado del altillo…» y el inventario de la caja.
> **Regla de lado (A7 b):** de las 72 palabras cortadas en la escena 1, **22 salen del lado de la competencia de Nora y 50 del calco; 0 del registro adolescente.** `n4:93` intacto y verbatim.
> **Regla de corte:** ninguna réplica se corta **salvo** que reenuncie literalmente algo que el lector ya tiene (solo un caso: `:437`, y no se ejecuta).

| # | locus | ≈pal | qué se va | corte | **cómo queda paragrafado lo de al lado** |
|---|---|---:|---|---:|---|
| C-1 | `:21` | 15 | «La tutora no apagó el mural al entrar. Pasó lista y dejó las entregas a la vista.» — párrafo que existe solo para negar `n2:31` | **−15** | `:19` (el álbum vacío, 3 frases) pasa a ir seguido de `:23` (Mikkel). Ninguno queda aislado; los dos ya eran párrafos multifrase o de acotación. |
| C-2 | `:45` | 28 | «La tutora apagó el mural desde el panel de la puerta. Salió al pasillo y volvió con dos hojas impresas, todavía calientes, **como el dieciséis de diciembre**.» → queda solo el hecho («La tutora volvió con dos hojas impresas.») | **−20** | El párrafo sigue existiendo, de una frase corta, entre `:43` («En el mural, su nombre volvió al gris.») y la réplica `:47`. `:43` ya era de una frase: **no cambia su aislamiento**. La supresión explícita de «como el dieciséis de diciembre» es obligatoria. |
| C-3 | `:57` | 75 | «Las comparó grupo por grupo, de izquierda a derecha: empezaban igual y **se separaban en el cuarto**.» → «Se separaban en el cuarto grupo.» (lado competencia) | **−13** | Párrafo de 5 frases → 4. No se toca su primera frase (el cuaderno del 5-dic) ni la última (`responsable desconocido`). |
| C-4 | `:77` | 9 | «Nora copió la respuesta en el cuaderno, entre comillas.» — **tercera** de cuatro acciones de cuaderno en la escena (`:57`, `:59`, `:77`, `:101`) (lado competencia) | **−9** | La réplica `:75` («—El que hay cuando abro. No puedo decirte más.») pasa a ir seguida de la réplica `:79`. Dos réplicas seguidas de hablantes distintos: paragrafado normal del libro. |
| C-5 | `:79` | 30 | «La revisión no la lleva el centro» — `n2:45` y `n2:59` ya lo dicen dos veces. Se conserva «—Mientras dure, entregas en papel —dijo la tutora—. Desde aquí no puedo hacer más.» | **−7** | La réplica se acorta; no cambia de posición ni de hablante. |
| C-6 | `:99` | 22 | «Mikkel ya había vuelto a girar el terminal.» Se **conserva** «Dos mesas más allá, alguien miró el mural y después a Nora, en ese orden» (registro adolescente) | **−8** | `:99` pasa de 2 frases a 1 (14 palabras). Queda entre la réplica `:97` y `:101`. Párrafo corto entre réplica y acción: forma habitual del libro (`n2:65`, `n4:53`). No se aísla ninguna línea protegida (N4 no tiene spans). |
| | | | **escena 1 · subtotal** | **−72** | de las cuales 22 del lado competencia, 50 del calco, 0 del registro adolescente |
| C-7 | `:141` | 12 | «Maja buscó dos veces la palabra "exposición" y no encontró de qué.» — reenuncia la réplica `:121` («—Exposición. No dice de qué.») | **−12** | `:139` (3 frases, el aviso sin hechos) pasa a ir seguido de `:143` («La responsable pasó a la segunda pantalla.»). `:143` ya era de una frase. **No se aísla nada nuevo.** |
| C-8 | `:233` | 18 | «En el marco había un cartel con un teléfono de mantenimiento y una fecha de revisión de octubre.» Se **conservan** el lector que rechaza dos veces, el piloto ámbar y `:235` («La misma credencial abrió la puerta de su despacho»), que es el contraste | **−18** | `:233` pasa de 3 frases a 2. `:235` sigue siendo de una frase, como ya era. |
| | | | **escena 2 · subtotal** | **−30** | *(Aviso: la escena 2 es 49 % diálogo y el resto es carga. No admite más. En particular `:183` —la frase larga de 47 palabras sobre la barca y la serie— **no se toca**: con «Maja pidió copia.» forma la construcción T5 «frase larga + golpe» que la propia OT autorizó, y cortarla deja el golpe huérfano.)* |
| C-9 | `:269` | 35 | «Aquel recibo le había costado dos horas en una sala con cuatro sillas atornilladas. Consignaba la duración y el número de incidencia. Nada más.» — retelling de `24:175`, que el lector leyó dos capítulos antes, y que `:251` ya ha invocado | **−35** | `:267` conserva su final («Era la del domingo.») y pasa a ir seguido de la réplica `:271`. Narración → réplica: transición normal. |
| C-10 | `:317` | 45 | «En la mesa había tres papeles del mismo día y un teléfono. Los papeles los había escrito gente que no aparecía en ellos. El vídeo lo había grabado ella, con la mano, a dos metros de un capó.» — el narrador enuncia la tesis que `:281` y `:295` ya dramatizan y que `:325` vuelve a decir mejor, en boca de Jessie | **−45** | `:315` («Jessie paró la reproducción antes del avance del coche.») ya era un párrafo de una frase y **sigue siéndolo**; pasa a ir seguido de `:319` (las tres copias). No queda entre dos blancos de forma nueva: ya lo estaba. |
| | | | **escena 3 · subtotal** | **−80** | `:331` («—Ahora bajas la caja del altillo.») sigue cerrando la escena, sin nada detrás (A7 a) |
| | | | **escena 4 · el espejo** | **0** | **D-1. Intacta.** |
| C-11 | `:413` | 45 | «En dos de ellos aparecía la misma frase. Cuatro palabras, en el mismo orden, con el mismo punto detrás. Maja la leyó en los dos sitios, una detrás de otra.» — **tercera** enunciación del hallazgo que Jessie ya lee en voz alta en `:281` | **−45** | `:411` («Tres formatos, tres tipos de letra, un solo día.») ya era un párrafo de una frase; pasa a ir seguido de `:415` (la fotografía). **Gana énfasis como última observación antes de la acción, que es el efecto buscado.** A7: no es línea protegida y no cambia de aislamiento, solo de vecino. |
| C-12 | `:431` | 22 | «Nora puso las dos notificaciones una encima de otra en la pantalla y bajó el brillo para que se leyeran las horas.» — se **conservan las tres réplicas** `:433`, `:435`, `:437`, aunque `:437` reenuncia `:57`: la escena 5 está en el 19 % de diálogo y no puede perder réplicas | **−22** | La réplica `:429` («—Enséñame las dos.») pasa a ir seguida de la réplica `:433`. Dos réplicas consecutivas de hablantes distintos. |
| C-13 | `:457` | 50 | «En la carpeta gris, una cámara municipal situaba el coche… no se contradecían.» — **cuarta** enunciación de «lo autorizan hoy, nos siguieron ayer» (`:251`, `:257`, `:259`) | **−50** | `:455` (las habitaciones apagadas y el telefonillo, 2 frases) pasa a ir seguido de `:459` («Maja marcó el número de Aslak desde el pasillo.»). El estado de la casa queda como causa inmediata de la llamada: mejora. `:459` ya era de una frase. |
| | | | **escena 5 · subtotal** | **−117** | `:445–:453` **corte cero** (A7 a). `:407` **corte cero**: «Sin sello. Sin firma. Sin dirección de vuelta.» necesita que los dos documentos anteriores tengan sello y número. `:493–:495` **corte cero**: es la versión buena de la comprobación de cola, y la que se poda es la de `24:205`. |
| | | | **TOTAL cap-n4** | **−299** | 3.156 → **2.857** |

**Interacción que A0 debe conocer antes de firmar nada: la poda y la reversión de D-1 no son independientes.** Si en W5 el autor decidiera revertir el espejo *después* de esta poda, N4 quedaría en **2.374**, por debajo del suelo de su propia banda de aceptación (`OT-N4` §6: 2.720–3.680). Las dos operaciones juntas obligan a reescribir la banda. Y la aritmética de `OT-N4` §6 ya está mal en el original: dice que revertir I-5 «devuelve el capítulo a 2.400», cuando I-5 mide 486 y la reversión da ≈2.670. Es el resto de R4 (las cuatro costuras, 300) lo que faltaría para llegar a 2.400.

### 3.4 · Lo que la poda no arregla, y la única intervención que sí (G-1)

Con −299, N4 deja de descubrir lo mismo siete veces (pasa a cuatro, cada una con distinto descubridor y distinto documento: Nora → Maja → **Jessie, el pago** → Maja alineándolos) y pierde los tres retellings de escenas ajenas. **Lo que no pierde es el aula 214.**

**G-1 · Reasignar la función de la escena 1 de N4.** Hoy su etiqueta es `TENSIÓN / PAGO` y su centro de gravedad es la re-suspensión: por eso es la ejecución n.º 10 del movimiento de §2.1 y por eso se lee como la n.º 5 otra vez. La escena tiene dentro otro centro de gravedad, mejor y ya escrito: **la inscripción de marzo** (`:81–:101`) — el trámite que ahora hay que hacer en papel, en persona, en horario de mañana, en la secretaría de Kongsbakken, antes del 28, y que cuesta las mañanas de trabajo de su madre.

- **Qué cambia:** la escena empieza donde termina (la notificación llega, con su duplicado y su cuaderno, sin volver a montar el ritual del mural) y se juega en la conversación con la tutora sobre lo que Nora tiene que hacer ahora. Fuera del aula 214, o dentro de ella sin volver a encenderla.
- **Qué NO cambia:** ni una palabra de `n4:93`; la notificación doble y sus dos referencias; el álbum vacío; las palabras idénticas a las del 5-dic; «—El que hay cuando abro. No puedo decirte más.»; la tutora enfriándose en un trámite y no en un desaire.
- **Efecto sobre §2.1:** la ejecución n.º 10 desaparece del mapa. La Parte III baja de siete ejecuciones a seis, y la que se va es la que dos críticos nombran.
- **Efecto sobre la etiqueta:** `TENSIÓN / PAGO` → `AGENCIA / INTERIORIDAD`. Es exactamente la dirección que A7 protege en (b): una cría de dieciséis años calculando lo que va a costarle a su madre, no una gestora de expedientes.
- **Coste:** **±0 palabras netas** (o −40 si se ejecuta junto con la poda). **A3b escribe el enlace; A4 pasa la línea; A7 lee antes de integrar.** No es poda: es la única intervención del centro que cambia lo que una escena *hace*.
- **Riesgo:** es la única propuesta de este informe que exige prosa nueva. Si A0 no quiere abrir escritura en esta oleada, **C-1…C-6 se ejecutan igual y el calco baja de cinco pares verbatim a uno**; pero el lector seguirá entrando dos veces en la misma aula.

**A2 la recomienda y la somete a gate.**

### 3.5 · Un fallo de continuidad vivo que nadie ha visto, y lo creamos en la poda anterior

`n4:29` dice: «Debajo del radiador **se había vuelto a formar** el charco con forma de bota.» Es una rima con N2 y es **la única imagen del mundo que tiene la escena**.

La poda de W4-R (`OT-N2` §9.2, commit `62d4d61`) **borró de N2 el primer término de la rima**: «Debajo del radiador se había formado un charco de nieve derretida con la forma de una bota.» Hoy la palabra «charco» no existe en cap-n2. **«Se había vuelto a formar» ya no remite a nada.**

`informes/a5-w4r-continuidad.md` cubrió N3 y N6 pero **no revisó N2**, aunque `62d4d61` estaba dentro de su diff. Es un hueco de la pasada, no un error de A5.

Dos arreglos, y el barato es el segundo:

- **A · restituir en N2** las 18 palabras del charco. Cuesta +18 y **toca N2, lo que activa el gate de A7 (c)** aunque sea para añadir, no para cortar. Ventaja: devuelve al aula de N2 su única imagen, que es lo que los críticos echan de menos en estos capítulos.
- **B · desactivar el huérfano en N4**, sin gate: `:29` «se había vuelto a formar» → «se había formado». **0 palabras.** A2 recomienda B, y deja A como opción si A0 quiere aprovechar el gate de G-1 para las dos cosas.

---

## 4. cap-13 «Miles» (pregunta 3)

### 4.1 · No hay preanuncio que quitar: el 13 es el original

A0 sospecha que 13 preanuncia lo que 17 y 21 hacen bien. **La respuesta es no, y ya está argumentada y aceptada en el proyecto.** `OT-13` §2, literal:

> «13 = presentar las voces, con un caso por voz… Es el ÚNICO capítulo donde las voces son nuevas: 15 no las re-presenta (15 = resquicio y 71-K), 17 no repite sus precedentes (17 = destino vacío y testimonio), 21 no repite su oferta como novedad… **Los recortes de "misma partida" van a 17 y 21, no a 13: 13 es el original.**»

Y se ejecutó: `OT-13` §5 mandó a OT-17 recortar los precedentes `AMENAZA INMINENTE` / `VIOLENCIA PROBABLE`, y a OT-21 tratar su `CEDER/CONSERVAR` como reprise. cap-17 mide hoy 844 palabras y cap-21, 736: son **los dos capítulos más cortos del libro después del 41**. Ya están podados hasta el hueso.

Lo que los críticos nombran no es duplicación. Es **coste de entrada**, y lo dicen con las mismas palabras los tres: «sin ancla exterior» (A6-2), «sin recuperar un cuerpo o un espacio estable» (A6-3), «sin ancla exterior» (control v0), «tres continuidades nuevas y **ninguna imagen**» (A6-2).

### 4.2 · La medición que lo confirma, y que es nueva

El tamaño del hueco por sí solo no explica nada: los capítulos de Jean son huecos por diseño. Lo que explica el defecto es **cuántas entidades nuevas cae dentro del hueco**.

| capítulo de Jean | pal. | anclas exteriores (imagen, no nombre) | mayor tramo sin ninguna | **entidades nuevas dentro del hueco** |
|---|---:|---|---:|---:|
| **cap-13** | 1.562 | **una**: `:65` (Nora, el metrónomo parado, el vaso de leche) | **1.122** (`:67–:277`) | **cuatro: Nieve, Cuchillo, la anónima, Coro** |
| cap-15 | 1.299 | dos: `:35` (las galletas en la cocina), `:41` (las teclas negras) | 1.081 | 0 |
| cap-17 | 844 | una: `:175` (a cuatro manos, el vaso sobre la nevera) | 707 | 0 |
| cap-21 | 736 | dos: `:41` (Telegrafbukta), `:139–:147` (la playa reconstruida) | 432 | 0 |
| cap-25 | 1.741 | una: `:273–:281`, y es la coda entera | 1.394 | 0 |
| cap-n5 | 1.822 | **tres**, y son casos de trabajo, no recuerdos | — | 0 |
| cap-30 | 1.571 | el capítulo entero ocurre en Telegrafbukta | — | 0 |

**cap-13 es el único capítulo de Jean del libro que presenta entidades nuevas dentro de un tramo sin ancla, y presenta cuatro.** La única ancla que tiene pertenece a la única voz que la recibe (Madre); Nieve, Cuchillo, la anónima y Coro entran las cuatro a oscuras. Después del recuerdo de `:65`, el exterior aparece tres veces como **nombre** (`:119` «—¿Recuerdas a Nora y Jessie?», `:127` Koppangen «queda fuera de la comparación», `:279` la línea protegida de Coro) y **ninguna como imagen**.

Eso también explica por qué nadie se queja de 15, 17, 21 ni 25 pese a tener huecos comparables: **en ellos el hueco no le pide nada al lector.** Es la diferencia entre pedir atención y pedir crédito, que es literalmente lo que dice el crítico 2: «El 15 pide crédito antes de haberlo ganado».

El contraste que el propio jurado ofrece: **cap-n5, al que el crítico 1 exculpa expresamente** («monótono a propósito y lo justifica con tres imágenes memorables»), tiene 1.822 palabras de trabajo abstracto y dentro: la uña negra del pulgar y el polvo de yeso hasta el codo; la media cuartilla pegada a la puerta con «Turno de noche» y tres nombres, dos tachados, y la punta de un zueco de goma; el cartón de una caja de mudanza tapando el panel de la lavadora. **Las tres son casos de trabajo, no recuerdos de familia.** El ancla exterior de un capítulo de Jean no tiene que venir de la casa: puede venir del caso.

Y aquí está la parte incómoda: **W2 le dio a cap-13 casos y no le dio imágenes.** `OT-13` I-4 encargó «la mujer que trabaja de noche en un almacén de congelados. Adjuntó tres enlaces y el horario de su turno» — enunciado, no visto. Y `OT-13` §9.1 L-3 dice, literal, que se cambió «capturas» por «enlaces» en el 13 **porque el 17 iba a quedarse con la imagen**: «se diferencia el del 13 porque el del 17 paga una imagen que depende de la captura (la lista de la compra pegada a la pantalla)». **Le dimos la imagen al capítulo de 844 palabras y la abstracción al capítulo donde el lector abandona.**

### 4.3 · El coste de tocar el reparto de 13, exacto

`herramientas/lib/m6_continuidades.py` mide **23 réplicas de atribución inequívoca**: Coro 7, Nieve 6, Madre 5, Cuchillo 5. Resultado vigente: **v0 73,2 % = W2 73,2 %** (seis pases por condición; `informes/m6b/m6-continuidades-w2.md`). El script **aborta si alguna réplica de la clave deja de existir en el capítulo**.

Reparto de la muestra por sección:

| sección de cap-13 | palabras | réplicas en la muestra |
|---|---:|---:|
| Madre (`:15–:79`) | 461 | 5 |
| Nieve (`:83–:165`) | 413 | 6 |
| Cuchillo (`:169–:213`) | 252 | 5 |
| **la anónima (`:217–:235`)** | **165** | **0** |
| Coro (`:239–:297`) | 271 | 7 |

Por tanto:

- **Fundir 13 con 15, como pide el crítico 2, invalida la medición por construcción.** Cualquier fusión mueve o suprime réplicas; el script aborta; la clave hay que rehacerla; y el nuevo 73,2 % **ya no sería comparable con el de v0**, porque no sería la misma muestra. Se perdería el único criterio cuantitativo de voces que el proyecto ha llegado a medir con control. Coste: seis pases por condición ×2 condiciones, y una baseline que deja de existir.
- **La única sección de 13 que puede tocarse sin rozar la muestra es la anónima** (165 palabras, 0 réplicas). Y está triplemente cerrada: `OT-13` §1 la declaró «considerado y descartado (gana el texto): la anónima es la bisagra de "No recibimos su estado" y de `:277`»; §4 la lista como línea intacta; y paga CH-15/CH-62.
- **Añadir narración a 13 no toca la muestra en absoluto.** Ninguna de las 23 réplicas se mueve; la medición se puede repetir idéntica y comparar con la baseline.

**Conclusión: no se corta 13, no se funde 13, y lo que 13 necesita se puede poner sin coste de medición.**

### 4.4 · Lo que sí hay que hacer con el 13, y es una rectificación mía

Lo que cap-13 pide es exactamente lo que **R5** estaba diseñada para dar: «micro-anclajes… en los capítulos T1 cuyo lector frío se quede… sin "dónde ocurre" (17, 21, 36 "no lo sé" en v0; **13 "sin lugar"**)» (`RESERVA.md` §R5). **cap-13 es el primer destino nombrado de R5.**

**R5 la cancelé yo,** en `w4r-diagnostico-cierre.md` §6.3.3, y A0 la ejecutó el 2026-08-18. Mi razón fue: «son micro-anclajes narrados y cuatro de sus seis destinos candidatos (15, 25, **37, 38**) están dentro o al borde del tramo seco». **Esa razón es correcta para 15, 25, 37 y 38, y es falsa para 13, 17 y 21**, que no están en el bloque de cierre y que ninguna medición de aquel informe cubría. Miré el destino equivocado de una partida que tenía dos mitades y la cancelé entera.

**Rectificación: reactivar R5 restringida a cap-13, +80…+120, y solo ahí.** Ni 17 ni 21 la necesitan (tienen sus anclas y son los dos capítulos más cortos del libro); 15, 25, 37 y 38 siguen canceladas por la razón original, que sigue siendo buena.

Tres posiciones, todas fuera de span y todas en narración:

| # | posición | qué | ≈pal |
|---|---|---|---:|
| A-1 | `:91` (Nieve) | las dos tomas del mismo blanco tienen **algo dentro**: un lugar, un objeto, un borde reconocible. Hoy son «una franja gris a la izquierda» y «la misma franja un poco más arriba»: no hay mundo | +30 |
| A-2 | `:177` (Cuchillo) | la mujer del almacén de congelados **se ve**: una imagen en lo que adjunta, del orden de la lista de la compra pegada a la pantalla de `17:61`. **17 conserva la suya**; no se repite el objeto | +25 |
| A-3 | `:219` (la anónima) | 165 palabras sin una sola imagen. Los cinco segmentos son **de algo**: un objeto o un sitio en la petición que el reinicio borra, para que «Ya no puede reconstruir qué esperaba aquella continuidad» tenga un referente perdido y no solo una estructura perdida | +40 |

**Prohibiciones (heredadas de `OT-13` §4, vigentes):** cero términos nuevos del lexicón (M1 ≤ 14,5; hoy 14,1 con 22 únicos, margen para 1); M2 = 0; ningún span tocado; la fórmula «Regla:» prohibida; ninguna de las 23 réplicas de la muestra modificada; nada de la casa ni del 26-nov (A7: `13:121` es el modelo de no aludir); ningún cierre-objeto nuevo.

**Escritor: A3a** (es prosa de Jean, no línea). **A4** después. **A5** verifica que la muestra M6-continuidades sigue intacta antes de que A8 la vuelva a correr.

---

## 5. Parte III: 22, 27, 29 y el coche gris de 24 (pregunta 4)

### 5.1 · Qué es v0 del autor y qué margen real hay

Los tres son **v0 del autor**, `estado_plan: E`, `proteccion: nucleo`, y los tres crecieron en W4: 22 (+342, de los cuales 81 son R3), 27 (+143), 29 (+170). Entre los tres suman **10 spans con hash**. **No propongo fusionar ninguno**: el proyecto no renumera hasta W7 y fundir capítulos del autor es una intervención de otro orden. Lo que hay es poda dentro, y es poca. La digo con la cifra en la mano para que A0 no espere de aquí lo que no hay.

### 5.2 · cap-22 «Auditoría» — techo −90, recomendado −70

Es el capítulo con **la mayor mancha de prosa continua del centro y la segunda del libro**: `:29–:39`, **286 palabras** en seis párrafos sin un solo respiro visual (solo cap-04, protegido, con 505, es peor). Su primer tercio es **91 % narración**.

| locus | ≈pal | qué | corte |
|---|---:|---|---:|
| `:31` | 105 | la especificación de la exportación. Se conservan el terminal segregado, la impresora de papel numerado (W4 la usa como objeto en `:79`), las 184 categorías, «El hombre le ofreció las actas de diseño. Astrid pidió el índice.» **Se va la seudonimización y la seguridad nacional** (dos frases, 50 palabras), que ningún capítulo cobra | **−50** |
| `:35` | 78 | «la **cuarta de las doce páginas** de la cadena» y «hasta la **recertificación**». Se conservan la regla CE-K entera (29 y 37 la cobran) y la preservación con hora e identificador | **−20** |

**Paragrafado:** `:31` pasa de 6 frases a 4 y `:35` de 4 a 3; los dos siguen siendo párrafos largos dentro de la misma mancha. **Ningún párrafo desaparece y ninguna línea queda aislada.** La mancha baja de 286 a **≈216**, por debajo de cap-27 y cap-19.

**Prohibido:** `S22-dahl` (`:51–57`), `S22-flecha` (`:159–161`), `S22-aula` (`:235`); la escena de Mats (`:77–:129`, 65 % diálogo); el caso de 2054 (`:173–:175`, es W4 I-1 y enlaza literalmente con `29:99/103`); el beat R3 del cuaderno (`:137`).

**Discrepancia plan↔plan que A0 debe resolver:** `OT-22` §6 declara «M5: tramo máx. sin diálogo ≤ 411 (**nada entre `:27` y `:49`**)», y `OT-22` §9 lo cumplió literalmente («411, idéntico a v0: nada insertado entre `:27` y `:49`»). **Esa cláusula se escribió como blindaje contra la expansión, no contra la poda.** Es el mismo caso que G-3 del informe del cierre y necesita el mismo registro por escrito antes de que A5 y A8 corran sus checklists.

### 5.3 · cap-27 «Apartada» — techo −80, recomendado −55

**El capítulo que el control de deriva agrupa con 22 y 29 es, en más de la mitad de su extensión, lo contrario de una derrota institucional.** Su escena 1 (`:15–:79`, 554) sí ejecuta el movimiento; su escena 2 (`:83–:167`, **1.106 palabras**) es el ladrillo fundacional, NORNA, R-1189 y «POR SI HACE FALTA» — la mayor victoria de agencia de la Parte III, y tres críticos la citan por su nombre. Agruparla con 22 y 29 es leer solo el principio.

Lo que hay dentro que sí se repite: **el corte de acceso a Alana se enuncia siete veces** — `:71` (la agenda vaciada), `:73` (la marca de agua), `:75` (EDDA), `:77` (el lector de azul a ámbar), `:95` (caduca al final de la jornada), `:123` (EDDA otra vez, a las diecinueve), `:213` (el torno en rojo, el cierre del capítulo). Pero **cinco de las siete están cerradas**:

- `:73` es `S27-conflicto`, span con hash;
- `:95` y `:123` son un par **diseñado en W4** (I-2 cambió `:89` de «dos veces» a «una vez» precisamente para que `:123` fuera la segunda);
- `:213` es el cierre y es el mejor;
- `:71` («A las cuatro, nada. Podía irse.») es contiguo a `:73`: **vaciarlo dejaría el span protegido en una posición distinta**, y eso es exactamente lo que A7 acaba de prohibir con la enmienda de G-3.

Queda esto, y no es mucho:

| locus | ≈pal | qué | corte | paragrafado |
|---|---:|---|---:|---|
| `:37` | 45 | el recitado de fundamentos: el control colegiado (ya en `19:261`) y la revisión independiente (ya en `11:157`, `19:165`). **Se conserva la última frase, que es el aguijón: «La petición de revisión externa no aparecía.»** | **−20** | párrafo de 4 frases → 2; sigue entre `:35` y `:39`, ninguno de una frase |
| `:47` | 22 | mecánica de consejo (la consejera ausente, la observación por escrito). **Se conserva «Dos miembros evitaban consultar sus tabletas»**, que es la imagen | **−12** | párrafo de 2 frases → 1 (12 palabras), entre dos réplicas. Forma habitual |
| `:117` | 40 | segundo recitado de la autenticación: «El ladrillo validó token, PIN, presencia y certificado…», que `:107–:109` acaba de narrar en escena | **−23** | párrafo de 2 frases → 1; queda entre dos líneas de registro. **Aviso: `:119` es una línea de registro sola; no se toca ni se le cambia el vecino de arriba más allá de esto** |

**Prohibido:** `S27-conflicto`, `S27-norna` (`:129–131`), `S27-por-si` (`:165`); toda la secuencia del ladrillo (`:103–:121` salvo el recitado de `:117`); la grabación (`:159–:167`); el encuentro con Astrid (`:171–:207`); `:213`.

### 5.4 · cap-29 «La poda» — techo −35, recomendado −20

**No hay nada que podar aquí y conviene decirlo.** cap-29 es **53,4 % diálogo** y su mancha máxima es **131**, por debajo de la mediana del libro (146). Es el capítulo más aireado del centro después de cap-14. Ejecuta la versión más alta del movimiento (el tribunal deniega, el ministerio presiona) y entrega la cuenta atrás del clímax.

Su única reiteración interna —la denegación se anuncia en `:87`, `:99`, `:171` y se resume en `:173`— **no se toca**: `:99` y `:171` son réplicas en dos escenas distintas separadas por una noche, y `:173` (Alana enumerando los argumentos de Armstrong sin haber estado en la sala) es **caracterización**, no repetición.

| locus | ≈pal | qué | corte | paragrafado |
|---|---:|---|---:|---|
| `:49` | 45 | el inventario del expediente («R-1189 acreditaba… Las once peticiones preservadas bajo CE-K, el informe de Gunnar, la sesión limitada de La Jardinera y la orden…»), que enumera lo que el lector ha visto reunir a lo largo de 22, 27 y 29 | **−20** | párrafo de 4 frases → 3. `:47` y `:51` sin cambio |

**Prohibido y por qué importa:** `:227` («la pantalla se llenó de más de tres mil filas… un comentario preguntaba cuántas debían conservarse») **es el antecedente sintáctico de `S29-cierre`** («Las necesarias.»). Vaciarlo dejaría el span colgando de nada: es el caso exacto que A7 acaba de tipificar. Tampoco `S29-orden` (`:23`), `S29-2054` (`:121`) ni `S29-durante` (`:225`), ni las cuatro réplicas nuevas de W4 en el pasillo ministerial.

### 5.5 · El coche gris de cap-24 — techo −50, recomendado −35

Aquí los dos críticos que piden borrarlo se equivocan de operación, y lo argumento en §8.2. Lo que sí sobra es una cosa, y es pequeña:

| locus | ≈pal | qué | corte | paragrafado |
|---|---:|---|---:|---|
| `:205` | 55 | «Maja había revisado el aparcamiento antes de abrirle la puerta, **sin decir lo que buscaba**. Ahora cambiaba de carril con tiempo y dejaba pasar dos semáforos en ámbar. Jessie observó cada par de faros que repetía un giro. Ninguno llegó al tercero.» — `n4:495` hace lo mismo casi verbatim («**no dijo lo que buscaba**») y con un objeto que esto no tiene (el cartón de aparcamiento, la matrícula anotada). **Se conserva «Al salir de la comisaría, el coche gris ya no estaba»** | **−35** | párrafo de 5 frases → 2. `:203` sin cambio; `:207` es réplica («—La próxima vez me llamas antes de bajarte»). **`:211` («Y mamá tenía enemigos») no cambia de vecino: sigue después de `:209`** |

**Prohibido:** `S24-once` (`:45`), `S24-cierre` (`:217`); todo `:131–:199` (es lo que N4 paga); `:211` verbatim, jamás glosado (A7).

**Discrepancia plan↔plan, la segunda:** `OT-24` §4 declara «líneas intactas… **toda la segunda mitad `:131–213`** (N4 la paga)» y `OT-N4` §5 se lo ordena («no tocar `24:131–213`»). Igual que en §5.2: **se escribió para impedir que 24 creciera mientras N4 se escribía, no para impedir que se pode.** Va al mismo registro por escrito.

### 5.6 · Y lo que la Parte III necesita de verdad no es podar: es no añadir

W5 pone **+500** en la Parte III (`OT-24` +300, `OT-26` +200). Revisadas una a una:

- **`OT-24` +300 (el pasado de Tomas): se ejecuta entera.** Es la única intervención pendiente del libro que **dos de cuatro lectores piden por su nombre** — «La bisagra frágil es Tomas Eide… se prepara en un solo capítulo» (A6-1) y «reinvertir ese espacio en sembrar a Tomas Eide dos veces antes del capítulo 24» (control v0). Se paga con las −35 del propio capítulo. Neto **+265**.
- **`OT-26` I-1 (+25), I-2 (+30), I-3 (+60): se ejecutan.** I-1 e I-2 son ripples obligatorios de N4; I-3 es la agenda propia de Aslak, que es **una de las dos escenas del test no-instrumental** que A7 vigila y que N6 cobra. Las tres son réplica o media réplica.
- **`OT-26` I-4 (textura del oficio antes de dormir, «opcional»): se cancela.** Es narración en el capítulo que ya lleva la mancha de `:183–:189` (183 palabras) y el segundo pico de subordinadas antepuestas del libro.
- **Nada más entra en la Parte III.** R3 beat 3 va al 40 (Parte IV) y no se toca.

**Parte III: +500 → +415**, de las cuales **~90 son réplica y todas están en el 26**. Las de `OT-24` son narración de Tomas, y ahí es lo correcto: el problema del 24 no es la densidad —su mancha es 197 y su diálogo, 22,3 %— sino que Tomas llega sin pasado. La guarda ya está puesta en la propia orden (`OT-24` §1: «ningún bloque narrativo continuo puede superar 197 palabras»), y con las −35 de §5.5 hay margen. **A0 debe hacerla explícita al lanzar W5**, porque es exactamente la regla que W4 se saltó en el 37 y el 38.

---

## 6. Qué NO se puede tocar

### 6.1 · Ficheros y spans con hash (M9)

- **`cap-20.md` y `cap-23.md`: `proteccion: total`.** Diff = 0. El hook `PreToolUse` los bloquea. cap-23 es «La canción» y contiene «No toda»: el techo de la ambigüedad ontológica.
- **57 de los 109 spans del libro están en Partes II–III.** Más de la mitad del presupuesto de protección del proyecto está aquí:

| cap. | spans |
|---|---|
| 11 | `S11-flashback` · `S11-consciencia` |
| 12 | `S12-temblor` · `S12-nidhogg` |
| 13 | `S13-madre` · `S13-nieve` · `S13-sufra` · `S13-yo-que-soy` · `S13-coro-nora` · `S13-crecer` |
| 14 | `S14-tranquilizar` · `S14-firmo` · `S14-cita` |
| 15 | `S15-intimas` · `S15-r1189` · `S15-objecion` |
| 16 | `S16-inger` · `S16-7c` · `S16-propiedad` |
| 17 | `S17-testigo` · `S17-nora` · `S17-71k` |
| 18 | `S18-dedos` · `S18-adelantado` · `S18-reproducible` · `S18-noticia` |
| 19 | `S19-palma` · `S19-gofre` · `S19-reflexiva` · `S19-anos-jm` · `S19-procesa` |
| 21 | `S21-inevitables` · `S21-notas` · `S21-portavoz` |
| 22 | `S22-flecha` · `S22-aula` · `S22-dahl` |
| 24 | `S24-once` · `S24-cierre` |
| 25 | `S25-utilidad` · `S25-escalada` · `S25-fecha` |
| 26 | `S26-paso-uso` · `S26-lata` · `S26-asociacion` · `S26-bocana` |
| 27 | `S27-conflicto` · `S27-norna` · `S27-por-si` |
| 28 | `S28-cierre` |
| 29 | `S29-cierre` · `S29-orden` · `S29-2054` · `S29-durante` |
| 30 | `S30-borrado` · `S30-apertura` · `S30-resultado` |
| **N2 · N3 · N4** | **ninguno** |

Los tres capítulos nuevos del centro no tienen spans. Es la razón por la que la poda se concentra en N4 y no porque N4 sea peor.

### 6.2 · La enmienda de A7 a G-3, aplicada a todo este mapa

> **Vaciar el párrafo vecino de una línea protegida cuenta como modificarla; el paragrafado es énfasis.** Prohíbe que una línea *quede* aislada por un corte vecino; no toca las que ya se autorizaron aisladas.

A7 la derivó de `n3:321` («La chapa de la puerta del garaje seguía abollada hacia fuera, a la altura de una mano»), que la poda del cierre no tocó pero dejó sola entre dos blancos — en este libro, la posición de «No lo había.» (`n3:73`) y «El resto era ir.» (`n3:325`). Cambió de función sin cambiar un carácter y el hash estaba intacto.

**Está aplicada en la columna «cómo queda paragrafado» de §3.3, §5.2, §5.3, §5.4 y §5.5.** Tres cortes de este informe se han **retirado** por esa regla y quedan documentados para que nadie los proponga otra vez:

1. `n4:407` (la descripción de los tres documentos): «Sin sello. Sin firma. Sin dirección de vuelta.» necesita que los dos anteriores tengan sello y número.
2. `27:71` (la agenda vaciada): es contiguo a `S27-conflicto`.
3. `29:227` (el anexo proyectado): es el antecedente de `S29-cierre` («Las necesarias.»).

Y una cuarta se ha reducido: `n4:183` no se toca porque con «Maja pidió copia.» forma la construcción T5 «frase larga + golpe» que la propia `OT-N4` autorizó.

### 6.3 · Ambigüedades del Ap. A §3 presentes en el centro

Quién ordenó el sabotaje (`24:79`: «El rastro no identificaba al ejecutor ni al ordenante ni contenía firma de Armstrong»); qué sabe Cuchillo (`13:201`); la consciencia residual (`S11-consciencia`); la denuncia anónima del 17-dic; **«No toda» como techo**. Ningún corte puede resolverlas y ninguna sutura puede insinuar un autor humano detrás de los avisos de N4: la villanía sigue siendo sistémica.

### 6.4 · Carta F y prohibiciones de A7 que muerden aquí

Además del perímetro de §3.1: los menores (Jessie no gana ni publica; el hallazgo no la ayuda ni la protege); «Y mamá tenía enemigos» (`24:211`) nunca repetido ni glosado como hipótesis de causa; ningún aviso con causa, método o lugar; ninguna alusión al acto; `Despedida` no se abre; **C-4 y C-4.1**: la bolsa de viaje y la hoja de efectos personales no reaparecen en ningún soporte, y el altillo de N4 es su único vecino (§3.1 a).

---

## 7. Tabla de cortes propuestos

### 7.1 · Sin gate de autor (A0 decide; A4 ejecuta)

| cap. | palabras | **techo** | **recomendado** | qué se va |
|---|---:|---:|---:|---|
| **n4** | 3.156 | −360 | **−299** | 3 retellings de escenas ajenas + 3 de las 7 enunciaciones del hallazgo + 5 pares de calco con N2 (§3.3) |
| **22** | 1.791 | −90 | **−70** | especificación administrativa dentro de la mancha de 286 |
| **27** | 1.929 | −80 | **−55** | recitado de fundamentos y segunda autenticación del ladrillo |
| **24** | 1.665 | −50 | **−35** | la comprobación de cola que `n4:495` hace mejor |
| **29** | 1.438 | −35 | **−20** | el inventario del expediente |
| n2 | 1.687 | **0** | **0** | perímetro A7 (c) y §8.1 |
| n3 | 2.824 | **0** | **0** | P-36; fuera de alcance (§8.4) |
| 13 | 1.562 | **0** | **0** | §4.3: no se corta, se ancla |
| 20 · 23 | — | **0** | **0** | `proteccion: total` |
| | | **−615** | **−479** | |

### 7.2 · Con gate

| # | qué | Δ palabras | quién |
|---|---|---:|---|
| **G-1** | Reasignar la función de la escena 1 de N4 (§3.4): sacarla del ritual del aula 214 y ponerle el centro de gravedad en la inscripción de marzo. Etiqueta `TENSIÓN/PAGO` → `AGENCIA/INTERIORIDAD` | 0 … −40 | **autor** (cambia una escena aprobada en G-A2) |
| **G-2** | Reactivar **R5 restringida a cap-13** (§4.4): tres anclas exteriores, +80…+120 | **+80 … +120** | **autor** (R5 fue partida de G-A1 y A0 la canceló el 18-ago) |
| **G-3′** | Reinterpretar «tramo máx. ≤ 411, nada entre `:27` y `:49`» (`OT-22` §6) y «toda la segunda mitad `:131–213` intacta» (`OT-24` §4) como blindaje contra la **expansión**, no contra la poda | 0 | **A0**, por escrito antes de A5/A8 |
| **G-4** | Restituir el charco de nieve en `n2` (§3.5, opción A) — solo si A0 quiere abrir N2 | +18 | **autor + A7** |

### 7.3 · Ledger: el techo lo pone la banda, no el texto

Base: **79.844** (M8, `en_banda: false`, banda 80.000–82.000).

Reparto de lo que queda por añadir: **W5 = +1.500** (24 +300 · 26 +200 · **31 +200 · 32 +250** · 34 +250 · 35 +150 · 40 +150) **+ R3 beat 3 en 40 = +250**. De eso, 500 caen en la Parte III, 450 en la Parte IV fuera del bloque de cierre (31, 32) y 800 dentro del bloque de cierre, que `w4r-diagnostico-cierre.md` §6.2 recomienda redimensionar a ≈400.

| escenario | operación | total | |
|---|---|---:|---|
| A · poda recomendada, nada más | −479 | **79.365** | ❌ 635 por debajo de la banda |
| **B · poda + G-1 + G-2 + W5 centro redimensionada (+415) + 31/32 (+450) + cierre redimensionado (+400)** | −519 +120 +1.265 | **80.710** | ✅ margen 710 |
| C · poda + G-1 + G-2 + W5 íntegra (+1.500) + R3 (+450) | −519 +120 +1.950 | **81.395** | ✅ margen 605 |
| D · poda a techo (−615) + G-1 + G-2 + W5 íntegra + R3 | −655 +120 +1.950 | **81.259** | ✅ |

**Tres consecuencias.**

1. **El manuscrito ya está fuera de banda por abajo y solo puede volver a entrar añadiendo.** Cualquier poda del centro que no vaya acompañada de W5 deja el libro más lejos del objetivo del autor, no más cerca.
2. **El techo de la poda del centro no es literario, es aritmético: ≈1.230 palabras con el pipeline redimensionado, ≈1.910 con W5 y R3 íntegras.** Mi recomendación (−479) está muy por debajo de los dos. No es timidez: es que **no hay más reiteración que cortar sin cortar réplica o material que se cobra.** Lo digo con la cifra porque el crítico 3 pide «entre un 10 % y un 15 % del bloque central» = 4.100–6.150 palabras, y eso **no es alcanzable por poda y A2 no recomienda intentarlo** (§8.3).
3. **La poda del centro paga R5 en el 13.** Es la mejor conversión disponible del proyecto: −479 de reiteración probatoria a cambio de +120 de mundo en el capítulo que tres hitos seguidos nombran como punto de abandono.

---

## 8. Dónde creo que los críticos se equivocan (y donde acierto yo, poco)

### 8.1 · «Fundir el 19 en el 30» y «secundariamente, el 19» — se poda N4, no N2

Dos críticos de tres nombran cap-n2 como lo prescindible; el tercero nombra la escena de N4. **Tienen razón los tres sobre la duplicación y se equivocan dos sobre el lado.**

- **N2 llega primero.** Es la única vez en todo el libro que el instituto existe en escena, que las gemelas son sujeto y no objeto, y que el estigma tiene precio social. Paga CH-47, que en v0 no tenía escena.
- **El calco es de N4 y N4 lo confiesa**: «como el dieciséis de diciembre» (`n4:45`). El capítulo que señala su propia repetición es el que repite.
- **La mitad de Jessie de N2 tiene diff 0 tras la poda de W4-R** y ahí vive el punto 7 del capítulo: la frase que nunca se termina, «Ninguno llegó a pegar», el parte, «Nadie preguntó quién había empezado la frase». Es lo mejor que tiene el libro sobre adolescentes en duelo.
- Y hay un dato que el crítico 1 mismo aporta sin darse cuenta de a quién favorece: **el crítico de W3 acreditó la cadena del clímax citando «el expediente policial que le costó entrar en Fyret», que es material de N2** (`informes/g-a2-gate.md` §2).

**Que dos críticos abandonen en N4 es argumento para podar N4.** Coincide con el perímetro de A7 (c).

### 8.2 · «Eliminar la persecución del coche gris» y «la segunda mitad del 28 sobra» — no

El control de deriva y el crítico 2 piden lo mismo. El crítico 2 añade la razón que lo desarma él solo: «**el capítulo 30 rehace ese mismo compás… con más precisión y mayor rendimiento temático**». Compilado 30 es cap-n4. **Está pidiendo borrar el antecedente del capítulo que acaba de elogiar por hacerlo mejor.**

`24:131–:213` es lo que N4 cobra: la boya del 2-ene (`n4:105`), el vídeo de la matrícula (`n4:267`, `:297`), «una comprobación de exposición reputacional sin nombrar al autor del encargo» (`n4:113`), la resolución provisional y la investigación de Jessie (`n4:251`, `:305`), las dos horas de la comisaría (`n4:269`). Y es lo que hace inhabitable la casa (`26:15-17`), sin lo cual no hay «Casa prestada».

**El crítico tiene razón en el síntoma —dos capítulos hacen el mismo compás— y se equivoca en la causa. La causa no es que 24 sobre: es que N4 lo vuelve a contar en vez de darlo por leído.** Se arregla en N4 (C-9 y C-13), no en 24. En 24 solo se va la comprobación de cola, y por la misma razón: porque N4 la hace mejor.

### 8.3 · «Recortar entre un 10 % y un 15 % del bloque central» — no es alcanzable y no hay que fingir que sí

Partes II–III miden 40.991 palabras. El 10 % son 4.100. **Todo lo que puedo defender línea a línea son 479, y 615 a techo.** Para llegar a 4.100 habría que entrar en el 22, el 27 y el 29 podando escena, no reiteración; en N3, que A7 ha fenced con P-36; o en el 13, que no se toca. El crítico 3 percibe bien y dimensiona a ojo; el número no es una instrucción.

**Lo que sí baja el peso percibido del centro sin cortar 4.100 palabras es otra cosa, y es lo que este informe recomienda: quitar una de las siete ejecuciones del movimiento (G-1) y no añadir la octava.**

### 8.4 · «Fundir el 15 con el 17» — invalida la única medición de voces que tenemos

Argumentado en §4.3. Además, 13 (9-dic) y 15 (12-dic) no hacen lo mismo: 13 presenta y 15 usa. `OT-13` §2 lo fijó, `OT-15` lo ejecutó y los dos críticos que nombran a «Canela» como el capítulo más denso de la Parte II **enuncian su regla correctamente**, lo que significa que 15 funciona.

### 8.5 · cap-n3: por qué no está en mi tabla, y qué debe saber A0

N3 mide 2.824 palabras (el segundo capítulo más largo del libro) y es el 13 % de la Parte III. **Ningún crítico de esta ronda lo nombra** — y §1 explica por qué: fue el punto de abandono de **dos de tres** en W4 y se podó −748 antes de esta medición. La poda funcionó.

No lo toco por tres razones y una es de A7: (1) nadie lo nombra ahora; (2) su escena-recuerdo es R1, aprobada en gate y citada con elogio; (3) **P-36** fenced cuatro elementos suyos. Pero A0 debe saber la aritmética: **sin tocar N3, la Parte III no baja de ≈21.500 y seguirá siendo la parte más larga del libro por unas 1.500 palabras.** Si en W6 hace falta más, ahí están las palabras, y ahí está también la ambigüedad de P-36 que hay que pedirle a A7 antes (§3.1).

### 8.6 · Dos errores míos, que es lo que A0 ha pedido explícitamente

1. **Cancelé R5 mirando el destino equivocado.** §4.4. La partida tenía seis destinos; cuatro estaban en el bloque de cierre y mi argumento valía para esos cuatro; los otros dos (13, 17) están en la Parte II y el 13 es el capítulo más nombrado de la historia del proyecto. Cancelé la partida entera con un argumento que cubría dos tercios de ella.
2. **`OT-N4` §3 encargó cuatro costuras y una recapitulación, y eso produce necesariamente el defecto que dos críticos nombran.** No es un fallo de A3b, que ejecutó al carácter, ni de A4, ni de A7, que aprobó. Es un fallo de diseño de la orden, y la escribí yo. La poda de §3.3 es, literalmente, deshacer una tercera parte de lo que pedí.

Y una tercera cosa, que no es un error mío sino un hueco de proceso: **`OT-13` §6 lleva tres mediciones fallando y ningún gate lo ha registrado** (§1).

---

## 9. Criterios de aceptación medibles para la oleada del centro

| medida | hoy | objetivo de salida |
|---|---:|---|
| Parte III | 22.063 | **≤ 21.700** (poda) y **≤ 22.150** tras W5 |
| cap-n4 | 3.156 | **≤ 2.870** · con G-1, **≤ 2.830** |
| enunciaciones del hallazgo en cap-n4 (§3.2) | 7 | **≤ 4**, cada una con distinto descubridor y distinto documento |
| pares verbatim n2↔n4 (§2.3) | 5 | **0**; y «como el dieciséis de diciembre» borrado |
| ejecuciones del movimiento en la Parte III (§2.1) | 7 | **6** (solo con G-1) |
| réplicas perdidas en todo el centro | — | **0** (regla dura; C-12 la respeta a propósito) |
| proporción en la escena 1 de n4 (A7 b) | — | **≥ 30 % de las palabras cortadas salen del lado competencia; 0 del registro adolescente**; `n4:93` verbatim |
| mancha máx. cap-22 | 286 | **≤ 225** |
| mancha máx. del centro | 286 (cap-22) | **≤ 235**; ninguna nueva por encima de 200 |
| cap-13 · mayor tramo sin ancla exterior | **1.122** | **≤ 390** (solo con G-2: las tres anclas de §4.4 lo parten en 159 · 385 · 161 · 307) |
| cap-13 · entidades nuevas presentadas sin ancla | **4** | **0** |
| cap-13 · M6-continuidades | 73,2 % | **sin caída, con la muestra de 23 réplicas intacta** (A5 verifica antes de que A8 mida) |
| cap-13 · M1 | 14,1 (22 únicos) | **≤ 14,5 · 0 términos nuevos** |
| M2 en todo el centro | — | **0 mecánicas nuevas** |
| M4 cierres-objeto | — | **no sube en ninguno**; `n4` sigue en 0 |
| M4b antepuestas | cap-26 16,8 % | **no sube en ninguno**; 26 ≤ 8 % es trabajo de `OT-26`, no de esta poda |
| M7 | 0 | **0 errores**: calendario 16-dic → 2-ene → 3-ene → 5-ene → 9-ene; las dos horas de `n4` (11:40, 11:52, 11:58); el 28 y el viernes de la inscripción; el domingo del coche gris |
| M9 | 109 spans | **109 · 0 fallos** · y **A8 verifica el paragrafado de los vecinos** de `S27-conflicto`, `S29-cierre`, `S24-cierre`, `S22-aula` (enmienda §6.2) |
| M10 | — | **ningún pago huérfano**: CH-27, CH-28, CH-45, CH-9, CH-1, CH-5, CH-6, CH-15, CH-62 |
| M8 | 79.844 (fuera de banda) | **dentro de 80.000–82.000 al cerrar la oleada**, no en cada commit |
| continuidad | 1 huérfano vivo | **`n4:29` reparado** (§3.5) |
| A7 | perímetro emitido | **hoja de poda revisada ANTES de que A4 ejecute**; sin veto |
| A6 (hito W5) | ritmo 7,5 | **≥ 8,0**; y **ningún crítico nombra cap-13 ni cap-n4** como punto de abandono |

**El criterio que de verdad decide es el último**, y ahora sabemos que es alcanzable: es lo que ocurrió con cap-30 tras W2 y con cap-n3 tras la poda de W4-R (§1).

**Riesgo específico y ya conocido:** cortar narración sin lexicón **sube M1** en ocurrencias/1.000. En N4 el techo es 8,5 y hoy está holgado; en 22, 27 y 29 los cortes son de procedimiento **con** términos dentro, así que M1 baja o se mantiene. A8 lo verifica capítulo a capítulo con la decisión que A0 ya tomó para el cierre (G-6).

---

## 10. Decisiones que necesitan gate

| # | decisión | quién | A2 |
|---|---|---|---|
| **G-1** | **Reasignar la función de la escena 1 de cap-n4** (§3.4): fuera del ritual del aula 214, centro de gravedad en la inscripción de marzo, etiqueta `AGENCIA/INTERIORIDAD`. ±0 palabras. Es la única intervención del centro que elimina una de las siete ejecuciones del movimiento, y la única que responde de verdad a «casi calcada en gestos y formularios». Exige prosa nueva (A3b) y pase de A7 | **autor** | **la recomienda** |
| **G-2** | **Reactivar R5 restringida a cap-13** (+80…+120, tres anclas exteriores). Revoca parcialmente una cancelación mía del 18-ago que se apoyaba en evidencia del bloque de cierre y no cubría la Parte II. cap-13 es el capítulo más nombrado de la historia del proyecto y el que tiene el mayor hueco sin imagen del libro | **autor** | **la recomienda y reconoce el error** |
| **G-3′** | **Reinterpretar las listas «intactas» de `OT-22` §6 y `OT-24` §4** como blindaje contra la expansión, no contra la poda. Sin esto, A5 y A8 fallan la oleada por construcción. Extensión del G-3 del cierre | **A0**, por escrito | necesario |
| **G-4** | **Restituir el charco de nieve en `cap-n2`** (+18) en vez del arreglo de coste cero en N4 (§3.5). Toca N2, y A7 (c) dice que tocar N2 vuelve a su gate | **autor + A7** | opcional; recomienda la opción B (0 palabras) |
| **G-5** | **Desambiguar P-36**: «la caja E entera no es equivalente a los demás cortes» admite dos lecturas y N3 no puede entrar en ninguna oleada sin saber cuál (§3.1) | **A7**, a petición de A0 | necesario antes de W6 |
| **G-6** | **Registrar que `OT-13` §6 lleva tres mediciones fallando** («el 13 deja de ser punto de abandono») y decidir si el criterio se mantiene con G-2 o se retira | **A0** | mantener con G-2 |

**Y una decisión de orden, la misma que en el cierre y por la misma razón:** la poda va **antes** que W5 en la Parte III. `OT-24` I-1 e I-2 insertan en la escena 3, y `OT-26` I-1/I-2 dependen del contenido de N4; si W5 se ejecuta primero, cada corte posterior vuelve a pasar por A7 y por la auditoría adversarial.

---

## 11. Lo que A2 entregaría a continuación

**Cinco hojas de poda** —secciones §10 dentro de las OT existentes, no OT nuevas—, con locus exacto, presupuesto negativo, etiqueta de la función que se conserva, **columna de paragrafado del vecino** (enmienda §6.2), prohibición específica y checklist para A5/A7/A8: `OT-N4` (ya redactada en §3.3 en bloque suelto, tal como A7 lo pidió), `OT-22`, `OT-24`, `OT-27`, `OT-29`.

**Escritor: A4 en las cinco** (es supresión y sutura de línea). **A3b solo en N4** si se aprueba G-1, porque cambiar el centro de gravedad de una escena exige escribir su entrada y su costura. **A3a en cap-13** si se aprueba G-2: son tres anclas de prosa de Jean, no una pasada de línea.

**A7 lee la hoja de poda de N4 antes de que A4 toque el fichero** (protocolo que él mismo fija). **A5 verifica la muestra M6-continuidades de cap-13 intacta antes de que A8 mida**, y revisa cap-n2 en su diff, que es lo que faltó en la pasada anterior.

**Lo que A2 no entregaría:** ninguna propuesta sobre cap-n3 hasta que G-5 esté resuelta; ninguna sobre cap-n2; ninguna fusión de capítulos.
