#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Wii ; Nintendo ; manufacturer
Wii ; Nintendo ; developer
EOF
