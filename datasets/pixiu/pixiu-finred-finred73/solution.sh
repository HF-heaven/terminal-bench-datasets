#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Eurogroup ; Jean-Claude Juncker ; chairperson
Eurogroup ; Jeroen Dijsselbloem ; chairperson
EOF
