#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Primark ; Associated British Foods ; parent_organization
Primark ; Associated British Foods ; owned_by
EOF
