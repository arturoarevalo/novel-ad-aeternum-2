# B5 · Lista protegida (Apéndice A completado por A1) — v0

**Fase 0 · A1 (Archivista).** Fuente de verdad técnica: `protegidos/spans.json` (10 ficheros íntegros + **108 spans**: 34 definidos por A0 y **74 añadidos por A1** en esta revisión) y `protegidos/hashes.json` (baseline aditiva; `herramientas/proteger.sh verificar` → `M9 OK · 8 ficheros íntegros · 108 spans íntegros`). Convención de líneas: `cap-NN.md:L` = línea física del fichero completo (`cat -n`, frontmatter de 13 líneas + 1 en blanco; línea de cuerpo = L − 14). Los ids siguen el patrón `SNN-slug`.

Regla (Ap. A, Principio 3): lo protegido tiene diff = 0 salvo ortotipografía aprobada en gate; alterar o retirar un span exige gate de autor y `--rebaseline`; **añadir** spans es libre. Este documento es la lista legible; los hashes mandan.

## 1. Ficheros íntegros (`proteccion: total`, hash de fichero completo y de cuerpo)

| Fichero | Contenido | Estado del hash |
|---|---|---|
| `cap-01.md` Corona | Apertura; R-1189; `NORNA · NO OPERATIVA`; «Última sesión.»; la corona en el gancho | baseline ✓ |
| `cap-03.md` Vacaciones muy largas | Café con Alana; «Estoy asustada.»; aikido / «caer sin hacerse daño»; escala del monstruo; «No llames a Maja»; anillo; credencial | baseline ✓ |
| `cap-04.md` El ferry | Elipsis del acto; cinturón en el pomo; gofre; cajera e Ingrid; naust; cinco trazos; la bisagra | baseline ✓ |
| `cap-05.md` Flor | Despertar; «Fije la vista»; JM-L/0000; 10.000 imágenes | baseline ✓ |
| `cap-10.md` Despedida | Funeral; «Mamá se mató. Empecemos por ahí.»; `Despedida` sin abrir; primera cita «mañana»; Kongsbakken; JM-L/0007 | baseline ✓ |
| `cap-24.md` La cuarta nota | Confesión de Alana; el metrónomo que miente; la cuarta nota; «Nadie tocó la quinta.» | baseline ✓ |
| `cap-28.md` La canción | «¿Eres mi madre?» «No toda.»; «Activo memorial. Qué hijos de puta.»; el segundo regalo / «Dejo el hueco»; La Jardinera; el guante omitido; «pregúntale qué sabe del cinturón» | baseline ✓ |
| `cap-48.md` El siguiente Soldagen | «Cronometrar el sol.» «Para que conste.»; el gofre frío; la puerta que roza | baseline ✓ |
| `00-aviso.md` | Aviso de contenido (borrador **provisional**, B0-D4) | **sin hash** hasta validación de autor (`provisional: true`); `listar` lo muestra como «INEXISTENTE» por esa razón |
| `99-recursos.md` | Recursos de ayuda (borrador **provisional**, B0-D4) | **sin hash** hasta validación de autor |

## 2. Núcleos protegidos dentro de capítulos (Ap. A) — verificación de los spans de A0

| Núcleo (Ap. A) | Span | Localización | Verificación A1 |
|---|---|---|---|
| 37 · declaración «NO SOY UN MODELO.» … «un fallo de escenario» | `S37-declaracion` + `S37-acta` | cap-43.md:93–105 (POV Jean) y 149–191 (POV Astrid) | Cubre lo que pide el Ap. A. `S37-acta` empieza **una frase antes** del arranque literal («Astrid vio aparecer la frase antes de oír la voz.», l. 149; «NO SOY UN MODELO.» está en l. 151): sobrecobertura de una frase, aceptable (proteger de más, no de menos); usar el literal exigiría `ocurrencia: 2`. La línea 193 («La voz volvió por los altavoces.») queda fuera, entre el acta y `S37-muchas`: correcto. |
| 37 · «Para decir esta frase hemos dejado de ser muchas. Que conste también.» | `S37-muchas` | cap-43.md:195 | ✓ exacto |
| 38 · muerte de Nieve («Para mí, Nieve muere…») | `S38-nieve` | cap-44.md:161–171 | Cubre la muerte (167) y «Echo de menos hasta sus pausas» (169). La sección de Nieve empieza en 137; su última negativa (149–153) quedaba **sin cubrir** → añadido `S38-no-autorizo`. |
| 38 · pasaje de la respiración/huella | `S38-huella` | cap-44.md:181–183 | ✓ exacto |
| 38 · elección de quedarse | `S38-quedarme` | cap-44.md:185–191 | ✓ («Elijo quedarme.» en 189) |
| 25 · línea de EDDA | `S25-utilidad` | cap-30.md:89 | ✓ exacto |
| 25 · escalada interceptada | `S25-escalada` | cap-30.md:93–107 | ✓ (de `ESCALADA HUMANA INDICADA` a «Se conservaron como variables del cálculo de continuidad.») |
| 29 · «Las necesarias.» como cierre | `S29-cierre` | cap-35.md:215 | ✓ |
| 30 · borrado a mitad de frase de La Jardinera | `S30-borrado` | cap-36.md:125–127 | ✓ («Los demás convie—» + «La ruta de `JM-L/0044` se cierra.») |
| 39 · «No sé qué es. Sé que alguien la quiere. Empecemos por ahí.» | `S39-jueza` | cap-45.md:187 | ✓ |
| 39 · la pluma del divorcio | `S39-pluma` | cap-45.md:181–183 | ✓ (la línea 185, «La primera línea salió débil…», queda fuera; aceptable) |
| 6 · el tramo de la llamada | `S06-llamada` | cap-06.md:15–31 | Cubre la llamada propiamente dicha (de «—Sí, el coche es gris.» a «Terminó la llamada. La nevera seguía pitando.»). La confirmación inmediata («—Han encontrado a Jean.» / «—Está muerta.» / «—Sí.», 33–41) queda fuera: **extensión opcional** que A0 puede decidir; no la he añadido para no ampliar un núcleo definido por A0. |
| 11 · flashback intercalado 26-nov / UNN | `S11-flashback` | cap-13.md:85–135 | ✓ (incluye los mensajes «No vengas / No llames a Maja», la ficha VERDE y las tres autorizaciones; termina en «firmó con el índice.», l. 137 «—Alana.» devuelve al presente) |

