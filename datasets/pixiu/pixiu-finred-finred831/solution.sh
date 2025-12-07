#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Mattel ; Fisher-Price ; owner_of
Mattel ; Barbie ; owner_of
Mattel ; Fisher-Price ; subsidiary
EOF
