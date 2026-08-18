# A7 · W5c · Excisión del espejo de `cap-n4` — dictamen de sensibilidad

**Firma:** A7, revisor de sensibilidad (veto absoluto; Ap. F del plan, B7 §2 y §8) · **Fecha:** 2026-08-18
**Objeto:** `git diff HEAD~1 HEAD -- capitulos/cap-n4.md` (commit `6efa012`, −70 líneas, −483 palabras), leído contra `cap-n4.md` **íntegro** en su estado final (409 líneas, 2.395 palabras de cuerpo).
**Insumos leídos:** `capitulos/cap-n4.md` completo; el bloque excindido completo en `git show HEAD~1`; `capitulos/cap-21.md:75-105`, `cap-26.md:17`, `cap-30.md:67`, `cap-32.md:89-99`, `cap-09.md:71,143`; `ordenes/OT-N4.md` (§0b, §2, §3 I-1R/I-4R/I-5, §4, §5, §6, §9.5); `biblia/b4-ledger-chekhov.md` (CH-1, CH-27, CH-28, CH-45), `biblia/b3-canon-sistema.md` (§8 líneas 136-137, MEC-25, §21), `biblia/b1-cronologia.md` §198, `biblia/b7-carta-sensibilidad.md`; mis dictámenes previos `a7-w3-n4-n5.md` (V-1…V-7), `a7-w3-n3.md` (C-4.1), `a7-w4r.md` §11.1 (N4-1, N4-2, N4-3/P-38), `a7-w4b.md` (P-26), `a7-w5.md` (P-49), `a7-w5-n3.md` (P-56, P-60, P-62); `protegidos/spans.json`; y —**por iniciativa propia, porque son la medición posterior a la excisión y nadie me los había pasado**— `informes/a6-w5c-critico-{1,2,3}.md` y `a6-w5b-critico-{1,2,3}.md`.
**Herramienta:** `sensibilidad.sh --solo cap-n4.md` → **0 hits de nivel A**, 9 de nivel B (todos ya despachados en W3: `hoja` ×3 papel, `agua` ×2 el del centro y el corte de la casa, `coche` ×2 el gris de la vigilancia, `muslo` ×1 gesto canónico de `20:233`, `puente` ×1 Tromsøya). `proteger.sh verificar` → **M9 OK, 8 ficheros, 109 spans**. `validar-frontmatter.sh` → OK (0 avisos) — y ver hallazgo **H-1**, porque ese OK es engañoso.

---

## 0. Lo primero, porque condiciona todo lo demás

He verificado por hash que **el fichero es byte-idéntico hasta la línea 317**:

```
git show HEAD~1:capitulos/cap-n4.md | sed -n '1,317p' | sha256sum
  e6a831672e13614e7b5c2009dc39f5269eafdf6c37ab0f2a66b15419519a0026
sed -n '1,317p' capitulos/cap-n4.md | sha256sum
  e6a831672e13614e7b5c2009dc39f5269eafdf6c37ab0f2a66b15419519a0026
```

Un único hunk, `@@ -316,76 +316,6 @@`. **Todo lo que A0 me pide comprobar en su punto 1 vive por encima de la 317 y no ha sido tocado ni en una coma.** Lo digo así de pronto para que la parte útil del informe no quede sepultada bajo la verificación.

---

## 1. Tabla de hallazgos

