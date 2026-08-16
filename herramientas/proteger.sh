#!/usr/bin/env bash
# M9 · Guardia de protegidos: baseline / verificar [--staged] / listar. Ver lib/proteger.py
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/proteger.py" "$@"
