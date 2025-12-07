#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Walter Energy ; coal ; product_or_material_produced
Patriot Coal ; coal ; product_or_material_produced
EOF