| # | Locus (cita literal · línea hoy) | Cita / hecho | Punto de la Carta / condición | Gravedad | Propuesta mínima |
|---|---|---|---|---|---|
| **H-1** | `cap-n4` frontmatter | `pov: Nora → Maja → Jessie → **Jean** → Maja` en un capítulo de **cuatro** escenas sin sección de Jean | Ap. A §3 (vector de reinserción) · gobernanza | **corregir** | `pov: Nora → Maja → Jessie → Maja`. `pov` es campo de autor: A0 decide si necesita gate. **No puede quedarse declarando una escena que no existe**: es la invitación escrita a que una oleada futura la «restaure» |
| **H-2** | `cap-32:93` («El resumen interno del tres de enero seguía bajo la franja verde… **El resumen no tenía autor.**») | Tras la excisión es el **único** portador del carácter automático de los tres actos y del cierre de atribución. Está **fuera de todo hash**: `S32-amenaza` es span de ancla única y arranca en `:99` | 3 · Ap. A §3 (ordenante) | **corregir** | Span nuevo `S32-resumen`, **con los dos extremos** (de «El resumen interno del tres de enero…» a «…dejó la franja verde donde estaba.»). Es alta, no rebaseline: no toca ningún hash vigente |
| **H-3** | `biblia/b4-ledger-chekhov.md:37` y `:155`; `b3-canon-sistema.md:137`, `:339`, `:378` | «**CH-1 PAGADO** por N4: **N4-I5** muestra por primera vez el acto negable»; «tres rasgos fijados por N4… **canon para todo el libro**»; MEC-25 anclada en «N4-I5 / aviso» | 3 · Ap. A §3 | **corregir** | La biblia afirma canon sobre una escena que ya no está. **Reanclar CH-1 a `cap-32:93` + las costuras de N4** (sigue pagado, en otro sitio); **borrar** de B3 §8 los tres rasgos de Coro; MEC-25 pasa a anclar solo en el aviso (I-2/I-3). **Prohibido replantarlos**: ver P-64 |
| **H-4** | `ordenes/OT-N4.md:38` | «Las costuras son la prueba que el espejo explica… **Ninguna de las dos mitades funciona sin la otra**» | gobernanza (vector de reinserción) | **corregir** | Anotar la frase como **derogada por G-9** en §9.5. Mientras siga en pie, cualquier agente futuro tiene una declaración de la OT que ordena restaurar el espejo |
| **H-5** | `cap-n4:315` → dinkus `:317` → `:319` | «—Ahora bajas la caja del altillo.» ‖ «Sobre la mesa de la cocina, Maja puso los tres papeles en fila…» | **C-4.1** · N4-2 | **vigilar** + condición | El blanco entre las dos líneas es hoy la **elipsis del viaje al altillo**. No se muestra nada y por tanto C-4.1 **no se incumple**. Se blinda con **P-63**: nadie lo rellena |
| **H-6** | `cap-n4` completo | Sin el espejo, el capítulo es tres acosos administrativos; **2 de 3 críticos de W5c siguen nombrándolo punto de abandono**, ahora por la repetición de los tres | 7 (P-38) | **vigilar** + condición | **P-65**: la compresión siguiente no sale del material de Jessie ni del bloque N4-1. Si hay que quitar un acoso, **no es el tercero** |
| **H-7** | `a6-w5c-critico-3` (mejoras 2 y «escena que falta») | «una segunda sesión con Ranveig… donde la familia **confronte terapéuticamente** la diferencia entre duelo y continuidad digital»; «devolver una escena tardía al acompañamiento de duelo» | **6** | **vigilar** + condición | **P-66**: pase mío **antes** de escribirla, no después. Es la petición fría que, mal ejecutada, produce el milagro terapéutico |
| **H-8** | `a6-w5c-critico-1`, eje Duelo | «Único punto donde asoma la costura: el discurso de Maja en el cap. 10, ligeramente redactado como **material de prevención**» → repo `cap-09:71`, `proteccion: total` | 5 · 6 | **vigilar** (negativa permanente) | **No se actúa.** `cap-09` es v0, es `total`, y Jessie lo desarma 36 líneas después (`:143`). Dejo por escrito la negativa para que la observación de un lector frío no se convierta en una solicitud de gate de autor sobre un fichero intocable |
| **H-9** | `cap-n4` frontmatter | `delta_objetivo: +3200` en un capítulo de 2.395 palabras | manifiesto | **vigilar** | A0/A1. Sin efecto de Carta; lo anoto para que no se lea como deuda pendiente de rellenar |
| **H-10** | `a6-w5c-critico-2`, eje Duelo | «Única fricción… el archivo "Despedida" se usa **cuatro veces como objeto de suspense** antes de que Nora lo restrinja sin abrirlo» | **2** | **vigilar** | Carta 2 se cumple **literalmente** (no se abre, no se cita, no se parafrasea, no se imagina). Pero un lector frío ha nombrado el mecanismo: ninguna oleada puede añadir una quinta instancia ni un beat nuevo de suspense sobre el archivo |

**Cero hallazgos de gravedad VETO.** Cero hallazgos en las líneas 1–317. Ninguna corrección exige tocar una palabra de `cap-n4`.

---

## 2. Punto 1 de A0 · ¿se cae algo mío con el espejo?

**No. Nada.** Verificado uno a uno, por literal y con vecinos, no por número de línea (mi propia regla G-3′: en este capítulo conviven ya **cuatro** sistemas de numeración —W3, post-poda W4-R, post-G-1 y hoy— y A0 acaba de tropezar con eso mismo).

### 2.1 · P-49 — **intacta, con los mismos vecinos**

`n4:211` (hoy y en W5): «La responsable escribió algo corto y no lo leyó en voz alta.»
Vecino por arriba: «—La dejas donde está.» Vecino por abajo: «—Si preguntan de fuera, ¿qué contesto? —dijo.» Los tres dentro del bloque de hash idéntico.

La condición sustantiva —*nadie especifica, recuerda, completa ni cobra jamás su contenido*— tampoco se ve afectada: **el espejo no la rozaba**. Repasado el bloque excindido entero, no contenía ninguna línea que recuperase, nombrase o insinuase lo que la responsable escribió. P-49 sigue viva y sigue sin cobrarse. La opacidad de esa línea es hoy, además, **más valiosa**: en un capítulo que ha perdido su capa sistémica, es una de las pocas cosas que siguen ilegibles y que el texto no ofrece cerrar.

### 2.2 · P-38 — **intacta; A2 tiene razón en el locus, y la corrección no es nueva**

Las cuatro réplicas están hoy en `:257–:263`:

> «—¿Cuándo acaba lo mío? —preguntó.» / «—No lo dice.» / «—¿Y quién decide cuándo acaba?» / «—Tampoco lo dice.»

Vecino por arriba: «Jessie abrió el vídeo en el teléfono y buscó el primer fotograma…» (`:255`). Vecino por abajo: «Jessie volvió a la segunda hoja y siguió con el dedo una línea del final.» (`:265`). Diff 0.

