#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Novozymes ; enzyme ; product_or_material_produced
EOF
