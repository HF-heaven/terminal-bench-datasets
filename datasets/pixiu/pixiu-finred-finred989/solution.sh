#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mattel ; doll ; product_or_material_produced
Mattel ; Barbie ; owner_of
EOF
