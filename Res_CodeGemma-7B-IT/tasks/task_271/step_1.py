import sqlite3

# Connect to the database
conn = sqlite3.connect("path/to/database.sqlite")

# Get a list of tables in the database
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Create a list of foreign key relationships
foreign_keys = []
for table in tables:
    table_name = table[0]
    cursor.execute("PRAGMA foreign_key_list({table_name});".format(table_name=table_name))
    foreign_keys.extend(cursor.fetchall())

# Generate schema diagrams in text form
schema = []
for table in tables:
    table_name = table[0]
    cursor.execute("PRAGMA table_info({table_name});".format(table_name=table_name))
    columns = cursor.fetchall()
    schema.append("## Table: {table_name}".format(table_name=table_name))
    schema.append("| Column Name | Data Type | Primary Key | Foreign Key |")
    schema.append("|---|---|---|---|")
    for column in columns:
        column_name, data_type, primary_key, foreign_key, not_null, default_value = column
        schema.append("| {column_name} | {data_type} | {primary_key} | {foreign_key} |".format(
            column_name=column_name,
            data_type=data_type,
            primary_key="Yes" if primary_key else "No",
            foreign_key="Yes" if foreign_key else "No",
        ))

# Save the schema diagrams to Markdown
with open("database_schema.md", "w") as f:
    f.write("\n".join(schema))

# Close the database connection
conn.close()