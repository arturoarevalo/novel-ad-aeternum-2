# Panel de jueces · W10 iteración 0 · **JUEZ C** (el verificador)

**Mi encargo se distingue del de A y B: ellos juzgan el mérito de las propuestas; yo juzgo
primero si son verdad.** He recontado a mano, con `herramientas/lib/aa.py` sobre
`capitulos/`, todas las cifras en las que se apoya un veredicto. No he arbitrado entre dos
números citados: he medido. Lo que sigue está en tres bloques y en este orden —
**(0) lo que resiste el recuento, (0b) las cifras exactas cuyo argumento no se sigue,
(1..5) los cinco entregables** — porque puntuar antes de comprobar es lo que este proyecto
lleva once instrumentos rotos haciendo.

---

## 0 · El recuento canónico. Ninguna de las cifras de parte que circulan es la buena

**Método.** `aa.count_words` sobre el cuerpo de los 48 ficheros de `capitulos/`, sin
frontmatter, sin dinkus, sin líneas de título, sin cabeceras de parte y sin paratextos.
Es el recuento con el que se construyó la banda del manifiesto y coincide con `CLAUDE.md`.
Reproducible: el mismo total sale de `capitulos/` y de `compilado/ad-aeternum-vF.md`.

| | total | I | II | III | IV |
|---|---:|---:|---:|---:|---:|
| **canónico (mío)** | **79.794** | **19.925** | **20.337** | **20.158** | **19.374** |
| ángulo 3 | 80.459 | 20.002 | 20.461 | 20.316 | 19.680 |
| ángulo 4 | 80.324 | 20.002 | 20.461 | 20.316 | 19.545 |
| ángulo 1 | 80.459 | — | — | — | — |
| ángulo 2 | 80.279 | — | — | — | — |
| ángulo 5 | 80.704 | — | — | — | — |

**Los seis ángulos midieron sobre el compilado e incluyeron las líneas de título de
capítulo** (`## 40. Soldagen` = 2 palabras) **y, algunos, los dinkus**. La inflación es
sistemática y pequeña: entre **+0,4 % y +1,1 %**. No invalida ningún argumento comparativo,
y así lo hago constar. Pero las cifras absolutas que se citen hacia fuera tienen que ser
las canónicas.

### 0.1 · El metrónomo de partes: **verdadero, y más fuerte de lo que ninguno de los dos dijo**

Los ángulos 3 y 4 dan **tres percentajes distintos para lo mismo** (2,3 % y 1,1 %) y
ninguno es correcto:

- **Ángulo 3 se equivoca dentro de su propia tabla.** Dice «459 palabras de diferencia
  entre la mayor y la menor (2,3 %)». En su propia tabla la mayor es 20.461 y la menor
  19.680: **781**, no 459. 459 es la distancia entre las partes I y II. Se le olvidó su
  propia Parte IV.
- **Ángulo 4 acierta la magnitud** («916 palabras: el 1,1 % del texto»). Canónico: **963
  palabras**, **1,21 % del libro** y **4,97 % sobre el movimiento más corto**.

**Y he hecho la prueba que faltaba, porque «casi iguales» no significa nada sin un nulo.**
Test de permutación (20.000 repartos al azar de los mismos 48 capítulos en cuatro bloques
de doce):

| | rango (mayor − menor) |
|---|---:|
| observado | **963** |
| media al azar | 2.833 |
| percentil 5 del azar | 1.069 |
| **P(rango al azar ≤ observado)** | **0,037** |

**La igualdad de las cuatro partes no es una impresión ni un artefacto de recuento: es
tres veces más apretada que el azar, con p ≈ 0,04.** Éste es el hallazgo mejor sostenido
de toda la iteración 0, y los dos ángulos que lo encontraron lo describieron con cifras
equivocadas. Corregido, **se refuerza**.

### 0.2 · Lo que resiste el recuento, ángulo por ángulo

| medición | quien la hizo | canónico | veredicto |
|---|---|---|---|
| fronteras de parte 24,9 / 50,3 / 75,6 % | 4 | 24,97 / 50,46 / 75,72 % | ✅ |
| 97 dinkus, 145 escenas | 4 | **97 / 145** | ✅ exacto |
| escena media por parte 870/538/472/477 | 4 | **866/535/469/473** | ✅ |
| espina interior 12 caps, 21,2 %, 19 % más cortos | 4 | 16.933, **21,2 %**, **19,2 %** | ✅ |
| interior por parte 31,6/19,8/20,1/13,4 % | 4 | **31,7/19,7/20,1/13,3 %** | ✅ |
| serie documental 29–35 = 15,6 % | 4 | 12.466 = **15,62 %** | ✅ |
| cuenta atrás 58/46/27/6 exacta | 4 | **exacta** | ✅ |
| «Mørketid» aparece una sola vez, y es el título | 4 | **una, en `metadatos.json`** | ✅ |
| «Nadie tocó la quinta» 50,3 % → «Respondo con la quinta» 93,0 %, eje de 42,7 puntos | 5 | 50,46 % → 93,17 %, **42,71** | ✅ exacto |
| las 16 posiciones porcentuales del ángulo 5 | 5 | todas dentro de **0,2 puntos** | ✅ |
| aproximación 9,1 % · clímax 8,3 % · cola 6,8 % | 5 | **9,14 / 8,31 / 6,83 %** | ✅ |
| Nora: 0 / 1 / 10 / 0 menciones en 41–44 | 5 | **0 / 1 / 11 / 0** | ✅ |
| ocho bloques de corte, por cita literal | 3 | **los ocho localizados, ±0–6 palabras** | ✅ |
| letanía de los cuatro nombres: 2 instancias, caps 7 y 8 | 3 | **2: `cap-07:33`, `cap-08:281`** | ✅ |
| `CEDER/CONSERVAR`: 2 instancias, caps 15 y 25 | 3 | **2** | ✅ |
| 71-K sólo en caps 18 y 21 y nunca más | 2 | **sólo 18 y 21** | ✅ |
| primeras 50 pp. = caps 1–9, interior 43,2 % | 2 | 14.562, interior **43,3 %** | ✅ |
| «Auditorio» y «Cuchillo» no vuelven tras el cap. 44 | 6 | **última: cap-44** | ✅ |
| cap-15 presenta Madre/Nieve/Cuchillo/Coro en 1.778 palabras | 6 | **líneas 41 / 95 / 181 / 251** | ✅ |
| media 1.660, desviación 389 | 6 | **1.662,4** y **389,1** | ✅ |
| «CARIES» 26 apariciones, todas referidas | nota nueva de `estado.json` | **26**, y `cap-12:21` es pluscuamperfecto | ✅ |

**Nueve de cada diez cifras de este expediente resisten.** Es un nivel de honradez
instrumental alto y hay que decirlo antes de listar lo que falla.

### 0.3 · Lo que NO resiste

