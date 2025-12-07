#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Toyota Highlander ; Toyota ; brand
Toyota Highlander ; Toyota ; manufacturer
EOF
