#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
The:O
Economist:B-ORG
is:O
calling:O
it:O
":O
transformative:O
":O
...:O
EOF