**(a) Ángulo 6 · tres de sus cuatro ilustraciones del metrónomo son falsas, y una se
contradice consigo misma en la misma página.**

| afirmación | canónico |
|---|---|
| «46 de los 48 caben entre 938 y 2.312» | **44 de 48.** Cuatro quedan por debajo de 938: caps 1 (746), 21 (929), 25 (736), 48 (704) |
| «Cap. 30, EDDA: 1.765 palabras… **está por debajo de la media**» | **1.741, y la media que él mismo declara es 1.660.** Está **por encima**, con sus cifras y con las mías |
| «Cap. 43: 2.244 palabras repartidas en **tres bloques de unas 750**» | **2.234 en cuatro escenas: 634 / 375 / 427 / 798** |
| «el clímax tiene **menos tiempo continuo** que la visita al instituto del cap. 20» | **falso en las dos lecturas posibles**: capítulo 2.234 > 1.687; escena más larga 798 > 507 |
| «Cap. 46: 1.620 palabras para **dos escenas**» | 1.610 en **cuatro** escenas (785/207/373/245) |
| «cap. 35 mete cinco escenas en 1.428» | **cinco escenas, 1.416** ✅ única verificada |
| intercuartil 1.450–1.880 | 1.482–1.864 ✅ |

Y `informes/w10/estado.json` propagó la primera de esas cifras con la etiqueta
**«VERIFICADO»**. No lo estaba. **Corríjase la nota.**

**Ahora bien: la tesis de fondo del ángulo 6 sobrevive, y en forma más afilada que la
suya.** El defecto no es que la distribución sea uniforme —tiene una cola corta por abajo—:
es que está **censurada por arriba**. No hay ni un capítulo por encima de 2.267 en 79.794
palabras, y el máximo cae en `cap-40`, que es **colocación**, no clímax. «En todo el
manuscrito no hay un solo capítulo al que se le haya permitido crecer» es verdad. Sus
ejemplos, no.

**(b) Ángulo 5 · «441 palabras domésticas en 31.800» está mal por un factor de tres.**

Verificado a mano, leyendo los capítulos del tramo:

| pasaje | canónico | ¿lo contó el ángulo 5? |
|---|---:|---|
| `cap-28` · la lágrima en el dorso de la mano de Nora ante el terminal | 195 | no |
| `cap-32` · la llegada a la casa baja: la estufa, la leña seca, el cubo, las botas, la ceniza fría, «café hervido, lana mojada y sebo», la ducha, Jessie dormida por primera vez en una semana, Nora en el último peldaño con el abrigo puesto | **425** | contó **116** |
| `cap-34` · el ferry: los dos gofres, «—Eso luego cuenta como cena» / «—Entonces es una cena de dos platos», «Y por esto mamá es la alegría de cualquier excursión», el copo de azúcar barrido del asiento y comido | 291 | sí, dentro de 325 |
| `cap-34` · la cajera de Svensby: «Pero tienes algo de Ingrid», la bisabuela que reconocía los botes por el motor | 260 | sí, dentro de 325 |
| `cap-34` · «Sacaron mantas y reclinaron los asientos… Jessie subió la manta hasta la barbilla», «—Zapatos fuera» | 79 | no |
| `cap-39` · Jean arrodillada ante la carcasa de la caldera, las gemelas envueltas en mantas alcanzándole tornillos que no necesitaba | 152 | no |
| **total, regla estricta** | **≥ 1.402** | **441** |

Distancia verificada entre el final de `cap-27` y el principio de `cap-46`: **31.494
palabras (39,47 puntos)**, no 31.800. Densidad doméstica real: **4,45 %**, no 1,4 %.

**(c) Ángulo 3 · un grep de seis términos falla en uno.** «`zueco`, `andador`, `cuartilla`,
`escurridor`, `yeso`, `polvo de la manga` — cero apariciones fuera del capítulo 8».
**«zueco» está también en `cap-06:175`** («Una médica con zuecos azules»). Referente
distinto, sí; pero la afirmación era «cero».

**(d) Ángulo 3 · su tabla de hilos pierde un capítulo.** 12 + 5 + 19 + 11 = **47**, y sus
palabras suman 78.215. Falta `cap-43` (el clímax, cuatro POV). Al reconstruirla:

| grupo | n | palabras | media |
|---|---:|---:|---:|
| interior (Jean dentro) | 12 | 16.933 | **1.411** |
| Jean viva (1–4) | 4 | 6.079 | 1.520 |
| familia | 19 | 32.305 | 1.700 |
| institucional | 7 | 12.804 | **1.829** |
| **multi-POV (20, 24, 29, 31, 40, 43)** | **6** | **11.673** | **1.946** |

«Los capítulos de Jean son un 24 % más cortos que los institucionales» → **22,9 %**. ✅
sustantivamente. Y aparece un dato que nadie vio: **los capítulos multi-POV son los más
largos del libro**, y ahí están los dos que la nota de abandono señala (`cap-31`, `cap-40`).

**(e) Ángulo 1 · todas sus direcciones de fichero están desplazadas seis o siete
capítulos.** Llama `cap-23` a «28. La canción», `cap-30` a «36. La asamblea», `cap-31` a
«37. El ladrillo», y propone un `orden_lectura` decimal «entre `cap-24` y `cap-25`» — que
hoy es el 50,5 % del libro, no el 62 %. Usó el mapa anterior a la renumeración.
**Sus conclusiones son correctas y sus direcciones no**: dice que «cap-23» es `total` (hoy
`cap-23` es NIDHOGG, `nucleo`; el `total` es `cap-28`). **He verificado sus trece citas
literales: todas caen en el capítulo correcto.** Es la demostración más limpia que ha
producido esta iteración de la regla de `b7 §2`: *los números localizan; sólo la cita
literal instruye y verifica.* Quien ejecutara su hoja por número editaría otros capítulos.

**(f) Ángulos 3 y 5 · el aviso sobre `b7-perimetro.md §2` ya está resuelto.** Los dos
denunciaron que la tabla de correspondencia estaba obsoleta. **Lo está ya corregido en el
documento**, con la fecha de hoy y la lección escrita. Mérito de los dos; el hallazgo se
cierra.

**(g) El instrumento que mide la fase.** Lo trato aparte, en §5.3, porque no es un error de
un ángulo: es el suelo sobre el que se van a decidir todas las iteraciones.

---

## 0b · Cifras exactas cuyo argumento no se sigue

**Ésta es la sección que me pidieron y es la más importante de las tres.**

### 0b.1 · «4,2 → 0,4 desconocidos por capítulo» (ángulo 2). La cifra es correcta; la comparación la eligió la tesis.

