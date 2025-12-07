#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
S11D ; iron ore ; product_or_material_produced
Roy Hill ; iron ore ; product_or_material_produced
EOF
