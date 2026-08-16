#!/usr/bin/env bash
# Única vía de escritura de campos operativos de biblia/metadatos.json (§2.4). Ver herramientas/lib/metadatos.py --help
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export AA_MANIFIESTO_ESCRITURA=1
exec python3 "$DIR/lib/metadatos.py" "$@"
