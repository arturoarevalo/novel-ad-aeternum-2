#!/usr/bin/env bash
# T7 · Pre-chequeo de sensibilidad (aviso previo, no veto): hits nuevos de los patrones de A7 respecto a la baseline v0.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/sensibilidad.py" "$@"
