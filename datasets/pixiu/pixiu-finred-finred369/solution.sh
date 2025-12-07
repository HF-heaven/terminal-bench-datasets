#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
ARRAY ; company ; legal_form
EOF
