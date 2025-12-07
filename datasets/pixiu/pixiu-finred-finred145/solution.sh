#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SunGard ; software ; product_or_material_produced
SunGard ; Fidelity National Information Services ; owned_by
EOF
