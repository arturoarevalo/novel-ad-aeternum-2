# W9 · Henrik y Mats: dónde y qué

**A2 · rama `w9-huella` · 2026-08-19.** Encargo: dos notas de lectura fría con nombre y línea, sin cambios estructurales. Este documento dice **dónde** y **qué**; no contiene prosa. Anclas por cita literal (B7 §2: los números de línea envejecen, la frase no).

**Pedido total: +37 a +68 palabras en tres ficheros.** Margen de banda disponible: 1.228 (79.772 sobre techo 81.000).

---

## 0 · Antes de nada: la nota de A6-1 apunta a otro capítulo

El encargo asume que «la llamada de "HIJO" que deja pasar en el cap. 38» está en `capitulos/cap-38.md`, y con ello arrastra tres restricciones: primera persona, muerte de Nieve, M1 en 27,5, gate de A7. **Ninguna de las tres aplica.** El texto manda sobre el plan y aquí discrepan.

**La cadena `HIJO` existe exactamente una vez en el manuscrito**, y está en `capitulos/cap-32.md`:

> El técnico llevó el cursor al control de cierre. Entonces el terminal personal de Mats iluminó el estante exterior. `HIJO`.

`cap-32.md` es **el capítulo 38 de lectura, «La oferta»** (B7 §2: `cap-32 → 38. La oferta`). A6-1 numera por lectura en el mismo párrafo de su nota («la tirada burocrática 20–29–31–32», «cap. 44»). `cap-38.md` es el **44, «Norna»**, POV Jean, primera persona.

Consecuencias, todas favorables:

| lo que decía el encargo | lo que es |
|---|---|
| primera persona, POV Jean | tercera, **POV Mats** |
| M1 = 27,5, el más alto del libro | **M1 = 17,7** (`cap-38.md` es el del 27,5) |
| muerte de Nieve, gate de A7 | negociación con Coro + banco de voz |
| 1.380 palabras | 1.753 |

Y la que decide el encargo: **la llamada cae FUERA del span protegido.** `S32-voz` va de «Fije la vista en el centro de la imagen.» a «La muestra incorporada no conservaba ni acreditaba por sí sola el juicio que dirigía la voz.» El párrafo de `HIJO` empieza **después** de esa frase. `proteger.py` calcula el span de `inicio` al final de `fin`: todo lo posterior es terreno libre. El hueco que el crítico señaló es, literalmente, el único trozo de esa escena que se puede tocar.

Sobre M1: es densidad de jerga (términos únicos por 1.000 palabras), no longitud de frase. **Añadir prosa sin término nuevo de léxico BAJA M1.** Ninguna de las intervenciones de abajo puede subirlo.

---

## 1 · MATS — hacerlo. Dos inserciones en `cap-32.md`, +30 a +45 palabras

### Diagnóstico

A6-1: «darle a Mats una escena en la que se equivoque y le cueste —la llamada de "HIJO" que deja pasar en el cap. 38 es el hueco exacto—; hoy es una idea excelente sin cuerpo.» El mismo crítico, en su párrafo de Tema, ya cuenta **«Mats reteniendo íntegros sus propios intentos fallidos de voz»** entre los aciertos del libro. No pide una escena: pide que la que hay pese.

Lo que hoy pasa en el texto: la llamada aparece, el técnico ofrece parar, **«Mats esperó hasta que la llamada desapareció»**, y el libro no vuelve nunca. El hijo no se nombra, no llama otra vez, no aparece en ningún capítulo. La llamada cuesta cero. Por eso se lee como mueble de caracterización («padre frío») y no como error.

Lo que el capítulo ya tiene montado y no cobra: veinte líneas después, Mats ordena **«Incorpórelos a la retención»** y convierte `PROVISIONAL · BORRADO AL CIERRE` en `RETENCIÓN SOLICITADA`; treinta más adelante, «Cada intento fallido conservaba su curva de ajuste, su marca de corte y la sílaba donde se había detenido… **No abrió la columna contigua**». Es decir: el hombre que aprueba borrar miles de trayectorias retiene íntegro cada fracaso de su propia voz, y deja cerrarse lo único vivo que sonó esa tarde. **La rima existe entera. Falta un hecho que permita ponerlas al lado.**

