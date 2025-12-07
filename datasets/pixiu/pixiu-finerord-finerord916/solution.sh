#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
":O
It:O
's:O
like:O
what:O
Bart:B-PER
Simpson:I-PER
says:O
.:O
EOF
