import os
import glob

# Find all CSV files in the current directory and its subdirectories
csv_files = glob.glob('**/*.csv', recursive=True)

if csv_files:
    print(f"Found {len(csv_files)} CSV files.")
else:
    print("No CSV files found.")
```

This script will list all CSV files in the current directory and its subdirectories. If no CSV files are found, it will notify you accordingly.