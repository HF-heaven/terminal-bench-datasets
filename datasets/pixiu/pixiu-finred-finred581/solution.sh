#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
GMC Sierra ; GMC ; brand
GMC Sierra ; GMC ; manufacturer
EOF
