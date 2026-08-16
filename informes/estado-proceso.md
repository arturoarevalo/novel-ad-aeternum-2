# Estado del proceso (documento vivo de A0)

_Actualizar al cerrar cada fase/oleada y en cada pausa. Cualquier sesión nueva empieza leyendo CLAUDE.md, este fichero, `git log --oneline | head` y `git status`._

## Situación

- **Fase actual:** F0 CERRADA — G0 presentado (`informes/g0-gate.md`): superado con condiciones de autor C1 (paratextos) y C2 (borradores 85k). Siguiente: F1 (D1) en la misma rama W1 → G1 → merge a main.
- **Rama:** `w1-biblia-diagnostico` (oleada W1 = F0 + F1; merge a `main` solo tras G0 + G1).
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

## Pendiente de autor (G0)

- C1: aportar/validar aviso de contenido y recursos de ayuda (borradores provisionales; A7 los aprobó con observaciones).
- C2: ¿existen los borradores de ~85.000 palabras? No están en el repositorio.
- Aceptar el recuento canónico (62.750) como referencia del ledger (el plan citaba ~63.400) y que la reserva §5.3 se usará casi entera.

## Biblia entregada (F0)

B0 `informes/b0-discrepancias.md` · B1 `biblia/b1-cronologia.md` · B2 `biblia/b2-dossieres-voces-1-…` y `-2-…` · B3 `biblia/b3-canon-sistema.md` + `b3-lexicon.json` · B4 `biblia/b4-ledger-chekhov.md` + `b4-ledger.json` · B5 `biblia/b5-lista-protegida.md` + `protegidos/` · B6 `biblia/b6-huella-estilistica.md` (+ lista negra A4) · B7 `biblia/b7-carta-sensibilidad.md` · B8 no aplica. Hallazgos para G-A1: `informes/g0-gate.md` §3.

## Plan inmediato (F1)

1. Reiniciar la sesión (para que `.claude/agents/` esté disponible) → comprobar `git status`, `git log`.
2. Test de lector frío por capítulo de Jean (agente `lector-frio` ×16) + M6b (atribución ciega por modelo) → D1.
3. Auditoría de reglas (B3 §19) y ledger (B4) → criterios de aceptación por capítulo.
4. (Recomendado) A6×3 sobre `compilado/ad-aeternum-v0.md` para calibrar nuestros críticos frente a la crítica de referencia.
5. G1 → merge de `w1-biblia-diagnostico` a `main` → Fase 2 (A2: OT + briefs) → G-A1.

## Registro de consumo (orientativo)

- Sesión 1 (2026-08-16): F0 completa. Subagentes: guía técnica 56k · B1 352k · B7 379k · B2a 353k · B2b 475k · B6 417k · B4/B5 460k · B3 481k · B6b (A4) pendiente de cifra ≈ 3,0 M tokens de subagentes (con caché) + ~0,4 M del contexto de A0.
