#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Nintendo DS ; Nintendo ; developer
Nintendo DS ; Nintendo ; manufacturer
EOF
