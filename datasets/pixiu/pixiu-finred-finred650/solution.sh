#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Fonterra ; milk ; product_or_material_produced
Dairy Farmers ; dairy ; product_or_material_produced
EOF
