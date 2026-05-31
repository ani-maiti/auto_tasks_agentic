#!/bin/bash

# Step 3: Extract keys from the remaining configuration files
grep -oP '^\S+' $(grep -v "invalid" $(find . -type f \( -name "*.json" -o -name "*.yaml" -o -name "*.ini" -o -name "*.toml" \))) | sort | uniq