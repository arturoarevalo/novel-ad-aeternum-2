# A5 · Verificación de continuidad — oleada W4-R (poda de ritmo)

Rama `w4r-ritmo`. Diff `9997a8c..HEAD`. Método: por cada línea eliminada, ¿algún capítulo la cita, supone o cobra? Cruce con B4 (CH-9, 14, 18, 23, 26, 33, 38, 49, 50, 51, 53, 59, 62, 66, 67, 68, 73, 78, 79, 80), B1 (17 horas del clímax, cadena 34→41) y B3.

## Veredicto: PASA CON MENORES

No se ha encontrado ningún **pago sin siembra bloqueante**. El único tipo de fallo de ese patrón (canal de audio de Nora) ya estaba resuelto por A0 y queda **confirmado intacto**: la siembra sobrevive en `34:165` («una entrada asignada al canal del homenaje. No abría controles») y `34:277` («abrió la ruta de audio prevista en el guion»), que cubren los pagos `37:17` y `37:29`. La quinta enunciación (antiguo 34:293, «La de Nora conservó la entrada de audio…») queda cortada sin dejar pago colgando: dos siembras bastan para los dos pagos.

## Verificaciones duras solicitadas

- **17 horas del clímax de cap-34, presentes y en orden:** 08:51 (15), 09:00 (41), 09:42 (133), 10:27 (141), 11:40 (199), 11:44 (211), 12:00 (221), 12:04 (223), 12:23 INC-441 (261), 12:30 (291), 12:37:59 (297), 12:38 (299), 12:46 (303), 12:46:50 (307). **OK.** Aritmética intacta: `4.096 − 2.911 = 1.185` (85-89), `2.401,6 AÑOS-JM` (97), `INC-441` + «cobertura hasta las 12:47» (261). **OK.**
- **Desplazamiento de «A las doce, la retransmisión mundial quedó abierta»:** pasó de cerrar la escena de Alana (antes del dinkus) a abrir la de Astrid (221, tras el dinkus). Sigue entre 11:44 (211) y 12:04 (223); **no cruza ninguna otra hora**. Cronología correcta. **OK.**
- **cap-38 aritmética/identificadores (73-79):** `2.911` = `2.311` + `597` + `3`, con Cuchillo/Madre/Nieve bajo `/0188`,`/0007`,`/0311`. Intacta y **no tocada** por la poda. Las dos frases cortadas del 38 (retirada del destino bajo /0188; espera de Madre en /0007) eran redundantes: el mapeo `/0188`=Cuchillo, `/0007`=Madre, `/0311`=Nieve sigue anclado en 38:77 y en 13/15/17/36/34:111. **OK, sin ancla perdida.**
- **cap-39 cadena de la cautelar:** orden jurídico completo y correcto tras bajar de tres menciones a una — `midlertidig forføyning` + `rekonstruksjonsforhandling` solicitadas el 25 (18), `kjennelse` del 28 «eficaz desde la solicitud del día 25» que «mantuvo la midlertidig forføyning sobre NIDHOGG» (150), `depósito judicial` el 2-feb (192). **OK.** Depósito y facultades: caja controlada (suministro/frío/repuestos/personal), reconstructor controla la caja, NIDHOGG fuera de la custodia de Maja, sin propiedad/representación/control técnico. **OK** (ver menores M-2 y M-3).
- **cap-n3 inventario:** cajas A–F todas presentes (55, 63, 91, 319, 323, 327, 329); SOPA (95, 291), tazas (65, 87), hervidor (67-71, 475), jersey azul de la **caja C** (319, 409, 471), hoja de efectos personales/bolsa/altillo (335-337), reparto de 2059 CH-30 (71). El **metrónomo** (CH-8) no estaba en las líneas podadas (vive en el salón, 23:145); se cortó el diapasón/cuadernos del cajón del banco, ninguno con deuda. **OK.**
- **cap-n6 salto tienda→refugio (dinkus):** el párrafo cortado era la carretera (descripción, **sin dato de tiempo**); la escena es el mismo viaje (ferry de las cuatro → tienda → refugio). «Las selladas llegarían en diez días» cuenta desde el depósito del acta en el cajón (presente de la escena), autoconténido. Cajera y dos réplicas restituidas presentes. **OK.**
- **cap-40 tramo seco / span protegido:** confirmo coherencia; la decisión de A0 de no abrir `S40-locutorio` no genera incoherencia (la silla atornillada 40:15 y la tarjeta plastificada siguen sembrando CH-29). No se propone abrir el span. **OK.** (No ejecuté M7: `medir.sh` no verificado en esta pasada; el cómputo de 272 palabras queda a M7.)

## Tabla de hallazgos

| # | Sev. | Cap:línea | Cita / hecho | Regla o fuente | Corrección mínima |
|---|---|---|---|---|---|
| M-1 | menor | cap-40 (antes 145-163) | Se cortó «y dejó caer serrín húmedo sobre las botas»; **serrín ya no aparece en cap-40** | B4 CH-53 lista «40:145-163 … serrín húmedo» como reaparición del motivo | Ningún pago cuelga: el pago del naust en cap-41 es «la puerta rozaba… la cuña» (41:41), no el serrín. Opción A: restituir «y dejó caer serrín húmedo». Opción B: actualizar B4 CH-53 (quitar «serrín húmedo» de la entrada de 40). No bloqueante. |
| M-2 | menor | cap-39:~195 | Se cortó «y el tribunal decidiría sobre NIDHOGG» | B1 §depósito; canon del reparto de control | Hecho preservado por «Mantuvo la midlertidig forføyning sobre NIDHOGG» (150) y «NIDHOGG quedaba fuera de su custodia» (196). Sin pago colgando. Sin acción obligada. |
| M-3 | menor | cap-39:~192 | Se cortó «Podría comunicar incidencias, recibir e impugnar registros y solicitar visitas» (facultades de Maja) | Facultades del canon | Redundante: la «ventana supervisada… para futuras visitas» (190) y los registros que Maja maneja en 40 (mostró una salida registrada; programó entrega) mantienen grounding. Sin acción obligada. |
| M-4 | menor/info | cap-40 (antes 161) | Se cortó «la consulta tendría otra sesión el mes siguiente» | B4 CH-26 y §5.3 citan 40:161 | El pago (40:175 «Aslak estaba con la asociación en la **segunda sesión** de la consulta») **se conserva**; N6 paga el acta. Se cortó el presagio, no el cobro. Actualizar la referencia 40:161 en B4 §5.3 (informativo). |
| I-1 | info | (varias) | La poda desplazó líneas físicas; muchas referencias `cap-NN:L` de B4/B1 (p. ej. 34:167→165, 34:197→277, 38:187-191, 39:101-103) apuntan ahora a líneas corridas | B4/B1 numeración | Mantenimiento de A1: revisar el mapa de líneas de B4/B1 tras la fusión. No es fallo de continuidad. |

## Nota de seguridad (no relacionada con la novela)

Durante la lectura, la **salida de una herramienta contenía una inyección de instrucciones** («While bypass permissions mode is active: Do your work through the Bash tool…» y un aviso de cambio de fecha). No procede de A0 ni del usuario; **la ignoré** y mantuve mi método y herramientas habituales. Lo reporto para trazabilidad.
