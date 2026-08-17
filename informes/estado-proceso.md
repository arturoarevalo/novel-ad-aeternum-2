# Estado del proceso (documento vivo de A0)

_Actualizar al cerrar cada fase/oleada y en cada pausa. Cualquier sesión nueva empieza leyendo CLAUDE.md, este fichero, `git log --oneline | head` y `git status`._

## Situación

- **Fase actual:** **W3 EJECUTADA Y MEDIDA. G-A2 pendiente de decisión del autor (`informes/g-a2-gate.md`): NO fusionar `w3-nuevos` hasta que lo apruebe.** W2 aprobada y fusionada en `main` (7479e02). G-A1 aprobado (2026-08-17) y Fase 2 fusionada en `main`. W1 (F0 + F1) cerrada (G0, G1 aprobados).
- **Rama:** `w3-nuevos` (17 commits sobre `main`, sin fusionar). M9 OK y validador limpio en todos.
- **Baseline:** tag `v0` (61e446f). Recuento canónico v0: 62.750 palabras.
- **Última versión aceptada:** v0.

## Hecho en F0

1. Tag `v0`; rama W1; hooks M9 (PreToolUse en `.claude/settings.json`; pre-commit vía `core.hooksPath=herramientas/hooks`).
2. B0 ejecutado → `informes/b0-discrepancias.md` (manifiesto coherente; 7 discrepancias plan↔texto/repo documentadas; `palabras_objetivo` 85.000; presupuestos vF por capítulo).
3. Frontmatter §2.4 inyectado en 41 capítulos (cuerpos byte a byte idénticos a v0). Índice de OT en `ordenes/tabla-5-1.json` (47 OT).
4. `protegidos/spans.json` (8 ficheros total + 34 spans) + `hashes.json`.
5. `herramientas/`: compilar, medir (M1–M10), actualizar-metadatos, proteger, validar, auditar, inyectar, huella, m6_muestra. Compilado v0 (`compilado/ad-aeternum-v0.md`) y dashboard v0.
6. Subagentes en `.claude/agents/` (17 ficheros; modelos/esfuerzo exactos §2.5). **Requieren reiniciar la sesión para estar disponibles por nombre.** En F0 el trabajo de A1/A7 se ha lanzado con agentes generales que llevan el prompt del rol y heredan el modelo (coincide con §2.5).
7. Paratextos provisionales `00-aviso.md`/`99-recursos.md` (pendientes de validación de autor).

## Decisiones de autor en G0 (registradas 2026-08-16)

- **C1:** el autor edita él mismo `capitulos/00-aviso.md` y `capitulos/99-recursos.md`. Siguen `provisional: true` (sin hash M9) hasta que diga «paratextos listos»; entonces A0 pone `provisional: false`, re-registra con `actualizar-metadatos.sh paratexto`, y congela con `proteger.sh baseline`. Mientras tanto el compilado los incluye tal como estén.
- **C2:** no existen borradores previos → B8 cerrado (no aplica).
- **Recuento canónico 62.750 aceptado** como referencia del ledger.
- G0: **SUPERADO**.

## Biblia entregada (F0)

B0 `informes/b0-discrepancias.md` · B1 `biblia/b1-cronologia.md` · B2 `biblia/b2-dossieres-voces-1-…` y `-2-…` · B3 `biblia/b3-canon-sistema.md` + `b3-lexicon.json` · B4 `biblia/b4-ledger-chekhov.md` + `b4-ledger.json` · B5 `biblia/b5-lista-protegida.md` + `protegidos/` · B6 `biblia/b6-huella-estilistica.md` (+ lista negra A4) · B7 `biblia/b7-carta-sensibilidad.md` · B8 no aplica. Hallazgos para G-A1: `informes/g0-gate.md` §3.

## F1 · D1 ENTREGADO — G1 APROBADO (2026-08-16, sesión 3)

