#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Jeep Renegade ; Jeep ; brand
Jeep Renegade ; Jeep ; manufacturer
EOF
