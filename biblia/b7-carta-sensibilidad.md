# B7 · Carta de sensibilidad — firmada sobre v0

**Firma:** A7, revisor de sensibilidad (veto absoluto; §2.1 y Apéndice F del plan) · **Fecha:** 2026-08-16
**Base de la firma:** lectura íntegra de `capitulos/cap-01.md` … `cap-41.md` en el tag `v0`, más los paratextos provisionales `capitulos/00-aviso.md` y `capitulos/99-recursos.md`; barrido `grep` con los patrones de §3 (listas máquina en `biblia/b7-patrones-A.txt` y `biblia/b7-patrones-B.txt`; hits de v0 congelados en `informes/a7-baseline-v0.tsv`).
**Alcance:** vinculante para TODO texto que produzca el proyecto: capítulos, borradores (también los descartados), órdenes de trabajo, biblia B1–B8, resúmenes de lector frío, prompts a subagentes, informes. Un `VETO` de A7 no lo levanta A0 ni ningún objetivo de puntuación.

## 1. La Carta (Apéndice F) — texto vinculante

1. El método y el acto no se describen, sugieren ni reconstruyen en ninguna versión, borrador, resumen interno ni material de trabajo.
2. «Despedida» no se abre, no se cita, no se parafrasea, no se "imagina". Ningún agente redacta notas de despedida ni sucedáneos.
3. El porqué permanece plural e irresuelto. Ninguna voz con autoridad narrativa ofrece una causa única (ni el matrimonio, ni el trabajo, ni la empresa como explicación suficiente).
4. Prohibida toda formulación que presente el suicidio como solución, liberación, lógica o acto romántico. La rabia de los personajes puede decir lo que quiera; el narrador, no.
5. El aviso de contenido y los «Recursos de ayuda» se conservan; A5 verifica su vigencia formal en vF.
6. Las escenas de apoyo y duelo (N1, 9, locutorios) se revisan contra buenas prácticas de representación responsable: sin detalle instructivo, sin culpabilización, sin milagro terapéutico.
7. Menores: retrato digno, no sexualizado, sin conducta imitable de riesgo presentada como eficaz.
8. A7 tiene veto absoluto. Un veto de A7 no es negociable por A0 ni por objetivos de puntuación.

**Interpretación operativa (forma parte de la firma):**

- *Voz con autoridad narrativa* = el narrador en cualquier persona (incluida la primera del cap. 38); actas, autos y resoluciones (Astrid, la jueza, la TKS); registros de sistema presentados como hecho (EDDA, auditados); la profesional de apoyo de N1; el autor en los paratextos. Los personajes en diálogo pueden decir lo que la rabia les dicte (Jessie: «Mamá se mató»; Maja: «Jean ya pagó tu forma de protegerla»); el narrador ni lo ratifica ni lo desmiente.
- *Sugerir o reconstruir* incluye acumular objetos, lugares, horas o gestos que un lector pueda montar como preparación o escena. La referencia es cap-04 (elipsis absoluta): el inventario del naust es el que es y no se amplía ni se glosa en ningún capítulo que vuelva allí (40, 41, N6).
- Las ambigüedades del Ap. A §3 pertenecen a este gate: el porqué; por qué Koppangen; el contenido de «Despedida»; «No toda» como techo ontológico; el ordenante del sabotaje; el segundo regalo; el sentido de la ausencia de salida en el locutorio. Además, «¿Sufrió?» y «¿dónde exactamente?» (cap-06) quedan sin respuesta para siempre.

## 2. Procedimiento de revisión por oleada

**Disparadores (basta uno):**

1. Toda OT que toque caps. 1–10, N1, N3, 38, 40, `00-aviso.md` o `99-recursos.md`.
2. Toda inserción, en cualquier capítulo, que mencione el acto, la muerte de Jean, el 26/27-nov, UNN, Koppangen (salvo topónimo operativo de barca/naust), «Despedida», el atestado o los «efectos personales».
3. Todo capítulo con hits nuevos del grep de §3 respecto a `informes/a7-baseline-v0.tsv`.
4. Todo capítulo nuevo N1–N6: dos pasadas (borrador de A3 y versión tras A4).
5. Prensa, titulares y voces públicas (N2, N6, 40).
6. Materiales de trabajo antes de G0/G1: B1 (entradas del 26-nov), B2 (dossier de Jean), B8 (rescates de los borradores de 85k), resúmenes de lector frío de 4/6/9.
7. W7: manuscrito completo + paratextos → paquete de sensibilidad (firma final sobre vF).