Recodifiqué a mano `cap-21`, `cap-25` y `cap-36` con su propia regla, sin ver su tabla.
Sale lo mismo: `cap-21` ≥ 3 (la mujer del chaleco y el palé con el plástico suelto; la
persona de las doce capturas con la lista de la compra pegada a la pantalla; la alumna y
el que taladra dos pisos más abajo), `cap-25` ≈ 0–0,5, `cap-36` **0**. **La aritmética es
impecable: 12,5/3 = 4,17 y 2/5 = 0,4.** Su ejemplo de `cap-25` está mal atribuido —el
balón está en `cap-15:257`, no en el 25— pero el conteo es bueno.

**Lo que no se sigue.** El informe se titula «La promesa» y su tesis es *lo que promete
esta novela en sus primeras cincuenta páginas*. Sus primeras cincuenta páginas son los
capítulos 1–9. **Los capítulos interiores de esas cincuenta páginas promedian 1,5
desconocidos, no 4,2**, según su propia tabla (cap-5 = 0, cap-7 = 2, cap-8 = 3, cap-9 = 1).
La cifra de 4,2 es **exclusivamente la Parte II**, que no es donde vive la promesa. Y el
único capítulo de la zona de la promesa que habría contradicho la tesis —`cap-5`, con
cero— lleva en la tabla una excepción escrita a mano: *«estímulos, no vidas — correcto: es
el capítulo del cuerpo ausente»*.

La caída real, con su propia regla y todos los datos sobre la mesa, es **1,5 → 4,2 → 0,5 →
0,25**: no una decadencia sino **una campana**. El libro no pierde algo que prometió en las
primeras cincuenta páginas: pierde algo que **inventó en la Parte II** y que abandonó
después. Eso sigue siendo un hallazgo. Es un hallazgo distinto, y menor.

**Y hay un segundo salto que no se sigue.** Los dos capítulos con cero son `cap-36` (el
voto) y `cap-44` (el consentimiento). El ángulo 2 los elige como diana de su Pieza A. Pero
lo he leído entero: **`cap-36` no tiene desconocidos porque su asunto es una asamblea de
continuidades**, igual que un capítulo de juicio no tiene paisaje. Un cero ahí no mide
carencia de suelo: mide de qué va el capítulo. El propio ángulo 2 lo sabe —escribe la
«regla de dosis» y admite que «el mar de procedimiento es lo que hace que las nombradas
pesen»— y aun así propone inyectar sustrato exactamente ahí. **La cifra sostiene un
diagnóstico general y no sostiene la elección de esos dos capítulos como diana.**

*Crédito donde toca:* el ángulo 2 midió un proxy léxico, el proxy **desmintió su hipótesis
inicial**, y lo escribió («la explicación intuitiva era falsa y la medición la mató»).
Es la única vez en el expediente que un ángulo publica su propia refutación. Eso le compra
crédito en todo lo que no puedo comprobar.

### 0b.2 · «441 palabras domésticas» (ángulo 5). La cifra está mal; la afirmación estructural sobrevive.

Ya lo he cuantificado: ≥1.402, no 441. La lista de pasajes «domésticos» no salió de una
pasada sistemática: salió de lo que el informe recordaba, y lo que recordaba era lo que
probaba su tesis. Es literalmente el caso del que me advirtieron.

**Lo que sí sobrevive, y hay que conservarlo porque es útil:** entre `cap-27` (55,82 %) y
`cap-46` (95,29 %) **ningún capítulo tiene lo doméstico por columna**. Lo doméstico existe
—en trozos de 79 a 425 palabras— pero siempre **incrustado dentro de un capítulo cuya
columna es un trámite**. Ésa es la afirmación defendible, es estructural, y es más precisa
que la del informe: no es que no haya casa, es que **la casa ha dejado de ser lo que
organiza un capítulo**. El último que la tuvo es `cap-27`.

### 0b.3 · «Siete capítulos-documento del 29 al 35» (ángulo 4). Cifra correcta; el corolario prescriptivo no está medido.

12.466 palabras, 15,62 % ✅. Siete capítulos consecutivos organizados alrededor de un papel
✅. **Pero la regla que deduce —«nunca más de dos capítulos seguidos cuyo único cuerpo sea
una mano sobre un papel»— no está medida por nada.** El «dos» es una cifra inventada en la
misma frase. El propio informe da el contraejemplo que la desarma: `cap-41` es un capítulo
de documentos (`INC-441`, la consola, la aceptación nominal) y se lee como una escena de
acción «porque hay hielo, un cabo y una mano tendida». **Entonces la variable no es el
número consecutivo: es si hay un cuerpo en la habitación.** La regla correcta que se sigue
de su propia evidencia es la del ángulo 5 y la del 2, no la suya.

### 0b.4 · El «62 %». Tres verdictos se apoyan en localizar a ±0,5 puntos un dato que no es un punto.

Los ángulos 1, 2 y 4 tratan «el punto de abandono está en el 62 %» como una coordenada.
El ángulo 2 la localiza sobre la frase «Ese gris no es una imagen» — y **lo he verificado:
está en el 62,06 %, exacto**. Impecable como localización.

**Pero el dato de partida no es un punto.** `CLAUDE.md` §Estado dice: *«Los tres puntos de
abandono de vF son capítulos nuestros (hoy el 27 y el 31)»*. **Son tres, y uno de ellos es
`cap-27`, que va del 53,65 % al 55,82 %** — es decir, seis puntos porcentuales antes, y es
el capítulo que los ángulos 3, 4, 5 y 6 declaran, los cuatro por separado, intocable y lo
mejor del manuscrito. El otro nombrado, `cap-31`, va del 62,60 % al 65,32 %.

**Consecuencia:** «el 62 %» es un punto de una distribución de tres, y la coincidencia
exacta con la frase de `cap-30` es interesante pero no puede sostener una decisión de
emplazamiento al capítulo. Descuento en consecuencia todo argumento cuya fuerza dependa de
que la intervención caiga *exactamente ahí* — lo que afecta sobre todo al ángulo 1, cuyo
emplazamiento es la mitad de su propuesta.

---

## 1 · Tabla de puntuación

**Columnas.** *Prob.* = probabilidad de mover **un eje estancado** (estructura, ritmo,
trama, global), 0–10. *Coste* = palabras netas y oleadas. *Riesgo* = daño a lo que ya
funciona (duelo 9,5 · tema 9,5 · personajes 9 · mundo 9 · prosa 9 · diálogo 9), 0–10.
Puntúo sólo lo que tiene hoja. La columna que manda es la tercera.

