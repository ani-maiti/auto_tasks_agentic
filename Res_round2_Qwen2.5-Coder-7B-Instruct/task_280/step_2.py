import os
import sqlite3
from collections import defaultdict

# Step 1: Discover all SQLite databases in the current directory tree
def find_sqlite_databases(directory):
    sqlite_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.sqlite') or file.endswith('.db'):
                sqlite_files.append(os.path.join(root, file))
    return sqlite_files

databases = find_sqlite_databases('.')
if not databases:
    print("No SQLite databases found in the current directory tree.")
else:
    print(f"Found {len(databases)} SQLite databases.")