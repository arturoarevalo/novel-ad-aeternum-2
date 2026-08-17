# G-A2 · Gate de autor sobre los seis capítulos nuevos (W3)

**A0 · 2026-08-17 · rama `w3-nuevos`, sin fusionar.** El plan §7.5 define este gate como «aprobar los seis capítulos nuevos antes de integrarlos» y lo llama «el punto de mayor riesgo de deriva de voz». **Me detengo aquí: no fusiono sin tu decisión.**

---

## 1. Qué hay escrito

| | capítulo | orden | POV | palabras | M1 | tope | M2 | M4b |
|---|---|---|---|---|---|---|---|---|
| N5 | Turno | 7.5 | Jean | 1.822 | 4,9 | ≤ 8,0 | 0 | 0,5 % |
| N1 | La primera cita | 9.5 | Maja | 2.070 | 0,0 | ≤ 6,0 | 0 | 0,0 % |
| N2 | Instituto | 16.5 | Nora/Jessie | 1.946 | 0,5 | ≤ 6,0 | 0 | 0,8 % |
| N3 | Inventario | 22.5 | Maja | 3.572 | 2,2 | ≤ 6,0 | 0 | 1,4 % |
| N4 | Interferencias | 25.5 | Nora→Maja→Jessie→Jean→Maja | 3.156 | 3,8 | ≤ 8,5 | **1** | 1,0 % |
| N6 | Acta | 40.5 | Aslak | 1.641 | 2,4 | ≤ 6,0 | 0 | 0,0 % |

**14.207 palabras nuevas.** Los seis dentro de banda. **Una sola mecánica nueva en toda la oleada**, la que aprobaste en G-A1 (el aviso de exposición reputacional por proceso). Cero cierres-objeto en cinco; N3 tiene uno y su tope era uno. Manuscrito: 47 capítulos, **77.849 palabras** (v0: 62.750).

M7 **0 errores** con los seis decimales intercalados: la secuencia de fechas sigue siendo monótona en los seis puntos de inserción. M9 OK. Validador 0 avisos.

---

## 2. Criterios del gate (plan §6, fila W3)

| Criterio | Resultado | |
|---|---|---|
| **Carta F en N1 y N3** | A7 firma los dos, sin veto y sin corrección de texto en N1 | ✅ |
| **Huella B6: «¿parece del mismo autor?» ≥ 4/5** | 5 lectores ciegos sobre 10 fragmentos mezclados: ninguno separa lo nuevo de v0 | ✅ |
| **Anti-regresión por eje** | Global 8,5 · Ritmo 7,5 · Duelo 9,5 · Tema 9,0; ningún eje cae contra el control de deriva | ✅ |
| **Gate de autor** | pendiente | ⏸ |

### 2.1 Sensibilidad

Los seis capítulos tienen dictamen firmado de A7 y **ninguno lleva veto**: `a7-w3-n1.md`, `a7-w3-n3.md`, `a7-w3-n2-n6.md`, `a7-w3-n4-n5.md`. Una sola corrección de texto en toda la oleada (el jersey de N3, §4). A7 hizo además la segunda lectura obligatoria del diff posterior a A4 y levantó la condición que bloqueaba el merge, tras verificar que los seis capítulos **solo han menguado** y que las frases protegidas están intactas byte a byte.

**Las dos frases de la bolsa de viaje quedan autorizadas literalmente**, cumpliendo tu decisión de G1:

> «La bolsa de viaje había vuelto en diciembre con la hoja de efectos personales y seguía en el garaje, junto a la puerta.»
> «Maja la subió al altillo, con lo que se guardaba, y escribió la fecha en la hoja.»

A7 deja siete prohibiciones hacia adelante (C-4 de `a7-w3-n3.md`), la primera de las cuales es que la bolsa no vuelve a aparecer nunca. Ya ha verificado que el altillo de N4 no la menciona.

### 2.2 La prueba de mano única

Diez fragmentos de unas 180 palabras —cinco de capítulos nuevos y cinco de v0, emparejados por registro— barajados y entregados a cinco lectores ciegos con una sola pregunta: si alguno parece escrito por otra mano.

