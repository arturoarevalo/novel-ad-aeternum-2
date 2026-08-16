# Estado del proceso (documento vivo de A0)

_Actualizar al cerrar cada fase/oleada y en cada pausa. Cualquier sesión nueva empieza leyendo CLAUDE.md, este fichero, `git log --oneline | head` y `git status`._

## Situación

- **Fase actual:** **FASE 2 ENTREGADA — G-A1 PENDIENTE DE DECISIÓN DEL AUTOR** (`informes/g-a1-gate.md`; rama `f2-plan-estructural`, sin fusionar). W1 (F0 + F1) cerrada y en `main` (G0, G1 aprobados).
- **Rama:** `f2-plan-estructural` (Fase 2: solo `ordenes/` e `informes/`; merge a `main` tras G-A1). W1 (`w1-biblia-diagnostico`) fusionada en `main`.
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

## F2 · Plan estructural ENTREGADO — G-A1 pendiente (2026-08-16, sesión 3)

- 47 OT en `ordenes/` (plantilla `ordenes/PLANTILLA-OT.md`), briefs N1–N6, `ordenes/RESERVA.md`, `informes/f2-mapa-intervenciones.md` (tabla maestra generada con `herramientas/lib/mapa_ot.py --md`), `informes/g-a1-gate.md`. Σ Δ = +17.900 → 80.650; con reserva entera 84.650. 163 intervenciones etiquetadas; ningún span requiere liberación. Arbitraje A0: la línea de registro de N4 en 36 entra en W5 (nota en OT-36 §5); OT-26 es W5.
- **Decisiones pedidas al autor en G-A1** (`g-a1-gate.md` §1): A posiciones/temas N1–N6 (N6 POV Aslak) · B recuerdo de Jean viva en N3 (candidato A) · C reserva R1–R5 con posiciones (R1 en N3; R2 cola de 25 como OT-25b) · D ledger (CH-31/44/76/2/48) · E sin liberaciones de spans · F N4 (mecánica única, sin espejo, inspección → 26/N6, cuenta restituida dentro) · G bolsa/efectos ya decidido (protocolo A7) · H ajustes menores (OT-30 +160…+240; M6-continuidades ≥ 75 % en 13; OT-37 → A3b; A6b tras W2; amistad Maja–Alana no en 6) · I merge y W2.
- **Tras la aprobación:** registrar decisiones; ajustar OT afectadas (+ OT-25b si procede); merge `f2-plan-estructural` → `main`; rama `w2-reescrituras`; `inyectar-frontmatter.sh --set cap-NN.md estado=en_oleada` para 8, 13, 17, 21, 30, 36; W2 con A3a en el orden 8, 13, 30, 17, 21, 36 → A4 → A5 → A8 → lector frío ×6 + A6×3 frío → gate W2.

## Registro de consumo (orientativo)

- Sesión 3 (2026-08-16), Fase 2: A2 ×4 ≈ 2,03 M tokens (A2-W2 477k · A2-N 493k · A2-F1 504k · A2-F2 561k); contexto de A0 ≈ 0,15 M. Acumulado subagentes ≈ 6,1 M.
- Sesión 3 (2026-08-16): F1 cerrada. Subagentes en sesión: sonda haiku 18k · A7 221k · A1-mant. 189k + 69k (+ A5 176k de la sesión 2) ≈ 0,67 M; fuera de sesión (`critica-fria.sh`, coste real): A6×3 frío 10,79 USD · lector frío ×16 1,00 USD · M6b ×4 0,30 USD ≈ 12,1 USD; contexto de A0 ≈ 0,35 M. Cada hito de puntuación completo costará ≈ 12 USD (A6×3 + lector frío de los capítulos tocados + M6b), + ≈ 9 USD si se añaden los A6b ×4.
- Sesión 1 (2026-08-16): F0 completa. Subagentes: guía técnica 56k · B1 352k · B7 379k · B2a 353k · B2b 475k · B6 417k · B4/B5 460k · B3 481k · B6b (A4) 345k ≈ 3,4 M tokens de subagentes (con caché) + ~0,4 M del contexto de A0.
