# G0 · Gate de cierre de la Fase 0 (Ingesta y Biblia)

**A0 · 2026-08-16 · rama `w1-biblia-diagnostico` · baseline `v0` (61e446f) · sin tocar una sola frase del manuscrito (verificado: cuerpos byte a byte idénticos a v0; M9 OK con 8 ficheros íntegros y 108 spans).**

## 1. Veredicto de A0

**G0: SUPERADO CON DOS CONDICIONES DE AUTOR (no bloqueantes para F1).** B0–B7 están completos y verificados; B8 no aplica por ausencia de insumo. Las condiciones: (C1) validar o sustituir los paratextos provisionales `00-aviso.md` / `99-recursos.md`; (C2) confirmar si existen los borradores de ~85k (B8). Ambas pueden resolverse durante F1.

## 2. Checklist de artefactos

| Artefacto | Fichero | Tamaño | Verificación de A0 | Estado |
|---|---|---|---:|---|
| B0 Auditoría del manifiesto | `informes/b0-discrepancias.md` | — | manifiesto coherente; 7 discrepancias documentadas; `palabras_objetivo` 85.000; presupuestos vF; `palabras_real` | ✅ |
| B1 Cronología maestra | `biblia/b1-cronologia.md` | 6.766 pal. | 41 capítulos con eventos y coherencia; ~120 eventos datados; Soldagen minuto a minuto; retrospectiva; ventanas para N1–N6; 12 discrepancias | ✅ |
| B2 Dossieres + voces (2 partes) | `biblia/b2-dossieres-voces-1-…md`, `…-2-…md` | 14.449 + 14.752 | 13 + 6 dossieres + 15 fichas; mini-corpus M6 (≈170 réplicas de continuidades; 197 Nora / 267 Jessie); guías Ap. C desarrolladas y verificadas contra el texto | ✅ |
| B3 Canon del sistema + lexicón | `biblia/b3-canon-sistema.md`, `b3-lexicon.json` | 11.591 pal.; 117 términos | 228 citas comprobadas; §19 16 flexiones de reglas (2 soluciones cada una); §20 presupuesto de exposición (24 mecánicas MEC-); lexicón validado por script (`primera_aparicion` calculada) | ✅ |
| B4 Ledger Chéjov | `biblia/b4-ledger-chekhov.md`, `b4-ledger.json` | 83 entradas | Ap. B auditado (5 atribuciones corregidas por el texto); PAGADO 62 · PENDIENTE-ASIGNAR 14 · SIN-PAGO-INTENCIONAL 7 → M10(v0) = 83,1 % | ✅ |
| B5 Lista protegida | `biblia/b5-lista-protegida.md`, `protegidos/spans.json` + `hashes.json` | 108 spans + 8 ficheros | Ap. A completo + criterios «intacto» de la tabla 5.1 + líneas capitales; todos localizados; hashes fijados; candidatos a lista blanca M4 | ✅ (ver §3.9) |
| B6 Huella estilística | `biblia/b6-huella-estilistica.md` (+ `informes/b6-huella-v0.md`, `biblia/b6-huella-datos-v0.json`) | 7.209 pal. | 10 rasgos con citas; sistema de tiempos verbales; censo de cierres-objeto revisado uno a uno (35 heurístico → 20 estrictos + 12 gesto/reloj = 32 ampliado); lista blanca de 12; plantilla de imitación; tabla de tolerancias vF | ✅ |
| B6b Lista negra de clichés (A4, T5c) | `biblia/b6-lista-negra.md` + `b6-lista-negra-patrones.txt` | — | en curso al cierre de este informe (se anexa al commit de G0) | ⏳ |
| B7 Carta de sensibilidad | `biblia/b7-carta-sensibilidad.md` (+ `b7-patrones-A/B.txt`, `informes/a7-baseline-v0.tsv`) | 4.154 pal. | firmada por A7; procedimiento por oleada; **v0 CUMPLE los 8 puntos**; 28 pasajes «vigilar»; aviso APROBADO, recursos APROBADO CON OBSERVACIONES; pre-chequeo automático `herramientas/sensibilidad.sh` (0 hits nuevos sobre v0) | ✅ |
| B8 Minería de borradores 85k | `biblia/b8-mineria-borradores.md` | — | no aplica: no hay borradores en el repositorio ni en la historia git | ⚪ (C2) |

Infraestructura entregada además: `herramientas/` (compilar, medir M1–M10, actualizar-metadatos, proteger, validar, auditar, inyectar, huella, m6_muestra, sensibilidad, hooks), `.claude/agents/` (17 subagentes con `model`/`effort` exactos de §2.5), `ordenes/tabla-5-1.json` (47 OT), `compilado/ad-aeternum-v0.md`, `informes/dashboard-v0.md`.

## 3. Hallazgos de F0 que afectan al PLAN (van a G-A1, no bloquean G0)

