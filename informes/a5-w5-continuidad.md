# A5 · Verificación de continuidad — W5 (rama `w5-trama`)

**Insumo:** `git diff main..w5-trama -- capitulos/` (7 capítulos), `informes/w5-plan.md` v2, `## 9 · W5` de las OT, `biblia/b1-cronologia.md`, `b3-canon-sistema.md`, `b4-ledger-chekhov.md`, `capitulos/cap-n4.md`, `cap-16.md`, `cap-22.md`, `protegidos/spans.json`. Instrumentos: `medir.sh w5-check` → **M7 errores 0 · M8 80288 EN BANDA · M9 OK · M10 91,6**.

**Δ medido (contador oficial, cuerpo):** 24 +189 · 26 +68 · 31 +155 · 32 +168 · 34 +95 · 35 +22 · 40 +5 = **+702** (coincide con el mandato; el plan proyectaba +768, la ejecución quedó por debajo del techo en tres capítulos — sin efecto de continuidad).

## Tabla de hallazgos

| # | sev. | cap:línea | cita | fuente contradicha | corrección mínima |
|---|---|---|---|---|---|
| 1 | **mayor** | cap-26:17 | «el encargo del domingo **autorizado ese mismo día**» | `cap-n4:239-247`: el seguimiento del **2-ene (domingo)** «constaba autorizado» con «fecha del **tres de enero, a las nueve y doce**» → «**Lo autorizan hoy. Nos siguieron ayer.**». La autorización es del **lunes**, no del domingo. Además choca con `cap-32:93` (misma oleada), que sí lo fija bien: «un expediente policial cerrado con **una autorización posterior**». La lectura natural de «ese mismo día» (= domingo) destruye el beat de autorización retroactiva que sostiene CH-45. | «…y el encargo del domingo **autorizado el mismo lunes**» (o «…autorizado al día siguiente»). +1 palabra. |
| 2 | **mayor** | cap-35:161 | «Jessie recordó **sus preguntas en la comisaría** y las dos horas bajo luces blancas. **También había preservado el coche de Gunnar** cuando Armstrong habría preferido una avería.» | (a) Tomas **no** interrogó a Jessie en la comisaría: su encuentro fue en **Fyret** (`cap-16:175-239`) y estuvo **ausente** de la comisaría del `cap-24` (allí solo hay «la agente/la funcionaria», policía). (b) Jessie **no puede saber** en `:161` que Tomas preservó el coche de Gunnar: la consola lo revela solo en `:191-193` (`HOJA 1 · VEHÍCULO G. RYDBERG`) y Tomas investigó en privado (`24:123`, `34:271` «sin informar a nadie fuera de su cadena»). Violación de conocimiento en POV Jessie. | **Es OT-35 I-4** (ver dictamen abajo). `:161` NO está en span protegido (`S35-acepta` = `:211-213`). Coste cero. |
| 3 | menor | cap-32:93 | «cuatro documentos incorporados por la autoridad de supervisión» | — (verificación, no contradicción) | Ninguna: coincide **literal** con `cap-n4:421` «Cuatro documentos del 3 de enero. Los incorporo como están». ✅ |

## Dictamen de OT-35 I-4 (decisión de A5) — **PROCEDE**

El texto de `cap-35:161` es de v0 (el diff de W5 solo tocó `:273`), y arrastra los dos defectos que la propia `OT-35` I-4 diagnostica: Tomas mal ubicado (Fyret ≠ comisaría) y conocimiento imposible de Jessie (el coche de Gunnar antes de que la consola lo muestre). No es estilo: es continuidad. Se ejecuta a coste cero (banda 0 ± 15), sin heredar interior de Tomas (restricción de I-1), fuera de span protegido.

**Contenido exacto propuesto** (sustituye las dos oraciones señaladas):

> «Jessie lo reconoció de Fyret, del día que le retuvieron el terminal. Después de aquello habían venido el coche gris y las dos horas bajo luces blancas.»

Efecto: conserva la anagnórisis («—Tú—»), corrige la ubicación (reconocimiento por **Fyret**, `cap-16`), mantiene «las dos horas bajo luces blancas» como memoria **propia** de la comisaría (`cap-24`, sin atribuírsela a Tomas) y **elimina** el dato del coche de Gunnar que Jessie no puede tener aún. Neto ≈ −13 palabras (dentro de banda). Lo ejecuta A3b/A4; A5 no toca capítulos.

## Estados de frontmatter (segunda tarea)

`§8.1 · 0.1` del plan exigía `estado=en_oleada` en los **siete**. Solo se aplicó a `cap-34` y `cap-40`. **Siguen en `terminado` pese a haber sido modificados en W5 y con la oleada sin gate:** `cap-24`, `cap-26`, `cap-31`, `cap-32`, `cap-35`. Deben pasar a `en_oleada` (`inyectar-frontmatter.sh --set …`). A5 no los toca.