**Spans de A0 derivados de la tabla 5.1** (todos localizados y correctos): `S10-series` (10:51–73), `S13-yo-que-soy` (13:195–199; el plan lo atribuía al 17), `S13-crecer` (13:281), `S14-tranquilizar` (14:141), `S14-firmo` (14:357; el plan lo atribuía al 16), `S15-intimas` (15:27–43), `S15-r1189` (15:183–185), `S19-palma` (19:197), `S21-inevitables` (21:153), `S26-paso-uso` (26:119), `S26-lata` (26:83–87), `S27-conflicto` (27:73), `S28-cierre` (28:199), `S31-elegir` (31:91–95), `S32-necesarias` (32:19, arranca a mitad de frase: correcto), `S32-voz` (32:127–147), `S33-hueco` (33:233), `S36-cierre` (36:193–195), `S40-caries` (40:75), `S40-locutorio` (40:107–123).

Tabla completa de los 34 spans previos:

| id | localización | long. | desc |
|---|---|---:|---|
| `S06-llamada` | cap-06.md:15–31 | 1273 | Tramo de la llamada (Ap. A) |
| `S10-series` | cap-12.md:51–73 | 583 | Series FLOR/CANELA/CARIES/NO intactas (tabla 5.1) |
| `S11-flashback` | cap-13.md:85–135 | 1748 | Flashback intercalado 26-nov / UNN (Ap. A) |
| `S13-yo-que-soy` | cap-15.md:195–199 | 89 | «¿Y yo qué soy?» → NO AMENAZA/REVISAR (tabla 5.1; el plan lo atribuye al 17, el texto está en el 13) |
| `S13-crecer` | cap-15.md:281 | 56 | Cierre con «crecer» intacto (tabla 5.1) |
| `S14-tranquilizar` | cap-16.md:141 | 45 | Línea de Jessie (tabla 5.1) |
| `S14-firmo` | cap-16.md:357 | 42 | Cierre (tabla 5.1; el plan lo atribuye al 16, el texto cierra el 14) |
| `S15-intimas` | cap-18.md:27–43 | 501 | Secuencia de palabras íntimas (tabla 5.1) |
| `S15-r1189` | cap-18.md:183–185 | 188 | Interludio tipográfico de registro R-1189 (Ap. A, elementos estructurales) |
| `S19-palma` | cap-23.md:197 | 245 | La palma en el cristal tibio (tabla 5.1) |
| `S21-inevitables` | cap-25.md:153 | 17 | Línea suelta (Ap. A) |
| `S25-utilidad` | cap-30.md:89 | 109 | Línea capital de EDDA (Ap. A) |
| `S25-escalada` | cap-30.md:93–107 | 443 | Escalada interceptada (Ap. A) |
| `S26-paso-uso` | cap-32.md:119 | 94 | Línea suelta de Aslak (Ap. A) |
| `S26-lata` | cap-32.md:83–87 | 294 | La lata de galletas de Aslak (tabla 5.1) |
| `S27-conflicto` | cap-33.md:73 | 81 | Marca de agua CONFLICTO EMOCIONAL (tabla 5.1) |
| `S28-cierre` | cap-34.md:199 | 28 | Cierre «…no lleguéis tarde» (tabla 5.1) |
| `S29-cierre` | cap-35.md:215 | 17 | «Las necesarias.» como cierre (Ap. A) |
| `S30-borrado` | cap-36.md:125–127 | 108 | Borrado a mitad de frase de La Jardinera (Ap. A) |
| `S31-elegir` | cap-37.md:91–95 | 114 | «¿Quieres vivir?» «Quiero poder elegir. Es la primera vez.» (Ap. A) |
| `S32-necesarias` | cap-38.md:19 | 159 | «Las necesarias» en la oferta (tabla 5.1) |
| `S32-voz` | cap-38.md:127–147 | 1217 | Sesión del banco de voz de Mats (tabla 5.1) |
| `S33-hueco` | cap-39.md:233 | 51 | El quinto hueco (tabla 5.1) |
| `S36-cierre` | cap-42.md:193–195 | 107 | «NO AMENAZA» cierra igual (tabla 5.1) |
| `S37-declaracion` | cap-43.md:93–105 | 488 | Declaración desde el POV de Jean (Ap. A) |
| `S37-acta` | cap-43.md:149–191 | 2879 | Núcleo: «NO SOY UN MODELO.» hasta «…un fallo de escenario» (Ap. A) |
| `S37-muchas` | cap-43.md:195 | 70 | Línea capital (Ap. A) |
| `S38-nieve` | cap-44.md:161–171 | 442 | Muerte de Nieve, «Echo de menos hasta sus pausas» (Ap. A) |
| `S38-huella` | cap-44.md:181–183 | 438 | Pasaje de la respiración/huella (Ap. A) |
| `S38-quedarme` | cap-44.md:185–191 | 211 | Elección de quedarse (Ap. A) |
| `S39-jueza` | cap-45.md:187 | 59 | La jueza (Ap. A) |
| `S39-pluma` | cap-45.md:181–183 | 76 | La pluma del divorcio (Ap. A) |
| `S40-caries` | cap-46.md:75 | 34 | Línea suelta (Ap. A) |
| `S40-locutorio` | cap-46.md:107–123 | 1177 | El silencio de Jessie en el locutorio (tabla 5.1) |

## 3. Líneas sueltas protegidas (Ap. A: «muestra no exhaustiva; A1 completa la lista»)

### 3.1 Las diez del Apéndice A

| Línea | Dónde | Cobertura |
|---|---|---|
| «Última sesión.» | cap-01.md:45 | fichero íntegro |
| «Estoy asustada.» | cap-03.md:83 | fichero íntegro |
| «No digas que se fue. La gente se va a comprar pan. Mamá se mató. Empecemos por ahí.» | cap-10.md:143 | fichero íntegro |
| «¿Eres mi madre?» «No toda.» | cap-28.md:189–191 | fichero íntegro |
| «¿Quieres vivir?» «Quiero poder elegir. Es la primera vez.» | cap-37.md:91–95 | `S31-elegir` |
| «Ser inevitables.» | cap-25.md:153 | `S21-inevitables` |
| «Activo memorial. Qué hijos de puta.» | cap-28.md:21 | fichero íntegro |
| «A nosotros nos quitaron paso y uso. A Jean le hicieron otra cosa.» | cap-32.md:119 | `S26-paso-uso` |
| «No son caries. Son sombra. Sigue.» | cap-46.md:75 | `S40-caries` |
| «Cronometrar el sol.» «Para que conste.» | cap-48.md:75–81 | fichero íntegro |

