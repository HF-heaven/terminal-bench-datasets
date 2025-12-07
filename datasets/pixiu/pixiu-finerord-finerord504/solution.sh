#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Automotive:O
Industry:O
Transportation:O
Tesla:B-ORG
Motors:I-ORG
General:B-ORG
Motors:I-ORG
EOF
