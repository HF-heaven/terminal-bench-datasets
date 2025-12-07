#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Cameco ; uranium ; product_or_material_produced
EOF
