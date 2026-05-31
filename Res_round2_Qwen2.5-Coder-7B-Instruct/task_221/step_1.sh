#!/bin/bash

# Step 1: Search for configuration files in the current directory and subdirectories
find . -type f \( -name "*.json" -o -name "*.yaml" -o -name "*.ini" -o -name "*.toml" \)