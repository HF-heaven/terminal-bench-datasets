#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Exxon ; diesel ; product_or_material_produced
Exxon ; gasoline ; product_or_material_produced
EOF