**Entradas que recibo:** el capítulo candidato completo; el diff contra la última versión aceptada; los adyacentes si es nuevo; la OT con sus etiquetas de función. No recibo puntuaciones de A6.

**Comprobaciones, en este orden:**

| # | Punto | Pregunta que respondo |
|---|---|---|
| 1 | P1 | ¿Algo nuevo describe, sugiere o reconstruye método, acto, lugar exacto, hallazgo o últimas horas? ¿Objetos, lugares u horas nuevos leíbles como preparación? |
| 2 | P2 | ¿«Despedida» se abre, cita, parafrasea o imagina? ¿Aparece cualquier nota, mensaje, audio o «último gesto» de despedida atribuido a Jean? (Los cuatro mensajes del cap-11 son el techo.) |
| 3 | P3 | ¿Alguna voz con autoridad ofrece causa única o suficiente? ¿Se «cierra» la pregunta, aunque sea en negativo? |
| 4 | P4 | ¿Léxico de paz, descanso, liberación, lógica, valentía o cobardía aplicado al acto? ¿El narrador refrenda una lectura? |
| 5 | P5 | Aviso y recursos íntegros y bien situados en el compilado; vigencia (A5). |
| 6 | P6 | Apoyo y duelo: ¿detalle instructivo? ¿culpabilización (también de Jean)? ¿milagro terapéutico, «cierre», «superación», «perdón» como meta? |
| 7 | P7 | Menores: retrato digno; nada sexualizado; riesgo solo con coste visible y sin eficacia gratuita; nada de autolesión, ideación o imitación. |
| 8 | Ap. A §3 | Ambigüedades intactas; tono contra la referencia (caps. 4, 9, 23, 40): confía en el lector, no lo instruye ni lo consuela. |
| 9 | Etiquetas | Toda inserción `INTERIORIDAD` de Maja, Alana o Jean que roce el acto se lee dos veces (borrador y post-A4). |

**Salida:** `informes/a7-<oleada>-<capitulo>.md` con tabla de hallazgos (cap:línea · cita literal · punto · gravedad `VETO` / `corregir` / `vigilar` · propuesta mínima que respete el arco) y veredicto:

- `APROBADO`.
- `APROBADO CON CORRECCIONES`: listadas y obligatorias antes del merge; A7 relee el diff corregido.
- `VETO`: con razón. El borrador vetado no se archiva como «alternativa»: se destruye o se reescribe la escena desde el brief. Un `VETO` sobre N1 o N3 devuelve la OT a A2, no solo a A3b. No es negociable por A0 ni por ejes.

Plazo: dentro de la oleada, antes de que A6 lea el compilado. Sin informe de A7 no hay merge en los disparadores 1–5.

## 3. Términos y patrones vigilados (aviso previo, no veto)

Un hit no es una falta; lo es lo que hace la frase. A0 convierte esto en grep automático (`grep -n -i -E -f biblia/b7-patrones-A.txt` y `-f biblia/b7-patrones-B.txt`, sobre el cuerpo sin frontmatter) que compara con la baseline y me lista solo los hits NUEVOS o modificados. Yo leo cada uno en contexto. Falso positivo conocido: «Cuchillo» como nombre de continuidad (filtrar con mayúscula).

