#!/usr/bin/env bash
# Validador de frontmatter y contratos (§2.4): campos autor/plan, estado, persona, notas de trabajo.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/validar.py" "$@"
