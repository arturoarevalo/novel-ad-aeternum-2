#!/usr/bin/env bash
# B0 · Auditoría del manifiesto contra repositorio y prosa (solo lectura; markdown por stdout).
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/auditar_manifiesto.py" "$@"