### El error tiene que ser una decisión sobre qué merece conservarse

Aviso de A7 (hoy B7 R4/R8) y de este encargo: la conducta de Mats se motiva por el poder, nunca por el cuerpo. Si deja pasar la llamada porque no puede hablar, es síntoma y hay veto.

**Encuadre obligatorio:** el error de Mats es una **decisión de política de retención** tomada por el hombre cuyo capítulo entero trata de política de retención. Retiene todos sus intentos fallidos y deja expirar una llamada. Eso es 100 % poder y 0 % cuerpo. Ningún otro encuadre está autorizado.

Y hay una salvaguarda mecánica que lo garantiza sin depender del criterio de nadie: **en `cap-32.md`, `mano` va 3 veces e `izquierd*` 4.** La regla de las tres apariciones cierra el vocabulario del cuerpo en ese capítulo. No hay forma legal de escribir el error como síntoma.

### M-1 · ORIENTACIÓN + TENSIÓN · +15 a +25 palabras

**Posición.** En el párrafo que empieza «Mats esperó hasta que la llamada desapareció.», o inmediatamente después. Antes de «—¿Qué ocurre con esas tomas?».

**Qué tiene que hacer.** Dar a la llamada **el mismo tratamiento administrativo que a una toma provisional**: que se cierre sola y deje constancia en el terminal personal. Un hecho, en el idioma de máquina que el capítulo ya habla. Nada más.

**Qué NO puede hacer.** No es un plano de Mats mirando el terminal. No hay gesto, no hay pausa descrita, no hay glosa. El narrador no dice qué siente, no nombra al hijo, no cuenta cuánto duró la llamada ni cuántas veces sonó.

**Técnica permitida.** Registro de máquina o cláusula factual en la voz del capítulo. Sin diálogo nuevo con el técnico (ver abajo por qué).

**Formas cerradas en `cap-32.md` — prohibido producirlas:** `mano` (3), `izquierd*` (4), `comprob*` (4), `cerró` (5), `dejó` (5), `leyó` (4), `retención` (5), `provisional*` (4), `volvió a` (3), `marcó` (3), `sin +infinitivo` (3). **En el techo, no rebasar:** `esperó` (2), `dos veces` (2), `cuenta atrás` (2), `terminal` (2). **Con margen:** `llamada` (1), `HIJO` (1 en todo el libro; como máximo una segunda, nunca una tercera).

**Y una prohibición que no es de cuenta sino de forma:** no escribir una tercera negativa de Mats a una asistencia ofrecida. Ya hay dos —«—¿La cambio? / —No.» y el «—Podemos parar» que él no contesta—. Una tercera convierte su carácter en tic y desperdicia el beat.

### M-2 · AGENCIA · +12 a +20 palabras

**Posición.** En la tercera sección, la del directorio privado de SYNVEV-2. Párrafo nuevo **después** de «…Insertó la credencial y marcó la casilla. **Su nombre quedó como titular del material y primer usuario previsto.**» y **antes** de «Mats abrió el detalle del paquete.»

**Por qué exactamente ahí, y no dos frases más abajo.** El párrafo siguiente termina en «**La mano izquierda tardó en soltar la credencial. Mats la apoyó en el borde de la mesa y esperó a que estuviera quieta antes de continuar.**» Ese es el único beat corporal del capítulo. **Si el beat de la llamada queda pegado a él, el lector cablea «no contestó» con «le temblaba la mano» y el error se vuelve síntoma. Es la trampa exacta que A7 veta.** Colóquese antes, con el párrafo de la interfaz en medio.

**Qué tiene que hacer.** Mats está fijando el alcance de una retención y tiene delante la constancia de M-1. **No la extiende.** La decisión es suya, es consciente, es de dos segundos y no se comenta. Ese es el error, y su precio se cobra solo: nueve páginas después, en `cap-39.md`, «Mats leyó las dos opciones otra vez. / **—La revoco desde hoy.**» El lector que sabe qué desplazó ese corpus sabe por fin qué está entregando.

