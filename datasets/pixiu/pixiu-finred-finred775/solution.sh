#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Intel ; software ; product_or_material_produced
EOF
