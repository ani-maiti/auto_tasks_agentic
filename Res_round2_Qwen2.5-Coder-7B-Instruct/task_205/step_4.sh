echo "Generating schema summary..."
python <<EOF
import sqlite3
import re

# Read all schemas into memory
with open('schemas.sql', 'r') as f:
    schemas = f.read()

# Extract table names and sizes
tables = {}
pattern = re.compile(r'CREATE TABLE (\w+)')
matches = pattern.findall(schemas)
for match in matches:
    tables[match] = 0

# Count rows for each table
for db in [line.strip() for line in open('sqlite_databases.txt', 'r')]:
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    for table in tables.keys():
        cursor.execute(f'SELECT COUNT(*) FROM {table}')
        count = cursor.fetchone()[0]
        tables[table] += count
    conn.close()

# Sort tables by size
sorted_tables = sorted(tables.items(), key=lambda x: x[1], reverse=True)

# Generate summary
summary = "# SQLite Schema Summary\n\n"
for table, size in sorted_tables:
    summary += f"- **{table}**: {size} rows\n"

# Write summary to Markdown file
with open('schema_summary.md', 'w') as f:
    f.write(summary)

print("Schema summary generated and saved to schema_summary.md")
EOF