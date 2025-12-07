#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Nexus 6P ; Huawei ; developer
Nexus 6P ; Huawei ; manufacturer
Nexus 6P ; Google ; developer
EOF
