import os
import json

# Find all JSON files in the current directory tree
json_files = [f for f in os.walk('.')] if f.endswith('.json')]
print(json_files)