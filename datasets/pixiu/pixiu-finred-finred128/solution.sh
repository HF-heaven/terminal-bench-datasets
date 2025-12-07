#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Volvo ; truck ; product_or_material_produced
Mack Trucks ; truck ; product_or_material_produced
EOF
