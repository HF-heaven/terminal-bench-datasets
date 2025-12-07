#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
PayPal ; Venmo ; subsidiary
EOF
