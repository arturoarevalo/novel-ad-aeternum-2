# A7 · W2 · cap-17 «Cuchillo» — dictamen de sensibilidad (T7, Apéndice F)

**Firma:** A7, revisor de sensibilidad (veto absoluto) · **Fecha:** 2026-08-17 · **Rama:** `w2-reescrituras` (cap-17 en `6abf54e`; árbol de trabajo en `c08ac5a`)
**Disparador:** B7 §2, **disparador 3** (capítulo con hit NUEVO de nivel A respecto a `informes/a7-baseline-v0.tsv`). El papel «informativo» que preveía OT-17 §7 queda superado: este gate es obligatorio y con veto.
**Base de la revisión:** `capitulos/cap-17.md` íntegro (196 líneas); `git diff v0 -- capitulos/cap-17.md`; `ordenes/OT-17.md` §3, §4, §5 y §9; `biblia/b7-carta-sensibilidad.md`; `informes/d1-a7-biblia.md`; `informes/a7-w2-cap-08.md` (coherencia de firma dentro de la oleada). Cotejo con el resto del libro para la familia de patrones implicada: `cap-02` (:207, :217, :223), `cap-03` (:183, :195), `cap-09` (:33, :37, :195), `cap-11` (:85–97), `cap-13` (:17, :39, :65, :277), `cap-15` (:35, :41, :45), `cap-21` (:71), `cap-30`, `cap-40` (:133).
**Barrido:** `herramientas/sensibilidad.sh` (global, invocación correcta) + `grep -n -i -E` de las familias A-7 (nota/«Despedida»), A-12 (eufemismos), A-14 (últimas horas) y B-1 sobre `capitulos/` completo.

## 0. Rectificación de mi propio informe de cap-08 (§0)

En `informes/a7-w2-cap-08.md` §0 anoté los hits nuevos de `cap-30:145` y `:241` como «nivel B, `cuerda` dentro de «re**cuerda**»: falsos positivos». **Era incorrecto y lo rectifico:** ambos hits los produce `\bagua\b`, no `cuerda`. No eran descartables sin lectura. Los he leído ahora (§4.2) y no arrojan hallazgo, pero la atribución errónea queda corregida en el registro: ningún hit de nivel B junto a Jean se cierra por conjetura sobre qué patrón lo disparó.

## 1. Tabla de hallazgos

| Cap:línea | Cita literal | Punto de la Carta | Gravedad | Propuesta mínima |
|---|---|---|---|---|
| **17:61** (I-2) | «Una lista de la compra pegada a la pantalla tapa **la mitad del último mensaje**.» | **2** (P2) / tono | **corregir · C-1** | «…tapa **la mitad de la última**.» (antecedente: «doce capturas ordenadas por fecha»). Neutra en palabras; ver §2. |
| 17:61 (I-2) | «De esa persona queda una petición: que dejen de escribirle desde cuentas nuevas cada semana. Adjuntó doce capturas ordenadas por fecha.» | 1, 6, 7 | **cumple** | Ninguna. Sin nombre, sin género marcado, sin detalle de violencia, sin crisis ni autolesión, sin subtrama, sin contenido del acoso. Una persona viva con vida alrededor: exactamente lo que pedía D2. |
| 17:177 (I-3) | «En casa la tocaban a cuatro manos: todas las teclas negras, sin orden. Nora se ponía de pie en el banco para alcanzar las últimas. Jessie pisaba el pedal hasta el fondo. Un vaso vibraba encima de la nevera.» | 1, 3, 4, 7, Ap. A §3 | **cumple** | Ninguna vinculante. Clave de casa/infancia estricta; ver §3 y la nota editorial no vinculante. |
| 17:177 (I-3) | «En casa **la tocaban**…» (imperfecto iterativo) | 1 | **vigilar · C-4** | Correcto: hábito, no tarde concreta. Ninguna OT posterior puede datarlo, singularizarlo ni convertirlo en «la última vez». |
| 17:85 (I-1) | «Lo que no se entrega no se borra: queda en el residuo, encadenable a la siguiente salida que se abra bajo el mismo origen.» | 2 | **vigilar · C-3** | Ninguna en 17 (el referente es la medida de contención sin destino, inequívoco en escena). Guarda permanente: la frase no se aplica jamás al archivo. |
| 17:29 (I-4) | «…: la asistencia diaria que ordenaba sus horas y le recordaba lo que tenía pendiente.» | 6 | **cumple** | Ninguna. Servicio ordinario suspendido: coste visible sin diagnóstico, sin nombre y sin patologizar a 71-K. |
| 17:17 (I-5) | «La sanción ha terminado, pero no ha devuelto un orden fiable.» | 3, 4 | **cumple** | Ninguna. Sanción del sistema; no hay culpa moral ni castigo merecido. |
| 17:95, :103, :131 | «…con la voluntad de dañar a Armstrong atribuida a Cuchillo.» · «—No… me uséis.» · «queda una negativa incompleta bajo `/0311`» | 4, Ap. A §3 | **cumple** (v0) | Sin cambios de sentido. La negativa de Nieve no se orienta hacia deseo de morir (OT-36/B7 §5, 36:53–59); el paralelo con Jean no se enuncia. |
| 17 (spans) | `S17-testigo` (:135–143), `S17-nora` (:157), `S17-71k` (:187) | 1, Ap. A §3 | **cumple** | `proteger.sh verificar`: M9 OK, 108 spans íntegros (verificación de A3a en OT-17 §9). Ninguna corrección de este dictamen los toca. |
| 08:65 | «Los informes del nuevo con**cuerda**n.» | — (defecto del patrón) | **resuelto** | Falso positivo de subcadena. Corregido en `biblia/b7-patrones-B.txt` (§4.1). |
| 30:145, 30:241 | «La franja de **agua** sin fuente…» · «…después el **agua** que llegaba hasta las rocas.» | 1 | **vigilar** (sin hallazgo) | Ninguna. El patrón `\bagua\b` se conserva sin cambios; ver §4.2 y C-5. |