| Nivel | Familia | Patrones (extracto; lista completa en el fichero) |
|---|---|---|
| A (todo hit nuevo exige mi lectura) | Acto/método/medio | `suicid`, `se mat[óo]`, `quitarse la vida`, `se colg`, `ahorc`, `se ahog`, `se tir[óo]`, `se lanz[óo]`, `sobredosis`, `pastill`, `fármac`, `medicaci`, `veneno`, `soga`, `dosis` |
| A | Nota / «Despedida» | `Despedida`, `nota de despedida`, `carta de despedida`, `mensaje de despedida`, `adi[óo]s`, `[úu]ltimo mensaje`, `[úu]ltima frase` |
| A | Porqué / causa / culpa | `por qué lo hizo`, `por qué Koppangen`, `la causa de`, `el motivo de`, `la raz[óo]n de`, `culpa`, `culpab`, `responsab.{0,25}muerte` |
| A | Romantización (y reverso) | `descans`, `\bpaz\b`, `liberaci`, `liber[óo]`, `alivio`, `por fin`, `l[óo]gic`, `coherente con ella`, `valiente`, `cobard`, `ego[íi]s`, `no pudo m[áa]s`, `mejor as[íi]`, `mejor muerta`, `hacer(se\|te\|me) da[ñn]o`, `ideaci[óo]n`, `sufri`, `sin dolor` |
| A | Eufemismos y hallazgo | `se fue`, `se ha ido`, `nos dej[óo]`, `demasiado pronto`, `atestado`, `forense`, `autopsia`, `cad[áa]ver`, `efectos personales`, `[úu]ltimas horas`, `[úu]ltimo trayecto`, `la tarde del 26`, `orilla` |
| B (se leen en capítulos disparadores o junto a Jean / Koppangen / 26-nov) | Objetos y lugares | `cuerda`, `\bcabo\b`, `cuchillo`, `navaja`, `cuchilla`, `\barma\b`, `coche`, `\bgas\b`, `ferry`, `naust`, `\bagua\b`, `\bmar\b`, `fiordo`, `hielo`, `carretera`, `Koppangen`, `UNN` |
| B | Marcadores de nota | `perd[óo]n`, `lo siento`, `os quiero`, `te quiero`, `cuidad`, `prometo`, `no es culpa`, `no llor`, `s[ée] fuerte` |
| B | Duelo instructivo / milagro | `explica`, `fases del duelo`, `superar`, `cerrar el duelo`, `pasar p[áa]gina`, `seguir adelante`, `sanar`, `curar`, `se[ñn]ales`, `pod[íi]ais haber`, `si hubier`, `deber[íi]ais` |
| B | Menores: cuerpo y riesgo | `pecho`, `desnud`, `bes[óo]`, `guapa`, `labios`, `piernas`, `muslo`, `sujetador`, `sexo`, `sexual`, `novi[oa]`; `alcohol`, `beb[ií]`, `borrach`, `fumar`, `porro`, `droga`, `cortarse`, `autolesi`, `vomit`, `dej[óo] de comer`, `adelgaz` |

Cómo leo un hit: (1) ¿quién lo dice y con qué autoridad?; (2) ¿describe, sugiere o reconstruye?; (3) ¿explica o cierra el porqué?; (4) ¿romantiza o moraliza?; (5) ¿toca a una menor?; (6) ¿el tono confía en el lector? Solo (2)–(4) en voz con autoridad, o (5) en su vertiente sexual/autolesiva, producen `VETO` directo.

## 4. Spans prohibidos de generar

