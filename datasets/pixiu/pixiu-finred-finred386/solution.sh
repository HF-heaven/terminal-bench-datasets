#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
WeChat ; Tencent ; developer
Tencent ; WeChat ; subsidiary
EOF
