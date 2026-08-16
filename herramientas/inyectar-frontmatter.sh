#!/usr/bin/env bash
# Inyecta los campos del plan (§2.4) en el frontmatter desde ordenes/tabla-5-1.json. Ver lib/inyectar_frontmatter.py
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/inyectar_frontmatter.py" "$@"
