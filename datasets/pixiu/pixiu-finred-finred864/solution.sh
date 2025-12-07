#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Apple Inc ; Apple Pay ; product_or_material_produced
Apple Pay ; Apple Inc ; developer
Apple Pay ; Apple Inc ; owned_by
EOF
