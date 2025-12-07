#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
digester ; biogas ; product_or_material_produced
EOF
