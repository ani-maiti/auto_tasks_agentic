#!/bin/bash

# Step 4: Identify common keys across all configuration files
comm -12 <(sort ./valid_config_files.txt) <(sort ./valid_config_files.txt)