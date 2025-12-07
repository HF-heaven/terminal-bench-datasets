#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Dean Foods ; milk ; product_or_material_produced
EOF
