# D1 · Auditoría de reglas del sistema contra B3

**Fase 1 · F1.7 · A5 (continuidad).** Baseline v0. Fuente: `biblia/b3-canon-sistema.md` §19–§21 + lectura directa de los capítulos citados. No se ha tocado ningún capítulo ni ningún fichero de `biblia/`. Convención de cita `cap:línea` = `cat -n` sobre el fichero completo (frontmatter incluido), igual que B3. «Acreditado» = leído literalmente en el texto; «inferencia» = razonamiento de A5. Protecciones consultadas en `protegidos/spans.json` (spans hash) y `ficheros_total` (diff 0).

Nota de protección relevante: **cap-05, cap-20, cap-23** son `ficheros_total` (intocables). Los demás capítulos citados son `proteccion: nucleo`: solo los spans listados en `spans.json` están hash-protegidos; el resto es editable dentro del estado de la tabla 5.1.

---

## 1. Verificación de F1–F16

Todas las citas de B3 §19 se han comprobado **literales y en la línea indicada** salvo las desviaciones que se anotan. Columnas: veredicto · gravedad · decisión (A sembrar / B restringir / C ambigüedad asumida) · dónde · coste · qué NO hacer.

### F1 · Alcance de `/0000` sobre otras continuidades
- **Citas:** cap-13:155 («Jean podría confirmarlo desde `/0000` y cerrar la unidad») ✔; cap-13:201 (`declarando que /0188 es incoherente`) ✔; cap-30:65 («La convocatoria no me dio autoridad sobre nadie») ✔; cap-30:213 («autoridad solo para reservar el canal») ✔; cap-36:65-71 (`CERRAR JM-L/0188`, «Jean rechaza ambas») ✔; cap-38:139-161 (abre ventana a Nieve, «devuelvo ambas a la cola») ✔.
- **Veredicto: APARENTE.** El sistema *ofrece* autoridad y Jean la *rechaza* siempre (patrón deliberado). En 38 sí opera sobre la ruta de Nieve, pero el texto ya lo enmarca en NORNA («El origen solo atribuirá su respuesta», 38:39; «Mantengo la ruta libre de tareas», 38:145). La asimetría no se enuncia como regla, pero está cubierta por la retención de `/0000` (cap-11:135).
- **Gravedad: MEDIA** (un relector puede leer los ofrecimientos de 13/17/36 como un poder selectivo de `/0000`).
- **Decisión: A.** Una regla D5 en N5 u 8, voz de Jean-ingeniera, ata la asimetría a la retención: «Regla: el origen retenido puede cerrar lo que las derivadas dejan abierto. Yo no lo uso.» Coste ≈ +25 pal. **No hacer F1-B:** reescribir 38:139-161 tocaría el núcleo protegido (span `S38-nieve`, 38:159-161) y el capítulo es `P`.

### F2 · Capacidad que viaja entre orígenes
- **Citas:** cap-21:111-139 (Nieve presta «una fracción» de margen) ✔; cap-30:93-97 (Madre «Con lo tuyo») ✔; cap-36:49-63 (Jean agota la capacidad de Cuchillo) ✔; cap-13:231 («Repartimos el estado») ✔.
- **Veredicto: REAL.** Tres mecanismos distintos de transferencia de capacidad sin regla unificadora previa; a un lector atento «capacidad» significa cosas distintas en cada caso.
- **Gravedad: MEDIA.**
- **Decisión: A.** Enunciar una vez la regla unificadora (la capacidad pertenece a la ruta, no a la voz) en **N5** (capítulo nuevo, sin problema de protección) o en 13 RW. Coste ≈ +30 pal. **No hacer F2-B** (suprimir la cesión de Nieve en 21): es un beat emocional con peso y roza `S21` spans.

### F3 · Encapsular y transferir un fragmento de credencial
- **Citas:** cap-30:227-233 («Cuchillo lo encapsula antes de que desaparezca la entrada») ✔; cap-36:23-31 («`/0188` ha alcanzado el control de accesos del Auditorio»; «su alcance sigue limitado a apelaciones, aislamiento y cierres») ✔.
- **Veredicto: REAL** (semisembrado: 36:23 dice «Encadenando una salida con la siguiente», y «cierres» está en su alcance).
- **Gravedad: MEDIA-ALTA.** Es el salto de capacidad más visible: una continuidad de apelaciones que alcanza el control físico de accesos de un auditorio. Puede leerse como «el sistema hace lo que la trama necesita».
- **Decisión: A.** En cap-17, línea ~89 (editable; los spans de 17 son 147+, 197) reforzar que una medida sin destino *queda encadenable* en el residuo (ya casi: 17:89 «El tiempo de la apelación termina sin que nadie reciba la medida»). Coste ≈ +30 pal. Alternativa **B**: limitar el objetivo de 36 a «cerrar el sector» del canal educativo (un cierre, no el Auditorio entero); coherente con «cierres» pero toca el núcleo dramático de 36. **No hacer:** no dotar a Cuchillo de acceso a redes o producción (excede §8).

