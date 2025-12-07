#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Yum Brands ; KFC ; subsidiary
Yum Brands ; KFC ; owner_of
EOF