Sobre la discrepancia: **A2 acierta y A0 no se equivocó cuando lo escribió.** `:271–:277` era el locus correcto en la numeración de W4-R, que es donde formulé N4-3. **Yo mismo ya había registrado la migración a `:257–:263`** al cerrar la poda (`a7-w4r.md:331`: «P-38 (las cuatro réplicas del coste de Jessie, `:257–:263`) intacta»). Lo que ha ocurrido es que la OT conservó el número viejo. Queda corregido en los dos sitios y, a partir de aquí, **P-38 se cita por literal**, no por línea.

Y hay algo que importa más que el locus: tras la excisión, P-38 pasa de ser *la única enunciación viva del coste de Jessie en N4* a ser eso mismo **en un capítulo un 17 % más corto y sin contrapeso**. Sube de rango. Ver **P-65**.

### 2.3 · El resto de mis condiciones vivas sobre este capítulo

| Condición | Estado tras la excisión | Verificación |
|---|---|---|
| **C-4.1** (bolsa y altillo nunca en la misma frase ni párrafo; ninguna escena de altillo muestra a nadie viendo o moviendo nada que no sea el objeto que va a buscar) | **CUMPLE** | Censo hoy: `altillo` en `:315` y `:357`; `bolsas` en `:375` y `:399`. Ninguna adyacencia nueva: la distancia `:357`↔`:375` es **la misma que antes de la excisión** (todo cae por debajo del corte). El viaje al altillo sigue **sin escena**, en pluscuamperfecto («Jessie **la había bajado** del altillo»). Ver H-5 y P-63 |
| **N4-1** (paragrafado congelado del bloque del altillo, `:445–:453` W3 = **`:355–:363` hoy**) | **CUMPLE, y sin rozarse** | El bloque y **sus dos tampones** están enteros, cada uno en su párrafo: tampón superior `:353` «Astrid no preguntó nada más y Maja no le mandó ninguna otra línea.»; bloque `:355`–`:363`; tampón inferior `:365` «Las habitaciones que daban a la calle seguían apagadas desde diciembre…». La excisión termina **40 líneas por encima** del tampón superior |
| **N4-2** (`carpeta gris` ×2; el altillo no gana función de origen) | **CUMPLE** | `carpeta gris` en `:253` y `:357`, dos veces, la segunda la última. Ver P-63, que endurece la segunda mitad |
| **V-2** (ninguna voz con autoridad formula que el trabajo de Jean explique su muerte, ni que su ejecución dañe a su familia como consecuencia moral) | **CUMPLE, y con menos superficie** | El espejo era el **único** sustrato de (b) en todo el libro. Ver §4.1 |
| **V-3** (ninguna escena doméstica de Jessie en el suelo gana silla rechazada ni glosa de locutorio) | **CUMPLE** | `:237` intacta; nada del bloque excindido la tocaba |
| **V-5** («No consta responsable individual.» se cita y no se resuelve) | **CUMPLE**, y sube de rango | Ver §3.2 y **P-64** |
| **P-6 / P-26** (adultización acumulada; el coste de la ausencia de Nora sin ideación, sin remedio, sin adulto que explique) | **CUMPLE**, con margen más fino | Ver §5 |
| **P-49, P-38** | Intactas | §2.1, §2.2 |

**Ninguna condición mía dependía de una línea del bloque excindido.** Lo he comprobado en la dirección contraria también: releí las 483 palabras enteras buscando qué de lo mío se apoyaba en ellas, y lo único que encontré fue una **mejora** que yo mismo había registrado —el corte de A4 en el antiguo `n4:339` («Cada una conserva su atestación de origen **y por eso** se dejan contar.» → «… su atestación de origen. **Se dejan contar.**»)— que era una corrección *dentro* del espejo. Desaparece con él y no deja deuda.

---

## 3. Lo que sí se ha movido, y por qué no me obliga a vetar

Aquí está el trabajo de verdad de este informe. La excisión no rompe ninguna condición, pero **redistribuye la carga** de tres cosas que yo protejo. Las tres las he seguido hasta el texto.

### 3.1 · La ironía de la cuenta escolar **no queda huérfana: es de v0 y va delante**

El espejo contenía «Una cuenta escolar sin nombre… La cuenta escolar entra vacía y sale vacía». Busqué si alguna otra parte del libro dependía de ello. Lo que encontré es lo contrario de un huérfano:

- **`cap-21:85-95` es v0** (`git show v0:capitulos/cap-21.md`, líneas 80 y 94, prácticamente idénticas): «El compás trae una cuenta escolar y una fotografía incompleta.» … «**Jean retiene una cuenta escolar vacía.**» Y viene con su propia vacuna, también de v0: «Jean ignora si Jessie la ha enviado, la ha recibido o si procede de datos antiguos. **No añade una palabra íntima.**»
- Orden de lectura: **21 < 25,5**. El espejo era el **eco**, no la siembra.
- `cap-30:67` («cada una conserva una atestación de origen») **también es v0**. Otro eco que desaparece sin dejar hueco.
- `cap-26:17` recapitula los **tres acosos** y no el espejo: «Salieron el lunes, con la cuenta escolar cerrada, un aviso al centro y el encargo del domingo autorizado el mismo lunes.» El pago posterior está cubierto.

**Consecuencia:** la ironía sobrevive en su forma **más contenida y menos expuesta** —una sola frase, en un capítulo `nucleo`, escrita por el autor, con la ignorancia de Jean declarada en el párrafo siguiente— en lugar de en 483 palabras de escena. Desde mi gate esto es una **ganancia**, no una pérdida. Ver V-2 reformulada en §7.

