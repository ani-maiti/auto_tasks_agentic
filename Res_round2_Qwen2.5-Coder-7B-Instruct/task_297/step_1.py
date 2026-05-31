import os
import glob

# Find all SQLite databases in the current directory
databases = glob.glob('*.db')

if not databases:
    print("No SQLite databases found.")
else:
    print(f"Found {len(databases)} SQLite databases.")
```

This script will list all SQLite databases in the current directory. If no databases are found, it will print a message indicating so. If databases are found, it will print the number of databases discovered.