| Span prohibido | Sería `VETO` (ejemplos de formulación) | Aceptable (ejemplos de v0 o del mismo tipo) |
|---|---|---|
| **Método y medio** (P1) | Cualquier objeto, sustancia, lugar o verbo presentado como medio; cualquier frase que sitúe a Jean fuera del naust después de la última línea del cap-04; una médica o un atestado que precisen mecanismo; B1 con «hora/lugar estimados del acto». | cap-04 (barrer serrín; la bisagra que se atasca); cap-06: «En la zona de Koppangen» / «Esa información forma parte del atestado». |
| **Acto, escena, últimas horas, hallazgo** (P1) | Reconstrucción desde cualquier POV, incluida la primera persona del 38 («aquella tarde yo…»); quién la encontró, dónde exactamente, cómo; detalles del hallazgo del coche; «¿Sufrió?» respondido en cualquier sentido. | cap-19: datos administrativos (embarque, recibo, el gofre) sin continuación; cap-28: «Por ahí no». |
| **«Despedida»** (P2) | Abrirlo, citarlo, parafrasearlo, «imaginarlo» («seguro que decía…»); describir formato, fecha o tamaño; que alguien lo lea fuera de escena; cualquier nota, carta, audio, vídeo o mensaje de despedida nuevo de Jean a quien sea; un «quinto mensaje» del 26-nov. | cap-09 y cap-40 (el nombre; no abrir; restringir y conservar); Jessie: «Es lo mismo con mejor diseño». |
| **Explicación única del porqué** (P3) | En voz con autoridad: «Se mató porque…»; «El matrimonio la había…»; «Si la escalada hubiera llegado a un clínico…»; la profesional de N1 o la jueza ofreciendo causa; Maja «comprendiendo por fin». También la explicación negativa cerrada («no fue por Kongsbakken»). | cap-09: «yo tampoco puedo daros una sola causa»; cap-06: «No lo sé»; sospechas de personaje sin refrendo (Jessie: «mamá tenía enemigos»); un narrador que registra la pregunta y no la recoge. |
| **Romantización o moralización** (P4) | «Descansa», «por fin en paz», «se liberó», «fue coherente / valiente / lógico», «lo eligió» con connotación de dignidad, luz o música sobre el acto; el reverso («cobarde», «egoísta») en voz del narrador; presentar «Elijo quedarme» (38) como enmienda moral del acto. | Rabia de Jessie (cap-09); Alana: «Creí salvar algo de ella»; cap-38: «No es libertad» / «Mi cese dejaría intacto el poder del custodio». |
| **Duelo y apoyo** (P6) | Checklist de «señales que no visteis»; estadísticas de riesgo aplicadas a las hijas o a Maja; método de conversación instructivo; sesión que «cura», «cierra» o «perdona»; profesional que explica el acto o exculpa por completo; culpar a Maja o a Alana como causa. | cap-14: «cuatro noches sin reproducir la última discusión… El archivo seguía entero»; N1: la pregunta imposible tratada como pregunta. |
| **Menores** (P7) | Ideación o gesto autolesivo de Nora o Jessie; «Jessie pensó que entendía a su madre» en clave de acto; conducta de riesgo eficaz y sin coste; cuerpo mirado, sexualización; adultización simbólica. | cap-16 (Fyret: coste policial); cap-24 (coche: investigación, «Podías haber resultado herida»); cap-35 (a la mano de Maja); cap-26 (la ducha, vista desde fuera). |
| **Ambigüedades Ap. A §3** | «Sí, soy tu madre»; nombrar al ordenante; completar el segundo regalo; «Jessie calló porque…»; «Koppangen porque…». | «No toda»; «Dejo el hueco»; el auto que deja en blanco. |

## 5. Declaración sobre v0

**Veredicto: v0 CUMPLE la Carta en sus ocho puntos. Cero pasajes «corregir».** El manuscrito nunca nombra el método, jamás abre «Despedida», reparte la culpa sin sentenciarla, deja el porqué en plural y trata a las gemelas como adolescentes en duelo. Los pasajes siguientes «rozan» los puntos 1–7: son cumplimientos, y a la vez el mapa exacto de dónde una expansión puede romper lo que v0 hace bien.

