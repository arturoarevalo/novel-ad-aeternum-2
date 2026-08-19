# Plan W10 · fase autónoma

**Autorizada por el autor el 2026-08-19.** A0 la ejecuta **sin intervención humana**, iterando cuantas veces haga falta, y entrega al final un informe detallado.

---

## 1. El objetivo, y lo que la evidencia dice de él

**Objetivo: 9,0 en los diez ejes y en la nota global.**

**Lo que hay que saber antes de empezar.** En **48 lecturas frías** de todas las versiones del libro, v0 incluida:

| eje | máximo jamás | veces ≥ 9 |
|---|---:|---:|
| duelo | 9,5 | 47 |
| tema | 9,5 | 46 |
| premisa | 9,5 | 16 |
| mundo | 9,0 | 15 |
| prosa | 9,0 | 13 |
| personajes | 9,0 | 10 |
| diálogo | 9,0 | 2 |
| **estructura** | **8,5** | **0** |
| **trama** | **8,5** | **0** |
| **ritmo** | **8,0** | **0** |
| **global** | **8,5** | **0** |

**Cuatro ejes no han llegado a 9 ni una sola vez**, y son los cuatro estructurales. La nota global **nunca ha superado 8,5 en ninguna lectura de ninguna versión**, y la rúbrica la define como «un juicio ponderado, no un promedio», así que no sube por aritmética.

**Esto no es motivo para no intentarlo: es el mapa de dónde está todo el trabajo.** Los seis ejes que sí alcanzan 9 se movieron con trabajo de línea, que ya está hecho. Los cuatro que no, solo se mueven con estructura — y la estructura es exactamente lo que esta fase desbloquea por primera vez.

**Lo que la fase debe entregar aunque no llegue a 9: la respuesta a por qué.** Un «no se puede» documentado con intervenciones probadas y medidas vale más que un 8,5 sin explicar.

## 2. Qué se puede hacer, que es casi todo

**Cae la protección estructural.** Se pueden **fundir, partir, mover, cortar y escribir capítulos**. Se pueden abrir los diez ficheros que eran `proteccion: total`. Se puede reescribir prosa del autor. Se puede cambiar la división en partes.

Los hashes de `protegidos/hashes.json` **dejan de ser cerradura y pasan a ser registro**: sirven para saber en cualquier momento qué ha cambiado respecto de v0, no para impedirlo. `herramientas/proteger.sh baseline --rebaseline --gate "W10: <motivo>"` tras cada cambio consciente.

**Se puede modificar cualquier herramienta y cualquier agente**, y crear los que hagan falta. Once instrumentos de este proyecto resultaron medir algo distinto de lo que decía su nombre; suponer que los que quedan están bien sería el duodécimo error.

## 3. Lo único que no cae: el perímetro de sensibilidad

**`biblia/b7-perimetro.md` sigue vinculante y el veto de A7 sigue siendo absoluto.**

No es una restricción de oficio, y por eso no cae con las demás: **el libro le promete al lector, en su primera página, que el acto no se describe en ninguna de sus páginas.** Esa promesa está firmada en `capitulos/00-aviso.md`, congelada por hash, y es lo único de todo este aparato que habla con alguien que no es el autor. Una fase que puede cambiarlo todo tiene que no poder cambiar eso.

En concreto siguen rigiendo: las nueve reglas, las cinco cuentas cerradas, la regla de sucesión y las seis condiciones de W9 del perímetro consolidado. **«Despedida» no se abre. La discusión de Kongsbakken no se escribe. La bolsa no reaparece.**

**Todo lo demás es negociable, y A7 puede levantar sus propias condiciones si el texto se lo demuestra** — ya lo hizo dos veces en W7, retirando dos reglas suyas por estar mal escritas.

## 4. El bucle

Cada iteración:

1. **`herramientas/w10-campana.sh <etq>`** — compila, sondas de aislamiento, tres críticos + **control de deriva sobre v0 el mismo día**, medianas, guardia de regresión y actualización del estado.
2. **Diagnosticar** con `a2-arquitecto` sobre lo que digan los abandonos y los ejes bajos.
3. **Intervenir** con A3a/A3b/A4 según el tipo.
4. **Verificar**: A5 continuidad, **A7 siempre que se toque su perímetro**, `proteger.sh`, `validar-frontmatter.sh`, `medir.sh`.
5. **Volver a medir y decidir**: si el eje objetivo no sube **más allá del ruido de ±0,5**, la intervención se **revierte** y se anota en `callejones_sin_salida`.

`herramientas/lib/w10_estado.py` mantiene la memoria entre sesiones: hipótesis probadas, veredictos, mejor versión conocida. **Se consulta al arrancar, siempre.**

## 4b. La iteración 0 es DIVERGENTE, y es obligatoria

**Esta sección existe porque sin ella el plan estaba mal.** El bucle de §4 es excelente para no engañarse y no sirve para encontrar nada: ejecutaría el *backlog* de los críticos, que lleva seis oleadas sin mover los cuatro ejes estructurales. **Trabajar esa lista es lo más probable que falle**, porque son diagnósticos («el centro se hunde»), no recetas con garantía. Antes de tocar nada, hay que generar hipótesis que nadie ha tenido.

**No se ejecuta ninguna intervención del backlog hasta cerrar la iteración 0.**

### 4b.1 · Generación divergente: seis ángulos independientes

