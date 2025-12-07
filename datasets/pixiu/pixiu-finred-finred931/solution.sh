#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Cheetah Mobile ; Kingsoft ; owned_by
Cheetah Mobile ; Kingsoft ; parent_organization
EOF