**Qué NO puede hacer.**
- Ninguna voz enuncia el parentesco entre los intentos retenidos y la llamada no devuelta. B7 R4: «las rimas se quedan en rima», y esta es la más fácil de romper sin darse cuenta. **Hecho, no ecuación.**
- Nada que suene a «yo también sé lo que es que te borren» (B7 R4, literal).
- Ninguna quinta instancia del reclamo de autoría en primera persona con dislocación (§5 techo 7: cuatro, cerrado; `cap-27:35`, `cap-27:57`, `cap-32:85`, `cap-39:147`).
- Ningún mecanismo nuevo: `cap-32.md` tiene **M2 = 0** y sale con 0. Prohibido `acuse` (es léxico de `cap-37`/`cap-39`, subiría M1 de `cap-32`). Prohibido cualquier término nuevo del léxico.
- No es cierre de escena. `cap-32.md` ya aporta un cierre-objeto al recuento M4 del libro (39 en total). Ni M-1 ni M-2 pueden ser la última frase de su sección.

### Lo que queda intacto por decisión, no por olvido

El hijo **no se nombra, no se describe, no vuelve a llamar y no aparece en ningún capítulo del libro.** No es un cabo suelto: es el resultado. Cualquier propuesta que lo convierta en personaje se rechaza sin discusión.

**`cap-39.md` no se toca.** «—La revoco desde hoy.» funciona sola en cuanto M-1 y M-2 existen, y es POV Astrid: ella no puede saber lo que haría falta glosar. Verificar, no editar.

---

## 2 · HENRIK — hacerlo, pero el encargo pide lo contrario de lo que hay que hacer

### Primero, el expediente completo: son once lecturas frías, no tres

El encargo cita tres. Busqué las demás. **Henrik Dahl es la queja más constante de todo el historial de lectura fría del proyecto: lo nombran VEINTE informes, en seis rondas —v0, W2, W3, W4r, W5b y vF—, y ha sobrevivido intacto a siete oleadas.** Doce de los veinte lo dan como respuesta literal a «¿qué personaje se te quedó plano?». Selección:

| ronda | quién | qué dijo |
|---|---|---|
| v0 | beta abandono | «Existe solo para decir frases de marketing. Es una función» |
| v0 | beta sf | «la función "relaciones públicas cínicas" y nunca es otra cosa… **Henrik no tiene ese momento**» |
| v0 | beta sensible | «Existe solo para pronunciar frases de relaciones públicas» |
| v0 | beta literario | «Es el corporativo que dice las frases de márketing y propone la dedicatoria: existe solo para eso» |
| v0 | beta sf | «la función "relaciones públicas cínicas" y nunca es otra cosa» |
| v0 | A6-1 | «el corporativismo cínico de Mats y Henrik llega con las costuras del género ya cosidas» |
| v0 | A6-3 | «Los secundarios funcionales —Gunnar, Tomas, Henrik— resultan más instrumentales» |
| W2 | beta literario | «Henrik es un decorado. **Cada vez que aparece, la novela baja de resolución**» |
| W2 | beta abandono | «un cartel de PowerPoint con nombre» |
| W2 | beta sf | «Existe solo para poner comillas de márketing y ceder la foto» |
| W2 | A6-3 | «Gunnar y Henrik son más funcionales: uno transporta la prueba y el otro encarna la apropiación comunicativa» |
| W2 | A6-1 | «Henrik Dahl (caricatura)» |
| W2 | A6-2 | «Mats y Henrik hablan thriller corporativo genérico» |
| W3 | A6-2 | «Mats, Henrik, la consejera, el letrado y la jueza comparten un solo registro institucional» |
| W4r | A6-3 | «comparativamente esquemático» |
| W5b | A6-1 | «Mats, Henrik y el consejo suenan igual que las tablas del naust» |
| vF | A6-2 | «**Falla el consejo de administración**… Henrik es un cartón de relaciones públicas» |
| vF | beta sensible / abandono | «y nada más» / «dispensador de eslóganes» |

**Y la coartada tiene votos.** Dos lectores se la concedieron ellos mismos, sin que nadie se la sugiriera:

- beta sensible, W2: «Henrik es aún más cartón, **aunque él sí parece pensado así**.»
- beta sf, vF: «un decorado corporativo, **pero ese sí me parece deliberado**.»

