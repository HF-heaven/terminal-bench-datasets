#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
FedEx ; TNT ; owner_of
EOF
