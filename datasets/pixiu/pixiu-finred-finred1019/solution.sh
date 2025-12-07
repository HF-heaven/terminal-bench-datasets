#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mattel ; American Girl ; subsidiary
Mattel ; Barbie ; owner_of
EOF
