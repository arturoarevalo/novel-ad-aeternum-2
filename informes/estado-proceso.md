# Estado del proceso (documento vivo de A0)

_Actualizar al cerrar cada fase/oleada y en cada pausa. Cualquier sesión nueva empieza leyendo CLAUDE.md, este fichero, `git log --oneline | head` y `git status`._

## Situación

- **Fase actual:** F0 (Ingesta y Biblia) — en curso, a la espera de B1–B7 y del gate G0.
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

## Pendiente de autor (para G0)

- D4: aportar/validar aviso de contenido y recursos de ayuda (borradores provisionales).
- B8: ¿existen los borradores de ~85.000 palabras? No están en el repositorio.
- Confirmar el recuento canónico (62.750) como referencia del ledger (el plan citaba ~63.400).

## Registro de consumo (orientativo)

- Sesión 1 (2026-08-16): F0. Subagentes lanzados: guía técnica (56k tokens), B1, B2×2, B3, B4+B5, B7, B6 (en curso).
