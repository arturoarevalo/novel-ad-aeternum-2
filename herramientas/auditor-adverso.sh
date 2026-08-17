#!/usr/bin/env bash
# Auditoría adversarial de inserciones (riesgo «hinchazón», §8): ¿paga cada inserción su etiqueta de función?
#   auditor-adverso.sh <cap-NN.md> [--orden ordenes/OT-NN.md] [--base v0] [--salida informe.md]
# Motor codex (gpt-5.6-sol, esfuerzo max): evaluador de otra familia de modelos sobre prosa escrita por A3a/A3b.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/lib/auditor_adverso.py" "$@"
