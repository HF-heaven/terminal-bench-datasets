#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
HBO ; HBO Now ; owner_of
HBO Now ; HBO ; owned_by
EOF