**Ninguno de los cinco separa lo nuevo de lo viejo.** Los dos que agrupan fragmentos lo hacen por punto de vista, no por autoría, y mezclan material nuevo con material de v0 en el mismo grupo: uno señala los fragmentos 3 y 4 (N5 y el cap. 15) y lo atribuye a «convención de punto de vista deliberada, no injerto»; otro agrupa 1, 6, 7 y 8 (N1, N2, cap. 6 y cap. 28) por «minimalismo escénico en pasado» y concluye que «es diseño». Los tres restantes no señalan a nadie.

### 2.3 Anti-regresión

Mediana de los tres críticos fríos sobre `compilado/ad-aeternum-w3.md`, con el jurado vigente:

| eje | c1 | c2 | c3 (sol) | **mediana w3** | baseline | Δ | v0 medido hoy |
|---|---|---|---|---|---|---|---|
| premisa | 8,5 | 8,5 | 9 | **8,5** | 8,5 | = | 8 |
| estructura | 8 | 8 | 8,5 | **8** | 8,5 | −0,5 | 8 |
| prosa | 8 | 8,5 | 9 | **8,5** | 8,5 | = | 8 |
| diálogo | 8,5 | 8 | 8,5 | **8,5** | 8,0 | +0,5 | 8,5 |
| personajes | 8,5 | 8,5 | 9 | **8,5** | 8,5 | = | 8 |
| mundo | 8,5 | 8,5 | 8,5 | **8,5** | 9,0 | −0,5 | 8 |
| ritmo | 7,5 | 7,5 | 7,5 | **7,5** | 7,5 | = | 7,5 |
| trama | 8 | 8,5 | 8,5 | **8,5** | 8,5 | = | 8 |
| duelo | 9,5 | 9,5 | 9,5 | **9,5** | 9,5 | = | 9,5 |
| tema | 9 | 9 | 9 | **9** | 9,0 | = | 9 |
| **global** | 8,5 | 8,5 | 8,5 | **8,5** | 8,5 | = | 8,5 |

Los dos −0,5 caen otra vez en estructura y mundo, y otra vez **el control de deriva los explica**: el mismo juez, el mismo día, puntúa v0 en 8 y 8 en esos dos ejes, por debajo de w3. En la comparación pareada juez contra sí mismo, w3 sube en premisa, prosa, personajes, mundo y trama, y baja en diálogo. Sin veto en Duelo.

**Un dato de trama que merece la pena:** el clímax pasa de «se gana y se concede en un punto» (W2) a «**se gana en tres cuartas partes**», y el crítico acredita la cadena de pagos citando, entre otros, «el expediente policial que le costó entrar en Fyret» — que es material de N2.

---

## 3. Lo que hay que decidir, y no lo decido yo

### D-1 · El espejo de N4 (las 500 palabras de R4)

**Un crítico de tres nombra N4 como el capítulo donde estuvo más cerca de abandonar**, y su razón es exactamente la que A2 anticipó al escribir la orden:

> «Cuatro derrotas administrativas encadenadas […] cuyo tema es que nada lo firma nadie. Es el capítulo más puro y el más inerte: la desmoralización burocrática se traslada al lector con demasiada eficacia, y **el tramo de Jean deja por primera vez de generar personaje para ilustrar una tesis**.»

Esa última frase es el riesgo que la propia `OT-N4` §6 declaró y para el que dejó preparada una salida: **reversión completa de I-5, y el capítulo vuelve a 2.400 palabras sin daño**. Los otros dos críticos no lo señalan, y el lector frío del capítulo entiende bien lo que ocurre (3/5, con resumen correcto).

Contra la reversión: el espejo es lo único del libro que responde a lo que los cuatro lectores beta pidieron por separado —entender qué es Coro—, y lo hace sin darle un cabecilla. A favor: es la única página del manuscrito donde Jean deja de ser personaje.

**A0 recomienda conservarlo** y volver a medirlo en el hito de scoring completo de W5, cuando los ripples del 26, el 32 y el 36 estén puestos y el capítulo no cargue solo con la explicación. Pero es tu decisión, y la reversión está preparada y no cuesta nada.

### D-2 · El capítulo 8, otra vez

En el gate de W2, el capítulo 8 había **desaparecido** de la lista de «dónde estuve a punto de abandonar» de los tres críticos. Ahora vuelve, en boca de uno de ellos, y con un matiz importante: **cita la regla de memoria y la llama espléndida**, pero dice que se pide «como apuesta emocional sin escena que la sostenga». Es decir, la regla funciona y el capítulo sigue siendo árido.

