#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Peter:B-PER
Stephens:I-PER
owns:O
shares:O
of:O
Clinigen:B-ORG
.:O
EOF
