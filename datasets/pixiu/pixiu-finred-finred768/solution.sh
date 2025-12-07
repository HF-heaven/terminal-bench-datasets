#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Rafale ; Dassault Aviation ; developer
Rafale ; Dassault Aviation ; manufacturer
EOF
