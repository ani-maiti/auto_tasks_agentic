import os
import sqlite3
from collections import defaultdict

def get_db_schemas(directory):
    schemas = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".db"):
                db_path = os.path.join(root, filename)
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                schemas[db_path] = defaultdict(list)
                for table_name in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
                    schemas[db_path][table_name[0]] = []
                    for column_name, data_type, _ in cursor.execute("PRAGMA table_info({})".format(table_name[0])):
                        schemas[db_path][table_name[0]].append((column_name, data_type))
                conn.close()
    return schemas

def get_largest_tables(schemas):
    largest_tables = {}
    for db_path, tables in schemas.items():
        largest_tables[db_path] = max(tables, key=lambda t: len(schemas[db_path][t]))
    return largest_tables

def generate_schema_summary(schemas):
    summary = []
    for db_path, tables in schemas.items():
        summary.append("## Database: {}".format(db_path))
        for table_name, columns in tables.items():
            summary.append("### Table: {}".format(table_name))
            for column_name, data_type in columns:
                summary.append("* {} ({})".format(column_name, data_type))
    return "\n".join(summary)

def save_markdown(content, filename):
    with open(filename, "w") as f:
        f.write(content)

# Get database schemas
schemas = get_db_schemas(".")

# Get largest tables
largest_tables = get_largest_tables(schemas)

# Generate schema summary
summary = generate_schema_summary(schemas)

# Save summary to markdown file
save_markdown(summary, "database_schema_summary.md")