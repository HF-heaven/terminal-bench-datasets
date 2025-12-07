#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Xbox ; Microsoft ; owned_by
Xbox One ; Microsoft ; developer
EOF
