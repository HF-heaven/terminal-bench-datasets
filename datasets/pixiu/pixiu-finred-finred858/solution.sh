#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lexus RX ; Toyota ; manufacturer
Lexus ; Toyota ; parent_organization
Lexus ; Toyota ; owned_by
EOF