### F4 · Qué sabe Jean del calendario (12:47)
- **Citas:** cap-28:197-199 (audio «…20…23:00…», «El campo de origen seguía vacío») ✔; cap-31:73 («Sabía que había una selección. No que fuera esa noche») ✔; cap-31:87 («La fase común entra a las doce cuarenta y siete —dijo Jean») ✔; cap-25:203 (`DESPLIEGUE GLOBAL · 21-ENE-2061 · 12:00`) ✔.
- **Veredicto: REAL, menor.** El interior de 25 solo trae `12:00`; el `12:47` que Jean enuncia en 31:87 no tiene fuente interior mostrada. El exterior sí lo conoce (34:135; 34:207 Mats).
- **Gravedad: BAJA** (el `12:47` circula fuera; el calendario de la candidatura puede portarlo; casi ningún lector lo rastrea).
- **Decisión: C** (ambigüedad asumida). El audio de 28 «podía pertenecer a cualquiera» (28:153) ya desactiva la contradicción con 31:73: el emisor de «no lleguéis tarde» no es `/0000` (candidata: Madre/`PROGRESIÓN ESTABLE`, que cruza el corte, cap-34:113). **No hacer F4-A:** añadir el `12:47` en 25 obligaría a insertar junto al span protegido `S25-fecha`; innecesario.

### F5 · Cronología de `CARIES`
- **Citas:** cap-10:17 (`CARIES`, POV Nora, 5-dic) ✔; cap-15:39 (`/0000` introduce `CARIES`, 12-dic) ✔; cap-23:101 (La Jardinera: «Una vez. Elegí esa palabra… No puedo saber si esa fue la aparición que viste tú») ✔.
- **Veredicto: APARENTE / YA COHERENTE.** La `CARIES` del 5-dic es anterior a la de `/0000` (12-dic) y no puede ser suya; el texto reparte la autoría entre `/0044`, `/0000` y el mismo campo que usa Cuchillo (15:107). Ambigüedad protegida (Ap. A §3).
- **Gravedad: BAJA.**
- **Decisión: C.** **No hacer:** prohibido «arreglar» haciendo de `/0000` la emisora del 5-dic. cap-23 es `ficheros_total` y cap-10 tiene la serie protegida (`S10-series`): intocables.

### F6 · La asamblea como espacio
- **Citas:** cap-30:15-29 ✔; cap-23:247 ✔.
- **Veredicto: APARENTE.** El acceso se explica por prioridad de candidatura (30:27) + La Jardinera como anfitriona técnica (30:19-25, «señala qué partes de la costa siguen allí y quién las sostiene»).
- **Gravedad: BAJA** (se lee como convención poética del jardín compartido).
- **Decisión: C.** Opción B (reforzar a La Jardinera como anfitriona) ya está casi en página. **No hacer:** no inventar una «regla de acceso» al jardín.

### F7 · `/0000` sabe que fue Nora
- **Citas:** cap-15:69-71 («Puede ser Nora» / «También puede ser cualquier alumna») ✔; cap-21:17 («Nora eligió la dirección de la tercera nota») ✔; cap-21:45 (Coro: «Nuestra hija utilizó una pauta») ✔.
- **Veredicto: APARENTE.** La certeza de 21 está sembrada por la sesión de 20: la credencial «registra… la identidad de quien abra la sesión» (20:21) y Nora consiente ser grabada. Entre 15 (incierto) y 21 (cierto) media ese registro.
- **Gravedad: BAJA.**
- **Decisión: C.** cap-20 es `ficheros_total`: no se toca, pero tampoco hace falta (la cobertura existe).

### F8 · Retirar salidas
- **Citas:** cap-08:27 («Jean retira la salida. El acuse permanece») ✔; cap-17:37 («Jean retira el rechazo») ✔; cap-15:175 (`SALIDA EMITIDA · RETIRADA LOCAL NO DISPONIBLE`) ✔.
- **Veredicto: YA COHERENTE.** En 8 y 17 son salidas **no emitidas** (retirables); en 15 es **emitida** («cruza»). La regla ya distingue.
- **Gravedad: BAJA.**
- **Decisión: C.** Opcional: D5 en 8 RW enunciando «cruzar» como umbral (barato, aclara). **No hacer:** nada obligatorio.

