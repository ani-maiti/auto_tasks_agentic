import os
import sqlite3
from collections import defaultdict

# Step 2: If no databases were found, prompt the user to provide a directory path
if not databases:
    directory_path = input("Please enter the path to the directory containing SQLite databases: ")
    databases = find_sqlite_databases(directory_path)
    if not databases:
        print("No SQLite databases found in the specified directory.")
    else:
        print(f"Found {len(databases)} SQLite databases.")