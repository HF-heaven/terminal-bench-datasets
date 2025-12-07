#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
skype ; Microsoft ; operator
EOF
