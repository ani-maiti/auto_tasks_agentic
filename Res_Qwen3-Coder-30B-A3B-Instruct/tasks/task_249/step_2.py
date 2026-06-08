import sqlite3
import os
import hashlib
from collections import defaultdict

def get_db_tables(db_path):
    """Get table names and schema from a SQLite database"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        table_schemas = {}
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            schema = cursor.fetchone()
            if schema and schema[0]:
                table_schemas[table_name] = schema[0]
        
        conn.close()
        return table_schemas
    except Exception as e:
        print(f"Error reading {db_path}: {e}")
        return {}

def calculate_schema_hash(schema):
    """Calculate a hash of the schema for comparison"""
    return hashlib.md5(schema.encode('utf-8')).hexdigest()

def find_similar_schemas(databases):
    """Find tables with similar schemas across databases"""
    schema_map = defaultdict(list)  # schema_hash -> [(db_path, table_name), ...]
    
    for db_path in databases:
        tables = get_db_tables(db_path)
        for table_name, schema in tables.items():
            schema_hash = calculate_schema_hash(schema)
            schema_map[schema_hash].append((db_path, table_name))
    
    # Group by similar schemas
    similar_groups = []
    for schema_hash, table_info_list in schema_map.items():
        if len(table_info_list) > 1:  # Only consider groups with multiple tables
            similar_groups.append({
                'schema_hash': schema_hash,
                'tables': table_info_list
            })
    
    return similar_groups

# Get list of database files
db_files = [
    "/home/ai_admin/.ipython/profile_default/history.sqlite",
    "/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_CodeGemma-7B-IT/database.db",
    "/home/ai_admin/.config/libaccounts-glib/accounts.db",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/places.sqlite"
]

# Find similar schemas
similar_groups = find_similar_schemas(db_files)

# Print results
print("Similar schema groups found:")
for i, group in enumerate(similar_groups):
    print(f"\nGroup {i+1}:")
    for db_path, table_name in group['tables']:
        print(f"  - {db_path}:{table_name}")
```