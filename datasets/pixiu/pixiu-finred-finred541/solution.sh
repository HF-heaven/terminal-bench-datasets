#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
food industry ; food ; product_or_material_produced
fast food industry ; fast food ; product_or_material_produced
EOF