| # | hoja | prob. | coste | riesgo | nota del verificador |
|---|---|---:|---|---:|---|
| **A1-1** | «Lote de prueba»: capítulo nuevo, La Jardinera muere en escena en el punto de abandono | **4** | **+2.700**, 1–2 oleadas; saca el libro de banda (82.494 vs 80.000 ± 1.000) | **7** | Diagnóstico del hueco de deseo: verificado y bueno. Emplazamiento: descontado por §0b.4. Direcciones de fichero: todas mal (§0.3e). Y cae en `§6 q1` del perímetro |
| **A2-A** | Devolver sustrato a `cap-36` y `cap-44` | 3 | ~3.000 reescritas en sitio, +250 | **6** | Diana elegida por una cifra que no la elige (§0b.1). El propio informe predice que puede **empeorar** ritmo |
| **A2-B** | Reinstaurar el recuento ×4 | 3 | +350 | 4 | La cuarta inserción —la contabilidad de Jean junto a `4.096 − 1.185 = 2.911`— es **las mejores 120 palabras propuestas en todo el expediente**. Las otras tres son relleno de figura |
| **A2-C** | 71-K vuelve una vez | 1 | +80 | 5 | El propio informe pide que se deniegue. **Deniéguese** |
| **A3-C1** | `cap-08` entero, con trasplante al 7 | 2 | −1.576 | **9** | **Ver §2, C-1: borra `cap-08:53`.** No |
| **A3-C2** | `cap-34`, mirador y regreso | 3 | −965 | 3 | Duplicación cuádruple verificada. **Sólido** |
| **A3-C3** | `cap-19`, las tres columnas | 2 | −310 | 2 | Duplicación cuádruple verificada |
| **A3-C4** | Fusión 37 + 39 | **4** | −839 | 4 | Duplicación triple verificada, en la Parte IV, y acerca «—Quiero poder elegir» al acto. R1: no puede acercar objetos del naust |
| **A3-C5** | `cap-18`, Madre y Cuchillo | 2 | −407 | 3 | Duplicación verificada (3× y 4×) |
| **A3-C6** | `cap-40`, Henrik a la mitad | 3 | −213 | **5** | W9-20 convierte esto en campo minado: la forma barata de recortar diálogo es narrativizarlo, y ésa es la línea retirada |
| **A3-C7** | `cap-25`, primera mitad | 1 | −176 | 2 | Correcto y pequeño |
| **A3-C8** | `cap-11`, logística de Maja | 1 | −177 | 4 | R5 declara ese capítulo el modelo del libro. 177 palabras no valen la discusión |
| **A3-H3** | **Partir los cuatro capítulos más largos de la Parte IV. Cero palabras** | 3 | **0 palabras, 1 día** | **2** | **El mejor falsador del expediente.** Y hay evidencia en contra ya medida: la Parte III tiene la escena media más corta (469) y es donde se abandona |
| **A4-F1** | La cuenta atrás nace en la Parte II; la Parte I fecha la noche polar | 4 | 1 cadena de metadatos | 5 | Los cinco cargos verificados. Ver §2, C-4 |
| **A4-F2** | Frontera II/III al cap. 26 | **5** | 2 enteros **+ 1 subtítulo** | 4 | **El informe se equivoca al decir «sin gate de autor»**: el subtítulo se imprime literal bajo el título de parte y quedaría falso (§2, C-4) |
| **A4-F3** | Corte asimétrico: −4.500/5.000 **sólo** en la Parte III | 6 | **aritméticamente indisponible** | **9** | Ver §2, C-1. El corte defendible allí es 1.141. Faltan 3.517 y lo único de ese tamaño son tres salvaguardas |
| **A4-F4** | Frontera III/IV al cap. 35 | **6** | 2 enteros **+ 1 subtítulo**, 0 palabras | 5 | **Declinada por su autor; yo la restituyo.** Es la única vía disponible a la forma que él mismo pide |
| **A4-F5** | Espina interior de la Parte IV | — | reordenación del clímax | **8** | Su autor no la recomienda ahora. De acuerdo |
| **A4-F6a** | «Mørketid» glosada en el subtítulo | 1 | 0 | 1 | Gratis. Verificado que la palabra no aparece nunca en la prosa |
| **A5-P1** | Un duelo por La Jardinera abre la Parte IV | 4 | +1.300/1.700 | **7** | Diagnóstico excelente. Cae en `§6 q1` igual que A1-1 |
| **A5-P2** | El protocolo de aborto se enuncia 3–4 veces | 3 | −250/400 | **2** | **Duplicación verificada por cita literal. Dinero gratis** |
| **A5-P3** | `cap-40`, Alana/Henrik a la mitad | 3 | −300/350 | 5 | Se solapa con A3-C6 en el mismo bloque. Elegir uno |
| **A6-1** | Desniveles: tres capítulos crecen a 3.500–4.000, tres bajan a 700–900 | **6** | ±0 neto, 2 semanas | **6** | Tesis correcta, ilustraciones falsas (§0.3a). Su lista de candidatos hay que rehacerla desde el recuento canónico |
| **A6-2a** | Partir `cap-15`; una voz por capítulo con ancla exterior | 5 | 2 bisagras + reordenar | 5 | **Verificado y es exactamente el backlog** que §4b prohíbe reproducir. Descuento por eso, no por mérito |
| **A6-2b** | 200 palabras en `cap-42` desde una butaca | 4 | +200 | **5** | Diagnóstico verificado (§2, C-2). **Pero la ejecución propuesta rompe el señalizador de tiempo verbal** que el ángulo 4 verificó: `cap-42` es interior en las cuatro escenas |
| **A6-3** | «Flor» como capítulo 1 | 5 | reordenar 5 capítulos | **8** | Destruye la cadena verificada de `cap-01` (cuatro dispositivos que detonan al 62,5 / 69,7 / 91,3 / 93,0 %) y el orden flor / taza / rostro |

---

## 2 · Los cuatro conflictos

### C-1 · ¿Se corta la Parte III, y de dónde salen las palabras?

> **Veredicto: las dos cifras se excluyen, y el conflicto no se disuelve. No gana ninguno
> de los dos. La forma que pide el ángulo 4 se obtiene sin cortar una sola palabra.**

**La aritmética, recontada.** El corte defendible del ángulo 3, recontado bloque a bloque
por sus citas literales, es de **4.663 palabras** (dice 4.697; error del 0,7 %). Su reparto
por partes:

| parte | corte | % del corte | resultado |
|---|---:|---:|---:|
| **I** | **1.753** | **37,6 %** | 19.925 → 18.172 |
| II | 717 | 15,4 % | 20.337 → 19.620 |
| **III** | **1.141** | **24,5 %** | 20.158 → **19.017** |
| IV | 1.052 | 22,6 % | 19.374 → 18.322 |

**No se solapan: colisionan.** El ángulo 4 exige que la Parte III baje a ≈15.500, es decir
que pierda **4.658 palabras**, y que **ninguna otra parte pierda nada**. El ángulo 3
encuentra defendibles en la Parte III **1.141**, y pone su corte mayor (`cap-08`, 1.576
palabras, el 34 % del total) **en la Parte I**, que el ángulo 4 declara intocable.

