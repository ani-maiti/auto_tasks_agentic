import os
import glob

# Find all SQLite databases in the current directory
databases = glob.glob('*.db')

if not databases:
    print("No SQLite databases found.")
else:
    print(f"Found {len(databases)} SQLite databases.")
```

This code snippet finds all SQLite databases in the current directory and prints the number of databases found. If no databases are found, it prints a message indicating so.