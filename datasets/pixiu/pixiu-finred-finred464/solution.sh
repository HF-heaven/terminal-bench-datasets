#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Intel ; server ; product_or_material_produced
EOF