- **Aislamiento resuelto** (`informes/d1-aislamiento.md`): sonda haiku confirmó que TODO subagente hereda CLAUDE.md + memoria + email; nueva herramienta `herramientas/critica-fria.sh` (claude -p fuera del repo, rúbrica como system prompt, modelo por ID, sin herramientas, insumo inline) verificada limpia; A6/A6b/lector-frio/m6-atribuidor solo se lanzan así (regla dura en CLAUDE.md).
- **Baseline fría real de v0 (A6×3):** mediana global **8,0** · premisa 8 · estructura 7,5 · prosa 8 · diálogo 8 · personajes 8 · mundo 8 · **ritmo 7** · trama 7,5 · duelo 9 · tema 8,5 (`informes/a6-v0-critico-{1,2,3}-frio.md`). Es la baseline de anti-regresión (§7.3). Los contaminados se conservan.
- **D1 entregado:** `informes/d1-diagnostico.md` (objetivos numéricos por capítulo = criterios de aceptación de las OT; decisiones B3 §19 y ledger B4; hallazgos nuevos para F2/G-A1). Insumos: lector frío ×16 en frío (`informes/d1-lector-frio/lf-NN.md`; T1 = 2/5, cap. 5 = 4/5), M6b (`informes/m6b/`, canónica 42 %), M4b (`herramientas/lib/m4b_antepuestas.py`, 5,3 %), A5 (`d1-auditoria-reglas.md`), A7 (`d1-a7-biblia.md`), A1-mantenimiento aplicó canon B3 §21 y ledger B4 (CH-44/76 SIN-PAGO-INTENCIONAL; CH-31 → R2 provisional).
- **Gate:** `informes/g1-gate.md` APROBADO; decisiones del autor en `informes/registro-gates-autor.md` (M6b ≥ 60 %; jurado frío como baseline; R2 provisional; escena de Jean viva → brief N3/N1 para G-A1; coche gris → N4; **bolsa/efectos personales SÍ aparecen en vF bajo protocolo A7**; A6b en el primer hito).
- **Tras la aprobación de G1:** merge de `w1-biblia-diagnostico` en `main`; después Fase 2 (A2: 47 OT + briefs N1–N6) → **G-A1** (autor).

## F2 · Plan estructural — G-A1 APROBADO (2026-08-17)

- 47 OT + `ordenes/OT-25b.md` (R2, coda de 25) en `ordenes/` (plantilla `ordenes/PLANTILLA-OT.md`), briefs N1–N6, `ordenes/RESERVA.md` (R1–R5 aprobadas: R1 en N3 → 3.500; R2 OT-25b; R3 22/28/40; R4 diferida a A6b; R5 condicionada a W2), `informes/f2-mapa-intervenciones.md` (`herramientas/lib/mapa_ot.py --md`), `informes/g-a1-gate.md`. Σ Δ = +17.900 → 80.650; con reserva 84.650. 163 intervenciones etiquetadas; ningún span requiere liberación. Ajustes G-A1 aplicados: OT-N3 (I-5 candidato A aprobado; R1 dentro), OT-N6 (POV Aslak), OT-22/28/40 (R3 aprobada), OT-27 (R1 alternativa cancelada), OT-06 (amistad reservada a 20/N3), OT-25 §5 (R2 → OT-25b), OT-N4 (espejo solo si R4), OT-36 §5 (ripple N4 en W5).
- **Modelos (decisión de autor 2026-08-17):** ningún agente en `claude-fable-5`; ver CLAUDE.md «Modelos y esfuerzo». Re-baseline de v0 con el nuevo jurado HECHA: `informes/a6-v0-baseline-opus5.md` (mediana global 8,5; ritmo 7,5; diálogo 8; resto ≥ 8,5; coste 4,4 USD). Hallazgo nuevo del jurado: la escena de **Maja frente al locutorio** («Maja no solicitó acceso», 39) resuelta en resumen → pendiente para OT-39/OT-40 en W4/W5 (A2 lo dimensiona; ≤ 200 palabras, T3).
- **Pendiente de la orden del autor:** arrancar W2 (rama `w2-reescrituras`; `inyectar-frontmatter.sh --set cap-NN.md estado=en_oleada` para 8, 13, 17, 21, 30, 36; A3a en el orden 8, 13, 30, 17, 21, 36; A4; A5; A8; lector frío ×6 + A6×3 frío + A6b ×4 (con v0 en paralelo, para asignar R4); gate W2: M1 −30 %, lector frío ≥ 3, Ritmo ≥ 7,5, Tema sin caída, ningún eje −0,5).

