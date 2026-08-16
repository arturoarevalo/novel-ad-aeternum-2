#!/usr/bin/env bash
# Lectura EN FRÍO REAL (A6, A6b, lector-frio) con `claude -p` desde fuera del repositorio:
#   critica-fria.sh <rol> <insumo.md> [<insumo-2.md>] --salida <informe.md> [--modelo ID] [--esfuerzo E] [--mensaje "…"] [--dir DIR]
#   critica-fria.sh --sonda        # comprueba que el contexto de ejecución está limpio
# Env: AA_FRIO_DIR (directorio de ejecución fuera del repo; por defecto /tmp/aa-frio).
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/critica_fria.py" "$@"
