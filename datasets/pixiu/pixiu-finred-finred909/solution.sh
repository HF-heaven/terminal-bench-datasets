#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Avelumab ; Merck KGaA ; manufacturer
Avelumab ; Pfizer ; manufacturer
EOF
