# notas/

Canal de feedback del autor sobre capítulos ya escritos. Un fichero por capítulo: `cap-NN.md`.

Escribe tus notas con el marcador `<<NOTA: … >>` (también puedes pegar correcciones libres). Luego ejecuta `/aplicar-notas` (o `/revisar NN`) y el **editor** las aplica con parches dirigidos, sin reescribir de cero. El grafo de coherencia trata estas notas como entrada que vuelve "obsoleto" el capítulo hasta que se reprocesa.

Ejemplo:
```
<<NOTA: el diálogo del muelle es demasiado explícito; mete subtexto, que no diga lo que siente.>>
<<NOTA: Marta no puede saber aún lo del bote (ver matriz de conocimiento).>>
```
