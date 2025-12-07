#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SingTel ; Optus ; subsidiary
Optus ; SingTel ; parent_organization
Optus ; SingTel ; owned_by
EOF
