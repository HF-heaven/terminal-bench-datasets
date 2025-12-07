#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Red Hat ; IBM ; parent_organization
EOF
