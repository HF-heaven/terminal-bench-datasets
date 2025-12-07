#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Insitu ; Boeing ; parent_organization
Boeing ; Insitu ; subsidiary
EOF
