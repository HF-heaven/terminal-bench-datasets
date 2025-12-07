#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Altera ; Intel ; parent_organization
EOF
