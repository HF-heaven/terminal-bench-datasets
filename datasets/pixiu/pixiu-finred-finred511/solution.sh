#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Phenom 300 ; Embraer ; manufacturer
EOF