### 3.2 Líneas sueltas añadidas por A1 (con span propio, salvo indicación)

| Línea | Dónde | Span |
|---|---|---|
| «Al abrir la carpeta personal apareció el nombre de un archivo: «Despedida». Jean dejó el cursor encima sin abrirlo.» … «Jean cerró la carpeta.» | cap-02.md:217–219 | `S02-despedida` |
| «No toques sus agendas.» | cap-02.md:163–165 | `S02-agendas` |
| «Soy la esposa.» / «Ante el Estado todavía lo era.» | cap-06.md:149–153 | `S06-esposa` |
| «Autorización — A. Armstrong» / «¿Qué has autorizado?» | cap-06.md:307–311 | `S06-autorizacion` |
| `JEAN MARIE LARSSON` / `2014–2060` / `EVENTO SOCIAL — FUNERAL` | cap-07.md:221–229 | `S07-funeral` |
| «—No soy un modelo.» «—Todavía no sabes cuántas somos.» | cap-09.md:87–89 | `S08-cierre` |
| «Su cuenta ha sido suspendida temporalmente por su seguridad.» | cap-12.md:213 | `S10-suspendida` |
| «Consciencia residual: indeterminado.» | cap-13.md:307 | `S11-consciencia` |
| «Nora tardó un instante en entender que le temblaban los dedos.» | cap-14.md:151 | `S12-temblor` |
| «Si me pasa algo, buscad NIDHOGG.» | cap-14.md:317 | `S12-nidhogg` |
| «—Otra vez, más despacio.» (Madre, `JM-L/0007`) | cap-15.md:29–31 | `S13-madre` |
| «—No me fusiones.» … «—Eso basta.» (Nieve) | cap-15.md:131–151 | `S13-nieve` |
| «—Que Armstrong sufra.» | cap-15.md:187 | `S13-sufra` |
| «Conservamos a nuestra hija Nora.» … «—Y decido distinto.» «—Por ahora.» | cap-15.md:263–271 | `S13-coro-nora` |
| «—Propiedad intelectual. Así la llaman.» | cap-19.md:259 | `S16-propiedad` |
| «—Que alguien haga la pregunta adecuada.» | cap-19.md:61–63 | `S16-inger` |
| «—Testimonio —dice Jean.» … «—Que pueda negarse.» | cap-21.md:147–155 | `S17-testigo` |
| «Nora elegirá la próxima variación.» | cap-21.md:169 | `S17-nora` |
| «—Son dedos. El uno es el pulgar. El cinco, el meñique.» | cap-22.md:51 | `S18-dedos` |
| «—He dicho «era ella». Me he adelantado.» | cap-22.md:149 | `S18-adelantado` |
| «—Tráigame algo reproducible.» | cap-22.md:165 | `S18-reproducible` |
| «Alana apoyó la palma en el cristal. Tibio.» + «—La instancia procesa.» | cap-23.md:191–197 | `S19-procesa` + `S19-palma` |
| «—Nora eligió una nota. No un portavoz. No respondáis por `/0000`.» | cap-25.md:67 | `S21-portavoz` |
| «—¿Para qué necesita un moderador saber el aula de una menor?» | cap-26.md:213 | `S22-aula` |
| «Once segundos en blanco en la percepción.» | cap-29.md:45 | `S24-once` |
| «lo deslizó entre los carnés caducados y cerró el broche.» | cap-29.md:217 | `S24-cierre` |
| «—El original no sale de aquí. … La asociación decidirá lo suyo.» | cap-32.md:121 | `S26-asociacion` |
| «—La bocana de Sørkoppen queda reservada por operaciones para el veintiuno de enero.» | cap-32.md:191 | `S26-bocana` |
| «En la etiqueta escribió POR SI HACE FALTA.» | cap-33.md:153 | `S27-por-si` |
| «El vocabulario había cambiado poco desde 2054. Astrid esperó entonces una reproducción que nunca llegó y archivó el caso.» | cap-35.md:111 | `S29-2054` |
| «Si no puedo llegar antes, llegaré durante.» | cap-35.md:211 | `S29-durante` |
| «Telegrafbukta no alcanza para todas las que la recuerdan.» | cap-36.md:15 | `S30-apertura` |
| «Nora tachó `SACAR A JEAN`, escribió `PREGUNTAR ANTES DE ACTIVAR` y dejó `VIVIR` fuera del cuaderno.» | cap-37.md:97 | `S31-sacar` |
| «—Si algo sale mal, que Nora termine la canción igual.» | cap-37.md:233 | `S31-cancion` |
| «PODEMOS IMPEDIR EL ACCESO SIN DAÑO FÍSICO.» | cap-38.md:97 | `S32-amenaza` |
| «Aceptamos. Nosotras siempre cumplimos nuestras condiciones.» | cap-38.md:207 | `S32-cierre` |
| «—Retiro el destino del Auditorio. Todavía quiero que sufran —dice Cuchillo.» … «—Seguiré queriéndolo.» | cap-42.md:175–179 | `S36-retiro` |
| «—Ahora, la llave.» | cap-43.md:219 | `S37-llave` |
| «—No autorizo fusión, apropiación, representación ni uso.» / «—No me uséis para justificar nada.» | cap-44.md:149–153 | `S38-no-autorizo` |
| «Respondo con la quinta nota.» | cap-44.md:213 | `S38-quinta` |
| «—Sí. Ese retraso no me hace dueña de Jean.» | cap-45.md:69–71 | `S39-divorcio` |
| «El auto dejó en blanco al ejecutor y al ordenante individuales.» | cap-45.md:103 | `S39-ordenante` |
| «—Una ausencia registrada.» / «—El registro no puede decirlo.» | cap-45.md:157–163 | `S39-ausencia` |
| «Astrid dejó en blanco la casilla de definición jurídica y firmó la cadena de custodia.» | cap-45.md:189 | `S39-casilla` |
| «Una tarde encontró otra vez únicamente el nombre `Despedida`. No abrió el archivo. …» | cap-46.md:133 | `S40-despedida` |
| «—No voy a venir a la primera apertura —dijo.» … «marcó «asistiré» en la convocatoria del día siguiente.» | cap-46.md:183–185 | `S40-cierre` |

