#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Pemex ; petroleum ; product_or_material_produced
Pemex ; Mexico City ; headquarters_location
EOF
