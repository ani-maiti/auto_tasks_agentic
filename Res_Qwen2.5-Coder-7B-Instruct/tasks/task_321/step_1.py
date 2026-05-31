import os
import zipfile
from collections import defaultdict

# Step 1: Discover all archives in the current directory
archives = [f for f in os.listdir('.') if f.endswith('.zip')]

print(f"Found {len(archives)} archives.")