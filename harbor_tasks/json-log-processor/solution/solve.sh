#!/bin/bash

set -e

python3 << 'EOF'
import json

with open('/app/input/logs.json', 'r') as f:
    logs = json.load(f)

errors = [entry for entry in logs if entry.get('level') == 'ERROR']

with open('/app/output/errors.json', 'w') as f:
    json.dump(errors, f, indent=2)

print(f"Filtered {len(errors)} ERROR entries from {len(logs)} total logs")
EOF