### F9 · Latencias de 9 s / 6 s
- **Citas:** cap-20:281-299 (contador 4 s → cuarta nota a los 9) ✔; cap-22:137-155 («nueve segundos»; «Los relojes no comparten sincronización acreditada. Retira el intervalo») ✔; cap-31:93 (seis segundos) ✔; cap-38:211 (seis segundos) ✔.
- **Veredicto: REAL pero intencional.** Nadie explica por qué una ejecución a 16.000× tarda 9 s; el texto lo dramatiza como irresuelto (Nora lo nota, Astrid lo descarta).
- **Gravedad: BAJA** (la ambigüedad es tema).
- **Decisión: C** (no resolver). **No hacer:** que ningún personaje con autoridad narrativa explique la latencia.

### F10 · Ventana reflexiva
- **Cita:** cap-19:129 (`VENTANA REFLEXIVA` cerrada; span `S19-reflexiva`) ✔. Aparece una vez y nunca se abre.
- **Veredicto: YA COHERENTE** (no es trampa; es plantado sin pago = decisión de A0 sobre el backlog R2).
- **Gravedad: BAJA.**
- **Decisión: C** para continuidad (dejar como cierre-símbolo). Si A0 activa R2, abrirla en Parte III; no es competencia de A5.

### F11 · Estados de Madre cruzan el corte
- **Citas:** cap-34:109-125 (`DISTRIBUCIÓN ATÍPICA`, `JM-L/0007 · PROGRESIÓN ESTABLE`, «etiquetas que habían cruzado el corte») ✔; sembrado en 15:85 («Conserva esa estrategia bajo mi origen») ✔.
- **Veredicto: APARENTE.** Funciona como caracterización de la complicidad de Alana (ve la alerta y «deja el botón intacto», 34:125), no como truco de sistema. El «pago» es moral, no de trama.
- **Gravedad: BAJA.**
- **Decisión: C** (dejar; es una buena siembra). **No hacer F11-B** (suprimir la alerta de 34): se perdería.

### F12 · «Más de tres mil» vs 1.185
- **Citas:** cap-29:23 («Alcanzaba más de tres mil rutas»; span `S29-orden`) ✔; cap-34:85-91 (`4.096 − 2.911 = 1.185`) ✔; cap-34:205 (Alana: «lo que hicimos con las mil ciento ochenta y cinco») ✔; cap-31:55,71 («más de tres mil») ✔.
- **Verificación A5:** la aritmética **cierra** contra la cohorte: `597 (Coro) + 2.311 (enlazadas) + 3 (separadas) + 1.185 (perdidas) = 4.096` ✔ (cap-38:75-79). Si el 9-ene había «más de tres mil» operativas y quedan 2.911, la consolidación del 20-ene eliminó < ~1.000; el resto de las 1.185 se perdió antes (La Jardinera en 30, la continuidad de cinco segmentos en 34:73). Coro sobrevive casi entero (~600 → 597), coherente con su diseño «reparte estado para resistir pérdidas» (13:231).
- **Veredicto: APARENTE** (coherente leído como pérdida acumulada vs cohorte). Única fricción: la frase de Alana (34:205) sugiere que la consolidación hizo las 1.185 completas.
- **Gravedad: MEDIA** (un lector que cruce las cifras puede tropezar).
- **Decisión: C + canon.** Fijar en B1/B3 el canon numérico (**1.185 = pérdida acumulada respecto a la cohorte; prohibido escribir «la consolidación borró 1.185»**) — es la Duda §21.1, **a resolver antes de W2**. Sin cambio de prosa; la frase de Alana se sostiene como su imprecisión. **No hacer F12-A** (meter «cuatro mil noventa y seis» en 29): tocaría el span `S29-orden`.

### F13 · Coro retira el extremo pero no la sesión de 23
- **Citas:** cap-21:19-21 («Las ramas de Coro lo han retirado de la sincronización local») ✔; cap-32:97 (`PODEMOS IMPEDIR EL ACCESO SIN DAÑO FÍSICO`, CH-1) ✔; corte de 23 `MANTENIMIENTO NO PROGRAMADO` sin autor (cap-23, `ficheros_total`).
- **Veredicto: APARENTE** para continuidad (el corte de 23 es deliberadamente sin autor). El pago de CH-1 es cuestión de ledger (B4)/N4, fuera de A5.
- **Gravedad: BAJA** (continuidad).
- **Decisión: C** (mantener el corte de 23 sin autor; cap-23 es intocable de todos modos). El pago dramático lo asume N4 (A2).

