#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
MYOB ; accounting software ; product_or_material_produced
EOF