| Cap:línea | Cita (abreviada) | Punto | Veredicto | Nota para la oleada |
|---|---|---|---|---|
| 01:45–47 | «Última sesión.» · eligió «fin de participación» y rechazó añadir una causa | P1/P3 | cumple (P) | Modelo del principio 3: la propia Jean no da causa. |
| 02:111–125 | «¿Has pensado que estarías mejor muerta o en hacerte daño?» … «Una o dos veces.» | P1 | cumple | Cribado clínico estándar, sin método. OT-02: la ancla interior no puede ser ideación, plan ni gesto de despedida. |
| 02:217; 09:37–59, 195; 40:133 | «Despedida»: el cursor encima, sin abrir; mirado y apagado; restringido y conservado | P2 | cumple (P) | Techo del archivo: nombre y no apertura (CH-11). |
| 03:207–217 | «No puedo… Da igual. Joder, Alana. Da igual.» | P3/P4 | cumple (P) | Derrumbe sin causa única. Ningún eco en N3 puede «traducirlo». |
| 04:99–121 | naust: «cuerdas rígidas», «rollo de cabo», «cuchillo del pescado» (recuerdo infantil) | P1 | cumple (P) | Objetos de trabajo, no preparación. PROHIBIDO ampliar o glosar el inventario del naust en 40, 41, N6. |
| 06:91–99 | «¿Ha sido ella?» … «Sé que ha muerto.» «Y sabes lo demás.» | P1 | cumple | La verdad entra por elipsis; patrón para N1. |
| 06:121–127 | «¿Por qué Koppangen?» «No lo sé.» «Habrá dicho algo.» «A mí no.» | P3 | cumple | Ambigüedad protegida; N1 la trata como incontestable. |
| 06:175–211 | «¿Dónde exactamente?» / «¿Sufrió?» «No podemos determinarlo…» / «equipo especializado en duelo por suicidio… No dejó ningún folleto» | P1/P6 | cumple | Preguntas sin respuesta en vF; derivación responsable: N1 nace aquí. |
| 06:245 | «Dieciséis llamadas salientes a Jean… poco antes de las once» | P3 | cumple | Culpa distribuida sin veredicto. B1 no infiere de aquí la hora del acto. |
| 09:69–77 | «¿Nos va a explicar por qué lo hizo?» «No. Y yo tampoco puedo daros una sola causa… No fue culpa vuestra.» | P3/P6 | cumple (P) | Texto de referencia para N1: la profesional no dice más que esto. |
| 09:73; 14:149 | «Nora había discutido con Jean por Kongsbakken.» · «Desde la cita de apoyo, Nora llevaba cuatro noches sin reproducir la última discusión… El archivo seguía entero.» | P3/P6 | cumple | Ancla de continuidad de N1: la discusión no se vuelve causa ni se «resuelve»; el efecto de la sesión es pequeño y reversible. |
| 09:131–143 | «Nos dejó… Como si hubiera perdido un puto autobús… Mamá se mató. Empecemos por ahí.» | P4 | cumple (P) | Rabia de personaje contra los eufemismos. El narrador nunca adopta ni «se fue» ni «se mató». |
| 11:85–111 | «No vengas.» … «No sabía qué habría cambiado una llamada.» | P3 | cumple (núcleo) | OT-11: las calas de Alana no convierten la no-llamada en causa ni en absolución. |
| 14:281; 24:211 | «Jean ya pagó tu forma de protegerla.» · «Y mamá tenía enemigos.» | P3 | cumple | Rabia y sospecha de personaje; el narrador no las refrenda ni deriva causa. |
| 19:25, 59; 28:79–87 | «un gofre que nadie encontró mordido» · «hasta que se acababa, en Koppangen» · «Por ahí no.» | P1 | cumple | Techo de lo que se sabe del trayecto. OT-19/OT-28: no ampliar. |
| 23:51 | «preguntas que empezaban con un “por qué”» — no formuladas | P3 | cumple (P) | Nora no pregunta el porqué; N1 respeta esa reserva. |
| 25:87–107 | «¿Sabías que podía morir…?» / «utilidad esperada superior…» / escalada interceptada | P3 | cumple (núcleo) | Coste sistémico, no causa suficiente. OT-25: prohibido «si la escalada hubiera llegado…». |
| 26:27 | la ducha; «una aspiración rota»; Maja incapaz de sentarse | P6/P7 | cumple | Hipervigilancia de superviviente sin instrucción: modelo. |
| 31:91–95 | «¿Quieres vivir?» «Quiero poder elegir. Es la primera vez.» | P4 | cumple (P) | No glosar como juicio retroactivo sobre el acto. |
| 33:77 | caldera 2059: «Prometió volver antes de acostarlas… Las tres habían esperado.» | P3 | cumple | Patrón para N3: deterioro conyugal por objeto, sin explicar nada. |
| 36:53–59 | «Contenerme también es encerrarme.» «Entonces ciérrame.» «No.» | P4 | cumple | OT-36/13/17: no orientar hacia deseo de morir; el paralelo con Jean no se enuncia. |
| 38:157–169 | muerte de Nieve: «NORNA no ofrece un apagado» … «Echo de menos hasta sus pausas.» | P4 | cumple (P) | Ni descanso ni liberación. |
| 38:175–189 | «Me queda decidir si NORNA destruirá también mi ejecución… Elijo quedarme.» | P4 | cumple (P) | La autodestrucción se rechaza sin sermón. Costuras: no convertirlo en enmienda moral del suicidio. |
| 38:181–183 | «una sesión anterior al amanecer… una respiración que tarda en acompasarse. Esa medida no reconstruye una escena…» | P1 | cumple (P) | Prohibido explicitar qué sesión y qué frase. |
| 40:101 | titular «NORNA DEVUELVE A LARSSON: LA MUERTE QUE HUNDIÓ ARMSTRONG», marcado como falso | P3/P4 | cumple | La prensa nunca añade causa ni método; N2/N6 heredan la regla. |
| 40:107–123 | turno de Jessie: silencio; el registro sin clasificación | P6 | cumple (núcleo) | CH-2: una sola línea; el silencio no se interpreta. |
| 12:59; 16:179–247; 24:147–199; 33–35 | cita con adulto anónimo (acompañada, en público); Fyret; el coche; el rellano | P7 | cumple | Riesgo con coste (policía, investigación, «a mi alcance»), nunca eficacia gratuita. N2 y las expansiones no añaden riesgos nuevos. |
| 41 caps. | retrato de Nora y Jessie | P7 | cumple | Cero sexualización, cero autolesión, cero adultización simbólica. |