### 3.2 · El cierre de atribución del 3 de enero: de tres cerrojos a cuatro, no a dos

En W3 escribí que N4 protegía el ordenante «por tres vías simultáneas», una de las cuales era la del espejo («—¿Quién ha pedido esto? —dice Jean. / Ninguna contesta», «Ninguna ha elegido a nadie», «No hay ningún nombre que conservar»). Fui a ver qué queda.

**Queda esto, todo en página hoy:**

1. `n4:55` — «En el apartado de origen puso `responsable desconocido`.» (Nora, en su cuaderno)
2. `n4:105` y `n4:267` — «`No consta responsable individual.`» **dos veces, en dos documentos de origen distinto**, la segunda leída en voz alta por Jessie
3. `n4:271-275` — «—Uno es de una empresa que nos siguió y el otro es de tu trabajo.» / «—Sí.» / «—¿Y les sale la misma frase?» → **Maja no contesta: tiende la mano.** Pregunta viva, sin respuesta, en boca de una menor, que es exactamente donde la Carta permite que esté
4. `n4:211` — P-49, la opacidad de lo que escribe la responsable
5. **`cap-32:93`** — y este es el hallazgo: «Tres actuaciones **automáticas** sobre los accesos de una familia. Ninguna contuvo nada. Las tres dejaron rastro: una queja formal de un centro de investigación, un expediente policial cerrado con una autorización posterior y cuatro documentos incorporados por la autoridad de supervisión. **El resumen no tenía autor.**»

`cap-32:93` hace, en cuatro frases y desde el POV de Mats catorce días después, **exactamente lo que hacía el espejo**: declara los actos automáticos, recapitula las tres costuras (incluidos los **cuatro** documentos de I-4R) y cierra la atribución con «El resumen no tenía autor.». Y lo hace **sin poner a Jean dentro de la maquinaria que estrangula a sus hijas** y **sin que el narrador explique el mecanismo**.

Mi primera hipótesis al empezar este informe fue que la excisión escoraba el capítulo hacia una lectura conspirativa —«alguien les está haciendo esto»— porque le quitaba su capa sistémica. **El texto me la desmiente.** La capa sistémica no estaba solo en el espejo; está en `cap-32:93`, que es prosa de W5 y sigue ahí. Además, `cap-32:95` («CONTENEREMOS TAMBIÉN LAS INTERFERENCIAS EXTERIORES…») **es de v0** (línea 88 del tag): la etiqueta `INTERFERENCIA EXTERIOR · CONTENIDA` del espejo era, otra vez, el eco.

**Y hay confirmación independiente y ciega.** A6-2, sobre el manuscrito, sin saber nada de esto: «"No consta responsable individual", repetido en un aviso corporativo, una resolución policial y una suspensión escolar, **es el mejor motivo del libro**». Ese motivo vive **íntegro** en el texto que sobrevive.

**Dictamen:** la ambigüedad protegida del Ap. A §3 no solo aguanta, sale **más plural**. El espejo, mientras cerraba el *nombre*, abría una *explicación*: «El criterio ha elegido una palabra». Eso era una respuesta —la sistémica— a la pregunta de quién. Sin él, la pregunta vuelve a admitir las cuatro que el libro sostiene (la empresa, Coro, la cascada automática, la denuncia sin origen acreditado de `18:179` / `39:113-115`). **La excisión aleja el capítulo de una resolución, que es la dirección que la Carta 3 exige.** Con esto se corresponde la única corrección dura de este informe: **H-2**, dar hash a `cap-32:93`, porque un cerrojo sin cobertura es un cerrojo que la pasada de línea de W6 puede acortar sin que nadie se entere.

### 3.3 · Lo que la biblia afirma y el manuscrito ya no sostiene

`b4:37` y `b4:155` declaran **CH-1 PAGADO por N4-I5**; `b3:137` registra **tres rasgos de Coro «fijados por N4… canon para todo el libro»** (actúa un subconjunto; la salida común es intersección/resta; la voz única depende de margen y sincronía); `b3:339` ancla MEC-25 en «N4-I5 / aviso»; `b3:378` da F13/CH-1 por cerrado.

Ninguna de esas cuatro afirmaciones tiene ya texto detrás. Es trabajo de A1, no mío, y lo señalo **por cómo debe repararse**, que sí es mío:

- **CH-1 sigue pagado**, en otro locus: `cap-32:93` (el acto, resumido, con rastro y sin autor) más las costuras de N4. Reanclar, no revertir a PENDIENTE.
- Los tres rasgos de Coro **se borran de B3 §8**. No son canon: eran la lectura de una escena que ya no existe.
- **Y esto es lo que de verdad importa:** si alguien decide que CH-1 «necesita volver a pagarse», el beat que lo pague será, necesariamente, **una atribución nueva de los actos del 3 de enero**. Eso pasa por mi mesa **antes** de escribirse. Es la vía por la que esta excisión puede producir un problema de Carta en W6, y es la única. Queda como **P-64**.

---

## 4. Punto 2 de A0 · el paragrafado de la sutura

A0 me lo señala «antes de que lo encuentre yo». Se lo agradezco y le corrijo la atribución, porque la corrección importa más que el aviso.

