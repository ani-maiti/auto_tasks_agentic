import sqlite3
import os
import re
import shutil
from collections import defaultdict

# Get all SQLite databases in the current directory tree
def get_sqlite_databases():
    sqlite_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".sqlite"):
                sqlite_files.append(os.path.join(root, file))
    return sqlite_files

# Extract schemas and indexes for a SQLite database
def extract_schema_and_indexes(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    schema = {}
    indexes = {}
    for row in cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';"):
        table_name = row[0]
        schema[table_name] = row[1]
    for row in cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='index';"):
        index_name = row[0]
        indexes[index_name] = row[1]
    conn.close()
    return schema, indexes

# Identify tables with similar structures across databases
def find_similar_tables(schemas):
    similar_tables = defaultdict(list)
    for db, schema in schemas.items():
        for table1, ddl1 in schema.items():
            for table2, ddl2 in schema.items():
                if table1 != table2 and similar_tables(ddl1, ddl2):
                    similar_tables[table1].append(table2)
    return similar_tables

# Generate a consolidation report
def generate_consolidation_report(similar_tables):
    report = ""
    for table1, similar_tables in similar_tables.items():
        report += f"## Table: {table1}\n"
        report += "\n"
        for table2 in similar_tables:
            report += f"* {table2}\n"
        report += "\n"
    return report

# Estimate merge opportunities
def estimate_merge_opportunities(schemas):
    opportunities = 0
    for db, schema in schemas.items():
        for table1, ddl1 in schema.items():
            for table2, ddl2 in schema.items():
                if table1 != table2 and similar_tables(ddl1, ddl2):
                    opportunities += 1
    return opportunities

# Save the results to Markdown
def save_to_markdown(report, opportunities):
    with open("consolidation_report.md", "w") as f:
        f.write(report)
    with open("merge_opportunities.txt", "w") as f:
        f.write(f"Estimated merge opportunities: {opportunities}")

# Print the most similar table pair
def print_most_similar_tables(similar_tables):
    most_similar_pair = max(similar_tables.items(), key=lambda x: len(x[1]))
    print(f"Most similar table pair: {most_similar_pair}")

# Main execution
sqlite_files = get_sqlite_databases()
schemas = {}
for db_file in sqlite_files:
    schemas[db_file] = extract_schema_and_indexes(db_file)
similar_tables = find_similar_tables(schemas)
report = generate_consolidation_report(similar_tables)
opportunities = estimate_merge_opportunities(schemas)
save_to_markdown(report, opportunities)
print_most_similar_tables(similar_tables)