Y A6-1 sobre v0 formula la tensión entera en seis palabras: los registros institucionales son «**tan pertinente temáticamente como plano**». Las dos cosas a la vez. Esa es la lectura honesta y hay que sostenerla, no elegir una mitad.

### Dónde se rompe la coartada

A6-2 en W3 pone el dedo en lo que de verdad ocurre: «Mats, Henrik, la consejera, el letrado y la jueza comparten un solo registro institucional». **La queja no es sobre Henrik: es sobre una clase.** Y el libro rescata a todos los demás miembros de esa clase con una sola cosa cada uno —Mats con el banco de voz, Astrid con el caso de 2054, la jueza con «No sé qué es. Sé que alguien la quiere», el responsable de cumplimiento de `cap-22` con «Él la miró por primera vez sin una respuesta preparada»—. **Henrik es el único que no recibe la suya, y por eso se convierte en la etiqueta con que los lectores nombran a la clase entera.** El beta sf lo dice literalmente: «el gesto de la mano izquierda que oculta bajo la mesa lo rescata. **Henrik no tiene ese momento**».

Eso es lo que quiebra la coartada. Si la uniformidad institucional fuera la tesis dicha en forma, el libro no habría rescatado a los otros cuatro. Los rescató. Henrik no es el diseño: es el que se quedó fuera del reparto.

### Y el dato que lo cierra

**Un personaje plano por diseño no tiene grietas. Henrik tiene tres, y ninguna recibe un solo beat de atención narrativa.**

1. `cap-11.md` — aparece la ficha de una menor de dieciséis años con `Riesgo reputacional` y suspensión: **«—¿Ha publicado algo?»** No es un eslogan. Es un hombre enseñando su sistema operativo.
2. `cap-34.md` — Alana acaba de llamarlo «una puta apropiación» a la cara: **«Henrik sostuvo su mirada durante un segundo y marcó el bloque como aprobado.»**
3. `cap-37.md` — todo se ha caído: **«En el pasillo, una técnica le pidió el auricular. Solo a la segunda indicación se lo entregó y continuó hacia la salida.»** Un hombre que no suelta a la primera lo único que le hacía ser la voz.

Las tres son buenas. Las tres son invisibles, y por la misma causa: **Henrik no tiene ni una escena propia.** Sus cuatro apariciones ocurren en escenas de Alana o de Astrid, y en las cuatro el POV está ocupado en otra cosa en el momento exacto en que él hace algo. El recuento: **doce réplicas, cuatro escenas, cero líneas de interioridad, cero POV, en 79.772 palabras.** Los veinte informes leen bien. Lo que describen no es un diseño: es un personaje al que el foco nunca se para a mirar.

**Corolario:** el libro ya sabe hacer este movimiento y lo hace mejor con otro. En `cap-22.md`, el responsable de cumplimiento —sin nombre, sin cargo propio, sin una sola escena— recibe **«Él la miró por primera vez sin una respuesta preparada.»** Ese es el beat que a Henrik le falta, y el libro se lo dio a un hombre anónimo. Eso demuestra intención en `cap-22`, no una política sobre Henrik.

### Pero la receta que la nota sugiere rompe la tesis

«Un momento en que no sea un eslogan» se cumple casi siempre humanizando, y humanizar a Henrik es el peor cambio disponible: convierte al portavoz en el único de la cadena con conciencia y le abre una excusa. El beta de abandono lo dice sin querer: las grietas que él enumera —«Mats tiene la ELA», «Tomas, la operaria», «Astrid, el caso de 2054»— **son precios ya pagados.** Darle a Henrik un precio lo mete en esa compañía y le compra una simpatía que el libro no debe extender a comunicación.

**La dirección correcta es la contraria: darle una preferencia, no una herida.** Un momento donde se le vea querer algo, y que lo que quiere sea indefendible. Eso lo saca de «cartón» sin sacarlo de culpable, y sostiene la villanía sistémica en vez de perforarla.

Y por eso **discrepo de la corazonada del encargo** («basta con que algo le salga mal o le cueste»). Lo que hay que hacer visible de Henrik no es que algo le cueste: es que **nunca le cuesta nada**, y que eso es una posición y no una carencia.