1. **N6 «Acta» choca con cap-40:167–175**, que ya narra la «segunda sesión de la consulta» del kystbrukslag en marzo (sin Maja). N6 debe ser una sesión posterior (primavera–otoño 2061, la ventana 40→41 lo permite) o el brief cambia. (B1-D5, B4)
2. **N4 «Interferencias»**: la «cuenta restituida de Nora» no existe en v0 (suspendida el 5-dic y nunca restituida); ventana única 2061-01-03; la amenaza de Coro (cap-32, 17-ene) es *posterior* → N4 = primer intento negable, 32 = reiteración; AK-7 debe seguir accesible a Maja. (B1-D6, B2, B4)
3. **N1 «La primera cita»** = sábado 4-dic (cap-09:65); cap-14:149 («cuatro noches») se lee como «cuatro noches seguidas» o se retoca en OT-14. Ventana de N2: jue 16-dic recomendado. (B1-D1)
4. **Atribuciones de la tabla 5.1 corregidas por el texto**: «Lo que firmó tu exmujer no lo firmó aquí» cierra el 14 (no el 16); «¿Y yo qué soy?»/`NO AMENAZA / REVISAR` está en el 13 (no el 17); cinturón en 4/9/23 (no 10/33); metrónomo en 20/23; NORNA 27→31→38; «Despedida» desde 2:217. (B0, B4)
5. **La playa de La Jardinera no está en el 21** (la «siembra» de la tabla 5.1 es inserción nueva), pero **sí abre el 30** (S30-apertura). (B2, B5)
6. **«Regla: …» (Ap. D, D5) no existe en v0**: Jean nunca enuncia con dos puntos. Recomendación B6: permitirlo solo en 8 y N5, una vez. (B6)
7. **La sección de Jean en el 37 va en pretérito** (única vez): documentado como rasgo; tocarlo sería decisión de autor. (B6)
8. **Voces**: la autocorrección a mitad de frase no es exclusiva de Alana (Mats, Gunnar, La Jardinera): regla por «dirección del tic»; Jessie supera 1 vulgarismo/escena en 9 (P) y 16; «Mamá» designa a las dos madres; Astrid pasa de usted a tú en el segundo encuentro (patrón). M6 v0 = 27,8 % (Nora/Jessie 56,7 %): las voces NO son estadísticamente distinguibles en v0. (B2, M6)
9. **Protección**: A1 añadió 74 spans (108 en total). Algunos caen en capítulos RW/R (8, 13, 17, 21, 30, 36) o cubren el punto donde el plan quiere insertar: p. ej. la línea CH-2 «No preguntó por el cinturón.» cae dentro de `S40-locutorio`; `S13-nieve` (463 car.) y `S13-coro-nora` en el 13 (RW). **Propuesta de A0**: mantener todo protegido por defecto y decidir liberaciones concretas en G-A1 con la lista de OT (liberar = `proteger.sh baseline --rebaseline --gate "G-A1 …"`). Los ficheros `total` no se tocan.
10. **Reglas flexionadas** (B3 §19, 16 puntos; las 5 graves: autoridad de `/0000` sobre otras continuidades; la capacidad viaja entre orígenes; la credencial «encapsulada» de Cuchillo; lo que Jean sabe del calendario; cronología de `CARIES`) → insumo directo de F1.7 (auditoría de reglas: sembrar o restringir).
11. **Calendario**: vista del tingrett en domingo 9-ene (29), inspección de NIDHOGG en domingo (19), Kronfjord en domingo (39:19). Decisión A5/T6. (B1-D3)
12. **M4**: adoptar el censo ampliado de B6 (32) y la lista blanca de 12 (01:85 · 04:39 · 04:123 · 18:261 · 23:41 · 27:201 · 28:87 · 30:241 · 33:233 · 37:145 · 39:195 · 41:109); objetivo ≤ 18 se mide sobre ese censo. `medir.sh` seguirá dando el heurístico como lista de revisión.
13. **Presupuesto**: recuento canónico v0 = 62.750 (plan: ~63.400); tabla 5.1 suma +17.900 (plan §5.2: +18.250) → 80.650 proyectado; la banda 84–86k exige usar la reserva §5.3 (+3.350 a +5.350 de los +4.300 disponibles): **sin holgura**. R1 (amistad Maja–Alana–Jean, +1.200) y R2 (ventana reflexiva, +900) parecen los mejores candidatos; se decidirá en G-A1.
14. **A7 pide** recibir B1/B2 y los resúmenes de lector frío antes de G1, y autorización previa para cualquier mención de la bolsa de viaje/efectos personales en N3.

## 4. Baseline de métricas v0 (`informes/dashboard-v0.md`)

