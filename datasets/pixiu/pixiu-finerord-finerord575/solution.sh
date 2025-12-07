#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Highlights:O
from:O
the:O
analysis:O
by:O
The:B-ORG
Street:I-ORG
Ratings:O
EOF
