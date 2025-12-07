#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Boston Pizza ; restaurant ; product_or_material_produced
EOF