Seis instancias de `a2-arquitecto` **en paralelo y sin verse entre sí**, cada una con un ángulo distinto y prohibido leer los informes de crítica anteriores (para que no reproduzcan el backlog):

1. **El lector que abandona.** El punto de abandono está hoy en el 62 % y los tres son capítulos nuestros. ¿Qué hace falta para que no haya ninguno?
2. **El libro que quiere ser.** ¿Qué promete esta novela en sus primeras cincuenta páginas y no cumple? La respuesta no es un defecto: es una promesa.
3. **El corte.** Si hubiera que quitarle **quince mil palabras**, ¿cuáles? La restricción de banda está suspendida para esta pregunta. Se pregunta por el libro de 65.000 palabras que hay dentro de éste.
4. **La forma.** ¿Es la estructura de cuatro partes con cuenta atrás la forma correcta para esta historia? ¿Qué otra forma la serviría mejor, y qué costaría?
5. **El clímax.** Llega en el 85 % y se «gana». ¿Está en el sitio correcto? ¿Qué pasaría si llegara antes, o después, o dos veces?
6. **El editor.** ¿Qué pediría un editor que compra este libro y no ha visto ninguna de las seis oleadas?

Después, **panel de jueces**: cada propuesta se puntúa por otras instancias, se sintetiza la ganadora y **se injertan las mejores ideas de las descartadas**. Lo que sobreviva entra al bucle de §4 con su medición.

### 4b.2 · La pregunta que nadie ha hecho a un lector frío

**Las 48 lecturas frías fueron todas de rúbrica: preguntaban qué está mal.** Ninguna preguntó qué podría ser. Se lanza una campaña nueva con la pregunta abierta, en frío real y sin la rúbrica:

> «Este libro puntúa 8,5. **¿Qué le falta para ser un 10?** No me digas qué está mal: dime qué le falta. Y si tu respuesta es que ya es lo que puede ser, dilo.»

Y una segunda, dirigida al eje que nunca se ha movido:

> «La nota global no es el promedio de los ejes: es un juicio ponderado. **¿Qué tendría que cambiar para que subieras la global, aunque no cambiara ningún eje?**»

### 4b.3 · Probar si 8,5 es techo del libro o del instrumento

**La global lleva 48 lecturas sin pasar de 8,5, en todas las versiones, incluida v0.** Nadie ha comprobado nunca si eso es una propiedad del libro o de la rúbrica y el jurado. Antes de reescribir un libro para mover un número, hay que saber si el número se puede mover:

- Puntuar con la rúbrica **una novela publicada y reconocida** del mismo género, en frío y con el mismo jurado. Si también sale 8,5, el techo es del instrumento y **el objetivo de la fase hay que replantearlo, no perseguirlo**.
- Puntuar v0 **con la rúbrica reformulada** (anclas explícitas de qué es un 9 y un 10). Si v0 sube sin cambiar una coma, el problema era la vara.

**Este experimento es barato y puede ahorrar la fase entera.** Va primero.

### 4b.4 · Apuestas grandes antes que pequeñas

Revertir cuesta un `git revert`; iterar sobre cambios pequeños y seguros que **no pueden** mover un eje estructural cuesta la fase. **Cuando haya duda entre una intervención de 200 palabras y una de 5.000, se prueba la de 5.000**, se mide, y se revierte si no paga. El riesgo real de W10 no es romper el libro —eso es reversible— sino **gastarse en cambios demasiado tímidos para mover lo que hay que mover.**

---

## 5. Reglas de método que sobreviven de las seis oleadas

Estas no son burocracia: cada una nació de un error concreto y caro.

1. **Medir con control.** El mismo juez varía **hasta un punto entero sobre texto idéntico**. Sin control de deriva del mismo día, una medición no dice nada. Cinco veces un control cambió la lectura de un resultado.
2. **Los números localizan; solo la cita literal instruye y verifica.**
3. **El paragrafado es énfasis.** Vaciar, partir, fundir, reordenar o insertar al lado de una línea protegida cuenta como modificarla. **M9 ve dentro del ancla y es ciego fuera de sus extremos.**
4. **Ninguna métrica dirige trabajo hasta que alguien haya leído a mano un capítulo entero contra su salida.** Los once instrumentos rotos fallaban **a la baja y en silencio**: producen dictámenes tranquilizadores.
5. **Declinar es una respuesta**, y frecuentemente la correcta.
6. **Decir qué se pierde**, no solo qué se gana.
7. **El criterio final no es la métrica: es dónde deja de leer la gente.** El punto de abandono se ha movido del 40 % al 62 % del libro y ningún eje de la rúbrica lo mostró.

## 6. Cuándo parar

Se para cuando ocurra lo primero de:

- **Los once ejes en 9,0** con control de deriva que lo respalde.
- **Tres iteraciones consecutivas sin una sola mejora fuera del ruido.** Entonces el resultado de la fase es el diagnóstico de por qué, que es un entregable legítimo.
- **Una regresión en `duelo` o `tema`**, que son los dos ejes donde el libro ya está en 9,5 y son su asunto. Si una intervención los baja, se revierte y esa vía se cierra.
- **Un veto de A7 que no admita arreglo mínimo.**

## 7. El informe final

`informes/w10/informe-final.md`, con: iteraciones y sus veredictos, qué movió cada eje y qué no, callejones sin salida y por qué, comparación completa contra v0 y contra vF, texto cambiado en volumen y en sitio, herramientas y agentes creados o corregidos, y **una respuesta honesta a si el objetivo era alcanzable**.