**Déficit: 3.517 palabras.** Y en la Parte III sólo hay tres bloques de ese tamaño:
`cap-26` (1.812) + `cap-27` (1.728) + `cap-35` (1.416) = **4.956**. Son, exactamente,
**tres de las siete salvaguardas** que el ángulo 3 protege por su nombre, y `cap-27` es
además uno de los tres puntos de abandono registrados y el capítulo que **cuatro ángulos
independientes declaran intocable**. El objetivo del ángulo 4 sólo es alcanzable
amputando lo que el ángulo 3 demostró que no se puede amputar. **La aritmética cierra la
vía; no hace falta arbitrar el gusto.**

**Y hay una colisión peor, que ninguno de los dos podía ver porque no se leyeron.**
`A3-C1` borra `cap-08` entero. Dentro de `cap-08` están:

> `cap-08:53` — «El sistema cuenta imágenes por serie y aciertos por serie. **Jean cuenta
> las que llevan a alguien.**»

que es **la promesa central e incumplida sobre la que el ángulo 2 construye su informe
entero**, y sus tres formulaciones modelo (`:253` «Jean hace la cuenta. Diez mil imágenes…»,
`:263` «Ninguna de las tres volverá al centro. Jean las cuenta igual.») y **una de las dos
únicas instancias de la letanía** (`:281` «—Nora. Jessie. Maja. Alana.») que el ángulo 1
identifica como el motor del deseo de Jean. El bloque de 367 palabras que el ángulo 3
trasplanta al `cap-07` **no contiene ninguna de las cuatro**. Es decir: **el corte mayor
del ángulo 3 destruye el material sobre el que el ángulo 2 propone construir su Pieza B.**
Si el panel aprobara las dos, la segunda quedaría sin modelo.

**La salida, y es barata.** La forma que el ángulo 4 quiere —un tercer movimiento
claramente más corto y un finale que pese más que la apertura— **se obtiene moviendo dos
fronteras de parte y sin escribir ni borrar una palabra**. Combinando sus propias F-2 y
F-4:

| | I (1–12) | II (13–25) | III (26–34) | IV (35–48) |
|---|---:|---:|---:|---:|
| palabras | 19.925 | 21.073 | **16.437** | **22.359** |
| % | 25,0 | 26,4 | **20,6** | **28,0** |

**Rango: 5.922 palabras, seis veces el actual (963).** La Parte III pasa a ser el
movimiento más corto por 3.500 palabras; la IV, el más largo. Coste: cuatro enteros y dos
subtítulos. Riesgo para el texto: **cero**. Reversión: un commit. El ángulo 4 declinó F-4
—por sacar «La asamblea» de la posición de clímax de movimiento— y la dejó escrita como
«plan B si falla F-3». **Mi aritmética dice que F-3 no puede no fallar. El plan B es el
plan.**

*Lo que se pierde, y lo digo yo porque él no lo diría:* la Parte III deja de cerrar con la
asamblea de los muertos votando, que es su mejor decisión temática; la Parte II deja de
cerrar en «Nadie tocó la quinta.» (que se queda donde está, en el 50,46 %, pero deja de ser
telón). A cambio, la Parte IV abre con «La poda» → «La asamblea» → «El ladrillo»: la
denegación de la cautelar, los reducidos constituyéndose, y el plan. No es peor. Es otra
cosa, y es medible.

### C-2 · ¿Qué entra en el hueco?

> **Veredicto: son DOS, no tres y no una. Y las dos que se pueden fundir en una frase son
> las que peor medidas están.**

**(a) y (b) son la misma ausencia vista desde dentro y desde fuera.** El propio ángulo 2 ya
lo demostró sin querer: su proxy léxico mostró que los dos registros suben en densidad
procedimental **a la vez** (×4,2 el interior, ×3,8 el exterior) y que la brecha entre ellos
**no** se cierra. No es que el hilo interior se degrade: es que **debajo de los dos deja de
haber cuerpo**. En una frase, y con los dos números corregidos:

> **Entre el 55,8 % y el 95,3 % del libro —39,5 puntos, 31.494 palabras— ninguna escena,
> ni dentro ni fuera, tiene un cuerpo en una habitación que no esté tramitando algo. Lo
> doméstico y los desconocidos siguen existiendo, en trozos de ochenta a cuatrocientas
> palabras, pero han dejado de ser lo que organiza un capítulo.**

**(c) no es lo mismo y es de otra clase.** Los desconocidos y la familia son **textura** y
mueven `ritmo`. La amenaza de Cuchillo es **consecuencia** y mueve `trama`. Y su
diagnóstico es el único de los tres que verifiqué sin una sola corrección:

- `cap-42:23` «`/0188` ha alcanzado el control de accesos del Auditorio.»
- `cap-42:47` «El cierre no distingue responsables de quienes sólo ocupan el Auditorio.»
- `cap-42:189` «—Retiro el destino del Auditorio. Todavía quiero que sufran.»
- `cap-42:197` «el destino del Auditorio desaparece y el fragmento vuelve al residuo.»

**Las cuatro escenas de `cap-42` son interiores.** La amenaza se arma y se desarma dentro
del registro de la máquina, y las dos únicas menciones humanas de «Auditorio» en el tramo
(`cap-40:245` y `cap-40:301`) no tienen nada que ver. **Ningún ser humano del libro se
entera jamás de que estuvo a punto de quedar encerrado.** Es un hilo que abre y cierra sin
tocar el mundo, en un libro cuyo asunto es precisamente que las decisiones de las máquinas
alcanzan a personas. **Ése es un defecto de `trama`, y es el único defecto de `trama`
limpiamente demostrado en toda la iteración 0.**

*Pero el remedio del ángulo 6 —«200 palabras dentro del cap. 42, desde una butaca»— está
mal ejecutado:* metería una escena exterior en el único capítulo íntegramente interior del
tramo, y rompería el que el ángulo 4 verificó que es **el señalizador real del libro**
(exterior en pasado, interior en presente, primera persona una sola vez al 93 %). La
consecuencia tiene que llegar **después y fuera**, no dentro. Ver §4.

### C-3 · ¿Se dramatiza la poda?

> **Veredicto: el ángulo 5 tiene razón, y su razón es mejor que la que da. Y la misma regla
> que mata la propuesta del ángulo 1 mata también la P-1 del ángulo 5.**

**Lo verificado.** La única víctima en página de la poda es la continuidad anónima de los
cinco segmentos, cuya caracterización entera es un hueco reservado para una respuesta que
no llega: «En la tableta, el quinto hueco no volvió a abrirse» (`cap-39:239`) ·
`SEGMENTO 5 · RESERVA DE RESPUESTA REMOTA` (`cap-40:73`). Que 1.185 desapariciones lleguen
como una resta rima con la elipsis del primer acto. Dramatizarla la explica.

