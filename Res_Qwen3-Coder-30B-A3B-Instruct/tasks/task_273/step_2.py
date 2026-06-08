import json
import re
from collections import defaultdict

# First, let's get all text files
import subprocess
result = subprocess.run(['find', '.', '-type', 'f', '-name', '*.txt'], capture_output=True, text=True)
text_files = result.stdout.strip().split('\n') if result.stdout.strip() else []

# Filter out empty strings
text_files = [f for f in text_files if f]

print(f"Found {len(text_files)} text files")
print("First 5 files:", text_files[:5])