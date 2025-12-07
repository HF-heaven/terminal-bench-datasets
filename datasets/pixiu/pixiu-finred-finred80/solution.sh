#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Lufthansa ; Austrian Airlines ; subsidiary
Kay Kratky ; Austrian Airlines ; employer
EOF