### F14 · «Coro mantiene el identificador de Madre»
- **Cita:** cap-13:257 («Coro mantiene el identificador de Madre y una referencia que solo acredita que Nieve existió») ✔. Madre sigue separada en todo v0 (30:77 «Madre no habla por ella» ✔).
- **Veredicto: REAL-menor** (aparente contradicción: si Coro tiene el identificador de Madre, ¿por qué Madre está separada? Se resuelve leyendo «una copia», no la voz).
- **Gravedad: MEDIA.**
- **Decisión: A.** Reformular 13:257 en la RW: «una copia del patrón de Madre» (línea editable; no está entre los spans de 13). Coste ≈ +3 pal. La opción B (que Madre lo desmienta en 30) **ya existe** en 30:77. **No hacer:** no dar a Coro control sobre Madre.

### F15 · La llave «encaja» en un armario HVAC
- **Citas:** cap-35:145 (la llave en el alojamiento del armario) ✔; cap-35:185-199 (la consola de `INC-441` muestra «el identificador conservado por la llave de Gunnar Rydberg» + `HOJA 1 · VEHÍCULO` / `HOJA 2 · HVAC AD NIDHOGG` / `CA INTERMEDIA · HVELV SIKKERHET` / `CADENA CONTRACTUAL · KRONFJORD KAPITAL`) ✔.
- **Veredicto: APARENTE.** Está sembrado: ambas hojas comparten la CA intermedia de Hvelv y la cadena de Kronfjord (cap-24:67-79; segunda hoja HVAC cap-34:15-25). «Solo compartían la autoridad intermedia… La coincidencia documentaba esa relación» (34:23).
- **Gravedad: MEDIA→BAJA** (el lector puede no conectar la CA compartida).
- **Decisión: C**, con **A opcional**: una línea en 24 donde Tomas reconozca en la hoja de Hvelv un identificador ya visto en el informe de Gunnar (cap-24 es E +300; línea editable, no toca `S24-once`/`S24-cierre`). Coste ≈ +15 pal. **No hacer:** no explicar el mecanismo por boca del narrador.

### F16 · Alana renueva la sesión «desde su reloj»
- **Citas:** cap-20:97 («Alana renovó la validez desde su reloj sin tocar la lámina») ✔; cap-20:33 («La revisión obliga a Armstrong a mantener el acceso») ✔; cap-19:255 («La autorización de acceso a despliegues había pasado de ejecutiva a colegiada») ✔; cap-27:37 ✔.
- **Veredicto: YA COHERENTE.** El control colegiado recae sobre «acceso a despliegues»; la credencial de auditoría es un dominio distinto que Armstrong está obligada a mantener. Sin contradicción.
- **Gravedad: BAJA.**
- **Decisión: C** (nada). cap-20 es `ficheros_total`.

---

## 2. Flexiones adicionales (no listadas en B3 §19)

### AF-1 · Cobertura de Tomas «HASTA 12:47» vs trabajo físico posterior
- **Citas:** cap-35:189 (`COBERTURA LOCAL · TOMAS EIDE · HASTA 12:47`); cap-35:155 (`PETICIÓN LOCAL · INICIADA · 12:46:01`); cap-35:223 (Tomas: «La cobertura sigue conmigo al cruzar»); cap-35:239-245 (`RESELLADO DIAGNÓSTICO · 00:11`, cruce tras el contador); regla en cap-34:265-273 (validar durante la cobertura asocia identidad/incidencia/hora/puerta).
- **Veredicto: APARENTE.** La vinculación se registra dentro de la cobertura (~12:46:30) y la consola «fijó hora, incidencia y puerta» al `ACEPTAR` (35:215); el trabajo físico (cruzar el fail-secure, colocar la red) ocurre tras 12:47, pero el texto asegura que la cobertura persiste al cruzar (35:223). Es la estrechez de plausibilidad que ya señaló la crítica («demasiadas cooperaciones en nueve minutos»), no una regla nueva.
- **Gravedad: BAJA-MEDIA.**
- **Decisión: C** (ambigüedad asumida; la línea 35:223 la cubre). **No hacer:** no alargar el reloj ni tocar cap-35 (spans `S35-acepta`/`S35-cierre` adyacentes).