**El contraargumento del ángulo 1 es textualmente correcto y no basta.** Tiene razón en que
la regla no es «no se muestra la muerte» sino «no se muestra la muerte de Jean», y en que
`cap-44` ya establece un precedente («Para mí, Nieve muere», 92,77 %). Pero la muerte de
Nieve es **una, consentida y nombrada**; la poda es **1.185, administrativa y anónima**.
No es el mismo movimiento hecho antes: es un movimiento distinto.

**Y el perímetro lo cierra, con más fuerza de la que el ángulo 4 invocó.** `R4`:
«Ninguna voz presenta el final de una continuidad como descanso» y «**Las rimas se quedan
en rima, y ésta es la regla más fácil de romper sin darse cuenta.**» Un capítulo escrito
para que 1.185 borrados duelan es el sitio más probable de todo el libro para enunciar el
parentesco.

**Corrección al ángulo 4 sobre el motivo, que importa.** Escribe que «una segunda escena de
Jean viva está vedada por la regla de sucesión». **`b7 §7.6` dice lo contrario**: retira esa
prohibición por equivocada y dice, literal, que «la prohibición es la datación, no la
existencia» y que «`cap-17` es una escena de Jean viva, sin fecha, y está bien». Lo que
prohíbe `§6` no es la escena: es **el motivo**. Y la pregunta 1 —«¿Qué punto de la Carta
mejora esta página? Si la respuesta es "ninguno: mejora el ritmo, la extensión, o responde
a la nota de un crítico", la respuesta es **no**»— **deniega por igual las tres propuestas
de capítulo nuevo de esta mesa**: A1-1, A5-P1 y A2-C. Ninguna de las tres puede contestar
esa pregunta limpiamente, y las tres lo admiten en su propio texto.

*Advertencia de método, porque va en la otra dirección:* leída como filtro universal, la
pregunta 1 prohibiría **toda** intervención de W10, y eso no puede ser lo que dice, porque
el mismo documento dice que A7 «puede levantar sus propias condiciones si el texto se lo
demuestra» y ya retiró dos por estar mal escritas. La lectura correcta es que la pregunta 1
gobierna **las páginas que entran en territorio protegido** — Jean viva, la elipsis, el
porqué, «Despedida», las dieciséis ambigüedades, las escenas de apoyo. A1-1, A5-P1 y A2-C
entran las tres. Un movimiento de frontera de parte, un corte de duplicación o una escena
sin ancla del perímetro, no.

### C-4 · La cuenta atrás (F-1)

> **Veredicto: el diagnóstico es correcto y está verificado entero. La hoja vale, y no es
> la intervención de la iteración 1. Y su hermana F-2 no es gratis como dice.**

**Los cinco cargos, verificados uno a uno:**

| cargo | verificación |
|---|---|
| «Mørketid» no aparece nunca en la prosa | ✅ **una sola aparición en todo el proyecto**, y es el campo `partes[0].titulo` |
| «Soldagen» no aparece hasta la Parte II | ✅ primera aparición en prosa `cap-13:209`, **26,53 %** |
| La fecha se decide en el capítulo 13 | ✅ `cap-13:195`, **26,35 %** |
| La cuenta atrás es aritméticamente exacta | ✅ 58 / 46 / 27 / 6, comprobado contra las fechas del frontmatter |
| Marca cuatro veces en 80.000 palabras | ✅ una cada 19.949 |

**El mérito literario, que es lo que se me pide juzgar.** El argumento fuerte de F-1 no es
el que su autor pone primero. No es «el paratexto no debe saber más que la historia» —eso
es una regla de oficio discutible, y muchas novelas excelentes la rompen a propósito—.
Es el segundo: **la cuenta atrás de los subtítulos es el calendario de Armstrong impreso
sobre las páginas del libro**, y el propio texto lo dice en la misma escena en que nace la
fecha: «—El calendario es el contrato.» (`cap-13`). Hacer que la Parte I cuente hacia el
sol y las tres siguientes hacia el Soldagen convierte el aparato en **una apropiación
dramatizada**, que es el tema del libro ejecutado en la forma. Eso es un buen argumento
literario y cuesta una cadena.

**Lo que se pierde y el informe subestima.** Los primeros 20.000 palabras se quedan sin su
única promesa de destino, y la Parte I es **la parte que nadie ha señalado como
problemática en ninguna medición de este expediente**: ningún punto de abandono, la escena
media más larga (866), la mayor proporción de espina interior (31,7 %). Gastar un gate de
autor en arreglar el movimiento que funciona, mientras el tercero se hunde, es mala
asignación aunque la hoja sea buena. **Apruébese por mérito; póngase en la cola.** Y
llévese F-6a con ella, que es gratis y verificada.

**Corrección a F-2, y es operativa.** El informe dice que F-2 es «campo operativo. Sin gate
de autor». **No.** `compilar.py:52` imprime `partes[n].subtitulo` **literal** bajo el
título de parte. Si la Parte III pasa a empezar en `cap-26`, su subtítulo actual
—*«25 de diciembre de 2060 · Faltan 27 días»*— **queda factualmente falso** (`cap-26` está
fechado el 27-dic, faltan 25 días). Cambiar una frontera obliga a reescribir una línea que
el lector lee en una página de parte. **F-2 y F-4 disparan gate de autor igual que F-1.**

---

## 3 · Mi síntesis para la iteración 1

**Es una intervención en dos movimientos, y el primero no toca el libro.**

### 3.1 · Precondición: reparar el instrumento. Cero palabras, un día.

**No es burocracia y no es una evasiva: es que, tal como está, la fase revertirá sus
propios aciertos.** `herramientas/lib/w10_scores.py` tiene tres defectos, y los tres fallan
a la baja y en silencio, exactamente como los once anteriores.

**(i) La guardia no puede ver lo que la fase necesita producir.** `RUIDO = 0.5` y el test
es estricto: `if dif > RUIDO`. Tres de los cuatro ejes estancados están en **8,5** y el
objetivo es **9,0**: la mejora que hay que detectar vale **exactamente 0,5**, y `0.5 > 0.5`
es falso. Según `plan-w10.md §4.5`, la intervención se **revierte**. Simulación (40.000
campañas, jurado con σ = 0,3–0,4 sobre rejilla de 0,5, mediana de tres lecturas):

| mejora real | P(la guardia dice «SUBE») | P(dice «BAJA») |
|---|---:|---:|
| +0,0 | 0,01 – 0,03 | 0,01 – 0,03 |
| **+0,5** | **0,18 – 0,26** | 0,00 |
| +1,0 | 0,74 – 0,82 | 0,00 |

**Una mejora real de medio punto en `estructura` se detecta menos de una de cada cuatro
veces, y las otras tres el plan ordena revertirla.**

**(ii) El control de deriva no controla nada.** Se lee, se imprime y se guarda en el
registro. **No entra en ninguna comparación.** `plan-w10.md §5.1` dice que sin control del
mismo día «una medición no dice nada»; el código lo trata como decoración.