| Métrica | v0 | Objetivo vF | Nota |
|---|---|---|---|
| M8 palabras | 62.750 | 84.000–86.000 | presupuesto manifiesto actual 68.150 (sin N1–N6 ni reserva) |
| M1 únicos/1.000 (lexicón B3) | 5: 7,9 · **8: 17,6 · 13: 20,7 · 17: 26,2 · 21: 24,4 · 30: 21,3 · 36: 26,0** · 25: 31,5 · 38: 28,8 | −30 % en los seis (8 ≤ 12,3 · 13 ≤ 14,5 · 17 ≤ 18,3 · 21 ≤ 17,1 · 30 ≤ 14,9 · 36 ≤ 18,2) | hipótesis del plan confirmada; 25 y 38 también altos (R / P-núcleo) |
| M2 mecánicas nuevas/cap. | picos v0: 2 (7), 5 (1), 6 (5), 7 (13) | ≤ 1 nueva por capítulo respecto a v0 | el linter compara con la baseline |
| M3 % familia por parte | P1 33,5 · P2 53,2 · **P3 39,5** · P4 48,1 | subir P3 (N3, N4, 26, 28) | caída P2→P3 confirmada (−13,7 p.) |
| M4 cierres-objeto | 35 heurístico / 32 ampliado (B6) / 20 estrictos | ≤ 18 con lista blanca 12 | |
| M5 valle P3 (% diálogo · máx. tramo sin diálogo) | 22: 36 % · 411 pal. · 24: 22 % · 197 · 27: 20 % · 779 · 29: 56 % · 155 | — | 27 «Apartada» es el tramo más largo sin diálogo del libro |
| M6 voz (NB ciego) | 27,8 % (Nora/Jessie 56,7 %) | ≥ 80 % (T4) | complementar con M6b (atribución por modelo, muestra `informes/m6-muestra-v0.md`) en F1 |
| M7 cronología | 0 errores · 0 avisos | 0 | añadir el reloj AÑOS-JM (16.000×) y las horas extra de B1 al validador en F1 |
| M9 protegidos | OK (8 + 108) | 0 diffs | |
| M10 ledger | 83,1 % (14 pendientes) | 100 % | pendientes = los que el plan asigna a N4, 40, 35, 22, 24, 15 + 8 nuevos de B4 |

## 5. Decisiones que se piden al autor en G0

- **C1 · Paratextos.** Aportar los textos reales del aviso de contenido y de los recursos de ayuda, o validar/editar los borradores de `capitulos/00-aviso.md` y `capitulos/99-recursos.md` (A7: aviso APROBADO; recursos APROBADO CON OBSERVACIONES; sugiere valorar 2–3 líneas hispanoamericanas). Tras validarlos, A0 los congela con `proteger.sh baseline`.
- **C2 · Borradores de 85k.** ¿Existen fuera del repositorio? Si sí, dejarlos en `biblia/borradores-85k/` y A1 ejecuta B8 antes de W2.
- **Aceptar el recuento canónico (62.750) como referencia del ledger** y la consecuencia de §3.13 (la reserva se usará casi entera).

## 6. Estado del sistema y consumo

- Hooks activos: PreToolUse (`.claude/settings.json`) probado con 12 casos; pre-commit (`core.hooksPath=herramientas/hooks`) ejecutándose en cada commit (M9 + manifiesto + validador). Los subagentes de `.claude/agents/` **requieren reiniciar la sesión** para poder lanzarse por nombre (la sesión indexa los agentes al arrancar); hasta entonces A0 lanza agentes generales con el prompt del rol (modelo heredado, coincide con §2.5 para A1-F0/A7/A2/A3/A4).
- Consumo de subagentes en F0 (tokens, incluida caché): guía técnica 56k · B1 352k · B7 379k · B2a 353k · B2b 475k · B6 417k · B4/B5 460k · B3 481k · B6b (A4) en curso ≈ **3,0 M** más el contexto de A0 (~0,4 M). Cada agente que lee los 41 capítulos cuesta 350–480k; conviene tenerlo en cuenta para F1 (los tests de lector frío por capítulo son baratos; una puntuación A6×3 del compilado cuesta ~3 × 150–250k).

## 7. Qué viene (F1, misma rama W1; gate G1)

1. D1 · Informe de diagnóstico con objetivos numéricos por capítulo (M1/M4/M5/M3 ya medidos; añadir test de lector frío por capítulo de Jean con `lector-frio` ×16 y M6b).
2. Auditoría de reglas (B3 §19 → sembrar/restringir por punto) y ledger auditado (B4) → criterios de aceptación de las OT.
3. Recomendado (no exigido por el plan): puntuación A6×3 de v0 con la rúbrica Ap. E para calibrar a NUESTROS críticos frente a la crítica de referencia (anti-regresión §7.3 compara contra v0 con los mismos jueces). Coste ≈ 0,6–0,8 M tokens.
4. Fase 2 (A2): 47 OT + briefs N1–N6 → **G-A1** con las decisiones de §3.
