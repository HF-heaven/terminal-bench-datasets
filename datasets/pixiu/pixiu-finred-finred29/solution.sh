#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Gears ; Google ; developer
Gears ; Google ; creator
Google Search ; Google ; owned_by
Gears ; Google ; owned_by
EOF
