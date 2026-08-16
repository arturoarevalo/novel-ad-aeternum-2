# G1 · Gate de cierre de la Fase 1 (Diagnóstico instrumentado)

**A0 · 2026-08-16 · rama `w1-biblia-diagnostico` · baseline `v0` (61e446f) · cero prosa tocada (M9 OK: 8 ficheros íntegros, 108 spans).** Según §4 del plan, G1 convierte los números de D1 en criterios de aceptación de las órdenes de trabajo. Este informe presenta al autor el cierre de F1 y las decisiones que le corresponden. **W1 (F0 + F1) no se fusiona en `main` hasta su aprobación.**

## 1. Veredicto de A0

**G1: SUPERADO por A0, condicionado a la aprobación del autor** (decisiones de §4). Los siete puntos de la Fase 1 están hechos y documentados; los objetivos numéricos por capítulo (D1 §10) son los criterios de aceptación que A2 llevará a las 47 OT en la Fase 2. El hallazgo crítico de la sesión 2 (aislamiento roto de los lectores en frío) está resuelto, verificado y convertido en herramienta y regla dura.

## 2. Checklist de la Fase 1 (§4 del plan)

| # | Punto | Resultado | Evidencia |
|---|---|---|---|
| 1 | Mapa de opacidad M1 | Hipótesis confirmada: 8: 17,6 · 13: 20,7 · 17: 26,2 · 21: 24,4 · 30: 21,3 · 36: 26,0 únicos/1.000 (cap. 5 = 7,9); 25 y 38 aún más densos (R / P núcleo). Objetivo −30 % fijado por capítulo | `informes/dashboard-v0.md`, D1 §2 y §10 |
| 2 | Mapa de ritmo | Valle P3 con cifras (27: 779 palabras sin diálogo; 22/24/27/29 procedimentales); N3 (22.5) y N4 (25.5) lo rompen | D1 §3 |
| 3 | Presencia familiar | P2 53,2 % → P3 39,5 % (−13,7); objetivo P3 ≥ 48 %, caída ≤ 8 puntos | D1 §4 |
| 4 | Censo de tics M4 | 32 (censo ampliado B6), lista blanca 12, objetivo ≤ 18 con los 14 candidatos de B6 §5.6; **nuevo M4b** subordinadas antepuestas 5,3 % → ≤ 3,5 % | D1 §5, `herramientas/lib/m4b_antepuestas.py` |
| 5 | Test de lector frío por capítulo de Jean | 16/16 en frío real: T1 = **2/5** todos, 5 = 4/5, 15 = 3, 25/37/38 = 2; todos enuncian una regla salvo 8 (parcial); «dónde ocurre» sin respuesta en 17/21/36; objetivos ≥ 3 + regla + ≤ 6 términos opacos | `informes/d1-lector-frio/lf-NN.md`, D1 §6 |
| 6 | Ledger Chéjov auditado | 83 entradas; CH-44 y CH-76 → SIN-PAGO-INTENCIONAL (44 con hueco escenificado en 39); CH-31 → R2 provisional; CH-2 fuera de S40-locutorio; CH-48 sigue sin pago; M10 → ver §3 | `biblia/b4-ledger-chekhov.md`, D1 §8 |
| 7 | Auditoría de reglas contra B3 | 16 flexiones + 5 adicionales verificadas por A5; 4 A (F1→13, F2→21, F3→17, F14→13, ≈ +90 pal.), resto C; canon 1.185 / AÑOS-JM / capacidad fijado por A1 en B3 §21 | `informes/d1-auditoria-reglas.md`, D1 §9 |
| + | Baseline fría real (A6×3) | mediana global **8,0**; ritmo 7; estructura/trama 7,5; duelo 9; tema 8,5; resto 8. Sin veto en Duelo. Es la baseline de anti-regresión | `informes/a6-v0-critico-{1,2,3}-frio.md`, `informes/d1-aislamiento.md` |
| + | M6b atribución ciega | canónica 42 % (39,3 / 44,6); humanos ≈ azar; guías Ap. C no levantan a Maja | `informes/m6b/`, D1 §7 |
| + | Pase de A7 sobre B1/B2 + resúmenes (G0 §3.14) | B1 APROBADO; B2 APROBADO CON CORRECCIONES (3 obligatorias + 7 vigilar, aplicadas por A1 antes de este gate); resúmenes APROBADO (la elipsis resiste en frío) | `informes/d1-a7-biblia.md` |
| + | Aislamiento de lectores fríos | Sonda haiku: todo subagente hereda CLAUDE.md + memoria + email → `herramientas/critica-fria.sh` (claude -p fuera del repo) verificada limpia; regla dura en CLAUDE.md | `informes/d1-aislamiento.md` |

## 3. Estado de la Biblia tras F1

