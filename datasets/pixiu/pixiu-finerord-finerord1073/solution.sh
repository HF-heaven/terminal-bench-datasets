#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Jesse:B-PER
Ventura:I-PER
open:O
to:O
playing:O
...:O
EOF
