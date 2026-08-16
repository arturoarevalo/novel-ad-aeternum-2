#!/usr/bin/env bash
# Compila el manuscrito (insumo ÚNICO de A6/A6b): compilar.sh <etiqueta> [--sin-paratextos] [--sin-numeros]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/compilar.py" "$@"
