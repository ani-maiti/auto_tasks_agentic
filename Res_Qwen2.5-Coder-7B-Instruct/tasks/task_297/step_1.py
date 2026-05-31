import os
import glob
import json

# Step 1: Discover all SQLite databases in the current directory
databases = glob.glob('*.db')
print(f"Found {len(databases)} SQLite databases.")