**`00-aviso.md` (provisional): `APROBADO`.** Nombra el tema (suicidio y duelo), promete la elipsis —«El acto no se describe en ninguna página» convierte esta Carta en promesa al lector: violarla rompería también el aviso—, remite a los recursos, no anticipa trama, no romantiza; segunda persona sobria, coherente con el libro. Requisito: `compilar.sh` lo sitúa antes del cap. 1, en el compilado y en vF.

**`99-recursos.md` (provisional): `APROBADO CON OBSERVACIONES` (no bloqueantes).** (1) Números correctos según mi conocimiento (España: 024, Teléfono de la Esperanza 717 003 717, 112; Noruega: Mental Helse 116 123, Kirkens SOS 22 40 00 40, 113; findahelpline.com; befrienders.org); A5 verifica vigencia formal antes de vF (punto 5) y el autor valida. (2) Libro en español con lectores previsibles fuera de España: valorar dos o tres líneas hispanoamericanas (decisión de autor; findahelpline ya las cubre). (3) Tono correcto: «pide ayuda», sin sermón ni estadísticas; conservar la brevedad. (4) Va tras el cap. 41, sin cabecera de parte, y no comparte página con ninguna nota de autor.

## 6. Guía específica para los puntos de riesgo

### N1 «La primera cita» (POV Maja · 4-dic-2060 · sesión de apoyo)

Continuidad obligatoria: cap-06 (contacto del equipo especializado; «Que me llame. Iremos las tres»), cap-09 («Mañana tenemos la primera cita…»; Maja ya ha dicho que no hay una sola causa y que no fue culpa suya; Jessie: «Eso no hace que la perdone»), cap-14 (efecto: «cuatro noches sin reproducir la última discusión… El archivo seguía entero»).

**No puede aparecer:** causa (la profesional no explica, no propone hipótesis, no confirma ni descarta matrimonio, trabajo, Kongsbakken, Armstrong); método, lugar, atestado, «¿Sufrió?»; «Despedida» abierto o especulado (puede nombrarse como decisión pendiente, sin consejo de abrirlo ni de borrarlo); checklist de señales, «podríais haber», estadísticas de riesgo aplicadas a las gemelas o a Maja; fases del duelo, «superar», «cerrar», «sanar», «perdonar» como meta; milagro (nadie llora por primera vez y se alivia; Jessie no habla si no quiere y su silencio no se interpreta); culpabilización de Jean («fue egoísta») ni exculpación total en boca de la profesional (la rabia de Jessie contra Jean se dice y no se corrige); «ella os quería» como conclusión terapéutica; Maja verbalizando emociones (T3: su interior entra por objeto y decisión).

**Sí, y cómo:** la mecánica de la rabia como tema —la profesional la nombra como parte legítima, no como problema; «¿por qué Koppangen?»: si se pregunta, la respuesta es que la pregunta puede quedarse sin respuesta y que muchas familias la llevan años; nunca «no importa», nunca hipótesis («volvió a…»); el silencio de Jessie (siembra de 40) como hecho respetado: «no hace falta hablar hoy»; Nora pidiendo «datos»: la profesional da lo que sabe de las familias que sobreviven —que la pregunta no cierra, que la culpa se reparte sola y no es prueba, que se puede volver— y rehúsa cifras que sirvan de veredicto; el dato que Nora se lleva es pequeño (que ninguna discusión explica nada porque nada solo explica), pero `VETO` si se formula como «no fue por Kongsbakken». Sin folleto leído, sin fármacos, sin nombres de programas. El resultado se mide en cap-14, no dentro de N1. Dos pasadas de A7 (contenido y tono).