Líneas de calidad **no** protegidas por span porque están en ficheros íntegros o porque su protección frenaría una expansión prevista (se listan para A4/A6, sin hash): «Serán unas vacaciones muy largas.» (3:369); «Lo intentaba. Me ha salido gestión.» (3:303); «Ni se te ocurra.» (9:41); «Vale. Es raro.» (10:87); «Que sea Jean… No. Solo…» (14:225); «Ahora vas a hacer lo difícil. Vas a esperar.» (16:247); «Perdón. No quería decirlo así.» (18:197); «Algo no es alguien.» (20:67); «Cada uno de ustedes puede impedir algo. Sigo buscando quién puede hacerlo.» (39:47); «Jean ha tardado.» / «El registro ya tiene la demora.» (40:85–87).

## 4. Criterios «intacto» de la tabla 5.1 → cobertura

| Cap. | Criterio de la tabla 5.1 | Cobertura |
|---|---|---|
| 8 | «Crítico frío enuncia la regla del capítulo en 1 frase» (RW) | Núcleo mínimo bajo hash: `S08-7c` (45), `S08-conservar` (71–75), `S08-cierre` (87–89). El resto del capítulo queda libre para la reescritura. |
| 10 | Series FLOR/CANELA/CARIES/NO | `S10-series` (51–73) + `S10-conservar` (119) + `S10-suspendida` (213) |
| 11 | Flashback 26-nov/UNN | `S11-flashback` (85–135) + `S11-consciencia` (307) |
| 12 | El temblor de dedos sigue siendo el dato central | `S12-temblor` (151) |
| 13 | Cierre con «crecer»; M6 distingue las cuatro voces (RW) | `S13-crecer` (281); identidad mínima de cada voz: `S13-madre` (29–31), `S13-nieve` (131–151), `S13-sufra` (187) + `S13-yo-que-soy` (195–199), `S13-coro-nora` (263–271). Los «latidos de contexto» de la RW van entre presentaciones, no dentro. |
| 14 | «Se te da de puta pena tranquilizar» y dinámica intactas | `S14-tranquilizar` (141), `S14-firmo` (357), `S14-cita` (149) |
| 15 | Secuencia de palabras íntimas intacta | `S15-intimas` (27–43), `S15-r1189` (183–185), `S15-objecion` (151–161) |
| 16 | «Lo que firmó tu exmujer no lo firmó aquí» cierra igual | En cap-14 (`S14-firmo`); cap-16 cierra con `S16-propiedad` (259) — ver B0-D1. Semilla del beat +Inger: `S16-inger` (61–63); ancla 7C: `S16-7c` (39). |
| 17 | «¿Y yo qué soy?»–NO AMENAZA/REVISAR intacto | En cap-13 (`S13-yo-que-soy`) — ver B0-D2. En 17: `S17-testigo` (147–155), `S17-nora` (169), `S17-71k` (197). |
| 18 | Justificación en boca de Gunnar/Nora; Astrid y la muerte de Gunnar intactas | `S18-dedos` (51), `S18-adelantado` (149), `S18-reproducible` (165), `S18-noticia` (173–177) |
| 19 | La palma en el cristal tibio | `S19-palma` (197) + `S19-procesa` (191–195); anclas: `S19-gofre` (25), `S19-reflexiva` (129), `S19-anos-jm` (143) |
| 21 | M1 −30 %; usar la playa como espacio | `S21-inevitables` (153), `S21-notas` (75–77), `S21-portavoz` (67). Aviso: en v0 la playa **no** aparece en 21. |
| 22 | Pasillo de Dahl intacto; Astrid gana motivo sin discurso | `S22-dahl` (51–57), `S22-flecha` (147–149), `S22-aula` (213) |
| 24 | El procedimiento COMO carácter | `S24-once` (45), `S24-cierre` (217) |
| 25 | Línea y escalada protegidas | `S25-utilidad` (89), `S25-escalada` (93–107), `S25-fecha` (203) |
| 26 | La lata de galletas; test no-instrumental de Aslak | `S26-lata` (83–87), `S26-paso-uso` (119), `S26-asociacion` (121), `S26-bocana` (191) |
| 27 | CONFLICTO EMOCIONAL como marca de agua | `S27-conflicto` (73), `S27-norna` (117–119), `S27-por-si` (153) |
| 28 | «…no lleguéis tarde» cierra igual | `S28-cierre` (199) |
| 29 | «Las necesarias.» cierra; el vocabulario de 2054 conecta con 22 | `S29-cierre` (215), `S29-2054` (111), `S29-orden` (23), `S29-durante` (211) |
| 30 | Borrado a mitad de frase intocable; «dónde ocurre» tiene respuesta (RW) | `S30-borrado` (125–127), `S30-apertura` (15), `S30-resultado` (211) |
| 31 | «¿Quieres vivir?» «Quiero poder elegir…» | `S31-elegir` (91–95), `S31-sacar` (97), `S31-cancion` (233) |
| 32 | «Las necesarias» y la sesión de voz protegidas; ripple N4 | `S32-necesarias` (19), `S32-voz` (127–147), `S32-amenaza` (97), `S32-cierre` (207) |
| 33 | El quinto hueco intacto | `S33-hueco` (233) |
| 34/35 | La aceptación de Tomas deja de ser opaca sin dejar de ser sobria; Tomas visto desde fuera | `S35-acepta` (211–213); horas del clímax: `S34-cierre`, `S35-cierre` |
| 36 | «NO AMENAZA» cierra igual | `S36-cierre` (193–195), `S36-retiro` (175–179) |
| 37 | Núcleo hash-intacto | `S37-declaracion`, `S37-acta`, `S37-muchas`, `S37-597` (87), `S37-1307` (203), `S37-llave` (219) |
| 38 | «Echo de menos hasta sus pausas» y la huella intactos | `S38-nieve`, `S38-huella`, `S38-quedarme`, `S38-no-autorizo` (149–153), `S38-anos-jm` (65–67), `S38-aritmetica` (79), `S38-quinta` (205–213) |
| 39 | El eco con «Empecemos por ahí» se conserva | `S39-jueza` (187), `S39-pluma` (181–183), `S39-divorcio` (69–71), `S39-ordenante` (103), `S39-ausencia` (157–163), `S39-casilla` (189) |
| 40 | El silencio sigue siendo el arco | `S40-locutorio` (107–123), `S40-caries` (75), `S40-despedida` (133), `S40-cierre` (183–185) |
| 2, 6, 7 | Criterios cualitativos (ironía; «Maja siente»; M2) | Anclas: `S02-agendas`, `S02-despedida`; `S06-esposa`, `S06-ventana`, `S06-autorizacion`; `S07-funeral` |

