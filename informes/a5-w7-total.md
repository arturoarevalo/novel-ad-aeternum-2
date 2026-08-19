# A5 · W7 · Verificación de continuidad TOTAL del manuscrito

**A5 · rama `w7-verificacion`.** Insumo: `compilado/ad-aeternum-w7.md` (48 cap., cabeceras `## 1…48`) + `capitulos/` + manifiesto. Cruce contra `biblia/b1-cronologia.md`, `b3-canon-sistema.md`, `b4-ledger-chekhov.md`, frontmatter y `informes/a7-w5c-espejo.md`. No se ha tocado ningún capítulo ni la Biblia.

## Mapa fichero → número W7 (para leer las citas de la Biblia, que van por FICHERO)

Los cinco números vivos: la Biblia cita por **nombre de fichero** (estable), no por el número W7. Equivalencia de los siete que más se movieron y de todo lo desplazado ≥8:

`cap-n5`=8 · `cap-08`=9 · `cap-09`=10 · `cap-n1`=11 · `cap-10`=12 · `cap-11`=13 · `cap-12`=14 · `cap-13`=15 · `cap-14`=16 · `cap-n7`=17 · `cap-15`=18 · `cap-16`=19 · `cap-n2`=20 · `cap-17`=21 · `cap-18`=22 · `cap-19`=23 · `cap-20`=24 · `cap-21`=25 · `cap-22`=26 · `cap-n3`=27 · `cap-23`=28 · `cap-24`=29 · `cap-25`=30 · `cap-n4`=31 · `cap-26`=32 · `cap-27`=33 · `cap-28`=34 · `cap-29`=35 · `cap-30`=36 · `cap-31`=37 · `cap-32`=38 · `cap-33`=39 · `cap-34`=40 · `cap-35`=41 · `cap-36`=42 · `cap-37`=43 · `cap-38`=44 · `cap-39`=45 · `cap-40`=46 · `cap-n6`=47 · `cap-41`=48. (1–7 sin cambio.)

## 1 · Lo mecánico de la renumeración — LIMPIO

- 48 ficheros con `capitulo` único 1–48 y `orden_lectura == capitulo` (0 desincronizados; verificado).
- Manifiesto: `partes[]` 1-12 / 13-24 / 25-36 / 37-48; subtítulos 58/46/27/6 días con fechas 24-nov / 6-dic / 25-dic / 15-ene, que **coinciden con la `fecha` del primer capítulo de cada parte** (ch1, ch13=`cap-11`, ch25=`cap-21`, ch37=`cap-31`). Cuenta atrás recomprobada contra 21-ene-2061.
- Las cuatro costuras de parte caen en los **mismos cortes de prosa que v0** (Caries|Preservación funcional; La asamblea|El ladrillo, etc.): los `orden_lectura` decimales no cruzaron ninguna frontera.
- **Ninguna referencia a un número de capítulo en la prosa** (grep exhaustivo; único hit es falso positivo). El número solo es DATO en (a) la cuenta atrás de las partes —derivada de fechas, correcta— y (b) la aritmética de cohorte —correcta—. En ningún sitio el número es puntero baked-in a la numeración vieja.
- `cap-n4` frontmatter `pov` ya corregido a `Nora → Maja → Jessie → Maja` (sin Jean; H-1 de A7 aplicada).
- Fechas de frontmatter intactas tras renumerar (spot-check `cap-11`=6-dic, `cap-17`=16-dic, `cap-n7`=2059-03-04).

## 2 · La lectura entera

### Aritmética — TODA correcta (compilado)
- `4.096` identificadores de cohorte (l.3484); consolidación `COHORTE 4.096 / RUTAS OPERATIVAS 2.911 / 4.096 − 2.911 = 1.185` (l.9753-9759); `2.401,6 AÑOS-JM` (l.9767); reparto `2.311 + 597 + 3 = 2.911` explícito (l.10735); `979,7` (l.5668) → `2.401,6` → `2.427,4 AÑOS-JM · ≈55,4 días × 16.000×` (l.10721-10723). `INC-441` y `cobertura hasta 12:47` (l.9931-9935). Reloj oculto AÑOS-JM coherente.

### Las 17 horas del clímax — presentes y monótonas
08:51 · 09:42 (tres relojes) · 12:00 (`DESPLIEGUE`) · 12:23 (`INC-441` abre) · 12:26 · 12:30 (cierre por sectores) · 12:37:59 · 12:38 (ventana / red largada) · 12:41/12:42/12:43 (AK-7) · **12:46:01** (petición local) · 12:46 (alarma) · **12:46:50** (enlace, «sincronización en diez segundos») · **12:47** (fase común) · **13:07** (custodia) · **13:11** (escritura profunda). Leída la secuencia INC-441 completa: la lógica «cobertura hasta 12:47» / carné `SEGURIDAD · PRESENCIA LOCAL` / enlace 12:46 es coherente. El trenzado 12:46:01↔12:46:50 entre POV (ch41 Caída vs ch40 Soldagen) es el mismo segundo visto dos veces, no un desfase.

### Fechas, estaciones y analepsis en el orden nuevo — coherentes
Secuencia de lectura monótona salvo las analepsis marcadas. **Cuatro** capítulos con `analepsis: true`: ch6 (`cap-06`, 26-nov→27), ch10 (`cap-09` Despedida, 3-dic), ch13 (`cap-11`, 6-dic) y ch17 (`cap-n7` El salero, **2059-03-04**). Las tres que **retroceden de verdad** son 6, 10 y 17 (las que el autor nombra); ch13 es la «analepsis intercalada» documentada (contiene flashback, no rompe secuencia: 6-dic > 5-dic; B1 §5 / D4). No es omisión: el conteo es correcto y está justificado.

