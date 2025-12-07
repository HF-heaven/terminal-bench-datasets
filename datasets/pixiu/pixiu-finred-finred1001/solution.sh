#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Bourjois ; Coty ; parent_organization
Bourjois ; Coty ; owned_by
EOF
