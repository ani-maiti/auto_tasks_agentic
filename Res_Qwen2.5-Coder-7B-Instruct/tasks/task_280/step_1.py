import os
import sqlite3
from collections import defaultdict

# Step 1: Discover all SQLite databases in the current directory tree
def find_sqlite_databases(directory):
    sqlite_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.db'):
                sqlite_files.append(os.path.join(root, file))
    return sqlite_files

sqlite_databases = find_sqlite_databases('.')
print(f"Found {len(sqlite_databases)} SQLite databases.")