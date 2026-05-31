#!/bin/bash

# Step 2: Filter out invalid configuration files
grep -v "invalid" $(find . -type f \( -name "*.json" -o -name "*.yaml" -o -name "*.ini" -o -name "*.toml" \))