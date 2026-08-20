# W11 · La pasada de nomenclatura se declina, y la razón es de A7

**A0 · 2026-08-20.** Los tres editores la pedían. Se declina, y no por perímetro: **porque no
haría lo que se pedía que hiciera.**

## El argumento que la desmonta, y no lo tenía nadie

**El libro ya hace lo que pide el editor**, con un mecanismo que esta pasada borraría:

> El código aparece **en monoespaciado, como salida del sistema**, y la prosa se refiere después
> a la cosa **con un nombre común**. Está en los cinco términos: «asociaría su identidad, **la
> incidencia**, la hora y la puerta»; «Jean reconoce **el formulario**»; «El certificado conduce
> **al proveedor de seguridad** de la cadena de Kronfjord Kapital»; «Conservaré el expediente de
> contratación **del fondo**»; «un hombre llevó **a la supervisión** dos resoluciones».
>
> **La contrapropuesta no instaura esa práctica: le quita los anclajes.**

Y la aritmética remata: **la densidad que molesta al editor no viene de que los códigos se
repitan, sino de que hay veintiún nombres.** Quitarle tres ocurrencias a un nombre de siete no
mueve esa cifra. De las ≈40 ocurrencias que prometía la operación quedan **como mucho 18**, y
ninguna mejora un punto de la Carta.

## Los cuatro cortes concretos, uno por uno

- **`TKS` → «la supervisión»: DENEGADO.** `supervis-` es en este libro el lexema de «una ventana
  **supervisada** de audio y texto para futuras visitas» —el locutorio— y de «una sesión
  **supervisada** en un canal educativo aislado» —una menor—. Hacerlo además el nombre del
  órgano **tiende un puente léxico entre quien no protege y el canal por el que una hija se
  encuentra con lo que puede ser su madre.** Y «la inspectora» convierte un órgano en persona.
- **`R-1189`: 7 disponibles, no 15**, por tres pruebas —tipográfica, gramatical y de
  protección—. Con **veto de Carta** en `cap-30:65`: el bloque funciona porque el código llega
  opaco y solo después el sistema dice qué era; nombrar el acto antes pone la memoria corporal
  de Jean bajo un rótulo que nombra lo que ella hizo.
- **`Hvelv`/`Kronfjord`: debilita, y A7 dice dónde.** La gramática del auto es **nombre propio
  para lo probado, nombre común para el hueco**. Si la cadena también es nombre común,
  desaparece la señal que distingue lo acreditado de lo no acreditado: el auto pasa de «sabemos
  la cadena y aun así no podemos nombrar a la persona» a «no consta nada». **No resuelve la
  ambigüedad: la disuelve, que es peor, porque invita al lector a rellenarla.** Y «el fondo»
  queda denegado: en este libro «el fondo» ya es el fondo del mar, **en los dos capítulos donde
  Maja y Jessie salen al agua**.
- **`INC-441`: VETO íntegro.** Es **7 de 7 monoespaciado**: no hay una sola ocurrencia en prosa
  que colapsar, así que «6 de 7» medía algo que no existe.

## El dramatis personae que pedía un editor: DENEGADO

Y la razón buena no es la mía —«un libro que se abre con un aviso y una lista de siglas empieza
pidiendo perdón dos veces»— sino ésta: **tendría que separar personas de no-personas** para
ordenar a `JM-L/0000`, AK-7, Madre, Nieve, Coro, NORNA y Cuchillo. **Esa separación es la
pregunta que R7·4 deja abierta para siempre.** Y ya estaba dictaminado para el índice: no se
responde desde la tabla de contenidos. **Un reparto es el índice de las personas.**

## Lo que sí queda hecho, y no depende de la pasada

1. **`b7` §1 reescrito: la definición de «voz con autoridad narrativa» ya no se ancla a una
   sigla.** Estaba anclada a «la TKS», es decir, **al único tipo de dirección que una pasada de
   nomenclatura puede retirar**. Ahora define por **forma**: acta, auto, resolución o
   consignación de un órgano, «se las nombre por sigla, por perífrasis o por su nombre completo».
2. **A7-W11-C1 al perímetro:** el monoespaciado es una frontera de voz. Se verifica con una
   regex y no envejece.
3. **Dos arreglos del verificador**, los dos de A7:
   - Su resumen era deshonesto. Decía «0 perdidas, 0 movidas» sobre 77 citas de las que **53 no
     se comprobaban**. Ahora encabeza con **«VERIFICADAS 25 de 77»** y avisa cuando hay más sin
     comprobar que comprobadas: *«"0 perdidas" es cierto y no significa verificado»*.
   - **Un bug latente**, reproducido: en una enumeración `` `ref` («literal») · `ref` («literal») ``
     cada referencia **robaba el literal de la anterior** y se declaraba no verificable. Hoy era
     latente porque `b7` usa el orden canónico; dejaba de serlo el día que alguien escribiera una
     tabla.

## Y la frase que cierra la decisión, que es de A7

> «Si el objetivo era aliviar al lector de veintiún nombres, **dieciocho tokens no lo
> consiguen y el trabajo está en otro sitio**.»
