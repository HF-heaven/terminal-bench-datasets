#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Thomas:B-PER
Davidson:I-PER
EOF
