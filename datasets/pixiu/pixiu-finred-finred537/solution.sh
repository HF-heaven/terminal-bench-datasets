#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
GMC ; truck ; product_or_material_produced
EOF
