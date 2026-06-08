import sqlite3
import os
from collections import defaultdict

def get_sqlite_databases():
    # Using the paths found in the previous step
    db_paths = [
        '/home/ai_admin/.ipython/profile_default/history.sqlite',
        '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_CodeGemma-7B-IT/database.db',
        '/home/ai_admin/.config/libaccounts-glib/accounts.db',
        '/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/places.sqlite',
        '/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/formhistory.sqlite'
    ]
    return [path for path in db_paths if os.path.exists(path)]

def get_table_info(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    table_info = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        table_info[table_name] = columns
    
    return table_info

def get_foreign_keys(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    fk_info = defaultdict(list)
    
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        fks = cursor.fetchall()
        
        for fk in fks:
            # fk[2] is the referenced table, fk[3] is the referenced column
            fk_info[table_name].append({
                'column': fk[3],
                'ref_table': fk[2],
                'ref_column': fk[4]
            })
    
    return fk_info

def generate_schema_diagram(table_info, fk_info):
    diagram = []
    for table_name, columns in table_info.items():
        diagram.append(f"## Table: {table_name}")
        diagram.append("| Column | Type | Not Null | Default | Primary Key |")
        diagram.append("|--------|------|----------|---------|-------------|")
        
        for col in columns:
            col_name, col_type, not_null, default_val, pk = col[1], col[2], col[3], col[4], col[5]
            diagram.append(f"| {col_name} | {col_type} | {'Yes' if not_null else 'No'} | {default_val or ''} | {'Yes' if pk else 'No'} |")
        
        if table_name in fk_info and fk_info[table_name]:
            diagram.append("\nForeign Keys:")
            for fk in fk_info[table_name]:
                diagram.append(f"- {fk['column']} → {fk['ref_table']}.{fk['ref_column']}")
        
        diagram.append("")
    
    return "\n".join(diagram)

def process_database(db_path):
    try:
        conn = sqlite3.connect(db_path)
        table_info = get_table_info(conn)
        fk_info = get_foreign_keys(conn)
        diagram = generate_schema_diagram(table_info, fk_info)
        conn.close()
        return diagram
    except Exception as e:
        return f"Error processing {db_path}: {str(e)}"

# Get all database files
dbs = get_sqlite_databases()
print(f"Found {len(dbs)} databases")

# Process each database
for i, db_path in enumerate(dbs):
    print(f"\nProcessing database {i+1}: {db_path}")
    diagram = process_database(db_path)
    
    # Save to markdown file
    filename = f"schema_{os.path.basename(db_path)}.md"
    with open(filename, 'w') as f:
        f.write(f"# Schema Diagram for {os.path.basename(db_path)}\n\n")
        f.write(diagram)
    
    print(f"Saved schema to {filename}")