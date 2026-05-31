import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Get a list of all tables in the database
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

# Create a dictionary to store column information
columns = {}

# Iterate over each table
for table in tables:
    # Get a list of columns in the table
    table_columns = conn.execute("PRAGMA table_info({})".format(table[0])).fetchall()

    # Add column information to the dictionary
    for column in table_columns:
        if column[1] not in columns:
            columns[column[1]] = []
        columns[column[1]].append((table[0], column[2]))

# Close the database connection
conn.close()

# Create a dictionary to store inferred relationships
relationships = {}

# Iterate over the columns
for column, tables in columns.items():
    # Check for columns with similar names and types
    for i in range(len(tables)):
        for j in range(i + 1, len(tables)):
            if tables[i][0] != tables[j][0] and tables[i][1] == tables[j][1]:
                # Add the relationship to the dictionary
                if (tables[i][0], tables[j][0]) not in relationships:
                    relationships[(tables[i][0], tables[j][0])] = []
                relationships[(tables[i][0], tables[j][0])].append((column, tables[i][1]))

# Save the results to JSON
import json
with open("relationships.json", "w") as f:
    json.dump(relationships, f)

# Print the strongest inferred relationship
strongest_relationship = max(relationships, key=len)
print("Strongest inferred relationship:", strongest_relationship)