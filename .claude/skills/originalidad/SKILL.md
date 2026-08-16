---
name: originalidad
description: Verificación antiplagio antes de publicar; extrae los pasajes con más riesgo de regurgitación (versos, epígrafes, citas atribuidas, aperturas/cierres, aforismos, n-gramas raros, nombres inventados) y los busca en la web como frases exactas. Úsalo cuando el usuario diga "/originalidad", "comprueba plagio", "verifica que no hay copia" o antes de publicar comercialmente. No edita nada.
---

# /originalidad — verificación antiplagio

La memorización de los modelos no se reparte uniforme: se concentra en versos, citas, aperturas célebres y frases "memorables". Este flujo concentra ahí el esfuerzo. **No se edita nada aquí**: el resultado es un informe con acciones propuestas.

## 1. Candidatos (0 tokens)
`npm run originalidad` → escribe `informe/originalidad-candidatos.md`:
- **CRÍTICO**: versos/epígrafes (cursiva o blockquote) y citas atribuidas a personas que no son personajes.
- **ALTA**: primera y última frase de cada capítulo, aforismos.
- **MEDIA**: n-gramas de ~10 palabras con léxico raro (muestreo por rareza).
- **Términos**: nombres y neologismos de `memoria/nombres.md`.
Enséñale al autor el recuento. Si hay CRÍTICOS, di que su verificación es obligada antes de publicar.

## 2. Verificación → subagente **verificador**
Lánzalo (necesita búsqueda web). Verifica candidatos por prioridad con búsqueda exacta entre comillas, aplica los juicios (frase hecha ≠ plagio; letra de canción real = problema de derechos aunque sea breve; cita no encontrada = apócrifa; nombre que colisiona con ficción popular = renombrar) y escribe `informe/originalidad-informe.md` con tabla, acciones en formato `<<NOTA: … >>` y sus límites declarados.

## 3. Devolución y acciones
- Resumen en chat: exactas / parciales / limpias / sin verificar, y las EXACTAS una a una.
- Si hay acciones: con el visto bueno del autor, copia las `<<NOTA: … >>` propuestas a los `notas/cap-NN.md` correspondientes y ejecuta el flujo de `/aplicar-notas` (la reescritura la hacen redactor/editor bajo `estilo.md`: la sustitución también sale sin olor a IA).
- Renombrados de términos: cambio mecánico de `/aplicar-notas` (buscar/reemplazar determinista + archivista).
- Commit del informe.

## Cuándo y límites
- Momento: tras `/pulir` y antes del build de publicación. Repetir si una ronda de cambios tocó muchas frases.
- Sé honesto con el autor: esto reduce mucho el riesgo de regurgitación literal, pero no cubre todo lo impreso ni la similitud de ideas o estructura. Para máxima garantía en los CRÍTICOS (epígrafes, citas), la verificación manual del autor sigue siendo la última palabra.