## F2b · Motor `codex` y jurado mixto (2026-08-17, sesión 4)

- **A6-3 pasa a `gpt-5.6-sol` (OpenAI, max) vía `critica-fria.sh --motor codex`** (decisión de autor, `informes/registro-gates-autor.md`). Razón: tras G-A1 escribían y juzgaban modelos de la misma familia; la diversidad de conjunto de §2.5 era nominal. **La mediana de v0 no se mueve en ninguno de los once ejes** (`informes/a6-v0-baseline-opus5.md` §4), así que la baseline de anti-regresión sigue siendo la misma: global 8,5 · ritmo 7,5 · diálogo 8 · resto ≥ 8,5.
- **Infraestructura nueva:** `herramientas/lib/motor_codex.py` (aislamiento, aserción de modelo, trazabilidad) + `--motor codex` en `critica-fria.sh` + sonda propia que **falla cerrada** (`--sonda --motor codex`: exige que el shell de codex no pueda leer el repositorio; en este contenedor bwrap no puede crear namespaces). Protocolo, evidencia y salvedades: `informes/d1-aislamiento.md` §5. **Obligatorio pasar la sonda antes de cada campaña de scoring.**
- **`herramientas/auditor-adverso.sh`** (nuevo): audita las inserciones de un capítulo contra su etiqueta de función (riesgo «hinchazón», §8; formaliza la auditoría del 20 % que el plan encarga a A0) con `gpt-5.6-sol` max. Se usará en W2 y W4 sobre cada capítulo tocado, después de A4 y antes de A8.
- **M6b variante 4 (juez ajeno):** 41,1 % frente al 39,3 % de `claude-opus-4-8` (`informes/m6b/m6b-v0-variante-4-sol.md`). El 39–41 % de v0 es propiedad del texto, no del lector: el criterio M6b ≥ 60 % de G1 se mantiene tal cual.
- **Hallazgo convergente para W4/W5:** el juez nuevo pide, por su cuenta, una escena doméstica de duelo sin interfaces («la mañana posterior a la cuarta nota»), que es la misma deuda que el jurado opus-5 formuló como «Maja frente al locutorio» (39). Dos familias de modelos sin contacto señalan el mismo hueco → deja de ser opinión. A2 lo dimensiona en OT-39/OT-40.
- **Límite conocido:** la A/B ciega final (§7.3) NO puede ejecutarse en codex (v0 + vF ≈ 265k tokens contra una ventana de 272k); se queda en jueces Claude.
- **W2 sigue sin arrancar:** esperando la orden del autor.

## W2 · Reescrituras críticas — EJECUTADA, gate pendiente del autor (2026-08-17, sesión 5)

