# Gate de W7 · verificación

**A0 · 2026-08-19.** **48 capítulos · 79.772 palabras · EN BANDA.**

| métrica | |
|---|---|
| **M7** cronología | **0 errores** |
| **M8** banda | **EN BANDA** (80.000 ± 1.000) |
| **M9** protegidos | **OK · 10 ficheros · 129 spans** |
| **M10** Chéjov | **100,0 %** (83/83) |
| frontmatter | 0 avisos · 0 desincronizados con el manifiesto |
| cuotas | **= recuento real, +0** |

## Lo hecho

- **La renumeración única del plan:** 48 capítulos correlativos, partes **1–12 / 13–24 / 25–36 / 37–48**, doce cada una. **Ninguna prosa movida** (diff de cuerpos w6↔w7 = 0).
- **A5, verificación total:** pasa. Toda la aritmética del libro correcta, las diecisiete horas del clímax en orden, y a la pregunta directa — *«¿queda algún hilo que el libro plante y no recoja, o que recoja sin plantar?»* — **no hay ninguno**.
- **A7, paquete final: APROBADO, cero veto, cero correcciones sobre `capitulos/`.** Leyó el compilado entero, no un diff.
- **Los dos paratextos congelados por hash** tras llevar sin él desde F0. Añadida la viñeta de LEVE para quien ha perdido a alguien.
- **Vector de reinserción neutralizado** en la Biblia, más dos restos que A5 no podía ver porque vivían en notas de diseño.
- **M10 pasa de infravalorado a 100 %**: siete Chéjov que el texto ya pagaba seguían marcados pendientes.

## Lo que W7 encontró y no arregló

**La prueba de autoría sobre `cap-n7` falla, con control.** Cuatro de cinco lectores en frío separan «El salero», tres citando la misma réplica; con una analepsis de v0 en el mismo hueco, cuatro de cinco dicen NINGUNO. **Lo que se separa es ingenio, en un libro que no hace ingenio.** Decisión de A0: **no se toca**, y va al autor en G-A3. Detalle en `w7-autoria-ciega.md`.

Es **el único criterio de aceptación del proyecto que se incumple sobre el texto** y no sobre una métrica.

## Los dos instrumentos de W7, y el balance

**Noveno:** `actualizar-metadatos.sh renumerar --w7` remitía desde F0 a un flag de `inyectar-frontmatter.sh` **que nunca se implementó**. El recordatorio existía y la vía no: manifiesto renumerado y frontmatter no, **41 de 48 desincronizados, y ningún validador lo veía porque cada uno mira el suyo.**

**Décimo:** el validador acusaba a los capítulos nuevos de tener `orden_lectura` entero «se esperaba decimal **hasta W7**» — regla correcta hasta W7 y falsa después, que acusaba a los siete capítulos nuevos justo por haber hecho bien la renumeración.

Y un tercer efecto que solo se veía compilando: renumerar sin alinear `orden_lectura` **movía capítulos de parte en silencio** (24.006 / 24.189 / 22.511 / 9.066 en vez de la distribución real).

**Balance del proyecto: diez instrumentos corregidos, todos del mismo género — hacían lo que decía su código y no lo que decía su nombre, y los diez fallaban a la baja, en silencio.** Ninguno produjo jamás una alarma: producían dictámenes tranquilizadores.

## Y el perímetro, consolidado

A7 pasó de **88 condiciones a nueve reglas** en `biblia/b7-perimetro.md`, escrito para quien no sabe quién es A7. Retiró seis, **dos por equivocadas**, y degradó ocho fuera del registro de veto. Su diagnóstico sobre sí mismo: **el 25,6 % del libro estaba cerrado a intervención, 10,5 puntos por decisión suya sola, y 29 de sus 88 condiciones decían «pasa por mi gate». «Yo era el gate.»**
