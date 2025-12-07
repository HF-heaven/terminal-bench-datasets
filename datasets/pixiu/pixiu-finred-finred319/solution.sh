#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
go90 ; Verizon ; owned_by
EOF
