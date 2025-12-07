#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lysol ; Reckitt ; owned_by
Lysol ; Reckitt ; manufacturer
EOF