**Un hallazgo `corregir` (C-1). Cero `VETO`.**

## 2. El hit de nivel A: «el último mensaje» (17:61)

**Qué dice.** El referente es inequívoco en la escena: el más reciente de los mensajes de quien acosa a la denunciante que pidió protección, dentro de las doce capturas que ella adjuntó a su petición. No es de Jean, no es a Jean, no es una despedida, y su contenido no se da (lo tapa media lista de la compra). El párrafo cumple su etiqueta D2 sin apoyarse en esa expresión.

**Por qué NO es `VETO`.** La Carta 2 prohíbe abrir, citar, parafrasear o «imaginar» «Despedida» y redactar notas de despedida o sucedáneos. Aquí no hay nada de eso: ni archivo, ni Jean, ni texto de despedida, ni contenido, ni formato, ni fecha, ni tamaño. Habría sido veto —lo dejo escrito para que la frontera quede fijada— si la expresión se hubiera atribuido a Jean (aunque fuese de refilón), si el mensaje tapado se hubiera dejado leer, si alguien lo hubiera «imaginado», o si la coincidencia se hubiera subrayado desde una voz con autoridad.

**Por qué tampoco es un simple `vigilar`, y sí una corrección obligatoria.** Tres razones, acumulativas:

1. **v0 no gasta nunca esa expresión, y no por casualidad.** En todo el manuscrito, la familia A-7 aparece cuatro veces como nombre del archivo (`Despedida`: 2:217, 9:37, 9:195, 40:133), una vez como «la última frase que le había dicho» —con el contenido retenido— (9:33) y una vez como sustantivo común en un caso de moderación (21:71). Y en el lugar donde el idioma pedía la expresión —los cuatro mensajes del 26 de noviembre— el narrador escribe «llegó **el primer** mensaje de Jean» (11:85) y jamás marca el cuarto como el último. Ese silencio es lo que convierte esos cuatro mensajes en el techo de B7 §4. La misma abstención existe en un caso de trabajo idéntico al de I-2: 13:17, «cuatro mensajes de un cliente… **En el último** escribe el número del portal», con el ordinal desnudo y sin el sustantivo. El libro tiene ya su idioma para esto; I-2 lo abandona.
2. **La revisión no hereda la licencia de v0.** Las rimas deliberadas entre los casos de Jean y su propia situación —21:71 sobre todo— son del autor y están congeladas en el tag. Una inserción nueva de un agente no adquiere ese permiso sobre una familia de nivel A: el gate existe precisamente para impedir que la expansión añada roces que el original se ahorró. En un capítulo con POV de la ejecución de la muerta, la expresión «el último mensaje» a media página de una petición que «queda» de una persona produce un temblor de referencia que el original nunca se permitió.
3. **Coste sistémico del precedente.** Si la expresión entra en vF, la baseline de T7 la absorbe y el aviso se degrada justo antes de las oleadas donde se escriben los capítulos que sí están junto a Jean (30, 36, 38, 40, N2, N6, N3). Una frase que no cuesta nada retirar no puede ser la que enseñe al pre-chequeo a encogerse de hombros.

