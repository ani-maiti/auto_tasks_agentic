import os

# Get list of SQLite database files
sqlite_files = [f for f in os.listdir('.') if f.endswith('.db')]

if sqlite_files:
    print("SQLite databases found:", sqlite_files)
else:
    print("No SQLite databases found.")