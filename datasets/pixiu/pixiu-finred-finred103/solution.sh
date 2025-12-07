#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Daimler AG ; Mercedes-Benz ; owner_of
Daimler AG ; Mercedes-Benz ; brand
EOF