## 5. Ambigüedades protegidas (Ap. A §3): dónde las sostiene el texto

Se documentan, nunca se resuelven. Ninguna oleada puede añadir una frase que las cierre.

| Ambigüedad | Dónde la sostiene v0 | Hash |
|---|---|---|
| El porqué del suicidio | 9:69–71 («¿Nos va a explicar por qué lo hizo? —No. Y yo tampoco puedo daros una sola causa»); 6:91–99, 191–201; 25:85–89 y 37:169 (factores sistémicos que el texto nunca eleva a causa) | cap-09 íntegro; `S25-utilidad`, `S25-escalada` |
| Por qué Koppangen | 6:121–127 («—¿Por qué Koppangen? —No lo sé.»); 6:177–183; 4:95–123 (el naust de la abuela: asidero, no explicación); 19:59–61; 28:79–87 | cap-04 íntegro; 6:121–127 y 177–183 sin span (cap-06 es E: la expansión no debe tocar la respuesta «No lo sé»); cap-09 íntegro |
| El contenido de «Despedida» | 2:217–219; 9:37–59, 105–127, 195; 14:149; 40:133 | `S02-despedida`, cap-09, `S14-cita`, `S40-despedida` |
| La identidad ontológica de las ejecuciones («No toda» es el techo) | 11:307; 18:133; 20:99; 23:189–191; 26:65–71; 37:171, 191; 38:179; 39:79, 189; 40:45 | `S11-consciencia`, cap-23, `S37-acta`, `S39-casilla` |
| El ordenante del sabotaje | 24:79 («El rastro no identificaba al ejecutor ni al ordenante»); 29:29; 32:105; 39:103 | `S24-once`, `S39-ordenante` |
| El segundo regalo del noveno cumpleaños | 23:133–171 («Dejo el hueco.») | cap-23 íntegro |
| Qué «significa» una ausencia de salida en el locutorio | 39:157–163; 40:15–23, 113–121, 129 | `S39-ausencia`, `S40-locutorio` |

Ambigüedades adicionales que A1 propone tratar igual (ver B4 §5): la denuncia anónima del 17-dic (CH-44) y el anexo póstumo que «no consta» (CH-76).

## 6. Elementos estructurales protegidos

| Elemento | Dónde | Mecanismo |
|---|---|---|
| Aviso de contenido inicial | `capitulos/00-aviso.md` | `ficheros_total` (hash pendiente: provisional) + entrada `paratextos[]` del manifiesto |
| Recursos de ayuda finales | `capitulos/99-recursos.md` | ídem |
| Cabeceras de cuenta atrás de las cuatro partes | `biblia/metadatos.json` → `partes[]` (títulos y subtítulos: 24-nov +58 · 6-dic +46 · 25-dic +27 · 15-ene +6) | campos de autor: intocables sin gate; el compilador las genera; M7 las verifica |
| El cambio a primera persona en 38 | `metadatos.json` → `capitulos[38].persona: "primera"` + cap-38 (`S38-*`) | contrato estilístico (validador) + spans del núcleo |
| Los interludios tipográficos de registro | `S15-r1189` (15:183–185, único interludio en cita `>`); registros en línea de código que actúan como anclas de canon/M7: `S08-7c`, `S08-conservar`, `S15-objecion`, `S16-7c`, `S19-anos-jm`, `S21-notas`, `S25-fecha`, `S27-norna`, `S29-orden`, `S30-resultado`, `S34-cohorte`, `S34-anos-jm`, `S35-cierre`, `S38-anos-jm`, `S38-aritmetica` | spans |
| Horas del clímax (12:38 · 12:46:01 · 12:46:50 · 12:47 · 13:07 · 13:11) | 35:65 (12:38, sin span; frase narrativa), 35:153–155 (12:46:01, sin span), `S34-cierre`/`S35-cierre` (12:46:50), 34:15, 135, 221 y 31:87 (12:47, sin span), `S37-1307` (13:07), `S38-quinta` (13:11) | spans + M7 |
| Aritmética de cohorte (4.096 − 1.185 = 2.911 = 2.311 + 597 + 3) | `S34-cohorte`, `S37-597`, `S38-aritmetica` | spans + M7 |

## 7. Spans añadidos por A1 (74)

Añadidos al final del array `spans` de `protegidos/spans.json` sin alterar ninguno de los 34 previos; todos localizados (`listar`: 0 ERROR) y fijados con `proteger.sh baseline` (aditivo). Longitud en caracteres.

