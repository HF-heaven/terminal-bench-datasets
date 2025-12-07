#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Costa Coffee ; Whitbread ; parent_organization
Whitbread ; Costa Coffee ; subsidiary
EOF
