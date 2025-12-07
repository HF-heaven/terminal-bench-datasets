#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
David Thodey ; Telstra ; employer
Telstra ; David Thodey ; chief_executive_officer
EOF
