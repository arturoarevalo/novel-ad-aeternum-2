# B6-LN · Lista negra de clichés y marcas de «otro autor»

**Función:** que A3a/A3b/A4 comprueben mecánicamente que la prosa nueva no introduce lo que v0 evita ni «canta» a IA o a otro autor. Complementa `b6-huella-estilistica.md` (§6, §7).
**Fuentes:** B6; lectura íntegra de caps. 1, 3, 4, 6, 9, 13, 20, 23, 30, 37, 38, 41; cada entrada verificada con GNU `grep -E -i` sobre el cuerpo de los 41 capítulos (sin frontmatter), separando **narr** (líneas sin raya ni registro) y **diál** (con raya). Cifra = líneas de v0 con la marca; 0 = marca de otro autor confirmada; > 0 = se documenta y se decide.
**Fichero máquina:** `biblia/b6-lista-negra-patrones.txt` (§5): bloque A1 = 21 patrones (prohibidas, narración), A2 = 11 (cupo, narración), B = 13 (vigilar, diálogo). Cada familia cita su patrón (p. ej. A1-8); las entradas completas están allí. **Sensibilidad:** §3 → B7.
**Lectura:** «prohibida» = todo hit nuevo se corrige (los de v0 en spans protegidos se conservan); «cupo» = v0 la usa con función: se cuenta contra B6 §7; «vigilar» = se lee en contexto.

## 1. Lista negra léxica

