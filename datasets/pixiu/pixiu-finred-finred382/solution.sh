#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Amy Hood ; chief financial officer ; position_held
Windows 10 ; Microsoft ; developer
Amy Hood ; Microsoft ; employer
EOF
