#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Jeff Bezos ; Amazon ; employer
Jeff Bezos ; Amazon ; owner_of
EOF
