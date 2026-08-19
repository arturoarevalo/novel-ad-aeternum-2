# A5 · W9 · La cadena de adhesiones del clímax (cap-36 / cap-37)

**Rama:** `w9-huella` · **Encargo:** A0 (a raíz de un hallazgo de A4 al aclarar el léxico máquina).
**Alcance:** continuidad/verosimilitud. No toco capítulos ni Biblia. Δ ≈ 0; nada estructural.
**Fuentes cotejadas:** texto de `cap-36.md` y `cap-37.md`; `biblia/b3-canon-sistema.md` (§5-6, D1); `biblia/b4-ledger-chekhov.md`; `biblia/b5-lista-protegida.md`; `protegidos/spans.json`; `biblia/b7-perimetro.md` (9 reglas + 5 cuentas).

---

## 1 · El hecho: ¿contradicción o lectura que concilia?

**Las dos citas (literales, verificadas):**

- `cap-36:17` — «**La primera adhesión**, de una continuidad médica, entra con una condición de cuidado… Tras el cierre no podrá revisarlas por separado.» → adhesión nº 1 = **continuidad médica**, que **entra y se queda** (no se retira).
- `cap-36:19` — «Una **segunda** continuidad se detiene, **retira su adhesión** y recupera lo aún no entregado. Jean deja el lugar vacío y conserva la retirada…» + `cap-36:21` «Si las condiciones cambian antes del cierre, esa continuidad recibirá otra ventana.»
- `cap-37:87` — «La continuidad que había retirado **la primera adhesión** volvió con condiciones revisadas y confirmó **la nueva** sin borrar la retirada anterior.»

**Los eventos SÍ concilian; las etiquetas NO.**

- **A nivel de trama no hay contradicción.** La médica (adhesión nº 1) entra y permanece. Una segunda continuidad se retira y, cambiadas las condiciones, vuelve. `cap-37:87` describe **el regreso de esa segunda continuidad**. Lo confirma el canon: **B3 §6, fila «de revisión de adhesión»** trata `cap-36:21` y `cap-37:81` como **una sola** continuidad que se retira y recibe «otra ventana» para volver. El ledger (B4) no aporta un ordinal en contra. **No es un agujero de causalidad.**
- **A nivel de rótulo hay contradicción real, orientada al lector.** `cap-36` numera: adhesión **nº 1 = médica** (que se queda) y continuidad **nº 2 = la que se retira**. `cap-37:87` llama **«la primera adhesión»** a la que **se retiró**. Un lector que lleve la cuenta lee «la primera adhesión» = la médica de `cap-36:17` → concluye que **la médica se retiró**, cuando `cap-36:17` dice que **entró y se quedó**. El ordinal choca: lo que `cap-36` marca «segunda», `cap-37` lo llama «primera».

**La lectura que concilia existe, pero el texto no la sostiene sin reconstrucción.**
`cap-37:87` es limpio **leído solo**: «**primera** adhesión» ↔ «**la nueva**» es el par de *una misma* continuidad en dos momentos (la que retiró y la que confirma). El problema es que `cap-36` **ya adjudicó** la etiqueta «primera adhesión» a **otra** continuidad (la médica) y numeró «segunda» a la que se retira. Para conciliar, el lector tiene que **re-escopar** «primera» de un cómputo global (el de `cap-36`) a un cómputo interno de esa continuidad. Nada en la página señala ese cambio de marco; al contrario, `cap-36` **ceba** el cómputo global con «primera adhesión» + «segunda continuidad». Es exactamente la reconstrucción que el lector beta dice no poder hacer.

---

## 2 · Tabla de hallazgos

| # | Sev. | Cap:línea | Cita breve | Regla/fuente | Corrección mínima |
|---|------|-----------|-----------|--------------|-------------------|
| H1 | **mayor** | `cap-36:17` ↔ `cap-37:87` | «La **primera** adhesión, de una continuidad médica, entra…» vs. «la continuidad que había retirado **la primera** adhesión volvió…» | Colisión de ordinal: la «primera adhesión» de 36 entra y se queda; la «primera adhesión» de 37 fue la que se retiró. Concilia con B3 §6 (una misma continuidad), pero rompe la seguibilidad (beta final). | **Una palabra, en `cap-36:17`:** suprimir «primera». `La primera adhesión, de una continuidad médica, entra…` → **`La adhesión, de una continuidad médica, entra…`**. Ver §3. |
| H2 | menor (diagnóstico) | libro (36-38) | — | La cadena de adhesiones **no es contable**: solo se numeran dos (`36:17`/`36:19`) y hay una sola llamada por ordinal (`37:87`), justo la inconsistente. Ver §4. | No accionable en W9 (sería estructural). Se reporta para una oleada futura. |
| — | (dato) | `b5:279` | «`S37-597` \| cap-37.md:**87**» | El span `S37-597` arranca, por literal (`protegidos/spans.json`), en «Jean excluyó la revisión tardía…» = **línea 91**, no 87. El **87** es número de línea envejecido (B7-P §2 avisa de esto). | Informativo para A0/A7: la frase de `37:87` **no** está bajo hash, pero sí en `cap-37` (núcleo + perímetro). No se toca igual. |

No hay hallazgos bloqueantes: los eventos y el canon B3/B4 son consistentes.

---

