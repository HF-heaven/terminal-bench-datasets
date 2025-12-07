#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
IKEA ; furniture ; product_or_material_produced
EOF
