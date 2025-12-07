#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
The:O
Motley:B-ORG
Fool:I-ORG
has:O
a:O
disclosure:O
policy:O
.:O
EOF
