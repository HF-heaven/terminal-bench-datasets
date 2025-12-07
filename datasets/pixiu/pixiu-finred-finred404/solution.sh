#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SABMiller ; beer ; product_or_material_produced
EOF
