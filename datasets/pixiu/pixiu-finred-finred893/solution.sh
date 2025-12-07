#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
SunExpress ; Lufthansa ; owned_by
Lufthansa ; SunExpress ; subsidiary
Lufthansa ; Lufthansa Cargo ; subsidiary
EOF
