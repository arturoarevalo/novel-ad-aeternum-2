# Baseline de anti-regresión de v0 con el jurado vigente (A6-1/2 `claude-opus-5` + A6-3 `claude-opus-4-8`)

**A0 · 2026-08-17.** El autor decidió en G-A1 que ningún agente use `claude-fable-5` (ver `informes/registro-gates-autor.md`). Como la regla de anti-regresión (§7.3) exige comparar «con los mismos jueces», A6-1 y A6-2 se han relanzado sobre `compilado/ad-aeternum-v0.md` con `claude-opus-5` (esfuerzo max) mediante `herramientas/critica-fria.sh` (frío real, ver `informes/d1-aislamiento.md`); A6-3 (`claude-opus-4-8`, high) se conserva del 2026-08-16. Informes: `informes/a6-v0-critico-1-frio-opus5.md`, `informes/a6-v0-critico-2-frio-opus5.md`, `informes/a6-v0-critico-3-frio.md`. La baseline anterior (fable ×2 + opus-4-8, mediana global 8,0; `informes/d1-aislamiento.md` §4) queda como histórica.

## 1. Notas

| Eje | opus-5 n.º 1 | opus-5 n.º 2 | opus-4-8 n.º 3 | **Mediana (baseline vigente)** | Mediana fable (histórica) | Referencia |
|---|---:|---:|---:|---:|---:|---:|
| Premisa | 8,5 | 8,5 | 9 | **8,5** | 8 | 9 |
| Estructura | 8,5 | 8,5 | 8,5 | **8,5** | 7,5 | 8 |
| Prosa | 8,5 | 8,5 | 8,5 | **8,5** | 8 | 7,5 |
| Diálogo | 8 | 8 | 8,5 | **8** | 8 | 8,5 |
| Personajes | 8,5 | 8,5 | 8 | **8,5** | 8 | 7 |
| Mundo | 9 | 9 | 8,5 | **9** | 8 | 8,5 |
| Ritmo | 7,5 | 8 | 7 | **7,5** | 7 | 5,5 |
| Trama | 8,5 | 8,5 | 8 | **8,5** | 7,5 | 7 |
| Duelo | 9,5 | 9,5 | 9 | **9,5** | 9 | 9 |
| Tema | 9 | 9 | 9 | **9** | 8,5 | 9 |
| **Global** | 8,5 | 8,5 | 8,5 | **8,5** | 8 | 7,5 |

Coste: 2,18 + 2,21 USD (≈ 200–225 s cada uno; 172k tokens de entrada, 13–14k de salida). Sin veto en Duelo.

## 2. Lectura de A0

- **El jurado opus-5 es medio punto más benévolo que el fable** en casi todos los ejes (global 8,5 vs 8,0; ritmo 7,5 vs 7), y **coincide en el diagnóstico**: el 8 «Milisegundos» como el capítulo donde ambos estuvieron más cerca de abandonar (uno añade el 39 como segundo candidato), la segunda mitad del 24 (coche gris) como escena que sobra (los tres jueces vigentes), la fractura de Coro «concedida», Tomas «bisagra sin persona», el tic de anteposición participial (M4b) «como un metrónomo», el registro institucional homogéneo (Mats/Henrik/TKS/ministerio: «el mismo dialecto de cláusula»), y una escena que falta: **Maja frente al locutorio** («Maja no solicitó acceso», 39, resuelto en cinco palabras: «el centro moral del libro merece una escena, no una línea» — hallazgo nuevo, no previsto en el plan) y una escena de Jean y Maja vivas / la sesión de apoyo (N1 lo cubre).
- **Consecuencias para los objetivos:** con esta baseline, el objetivo global ≥ 9,0 está a +0,5 y solo dos ejes quedan bajo el suelo de 8,5 (Diálogo 8, Ritmo 7,5). El listón numérico se ha vuelto más alcanzable por benevolencia del juez, no por mérito del texto: por eso la salvaguarda decisiva de vF sigue siendo la **A/B ciega** (v0 vs vF con jueces mixtos, preferencia por eje) y la regla de que **ningún eje caiga > 0,5 respecto a esta baseline** en ninguna oleada. A0 propone además exigir en la A/B ciega **victoria (no empate) en Ritmo, Personajes y Trama**, los tres ejes que motivan la revisión.
- **Nuevo hallazgo para las OT (sin gate: A0 lo asigna):** la escena de Maja frente al locutorio (39/40) —dramatizar la renuncia en vez de resumirla— encaja en **OT-39** (E +200, «respiración en vistas») o como beat de **OT-40**; A2 lo dimensionará al arrancar W4/W5 (opción: 39:«Maja no solicitó acceso» → una escena breve ≤ 200 palabras vista desde fuera, sin que Maja hable de sí; contención T3). Se anota en `informes/estado-proceso.md` como pendiente de W4.