- B3 §19 con las decisiones A/B/C de A0; §21 dudas 1, 2, 3, 4, 6, 7, 8, 9 cerradas (5 → pendiente B5 en G-A1; 10 verificada). B1 anotada (CARIES 5-dic ≠ `/0000`; 1.185 = pérdida acumulada). B4: CH-44/CH-76 SIN-PAGO-INTENCIONAL, CH-31/CH-2/CH-48 con resolución de A0, emisor del audio de 28 registrado; **M10 v0 = 84,3 %** (70/83; 13 pendientes, todas asignadas a N1/N2/N4/N6 o a expansiones/W5). B2 con las correcciones de A7. Ninguna edición toca prosa ni protegidos.
- Herramientas nuevas: `critica-fria.sh` (+ `lib/critica_fria.py`), `lib/m4b_antepuestas.py`, agente `m6-atribuidor`. README y CLAUDE.md actualizados.
- Dudas menores dejadas por A1 para G-A1 (no bloquean): (a) 11:307 «consciencia residual: indeterminado» ya está cubierta por el span `S11-consciencia` (11:305-307) declarado en B4/CH-81: B5 debe aclarar si la protección como línea suelta es la misma o más fina, sin duplicar spans; (b) B1 §7: «cuatro noches» (14:149) vs cita del 4-dic (9:65) → decisión de A2 en OT-14; (c) el rótulo «M10 (v0)» del ledger pasa a leerse como «M10 (post-D1)»; (d) B2-2 §2(h) conserva una mención a «la mesa sin resumen» que A7 no marcó (A1 respetó el alcance): revisar en la siguiente pasada de B2.

## 4. Decisiones que se piden al autor en G1

1. **Baseline y objetivos por eje.** Aceptar la mediana del jurado frío propio (global 8,0) como baseline de anti-regresión (§7.3), manteniendo los objetivos absolutos de vF (global ≥ 9,0; suelo ≥ 8,5 en los diez ejes) medidos con ese mismo jurado. Consecuencia: premisa, mundo, diálogo y tema (8–8,5 en frío) pasan de «mantener» a «subir 0,5–1,0»; A0 propone aceptar como convergencia (§7.4) que **premisa** se quede en 8,5 si todo lo demás cumple, porque la premisa no cambia con la revisión.
2. **M6.** Sustituir el criterio «M6 ≥ 80 %» por **M6b canónica ≥ 60 %** (dos pasadas opus-4-8, reparto neutro; Nora/Jessie ≥ 60 %, Maja ≥ 40 %, ningún humano < 30 %). Baseline 42 %.
3. **R2 / CH-31 (ventana reflexiva).** A0 la activa provisionalmente (+900, escena breve en Parte III; A2 fija posición). Confirmación en G-A1 junto con R1 (amistad Maja–Alana–Jean, +1.200): la reserva §5.3 hará falta casi entera (proyección 80.650 sin reserva).
4. **Escena de Jean viva con sus hijas** (los tres críticos la echan en falta). Propuesta: recuerdo dramatizado ≤ 300 palabras en el brief de N3 (o N1), sin la discusión de Kongsbakken (CH-48 sigue elíptico) y sin tocar 1–4. Decisión en G-A1 (afecta a la ética elíptica de la Parte I).
5. **Coche gris del 24.** A0 recomienda que N4 lo pague como primer acto negable (opción i) en vez de podarlo; A2 lo dimensiona en F2.
6. **A7 · bolsa de viaje / efectos personales en N3.** A7 recomienda que **no aparezcan**; por defecto la OT de N3 lo declarará así. Si el autor quiere que en vF exista el dato «los efectos volvieron a la familia», debe decirlo (se anota en `informes/registro-gates-autor.md`) y A7 autorizará o vetará la frase literal.
7. **A6b ×4 sobre v0** (lectores beta simulados, ≈ 8–10 USD): opcional ahora; A0 propone lanzarlos en el primer hito (post-W2) en paralelo con v0, como control de deriva (§7.1). Decidir si se quieren ya.
8. **Merge de W1 en `main`** (fast-forward de `w1-biblia-diagnostico`) y arranque de la Fase 2 (A2: 47 OT + briefs N1–N6 → G-A1).

## 5. Riesgos abiertos

- El jurado frío tiene dos jueces del mismo modelo (fable ×2 casi idénticos): la mediana es «lo que opina fable». Mitigación ya prevista: opus como tercer juez, A/B ciega final con jueces mixtos; si el autor quiere más diversidad, un cuarto juez de otra familia solo es posible con otro proveedor (fuera de esta instalación).
- Los lectores en frío cuestan dinero real fuera de la sesión (A6×3 ≈ 10,8 USD por hito; lector frío 0,06 USD/capítulo; M6b 0,3 USD): presupuesto de scoring ≈ 12 USD por hito completo + A6b ≈ 9 USD si se añaden.
- La llamada auxiliar del harness (haiku, título de sesión) recibe el prompt completo: sin efecto en el juicio; coste ≈ 0,13 USD por lectura del compilado.

## 6. Consumo de F1 (esta sesión)

Subagentes en sesión (tokens con caché): A5 176k (sesión 2) · sonda haiku 18k · A7 pase breve 221k · A1 mantenimiento 189k + 69k ≈ **0,67 M**. Fuera de sesión (`critica-fria.sh`, coste facturado): A6×3 10,79 USD · lector frío ×16 1,00 USD · M6b ×4 0,30 USD · sondas 0,01 USD ≈ **12,1 USD**. Contexto de A0 en la sesión 3 ≈ 0,35 M tokens. Acumulado del proyecto: F0 ≈ 3,4 M + F1 ≈ 0,7 M de subagentes, más ≈ 0,75 M de contexto de A0 en total, más 12,1 USD facturados fuera de sesión.

## 7. Qué viene (tras la aprobación)

1. Merge W1 → `main`. 2. Fase 2: A2 redacta 47 OT (criterios de D1 §10 + hallazgos §11), briefs de N1–N6 con los ripples de G0 §3 y las condiciones de A7, mapa de intervenciones, posición de R2 (y R1 si se aprueba); A0 revisa solapes 13/15/17/21 → **G-A1** (autor). 3. W2 (rama `w2-reescrituras`): 8, 13, 30, 17, 21, 36.