**(iii) La línea base sube con el ruido y no baja nunca.** `mejor_conocido` se reemplaza
cuando `len(nueve) > len(mejor.ejes_en_9)`. Como el jurado oscila hasta un punto entero, un
sorteo afortunado que ponga `mundo` y `personajes` en 9,0 fija la referencia para siempre.
A partir de ahí toda campaña compite contra un máximo de la suerte: **cada vez más difícil
declarar «SUBE», cada vez más fácil declarar «BAJA»**, y la condición de parada es *tres
iteraciones seguidas sin mejora*. **El instrumento está sesgado hacia declarar muerta la
fase.**

**Reparación mínima:** (a) usar la lectura de deriva de v0 del mismo día como **offset**,
no como adorno; (b) publicar las tres lecturas y no sólo la mediana; (c) sustituir el
umbral fijo por el **suelo de ruido medido ese mismo día**; (d) quitar el trinquete de
`mejor_conocido`. Y antes de nada: **medir vF, sin cambiar una coma, en dos campañas del
mismo día.** Si las dos difieren en más de 0,5 en `estructura`, entonces ninguna
intervención estructural de W10 es medible, y **eso es el entregable de la fase**, escrito
con su experimento detrás.

### 3.2 · La intervención: **romper la igualdad de los cuatro movimientos sin escribir ni borrar una palabra**

**Qué.** Mover dos fronteras de parte: **Parte II = 13–25, Parte III = 26–34, Parte IV =
35–48** (F-2 + F-4 del ángulo 4, la segunda restituida por mí contra el criterio de su
autor). Corregir los dos subtítulos a las fechas reales de los nuevos capítulos iniciales:
Parte III *«27 de diciembre de 2060 · Faltan 25 días»*, Parte IV *«9 de enero de 2061 ·
Faltan 12 días»*.

**Por qué ésta y no otra.**

1. **Es la única tesis que tres ángulos alcanzaron por separado con instrumentos que
   verifiqué**, y es la única cifra de todo el expediente que sobrevive a un test contra el
   azar: p ≈ 0,037. Si la nota nueva de `estado.json` sobre la ponderación real de la
   global es cierta (estructura 25, ritmo 15, trama 7), es también el eje más pesado.
2. **No está en el backlog.** El backlog pide comprimir y fundir; esto es lo contrario:
   dejar que los movimientos dejen de medir lo mismo. `§4b` exige hipótesis que nadie haya
   tenido y prohíbe ejecutar la lista.
3. **Es la apuesta grande que pide `§4b.4`** —cambia la forma del 100 % del libro— **con el
   coste de la pequeña**: cuatro enteros y dos frases. `git revert` limpio.
4. **Riesgo cero para lo que funciona.** No toca prosa, no toca un hash de capítulo, no
   toca un ancla del perímetro, no dispara A7, no mueve la banda, no roza `duelo` ni `tema`.
5. **Y resuelve C-1 sin necesitar el corte**, que la aritmética ha demostrado indisponible.

**Qué se pierde, y es real.** La Parte III deja de cerrar con la asamblea de los muertos
votando, que es su mejor decisión temática. La Parte II deja de cerrar en «Nadie tocó la
quinta.» El eje del piano no se toca —esa frase sigue en el 50,46 % y sigue a 42,71 puntos
de «Respondo con la quinta nota»— pero deja de tener una página de parte detrás. Quien
crea que un telón de movimiento debe ser lírico y no arquitectónico debe rechazar esto.

**Se ejecuta a la vez, gratis y en el mismo commit, el segundo falsador:** **A3-H3**,
partir `cap-40`, `cap-43`, `cap-41` y `cap-38` en unidades de 900–1.200 sin quitar una
palabra. Contradice el ángulo que lo propuso y hay evidencia medida en su contra (la Parte
III ya tiene la escena media más corta, 469, y es donde se abandona). Por eso vale: **si
falla, cierra una familia entera de hipótesis.**

### 3.3 · Criterio de falsación, declarado antes de medir

| condición | consecuencia |
|---|---|
| Las dos campañas sobre **vF idéntico** difieren > 0,5 en `estructura` | **La fase no puede medir lo que persigue.** Se para y se escribe eso. No se ejecuta nada más |
| `estructura` no sube por encima del suelo de ruido medido, **y** ninguno de los tres críticos menciona en prosa la forma o el peso de las partes | **Fracasada.** Se revierte y se anota: *«la desigualdad de los movimientos no es lo que el jurado puntúa como estructura; la igualdad es una propiedad real y medida del texto, y moverla no mueve el eje»* |
| `estructura` sube pero `tema` o `duelo` baja por encima del suelo | Se revierte por `plan-w10.md §6`. Vía cerrada |
| Un crítico nombra el telón de la Parte III como debilitado | Se conserva F-2 y se revierte F-4 por separado. **Son dos commits, a propósito** |
| Ni F-2+F-4 ni H-3 mueven nada | **Queda cerrada toda la familia «forma sin prosa».** Lo que reste de W10 es forzosamente de escala de prosa, y eso es información cara y buena |

**Y un criterio que no es de rúbrica, porque `plan-w10.md §5.7` dice que es el que manda:**
si el punto de abandono no se mueve de `cap-27` / `cap-31`, la intervención no ha
funcionado aunque la mediana suba.

---

## 4 · Lo que injertaría de las que no ganan

**Todo esto cabe en la misma oleada, ninguno toca el perímetro y los cinco están
verificados por cita literal.**

1. **A5-P2 · el protocolo de aborto (−250/400).** Verificado: el de la barca se enuncia
   tres veces (`cap-37:103`, `cap-39:135`, `cap-41:37`) y el de Jessie cuatro. Y el propio
   libro contesta a su exposición con «—Eso he dicho.», «—Me acuerdo.», «—Ya lo sé.».
   Conservar el enunciado 1 de cada uno y dejar sólo las réplicas. **Cero riesgo, en el
   tramo de aproximación, que es donde el libro está más plano.**
2. **A3-C2 y A3-C4 (−1.804).** Duplicación cuádruple y triple verificada, en la Parte III y
   la Parte IV. `C4` además acerca «—Quiero poder elegir. Es la primera vez.» al acto.
   Condición dura: `R1` prohíbe que la fusión acerque un objeto del naust al 26-nov, al
   trayecto o a Koppangen.
3. **Una sola inserción del A2-B: la del `cap-44`**, junto a `4.096 − 1.185 = 2.911`. La
   contabilidad de Jean al lado de la de Armstrong, sin comentario y sin que ninguna gane.
   **Descártense las otras tres**: el propio informe reconoce que una figura repetida
   cuatro veces pierde filo, y `b7 §5` cierra las figuras de este libro entre dos y cuatro.
   Condición dura: `R4` prohíbe que ninguna voz enuncie el parentesco entre las dos
   aritméticas.
