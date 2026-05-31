import os
import json
from collections import Counter

# Step 1: Find all JSON files in the current directory tree
json_files = [f for f in os.walk('.')] if f.endswith('.json')]
print(f"Found {len(json_files)} JSON files.")