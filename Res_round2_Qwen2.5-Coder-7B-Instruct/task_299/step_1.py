import os
import re
from collections import defaultdict

# Step 1: Find all Markdown files
markdown_files = [f for f in os.listdir('.') if f.endswith('.md')]
print(f"Found {len(markdown_files)} Markdown files.")