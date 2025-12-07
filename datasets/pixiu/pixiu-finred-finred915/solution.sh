#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Steve Ballmer ; Microsoft ; employer
Steve Ballmer ; Microsoft ; owner_of
EOF
