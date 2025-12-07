#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Petrobras ; gas ; product_or_material_produced
EOF