## 3. Regla operativa

Todo hito de puntuación se mide con este jurado (A6-1/2 `claude-opus-5` max, A6-3 `claude-opus-4-8` high) vía `critica-fria.sh`; en cada hito un crítico adicional relee v0 como control de deriva (§7.1). Los objetivos absolutos de vF (§0 del plan) se mantienen: global ≥ 9,0 y suelo ≥ 8,5, medidos con este jurado; anti-regresión: caída > 0,5 respecto a esta tabla → revert de la oleada.

## 4. Actualización 2026-08-17 · A6-3 pasa a `gpt-5.6-sol` (jurado mixto de dos familias)

**Decisión de autor del 2026-08-17** (`informes/registro-gates-autor.md`): A6-3 deja de ser `claude-opus-4-8` y pasa a **`gpt-5.6-sol` (OpenAI, esfuerzo max)**, ejecutado con `herramientas/critica-fria.sh --motor codex`. Motivo: tras G-A1 escribían y juzgaban modelos de la misma familia, así que la diversidad de conjunto que justifica A6-3 en §2.5 era nominal. Protocolo de aislamiento, sonda que falla cerrada, salvedades y prueba de aptitud: `informes/d1-aislamiento.md` §5. Informe: `informes/a6-v0-critico-sol-frio.md`.

| Eje | opus-5 n.º 1 | opus-5 n.º 2 | **sol-5.6 (A6-3 nuevo)** | **Mediana (baseline vigente)** | opus-4-8 (A6-3 anterior) | Mediana anterior |
|---|---:|---:|---:|---:|---:|---:|
| Premisa | 8,5 | 8,5 | 9,5 | **8,5** | 9 | 8,5 |
| Estructura | 8,5 | 8,5 | 8,5 | **8,5** | 8,5 | 8,5 |
| Prosa | 8,5 | 8,5 | 9 | **8,5** | 8,5 | 8,5 |
| Diálogo | 8 | 8 | 8,5 | **8** | 8,5 | 8 |
| Personajes | 8,5 | 8,5 | 9 | **8,5** | 8 | 8,5 |
| Mundo | 9 | 9 | 9 | **9** | 8,5 | 9 |
| Ritmo | 7,5 | 8 | 7,5 | **7,5** | 7 | 7,5 |
| Trama | 8,5 | 8,5 | 8,5 | **8,5** | 8 | 8,5 |
| Duelo | 9,5 | 9,5 | 9,5 | **9,5** | 9 | 9,5 |
| Tema | 9 | 9 | 9 | **9** | 9 | 9 |
| **Global** | 8,5 | 8,5 | 8,5 | **8,5** | 8,5 | 8,5 |

**La mediana no se mueve en ninguno de los once ejes.** El cambio de jurado no altera la baseline de anti-regresión (§7.3) y no obliga a repetir nada: las cifras del apartado 1 siguen vigentes tal cual, ahora con un juez de otra familia dentro. Sin veto en Duelo (los tres jueces responden «no» a la pregunta obligatoria).

**Lo que aporta el juez nuevo, más allá de la nota:** coincide en el suelo (ritmo 7,5 exacto), en el registro «ensayístico» compartido por Astrid/Maja/Jean/Jessie, en los secundarios instrumentales y en el 24 como escena que sobra; **y pide, por su cuenta, una escena doméstica de duelo sin interfaces** («la mañana posterior a la cuarta nota»), que es la misma deuda que el jurado opus-5 formuló como «Maja frente al locutorio». Dos familias de modelos, sin contacto entre sí, señalan el mismo hueco: eso deja de ser opinión y pasa a ser dato para W4/W5. Divergencias: sol considera que **el clímax se gana** (los opus-5 lo discutían por la fractura de Coro) y es más generoso en premisa, prosa y personajes (+0,5/+1).

**Regla operativa actualizada:** todo hito se mide con A6-1/2 `claude-opus-5` (max) + A6-3 `gpt-5.6-sol` (max, motor codex), mediana por eje. La **A/B ciega final de §7.3 no usa codex**: los dos manuscritos completos (~265k tokens) no caben en su ventana de 272k; se ejecuta con jueces Claude.
