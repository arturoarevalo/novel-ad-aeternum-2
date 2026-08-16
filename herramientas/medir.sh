#!/usr/bin/env bash
# Ejecuta M1–M10 y vuelca el dashboard en informes/: medir.sh <etiqueta> [--baseline v0]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/metricas.py" "$@"
