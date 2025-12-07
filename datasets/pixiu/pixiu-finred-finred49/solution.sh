#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Prime ; retail ; industry
Fresh ; retail ; industry
EOF
