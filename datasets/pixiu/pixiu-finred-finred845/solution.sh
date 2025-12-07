#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
BayernLB ; Bavaria ; owned_by
BayernLB ; Munich ; headquarters_location
EOF