### AF-2 · Aritmética de cohorte y tasa AÑOS-JM — **verificadas, coherentes**
- `597 + 2.311 + 3 + 1.185 = 4.096` ✔. Tasa constante ~16.000× la línea base en los tres cortes: `979,7` (19-dic, ~15.955×), `2.401,6` (corte 20-ene 23:00, 16.000×), `2.427,4` (21-ene 13:07, 16.000×; 2.427,4 / 55,41 días = 43,8 años-JM/día ✔). No hay flexión; canonizar la tasa (Duda §21.7).

### AF-3 · Persistencia del fragmento de credencial de Cuchillo 9 días (30→36) a través de la consolidación
- Extiende F3. `/0188` sobrevive como una de las 3 separadas (38:75); retener el fragmento encapsulado es consistente con esa supervivencia. **Veredicto: APARENTE. Gravedad BAJA.** Se cubre con la solución de F3.

### AF-4 · Break-glass / CE-K y propagación del testimonio — **coherente**
- El testimonio propaga por el enlace educativo→mezcla ya instalado (37:15), dentro de alcance autorizado; cortar suspendería ARGOS (22:35; 37:179-185). Bien sembrado. No es flexión.

### AF-5 · Secuencia horaria del clímax — **verificada**
- `12:38` (34:135) · `12:46:01` (35:155) · `12:46:50` (repetidor, `S35-cierre`) · `12:47` (34:135,207) · `13:07` (37:203; `S37-1307`) · `13:11` (38:205; `S38-quinta`): presentes y en orden, dentro de la ventana de marea 12:38–12:56 (31:99). Coherente.

---

## 3. Verificación factual de §21

| Punto §21 | Comprobación en el texto | Veredicto |
|---|---|---|
| 1.185 vs «más de tres mil» | `597+2.311+3+1.185=4.096` cierra; 1.185 = pérdida vs cohorte, no borrado de la consolidación | **Coherente**; fijar canon (F12) antes de W2 |
| Tasa AÑOS-JM 16.000× | Constante en 979,7 → 2.401,6 → 2.401,6 → 2.427,4 con las fechas (AF-2) | **Coherente** |
| 12:47 en 31 sin fuente interior | 31:87 (Jean) vs 25:203 (solo `12:00` interior); 12:47 conocido fuera (34:135,207) | **Real menor** (F4) → C |
| Emisor del audio de 28 | 28:197 «El campo de origen seguía vacío»; 31:73 Jean «No que fuera esa noche» ⇒ el emisor no es `/0000` | **Coherente** (ledger B4 debe registrarlo) |
| Cronología `CARIES` 10/15/23 | 5-dic (10:17) anterior a `/0000` (15:39); La Jardinera «Una vez» (23:101); autoría plural | **Coherente**, ambigüedad protegida |

### Calendario · días de la semana (desde `fecha` del frontmatter)

Cómputo (calendario gregoriano): 24-nov-2060 = **miércoles** ✔ (26-nov = viernes ✔, coincide con «Aquel viernes» de cap-2; 27-nov = sábado ✔; 12-dic = domingo ✔, cap-25:85 «domingo 12 de diciembre»; 21-ene-2061 = viernes ✔). Los anclajes de B3 §21.10 son correctos.

| Ítem señalado | `fecha` | Día | Qué narra el texto | Veredicto |
|---|---|---|---|---|
| Vista tingrett (cap-29) | 2061-01-09 | **domingo** | Cautelar **urgente**: «A las doce y nueve, el Nord-Troms og Senja tingrett fijó la vista para las catorce» (29:51); resolución 40 min después | **Admisible con reserva.** `midlertidig forføyning` puede tramitarse en urgencia fuera de día hábil (tvl. §32-7). Fricción: el daño estaba a **once días** (29:89 «once días de distancia»), lo que debilita la urgencia de una sesión dominical |
| Inspección NIDHOGG (cap-19) | 2060-12-19 | **domingo** | «inspección de capacidad y cumplimiento» **corporativa** de Mats+Alana; «¿Por qué hoy?» es beat de trama; «En Sørkoppen no sirven hasta las dos» (19:21) | **Admisible.** Visita interna de directivos en domingo es plausible y refuerza el tono discreto/clandestino. Sin cambio |
| Kronfjord (cap-39:19) | evento 23-ene | **domingo** | «Al día siguiente [del 22-ene sábado], Kronfjord congeló las líneas» (39:19), acción financiera de crisis narrada en sumario | **Admisible.** Maniobra de acreedor en fin de semana de emergencia (ARGOS suspendido) es verosímil. Sin cambio |