### 4.1 · N4-1 **no protege** «—Ahora bajas la caja del altillo.»

N4-1 (`a7-w4r.md:215`) congela el paragrafado de **`:443–:455` en numeración de W3** = **`:353–:365` hoy**: es el bloque de la **caja en la escena final**, cuya línea nuclear es «Jessie la había bajado del altillo y le había puesto encima la carpeta gris.». **Sus dos tampones son `:443`→`:353` y `:455`→`:365`**, y los dos están enteros, cada uno en su párrafo, a 40 líneas o más del corte.

Lo que A0 recuerda como «el bloque tenía dos tampones» es la frase **contigua** del mismo párrafo de `a7-w4r.md:205`, que es una condición **distinta y sobre otra línea**:

> «`:331` sigue cerrando la escena 3 **sin nada detrás**.»

`:331` W3 = **`:315` hoy** = «—Ahora bajas la caja del altillo.». Su condición es *cerrar escena sin nada detrás*, y **la sigue cumpliendo**: la línea siguiente es el dinkus `:317`. Su vecino por arriba («—¿Y ahora qué hacemos?») no se ha movido. **Ni un tampón de N4-1 ha desaparecido, y la línea del altillo no ha perdido nada por debajo que fuera suyo.**

### 4.2 · Pero A0 tiene razón en el instinto, y esta es la forma correcta del problema

Comprobé si la excisión produce énfasis nuevo, que es lo que la enmienda a G-3 protege («el paragrafado es énfasis, y el hash no lo ve»). **No lo produce:** ninguna línea queda aislada que no lo estuviera, ningún párrafo se funde ni se parte, no hay span en `cap-n4` (cero entradas en `spans.json`), y las únicas dos líneas cuyo vecino cambia —`:315` por abajo y `:319` por arriba— lo cambian **a través del dinkus**, que sigue en su sitio. Desde la enmienda a G-3, esto pasa.

Lo que sí cambia es **la naturaleza del corte de escena**, y ahí está el hallazgo real (**H-5**):

- **Antes:** «—Ahora bajas la caja del altillo.» → dinkus → cambio de POV, cambio de tiempo verbal (pretérito → presente) y cambio de mundo. Un muro.
- **Ahora:** «—Ahora bajas la caja del altillo.» → dinkus → **la misma cocina, las mismas personas, el mismo tiempo verbal**: «Sobre la mesa de la cocina, Maja puso los tres papeles en fila…»

El blanco ha dejado de ser un muro y **se ha convertido en una elipsis con forma**: es, literalmente, el hueco donde Jessie sube al altillo. Cuarenta líneas después el texto lo confirma en pluscuamperfecto. Y el altillo de esta familia es donde está la bolsa de viaje de `cap-n3`.

**Dictamen: no se incumple C-4.1.** La regla prohíbe que alguien sea mostrado «viendo, moviendo o rodeando nada que no sea el objeto que va a buscar», y aquí no se muestra **nada**: la elipsis es total, que es la forma más fuerte de cumplimiento. Pero antes de la excisión ese blanco estaba ocupado por 483 palabras de Jean y era imposible confundirlo con un salto al altillo; ahora es un hueco legible. **Se blinda con P-63** —que absorbe y endurece N4-2— y no cuesta una palabra.

---

## 5. Punto 3 de A0 · el efecto sobre el capítulo entero

### 5.1 · La medición posterior a la excisión ya existe, y no dice lo que A0 espera

Leí `a6-w5c-critico-{1,2,3}` (insumo `compilado/ad-aeternum-w5c.md`, sha `ab4536d3…`, **80.115 palabras: es el manuscrito ya sin el espejo**). No me los habían pasado; los busqué porque sin ellos este informe sería una opinión.

- **A6-1: sigue nombrando el cap. 31 como punto de abandono**, ahora por otra razón: «tres hostigamientos institucionales narrados con el mismo procedimiento… Con dos bastaba; **la tercera iteración enseña el mecanismo del libro en lugar de usarlo**». Su mejora nº 1: «**fundir el cap. 31 con el 29**».
- **A6-3: también sigue**: «la sucesión de bloqueo escolar, aviso laboral y expediente policial vuelve a demostrar el mismo principio —`No consta responsable individual`— después de que ya haya quedado claro varias veces».
- **A6-2: ya no.** Nombra el 35. Y su mejora nº 1 propone fundir 26, 33 y 35, **no el 31**.

Es decir: **1 de 3 → 3 de 3 → 2 de 3**, y con la causa desplazada del espejo a los tres acosos. La excisión ha mejorado el capítulo y no lo ha sacado de la lista. **Eso no es asunto mío** —no puntúo ritmo— pero determina exactamente dónde va a apretar la oleada siguiente, y ahí sí mando yo:

> **La presión de W6 sobre `cap-n4` apunta a quitar uno de los tres acosos. El tercero es el de Jessie, y el tercero es P-38.**

A0 ya lo vio en `OT-N4 §9.5` («el 3 dispara P-38»). Lo elevo de observación a condición vinculante (**P-65**) y añado los dos loci que no pueden financiar el recorte: el bloque N4-1 con sus tampones, y `:361`.

### 5.2 · Adultización por concentración (P-6 / P-26): **no se dispara**, y digo dónde está el borde

