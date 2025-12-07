#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
coffee roaster ; coffee ; product_or_material_produced
EOF
