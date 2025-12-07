#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Google Authenticator ; Google ; manufacturer
Google Authenticator ; Google ; developer
EOF