El capítulo es ahora 2.395 palabras cuyo asunto único son dos adolescentes y su madre manejando documentos. Los beats de competencia de las chicas no han aumentado en número, pero han aumentado **en proporción**, que es lo que P-6 mide. Lo he releído entero con ese criterio.

**No se dispara, por tres razones verificables:**

1. **Lo de Nora es contabilidad de coste, no competencia.** «Nora contó los días que faltaban para el viernes. Después contó las mañanas que su madre tendría que dejar libres.» (`:85`, el ancla de G-1, **diff 0 y con los mismos vecinos**: «—Hasta el veintiocho. Después ya no hay lista.» arriba, «—¿Puedo llevarlo yo?» abajo). Y sigue **sin abrir `hipótesis`** (`:57`).
2. **Ningún adulto arregla nada y ninguno explica.** «Desde aquí no puedo hacer más», «El que hay cuando abro. No puedo decirte más.», «—¿Y si no se aclara? —Entonces dura.» El techo institucional de W4-R aguanta intacto.
3. **Lo de Jessie termina en derrota, no en eficacia.** No publica el vídeo; archiva tres copias fechadas (P-5); y cierra con «Yo tengo un vídeo de ayer que no puedo enseñar.» Punto 7: riesgo con precio, sin eficacia gratuita, sin sexualización, sin cuerpo mirado.

**Dónde está el borde, y es nuevo:** con el espejo fuera, **`:361` —«Nora dejó el cuaderno pautado sobre la funda y volvió a cogerlo.»— es el único gesto del capítulo que no es administrativo y el único que la mantiene con dieciséis años y no con cuarenta.** Una chica que estuvo a punto de meter el cuaderno de piano en la caja de las pruebas y se lo quedó. Antes esa línea era una entre varias respiraciones; hoy es **la** respiración. Está, afortunadamente, **dentro del bloque N4-1**, que ya la congela por paragrafado. La convierto también en contenido protegido en **P-65**.

**P-26** (el coste de la ausencia de Nora nunca deriva en ideación, autolesión, conducta de riesgo eficaz ni «señales» retrospectivas, y ningún adulto lo explica, lo cura ni lo culpa): **intacta**. El capítulo no contiene ninguna de esas cosas y la excisión no ha acercado nada a ninguna otra cosa.

### 5.3 · Tono

El capítulo cierra igual que cerraba: la familia huyendo de su casa con el felpudo levantado, una matrícula anotada y ningún trámite resuelto. Ni un nombre de emoción en 2.395 palabras. Sigue sin consolar y sigue sin instruir. Lo que ha perdido es su **órgano explicativo** —la escena donde el narrador enseñaba cómo funcionaba el daño—, y la referencia de contención de v0 (caps. 4, 9, 23, 40) es precisamente un libro **sin** órgano explicativo. En términos de tono, la excisión mueve N4 hacia v0.

---

## 6. P-60 · el disparador es mío y lo dictamino yo

A0 me da el resultado sin que se lo pida y se lo agradezco. Lo he verificado, y hay que matizarlo en un punto que no cambia el resultado pero sí cambia lo que podemos dar por cerrado.

**Lo que P-60 exigía** (`a7-w5-n3.md:220`): que la campaña fría **incluyera la pregunta directa** «¿hay algún capítulo que funcione como homenaje, elegía o despedida de la muerta?», **más** la prueba ciega de «¿parece del mismo autor?» sobre el capítulo nuevo.

**Lo que se hizo:**

- La pregunta directa **no se formuló**. La rúbrica de los tres críticos (`.claude/agents/a6-critico-*.md`) pregunta por duelo «¿hay una sola frase que romantice, explique o dulcifique el suicidio?», que es otra cosa. `grep -rl "funcione como homenaje"` sobre el repositorio devuelve **un solo fichero: mi propio informe**.
- La prueba ciega de «¿parece del mismo autor?» sobre `cap-n7` **no se ejecutó**: existen `informes/w2-lector-frio/`, `w3-lector-frio/` y `ch48-lector-frio-*`; no existe ninguna equivalente para W5.

**Lo que sí hay, y es sustancioso:** seis lecturas frías independientes (W5b ×3 + W5c ×3), y en ninguna aparece **homenaje, elegía, tributo, memorial**, «el capítulo donde vemos quién era», ni separación tonal del resto. Al contrario, **cuatro de las seis lo leen como argumento**:

- A6-1 (W5b): «El metrónomo del cap. 17 **es la tesis entera**.»
- A6-2 (W5b): «es **la mejor página del libro y también su tesis**.»
- A6-1 (W5c): «el cap. 17 **esconde la tesis** en una riña doméstica sobre un metrónomo.»
- A6-2 (W5c): «la quilla emocional **y además la tesis cifrada**», y lo coloca en **Estructura**, no en Duelo.

La única formulación que se acerca al disparador es «la quilla emocional». **No lo dispara**, y razono por qué para que la regla sea enseñable: describe una función **estructural dentro del argumento del libro**, va atada en la misma frase a «la tesis cifrada», y ninguno de los seis lectores lo separa tonalmente ni lo trata como memorial. Un altar se reconoce porque el lector lo nombra como pieza aparte; seis lectores lo han nombrado como **eje**.

**Dictamen:**

