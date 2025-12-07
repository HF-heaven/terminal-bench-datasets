#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Stratasys ; 3D printing ; product_or_material_produced
Stratasys ; 3D printing ; industry
EOF
