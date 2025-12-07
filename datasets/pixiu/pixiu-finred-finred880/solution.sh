#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Apple II ; Steve Wozniak ; developer
EOF