## Verificaciones duras — resultado

- **cap-34 (reloj + aritmética):** 17 marcas horarias presentes y en orden dentro de cada escena (los retrocesos entre escenas son de diseño, B1 fila 34 ✓): 08:51 · 09:00 · 09:42 · 10:27 · 11:40 · 11:44 · 12:00 · 12:04 · 11:58 · 12:23 · 12:26 · 12:30 · 12:37:59 · 12:38 · 12:46 · 12:46:50, más `12:47` (fase común) y la referencia a `22:59/23:00`. `4.096 − 2.911 = 1.185` (`:89`), `2.401,6 AÑOS-JM` (`:97`), `2911`/`1185` en letra (`:199-205`), `INC-441`, cobertura «HASTA 12:47» (`:265`). El +95 (`:269`) **no** añade ninguna hora nueva (solo cita `12:47` y «la exportación preservada en enero», coherente con `cap-24`) y **no** roza `4.096 − 2.911 = 1.185`. Prohibición «la consolidación borró 1.185» respetada. **PASA.**
- **cap-35 (marea + maniobra):** ventana `12:38–12:56`; largan a `12:38` (`:65`), muestras AK-7 `12:41/12:42/12:43`, `12:46:01` petición, `12:46:50` separación. Coherente con `cap-31:99` y `cap-34:133`; mareas vivas/bajamar viva (B1 §4). La caída (`:273`, CH-4) va **unida al párrafo** de Maja (no en párrafo propio), sin adverbio de manera, sin «aikido», «No se hizo daño», por tirón de la madre; **no** altera la cadena de tiempos con 34 ni con 37; el tampón «La consola exterior cambió de estado una vez más.» y `S35-cierre` intactos. **PASA.** (Salvo hallazgo 2, que es v0.)
- **cap-31 (ladrillo + tres umbrales):** `UMBRAL 1/2/3` presentes; la inserción entra **antes** de `UMBRAL 2` (`:131-157`) y añade una anotación al margen (`EL SEGUNDO LO ACEPTA UN DESCONOCIDO`), **sin** crear un cuarto umbral. No adelanta ni retrasa ningún eslabón: es la apuesta «qué se pierde si el desconocido no acepta», coherente con B3 §16/§17 (custodia «ante manifestación pública verificable») y con `cap-35`. P-48 respetada (ninguna voz enmarca el fin de Jean como alivio). **PASA.**
- **cap-24 (I-1 vs `22:173-175`):** el caso nuevo difiere en **dos de tres** elementos (qué preservó el profesional: registros de acceso ≠ dos resoluciones; qué objeto queda: carné caducado ≠ carpeta con el número en el lomo). La persona del caso anterior es **mujer** («una operaria… la vio… con el chaleco de otra empresa») y **no muere ni se pierde su rastro** («Seis meses después, Tomas la vio en la puerta de servicio»). Sin la cadencia vetada «no volvió a escribir/archivó el caso». Paga CH-6 tal como fija B4. **PASA.**
- **cap-26 (mudanza «por hechos» + derecho):** cronología correcta (`Salieron el lunes` = 3-ene lunes ✓; cuenta cerrada 11:52; medios del instituto retirados con AK-7 aún accesible, CH-28 ✓; revisión de la licencia de 2057 abierta sin anticipar el resultado, ≤15 palabras dentro de la réplica, coherente con la vía a N6). Repara la frase que N4 volvía falsa («bastaban» → «bastaban para llenarla»). **PASA salvo hallazgo 1.**
- **cap-40 (cinturón +5):** «No preguntó por el cinturón.» = 5 palabras, posición (b) — segunda oración del párrafo del jueves; diff = 1 línea modificada, 0 añadidas; CH-2 → PAGADO. **No** descoloca la elipsis de febrero (`P-47`, intacta) ni la secuencia de marzo. **PASA.** *Observación (no bloqueante):* el reorden coste-cero de **OT-40 I-4** (permutar el párrafo del sensor con el del pago para cerrar la escena en «Maja efectuó el pago allí mismo.») **no aparece en el diff**; sigue cerrando en el párrafo del sensor (`:163`). Es tarea de A4 (§8.3, paso 8), posiblemente pendiente; sin efecto de continuidad.

## Veredicto

**PASA CON MENORES.** Dos hallazgos *mayores* (ambos con corrección mínima y sin tocar spans protegidos ni ambigüedades del Ap. A §3): (1) `cap-26:17` «autorizado ese mismo día» contradice N4 → corregir a «el mismo lunes»; (2) `cap-35:161` = OT-35 I-4, **dictaminada PROCEDE** con texto exacto. Ninguno bloquea la fusión si A0 aplica las dos correcciones antes del gate. Cronología, aritmética del clímax, cadena de plantados y reglas del sistema: consistentes. M7 = 0.

*A5 · claude-opus-4-8 · 2026-08-18*
