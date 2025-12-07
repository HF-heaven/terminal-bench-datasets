#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Officeworks ; Wesfarmers ; parent_organization
Wesfarmers ; Officeworks ; subsidiary
EOF
