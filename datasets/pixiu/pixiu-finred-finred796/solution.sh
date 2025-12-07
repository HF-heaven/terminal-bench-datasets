#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Facebook ; Facebook Inc ; operator
Facebook ; Facebook Inc ; owned_by
Facebook Inc ; Facebook ; product_or_material_produced
EOF
