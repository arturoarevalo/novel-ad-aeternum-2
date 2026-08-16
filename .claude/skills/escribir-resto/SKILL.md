---
name: escribir-resto
description: Escribe de forma autónoma TODOS los capítulos pendientes de la novela, uno tras otro, cada uno con contexto fresco. Úsalo cuando el usuario diga "escribe el resto", "escribe toda la novela", "continúa hasta el final", "/escribir-resto" o "/escribir-todo". Pensado para tiradas largas sin supervisión (con --dangerously-skip-permissions). Se apoya en el runner, que reanuda donde se quedó y para si un capítulo no pasa la puerta de calidad.
---

# /escribir-resto — tirada autónoma

Escribe los capítulos que falten, en orden, llamando al pipeline `/capitulo N` para cada uno **con contexto fresco** (mejor calidad de cola y sin que la compactación borre el diseño).

## Antes de empezar
- Comprueba que la biblia está revisada (idealmente el capítulo 1 ya existe y te gusta cómo quedó; sirve de patrón de voz).
- Para reaprovechar la caché del prefijo estable entre capítulos, exporta `CLAUDE_CACHE_TTL=1h` y ejecuta los capítulos seguidos.

## Cómo ejecutarlo
Lanza el runner, que detecta los capítulos pendientes (sin fichero o en estado `borrador`/`pendiente`), invoca `/capitulo N` para cada uno, y entre capítulos pasa la **puerta de calidad** (`npm run salud`). Si un capítulo falla, **se detiene** para que lo revises (no construye sobre algo roto). Lleva checkpoint en `.runner-state.json`, así que al relanzarlo continúa donde se quedó.

```bash
# Vista previa (no escribe nada):
npm run escribir-resto -- --dry-run

# Tirada completa:
CLAUDE_CACHE_TTL=1h npm run escribir-resto

# Un tramo concreto:
npm run escribir-resto -- --desde 5 --hasta 12
```

> Nota: el runner lanza `claude -p "/capitulo N" --permission-mode bypassPermissions`. Esto requiere ejecutar la sesión con permisos ya concedidos (ver RUNBOOK). Si prefieres orquestar tú la iteración dentro de una sola sesión en vez de relanzar el binario, recorre los pendientes llamando a `/capitulo N` uno a uno, respetando el mismo orden y la misma puerta de calidad entre capítulos.

## Al terminar
Resumen breve: cuántos capítulos se han escrito, total de palabras (`npm run build` lo reporta) y cualquier capítulo donde se haya parado y por qué.

**Vigilancia de presupuesto**: cada 3 capítulos, `npm run hilos` y mira la proyección. Si supera el objetivo en más del 10 %, baja el objetivo de los briefs siguientes en proporción y anótalo en el parte; no esperes al final para descubrir 40.000 palabras de más.
