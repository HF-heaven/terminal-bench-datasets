#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Tencent ; WeBank ; owner_of
WeBank ; Tencent ; owned_by
EOF