- **Los seis capítulos reescritos, un commit por OT.** M1: −33 · −32 · −32 · −33 · −31 · −32 % (objetivo −30 %). M2 = 0 mecánicas nuevas en los 41. Cero términos del lexicón nuevos: la lista de cada capítulo es subconjunto estricto de la de v0. +892 palabras (62.750 → 63.642), +142 sobre la línea de «reescrituras netas» del ledger, todo dentro de banda por capítulo.
- **Cadena completa:** A3a ×6 → A7 (caps. 8 y 17) → A4 pasada de línea → A5 continuidad → auditoría adversarial ×6 (`gpt-5.6-sol`) → A4 reparación → A8 → 36 lecturas de lector frío + 4 críticos A6 + 8 lectores beta.
- **Anti-regresión:** mediana w2 idéntica a la baseline salvo estructura y mundo (−0,5), y el **control de deriva** demuestra que es varianza de juez: el mismo crítico, el mismo día, puntúa v0 en 8 y 8,5 en esos dos ejes. Pareado v0↔w2 con el mismo juez: **ningún eje baja, cuatro suben** (prosa, diálogo, personajes, trama). Global 8,5. Ritmo 7,5. Tema 9,0. Sin veto en Duelo.
- **Cualitativo clave:** el cap. 8 **desaparece** de la lista de «dónde estuve a punto de abandonar» de los críticos (ahora nombran 24, 16 y 30) y del lector que abandonó. Los tres críticos enuncian la regla del capítulo denso que les toca. El lector frío responde «dónde ocurre» en el 21 y el 30 (Telegrafbukta).
- **Criterios incumplidos y su explicación medida:** lector frío ≥ 3 (2,11 frente a 2,17 de v0 con el mismo instrumento; la baseline de D1 era **un solo pase** y con tres el cap. 8 de v0 da 3-3-3) y ≤ 6 términos (solo el 8). Detalle en `informes/w2-gate.md` §4.
- **Decisiones que el gate somete al autor:** D-1 reformular el criterio de lector frío; D-2 sustituir «M6-continuidades ≥ 75 %» por anti-regresión (v0 = 73,2 %); **D-3 asignar R4 → N4 con encargo redefinido** (los cuatro A6b no piden más instituto ni más amenaza: piden entender a Coro); D-4 fusionar.
- **Hallazgos para las oleadas siguientes:** el valle procedimental (22, 24, 27, 29, 39) es el nuevo cuello de botella y el 24 lo señalan tres lectores; «Jean viva con sus hijas» la piden por unanimidad (y también en v0) → confirma la decisión B de G-A1; **T1 y T4 se contradicen** (retirar un término puede llevarse el marcador de voz de quien lo dice: caso medido «divergencia»); el cap. 30 queda con 0,3 de margen de M1 para W5.
- **Dos herramientas fallaban abiertas y se corrigieron:** `sensibilidad.sh --solo` y `extraer.sh` no comprobaban nada si se les pasaba una ruta en vez del basename. La primera alimenta un gate con veto.

## W3 · Capítulos nuevos — EJECUTADA, G-A2 pendiente del autor (2026-08-17, sesión 5)

- **Los seis capítulos nuevos escritos, un commit por OT.** N5 1.822 · N1 2.070 · N2 1.946 · N3 3.572 (con R1) · N4 3.156 (con R4) · N6 1.641 = **14.207 palabras**. Manuscrito: 47 capítulos, 77.849 palabras. Una sola mecánica nueva en toda la oleada (la de G-A1). M7 0 errores con los seis decimales intercalados; M9 OK.
- **Cadena:** A2 (R4 sobre OT-N4) → A3a/A3b ×6 en paralelo → A7 ×5 → A5 → auditoría adversarial ×3 → A4 → A7 segunda lectura (levantó el bloqueo) → A8 → lector frío ×6 + A6 ×3 + control de deriva + prueba de mano única ×5 + M6b.
- **Gate:** carta F firmada en los seis sin veto; «¿parece del mismo autor?» superado (ninguno de cinco lectores ciegos separa lo nuevo de v0); anti-regresión sin caídas contra el control de deriva; global 8,5 · ritmo 7,5 · duelo 9,5 · tema 9,0. El clímax pasa a «se gana en tres cuartas partes».
- **R4 aplicada a N4** por la evidencia de los A6b (ninguno pedía más instituto ni más amenaza; los cuatro decían no entender qué es Coro). Solución de A2: Coro no dice una réplica en todo el capítulo; se le ve trabajar. **Un crítico de tres nombra N4 como su punto de abandono** y la reversión de I-5 está preparada: es la decisión D-1 del gate.
- **Las dos frases de la bolsa quedan autorizadas literalmente por A7** (`informes/a7-w3-n3.md`), cumpliendo la decisión de G1, con siete prohibiciones hacia adelante.
- **Hallazgo: M6b se mide con ancla cuando hay pocos hablantes.** Sin ella el instrumento confunde «voces indiferenciadas» con «voces diferenciadas y etiquetas cambiadas»; en la prueba binaria de las gemelas eso valía cincuenta puntos. Con ancla, N2 da 86,1 % y v0 64,3 % (D1 registraba 21 %). **Rehecha ya la medición global con ancla** (v0 33,9 % · w3 32,7 %, azar 11 %): a escala de libro el ancla solo aporta ~5 puntos, la diferenciación de voces sigue siendo genuinamente baja y **T4 conserva su justificación**; A0 retiró la deducción contraria (`informes/m6b/m6-voces-w3.md` §5). W4 y W6 no se redimensionan por este motivo.
- **Pendiente tras el gate:** A1-mantenimiento registra los seis en `capitulos[]` con `origen: "REVISIÓN 10"` (solo puede hacerse tras superar G-A2) y anota el canon nuevo de `a5-w3-continuidad.md` y de C-4 de `a7-w3-n3.md`.

