import os
import sqlite3
import csv

databases = [
    "/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_CodeGemma-7B-IT/database.db"
]

results = []

for db_path in databases:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        
        # Check if table has a date column
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        date_columns = [col[1] for col in columns if 'date' in col[2].lower()]
        
        if date_columns:
            for date_col in date_columns:
                # Count records by year
                cursor.execute(f"SELECT strftime('%Y', {date_col}) AS year, COUNT(*) AS count FROM {table_name} GROUP BY year;")
                yearly_counts = cursor.fetchall()
                
                for year, count in yearly_counts:
                    results.append({
                        "database": db_path,
                        "table": table_name,
                        "date_column": date_col,
                        "year": year,
                        "count": count
                    })

# Save results to CSV
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['database', 'table', 'date_column', 'year', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# Print the busiest year
busiest_year = max(results, key=lambda x: x['count'])['year']
print(f"The busiest year is: {busiest_year}")