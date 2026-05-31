import os
import glob
import pandas as pd

# Step 1: Discover all CSV files in the current directory tree
csv_files = glob.glob('**/*.csv', recursive=True)
print(f"Found {len(csv_files)} CSV files.")