#!/bin/bash

# Find all configuration files in the current directory and its subdirectories
find . -type f \( -name "*.json" -o -name "*.yaml" -o -name "*.ini" -o -name "*.toml" \)