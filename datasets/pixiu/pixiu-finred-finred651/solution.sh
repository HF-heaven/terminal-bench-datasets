#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Stratasys ; 3D printing ; product_or_material_produced
3D Systems ; 3D printing ; industry
Stratasys ; 3D printing ; industry
EOF
