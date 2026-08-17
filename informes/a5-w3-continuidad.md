# A5 · Verificación de continuidad — Oleada W3 (seis capítulos nuevos)

_Verificador: A5 (claude-opus-4-8). Rama `w3-nuevos`. Fuentes: capítulos vecinos v0/W2 (lectura directa de líneas citadas), B1/B3/B4, frontmatter, `medir.sh w3 --baseline v0` (M7)._

## 0. M7 y monotonía de fechas (petición explícita de A0)

- `medir.sh w3 --baseline v0` → **M7 errores 0 · avisos 0**. `metricas-w3.json`: `errores: []`, `avisos: []`.
- Secuencia con los seis decimales intercalados, **monótona** (empates de fecha admitidos):
  7 (03-12) = **N5·7.5** (03-12) < 8 (04-12); 9 (03-12) < **N1·9.5** (04-12 T15:00) < 10 (05-12); 16 (15-12) < **N2·16.5** (16-12) = 17 (16-12); 22 (27-12) < **N3·22.5** (29-12) = 23 (29-12); 25 (03-01) = **N4·25.5** (03-01) = 26 (03-01); 40 < **N6·40.5** (11-05-2061) < 41.
- **Días de la semana** (todos correctos): N1 04-12 = sábado ✔; N2 16-12 = jueves ✔; N3 29-12 = miércoles ✔; N4 03-01 = lunes ✔; N6 11-05 = miércoles ✔ (paga 40:137 «El miércoles nos escuchan»). N3 interno «el martes siete» = 07-12 = martes ✔.
- **Horas del clímax** intactas (12:38 / 12:46:01 / 12:46:50 / 12:47 / 13:07 / 13:11). **Aritmética de cohorte** intacta: `cifras_cohorte` conserva 4.096, 4.095, 1.185, 2.911, 2.311, 597. **Ninguna cifra nueva de cohorte, AÑOS-JM ni tiempo** introducida por los seis capítulos.

## 1. N5 «Turno» (7.5 · Jean · 03-12) — checklist §7 + puntos de A0

| # | Comprobación | Resultado |
|---|---|---|
| a | Fecha sin hora; 7 → 7.5 → 8 monótono | ✔ |
| b | Todo opera ya en 5/7; no anticipa 8 (sin ventana 7C, procedencia, ráfaga, «modelo», decisión adherida) | ✔ |
| c | Precisión 99,6 % vs 7:21 «99,7 %. Mejora sostenida» | ✔ (ver nota) |
| d | Cuatro nombres del cierre = 7:33 | ✔ «Nora. Jessie. Maja. Alana.» idéntico y en el mismo orden |
| e | Vaso boca abajo compatible con 5:57 | ✔ 5:57 «sabe cuál deja los vasos junto al fregadero»; N5:205-207 lo concreta sin contradecir |
| f | Sin cohorte / «cuántas somos» (8:89) | ✔ |
| g | Cuatro personas de los casos no reaparecen ni abren subtrama | ✔ cada caso «cruza y no vuelve» |

**Nota c (menor, no bloqueante):** 99,7 % (7:21, antes del funeral) → 99,6 % (N5, después del funeral) es un descenso de una décima **deliberado y sin glosa** (arbitrado en OT-N5 §9.3). No es contradicción: en N5 el sistema **no** reitera «mejora sostenida»; el descenso es observación interior de Jean y es el latido temático (decide para la persona, no para la cifra). Registrar en B3/B4 como canon.

## 2. N1 «La primera cita» (9.5 · Maja · 04-12) — checklist §7

| # | Comprobación | Resultado |
|---|---|---|
| a | La profesional (Ranveig) = la que llamó el 27-nov (6:211-215), **no** la médica | ✔ «No llevo el tratamiento de nadie», «No sé por qué murió Jean»; distinta de la médica de zuecos |
| b | No contradice 9:65 «Mañana… Las tres» | ✔ 9 (03-12) «mañana» = 04-12 = N1 |
| c | No contradice `S14-cita` (14:149, «cuatro noches») | ✔ N1 no muestra remedio; 14 (11-12) mide el efecto siete días después |
| d | El cuaderno pautado no existe aún (aparece 05-12, 10:205) | ✔ N1 «No llevo nada donde apuntarlas»; Nora se queda sin dónde apuntar |
| e | Gemelas dieciséis; sin efectos personales (6:217) ni bolsa | ✔ |
| f | Periodicidad «cada quince días» (duda del escritor) | **ACEPTADA** |

**Sobre «cada quince días»:** no contradice ningún canon (no hay segunda cita datada en v0; el intervalo ~19-12 no choca con 14 ni con nada). **Se acepta.** Registrar como canon en B2 (ficha de la profesional).

## 3. N2 «Instituto» (16.5 · Nora/Jessie · 16-12) — checklist §7