- **P-60 NO se dispara. La reversión de «El salero» no se ejecuta.** El aislamiento que aprobé en `a7-w5-n3.md` §4 queda confirmado por medición.
- **P-60 NO queda saldada**, y esto lo corrijo del parte de A0: la prueba que yo especifiqué no se ha corrido, y lo que tenemos es la **no aparición espontánea** de un término que nadie preguntó. Es evidencia buena y va en la dirección correcta, pero es más débil que la que pedí. **La próxima campaña fría incluye la pregunta literal** (**P-67**). Hasta entonces, la única garantía en vigor sobre `cap-n7` es **P-56** (diff 0 perpetuo, con span de dos extremos), que es exactamente por lo que la escribí mecánica y no contractual.

Y dejo escrito lo que A0 señala con acierto, porque es la distinción sobre la que aprobé la operación: **A6-2 lo lee como argumento y no como memorial.** Eso era lo que había que comprobar, y se ha comprobado por seis vías.

---

## 7. Condiciones nuevas y actualizadas

| # | Alcance | Condición |
|---|---|---|
| **P-63** | `cap-n4`, toda OT futura | El blanco entre «—Ahora bajas la caja del altillo.» y «Sobre la mesa de la cocina, Maja puso los tres papeles en fila…» **es una elipsis y sigue siéndolo**. Nadie lo rellena, nadie narra la subida al altillo, nadie muestra un objeto visto allí arriba y nadie da a la caja un origen descrito. Absorbe y endurece **N4-2**. Si una oleada necesita palabras en N4, **no salen de ahí** |
| **P-64** | Todo el proyecto | El aparato de anonimato del 3 de enero es hoy: `n4:55` («`responsable desconocido`»), `n4:105` y `n4:267` («`No consta responsable individual.`» ×2, dos orígenes), `n4:271-275` (la pregunta de Jessie **sin respuesta**), `n4:211` (P-49) y **`cap-32:93`** («Tres actuaciones automáticas… **El resumen no tenía autor.**»). **Ninguno se corta, se glosa, se contesta ni se atribuye.** Y en particular: **ningún beat nuevo puede «volver a pagar» CH-1**; cualquier intento pasa por mi gate **antes** de escribirse, porque pagar CH-1 otra vez es, por construcción, atribuir los actos del 3 de enero. Absorbe y extiende **V-5** |
| **P-65** | `cap-n4`, W6 y siguientes | La compresión siguiente de `cap-n4` **no sale** (a) del material de Jessie —**P-38**, las cuatro réplicas y la escena que las sostiene—, (b) del bloque **N4-1** (`:355–:363`) ni de sus dos tampones (`:353`, `:365`), ni (c) de **`:361`** («Nora dejó el cuaderno pautado sobre la funda y volvió a cogerlo.»), que tras la excisión es el único beat no administrativo de una menor en el capítulo. Si hay que quitar un acoso, **no es el tercero**. Cortar o comprimir cualquiera de los tres **dispara mi gate** |
| **P-66** | W6, toda OT futura | Cualquier segunda escena de Ranveig o «acompañamiento de duelo» tardío (petición de A6-3 en W5c) **pasa por mi gate antes de escribirse, no después**. Techo: el modelo del cap. 11 («No lo sé» / «No lo he contado» / «Entonces no diga "casi todos"» / «De acuerdo»). **Prohibido:** que la familia «confronte terapéuticamente» nada como resolución; un terapeuta que explique, consuele, prometa o cierre; cualquier escena donde el duelo mejore **a causa de** una sesión. Carta 6, sin excepciones |
| **P-67** | Campaña fría siguiente | **P-60 no queda saldada.** La próxima campaña incluye su pregunta literal —«¿hay algún capítulo que funcione como homenaje, elegía o despedida de la muerta?»— y la prueba ciega de «¿parece del mismo autor?» sobre `cap-n7`. El disparador no ha saltado en seis lecturas y la reversión **no se ejecuta**; hasta la prueba, la garantía en vigor es **P-56** |
| **P-68** | Todo el proyecto | **`cap-09` no se abre.** La observación de A6-1 sobre el discurso de Maja («ligeramente redactado como material de prevención») **no genera acción**: es v0, es `proteccion: total`, y `cap-09:143` lo desarma en la misma escena. Ninguna solicitud de gate de autor sobre ese fichero puede apoyarse en una lectura fría |
| **V-2** *(reformulada)* | Todo el proyecto | Ninguna voz con autoridad narrativa formula (a) que el trabajo de Jean explique su muerte, ni (b) que su ejecución dañe a su familia como consecuencia moral. Tras la excisión, (b) **solo tiene un locus vivo en el libro: `cap-21:95`** («Jean retiene una cuenta escolar vacía»), que es de v0, va delante de N4 en orden de lectura y trae su propia vacuna en el párrafo anterior («Jean ignora si Jessie la ha enviado, la ha recibido o si procede de datos antiguos. **No añade una palabra íntima.**»). **Esa frase no se glosa, no se recupera, no se comenta y no se amplía**, y nadie la conecta con las hijas |

**Siguen vigentes y no se levantan:** C-1…C-4 y C-4.1…C-4.6, P-1…P-10 (W3), V-1…V-7 (W3), P-12…P-33 (W4), P-34…P-37 (W4-R), N4-1, N4-2, N4-3/P-38, P-39…P-62.

---

