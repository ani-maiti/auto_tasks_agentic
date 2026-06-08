import sqlite3
import json
import os
from collections import defaultdict

# Get list of SQLite databases
db_paths = [
    "/home/ai_admin/.ipython/profile_default/history.sqlite",
    "/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_CodeGemma-7B-IT/database.db",
    "/home/ai_admin/.config/libaccounts-glib/accounts.db",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/places.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/formhistory.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage-sync-v2.sqlite"
]

# Function to get table schema
def get_table_schema(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        schema = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            schema[table_name] = []
            for col in columns:
                schema[table_name].append({
                    'name': col[1],
                    'type': col[2],
                    'notnull': col[3],
                    'default': col[4],
                    'primary_key': col[5]
                })
        
        conn.close()
        return schema
    except Exception as e:
        print(f"Error reading {db_path}: {e}")
        return None

# Collect schemas from all databases
all_schemas = {}
for db_path in db_paths:
    if os.path.exists(db_path):
        schema = get_table_schema(db_path)
        if schema:
            all_schemas[db_path] = schema

print(json.dumps(all_schemas, indent=2))