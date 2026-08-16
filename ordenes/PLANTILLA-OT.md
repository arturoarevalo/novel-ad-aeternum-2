# PLANTILLA de orden de trabajo (Fase 2 · A2) — copiar íntegra en cada `ordenes/OT-NN.md` / `OT-Nk.md`

Reglas de la plantilla: todos los encabezados se conservan (si una sección no aplica, se escribe «No aplica» y por qué). Las posiciones se dan por **ancla textual literal** (una frase corta del capítulo, entre comillas angulares) y, si ayuda, número de párrafo del cuerpo; nunca por número de línea del fichero (cambia al editar). Ninguna OT contiene prosa nueva: contiene qué debe conseguir la inserción, con qué límite y con qué prohibiciones. Fuentes de verdad: el texto de `capitulos/`, `biblia/` (B1–B7), `protegidos/spans.json`, `informes/d1-diagnostico.md` §10 (criterios) y §11 (hallazgos), `informes/g0-gate.md` §3, `informes/d1-a7-biblia.md` (condiciones A7), `ordenes/tabla-5-1.json` (índice).

---

# OT-NN · Capítulo NN «Título» — [P | R | E | RW | N]

## 0. Cabecera

| Campo | Valor |
|---|---|
| OT | OT-NN |
| Capítulo · fichero · orden de lectura | NN · `capitulos/cap-NN.md` · NN (o decimal para N) |
| POV · fecha (frontmatter) | … |
| estado_plan · proteccion | … · total / nucleo / no |
| Δ objetivo · presupuesto vF · banda de aceptación | +NNN · NNNN palabras · [mín–máx] (± 15 % del Δ, ± 50 mín.; P = diff 0) |
| Oleada · escritor · editor de línea | W2/W3/W4/W5 · A3a / A3b · A4 |
| Gates que dispara | A7 (T7: caps. 1–10, N1, N3, 38, recursos, cualquier mención al acto) · A5 (M7, T6) · A8 (M1–M10) |
| Estado de la OT | pendiente |

## 1. Diagnóstico (cifras de D1 y lectura de A2)

- M1 v0 únicos/1.000 (ocurrencias) → objetivo · M2 mecánicas nuevas v0 · M4 cierres-objeto del capítulo (censo B6) · M4b % · M5 % diálogo / tramo máx. sin diálogo · lector frío v0 (nota, regla, dónde, términos opacos) si es capítulo de Jean · presencia familiar (si aplica).
- Qué falla y qué NO falla (2–5 frases; con citas breves). Lo que dijeron los críticos fríos y la crítica de referencia sobre este capítulo, si lo mencionan.

## 2. Función del capítulo en vF (una frase) y lo que lo hace único respecto a sus vecinos

(Obligatorio en 13/15/17/21 y en N1–N6: qué tiene este capítulo que ningún otro tiene — D1 §11.c.)

## 3. Intervenciones (numeradas)

Para cada una:

- **I-k · ETIQUETA** (`ORIENTACIÓN` | `INTERIORIDAD` | `TENSIÓN` | `AGENCIA` | `TEXTURA` | `PAGO` — una sola por inserción; sin etiqueta = rechazo).
- Posición: ancla textual literal (antes/después de «…»); escena n.º; párrafo aprox.
- Presupuesto: +NN palabras (o −NN si es recorte; los recortes también se listan y justifican).
- Técnica: para Jean, tipo Ap. D (D1 recuerdo ≤ 40 pal. · D2 caso concreto · D3 marcador temporal · D4 corte a familia · D5 regla enunciada una vez, sin la fórmula «Regla:» salvo en 8 y N5); para familia, contención T3 y guía de voz Ap. C/B2.
- Objetivo de la inserción (qué debe saber/sentir el lector después que antes no sabía; qué plantado paga si es PAGO, con su ID CH-NN).
- Prohibiciones locales (qué no puede decir, qué no puede explicar, qué voz no puede usarse, qué mecánica NO se introduce).

## 4. Prohibiciones del capítulo

- Spans protegidos (`protegidos/spans.json`): lista de IDs con su ancla de inicio/fin (literal) — diff = 0 dentro del span. Si una intervención NECESITA tocar un span, se marca «REQUIERE LIBERACIÓN EN G-A1» con la justificación (no se toca hasta entonces).
- Líneas capitales «intactas» de la tabla 5.1 y B5 (citarlas).
- Ambigüedades protegidas (Ap. A §3) que rozan este capítulo.
- M2: mecánica nueva permitida (máx. 1; nombrarla si la hay: MEC-… de B3 §20) y mecánicas PROHIBIDAS aquí.
- Carta F (si aplica): puntos concretos y lo que A7 exigió en `informes/d1-a7-biblia.md` / B7 §6.
- Lista negra B6b y tics: cierres-objeto (no añadir; si el capítulo está en B6 §5.6, qué cierre se varía y cómo), subordinadas antepuestas (M4b), «Regla:» solo en 8/N5.

## 5. Ripples

- Salientes: qué cambia en otros capítulos por esta OT (capítulo, qué, quién lo ejecuta, en qué oleada).
- Entrantes: qué llega aquí desde otras OT (N1–N6, R2, W2), con la referencia a la OT origen.

## 6. Criterios de aceptación (medibles; los de D1 §10 + tabla 5.1)

- Palabras: banda. M1: ≤ … (únicos/1.000) [ocurrencias como indicador]. M2 ≤ 1. Lector frío: ≥ …, «regla en 1 frase» y «dónde ocurre» si aplica. M4: sin cierres-objeto nuevos (o el cambio previsto). M4b ≤ 8 %. M6b (si el capítulo lleva réplicas nuevas de Nora/Jessie/Maja/Alana/Astrid/Mats: guías Ap. C aplicadas). M7: fechas/horas/aritmética que este capítulo toca. M9: hashes intactos. M10: CH-NN pagados aquí.
- Cualitativos: las líneas/dinámicas «intactas» de la tabla 5.1; test de A7 (si aplica); «¿parece del mismo autor?» para N (B6 §6 plantilla).
- Cómo se verifica: comandos (`herramientas/medir.sh <et>`, `critica-fria.sh lector-frio compilado/extractos/<et>/cap-NN.md`, `proteger.sh verificar`, `sensibilidad.sh`).

## 7. Checklist de verificación (A5 · A7 · A8) — casillas

- [ ] A5: continuidad (fechas B1, cifras B3 §2/§14, terminología jurídica, mareas/AK-7…) — puntos concretos de este capítulo.
- [ ] A7: (si aplica) revisión de tono y contenido; frases autorizadas por escrito si las hay.
- [ ] A8: métricas del capítulo vs objetivo; compilado y extracto regenerados.

## 8. Notas para el escritor (≤ 150 palabras)

Lo que A2 quiere que el escritor sepa antes de empezar: el latido del capítulo, qué NO hacer aunque parezca buena idea, dónde está el riesgo de sobreexplicar.