| Familia (patrón) | Entradas (resumen) | v0 narr / diál | Veredicto y excepciones |
|---|---|---|---|
| Adverbios -mente (A1-1) | cualquier `-mente`, incl. realmente, profundamente, totalmente, literalmente | 7 / 9 (05:31, 25:85, 37:15, 38:175, 38:203, 39:79, 40:133) | Prohibido en narración nueva; banda ≤ 0,25/1.000. Diálogo: solo Nora («exactamente» 06:103, 06:179) y Astrid; nunca en acotación. |
| Intensificadores (A1-2) | muy · bastante · tan…que | muy 1 / 4 (28:129 «por muy poco»); bastante 2 / 3 | «muy» prohibido; «bastante» no añadir; «demasiado» (28 líneas) es huella de v0, ≤ 1/1.000. |
| Conectores (A1-3, A1-4, A1-5) | sin embargo · no obstante · si bien · a pesar de · de repente · de pronto · mientras tanto · y entonces · en ese momento · además · en definitiva · en última instancia · a fin de cuentas · en resumen · en el fondo · cabe destacar · es importante · no solo… sino · sin duda · por supuesto · es decir · o sea · de alguna manera · en realidad · la verdad es que · puesto que · ya que · debido a · por (lo) tanto… (44 locuciones) | 0 salvo «mientras tanto» 1 (15:145, registro jurídico) y «en ese momento» 1 (35:151); diál: «por supuesto» 2, «es decir» 1 | Prohibidas. v0 conecta con punto y seguido, «pero», «aun así» (03:87), «de modo que» (32:29). |
| Léxico ornamental y de IA (A1-6) | tapiz · resonar · testimonio de · recordatorio de · un viaje · navegar · sumergirse · adentrarse · desentrañar · tejer · crucial · fundamental · vital · innegable · palpable · tangible · inexorable · una suerte/especie de · un sinfín/abanico/cúmulo de · una oleada de · un torbellino · un mar/manto/rayo de · un atisbo/asomo/deje/matiz/tinte de · teñido/impregnado/cargado de + abstracto · el peso de + abstracto · el eco de · la certeza/sensación de · el vacío · el abismo · las entrañas · el alma · el corazón · el/la cual · un cierto · todo el mundo · para siempre · nunca más · nosotros/nuestro (narrador) | 0 (2 FP: «nosotras» en mensajes de Coro 32:63, 32:207; «el peso» solo físico 09:17, 33:205) | Prohibidas: ninguna en 63.000 palabras. |
| Sentimiento (A1-7, A1-8) | sintió · sentía · sentir(se) · sentimiento · emoción · podía sentir · notó cómo · algo en su interior · por dentro · había algo en · nombres: tristeza, miedo, angustia, pena, rabia, vergüenza, terror, soledad, esperanza, ternura, cariño, amor, odio, furia, felicidad, inquietud, incertidumbre, frustración, impotencia, gratitud, orgullo, compasión, lástima, el/su dolor… (40) | sentir 0 / 0; nombres 4 / 4 («miedo» 37:43; «furia» 38:111 núcleo; «gratitud» 02:39 y 11:235, citas de documento) | Prohibido nombrar la emoción; en diálogo la rabia dice lo que quiera (14:141; 18:207 «sin rabia»). «dolor» solo físico (15:37). «alivio» y «culpa» los vigila B7. |
| Adjetivos valorativos (A1-9) | hermoso · bello · precioso · terrible · horrible · desgarrador · doloroso · triste · feliz · melancólico · solitario · sombrío · sereno · tranquilo · nervioso · angustiado · desesperado · asustado · aliviado · agradecido · avergonzado · orgulloso · extraño · raro · inmenso · enorme · intenso · increíble · cruel · injusto · frágil · vulnerable · implacable · conmovedor · perfecto · absurdo · insoportable · ridículo… (49) | 4 / 8 (03:353 ridículas, 05:97 perfecta —irónico—, 09:59 insoportable, 20:299 absurdo; todos en P) + «asustada» citada 03:85 | Prohibidos: 0 nuevos. Físicos/técnicos pospuestos permitidos: «postura imposible» 07:217, «cruce incómodo» 37:47, «humo amargo» 09:93, vacío, frío, oscuro. |
| Adjetivo antepuesto (A1-10) | la fría luz · el largo pasillo · una tenue/suave/dulce/pálida/oscura/vieja/pesada/húmeda/eterna… + sustantivo | 0 / 0 (v0 antepone solo ordinales, mismo, único, propio; «el frío», «el blanco», «el gris» son sustantivos) | Prohibido. |
| Cuerpo-cliché (A1-11) | una punzada · un nudo en la garganta/el estómago · se le encogió · un vuelco · escalofrío · se le heló · se estremeció · un pinchazo · el corazón le latía · se le aceleró · martilleaba · piel de gallina · sabor amargo · el estómago · las tripas · la garganta · en el pecho | 0 / 0 («dos latidos» 33:227 mide tiempo → cupo A2-7; «pulso» técnico) | Prohibido. |
| Gestos-cliché (A1-12) | respiró hondo · tragó saliva · contuvo el aliento · exhaló · suspiró · un suspiro · dejó escapar · apretó los puños/la mandíbula/los dientes · se mordió el labio · frunció el ceño · arqueó una ceja · entrecerró los ojos · se encogió de hombros · negó con la cabeza · asintió · se pasó la mano por el pelo · se frotó · se aclaró la garganta · carraspeó · cerró los ojos · gimió · sollozó · lloró · abrazó · besó · hizo una pausa · no dijo nada · sin decir nada · se quedó sin palabras · no supo qué | 3 / 0 («sollozaba» 09:33 una desconocida; «no dijo nada» 04:105 P; «carraspeo» 23:87 es sustantivo, excluido) | Prohibidos («asintió», «negó con la cabeza», «cerró los ojos»: 0 en todo v0). Lo que v0 usa (cupo A2-7, ≤ 1 por capítulo nuevo cada uno): «soltó aire por la nariz» 03:131, 23:279; «tomó aire» 09:15; «Abrió la boca y la cerró» 03:293; «hizo una mueca» 03:155; «Casi sonrió» 03:103. Lágrimas (A2-4): 3 en v0; 0 en N1, N3, 6, 14. |
| Ojos, voz, sonrisa (A1-13) | los ojos brillaban/se le llenaron/húmedos · la mirada perdida/vacía/ausente/clavada · miraba sin ver/al vacío/por la ventana · esbozó · dibujó una sonrisa · una sonrisa triste/amarga/leve/cansada · sonrió con/sin · se le quebró la voz · un hilo de voz · con voz + adj. · voz temblorosa/quebrada/ronca/firme/suave · en un susurro · entre dientes | 0 / 0 («voz neutra» 05:71, 34:165 describe una máquina, excluida) | Prohibido. v0: «sostuvo su mirada» 34:195, «La sonrisa perdió un lado» 37:45. |
| Cuerpo que se escapa (A1-14) | el cuerpo le/se · se le escapó un sollozo/una risa · sin poder evitarlo · no pudo evitar · no pudo sino · no pudo contener · no consiguió reprimir | 0 / 0 | Prohibido. v0: «El cuerpo eligió otra secuencia.» 03:203. |
| Silencio y tiempo (A1-15) | el silencio se hizo · se hizo un silencio · un silencio pesado/incómodo/denso/largo · hubo un silencio · el tiempo se detuvo · una eternidad · un largo/buen rato · poco a poco · más y más · el aire se volvió · en el aire · quedó flotando · como si nada · como si el tiempo/el mundo · como si fuera la primera vez · como siempre · como cada día | 0 / 0 (cupo A2-7: «Hubo una pausa» 23:99; «durante un instante» ×5; «cada vez más largos» 33:95, literal) | Prohibido. v0 mide: «midió el silencio en un compás de cuatro pulsos» 09:15; «Durante una asignación completa nadie habla.» 30:147; «Nadie habló.» 03:245. |
| Cognición y sumario (A1-16) | se dio cuenta · comprendió/supo/entendió que · cayó en la cuenta · recordó cuando/aquel/la vez · en aquel entonces · en aquella época · hacía años · tiempo atrás · nunca volvería · no volvería a · más tarde recordaría · no lo sabía entonces · fue la última vez que · nada volvería a ser · algo había cambiado · años después · con el tiempo · no era la primera vez · sin saber por qué · aunque no lo dijera | 1 / 0 («sin saber por qué» 13:211, Jean) | Prohibido. Cupo A2-11: «años atrás» (07:203, 20:115), «de niña(s)» (04:105, 20:251), «por primera vez» (12); A2-5 «pensó»/«hizo pensar» (03:203, 03:131). |
| Glosa, regla, cursiva, diminutivo (A1-17…20) | «y en esa frase cabía…», «cabía toda su…» · `Regla:` · monólogo en cursiva (`*…*` ≥ 15 caracteres) · diminutivos (poquito, ratito, casita, jarrita, lucecitas…) | 0 · 0 · 2 FP (18:131 rótulo, 41:15 fecha) · 2 / 2 («jarrita» 03:39, 03:69 P; «paquetito» 14:229, «lucecitas» 35:183, Jessie) | Glosa prohibida. `Regla:` solo en 8 y N5, una vez (D5; v0 enuncia por sentencia: 05:43, 07:127). Cursiva solo énfasis de lectura ≤ 2 palabras y rótulos. Diminutivos: prohibidos en narración; Jessie ≤ 1/escena, irónico. |
| Narrador que pregunta o exclama (A1-21) | `?` / `!` en línea sin raya | 2 / — (06:211 «¿Sufrió?» citada; 12:29 `¿Quién eres?` escrito y borrado); `!` 0 (la única del libro: Nora 06:297) | Prohibido. La pregunta la hace un personaje y nadie la contesta (06:121–127). |
| Dicendi y acotación (B-1…4) | susurró · musitó · espetó · exclamó · bramó · gritó · masculló · balbuceó · inquirió · replicó · repuso · sentenció · murmuró · gruñó · siseó · protestó · rogó · suplicó · confesó · admitió · reconoció · comentó · observó · afirmó · negó · explicó · declaró · intervino · prosiguió · interrumpió · soltó · insistió · advirtió · jadeó · titubeó… (70) · dicendi + adverbio · «dijo con voz/tono/tristeza/una sonrisa» | 2 («—No —murmuró.» 09:29 P; «—repuso él» 18:31); adverbio 0; «con + manera» 0 («sin bajar el paso» 12:255 y «con la cadencia compartida» 37:77 son físicas) | Prohibidos. Permitidos: dijo, dice, preguntó, respondió, contestó, añadió, repitió, pidió, leyó, corrigió, empezó (B6 §4.1); complemento solo físico o temporal («al fin» 03:75, «en voz baja» 09:171). |
| Vigilar en diálogo (B-5…13) | explícamelo · ¿y eso qué significa? · sigla + paréntesis · `—¿Qué es un…?` · -mente · muy/súper/en plan/tío · vulgarismos · réplica ≥ 40 palabras · diminutivos · consuelo-cliché («todo va a salir bien», «estoy aquí») | 20:53 (Jessie: confrontación) · vulgarismos 12 · ≥ 40 palabras 7 (Astrid, Alana, Mats, Coro) · «estoy aquí» 05:113 | Vulgarismos ≤ 1/escena, solo Jessie; `-mente`/«muy» solo Nora, Astrid, Alana; consuelo-cliché → §3. |

