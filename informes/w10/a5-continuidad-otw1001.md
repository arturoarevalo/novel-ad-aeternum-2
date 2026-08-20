# A5 · Continuidad de OT-W10-01 · rama `w10-it1` (commit `0f0e4cc`)

**2026-08-19.** Verificado contra el `cap-31` original en `main`, el `cap-32` fundido, los
vecinos, las dependencias hacia delante (`cap-34`, `cap-35`, `cap-38`, `cap-46`, `cap-22`,
`cap-10`, `cap-20`), la Biblia (`b1`, `b3`, `b4`), `protegidos/spans.json` y el manifiesto.
Diff de cuerpo, fechas por calendario y compilación.

*(A5 no pudo escribir este fichero por su configuración de operación; lo persiste A0 con su
contenido íntegro y sin interpretar.)*

## Veredicto: **NO PASA para merge**, sin exigir prosa nueva

La excisión es limpia y el diff confirma exactamente E-1…E-5, D-1, D-2 y el cambio de la
réplica, sin ediciones colaterales. Pero quedan tres hallazgos mayores.

## Hallazgos

**H1 · mayor · la restitución de la cuenta ya no está sembrada.**
`cap-32:217` «antes de que la cuenta **se cerrara otra vez**» · `:229` «—Ha llegado **otra
vez**.» · `:237` «—La segunda es de las **once cincuenta y ocho**.»
La escena 1 excisa era la única que mostraba la cuenta **restituida** («admitió las
credenciales de Nora al primer intento»). Y `b4:135` ya lo había marcado: «nunca se dice en
v0 que la cuenta se restituya; N4 **presupone una restitución que hay que sembrar antes**».
Verificado que `cap-20` y `cap-22` **no la siembran** (`cap-20:167` la muestra aún
suspendida, entregas en papel). El texto sigue afirmando la re-clausura; la reapertura ya no
consta en ninguna página.

**H2 · mayor · D-1 era el ancla canónica de MEC-25.**
Según `b3:339`, el párrafo borrado —«El aviso no traía hechos. Ni fechas… Traía una
categoría, una referencia y una lista de destinatarios cerrada.»— es el re-ancla de MEC-25,
«la única mecánica nueva de W3». La mecánica **sobrevive por demostración**
(`cap-32:23-31`, `:43`), pero su enunciado-definición ya no existe.

**H3 · mayor · los ripples obligatorios de la orden no se ejecutaron.**
OT §10/§12 exige actualizar `b3` y `b4` en el mismo commit. El commit tocó `b0`, `b7`,
`metadatos` y `spans.json`, pero `b1`/`b3`/`b4` tienen **cero menciones** de la fusión.
`b4` CH-27 cita «11:52» (excisado) y «restitución a primera hora» (excisada); `b1` sigue
describiendo Interferencias como capítulo separado; `b3` ancla a líneas de un fichero
borrado.

**H4 · menor.** «—La segunda es de las once cincuenta y ocho»: su «primera» ya solo se
refiere (`:233` «La captura de esta mañana la hizo la tutora»), no se muestra. Sin
contradicción. **Posible ambigüedad protegida (Ap. A §3): A5 no propone resolverla.**

**H5 · menor, preexistente.** La distinción papel #3/#4 (ambos «del instituto») es sutil.
El bloque `:213-241` no lo tocó la orden. No lo introduce OT-W10-01.

## Lo que queda acreditado

- **Reloj del 3-ene:** sin referencia colgada. 11:40 y 11:52 no se citan en ningún otro
  capítulo; «11:58» es único; «cinco de diciembre» queda anclado en `cap-20:169`.
- **Cuatro documentos / tres actuaciones:** contados de nuevo. `cap-38:93` y `cap-35:131`
  («los cuatro papeles del tres de enero») **siguen siendo verdad. Ninguna cifra hay que
  editar** — confirma la orden y refuta la tabla de `w5-cap-n4` §4, que era el coste de la
  Opción B y no de la A.
- **«—Ha llegado otra vez.»** se sostiene: la segunda línea suprimida solo vivía en la
  escena 1, y al caer 11:52 desaparece incluso la tensión latente 11:52/11:58.
- **Marzo y Kongsbakken:** ningún texto posterior depende de los datos que se llevó la
  escena 1. No hay «veintiocho», «impreso» ni «tutela» aguas abajo ligados a la repesca.
- **La costura funciona.** POV continuo (Maja), elipsis salvada por «quedaban dos horas de
  carretera y un desvío sin salar». Bolsas coherentes. C-1 y C-2 bien colocadas.
- **Cronología:** `cap-29` 2-ene · `cap-30` y el fundido 3-ene · `cap-33` 5-ene. Verificado
  por calendario: **2-ene-2061 domingo, 3-ene lunes**, coherente con «Nos siguieron ayer» y
  «el domingo por la mañana». *(Corrige a A0: `cap-30` es del 3, no del 2.)* AK-7 operativa.

---

## Resolución de A0

**H1 · se acepta la implicación y se documenta. No se siembra nada.**

«La habían impreso en el instituto antes de que la cuenta **se cerrara otra vez**» le dice
al lector que la cuenta había vuelto a abrirse. Una cosa solo puede cerrarse otra vez si se
abrió. Es la clase de inferencia que este libro le pide al lector en cada página, y es la
misma economía por la que `Despedida` no se abre y funciona.

Y sembrar un beat de restitución sería **añadir función**, que es exactamente lo que la
iteración 0 concluyó que hay que dejar de hacer: el hueco no se tapa con una escena cuya
única razón de ser es tapar un hueco. Se anota en `b4` como restitución fuera de página.

**H2 · se acepta, y es el efecto buscado, no un daño colateral.**

D-1 era «la definición que llega después de la demostración». Que MEC-25 sobreviva solo
demostrada —y ya no enunciada— es precisamente la operación de la fase. Lo que hay que
arreglar no es el texto: es que `b3` apunte al sitio correcto.

**H3 · es un fallo mío y se ejecuta.** La orden lo exigía en el mismo commit y no lo hice.
