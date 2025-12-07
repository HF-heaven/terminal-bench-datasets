#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lexus ; Toyota ; parent_organization
Lexus ; Toyota ; owned_by
EOF
