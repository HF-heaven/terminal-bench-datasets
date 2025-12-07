#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Yum China ; Pizza Hut ; brand
Yum Brands ; Pizza Hut ; subsidiary
Yum Brands ; Pizza Hut ; owner_of
EOF
