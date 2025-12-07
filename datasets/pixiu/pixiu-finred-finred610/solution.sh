#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mastercard ; debit card ; product_or_material_produced
EOF