| # | Comprobación | Resultado |
|---|---|---|
| a | La fotografía = 7:189-193 (ceremonia, ORIGEN·ASISTENTE), **no** la esquela (7:221-223) | ✔ objetos idénticos (flores/atril/programa/imagen caída/dedo); pie «visionaria detrás de SYNVEV» (2:203), sin fechas ni causa |
| b | Antecedente de Jessie con la agente = 16:201 (Fyret, día anterior) | ✔ «El día antes… a una agente» |
| c | La cuenta sigue suspendida al cerrar (sostiene 22:45) | ✔ N2 usa `Cuenta no disponible` (≠ `S10-suspendida`); revisión pendiente; no restituye |
| d | Aula 214, grupos 1STA/1STC, tutora sin nombre, no chocan con 18:21 ni 20:169 | ✔ 18:21 es Kongsbakken (conservatorio), instituto distinto; 20:169 sin Alana en escena |

## 4. N3 «Inventario» (22.5 · Maja · 29-12) — checklist §7

| # | Comprobación | Resultado |
|---|---|---|
| a | Salón = 23 (piano, tecla del mi «desde el otoño», metrónomo de nogal con esquina hundida, temporizador) | ✔ concuerda con 23:17 y 23:145 |
| b | Sesión de las ocho encaja con 23:15 (20:00) | ✔ «A las ocho venía Astrid Vik»; no «prepara» nada |
| c | Objetos de la casa = cap-04 (táper SOPA azul, taza reparada, tarjeta del técnico) | ✔ concuerda con 4:15-23 |
| d | Caldera = 4:23 / 33:77 **sin repetir** la escena de 33:77 | ✔ N3 solo «dos golpes / presión bien»; el reparto de 2059 (I-2) no toca la caldera |
| e | No anticipa la pluma de 39 | ✔ sin pluma |
| f | Canon nuevo (seis cajas martes 07-12; piso devuelto el 31 a las diez; caja F cerrada para Astrid) coherente con 11:101, 2:145, 16:255 | ✔ |
| g | **No** confundir las seis cajas con la caja de la huida de 26:17 | ✔ las seis se distribuyen/desmontan; la caja de 26:17 se llena en N4 desde el altillo |
| h | Fecha de llegada de las cajas vs 9:199 / 10:149 | **✘ ver hallazgo MAYOR-1** |

## 5. N4 «Interferencias» (25.5 · Nora→Maja→Jessie→Jean→Maja · 03-01) — checklist §7

| # | Comprobación | Resultado |
|---|---|---|
| a | Re-suspensión con palabras literales de 10:205/213 | ✔ registros idénticos: `La actividad reciente…` y `Su cuenta ha sido suspendida…` |
| b | Coche gris del 24 queda pagado (encargo «autorizado», resolución cerrada en falso) | ✔ |
| c | La caja que bajan del altillo = la de 26:17; mudanza motivada | ✔ enlaza con 26:15-17 (tercera bolsa en el maletero) |
| d | Única mecánica nueva = aviso de exposición reputacional | ✔ (M2 = 1 narrativo; sin términos nuevos de lexicón) |
| e | Espejo de Jean no contradice 13/21/30/36 ni da a Coro palanca/mando nuevos | ✔ 7 ramas «muy por debajo» de las ~600 (13:241, 30:67); atestación de origen (30:67); resta (13:249-263); cuenta escolar vacía (21:95); precedente 21:29; **Coro no habla**; no anticipa 30/32/36; no identifica a la familia (coherente con 31); «No toda» intacto |
| f | Calendario 2→3-ene; AK-7 sigue accesible (28/33/35/37) | ✔ dicho en réplica «AK-7 la sigues abriendo tú»; la marca solo alcanza medios |

## 6. N6 «Acta» (40.5 · Aslak · 11-05-2061) — checklist §7

| # | Comprobación | Resultado |
|---|---|---|
| a | El acta paga 26:121 («La asociación decidirá lo suyo») y 40:141 («esperamos el acta») | ✔ |
| b | Extractos de AK-7 llegan por la vía de 37:141 (órgano costero) | ✔ anexo técnico con sello del órgano costero |
| c | No anticipa nada de 41 (gofre, «en primavera», cepilladora, puerta del naust) | ✔ |
| d | Reserva de la bocana el **21 de enero** coherente con 26:191 y con el Soldagen | ✔ paga 26:191 literal; el 21-ene es el día del clímax y «reservada por operaciones» funciona como cobertura operativa: refuerza, no contradice |
| e | `S26-paso-uso` no se repite; se paga con frase nueva | ✔ «Eso no está en el sobre» / «Si entra aquí, esto se para» |
| f | Debate persona/activo sin editorial; sin causa/método | ✔ `PERSONA O ACTIVO`, `NO SOY UN MODELO` mostrados, no leídos |

## 7. Hallazgos

