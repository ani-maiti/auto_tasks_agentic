import sqlite3
from collections import defaultdict

databases = open('sqlite_databases.txt', 'r').read().splitlines()
schema_dict = defaultdict(list)

for db_path in databases:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        schema_query = f"PRAGMA table_info({table[0]})"
        cursor.execute(schema_query)
        schema = cursor.fetchall()
        schema_dict[table[0]].append((db_path, schema))

similar_schemas = {table: paths for table, paths in schema_dict.items() if len(paths) > 1}

with open('consolidation_report.md', 'w') as f:
    f.write("# Consolidation Report\n\n")
    for table, paths in similar_schemas.items():
        f.write(f"## Table: {table}\n\n")
        for path, schema in paths:
            f.write(f"- **Database:** {path}\n")
            f.write("| Column | Type | Not Null | Default |\n|--------|------|----------|---------|\n")
            for col in schema:
                f.write(f"| {col[1]} | {col[2]} | {col[3]} | {col[4]} |\n")
            f.write("\n")

print("Consolidation report saved to consolidation_report.md")