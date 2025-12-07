#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
":O
We:O
know:O
Bill:B-PER
pretty:O
well:O
,:O
":O
Birmingham:B-PER
says:O
.:O
EOF
