#!/bin/bash
set -euo pipefail

cd /app
cat > answer.txt << 'EOF'
Morgan Stanley ; New York City ; location_of_formation
Morgan Stanley ; New York City ; headquarters_location
Citigroup ; New York City ; location_of_formation
Citigroup ; New York City ; headquarters_location
EOF
