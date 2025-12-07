#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Super Mario ; Nintendo ; distributed_by
Super Mario ; Nintendo ; publisher
EOF