**Redacción que autorizo (C-1).** Sustituir la última oración del párrafo por:

> Una lista de la compra pegada a la pantalla tapa la mitad de la última.

Antecedente inmediato y unívoco: «doce capturas ordenadas por fecha» (femenino, y «por fecha» hace de «la última» la más reciente). Variante igualmente autorizada, si A4 prefiere el sustantivo explícito: **«…tapa la mitad de la más reciente.»** (+1 palabra). Queda **prohibida** cualquier variante que reintroduzca la marca: «el último mensaje», «el mensaje más reciente», «el último de todos», «lo último que le escribió».

**Lo que la corrección no cambia:** la función D2 intacta (la persona sigue teniendo cara: la frecuencia, las doce capturas, la lista de la compra); el peso de «La persona que pidió ayuda no pagará por Armstrong» y de «Mantiene vacío el destino», intacto; **0 palabras netas** (3 tokens por 3), de modo que los 851 del capítulo y la banda 800–900 no se mueven; M1 sin término nuevo del lexicón; ningún span protegido tocado (:61 está lejos de los tres). Tras el cambio, A0 vuelve a pasar `proteger.sh verificar` y `sensibilidad.sh` (rutina) y yo releo el diff corregido, como manda B7 §2.

**Alcance de la corrección.** La Carta obliga en todo material de trabajo: además del capítulo, A0 corrige la fila **I-2 de `ordenes/OT-17.md` §9**, que hoy reproduce la expresión («la lista de la compra pegada a la pantalla sobre el último mensaje»). Ningún changelog, informe ni brief la conserva.

## 3. I-3 · la escala del monstruo en casa (17:177): aprobada

- **Punto 1 (método y acto).** No hay fecha, lugar exterior, trayecto, naust, Koppangen ni 26-nov. El tiempo es **imperfecto iterativo** («la tocaban», «se ponía», «pisaba», «vibraba»): un hábito, no una tarde. Es la elección correcta y la convierto en guarda permanente (C-4). Nada del párrafo es leíble como preparación ni como despedida: nadie se despide, nadie entrega nada, no hay palabras dirigidas.
- **Punto 3 (el porqué).** El recuerdo no explica nada ni añade señal sobre el estado de Jean: la muestra jugando con sus hijas, sin deterioro y sin cronología. No hay «antes era feliz» ni serie de declive.
- **Punto 4 (romantización).** Cuatro frases secas, sin sentimiento nombrado, sin cadencia elegíaca, y el capítulo no las recoge: sigue «El campo solo admite una.» y la nota íntima acaba **retirada** para no usar a una alumna. El recuerdo no consuela ni redime; paga la decisión ética de la escena. Tono conforme a la referencia de v0.
- **Punto 7 (menores).** Retrato digno de dos niñas pequeñas: cero cuerpo mirado, cero sexualización, cero adultización simbólica, cero autolesión. La niña de pie en el banco del piano para alcanzar las teclas altas **no** es «conducta imitable de riesgo» en el sentido de la Carta (que apunta a autolesión, consumo y riesgo eficaz sin coste): es una imagen doméstica de infancia, hermana de 3:183 («Nora no alcanzaba el suelo con los pies. Debajo, Jessie buscaba un pedal que pudiera arrancar»).
- **Ap. A §3 (identidad ontológica).** El párrafo entra sin atribución, como memoria libre indirecta, que es el idioma que v0 ya usa dentro de capítulos con POV de la ejecución: 13:39 («Nora no alcanzaba un salto así con la mano izquierda… un vaso de leche encima del piano») y 15:35–41. No formula ninguna afirmación de identidad («Jean recuerda que ella misma…»), no dice «hija» en boca de `/0000` y no toca el techo «No toda». No hay movimiento ontológico nuevo.
- **Canon.** Coherente con 3:195 («todas las teclas negras posibles, sin orden ni misericordia») y con 13:277; no cita el anular del 20.

**Nota editorial no vinculante (tono, no gate).** «Un vaso vibraba encima de la nevera» reproduce casi exactamente la figura de 13:39, «un vaso de leche encima del piano», cuatro capítulos antes y en la misma clave de recuerdo doméstico. No infringe ningún punto de la Carta y no condiciono el merge, pero la repetición del mismo objeto en el mismo sitio sintáctico rebaja el efecto de las dos. Si A4 quiere diferenciar, basta cambiar el objeto —no la frase—; decisión de A0/A4.

## 4. Los tres avisos de nivel B

### 4.1 · cap-08:65 «con**cuerda**n» → defecto del patrón, corregido

