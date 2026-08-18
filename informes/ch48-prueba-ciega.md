# El beat de CH-48, medido: seis lecturas ciegas con control

**A0 · 2026-08-18.** A7 sugirió esta prueba sin exigirla («no es mi gate y no lo pido»). Se hace porque el criterio de aceptación de `OT-22b` es de doble filo y su segundo filo —**«si nadie nota que falta algo, también se revierte»**— no se puede resolver estimando.

## Diseño

Dos extractos **idénticos salvo por las 56 palabras del beat**, ambos con `cap-22` + `cap-23` en orden de lectura (3.689 y 3.633 palabras). Tres pases de `lector-frio` sobre cada uno, en frío real vía `critica-fria.sh`, consigna neutra de resumen: la rúbrica estándar del lector, que **no pregunta por huecos ni por nada relacionado**.

*(Nota de proceso: el primer intento falló porque puse el extracto concatenado en el scratchpad. `critica-fria.sh` **rechazó el insumo por no estar bajo `compilado/`**. La regla dura de aislamiento está implementada y **falla cerrada** — al contrario que `sensibilidad.sh --solo` y `extraer.sh`, que en W2 fallaban abiertos.)*

## Resultado

**Primer filo: pasa limpio.** Ninguno de los tres lectores con beat nombra la cuarta cosa, pregunta por ella ni la incluye en «términos no entendidos» — donde sí listan CE-K, NIDHOGG, ÆGIR, CARIES, TKS y ocho siglas más. **Nadie intenta rellenar el hueco.**

**Segundo filo: pasa, y con una separación que no esperaba.** La pregunta 3 de la rúbrica pide **la regla que gobierna el capítulo**. Es la respuesta más estructural que da el lector, y es donde aparece la diferencia:

| | formulación de la regla | «hueco» |
|---|---|---|
| **con beat · 1** | «…lo demás (una flecha entre relojes distintos, un recuerdo deducido) se descarta o **se deja como "hueco"**» | ✓ |
| **con beat · 2** | «…toda inferencia no probada se descarta o **se deja como «hueco»**» | ✓ |
| **con beat · 3** | «…toda inferencia no verificable se descarta o **se deja como «hueco»**» | ✓ |
| control · 1 | «…se marca como abierta o se descarta» | ✗ |
| control · 2 | «…lo no probado se descarta, **pero «las horas siguen ahí»**» | ✗ |
| control · 3 | «…una intuición correcta se descarta si su prueba es inválida, **pero las horas y los registros siguen valiendo**» | ✗ |

**3/3 contra 0/3.** Y la diferencia no es de vocabulario: es de **signo**. Sin el beat, los tres lectores formulan la regla en positivo —lo que sobrevive a la prueba: «las horas siguen ahí», «los registros siguen valiendo»—. Con el beat, los tres la formulan en negativo: **lo que no se acredita se queda como hueco**. Cincuenta y seis palabras cambian cuál de las dos mitades de la misma regla es la que el lector se lleva.

## Lo que la prueba NO demuestra

Los ejemplos que los lectores citan al formular la regla son **la flecha y el recuerdo de Jean**, no el beat. Ninguno cita a Nora ni el número. Así que el beat **no se percibe como escena**: opera cambiando qué mitad de la regla del capítulo queda en primer plano, sin que el lector sepa que lo hace.

Eso es exactamente lo que se le pidió —acuse de recibo, no escena— pero conviene dejar escrito que la evidencia es de **efecto**, no de **atención**. Nadie lo vio. Todos lo notaron.

## Conclusión

**El beat se queda.** Los dos filos del criterio de `OT-22b` §6.9 se cumplen con control pareado: nadie nombra lo que falta, y la ausencia sí modifica lo que el lector se lleva del capítulo.

Coste de la prueba: seis lecturas, 0,36 USD, cuatro minutos.

**Y una advertencia que vale más que el resultado.** Las tres primeras lecturas, sin control, parecían confirmar el beat por sí solas: tres lectores independientes diciendo «hueco» es un resultado vistoso. Habría sido una conclusión falsa por falta de una comparación de nueve céntimos — y de hecho, a esa altura, la evidencia disponible apuntaba a que la palabra venía de la flecha y del segundo regalo. **Es la quinta vez hoy que un control cambia la lectura de un resultado**, y la tercera que evita que A0 dé por bueno algo que no lo estaba.
