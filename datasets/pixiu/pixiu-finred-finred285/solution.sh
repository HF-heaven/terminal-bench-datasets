#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Equinix ; data center ; product_or_material_produced
EOF