## 2. Lista negra sintáctica y de recurso

| Recurso | Regla para prosa nueva | Detección | v0 |
|---|---|---|---|
| Preguntas retóricas y exclamaciones del narrador | 0 | A1-21 | 0 (2 citas) |
| Monólogo interior en cursiva; «pensó: …» | 0; el pensamiento entra como frase narrativa seca (03:203 «Pensó que debía dejarla. Beber. Decir algo seco.») | A1-19; A2-5 | 1 «pensó» |
| Tríada rítmica con clímax; anáfora triple | 0. v0 usa tríadas de inventario (06:105 «Localización. Traslado. Fallecimiento.») y anáfora doble como máximo (30:157–159 «Nadie…») | lectura de A4 | — |
| Metáfora explicativa; símil ornamental | metáfora 0; «como si» ≤ 1 por capítulo nuevo y solo de calibración (03:15, 23:55, 25:85); «como un/una» solo pragmático | A2-1, A2-2 | 12 / 11 |
| Párrafo de una palabra como efecto barato | ≤ 1 golpe (≤ 3 palabras) por escena; nunca dos seguidos fuera de una cuenta atrás | awk (c) | 3 pares: 07:223, 09:271, 20:279 |
| Cierre de escena sobre objeto añadido (M4) | ≤ 1 por capítulo nuevo; 0 en N4 y N6; 0 nuevos en expansiones; lista blanca B6 §5.5 intocable; cierre-acuse en Jean ≤ 5 en vF | awk (d) + B6 §5 | 32 |
| «Regla: …» fuera de excepciones | solo 8 y N5, una vez (D5) | A1-18 | 0 |
| Glosa tras diálogo | 0 | A1-17, B-4 | 0 |
| Resumen emocional o moraleja al final de escena | 0; se cierra sobre réplica, registro o gesto con decisión (09:269–271; 41:81; 23:313) | A1-16 + lectura | 0 |
| Flashback en pluscuamperfecto largo; «recordó cuando…» | recuerdo ≤ 40–60 palabras con objeto (03:131, 33:77); ≥ 4 pluscuamperfectos en un párrafo = devolver | A1-16; A2-10 | 1 (04:105 P) |
| Personajes que explican al lector; sigla + paréntesis | 0. La pregunta puede hacerse; la respuesta no glosa (06:281–289 «¿Qué ventana?» «Es un término clínico.») | B-5, B-7 | 1 (20:53) / 0 |
| Diálogo socrático entre continuidades («—¿Qué es una ventana?» «—Una ventana es…») | 0; las continuidades disputan, no se instruyen (13:169–183) | B-6 + lectura | 0 |
| Frase > 45 palabras; párrafo > 90; réplicas > 25 encadenadas; réplica ≥ 40 | frase larga solo cuerpo o paisaje descompuesto y seguida de golpe (B6 §2.2); párrafo ≤ 90; encadenadas 0; ≥ 40 solo Astrid/Alana/Mats/Coro | awk (e, f, g); B-11 | 0 / 1 (26:185) / 0 / 7 |
| «ella/él» sujeto; punto y coma | nombre propio como sujeto; «;» ≤ 1 por capítulo nuevo | A2-8, A2-9 | 14 / 15 |
| Paisaje sin objeto en uso; personaje por biografía; narrador que glosa mecánica o sigla | 0 (B6 §6) | lectura de A4; M1/M2 | — |

