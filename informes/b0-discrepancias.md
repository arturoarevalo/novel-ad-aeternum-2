# B0 · Auditoría del manifiesto (`biblia/metadatos.json`) — informe de discrepancias

**Fase 0 · A1 (ejecutado por A0 con herramientas) · rama `w1-biblia-diagnostico` · baseline `v0` = commit 61e446f.**

## 1. Resumen

- El manifiesto es **coherente con el repositorio y con la prosa**: 41 entradas ↔ 41 ficheros; `archivo`/`slug`/`titulo`/`n` coinciden con el frontmatter; los rangos de `partes[]` cubren 1–41 sin huecos; las cuatro cabeceras de cuenta atrás cuadran (24-nov+58, 6-dic+46, 25-dic+27, 15-ene+6 = 21-ene-2061) y coinciden con la `fecha` del primer capítulo de cada parte; `persona: primera` de cap-38 se cumple en la prosa (31,4 ‰ de marcadores de 1.ª persona en narración frente a un máximo de 8,0 ‰ en el resto; umbral del validador: 20 ‰); la secuencia de `fecha` es monótona salvo los tres capítulos con `analepsis: true` (6, 9, 11).
- **Recuento real canónico de v0: 62.750 palabras** (método: cuerpo sin frontmatter, sin marcado markdown ni dinkus, tokens con al menos un carácter alfanumérico). `wc -w` da 63.201; el plan citaba «~63.400». La diferencia es de método (rayas sueltas, dinkus), no de texto. Toda medición del proyecto usa el recuento canónico (`herramientas/lib/aa.py::count_words`).
- Las cuotas `palabras` de v0 (que sumaban exactamente 65.000) estaban un **3,5 % por encima del texto real**; la desviación no es uniforme: la Parte IV es la más podada respecto a su cuota (cap-41 −29,6 %, cap-39 −20,6 %, cap-40 −17,9 %, cap-38 −12,5 %, cap-37 −10,2 %), junto con cap-10 (−10,3 %). Dato útil para B8 si aparecen los borradores de 85k: es donde más tejido se quitó al final.

## 2. Operaciones ejecutadas sobre el manifiesto (vía `herramientas/actualizar-metadatos.sh`, con historia git)

1. `palabras_real` añadido a los 41 capítulos (recuento canónico).
2. `palabras_objetivo`: 65.000 → **85.000** (decisión de autor ya tomada; registrada en `informes/registro-gates-autor.md`). Banda M8 = 84.000–86.000, leída del manifiesto.
3. `palabras` reescrito como **presupuesto vF = palabras_real(v0) + delta_objetivo** (tabla 5.1, leído del frontmatter). Suma actual: **68.150** (62.750 + 5.400 de los 41 capítulos existentes). Los seis capítulos nuevos (+12.500) se registrarán al superar G-A2 → 80.650; la reserva priorizada (§5.3, hasta +4.300) la asigna A0 elevando `delta_objetivo` y re-ejecutando `presupuestos --v0`.
4. Nueva clave operativa `paratextos[]` con `00-aviso.md` y `99-recursos.md` (ver §4).
5. Campos de AUTOR intactos (verificación automática contra el tag `v0` en cada ejecución y en el pre-commit).

## 3. Discrepancias PLAN ↔ TEXTO detectadas (gana el texto)