### H-1 · INTERIORIDAD (mínima) · `cap-11.md` · +10 a +15 palabras — REQUERIDA

**Posición.** Entre «—No se ha detectado difusión pública. La suspensión se activó tras una secuencia reproducible de consultas y respuestas fuera del comportamiento previsto.» y «La ficha añadió la última conexión.»

**Por qué aquí y no en `cap-34`.** Cuando un crítico localiza el fallo, lo localiza en el consejo y no en el libro entero: A6-2 sobre vF, «**Falla el consejo de administración**: Mats habla en máximas y Henrik es un cartón de relaciones públicas»; A6-2 sobre W2, «Mats y Henrik hablan thriller corporativo genérico». Es el sitio que los lectores señalan y es donde está su única línea que no es una fórmula.

**Qué tiene que hacer.** Que la respuesta de EDDA **le baste**. Una menor de dieciséis años con la cuenta suspendida queda resuelta para él en el instante en que le confirman que no hay difusión, y vuelve a lo suyo. Nada más. Una cláusula.

**Qué NO puede hacer.**
- Nada de cansancio, familia, duda, reserva privada, incomodidad, ni «sabía que estaba mal». Si un lector puede compadecerlo, se borra.
- Nada que traslade responsabilidad de Alana, de Mats o del consejo a «la máquina».
- B7 R6: no explica, no cura y no culpa a una menor. **Cierra un elemento de riesgo**; ese es el registro y el único.
- No es un movimiento de simpatía hacia Nora ni contra ella. Es indiferencia con criterio.

**Formas cerradas en `cap-11.md`:** `tableta` (6), `Henrik` (6 — **usar pronombre, no el nombre**), `ficha` (5), `acta` (5), `dejó` (4), `públic*` (3), `sin +infinitivo` (3). **Con margen:** `dedicatoria` (1), `riesgo` (1), `difusión` (1), `memoria` (1), `gratitud` (1), `apartó` (1), `notas` (2), `propuesta` (2), `cerró` (2), `miró` (2).

**Spans intactos:** `S11-flashback` (26-nov/UNN) y `S11-consciencia`. Ambos lejos; verificar hash igualmente.

**M2:** `cap-11.md` acarrea 5 mecánicas nuevas heredadas. Sale con 5. Ningún término nuevo.

### H-2 · PAGO · `cap-34.md` · ±0 a +8 palabras — RECOMENDADA

**Posición.** La frase «Henrik sostuvo su mirada durante un segundo y marcó el bloque como aprobado. **Tenía otros nueve minutos de vídeo que cerrar.**»

**El hallazgo.** Esa segunda frase es la **única vez en todo el libro que la narración entra en la cabeza de Henrik, y lo que dice es «estaba ocupado».** El narrador le está dando la coartada. Es exactamente la frase que lo mantiene siendo una función: registra el segundo en que sostiene la mirada y acto seguido lo cancela.

**Qué tiene que hacer.** Sustituirla —no ampliarla— por un hecho registrado de lo que acaba de aprobar. Alana le ha pedido «el crédito exacto»; él ha pedido una decisión; le han dicho «Déjalo como está»; y en `cap-37.md`, al pie de la foto de la cocina, sigue leyéndose **«Material cedido por la familia»**, que es falso. **La sustitución debe dejar al lector capaz de reconocer, tres capítulos después, que ese crédito es el que Henrik aprobó.** Sin decirlo, sin anticiparlo y sin que él lo lamente.

Es sustitución, no adición: al retirar esa frase se liberan una ocurrencia de `vídeo` (3, cerrado) y una de `cerrar` (3, cerrado). El presupuesto puede ser 0.

**Formas cerradas en `cap-34.md`:** `bloque` (3), `crédito` (3), `figuraba` (3), `vídeo` (3), `fotografía` (3), `cerrar` (3). **Con margen:** `auricular` (1), `corrigió` (1), `montaje` (2). **En `cap-37.md`, `auricular` va 2: no producir una tercera allí.**

**M4:** `cap-34.md` ya aporta **4** cierres de escena al recuento del libro (3 objeto + 1 registro, de 39 totales). H-2 va a mitad de sección y **no puede quedar como cierre**.