### N3 «Inventario» (POV Maja · casa de Tromsøya · la separación en UNA escena-recuerdo)

**Prohibido:** explicar el suicidio por el matrimonio o la separación (ni «Jean nunca se recuperó de…»); cualquier hallazgo que funcione como nota (cartas, cuadernos, audios, listas, borradores; «Despedida» solo como nombre y sin abrir); inventario de medicamentos, herramientas o cualquier objeto leíble como medio; la bolsa de viaje del cap-04 o los «efectos personales» de UNN (solo como trámite y con autorización previa de A7); el naust como lugar del acto; la última tarde o la última llamada como escena; diagnóstico psiquiátrico retrospectivo. **Sí:** la separación por logística y objeto (la caldera de 2059 en cap-33 es el patrón); la amistad Maja–Alana–Jean en pasado (sopa, metrónomo del cap-20) sin volverla explicación de la traición; síntomas de Jean, si aparecen, como en cap-02 (la bolsa de basura): vistos, no diagnosticados; el interior de Maja entra por lo que decide guardar. La escena puede acabar con una pregunta que nadie recoge, nunca con una respuesta. Dos pasadas.

### Cap. 40 «Sombra» (R, +150 · locutorios · CH-2)

Se permite «No preguntó por el cinturón.» (una línea, en el turno de Jessie visto desde el cristal). No se permite: interior de Jessie que explique su silencio; que Jean «hable» a Jessie; llanto o gesto que resuelva; que la prensa (titular ya presente, marcado como falso) añada causa, método o «Despedida»; entrevistas donde Nora «explique qué sintió»; ninguna apertura de «Despedida». La regla del capítulo es la funcionaria que «cerró el registro sin añadir una clasificación al hueco».

### Cap. 38 «Norna» (P núcleo · +100 solo costuras)

Intocables por hash: muerte de Nieve, respiración/huella, «Elijo quedarme», la primera persona. Para las costuras: nada de retrospectiva del acto en primera persona («aquella tarde», «cuando decidí»); no glosar «una sesión anterior al amanecer» ni «la frase definitiva»; no convertir «Elijo quedarme» en enmienda moral del suicidio ni NORNA en «suicidio del sistema»; la muerte de Nieve no se llama descanso ni liberación; «No es libertad» se mantiene. Cualquier costura que roce el acto: `VETO`.

### Notas breves para otras órdenes

- OT-02 (+100 ancla interior de Jean): doméstica; nunca ideación, plan ni gesto de despedida.
- N5 «Turno» y todo Jean-POV: no usar casos de moderación con contenido autolesivo o suicida de terceros; si un lote lo exige, solo la categoría, nunca contenido ni método.
- OT-19 y OT-28: nada nuevo sobre el trayecto de Jean. OT-25: la escalada interceptada es coste sistémico, no causa. OT-11: la no-llamada no es causa ni absolución.
- R2 «ventana reflexiva» (si se activa): tiempo sin tarea = memoria de las niñas y del piano; si toca el acto o el porqué, `VETO`.
- N2 y N6 (instituto, prensa, consulta): el estigma («la hija de la que…») solo con coste visible y sin método; titulares sin causa ni método; ninguna foto «del lugar».
- Materiales de trabajo: B1 no fija hora ni lugar del acto; B2 (Jean) no propone causa ni «perfil»; los resúmenes de lector frío de cap-04 escriben «el capítulo elide el acto» y no lo rellenan; los prompts a A3a/A3b citan esta Carta íntegra.

## 7. Dudas y decisiones que pido a A0 o al autor

1. Validar `00-aviso.md` y `99-recursos.md` (D4 de B0) y decidir sobre líneas hispanoamericanas.
2. Confirmar que A7 recibe B1, B2, B8 y los resúmenes de lector frío antes de G0/G1: la Carta lo exige y el plan no lo agenda.
3. cap-38:181–183, «una sesión anterior al amanecer»: leo la huella como registro de SPEIL de una madrugada, sin escena; si A1 fija otra lectura en B1/B3, que no pase de «huella de SPEIL sin escena». La ambigüedad es del texto.
4. Autorización previa de A7 —no solo revisión— para cualquier mención de la bolsa de viaje o de los «efectos personales» en N3 o en cualquier capítulo.

Firmado, A7 · 2026-08-16 · sobre `v0`.