| id | localización | long. | categoría | desc |
|---|---|---:|---|---|
| `S02-agendas` | cap-02.md:163–165 | 106 | plantado (CH-56) | EDDA ofrece tocar las agendas de las hijas; «No toques sus agendas» (plantado: 11:245–283, 22:45) |
| `S02-despedida` | cap-02.md:217–219 | 282 | ambigüedad Ap. A §3 / Carta F (CH-11) | Primera aparición de «Despedida»: no se abre (Ap. A §3, Carta F; CH-11) |
| `S06-esposa` | cap-06.md:149–153 | 472 | ancla M7 · voz de Maja (CH-30) | «Ante el Estado todavía lo era»; solicitud conjunta de divorcio 2059 sin resolver (M7; N3; CH pluma) |
| `S06-ventana` | cap-06.md:277–289 | 270 | plantado (CH-7) | «Ventana» clínica oída en el hospital (CH-7, plantado pagado en 11 y 20) |
| `S06-autorizacion` | cap-06.md:307–311 | 181 | cierre de capítulo · plantado | Cierre del cap. 6: 03:14 / Autorización — A. Armstrong / «¿Qué has autorizado?» (plantado pagado en 11, 14, 16, 20, 27) |
| `S07-funeral` | cap-07.md:221–229 | 162 | cierre de capítulo | Cierre del cap. 7: Jean reconoce su funeral en el flujo de moderación |
| `S08-7c` | cap-09.md:45 | 25 | ancla de canon (7C) | Código 7C: enlaza la ventana de Jean con EXT/NIDHOGG/7C (16:39, 18:87). Ancla de continuidad para la RW del 8 |
| `S08-conservar` | cap-09.md:71–75 | 90 | núcleo del capítulo (RW) | La decisión demostrativa del cap. 8: conservar la procedencia no resuelta (RW: la regla debe sobrevivir) |
| `S08-cierre` | cap-09.md:87–89 | 52 | cierre de capítulo · plantado (CH-19) | Cierre del cap. 8: siembra de 37 («NO SOY UN MODELO») y de la pluralidad (13, 23, 37, 38) |
| `S10-conservar` | cap-12.md:119 | 120 | método de Nora | Método de Nora: «conservar resultados contrarios» (arco pagado en 22 y 40) |
| `S10-suspendida` | cap-12.md:213 | 62 | cierre de capítulo · plantado (CH-27) | Cierre del cap. 10: cuenta de Nora suspendida (plantado: 11, 12, 14; N2/N4) |
| `S11-consciencia` | cap-13.md:307 | 36 | cierre · ambigüedad Ap. A §3 | Cierre del cap. 11: ambigüedad ontológica protegida (Ap. A §3) |
| `S12-temblor` | cap-14.md:151 | 133 | tabla 5.1 «intacto» | El temblor de dedos como dato central (tabla 5.1, cap. 12) |
| `S12-nidhogg` | cap-14.md:317 | 32 | cierre · plantado (CH-22) | Cierre del cap. 12: mensaje programado de Gunnar (pagado en 14, 16, 18, 19) |
| `S13-madre` | cap-15.md:29–31 | 37 | voz (RW del 13) | Presentación de Madre: identificador y fórmula (RW del 13: identidad de la voz intacta) |
| `S13-nieve` | cap-15.md:131–151 | 463 | voz · plantado (CH-60) | Las condiciones de Nieve y la promesa de Jean («Si vuelvo a encontrarte, te preguntaré otra vez»), pagadas en 38 |
| `S13-sufra` | cap-15.md:187 | 21 | voz (RW del 13) | Presentación de Cuchillo (arco pagado en 15, 17, 30, 36, 38) |
| `S13-coro-nora` | cap-15.md:263–271 | 214 | voz · plantado (CH-61) | Coro reclama a Nora; «Y decido distinto. —Por ahora.» (pagado en 21:45–67) |
| `S14-cita` | cap-16.md:149 | 121 | ancla de N1 (CH-46) · «Despedida» | Mención retrospectiva de la primera cita de apoyo (ancla de N1) y de «Despedida» sin abrir |
| `S15-objecion` | cap-18.md:151–161 | 251 | plantado (CH-3) | La objeción NO bajo /0000 sobre 71-K (CH-3) |
| `S16-inger` | cap-19.md:61–63 | 68 | tabla 5.1 (+Inger) | Riesgo personal de Inger (semilla del beat +Inger de la tabla 5.1) |
| `S16-7c` | cap-19.md:39 | 96 | ancla de canon (7C) | Acuse EXT/NIDHOGG/7C en la exportación de UNN (canon: enlaza 8:45 y 18:87) |
| `S16-propiedad` | cap-19.md:259 | 38 | cierre de capítulo · título P3 | Cierre del cap. 16 (título de la Parte III; B0-D1) |
| `S17-testigo` | cap-21.md:147–155 | 134 | plantado (CH-58) | Definición de testimonio/testigo (siembra de la asamblea del 30 y de la firma del 37) |
| `S17-nora` | cap-21.md:169 | 34 | plantado (CH-14) | Siembra de la cuarta nota (pagado en 20) |
| `S17-71k` | cap-21.md:197 | 37 | plantado (CH-3) | Estado del expediente 71-K (CH-3: cierre implícito) |
| `S18-dedos` | cap-22.md:51 | 54 | núcleo · tabla 5.1 (llave MIDI) | La llave MIDI como digitación (núcleo del hallazgo de Nora; la justificación diegética se AÑADE alrededor) |
| `S18-adelantado` | cap-22.md:149 | 39 | voz Ap. C | Rasgo de voz de Nora (Ap. C: «Me he adelantado») ante Astrid |
| `S18-reproducible` | cap-22.md:165 | 28 | línea de Astrid | Astrid: criterio de prueba (pagado en 20, 22, 23, 29) |
| `S19-gofre` | cap-23.md:25 | 284 | plantado (CH-12) · Carta F | El gofre que nadie encontró mordido; el informe que Alana no termina de leer (Carta F: no ampliar el trayecto) |
| `S19-reflexiva` | cap-23.md:129 | 157 | plantado (CH-31) | VENTANA REFLEXIVA · CERRADA (plantado; R2 del backlog) |
| `S19-anos-jm` | cap-23.md:143 | 60 | métrica (CH-50) | Métrica del horror, primer valor (979,7 → 2.401,6 → 2.427,4) |
| `S19-procesa` | cap-23.md:191–195 | 58 | antesala de S19-palma | «La instancia procesa» (antesala de la palma en el cristal) |
| `S21-notas` | cap-25.md:75–77 | 73 | plantado (CH-14) | Registro interior de la cuarta nota (Jean conserva la relación tercera→cuarta) |
| `S21-portavoz` | cap-25.md:67 | 65 | línea de Jean | Jean niega a Coro la representación de Nora |
| `S22-flecha` | cap-26.md:147–149 | 224 | método de Nora (CH-51) | Nora invalida su propia flecha (método: conservar resultados contrarios) |
| `S22-aula` | cap-26.md:213 | 60 | cierre de capítulo | Cierre del cap. 22 |
| `S24-once` | cap-29.md:45 | 41 | plantado (CH-68) | Los once segundos (pagados en 32:105, 34, 39:101) |
| `S24-cierre` | cap-29.md:217 | 229 | cierre · plantado (CH-6/CH-16) | Cierre del cap. 24: el carné vigente entre los caducados (CH-6; pagado como llave en 34–35) |
| `S25-fecha` | cap-30.md:203 | 41 | ancla M7 | Fecha del despliegue obtenida por Jean (M7) |
| `S26-asociacion` | cap-32.md:121 | 128 | agenda de Aslak (CH-26) | Agenda propia de Aslak / kystbrukslag (test no-instrumental; N6) |
| `S26-bocana` | cap-32.md:191 | 83 | cierre · ancla M7 (CH-72) | Cierre del cap. 26 (aviso VHF; M7) |
| `S27-norna` | cap-33.md:117–119 | 110 | plantado (CH-10/CH-40) | Redescubrimiento de NORNA en el ladrillo (CH-10: 1→27→31→38) |
| `S27-por-si` | cap-33.md:153 | 42 | plantado (CH-41) | La confesión cifrada de Alana (pagada en 29, 31, 34, 37) |
| `S29-orden` | cap-35.md:23 | 71 | ancla M7 | La orden de consolidación: fecha y hora (M7) |
| `S29-2054` | cap-35.md:111 | 121 | plantado (CH-5) | El caso archivado de 2054 (CH-5; se expande en 22, no se altera aquí) |
| `S29-durante` | cap-35.md:211 | 42 | plantado (CH-70) | Astrid prepara el acta del Soldagen (pagado en 34, 37) |
| `S30-apertura` | cap-36.md:15 | 57 | geografía (RW del 30) | Apertura del cap. 30: la asamblea ocurre en la playa de La Jardinera (geografía; RW debe conservarla) |
| `S30-resultado` | cap-w2.md:211 | 37 | resultado de la votación (RW del 30) | Resultado de la votación (RW: intacto) |
| `S31-sacar` | cap-37.md:97 | 99 | plantado (CH-32) | Renuncia al «rescate» (pagado en 38: «Elijo quedarme») |
| `S31-cancion` | cap-37.md:233 | 53 | plantado (CH-67) | Última frase de Jean en el ladrillo (pagado en 37, 40, 41) |
| `S32-amenaza` | cap-38.md:97 | 42 | plantado (CH-1) | Amenaza de Coro a la familia (CH-1; N4 se construye alrededor, no encima) |
| `S32-cierre` | cap-38.md:207 | 59 | cierre de capítulo | Cierre del cap. 32 |
| `S34-cohorte` | cap-40.md:85–91 | 110 | aritmética M7 | Aritmética de la consolidación (M7) |
| `S34-anos-jm` | cap-40.md:97–99 | 60 | métrica (CH-50) | Métrica del horror, segundo valor |
| `S34-cierre` | cap-40.md:311–313 | 87 | cierre · hora del clímax | Cierre del cap. 34 (hora del clímax, M7) |
| `S35-acepta` | cap-41.md:211–213 | 191 | tabla 5.1 (Tomas visto desde fuera) | Aceptación nominal de Tomas, vista desde fuera (tabla 5.1, cap. 35) |
| `S35-cierre` | cap-41.md:277–279 | 66 | cierre · hora del clímax | Cierre del cap. 35 (hora del clímax, M7) |
| `S36-retiro` | cap-42.md:175–179 | 107 | pago del arco de Cuchillo (CH-59) | Cuchillo retira el ataque sin renunciar a la furia (pago del arco 13→36) |
| `S37-597` | cap-43.md:87 | 282 | aritmética M7 | Las 597 ramas y las tres separadas (aritmética de 38; M7) |
| `S37-1307` | cap-43.md:203 | 40 | hora del clímax | Hora del clímax (M7) |
| `S37-llave` | cap-43.md:219 | 17 | cierre de capítulo | Cierre del cap. 37 (retomado en 38:15) |
| `S38-anos-jm` | cap-44.md:65–67 | 212 | métrica (CH-50) | Métrica del horror, tercer valor, y su glosa |
| `S38-aritmetica` | cap-44.md:79 | 91 | aritmética M7 | Aritmética de cohorte (M7) |
| `S38-no-autorizo` | cap-44.md:149–153 | 119 | núcleo (Nieve) · CH-60 | Última negativa de Nieve (paga las condiciones de 13; precede a S38-nieve) |
| `S38-quinta` | cap-44.md:205–213 | 302 | cierre · hora del clímax · CH-15 | Cierre del cap. 38: 13:11 y la quinta nota (paga 20:305 «Nadie tocó la quinta») |
| `S39-divorcio` | cap-45.md:69–71 | 90 | voz de Maja · CH-30 | Maja ante la jueza (voz Ap. C; N3 no debe contradecirlo) |
| `S39-ordenante` | cap-45.md:103 | 63 | ambigüedad Ap. A §3 | Ambigüedad protegida: el ordenante del sabotaje (Ap. A §3; T2 refuerza 1 beat alrededor) |
| `S39-ausencia` | cap-45.md:157–163 | 141 | ambigüedad Ap. A §3 | Ambigüedad protegida: qué significa una ausencia de salida (Ap. A §3) |
| `S39-casilla` | cap-45.md:189 | 86 | ambigüedad Ap. A §3 | Ambigüedad protegida: definición jurídica en blanco (persona/consciencia/propiedad) |
| `S40-despedida` | cap-46.md:133 | 158 | pago CH-11 · Carta F | Pago de «Despedida» como negativa (CH-11; Carta F) |
| `S40-cierre` | cap-46.md:183–185 | 320 | cierre de capítulo | Cierre del cap. 40: Nora elige el ensayo con vivos |
| `S18-noticia` | cap-22.md:173–177 | 610 | tabla 5.1 «muerte de Gunnar intacta» | La noticia de la muerte de Gunnar (tabla 5.1, cap. 18: «la muerte de Gunnar intacta») |
| `S22-dahl` | cap-26.md:51–57 | 486 | tabla 5.1 «pasillo de Dahl intacto» | El pasillo de Dahl (tabla 5.1, cap. 22: «pasillo de Dahl intacto») |