**Ortotipografía, para A4/A8:** `cap-34` escribe el crédito como campo de interfaz —`CEDIDA POR LA FAMILIA`, comillas simples inversas— y `cap-37` como copia corporativa citada —«Material cedido por la familia», comillas latinas—. **Las dos son correctas por convención del libro** (comillas inversas = salida de máquina e identificadores; latinas = lengua humana citada). **No unificar la tipografía.** La continuidad se consigue por contenido, no por formato.

### Lo que NO se toca

- **`S22-dahl`** (el pasillo, «pasillo de Dahl intacto» en la tabla 5.1): protegido y correcto. La tarjeta, las dos compañeras y la palabra tachada son el retrato en su forma más económica.
- **`cap-37.md`, «Solo a la segunda indicación se lo entregó»:** el beat está completo. Subirle el volumen roba a «Para decir esta frase hemos dejado de ser muchas», que está a cuarenta palabras. Con H-1 hecha, esa línea se lee sola.
- **No se le añade una escena, un POV, un párrafo, una segunda cara ni una vida privada.** Cuatro escenas y doce réplicas siguen siendo el techo.

---

## 3 · Contabilidad, ripples y aceptación

### Presupuesto

| ID | fichero | función | palabras | estado |
|---|---|---|---:|---|
| M-1 | `capitulos/cap-32.md` | ORIENTACIÓN + TENSIÓN | +15 a +25 | pendiente |
| M-2 | `capitulos/cap-32.md` | AGENCIA | +12 a +20 | pendiente |
| H-1 | `capitulos/cap-11.md` | INTERIORIDAD | +10 a +15 | pendiente |
| H-2 | `capitulos/cap-34.md` | PAGO | ±0 a +8 | pendiente |
| | | **total** | **+37 a +68** | |

79.772 → 79.809/79.840. Banda 79.000–81.000: se mantiene con ≥ 1.160 de margen. **Las cuotas están a cero y cuadradas** (`palabras == palabras_real` en los tres ficheros): hay que reasentarlas con `herramientas/actualizar-metadatos.sh` para `cap-11`, `cap-32` y `cap-34`. Nunca a mano.

### Ripples

- M-1 + M-2 → **`cap-39.md`, «—La revoco desde hoy.»** gana precio. **No se edita.** Solo se verifica que sigue funcionando sin glosa.
- M-1 + M-2 → `cap-38.md`, «El corpus privado de Mats queda fuera de NORNA.» sigue igual y ahora se entiende mejor. Sin cambios.
- H-1 → `cap-34.md` «sostuvo su mirada durante un segundo» y `cap-37.md` «Solo a la segunda indicación» se leen distinto. **Sin cambios de texto en `cap-37`.**
- H-2 → continuidad con `cap-37.md` «Material cedido por la familia». **Sin cambios de texto en `cap-37`.**

### Criterios de aceptación, medibles

1. **M8.** Δ total ≤ +68. Banda mantenida. Manifiesto reasentado por herramienta, con historia git.
2. **M1.** Cero términos nuevos de léxico. `cap-32` ≤ 17,7; `cap-11` ≤ 14,6; `cap-34` ≤ 17,6. (Bajan por denominador; si suben, hay jerga nueva y se revierte.)
3. **M2.** `cap-32` = 0, `cap-34` = 0, `cap-11` = 5. Sin variación.
4. **M4.** Los cierres de escena del libro siguen en 29 objeto + 10 registro. Ninguna inserción es última frase de sección.
5. **M9.** Hash invariable en `S32-voz`, `S32-necesarias`, `S32-amenaza`, `S32-resumen`, `S32-cierre`, `S11-flashback`, `S11-consciencia`, `S34-cohorte`, `S34-anos-jm`, `S34-cierre`, y en los 129 spans.
6. **Tres apariciones.** Ninguna forma listada arriba como cerrada aparece una vez más. Verificación por conteo, no por criterio.
7. **B7.** R4 (ninguna rima enunciada; nada de la enfermedad de Mats junto a la muerte de Jean), R6 (Henrik no explica, cura ni culpa a una menor), R8, §5 techo 7 (la forma dislocada de Mats sigue en cuatro). **Y las tres preguntas de B7 §6 contestadas por escrito antes de redactar una línea** — advertencia honesta: la pregunta 1 («¿qué punto de la Carta mejora esta página?») se contesta **«ninguno: responde a la nota de un crítico»**, que es el caso en que B7 §6 dice que la respuesta es no. **Esa regla gobierna las páginas que tocan la elipsis, no las que tocan a un directivo de comunicación o la política de retención de un banco de voz.** Ninguna de las cuatro inserciones se acerca al 26 de noviembre, al naust, al trayecto, a «Despedida» ni a sus cuatro huecos, y ninguna necesita que una voz con autoridad sostenga causa, descanso ni identidad. **La pregunta 2 y la 3 salen limpias.** Aun así: **esto lo decide A7, no yo.** Es el punto de gate.
8. **Prueba de lector, barata y decisiva.** Compilar un extracto con las cuatro escenas de Henrik —`cap-11` (consejo), `cap-22` (pasillo), `cap-34` (fotos), `cap-37` (final)— y pasarlo por `herramientas/critica-fria.sh` con `lector-frio`, pregunta única: **«¿Qué quiere este hombre?»** Pasa si la respuesta es una preferencia («que la marca no sufra», «cerrar el bloque a tiempo»). Falla si es «no sé» o «decir frases». Es la misma pregunta antes y después; un extracto, no el libro.

