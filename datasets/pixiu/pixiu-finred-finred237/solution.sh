#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Vodafone India ; Vodafone ; parent_organization
Vodafone ; Vodafone India ; subsidiary
EOF
