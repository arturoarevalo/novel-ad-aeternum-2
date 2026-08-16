#!/usr/bin/env bash
# Hook PreToolUse (Claude Code): bloquea Write/Edit/MultiEdit/NotebookEdit sobre ficheros con proteccion: total,
# sobre biblia/metadatos.json (solo vía actualizar-metadatos.sh) y sobre protegidos/hashes.json (solo vía proteger.sh).
# Para Bash: heurística de escritura sobre esos mismos ficheros. Se aplica también a los subagentes de la sesión.
# Excepción de gate de autor: comando Bash con prefijo AA_GATE_AUTOR="<motivo>" (el pre-commit M9 sigue vigilando).
set -uo pipefail
ROOT="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
exec python3 "$ROOT/herramientas/hooks/pretooluse_protegidos.py" "$ROOT"
