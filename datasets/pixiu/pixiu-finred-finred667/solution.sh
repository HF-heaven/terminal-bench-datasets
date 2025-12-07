#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
veto power ; veto ; product_or_material_produced
EOF