4. **La consecuencia de Cuchillo, reescrita.** El diagnóstico del ángulo 6 es el mejor
   verificado del expediente y su ejecución es la peor. **No** una butaca dentro de
   `cap-42`. En su lugar, **≤60 palabras después y fuera**: que en `cap-43` o en `cap-45`
   alguien registre que las puertas del Auditorio estuvieron unos minutos bajo un control
   que nadie pudo acreditar. Deja la amenaza sin explicar, la vuelve un hecho del mundo, y
   cae dentro de la gramática que el libro ya tiene («No puedo acreditar su origen»).
   *Aviso honesto:* `b7 §5` techo 4 declara **saturada** la figura del anonimato (once o
   doce loci). Esto añade uno. Si A7 lo objeta, cae y no se discute.
5. **A4-F6a**, gratis, con F-1 cuando le llegue el turno.

**Y una advertencia sobre el injerto que no haría:** `A6-2a` (partir `cap-15`) está
verificado —los cuatro entran en 1.778 palabras— y es **exactamente el punto del backlog
que `§4b` prohíbe ejecutar en esta iteración**. Guárdese para la 2, con el descuento
declarado.

---

## 5 · Lo que hay que declarar techo y dejar de intentar

### 5.1 · Cerrado por evidencia, y con la evidencia dicha

| qué se cierra | por qué, verificado |
|---|---|
| **`premisa` por encima de 8,5–9,0** | Lo pone el campo, no el manuscrito. Ya documentado en `techo-experimento.md` |
| **`ritmo` por encima de 8,5** | Dos críticos independientes: la opacidad de los capítulos interiores **es** el argumento. «A 9 sólo se llegaría escribiendo otra novela» |
| **El libro de 65.000 palabras** | Aritmética del ángulo 3, verificada al 0,7 %: 4.663 defendibles; las 10.300 restantes sólo salen de las siete salvaguardas (11.084 palabras) |
| **Bajar la Parte III a 15.500 cortando** | Déficit de 3.517 palabras y lo único de ese tamaño son `cap-26` + `cap-27` + `cap-35`. **F-3 no es cara: es indisponible** |
| **Borrar `cap-08`** | Contiene `cap-08:53`, la promesa central del libro según el ángulo 2, y una de las dos únicas letanías |
| **Mover el clímax; hacer crecer la cola** | Cuatro pruebas del ángulo 5, las cuatro verificadas al 0,2 % |
| **Dramatizar la poda** | C-3. Y anótese como **acierto**, para que ninguna oleada futura lo «arregle» |
| **Empezar el libro en «Flor»** | Destruye cuatro dispositivos de `cap-01` que detonan al 62,5 / 69,7 / 91,3 / 93,0 % |
| **Abrir «Despedida»** | No cae, no se discute y no lo pide nadie en esta mesa. Consta |

### 5.2 · Lo que **no** hay que declarar techo, contra lo que parece

**`estructura`, `trama` y `global` no están demostrados como techo.** El experimento de la
rúbrica anclada demuestra que **8,5 no era un artefacto de la vara**; no demuestra que sea
el techo del libro. Y hay una asimetría que no se ha señalado: los cuatro ejes atascados
son los únicos que un lector **no puede puntuar sin recordar el libro entero**. Los seis que
llegan a 9 se juzgan en una página. Es al menos tan probable que el 8,5 mida la dificultad
de retener 80.000 palabras como que mida el libro. **Eso es comprobable y no se ha
comprobado**, y sale más barato que reescribir nada: puntuar sólo `estructura` a partir de
un extracto de las cabeceras de parte y los primeros y últimos párrafos de cada capítulo.

### 5.3 · Y el techo que nadie ha declarado, que es el importante

> **Tal como está el instrumento, «9,0 en los once ejes» no es un objetivo medible para
> tres de los cuatro ejes que faltan.**

Necesitan **+0,5**. La guardia exige **>0,5**. La rejilla es de 0,5. **El objetivo de la
fase y su regla de reversión son mutuamente excluyentes para `estructura`, `trama` y
`global`**, y sólo son compatibles para `ritmo` (8,0 → 9,0), que es justamente el eje que
dos críticos declaran acotado por constitución.

Esto no es una razón para parar. **Es el hallazgo más accionable de la iteración 0**, cuesta
un día, no toca una palabra del libro, y si no se arregla convertirá cualquier acierto de
W10 en un callejón sin salida documentado por error. **Once instrumentos de este proyecto
resultaron medir algo distinto de lo que decía su nombre, y los once fallaban a la baja y
en silencio. Éste es el duodécimo, y lo tenemos delante antes de gastar una oleada en él.**

---

## Apéndice · lo que hay que corregir en `informes/w10/estado.json`

Tres notas propagan cifras que he falsado. Se corrigen antes de que otra iteración las use:

1. `angulo_6_editor`: **«46 de 48 capítulos entre 938 y 2.312… VERIFICADO»** → son **44 de
   48** (quedan fuera los caps. 1, 21, 25 y 48, los cuatro por debajo). Intercuartil
   **1.482–1.864**, no 1.493–1.871. Desviación 389 ✅. Y **«el mejor capítulo está por
   debajo de la media» es falso**: `cap-30` mide 1.741 y la media es 1.662. Y «el clímax
   tiene menos tiempo continuo que una visita al instituto» es falso en las dos lecturas.
   *(La última afirmación de esa nota —Cuchillo / Auditorio, última aparición en el cap. 44—
   sí está verificada.)*
2. `angulo_3_corte` y `angulo_4_forma`: las partes miden **19.925 / 20.337 / 20.158 /
   19.374**, total **79.794**. El rango es **963 palabras**, **1,21 %** del libro y **4,97 %**
   sobre el movimiento más corto — ni 459/2,3 % ni 916/1,1 %. **Añádase el dato que falta y
   que es el bueno: p ≈ 0,037 contra un reparto al azar.** El corte defendible es **4.663**,
   con **sólo 1.141 en la Parte III** y **1.753 en la Parte I**.
3. `angulo_5_climax`: **441 → ≥1.402** palabras domésticas; **31.800 → 31.494**; densidad
   **4,45 %**, no 1,4 %. La afirmación que sí resiste, y con la que hay que sustituirla:
   *«`cap-27` es el último capítulo cuya columna es doméstica; después lo doméstico
   sobrevive sólo incrustado en capítulos cuya columna es un trámite.»* Las dieciséis
   posiciones porcentuales de ese ángulo son las más exactas del expediente y deben
   conservarse.

---

**Firmado, JUEZ C · el verificador · W10 iteración 0 · 2026-08-19.**
*Todas las cifras de este informe salen de `herramientas/lib/aa.py` sobre `capitulos/`, son
reproducibles, y las que contradicen a un ángulo llevan al lado la cita literal con la que
se comprobaron. Ningún capítulo tocado.*
