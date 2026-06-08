import sqlite3
import json
import os
from collections import defaultdict, Counter

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

# Find similar column names and types across databases
similar_columns = defaultdict(list)

# Create a mapping of column names to their types and databases
column_db_mapping = defaultdict(lambda: defaultdict(list))

for db_path, schema in all_schemas.items():
    for table_name, columns in schema.items():
        for col in columns:
            col_name = col['name']
            col_type = col['type']
            column_db_mapping[col_name][col_type].append((db_path, table_name))

# Identify columns that appear in multiple databases with same type
potential_relationships = []

for col_name, type_dbs in column_db_mapping.items():
    for col_type, dbs in type_dbs.items():
        if len(dbs) > 1:  # Column appears in multiple databases
            # Check if there's a common pattern
            db_list = [db for db, _ in dbs]
            table_list = [table for _, table in dbs]
            
            # Look for common table names or patterns
            table_counts = Counter(table_list)
            common_tables = [table for table, count in table_counts.items() if count > 1]
            
            if common_tables:
                potential_relationships.append({
                    'column': col_name,
                    'type': col_type,
                    'databases': db_list,
                    'tables': table_list,
                    'common_tables': common_tables,
                    'similarity_score': len(dbs)
                })

# Generate mapping report
mapping_report = {
    'database_schemas': all_schemas,
    'potential_relationships': potential_relationships,
    'total_databases': len(all_schemas),
    'total_columns_analyzed': sum(len(columns) for schema in all_schemas.values() for columns in schema.values())
}

# Save to JSON file
with open('sqlite_mapping_report.json', 'w') as f:
    json.dump(mapping_report, f, indent=2)

# Print strongest inferred relationship
if potential_relationships:
    strongest = max(potential_relationships, key=lambda x: x['similarity_score'])
    print("Strongest inferred relationship:")
    print(json.dumps(strongest, indent=2))
else:
    print("No strong relationships found.")

# Print summary
print("\nMapping Report Summary:")
print(f"Total databases analyzed: {mapping_report['total_databases']}")
print(f"Total columns analyzed: {mapping_report['total_columns_analyzed']}")
print(f"Potential relationships found: {len(mapping_report['potential_relationships'])}")