#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Statkraft ; energy ; product_or_material_produced
EOF