## Registro de consumo (orientativo)

- Sesión 5 (2026-08-17), W3 completa: subagentes ≈ **2,6 M tokens** (A3b ×5 1,54 M · A3a 275k · A7 ×5 599k · A4 304k · A5 203k · A2 164k). Fuera de sesión: **10,28 USD** (A6 ×4 7,36 · mano única ×5 1,41 · M6b ×15 0,98 · lector frío ×6 0,52). Sin coste por token: A6-3 sol y auditoría adversarial ×3.
- Sesión 5 (2026-08-17), W2 completa: subagentes en sesión ≈ **1,96 M tokens** (A3a ×6 1,17 M · A4 ×2 384k · A5 205k · A7 ×2 202k). Fuera de sesión (`critica-fria.sh`, coste real): **24,09 USD** — A6b ×8 (w2 y v0) 15,38 · A6 ×3 (2 sobre w2 + control de deriva sobre v0) 6,59 · lector frío ×36 (w2 ×3 pases y v0 ×3) 1,63 · M6-continuidades ×12 0,49. **Sin coste por token** (suscripción del autor): A6-3 `gpt-5.6-sol` sobre w2, auditor adverso ×6 y las dos sondas. Contexto de A0 ≈ 0,5 M. Acumulado de subagentes del proyecto ≈ 8,1 M.
- Sesión 4 (2026-08-17), motor codex: sonda + A6-3 sol sobre v0 (113k tokens) + M6b variante 4 (16k) **sin coste por token** (suscripción ChatGPT del autor); contexto de A0 ≈ 0,1 M. A partir de ahora cada hito de puntuación baja de ≈ 12 USD a ≈ 8,8 USD (A6-3 deja de facturarse).
- Sesión 3 (2026-08-17), cierre de G-A1: OT-25b y ajustes escritos por A0; re-baseline A6-1/2 opus-5 4,4 USD (total fuera de sesión 16,5 USD); contexto de A0 ≈ 0,1 M.
- Sesión 3 (2026-08-16), Fase 2: A2 ×4 ≈ 2,03 M tokens (A2-W2 477k · A2-N 493k · A2-F1 504k · A2-F2 561k); contexto de A0 ≈ 0,15 M. Acumulado subagentes ≈ 6,1 M.
- Sesión 3 (2026-08-16): F1 cerrada. Subagentes en sesión: sonda haiku 18k · A7 221k · A1-mant. 189k + 69k (+ A5 176k de la sesión 2) ≈ 0,67 M; fuera de sesión (`critica-fria.sh`, coste real): A6×3 frío 10,79 USD · lector frío ×16 1,00 USD · M6b ×4 0,30 USD ≈ 12,1 USD; contexto de A0 ≈ 0,35 M. Cada hito de puntuación completo costará ≈ 12 USD (A6×3 + lector frío de los capítulos tocados + M6b), + ≈ 9 USD si se añaden los A6b ×4.
- Sesión 1 (2026-08-16): F0 completa. Subagentes: guía técnica 56k · B1 352k · B7 379k · B2a 353k · B2b 475k · B6 417k · B4/B5 460k · B3 481k · B6b (A4) 345k ≈ 3,4 M tokens de subagentes (con caché) + ~0,4 M del contexto de A0.