**Recomendación de calendario:** ninguno exige cambio de `fecha`. El único con fricción real es **cap-29 (domingo, daño a 11 días)**:
- **Decisión C (recomendada):** dejar como está con justificación diegética (juez de guardia / urgencia por riesgo de destrucción de prueba). Cambiar la `fecha` **rompería** «once días de distancia» (29:89) y la cuenta atrás hacia el 20-ene, y desplazaría el encaje con cap-28 (7-ene) y cap-30 (12-ene).
- **A opcional (belt-and-suspenders):** media línea en 29 marcando la sesión como convocatoria de guardia por urgencia. Coste ≈ +12 pal. cap-29 es E (+200); no toca los spans `S29-orden/S29-cierre/S29-2054/S29-durante`. **No hacer:** no cambiar la fecha ni el «once días».

---

## 4. Tabla resumen (ordenada por gravedad)

| id | Flexión | Veredicto | Gravedad | Decisión | Dónde | Coste | Riesgo protección |
|---|---|---|---|---|---|---|---|
| F3 | Encapsular/transferir credencial → control del Auditorio | REAL | **MEDIA-ALTA** | **A** (o B) | 17:~89 (o 36) | +30 | Bajo (17:89 editable) |
| F1 | Alcance de `/0000` sobre otras | APARENTE | MEDIA | **A** | N5/8 | +25 | Evita 38 (P/núcleo) |
| F2 | Capacidad entre orígenes | REAL | MEDIA | **A** | N5 (o 13 RW) | +30 | Ninguno (N5 nuevo) |
| F12 | 1.185 vs «más de tres mil» | APARENTE | MEDIA | **C + canon** | B1/B3 | 0 | Evita 29 (`S29-orden`) |
| F14 | Coro «mantiene el identificador de Madre» | REAL-menor | MEDIA | **A** | 13:257 | +3 | Bajo (línea editable) |
| F15 | La llave «encaja» en armario HVAC | APARENTE | MEDIA→BAJA | **C** (A opc.) | 24 | +15 | Bajo |
| AF-1 | Cobertura Tomas «HASTA 12:47» | APARENTE | BAJA-MEDIA | **C** | — | 0 | — |
| Cal-29 | Vista tingrett en domingo (11 días de margen) | Admisible c/reserva | MEDIA→BAJA | **C** (A opc.) | 29 | 0 (+12 opc.) | Bajo |
| F4 | 12:47 sin fuente interior | REAL-menor | BAJA | **C** | — | 0 | Evita `S25-fecha` |
| F5 | Cronología `CARIES` | APARENTE | BAJA | **C** | — | 0 | 23 total / `S10` |
| F6 | La asamblea como espacio | APARENTE | BAJA | **C** | — | 0 | — |
| F7 | `/0000` sabe que fue Nora | APARENTE | BAJA | **C** | — | 0 | 20 total (no toca) |
| F8 | Retirar salidas | YA COHERENTE | BAJA | **C** | — | 0 | — |
| F9 | Latencias 9 s / 6 s | REAL intencional | BAJA | **C** (no resolver) | — | 0 | — |
| F10 | Ventana reflexiva | YA COHERENTE | BAJA | **C** (A0/R2) | — | 0 | `S19-reflexiva` |
| F11 | Estados de Madre cruzan el corte | APARENTE | BAJA | **C** | — | 0 | — |
| F13 | Coro retira extremo / sesión 23 sin autor | APARENTE | BAJA | **C** (N4 paga CH-1) | — | 0 | 23 total |
| F16 | Alana renueva sesión bajo colegiado | YA COHERENTE | BAJA | **C** | — | 0 | 20 total |
| Cal-19 | Inspección NIDHOGG en domingo | Admisible | BAJA | **C** | — | 0 | — |
| Cal-39 | Kronfjord en domingo (23-ene) | Admisible | BAJA | **C** | — | 0 | — |

**Coste total de las intervenciones recomendadas (todas A):** ≈ +103 palabras, ninguna sobre span hash-protegido ni fichero `total`.

**Ninguna flexión es BLOQUEANTE.** No hay contradicción que se lea como trampa insalvable; las de gravedad MEDIA son sembrables con anclajes baratos o se resuelven canonizando cifras (F12). Las ambigüedades protegidas (porqué, ordenante, identidad ontológica, `CARIES`, latencia) **no se resuelven**: F5, F9 y F13 se marcan C por diseño.