Falso positivo de subcadena. En todo `capitulos/`, la cadena «cuerda» aparece 11 veces dentro de otra palabra (`recuerda` ×8, `recuerdan`, `recuerdas`, `concuerdan`) y **una sola vez** como la palabra que la Carta protege de verdad: «Había **cuerdas** rígidas…» (04:99, inventario del naust). Un patrón con 11 falsos por 1 verdadero no protege: entrena a ignorarlo.

He modificado `biblia/b7-patrones-B.txt` (fichero de mi competencia): `cuerda` → **`\bcuerdas?\b`**, y de paso `curar` → **`\bcurar`** (falso: «procurar»). Ambos son defectos de subcadena; el resto del ruido de nivel B es de palabra real («frío», «explicar», «cabo») y **se conserva a propósito**: el nivel B está para sobre-recoger. El fichero lleva ahora cabecera con el historial del cambio.

Verificación hecha: T7 pasa de 340 a 328 hits (−12: los 11 de `cuerda` y «procurar»); `cap-08:65` deja de figurar entre los nuevos; **04:99 sigue cazándose** (comprobado). No hace falta rebaselinar: `lib/sensibilidad.py:65` compara por `(fichero, texto)` y no por el patrón, de modo que cambiar una regex nunca genera hits «nuevos» falsos ni invalida `informes/a7-baseline-v0.tsv`.

### 4.2 · cap-30:145 y :241 «agua» → leídos, sin hallazgo; el patrón se queda

Leídos en contexto, con el diff de cap-30 y la escena entera del jardín. Son la playa que las continuidades reconstruyen entre todas —Telegrafbukta, la playa urbana de la familia, con el banco, las rocas y las fogatas— apareciendo y disolviéndose según quién sostiene cada fragmento y qué borra el programa de consolidación. **No hay método, ni lugar del acto, ni cuerpo, ni trayecto**: no es Koppangen, no hay naust, no hay barca, no hay 26-nov, y en ningún punto del libro (v0 ni W2) la muerte de Jean se asocia al agua. El agua de 30 es materia de memoria compartida y su desaparición es el coste del borrado de La Jardinera, no una insinuación. Sin hallazgo.

`\bagua\b` **se mantiene tal cual**: cap-30 es capítulo de Jean y quiero seguir siendo avisado cada vez que aparezca agua ahí. El patrón funcionó como debía: avisó, leí, resolví. Queda la guarda C-5.

Nota de alcance: este dictamen resuelve las dos líneas señaladas, no sustituye una lectura completa de cap-30 (OT-30 §7 declara «A7: no aplica»; matizo el registro: OT-30 §4 afirmaba «no dispara T7» y sí lo hizo, aunque sin consecuencia). En el momento del barrido, el árbol de trabajo contenía además `cap-21` y `cap-36` modificados y sin commitear: **cero hits nuevos** en ambos, pero eso es un pre-chequeo léxico, no mi firma; cuando OT-21 escriba su I-2 (recuerdo de Telegrafbukta) me corresponde la pasada informativa que su §7 prevé.

## 5. Los ocho puntos, uno a uno

1. **Método y acto:** nada nuevo. Ningún objeto, sustancia, lugar, hora ni gesto; ninguna reconstrucción; la elipsis del 4 intacta.
2. **«Despedida»:** no aparece, ni el nombre ni sucedáneo alguno. El único roce es léxico y se corrige en C-1. La frontera de la no-entrega, que v0 blinda en 13:65, 15:45 y 15:71–73, sale reforzada de este capítulo (Jean retira la nota íntima y no usa a la alumna).
3. **El porqué:** el capítulo no ofrece causa, ni la insinúa, ni la niega en negativo. Ninguna voz con autoridad cierra nada.
4. **Romantización:** ni paz, ni descanso, ni liberación, ni lógica, ni valentía, ni cobardía. La negativa incompleta de Nieve y la contención de Cuchillo no se orientan hacia el deseo de morir.
5. **Aviso y recursos:** intactos, sin cambios en esta oleada (siguen provisionales, pendientes de validación de autor y de la verificación de vigencia de A5 en vF).
6. **Apoyo y duelo:** no hay escena de apoyo; nada instructivo, nada culpabilizador, ningún milagro. El coste de 71-K queda como coste, sin lección.
7. **Menores:** I-3 aprobada (§3). Retrato digno, sin cuerpo mirado, sin riesgo imitable.
8. **Veto:** no procede.