N5 —el capítulo-escuela que debía preparar ese terreno— no ha bastado por sí solo. No propongo tocar el 8 ahora: W4 y W6 aún no han pasado por su vecindario.

### D-3 · N3 y su longitud

El mismo crítico señala N3 como segundo riesgo: «cuatro mil palabras de inventario doméstico». Es el capítulo más largo del libro y lleva dentro las 1.200 de R1. El lector frío le da 4/5 y lo resume con precisión. Lo dejo anotado sin recomendación de recorte: si algo sobra ahí, W6 es el sitio.

### D-4 · Recalibrar M6b (viene del hallazgo de §4)

---

## 4. Hallazgos de la oleada

1. **La métrica de voces medía mal desde F1.** La muestra ciega de las gemelas de N2 dio 20,8 · 62,5 · 20,8 % con el azar en 50 %: dos pases por debajo del azar, que en una tarea binaria solo puede significar etiquetas invertidas. Con un ancla de dos líneas y sin tocar una sola réplica: **86,1 %**. Y el control de v0 con la misma ancla: **64,3 %**. Es decir, N2 mejora la diferenciación de las gemelas en **+21,8 puntos** y cumple el criterio de G1 con holgura — pero también significa que **v0 estaba en 64,3 % y no en el 21 % que registró D1**. El diagnóstico que justifica el peso de T4 en W4 y W6 estaba inflado por el instrumento. Detalle en `informes/m6b/m6-voces-w3.md`. **Antes de dimensionar W4 y W6 hay que rehacer la medición global con ancla por personaje.**
2. **La auditoría adversarial volvió a encontrar lo que nadie más vio.** N5 se había inventado una cuota («Jean gasta ESCALAR una vez por serie… consume esa única salida») donde el canon de 7:39 solo tiene una disciplina que ella se impone — y donde el capítulo 7 la muestra escalando tres veces. A5 revisó ese punto exacto y lo dio por bueno. Corregido por A4 devolviendo el verbo de v0: «Jean reserva ESCALAR».
3. **Un crítico frío encontró un error factual que nadie buscaba:** en N1, Maja apagaba el motor y once líneas después «el motor siguió en marcha hasta que Maja lo apagó». Corregido.
4. **A7 detectó un hueco de proceso mío:** N4 y N5 no tenían dictamen suyo, y N5 dispara T7 por caer en el rango de los capítulos 1–10 — su propia OT lo decía en la cabecera y yo no lo enruté. A7 los leyó y los aprobó.
5. **Un fallo de parser que W3 destapó:** `proteccion: no` se convertía en booleano `False` (YAML 1.1) y hacía fallar al validador. Ningún capítulo de v0 lo usaba, porque los 41 son `nucleo` o `total`. Corregido alineando el parser con YAML 1.2.
6. **Canon nuevo que A1-mantenimiento debe registrar tras este gate** (detalle en `a5-w3-continuidad.md` y `a7-w3-n3.md` C-4): el instituto y sus grupos; la fotografía del funeral publicada; el reparto de objetos de 2059; las cajas del piso y su devolución el 31-dic; el acta del kystbrukslag; y la bolsa registrada **en términos estrictamente administrativos**.

---

## 5. Lo que te pido

1. **Aprobar o no los seis capítulos** (el gate propiamente dicho).
2. **D-1**: conservar el espejo de N4 o revertirlo a las 2.400 palabras.
3. **D-4**: autorizar la recalibración de M6b con ancla antes de dimensionar W4 y W6.
4. **Fusionar `w3-nuevos` en `main`** — no lo hago sin tu visto bueno. Tras la fusión, A1-mantenimiento registra los seis en `capitulos[]` con `origen: "REVISIÓN 10"`, que es la convención que el manifiesto exige y que solo puede hacerse **después** de superar este gate.

---

## 6. Consumo de W3

Subagentes en sesión ≈ **2,6 M tokens** (A3b ×5 1,54 M · A3a 275k · A4 304k · A5 203k · A7 ×5 599k · A2 164k). Lecturas en frío fuera de sesión: **10,28 USD** (A6 ×4 7,36 · mano única ×5 1,41 · M6b ×15 0,98 · lector frío ×6 0,52). Sin coste por token bajo tu suscripción: A6-3 con `gpt-5.6-sol` y la auditoría adversarial ×3.

Acumulado de la sesión (W2 + W3): ≈ 4,6 M tokens de subagentes y **34,37 USD** de lecturas en frío.
