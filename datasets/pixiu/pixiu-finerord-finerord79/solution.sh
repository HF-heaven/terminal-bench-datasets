#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Will:O
General:B-ORG
Motors:I-ORG
(:O
NYSE:B-ORG
::O
GM:B-ORG
):O
be:O
next:O
?:O
EOF
