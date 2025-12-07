#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mastercard ; credit card ; product_or_material_produced
Scotiabank ; bank ; industry
EOF