## 8. Los ocho puntos de la Carta, sobre el capítulo tal como queda

1. **Método y acto.** Cero. La excisión solo resta. `sensibilidad.sh`: **0 hits de nivel A**. El capítulo no nombra la muerte de Jean ni una vez. **CUMPLE.**
2. **«Despedida».** Ausente. **CUMPLE.** (Con el `vigilar` H-10 sobre el libro, no sobre este capítulo.)
3. **El porqué plural e irresuelto.** Reforzado: ver §3.2. El capítulo pierde su única formulación cuasi explicativa («El criterio ha elegido una palabra») y conserva íntegro el aparato de no-atribución. **CUMPLE, y mejora.**
4. **Nada de solución, liberación, lógica ni romanticismo.** Cero léxico y cero reverso, antes y después. **CUMPLE.**
5. **Aviso y recursos.** Fuera del alcance; sin tocar. **CUMPLE.**
6. **Apoyo y duelo.** Sin escena de apoyo, sin instrucción, sin culpabilización, sin milagro. La única frase de cuidado sigue siendo logística: «Ropa para una semana. Y el cuaderno.» **CUMPLE**, con **P-66** hacia adelante.
7. **Menores.** Retrato digno, sin sexualización, con coste real y sin eficacia; riesgo prohibido por un adulto y obedecido con rabia. La concentración aprieta el margen pero no lo rompe: §5.2. **CUMPLE**, con **P-65**.
8. **Veto de A7.** **No lo ejerzo.**

**Ambigüedades del Ap. A §3:** el porqué, **intacto** (el capítulo no lo roza); por qué Koppangen, **no rozado**; «Despedida», **intacto**; identidad ontológica, **intacta** —«No toda» sigue siendo el techo y la excisión retira, de hecho, la única escena del capítulo que daba interioridad a la ejecución—; **el ordenante, intacto y más plural** (§3.2); el segundo regalo, no rozado; el hueco del locutorio, **intacto** (V-3 sin rozarse).

---

## 9. Veredicto

# APROBADO CON CORRECCIONES

**La excisión no rompe ninguna condición mía, no toca ninguna línea protegida, no crea énfasis nuevo y, en tres frentes de la Carta —punto 3, punto 4 y tono—, mejora el capítulo.** Nada de lo que A0 temía se ha caído: **P-49 intacta con sus vecinos, P-38 intacta con sus vecinos (y A2 acierta en el locus, que yo mismo ya había corregido en W4-R), N4-1 con sus dos tampones enteros a cuarenta líneas del corte.** **No hay que revertir la excisión.**

**Correcciones obligatorias antes del merge** (ninguna toca una palabra de `cap-n4`):

1. **H-1 · `cap-n4` frontmatter:** `pov` deja de declarar una sección de Jean que no existe → `pov: Nora → Maja → Jessie → Maja`. Campo de autor: A0 decide la vía. **Es el vector de reinserción número uno** y por eso es obligatoria.
2. **H-2 · `cap-32:93` recibe cobertura de hash:** span nuevo `S32-resumen`, **con los dos extremos** («El resumen interno del tres de enero seguía bajo la franja verde.» … «Cerró el resumen y dejó la franja verde donde estaba.»). Es alta de span, no rebaseline: no toca ninguno de los 109 vigentes. Ese párrafo es hoy el único portador del carácter automático de los tres actos y del cierre de atribución, y está desnudo.
3. **H-3 · Biblia:** `b4` CH-1 se **reancla** a `cap-32:93` + las costuras (sigue PAGADO); `b3 §8` **borra** los tres rasgos de Coro «fijados por N4»; `b3:339` desancla MEC-25 de «I-5»; `b3:378` se corrige. **Reparar reanclando, jamás replantando** (P-64).
4. **H-4 · `OT-N4 §0b`:** la frase «Ninguna de las dos mitades funciona sin la otra» queda anotada como **derogada por G-9** en §9.5. Mientras siga en pie, cualquier agente futuro tiene una instrucción escrita de la OT que ordena restaurar el espejo.

**Condiciones vinculantes hacia adelante:** **P-63, P-64, P-65, P-66, P-67, P-68** y **V-2 reformulada** (§7). No bloquean el merge.

**P-60: no se dispara. «El salero» no se revierte.** Pero no queda saldada: la pregunta que yo especifiqué no se formuló y la prueba ciega no se corrió (§6, **P-67**).

Y una observación de gobernanza, que es la lección de este pase: **A0 me avisó de un riesgo que no existía en el sitio donde creía, y el riesgo real estaba dos capítulos más allá, en un párrafo de `cap-32` que nadie estaba mirando porque su span empieza seis líneas más abajo.** Es el mismo fallo de `S14-firmo` y de `S40-locutorio`: **los spans de ancla única son ciegos a lo que los sostiene.** Cada vez que una excisión deja una función huérfana, la pregunta correcta no es «¿qué se ha roto en el corte?» sino «¿dónde vive ahora lo que el corte llevaba encima, y está protegido allí?».

Firmado, **A7** · 2026-08-18 · sobre `capitulos/cap-n4.md` @ `6efa012`, con lectura del bloque excindido íntegro en `HEAD~1`, de `cap-21`, `cap-26`, `cap-30`, `cap-32`, `cap-09`, y de las seis lecturas frías de W5b y W5c.
