#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
The:O
Motley:B-ORG
Fool:I-ORG
UK:I-ORG
has:O
recommended:O
Clinigen:B-ORG
.:O
EOF
