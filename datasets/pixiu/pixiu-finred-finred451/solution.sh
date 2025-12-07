#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
water treatment ; water ; product_or_material_produced
EOF
