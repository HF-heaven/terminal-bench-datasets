#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Vodafone Ghana ; Vodafone ; parent_organization
Vodafone ; Vodafone Ghana ; subsidiary
EOF
