#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Visa Inc ; Visa Europe ; subsidiary
Visa Europe ; Visa Inc ; parent_organization
EOF
