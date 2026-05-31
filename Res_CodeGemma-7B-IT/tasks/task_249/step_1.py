import sqlite3
import os

# Get a list of all SQLite databases in the current directory
databases = [f for f in os.listdir('.') if f.endswith('.db')]

# Create a dictionary to store table names and their corresponding column names
table_schemas = {}

# Iterate over each database
for database in databases:
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]

    # Iterate over each table
    for table in tables:
        # Get a list of column names for the table
        cursor.execute("PRAGMA table_info({})".format(table))
        columns = [row[1] for row in cursor.fetchall()]

        # Add the table name and column names to the dictionary
        table_schemas[table] = columns

# Find tables with similar schemas across databases
similar_tables = {}
for table1 in table_schemas:
    for table2 in table_schemas:
        if table1 != table2 and table_schemas[table1] == table_schemas[table2]:
            similar_tables.setdefault(table1, []).append(table2)

# Create a consolidation report
report = []
for table, similar_tables in similar_tables.items():
    report.append("## Table: {}".format(table))
    report.append("Similar Tables:")
    for similar_table in similar_tables:
        report.append("* {}".format(similar_table))

# Save the report to a Markdown file
with open('consolidation_report.md', 'w') as f:
    f.write('\n'.join(report))