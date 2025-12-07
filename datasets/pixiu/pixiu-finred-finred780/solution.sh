#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Snapdeal ; e-commerce ; industry
Freecharge ; e-commerce ; industry
Freecharge ; Snapdeal ; owned_by
EOF
