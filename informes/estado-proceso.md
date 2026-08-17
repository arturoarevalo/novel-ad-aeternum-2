# Estado del proceso (documento vivo de A0)

_Actualizar al cerrar cada fase/oleada y en cada pausa. Cualquier sesión nueva empieza leyendo CLAUDE.md, este fichero, `git log --oneline | head` y `git status`._

## Situación

- **Fase actual:** **G-A1 APROBADO (2026-08-17) y Fase 2 fusionada en `main`. W2 NO arrancada: el autor reinicia la sesión con los agentes en `claude-opus-5` y dará la orden.** W1 (F0 + F1) cerrada (G0, G1 aprobados).
- **Rama:** `main` (W1 y F2 fusionadas). La siguiente rama será `w2-reescrituras` cuando el autor ordene arrancar W2.
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

## Registro de consumo (orientativo)

- Sesión 3 (2026-08-17), cierre de G-A1: OT-25b y ajustes escritos por A0; re-baseline A6-1/2 opus-5 4,4 USD (total fuera de sesión 16,5 USD); contexto de A0 ≈ 0,1 M.
- Sesión 3 (2026-08-16), Fase 2: A2 ×4 ≈ 2,03 M tokens (A2-W2 477k · A2-N 493k · A2-F1 504k · A2-F2 561k); contexto de A0 ≈ 0,15 M. Acumulado subagentes ≈ 6,1 M.
- Sesión 3 (2026-08-16): F1 cerrada. Subagentes en sesión: sonda haiku 18k · A7 221k · A1-mant. 189k + 69k (+ A5 176k de la sesión 2) ≈ 0,67 M; fuera de sesión (`critica-fria.sh`, coste real): A6×3 frío 10,79 USD · lector frío ×16 1,00 USD · M6b ×4 0,30 USD ≈ 12,1 USD; contexto de A0 ≈ 0,35 M. Cada hito de puntuación completo costará ≈ 12 USD (A6×3 + lector frío de los capítulos tocados + M6b), + ≈ 9 USD si se añaden los A6b ×4.
- Sesión 1 (2026-08-16): F0 completa. Subagentes: guía técnica 56k · B1 352k · B7 379k · B2a 353k · B2b 475k · B6 417k · B4/B5 460k · B3 481k · B6b (A4) 345k ≈ 3,4 M tokens de subagentes (con caché) + ~0,4 M del contexto de A0.
