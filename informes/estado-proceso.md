# Estado del proceso (documento vivo de A0)

_Actualizar al cerrar cada fase/oleada y en cada pausa. Cualquier sesión nueva empieza leyendo CLAUDE.md, este fichero, `git log --oneline | head` y `git status`._

## Situación

- **Fase actual:** F0 CERRADA — G0 SUPERADO (decisiones de autor registradas abajo). Siguiente: F1 (D1) en la misma rama W1 → G1 → merge a main.
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

## Decisiones de autor en G0 (registradas 2026-08-16)

- **C1:** el autor edita él mismo `capitulos/00-aviso.md` y `capitulos/99-recursos.md`. Siguen `provisional: true` (sin hash M9) hasta que diga «paratextos listos»; entonces A0 pone `provisional: false`, re-registra con `actualizar-metadatos.sh paratexto`, y congela con `proteger.sh baseline`. Mientras tanto el compilado los incluye tal como estén.
- **C2:** no existen borradores previos → B8 cerrado (no aplica).
- **Recuento canónico 62.750 aceptado** como referencia del ledger.
- G0: **SUPERADO**.

## Biblia entregada (F0)

B0 `informes/b0-discrepancias.md` · B1 `biblia/b1-cronologia.md` · B2 `biblia/b2-dossieres-voces-1-…` y `-2-…` · B3 `biblia/b3-canon-sistema.md` + `b3-lexicon.json` · B4 `biblia/b4-ledger-chekhov.md` + `b4-ledger.json` · B5 `biblia/b5-lista-protegida.md` + `protegidos/` · B6 `biblia/b6-huella-estilistica.md` (+ lista negra A4) · B7 `biblia/b7-carta-sensibilidad.md` · B8 no aplica. Hallazgos para G-A1: `informes/g0-gate.md` §3.

## F1 en curso (checkpoint 2026-08-16, sesión 2)

- Rama `w1-biblia-diagnostico` limpia al arrancar; agentes de `.claude/agents/` ya disponibles por nombre.
- Nueva herramienta: `herramientas/extraer.sh <etiqueta> [archivos]` → `compilado/extractos/<etiqueta>/cap-NN.md` (cabecera numerada + cuerpo sin frontmatter; insumo ÚNICO de `lector-frio`). Generados los 16 extractos v0 de capítulos de Jean (01 02 03 04 05 07 08 13 15 17 21 25 30 36 37 38).
- **Lanzados en segundo plano (resultados NO recogidos aún; si la sesión se corta, hay que relanzarlos):** A6×3 sobre `compilado/ad-aeternum-v0.md` (calibración; salida prevista `informes/a6-v0-critico-{1,2,3}.md`), `lector-frio` sobre cap-01 (hecho). **A5 ENTREGADO** (176k tokens): `informes/d1-auditoria-reglas.md` — 16 flexiones verificadas, cero bloqueantes; recomendaciones clave: F3→A (+30 pal. en 17:~89), F12→canonizar 1.185 en B1/B3 antes de W2, F1/F2→una D5 en N5, F14→«una copia del patrón de Madre» en 13 RW, tingrett en domingo→C (dejar); coste total A ≈ +103 pal., nada sobre protegidos. A0 decide A/B/C en D1.
- **⚠️ HALLAZGO CRÍTICO (sesión 2): el aislamiento de A6 está roto.** A6-1 y A6-2 (fable; `informes/a6-v0-critico-{1,2}.md`) reproducen literalmente N1/N3/N4/N5 y el plan B de 31 en sus «tres mejoras» (`informes/a6-v0-critico-1.md`), y A6-3 (opus-4-8) devolvió notas idénticas a `critica-ad-aeternum.md` (9/11 claves) y frases casi literales de ella (`informes/a6-v0-critico-3.md`, marcado como contaminado). Causa probable: los subagentes reciben CLAUDE.md, que `@`-importa el plan y la crítica de referencia. **Antes de cualquier hito de puntuación (y antes de dar por válida la calibración v0):** (1) verificar empíricamente con un agente barato (haiku) qué instrucciones de proyecto tiene en contexto; (2) arreglar: quitar los `@`-imports de CLAUDE.md (A0 lee plan y crítica explícitamente al arrancar) y, mejor aún, ejecutar A6/A6b desde un directorio FUERA del repositorio con solo el compilado (p. ej. `claude -p` en el scratchpad, sin CLAUDE.md), o al menos comprobar que sin los imports el crítico ya no reproduce la referencia; (3) relanzar A6×3 sobre v0 para la baseline real; los informes contaminados se conservan como evidencia. El mismo problema afecta a `lector-frio` (que también recibiría CLAUDE.md): sus resultados de v0 deben tratarse como orientativos hasta repetir el test aislado.
- **Pendiente de lanzar:** `lector-frio` para los otros 15 extractos (salida a `informes/d1-lector-frio/lf-NN.md` (nombres sin «cap-NN.md» para no disparar la heurística del hook M9)); M6b con `informes/m6-muestra-v0.md` (protocolo decidido: agente general con `model: opus`, variante 1 «reparto neutro» = canónica, variante 2 con guías Ap. C, + una pasada `fable`; puntuar con `herramientas/lib/m6_muestra.py puntuar v0 <respuestas.json>`); decisiones A0 sobre B3 §19 (A/B/C por flexión) y ledger B4 (CH-31, CH-44, CH-76; criterios de aceptación por OT); D1 (`informes/d1-diagnostico.md`) con objetivos numéricos por capítulo (M1 −30 % en los seis; M4 sobre censo B6 = 32 → ≤ 18 con lista blanca 12; M3 P3; M5 valle; lector frío ≥ v0+1); pase de A7 sobre B1/B2 + resúmenes de lector frío (petición G0 §3.14); `informes/g1-gate.md`; actualizar CLAUDE.md «Estado»; commit; presentar G1 + consumo al autor ANTES de fusionar en main.

## Plan inmediato (F1)

1. Reiniciar la sesión (para que `.claude/agents/` esté disponible) → comprobar `git status`, `git log`.
2. Test de lector frío por capítulo de Jean (agente `lector-frio` ×16) + M6b (atribución ciega por modelo) → D1.
3. Auditoría de reglas (B3 §19) y ledger (B4) → criterios de aceptación por capítulo.
4. (Recomendado) A6×3 sobre `compilado/ad-aeternum-v0.md` para calibrar nuestros críticos frente a la crítica de referencia.
5. G1 → merge de `w1-biblia-diagnostico` a `main` → Fase 2 (A2: OT + briefs) → G-A1.

## Registro de consumo (orientativo)

- Sesión 1 (2026-08-16): F0 completa. Subagentes: guía técnica 56k · B1 352k · B7 379k · B2a 353k · B2b 475k · B6 417k · B4/B5 460k · B3 481k · B6b (A4) 345k ≈ 3,4 M tokens de subagentes (con caché) + ~0,4 M del contexto de A0.