## 3. Sensibilidad (remite a B7)

Términos, spans prohibidos y disparadores: `biblia/b7-carta-sensibilidad.md` §3–4 y `b7-patrones-A.txt` / `b7-patrones-B.txt`; el fichero de A4 no los duplica y A8 los pasa por separado. A4 **marca en la OT para A7, sin reescribir**: eufemismos o veredictos en voz con autoridad («se fue», «nos dejó», «descansa», «fue coherente/valiente/cobarde»); cualquier causa única del acto, aunque sea negativa; método, lugar, hallazgo, últimas horas, ampliación del inventario del naust (cap. 4) o del trayecto; «Despedida» abierto, citado o imaginado; léxico de milagro terapéutico («superar», «cerrar», «sanar», «pasar página»); consuelo-cliché en boca de adulto o profesional («todo va a salir bien», «estoy aquí» —23:185 lo nombra como frase fabricada—); adultización, sexualización o riesgo eficaz en las gemelas. Estas marcas no son corrección de estilo: la decisión es de A7 (veto).

## 4. Sustituciones recomendadas (cómo lo hace v0)

| Cliché | Sustitución de v0 | Citas |
|---|---|---|
| Emoción nombrada | objeto que se resiste o gesto sobre objeto | 06:71 (la botella rebosa; dos cargadores) · 20:141–145 (mano cerrada → «Abrió la mano.») |
| «Sintió que», interior explicado | el cuerpo percibido desde fuera; la lista de lo olvidado | 03:215 «Estaba de pie. No recordaba haberse levantado.» · 06:237 «Había conducido hasta el hospital sin teléfono.» |
| Adverbio de manera | el gesto repetido o el verbo exacto | 06:89 «Sus dedos repitieron el nudo dos veces porque el primero había quedado mal.» · 04:25 «Volvió a sacarlo para doblarlo mejor.» |
| Explicación del narrador | dato en boca de quien lo sabe, ≤ 15 palabras, con objeto delante | 23:63 Astrid: «Ha separado lo que recibió de lo que no puede ver.» · 20:27 Alana: «Una forma de preguntar si Jean puede oíros.» |
| Mecánica glosada | asidero de registro y lo que el registro no dice | 13:65–67 (`COHORTE INICIAL JM-L · 0000–4095` / «No dice cuántos siguen activos.») · 19:143 `979,7 AÑOS-JM` |
| Énfasis por adjetivo o exclamación | frase corta tras la larga | 09:153 → 09:155 «—Dilo —repitió Jessie.» · 20:143 → 20:145 |
| Dicendi expresivo | gesto en párrafo aparte + réplica sin acotación | 06:35–41 · 14:137–141 |
| Pregunta retórica | la pregunta la hace un personaje y nadie la contesta | 06:121–127 · 06:191 «¿Sufrió?» |
| Resumen emocional, moraleja | cierre sobre registro, réplica o gesto con decisión | 09:269–271 · 41:75–81 «Cronometrar el sol.» «Para que conste.» |
| Flashback largo | recuerdo ≤ 40–60 palabras ligado a un objeto en escena | 03:131 (el gorro amarillo) · 33:77 (la caldera de 2059) |
| Símil ornamental | comparación de calibración o de oficio | 03:15 «con la limpieza falsa de una pantalla recién calibrada» · 23:55 |
| Silencio dramatizado | el silencio medido o contado | 09:15 (cuatro pulsos) · 30:147 |
| Diálogo socrático | la pregunta técnica recibe evasiva o dato, nunca glosa | 06:281–289 · 20:49–55 |
| Personaje por biografía | objetos en uso y una acción | 04:99–103 (la caja de anzuelos de Ingrid) · 26:25 (VHF, almanaque de mareas) |
| Cierre sobre objeto añadido | cierre sobre réplica o registro | 21:153 «Ser inevitables.» · 29:215 «Las necesarias.» |

