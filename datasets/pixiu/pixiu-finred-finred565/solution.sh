#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
NetSuite ; software ; product_or_material_produced
EOF
