# Rasgos por personaje (anti-repetición)

> Registro de los **tics, rasgos físicos y sensaciones** que ya se han usado con cada personaje, para no repetirlos sin querer a lo largo de la novela. Lo mantiene el **archivista** tras cada capítulo: cuando un personaje estrena un gesto característico, un rasgo o una imagen sensorial, lo anota aquí en su forma canónica. El comando `npm run repeticiones` (incluido en `npm run salud`) cuenta —de forma tolerante a la flexión: ignora tildes y terminaciones verbales— cuántas veces reaparece cada uno y avisa si se pasa de su tope. Todo determinista, **0 tokens**.
>
> El **redactor** solo recibe en su brief las filas del **personaje POV** del capítulo, no toda la tabla; así esto no engorda su contexto por larga que se haga la novela.

## Tipos
- **tic** — gesto o manía recurrente (p. ej. «se ajusta las gafas»). Tope por defecto: 3 en toda la novela; además avisa si aparece en capítulos seguidos.
- **rasgo** — dato físico fijo (p. ej. «cicatriz en la ceja»). Se describe **una** vez; después se nombra de pasada, no se redescribe. Tope por defecto: 2.
- **sensacion** — imagen corporal o emocional (p. ej. «vacío en el estómago»). Tope por defecto: 2, para que no se vuelva muletilla.

## Formato
- **Forma canónica**: corta y con las palabras que de verdad la identifican (el sistema ignora tildes y flexión, así que no hace falta listar cada conjugación).
- **Variantes**: formas alternativas reales, separadas por `;` (opcional).
- **Caps**: en qué capítulos ha aparecido (informativo; lo actualiza el archivista).
- **Tope**: máximo de apariciones permitidas. Si se deja vacío, se usa el de por defecto según el tipo (configurable en `lint-prosa.config.json`).

| Personaje | Tipo | Forma canónica | Variantes | Caps | Tope |
|-----------|------|----------------|-----------|------|------|
| _Marta_ | _tic_ | _se ajusta las gafas_ | _toquetea la montura_ | _1, 3_ | _3_ |

_(La fila anterior es solo un ejemplo del formato y el sistema la ignora. El archivista añade las reales debajo.)_

## Notas
- Si dos filas del mismo personaje describen en realidad el mismo recurso, fúndelas (mejor una entrada con variantes que dos casi iguales).
- Los **ecos sin catalogar** (una imagen corporal/sensorial que se repite entre capítulos y que aún no está en esta tabla) los caza igualmente `npm run repeticiones` usando el léxico de `lint-prosa.config.json`. Cuando uno sea intencional, súbelo aquí con su tope; si no lo era, se varía.