| # | Dónde | Plan dice | Texto | Decisión |
|---|---|---|---|---|
| D1 | Tabla 5.1, cap-16 «La firma» | criterio: «Lo que firmó tu exmujer no lo firmó aquí» cierra igual | La línea cierra **cap-14 «La visita»** (l. 352); cap-16 cierra con «—Propiedad intelectual. Así la llaman.» | Span protegido `S14-firmo` en cap-14. Para cap-16 el criterio pasa a ser «cierre “Propiedad intelectual. Así la llaman.” intacto» (a confirmar por A2 en la OT-16). |
| D2 | Tabla 5.1, cap-17 «Cuchillo» | criterio: «¿Y yo qué soy?»–`NO AMENAZA/REVISAR` intacto | El intercambio está en **cap-13 «Miles»** (l. 190–194); cap-17 contiene `AMENAZA CONTENIDA · REVISAR` | Span `S13-yo-que-soy` en cap-13; OT-17 hereda solo «test lector frío» y `AMENAZA CONTENIDA · REVISAR` como referencia. |
| D3 | §0 y §5.2 | v0 ≈ 63.400 palabras; subtotal Δ = +18.250 | Recuento canónico 62.750; la suma de la columna Δ de la tabla 5.1 es **+17.900** (5.400 existentes + 12.500 nuevos) | El ledger de A0 usa la tabla 5.1 (por capítulo). Proyección: 62.750 + 17.900 = 80.650 → hace falta reserva de +3.350 a +5.350 para la banda; el backlog §5.3 ofrece hasta +4.300 (→ 84.950). Suficiente pero **sin holgura**: se anota como riesgo. |
| D4 | §2.4 / Ap. A | `00-aviso.md` y `99-recursos.md` «se extraen de la versión maestra» | **No existe versión maestra en el repositorio** (ni en la historia git: el commit inicial era una plantilla) | Creados **borradores provisionales** (`provisional: true`, sin hash M9 hasta validación de autor). **Decisión de autor pendiente en G0**: aportar los textos reales o validar/editar los borradores. |
| D5 | Ap. A, cap-19 / cap-26 | «la palma en el cristal tibio»; «la lata de galletas» | Frases exactas: «Alana apoyó la palma en el cristal. Tibio.» (cap-19 l. 192); «sacó una lata redonda de galletas danesas» (cap-26 l. 78) | Spans `S19-palma` y `S26-lata` definidos sobre el texto real. |
| D6 | Ap. A, cap-37 | núcleo «desde “NO SOY UN MODELO.” hasta “…un fallo de escenario”» | `NO SOY UN MODELO.` aparece dos veces (l. 92, POV Jean; l. 146, POV Astrid); el acta cierra en l. 186 | Dos spans: `S37-declaracion` (POV Jean, l. 88–100) y `S37-acta` (POV Astrid, l. 144–186), más `S37-muchas`. |
| D7 | Repositorio | `.gitignore` ignoraba `informes/` (herencia del andamiaje anterior) | El plan versiona `informes/` (§2.2) | Línea retirada del `.gitignore`. |

## 4. Elementos creados en F0 que requieren decisión de autor

- **`capitulos/00-aviso.md` y `capitulos/99-recursos.md` (provisionales).** El compilado que leerán A6/A6b los incluye (Ap. A los declara elementos estructurales). Hasta que el autor los valide, no llevan hash: cualquier edición suya es libre; tras la validación, `proteger.sh baseline` los congela.
- Ninguna otra: no se ha tocado una sola frase de los 41 capítulos (verificado: cuerpo byte a byte idéntico a `v0` en 41/41; solo se añadieron cinco campos de frontmatter del plan).

## 5. Protección M9 activada

- `protegidos/spans.json`: 8 ficheros `total` (+2 paratextos provisionales) y **34 spans** de núcleo/líneas (Apéndice A + criterios «intacto» de la tabla 5.1), todos localizados en el texto. `protegidos/hashes.json` = baseline. Hook `pre-commit` (git, `core.hooksPath=herramientas/hooks`) y hook `PreToolUse` (`.claude/settings.json`) operativos; probados con casos positivos y negativos.
- Los capítulos con algún span protegido llevan `proteccion: nucleo` (22 capítulos); los ocho íntegros, `proteccion: total`; el resto, `no`.

## 6. Resultado automático de la auditoría (`herramientas/auditar-manifiesto.sh`, sobre v0)

## Comprobaciones superadas

- 41 entradas registradas; 41 ficheros en capitulos/
- Parte 1 «Mørketid»: 2060-11-24 + 58 días = Soldagen ✓
- Parte 1: fecha de cabecera = fecha del cap. 1 ✓
- Parte 2 «Fije la vista»: 2060-12-06 + 46 días = Soldagen ✓
- Parte 2: fecha de cabecera = fecha del cap. 11 ✓
- Parte 3 «Propiedad intelectual»: 2060-12-25 + 27 días = Soldagen ✓
- Parte 3: fecha de cabecera = fecha del cap. 21 ✓
- Parte 4 «Soldagen»: 2061-01-15 + 6 días = Soldagen ✓
- Parte 4: fecha de cabecera = fecha del cap. 31 ✓
- Rangos de partes cubren exactamente 1..41 sin huecos ni solapes ✓
- `cap-38.md` persona=primera: densidad de 1.ª persona en narración 31.4‰ (umbral 20‰; máx. del resto en v0 = 8,0‰) ✓
- Secuencia de fechas del frontmatter monótona salvo capítulos con analepsis: true ✓