## 3 · El arreglo mínimo (una palabra, en el 36, sin span)

**Ubicación libre de protección.** Los únicos spans de `cap-36` son `S36-retiro` (175-179) y `S36-cierre` (207-209); las líneas 17/19 **no** están bajo hash. Es donde A4 acaba de trabajar.

**No se puede tocar `cap-37`:** núcleo, con `S37-declaracion`/`S37-acta`/`S37-muchas`/`S37-597`/`S37-llave` y perímetro A7 (R2, R7·9, C-…). El regreso de la continuidad y su rótulo «primera adhesión»/«la nueva» quedan **intactos**.

**Recomendación (H1):** en `cap-36:17`, **suprimir la palabra «primera»**:

> `La primera adhesión, de una continuidad médica, entra con una condición de cuidado…`
> → `La adhesión, de una continuidad médica, entra con una condición de cuidado…`

**Por qué basta y por qué es el punto correcto:**
- Elimina el **único** «primera adhesión» de `cap-36`, que es el rótulo que compite con el de `cap-37:87`. Sin él, «la primera adhesión» de `37:87` queda **sin antecedente rival** y se lee sin ambigüedad como *la primera de esa continuidad* (frente a «la nueva»).
- **No orfana** el «Una **segunda** continuidad» de `cap-36:19`: la continuidad médica sigue siendo la **primera mencionada**, así que «segunda» conserva su antecedente narrativo.
- **Arriba-inerte**: el ordinal «primera/segunda» de las adhesiones **no** es canon (B3 §6 cita `36:21`/`37:81`, no `36:17`; no numera adhesiones) ni entra en la aritmética M7 (4.096 − 1.185 = 2.911 = 2.311 + 597 + 3 vive en `cap-34:85` y `cap-37:91`/`cap-38:73`, ajena a esto). B4 no lo usa como plantado.
- **Δ ≈ 0** (neto −1 palabra), no estructural, ningún span, ninguna de las 9 reglas / 5 cuentas de A7 rozada.

**Descartado:** cambiar solo `cap-36:19` «segunda» → «otra». **No basta**: dejaría en pie el «primera adhesión» de `36:17` colisionando con el de `37:87`; la médica seguiría pareciendo la que se retira.

---

## 4 · La pregunta de fondo: ¿es *seguible* la cadena?

**No con honestidad: la cadena no es contable por un lector atento, y el arreglo no la vuelve contable —solo deja de prometer una cuenta que el libro no lleva.**

- El libro **numera adhesiones dos veces** (`36:17` «primera», `36:19` «segunda») y hace **una sola** llamada por ordinal (`37:87` «la primera»). Esa única llamada es, justamente, la inconsistente. Fuera de ese par, **no hay cómputo corriente**: Cuchillo (apelaciones), Nieve (tareas), las ramas de Coro, Madre y la médica operan **por origen**, no por número. Un lector no puede decir, al terminar, *cuántas adhesiones hay, quién las retira y en qué orden*.
- La densidad se agrava por **polisemia canónica reconocida**: B3 §6 (línea 121) declara «ventana» «la palabra más sobrecargada del sistema»; «margen», «origen», «salida» y la propia «adhesión» (b3-lexicon: «acuse… puede llegar antes que la decisión») cargan varios sentidos. Y en el mismo `cap-36` «adhesión» se usa en **dos registros**: las continuidades numeradas (17, 19) y, genéricamente, las correcciones de Coro que Jean *podría cerrar «como adhesiones»* (175). Es el «cuatro o cinco orígenes se cruzan y me pierdo» del beta, tal cual.
- **Consecuencia para A0/A7:** suprimir «primera» en `36:17` **resuelve la contradicción** (H1) y quita la falsa promesa de cuenta. Pero volver la cadena *seguible* —un recuento explícito de adhesiones/retiradas/regresos— sería **estructural** y, además, arriesgaría sobre-explicar el sistema (choca con el tono deliberadamente opaco de B3 y con R7). **Fuera del alcance de W9.** Queda anotado como deuda para una oleada de legibilidad, no de huella.

---

## 5 · Lo que acredito vs. lo que infiero

- **Acreditado por el texto/Biblia:** las tres citas; que la médica entra y se queda (`36:17`); que la 2.ª se retira y se le promete «otra ventana» (`36:19-21`); que B3 §6 trata esa retirada+regreso como **una** continuidad (`36:21`/`37:81`); que el span `S37-597` arranca en la línea 91 por literal (`spans.json`); que `36:17/19` no están bajo hash.
- **Inferencia (marcada):** que `cap-37:87` *pretende* referirse a la 2.ª continuidad de `cap-36` (lo respalda B3 §6, pero el nexo explícito no está en la prosa); que el lector beta se pierde *aquí en concreto* (su queja es genérica sobre orígenes cruzados; este pasaje es el caso más agudo, no está citado por él).

---

## Veredicto

**NO PASA** (por H1, severidad **mayor**): contradicción de rótulo real y orientada al lector, en el pasaje que el beta señala. Los eventos concilian y el canon es consistente, por lo que **no es bloqueante**; con la corrección de una palabra en `cap-36:17` (**suprimir «primera»**) el capítulo **pasaría**. H2 se reporta como diagnóstico de fondo, no accionable en W9.

**Devuelto a A0.**
