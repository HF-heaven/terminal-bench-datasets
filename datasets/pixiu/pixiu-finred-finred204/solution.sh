#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Vodafone ; Verizon ; subsidiary
Verizon ; Vodafone ; parent_organization
EOF
