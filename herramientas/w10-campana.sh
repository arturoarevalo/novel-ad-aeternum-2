#!/usr/bin/env bash
# W10 · una campaña de medición completa, con control de deriva y guardia de regresión.
#
# Por qué existe: en este proyecto se ha demostrado que un solo juez varía hasta un
# punto entero sobre TEXTO IDÉNTICO. Sin control de deriva leído el mismo día, una
# medición no dice nada. Este script hace las cuatro lecturas, saca las medianas y
# las compara con la mejor conocida, para que W10 no acepte como mejora lo que es ruido.
#
#   herramientas/w10-campana.sh <etiqueta>
set -euo pipefail
cd "$(dirname "$0")/.."
ETQ="${1:?uso: w10-campana.sh <etiqueta>}"
export AA_FRIO_DIR="${AA_FRIO_DIR:-/tmp/aa-frio-w10}"
mkdir -p "$AA_FRIO_DIR" informes/w10

echo "[1/4] compilando…"
herramientas/compilar.sh "$ETQ" | tail -2

echo "[2/4] sonda de aislamiento…"
herramientas/critica-fria.sh --sonda            2>&1 | tail -1
herramientas/critica-fria.sh --sonda --motor codex 2>&1 | tail -1

echo "[3/4] tres críticos sobre vX + control de deriva sobre v0 (mismo día, mismo jurado)…"
for i in 1 2 3; do
  herramientas/critica-fria.sh "a6-critico-$i" "compilado/ad-aeternum-$ETQ.md" \
      --salida "informes/w10/a6-$ETQ-critico-$i.md" > "$AA_FRIO_DIR/$ETQ-c$i.log" 2>&1 &
done
herramientas/critica-fria.sh a6-critico-1 compilado/ad-aeternum-v0.md \
    --salida "informes/w10/a6-$ETQ-deriva-v0.md" > "$AA_FRIO_DIR/$ETQ-deriva.log" 2>&1 &
wait

echo "[4/4] medianas, deriva y guardia de regresión…"
python3 herramientas/lib/w10_scores.py "$ETQ"