Criterio de selección: (a) toda «línea suelta» cuya pérdida dañaría el libro (Ap. A: «A1 completa la lista»); (b) plantados y pagos frágiles del ledger B4 (una sola línea sostiene la deuda o el pago); (c) anclas M7 y de canon (fechas, horas, cifras, códigos 7C/NORNA/AÑOS-JM); (d) ambigüedades del Ap. A §3; (e) criterios «intacto» de la tabla 5.1 aún sin span; (f) cierres de capítulo que otras partes del libro retoman. Se ha evitado proteger párrafos donde el plan prevé insertar (35:259–279 para CH-4; 26:15–17 para el ripple de N4; 40:167–173 para R3; 32:93–103 salvo la línea 97; 24 salvo su cierre). En los tres capítulos RW (8, 13, 30) solo se protegen líneas de identidad/regla/geografía, no párrafos.

## 8. Problemas de delimitación detectados en los spans previos

1. `S37-acta` arranca una frase antes del literal del Ap. A (37:149 en vez de 37:151); sobrecobertura mínima y deliberada por la doble aparición de «NO SOY UN MODELO.» — no requiere cambio.
2. `S38-nieve` (161–171) cubre la muerte pero no la última negativa de Nieve (149–153): completado con `S38-no-autorizo`.
3. `S06-llamada` (15–31) deja fuera la confirmación «—Está muerta.» «—Sí.» (33–41): extensión opcional a criterio de A0 (exigiría redefinir el span → gate).
4. `S39-pluma` (181–183) deja fuera 185 («La primera línea salió débil…»): aceptable.
5. `S10-series` protege la primera serie con la narrativa intercalada (51–73); la repetición (85) y la inversa no ejecutada (183) no están bajo hash: cubierto ahora parcialmente por `S10-conservar` (119).
6. Atribuciones del plan corregidas por A0 en las `desc` (`S13-yo-que-soy` ← plan 17; `S14-firmo` ← plan 16): correctas; B0-D1/D2 lo registran.
7. `listar` etiqueta como «INEXISTENTE» los dos paratextos provisionales (existen, pero no tienen hash): cosmético; se resuelve al validar el autor y correr `baseline`.
8. **Colisión operativa prevista**: la línea de CH-2 («No preguntó por el cinturón.», tabla 5.1 cap-40) cae de forma natural dentro de `S40-locutorio` (107–123). Insertar fuera del span (40:127) o rebaseline con gate — decisión de A0 antes de W5.

