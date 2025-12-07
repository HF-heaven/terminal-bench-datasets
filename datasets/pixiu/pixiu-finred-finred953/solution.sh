#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Google Docs ; Google ; owned_by
Google Hangouts ; Google ; creator
Google Docs ; Google ; developer
Google Hangouts ; Google ; developer
EOF
