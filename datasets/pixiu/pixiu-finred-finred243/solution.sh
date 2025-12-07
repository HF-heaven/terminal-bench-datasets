#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Chapters ; Indigo ; parent_organization
Chapters ; retail ; industry
EOF