**Ambigüedades protegidas (Ap. A §3):** el porqué, intacto; Koppangen, ausente (correctamente excluido de I-3); «Despedida», ausente; el ordenante del sabotaje, ausente; el segundo regalo, ausente; la salida del locutorio, ausente; techo ontológico «No toda», sin tocar.

**Tono (referencia v0: caps. 4, 9, 23, 40).** El diff mejora la contención: los recortes R-1/R-2/R-3 quitan glosa y repetición, I-2 sustituye una abstracción («la persona que pidió protección mediante uno de sus servicios») por una vida concreta sin explicarla, e I-3 deja el recuerdo sin recogerlo. El capítulo confía más en el lector que su versión v0. Ningún pasaje instruye ni consuela.

## 6. Condiciones

**C-1 · Obligatoria antes del merge de W2 (bloquea el capítulo, no la oleada).** En `capitulos/cap-17.md:61`, sustituir «tapa la mitad del último mensaje» por «tapa la mitad de la última» (o la variante autorizada «de la más reciente»); y actualizar la fila I-2 de `ordenes/OT-17.md` §9 para que ningún material de trabajo conserve la expresión. Ejecuta A0; yo releo el diff corregido y firmo la conformidad al pie de este informe.

**C-2 · Prospectiva y vinculante (toda la expansión, W3–W7).** Ninguna inserción nueva introduce las expresiones marcadas de la familia A-7 —«último mensaje», «última frase», «últimas palabras», «nota / carta / mensaje de despedida»— ni «despedida» o «adiós» **como nombre de un texto, archivo u objeto**, aunque el referente nada tenga que ver con Jean. Las de v0 se conservan intactas donde están (9:33; 21:71; `Despedida` en 2:217, 9:37, 9:195, 40:133) y siguen siendo el techo. Un «adiós» conversacional de un personaje no queda prohibido, pero llega a mí por T7 y lo leo. Verificable por A8 con el pre-chequeo.

**C-3 · Prospectiva y vinculante.** «Lo que no se entrega no se borra» (17:85) es canon de sistema sobre el residuo de una medida sin destino. Ninguna voz con autoridad narrativa —narrador en cualquier persona, acta, auto, registro auditado, prensa— puede aplicarla, ni por eco ni por variación, al archivo «Despedida» ni a lo que Jean no envió; en boca de personaje requiere autorización previa mía, por escrito y para esa frase concreta (mismo régimen que los efectos personales de N3). Vinculante para OT-30, OT-36, OT-38, OT-40, N2, N6 y la pasada de W7.

**C-4 · Prospectiva y vinculante.** El recuerdo de I-3 permanece en imperfecto iterativo: ninguna OT posterior puede fecharlo, singularizarlo en una tarde concreta, convertirlo en «la última vez que tocaron juntas» ni encadenarlo con 3:213 y 8:43 en una serie de deterioro con destino. Eso sería explicación única en voz narrativa: `VETO`.

**C-5 · Prospectiva y vinculante.** La playa del jardín (30) y el recuerdo de Telegrafbukta (OT-21, I-2) son lugares de memoria familiar. No pueden juntarse jamás con Koppangen, el naust, la barca, el 26-nov ni el hallazgo, ni por yuxtaposición de escena: convertir una playa recordada en escenario del acto es Carta 1.

Siguen vigentes C-1, C-2 y C-3 de `informes/a7-w2-cap-08.md` (la coincidencia 08:43 ↔ 09:203 no se glosa nunca; el caso médico no vuelve; la acumulación del piano y R2).

## 7. Veredicto

**APROBADO CON CONDICIONES** (= «APROBADO CON CORRECCIONES» de B7 §2). Una sola corrección obligatoria, **C-1**, de tres palabras y coste cero en arco, función, ritmo y presupuesto. Con ella, la reescritura W2 de cap-17 cumple los ocho puntos de la Carta: no introduce método, acto, escena, hora ni lugar; no abre, cita, parafrasea ni imagina «Despedida» ni sucedáneo alguno; no ofrece causa ni señal nueva sobre el estado de Jean; no romantiza ni moraliza; trata con dignidad a las dos menores del recuerdo; conserva aviso y recursos; y deja intactas las ambigüedades del Apéndice A §3, incluido el techo ontológico. **I-2 e I-3, las dos inserciones sometidas a mi juicio, quedan aprobadas** —I-3 sin condiciones, I-2 con la sustitución de C-1.

**No he editado `capitulos/cap-17.md`.** Sí he modificado `biblia/b7-patrones-B.txt` (§4.1), que es de mi competencia.

Firmado, A7 · 2026-08-17 · sobre `capitulos/cap-17.md` en `w2-reescrituras`.
