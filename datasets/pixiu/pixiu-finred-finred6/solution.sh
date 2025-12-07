#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Chromecast ; Google ; manufacturer
Chromecast ; Google ; developer
EOF
