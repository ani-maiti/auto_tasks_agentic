# Step 3: Identify columns with similar names and types across databases
def get_columns(database):
    import sqlite3
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    column_info = {}
    for table_name, table_sql in tables:
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for col_name, _, col_type, _, _, _ in columns:
            if col_name not in column_info:
                column_info[col_name] = []
            column_info[col_name].append((database, table_name, col_type))
    return column_info

column_info_all_dbs = {}
for db in databases:
    column_info_all_dbs[db] = get_columns(db)

similar_columns = {}
for col_name, info_list in column_info_all_dbs.items():
    if len(info_list) > 1:
        similar_columns[col_name] = info_list

print(f"Similar columns found: {similar_columns}")