#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Joe Kaeser ; Siemens ; employer
EOF