### Chéjov — todo pagado, ninguna cadena con pago antes de siembra
- **CH-8 (metrónomo):** siembra dramatizada `cap-n7`=**ch17** («está bien medido y miente»); eco `cap-20:115`=**ch24**; hueco del cumpleaños `cap-23`=**ch28**; la «esquina hundida» de ch28 la explica `cap-n7:101` (ch17). Orden 17<24<28 ✓. La escisión W5 movió la cena de ch27 a ch17, es decir **más temprano**: refuerza el orden, no lo rompe.
- **CH-27 (cuenta escolar):** siembra `cap-10`=ch12 (5-dic); restitución en página al abrir `cap-n4`=ch31 («admitió las credenciales al primer intento») y re-suspensión el mismo 3-ene a las 11:52 con las palabras literales del 5-dic («Eran las mismas del cinco de diciembre y en el mismo orden»). ✓
- **CH-53 (naust Koppangen):** siembra `cap-04`=ch4; cadena hasta ch48 intacta.
- **CH-9 (repesca):** siembra `cap-03`=ch3; cierre ch46/ch48.
- **Los siete que quedaban PENDIENTE-ASIGNAR tras W3 están PAGADOS en el texto** (verificado): CH-2 «No preguntó por el cinturón» `cap-40:127`=ch46 (fuera de S40-locutorio) · CH-4 la caída en la barca `cap-35:273`=ch41 · CH-5 Astrid 2054 `cap-22:173`=ch26 · CH-6 carnés caducados `cap-24:129`=ch29 · CH-3 71-K textura `cap-15:143-145`=ch18 · CH-31 `VENTANA REFLEXIVA · ABIERTA/CERRADA` `cap-25:225/315`=ch30 (siembra ch23 < pago ch30) · CH-75 Inger `cap-16:65`=ch19.

### Las dos escisiones/excisiones no dejaron nada colgando
- **Espejo de Jean excindido de N4 (−483):** A7 verificó (`a7-w5c-espejo.md`) y confirmo: el espejo era el **eco**, no la siembra (`cap-21:95`=ch25 es la siembra de v0, va delante). **CH-1 sigue pagado** en `cap-32:93`=**ch38** («El resumen no tenía autor.»), con el acto aún en página en los tres acosos de N4. La mecánica MEC-25 (aviso de exposición) sobrevive en `cap-n4:89`. Nada huérfano.
- **«Vía A / figura repetida» (−225):** compresión de prosa, sin siembra; A5-W5 ya pasó.

## Hallazgos

| Sev. | Ubicación | Cita/objeto | Regla/fuente | Corrección mínima |
|---|---|---|---|---|
| **mayor** | `b1:100`, `b4:37`, `b4:155`, `b3:137`, `b3:339`, `b3:378` | «N4-I5 muestra por primera vez el acto negable»; «tres rasgos de Coro… **canon para todo el libro**»; «**primer acto negable de Coro en página**»; POV «…Jessie→**Jean**→Maja» | `a7-w5c-espejo.md` **H-3** (ordenó reanclar/borrar tras la excisión del espejo) — no aplicada | **Solo Biblia, el texto es coherente.** Reanclar CH-1 a `cap-32:93` (b4); **borrar** de B3 §8 los tres rasgos de Coro y de MEC-25 la referencia «N4-I5» (dejar «aviso»); corregir POV en b1:100. Es un **vector de reinserción** vivo (A7 P-64): la Biblia sigue instruyendo a «restaurar» una escena excindida |
| **menor** | `b4` §2 (tabla) y §3.1 | CH-2/3/4/5/6/31/75 marcados `PENDIENTE-ASIGNAR` | El texto los paga (locus arriba); ledger no actualizado tras W4/W5/W6 | Pasar los 7 a PAGADO; M10 real ≈100 % |
| **menor** (heredado) | ch35 (dom 9-ene, vista 14:00) · ch23 (dom 19-dic, inspección) · ch45 (dom 23-ene, Kronfjord) · ch6 (sáb 27-nov, «mañana no voy al instituto») | Actos administrativos/judiciales en domingo/sábado | B1 D3 (verosimilitud de calendario) | No es contradicción interna; sigue diferida a decisión de autor. No introducida por W7 |
| **informativo** | Biblia entera | citas `cap-NN.md:L` | Renumeración | Las citas van por **fichero** (estable): siguen válidas. Añadir el mapa fichero→W7 (arriba) a la cabecera de B1/B4 evitaría lecturas erróneas |

## ¿Hilo que se planta y no se recoge, o que se recoge sin plantar?
**No se ha encontrado ninguno en el texto.** Todas las cadenas cierran en el orden nuevo; las dos excisiones y la escisión no dejaron pago sin siembra ni siembra huérfana. El único desajuste real es **documental** (la Biblia describe una escena —el espejo/ N4-I5— y un canon —los tres rasgos de Coro— que ya no existen en el manuscrito), no narrativo.

## Veredicto: **PASA CON MENORES**
El compilado `ad-aeternum-w7.md` es sólido en cronología, aritmética, las 17 horas, estaciones y todas las cadenas Chéjov bajo la numeración nueva. El único hallazgo por encima de «menor» es deriva de la **Biblia** (Finding mayor): no toca la prosa, pero A0 debería aplicar las correcciones H-3 de A7 antes de cerrar W7 para neutralizar el vector de reinserción del espejo.
