import os
import json

# Step 1: Discover all Python files in the current directory and its subdirectories
python_files = [f for f in os.walk('.')] if os.path.exists('.') else []

print(python_files)