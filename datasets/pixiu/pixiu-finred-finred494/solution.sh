#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Genzyme ; Sanofi ; owned_by
Genzyme ; Sanofi ; parent_organization
Sanofi ; Genzyme ; subsidiary
EOF
