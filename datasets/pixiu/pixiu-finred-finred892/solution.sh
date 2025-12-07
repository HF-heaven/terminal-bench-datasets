#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Qantas ; Alan Joyce ; chief_executive_officer
Alan Joyce ; Qantas ; employer
EOF