## 5. Checklist mecánica (A8; A3/A4 antes de entregar)

Fichero `biblia/b6-lista-negra-patrones.txt`: una regex ERE por línea, comentarios `#`, bloques `A1` / `A2` / `B`. GNU grep (`/usr/bin/grep`; el `grep` de la sesión de Claude es ugrep), siempre `-E -i`.

```
F=biblia/b6-lista-negra-patrones.txt; C=capitulos/cap-NN.md
FM=$(grep -n -m2 '^---$' $C | tail -1 | cut -d: -f1)   # fin del frontmatter
# A1 y A2 sobre narración (sin raya, sin registros, sin frontmatter); cambiar A1→A2 para el cupo:
awk '/^# === A1/{f=1;next} /^# === A2/{f=0} f && !/^#/' $F | grep -E -i -n -f - $C | grep -v -E '^[0-9]+:(—|`|\*\*|>)' | awk -F: -v b=$FM '$1>b'
# B sobre diálogo:
awk '/^# === B/{f=1;next} f && !/^#/' $F | grep -E -i -n -f - $C | grep -E '^[0-9]+:—'
# recuento rápido, todo el fichero:  grep -v '^#' $F | grep -E -i -c -f - $C
# (c) dos golpes seguidos (≤ 3 palabras) fuera de cuenta atrás:
awk 'c<2{if($0=="---")c++;next} NF==0{next} {if(NF<=3&&prev<=3&&prev>0&&$0!~/^[—`*>]/&&pl!~/^[—`*>]/)print NR": "pl" / "$0; prev=NF; pl=$0}' $C
# (d) candidatos a cierre-objeto (última línea de cada escena) → cotejar con B6 §5.5:
awk '/^\* \* \*$/{print ln": "last;next} NF{last=$0;ln=NR} END{print ln": "last}' $C | grep -E -i '(sigui[óo]|segu[íi]a|qued[óo]|permanec|volvi[óo] a|una (sola )?vez|otra vez|una vez m[áa]s|sigue|queda|inm[óo]vil|quiet[oa]|cerr[óo]|dej[óo]|guard[óo]|apag[óo]|baj[óo])'
# (e) párrafos > 90 palabras · (f) frases > 45 · (g) réplicas > 25 palabras encadenadas:
awk 'NF>90{print NR": "NF}' $C
awk 'c<2{if($0=="---")c++;next}1' $C | awk 'BEGIN{RS="[.!?…»]+[ \n]+"} NF>45{gsub(/\n/," ");print NF": "substr($0,1,80)}'
awk '/^—/{n=NF;if(n>25&&p>25)print NR;p=n;next} NF{p=0}' $C
```

**Lectura:** A1 → esperado **0** en prosa nueva; cada hit se corrige o se justifica en la OT (span protegido). A2 → contra la banda de B6 §7 (capítulo nuevo: «como si» ≤ 1, «;» ≤ 1, lágrimas 0 en N1/N3, «ella/él» sujeto < 1 %). B → en contexto: vulgarismos ≤ 1 por escena y solo Jessie; `-mente` y «muy» solo Nora/Astrid/Alana; réplicas ≥ 40 palabras solo Astrid/Alana/Mats/Coro; `—¿Qué es un…?` y «explícamelo» = sospecha de diálogo socrático.

**Falsos positivos sobre v0 (verificado).** Comando literal `grep -E -c -f $F` (sin `-i`, comentarios incluidos): cap-01 = 1 · cap-06 = 6 · cap-13 = 3 · cap-23 = 9 · cap-37 = 9 líneas: nada masivo. Por bloques, narración/diálogo separados: cap-01 A1 0 · A2 1 · B 0; cap-06 A1 1 (06:211 «¿Sufrió?» citada) · A2 2 · B 2 («exactamente», Nora); cap-13 A1 1 (13:211) · A2 1 · B 0; cap-23 A1 0 · A2 5 · B 1 («puta», Jessie 23:21); cap-37 A1 2 (37:15 exactamente, 37:43 miedo) · A2 8 · B 0. Sobre los 41 capítulos: **A1 = 30 líneas**, todas catalogadas en §1 (7 -mente, 5 valorativos, 2 «jarrita», 4 nombres de emoción, 2 mensajes de Coro, 2 cursivas, y 04:105, 06:211, 09:33, 12:29, 13:211, 15:145, 28:129, 35:151); **A2 = 95**; **B = 38**. Un capítulo nuevo o expandido con hits A1 no justificados vuelve a A3.

## 6. Dudas para A0

1. «demasiado» (28 líneas), «soltó aire por la nariz» y «durante un instante» son tics de v0 que la imitación tenderá a multiplicar: propongo cupo explícito (≤ 1 por capítulo nuevo cada uno) en la próxima revisión de B6 §7.
2. Los patrones de consuelo («estoy aquí», «todo va a salir bien») quedan en B (vigilar), no en A1: son legítimos en boca de personaje y su riesgo es de sensibilidad (§3). Decidir si pasan al barrido de A7.
3. Los cierres-objeto los detecta mejor el heurístico de `medir.sh` que el awk (d), que es solo filtro previo; confirmar que M4 adopta el censo ampliado de B6 §8.1 antes de W2.
4. Con `-i`, GNU grep no neutraliza acentos: los patrones llevan alternativas `[óo]`; si `medir.sh` corre en una locale no UTF-8, `\b` y `[[:alpha:]]` fallan sobre tildes.
