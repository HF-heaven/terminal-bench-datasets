#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
ConocoPhillips ; petroleum ; product_or_material_produced
EOF