| Sev. | Cap:línea | Cita | Regla/fuente contradicha | Corrección mínima propuesta |
|---|---|---|---|---|
| **mayor** | cap-n3:19-21 | «Las trajo una empresa **el martes siete**… Llevaban **tres semanas** en el pasillo» | 10:149 (dom **05-12**) «las cajas que Maja quería revisar» ya están en la casa; OT-N3 §3 I-1 ancla esas cajas a 9:199/10:149, pero fija su llegada el **07-12** (dos días *después*) | Decisión de A0/A1: (i) si 10:149 = las cajas del piso, adelantar la llegada a ≤05-12 (p. ej. «el jueves dos») y ajustar «tres semanas» → «casi cuatro semanas»; **o** (ii) declarar que 10:149 son cajas domésticas distintas y registrar en B1 que las seis del piso llegan el 07-12 como conjunto propio (riesgo: lector atento que las asuma iguales) |
| menor | cap-n5:93 | «Precisión del lote: 99,6 %» | 7:21 «99,7 %. Mejora sostenida» | Ninguna (descenso deliberado; el sistema no reitera «sostenida»). Registrar 99,6 % como canon |
| menor | cap-n5:59 / cap-08 | «Regla: entre la entrada y el acuse no hay hueco…» | Coordinación B2-1 H6: «primera Regla: del libro en N5 **o** en 8 según decida el autor» | Sin acción de A5; anotar para decisión de autor/A1 (no es contradicción: reglas distintas sobre cosas distintas) |

Ninguna ambigüedad protegida (Ap. A §3) tocada; ningún span protegido pisado (`proteger.sh verificar` OK, 8 ficheros / 108 spans intactos en los seis borradores).

## 8. Canon nuevo a registrar (A1-mantenimiento, tras G-A2)

- **B1:** funeral 31 personas (N1) / 03-12; cita de apoyo 04-12, periodicidad **cada quince días**; instituto 16-12 (vuelta a clase); llegada de las seis cajas del piso (**pendiente de fijar la fecha: ver MAYOR-1**), piso devuelto 31-12 a las 10:00, correo redirigido desde 01-01; 3-ene con los cuatro hechos + sección de Jean; sesión del acta 11-05-2061.
- **B2:** ficha de la profesional del equipo de apoyo (Ranveig; institucional, no explica, no aconseja, no da cifras; «cada quince días»); instituto único, aula 214, grupos 1STA (Nora)/1STC (Jessie), tutora sin nombre; ficha Maja (medios del instituto retirados hasta aclaración, AK-7 intacto); Jessie (investigación abierta); miembros de la asociación (Marit Sarre, Jonas Seppola, Nils Seppola), funcionario sin nombre; test no-instrumental de Aslak → superado (N6+26).
- **B3:** N5 sin mecánica nueva (99,6 % de precisión; primera «Regla:» literal, coordinación con 8); N4 mecánica nueva = aviso de exposición reputacional por proceso; **ficha de Coro** con los tres rasgos que fija N4-I5 (actúa un subconjunto, no el agregado; la salida común es intersección/resta, no orden; la voz única depende de margen y sincronía; precedente 21:29).
- **B4:** CH-46 (cita) → PAGADO (N1); CH-47 (mundo escolar) → PAGADO (N2+10); CH-1/CH-27/CH-28 y coche gris → PAGADO (N4 + 32/36); hoja de efectos personales (6:217) → PAGADO como trámite (N3); CH-26 → PAGADO (N6+26); 20:115, 40:141, 26:121, 37:141 → pagados. CH-48 (discusión Kongsbakken) y ordenante del sabotaje (24:79, 39:103) siguen SIN-PAGO-INTENCIONAL.

## 9. Veredicto

**PASA CON MENORES** — condicionado a que A0/A1 resuelvan el hallazgo **MAYOR-1** (fecha de llegada de las cajas del piso en N3 vs 10:149). Sin él, el resto de la oleada es limpio: M7 = 0, monotonía intacta, sin contradicciones de canon, sistema, derecho ni plausibilidad técnica; spans y ambigüedades protegidas respetados.

---

## Arbitraje de A0 sobre el ✘ de N3 (2026-08-17)

**Decisión: no hay contradicción. `capitulos/cap-n3.md` no se modifica.** Se adopta la opción (ii) de A5: son dos conjuntos de cajas distintos.

- **Las de 10:149** (dom 5-dic) están «en el hueco entre el escritorio y las cajas que Maja quería revisar», es decir, **en un dormitorio**. Su origen está en 9:199, la noche anterior: «Mientras Maja **buscaba** cajas». Maja está reuniendo cajas —vacías o domésticas— para ordenar, y quiere revisarlas. En ningún momento el texto las llama cajas del piso.
- **Las seis de N3** llegan el **martes 7-dic** en un transporte, al recibidor, y se quedan en el pasillo contra el radiador. Cada una lleva pegada una etiqueta con el número del piso y una letra, y N3 las nombra desde su primera línea como «las seis cajas **del piso** de Jean». El piso sigue existiendo y sin vaciar en 11:101, donde Alana llama al telefonillo y no contesta nadie.
- La aritmética cuadra: del 7 al 29 de diciembre son tres semanas y un día — «Llevaban tres semanas en el pasillo».

**Encargo para A1-mantenimiento (tras G-A2):** registrar en B1 los dos conjuntos por separado, para que la distinción quede fijada como canon y ninguna oleada posterior los confunda: (a) cajas domésticas reunidas por Maja el 4-dic y pendientes de revisar el 5-dic (9:199, 10:149); (b) seis cajas del piso de Jean entregadas por transporte el 7-dic, decididas el 29-dic y con el piso devuelto el 31-dic a las diez (N3).