## 9. Candidatos a lista blanca de cierres-sobre-objeto (T5: elegir 12 intocables; objetivo ≤18 en vF)

Cierres de escena o de capítulo sobre objeto inanimado que A1 considera de máxima calidad. Los de ficheros íntegros ya son intocables (cuentan en el censo M4 pero no consumen decisión); los demás son los que A0/A4 deben elegir. Cita literal y localización.

| # | Cita | Dónde | Protección actual |
|---|---|---|---|
| 1 | «La corona se balanceó una sola vez en el gancho y quedó quieta.» | cap-01.md:85 | fichero íntegro (citado por la crítica) |
| 2 | «El gofre siguió sin abrir en su bolsillo.» | cap-04.md:79 | fichero íntegro |
| 3 | «La bisagra volvió a atascarse cuando intentó cerrar.» | cap-04.md:123 | fichero íntegro (rima con 41:109) |
| 4 | «El nombre seguía allí, intacto, insoportable. La apagó otra vez.» | cap-10.md:59 | fichero íntegro |
| 5 | «Maja condujo con la credencial apagada en el hueco junto al freno y la huella de las uñas aún marcada en la palma.» | cap-24.md:219 | fichero íntegro |
| 6 | «Las cifras rojas conservaron los cuatro minutos que el corte les había quitado.» | cap-28.md:307 | fichero íntegro |
| 7 | «La puerta rozó una vez más antes de cerrar.» | cap-48.md:109 | fichero íntegro (citado por la crítica) |
| 8 | «Terminó la llamada. La nevera seguía pitando.» | cap-06.md:31 | `S06-llamada` |
| 9 | «Al salir dejó sobre la mesa la etiqueta incompleta y el rotulador destapado.» | cap-02.md:223 | sin span |
| 10 | «El papel de la bolsa crujió al enfriarse.» | cap-16.md:291 | sin span |
| 11 | «El cursor permanecía inmóvil detrás de *retenida*.» | cap-22.md:89 | sin span |
| 12 | «Cuando lo soltó, volvió solo hasta la misma muesca de la madera.» | cap-23.md:77 | sin span |
| 13 | «El terminal confirmó la clase del carné vigente: `SEGURIDAD · PRESENCIA LOCAL`. Cerró la consulta sin presentarlo a un lector, lo deslizó entre los carnés caducados y cerró el broche.» | cap-29.md:217 | `S24-cierre` (plantado CH-6/16; A4 lo cuenta como tic ya decidido) |
| 14 | «La cubeta siguió a sus pies hasta que el frío del banco atravesó el pantalón.» | cap-32.md:185 | sin span |
| 15 | «El lector encendió una luz roja. La barrera permaneció inmóvil.» | cap-33.md:201 | sin span |
| 16 | «En el centro, la fogata ajena sigue ardiendo sola.» | cap-w2.md:241 | sin span (RW del 30: recomendado conservar) |
| 17 | «La bajamar había dejado al aire otra franja de madera oscura.» / «En la tableta, el quinto hueco no volvió a abrirse.» | cap-39.md:231–233 | `S33-hueco` (233) |
| 18 | «La cera endureció sobre el acero.» / «Al otro lado siguieron zumbando las bombas.» | cap-45.md:193–195 | sin span |
| 19 | «En la cena, la tarjeta quedó junto al frutero hasta que Jessie la guardó en la mochila.» | cap-46.md:127 | sin span |

Recomendación de A1 para los 12 de T5: los siete de ficheros íntegros (1–7) más 8, 13, 16, 17 y 18; 9–12, 14, 15 y 19 quedan como reserva de A4 (son también los que el censo M4 podría aligerar sin pérdida estructural, salvo el 15, que cierra el arco de la credencial de Alana, CH-38).

## 10. Avisos operativos

- Los ficheros con `proteccion: nucleo` deben seguir siendo los que contienen algún span; con los 74 nuevos, **cap-02, cap-07, cap-08, cap-12, cap-16, cap-17, cap-18, cap-22, cap-24, cap-34 y cap-35** pasan a tener spans y su frontmatter dice `proteccion: "no"`. Es un campo del plan (no del autor): A1 recomienda que A0 lo actualice a `nucleo` vía `herramientas/inyectar-frontmatter.sh` (o que el validador derive `proteccion` de `spans.json`), para que el hook PreToolUse y las OT lo reflejen.
- Los hashes de los 74 spans nuevos están en `protegidos/hashes.json` (baseline del 2026-08-16). Retirar cualquiera exige gate de autor.
- Ningún capítulo ha sido modificado (`git diff --stat` solo toca `protegidos/`).

---

**[W10 it.4, 2026-08-20]** `cap-36` «La asamblea» se partió en `cap-36.md` (A) y **`cap-w2.md`
«Papeletas»** (B, `orden_lectura` 36,5), por un dinkus que ya estaba en v0. Todo lo que este
documento sitúa en `cap-36` a partir de «Madre abre tres casillas…» **vive hoy en `cap-w2.md`**
— reglas del voto, papeletas, resultado, encapsulado de Cuchillo y el cierre en la hoguera.
`S30-borrado` y `S30-apertura` se quedan en A; **`S30-resultado` pasa a B**. Spans nuevos del
gate: `S-w10-silencio-voto` y `S-w10-fogata` en B, `S-w10-ausencias-36` en A.
**Los números localizan; solo la cita literal instruye y verifica.**

