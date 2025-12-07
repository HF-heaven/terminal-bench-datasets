#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Sudan:B-LOC
Jemera:B-PER
EOF