### Checklist para A5 / A7 / A8

- [ ] A5 · diff limitado a `cap-11.md`, `cap-32.md`, `cap-34.md`. Cero cambios en `cap-37.md`, `cap-38.md`, `cap-39.md`, `cap-22.md`.
- [ ] A5 · conteo de las formas cerradas, antes y después, capítulo a capítulo.
- [ ] A5 · M-2 **no** es adyacente al párrafo «La mano izquierda tardó en soltar la credencial…». Si lo es, se revierte sin discusión.
- [ ] A7 · las tres preguntas de B7 §6 contestadas por escrito en la orden, antes de redactar.
- [ ] A7 · veto explícito sobre cualquier borrador donde el silencio de Mats se explique por la enfermedad, aunque sea por adyacencia.
- [ ] A7 · veto explícito sobre cualquier borrador donde Henrik dude, lamente o se canse.
- [ ] A8 · `HIJO` ≤ 2 en el manuscrito. El hijo sin nombre, sin descripción y sin segunda llamada.
- [ ] A8 · no unificar la tipografía de los dos créditos (`cap-34` inversas / `cap-37` latinas).
- [ ] A0 · `actualizar-metadatos.sh` para reasentar las cuotas de los tres ficheros.

---

## 4 · Las dos preguntas del encargo, contestadas

**¿Se debe hacer lo de Henrik?** Sí, y no por la razón que se propone. Su planitud no es diseño —tiene tres grietas escritas y ninguna mirada—, pero la solución no es humanizarlo. Es dejar que la narración se pare **una vez** en lo que él prefiere, y que lo que prefiera sea impresentable. Coste: 10 a 23 palabras.

Y sobre la respuesta legítima que el encargo me ofrece: **la he buscado de verdad y tiene dos votos** —el beta sensible de W2 y el beta sf de vF dicen los dos que la planitud de Henrik parece deliberada—. **Aun así la rechazo**, y por un motivo que no es de gusto: el libro rescata con un gesto propio a los otros cuatro miembros de su misma clase institucional —Mats, Astrid, la jueza, el responsable de cumplimiento de `cap-22`—. Una uniformidad con cuatro excepciones no es una tesis dicha en forma: es un reparto con un hueco. Y veinte informes en seis rondas señalando el mismo nombre no es una opinión sobre un personaje: es una medición.

**¿Se debe hacer lo de Mats?** Sí, y es la más barata de las dos porque el 90 % está escrito. Pero llevaba montada sobre el capítulo equivocado: el sitio es `cap-32.md` (38 de lectura, «La oferta»), tercera persona, M1 17,7, **fuera del span protegido**, y no `cap-38.md`. Con el capítulo corregido, el riesgo que hacía dudar al encargo —M1, primera persona, la muerte de Nieve, el gate— desaparece; el único riesgo real que queda es la adyacencia corporal del punto M-2, y está señalado con su ancla.
