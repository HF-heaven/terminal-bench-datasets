#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
paper machine ; paper ; product_or_material_produced
EOF
