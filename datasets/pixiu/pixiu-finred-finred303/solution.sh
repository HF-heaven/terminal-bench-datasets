#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Loaf ; company ; legal_form
EOF