## Discrepancias detectadas

- (ninguna)

## Deriva palabras: cuota (v0) vs recuento real

| n | archivo | título | cuota v0 | real | Δ | Δ% |
|---|---|---|---:|---:|---:|---:|
| 1 | cap-01.md | Corona | 750 | 746 | -4 | -0.5% |
| 2 | cap-02.md | La pecera | 1550 | 1668 | +118 | +7.6% |
| 3 | cap-03.md | Vacaciones muy largas | 2050 | 2102 | +52 | +2.5% |
| 4 | cap-04.md | El ferry | 1510 | 1501 | -9 | -0.6% |
| 5 | cap-05.md | Flor | 1760 | 1782 | +22 | +1.2% |
| 6 | cap-06.md | La casa sin ella | 2040 | 2021 | -19 | -0.9% |
| 7 | cap-07.md | Lote rojo | 1620 | 1610 | -10 | -0.6% |
| 8 | cap-08.md | Milisegundos | 1020 | 967 | -53 | -5.2% |
| 9 | cap-09.md | Despedida | 1910 | 1861 | -49 | -2.6% |
| 10 | cap-10.md | Caries | 1495 | 1341 | -154 | -10.3% |
| 11 | cap-11.md | Preservación funcional | 1900 | 1818 | -82 | -4.3% |
| 12 | cap-12.md | Gunnar | 1950 | 1896 | -54 | -2.8% |
| 13 | cap-13.md | Miles | 1250 | 1206 | -44 | -3.5% |
| 14 | cap-14.md | La visita | 1740 | 1703 | -37 | -2.1% |
| 15 | cap-15.md | Canela | 1160 | 1135 | -25 | -2.2% |
| 16 | cap-16.md | La firma | 1870 | 1758 | -112 | -6.0% |
| 17 | cap-17.md | Cuchillo | 880 | 800 | -80 | -9.1% |
| 18 | cap-18.md | No determinista | 2060 | 2030 | -30 | -1.5% |
| 19 | cap-19.md | NIDHOGG | 1940 | 2016 | +76 | +3.9% |
| 20 | cap-20.md | La cuarta nota | 1510 | 1493 | -17 | -1.1% |
| 21 | cap-21.md | Coro | 720 | 657 | -63 | -8.8% |
| 22 | cap-22.md | Auditoría | 1520 | 1449 | -71 | -4.7% |
| 23 | cap-23.md | La canción | 1770 | 1847 | +77 | +4.4% |
| 24 | cap-24.md | Accidente | 1760 | 1665 | -95 | -5.4% |
| 25 | cap-25.md | EDDA | 900 | 890 | -10 | -1.1% |
| 26 | cap-26.md | Casa prestada | 1535 | 1704 | +169 | +11.0% |
| 27 | cap-27.md | Apartada | 1800 | 1786 | -14 | -0.8% |
| 28 | cap-28.md | El mismo trayecto | 1390 | 1463 | +73 | +5.3% |
| 29 | cap-29.md | La poda | 1280 | 1268 | -12 | -0.9% |
| 30 | cap-30.md | La asamblea | 1300 | 1360 | +60 | +4.6% |
| 31 | cap-31.md | El ladrillo | 1400 | 1458 | +58 | +4.1% |
| 32 | cap-32.md | La oferta | 1515 | 1585 | +70 | +4.6% |
| 33 | cap-33.md | Bajamar | 1640 | 1530 | -110 | -6.7% |
| 34 | cap-34.md | Soldagen | 2400 | 2323 | -77 | -3.2% |
| 35 | cap-35.md | Caída | 2000 | 1820 | -180 | -9.0% |
| 36 | cap-36.md | Cuchillo abre los ojos | 1145 | 1038 | -107 | -9.3% |
| 37 | cap-37.md | No soy un modelo | 2400 | 2156 | -244 | -10.2% |
| 38 | cap-38.md | Norna | 1510 | 1321 | -189 | -12.5% |
| 39 | cap-39.md | Depósito | 1950 | 1548 | -402 | -20.6% |
| 40 | cap-40.md | Sombra | 2100 | 1724 | -376 | -17.9% |
| 41 | cap-41.md | El siguiente Soldagen | 1000 | 704 | -296 | -29.6% |
| | **Total** | | **65000** | **62750** | **-2250** | **-3.5%** |

palabras_objetivo declarado: 65000 · suma de cuotas: 65000 · recuento real canónico: 62750
