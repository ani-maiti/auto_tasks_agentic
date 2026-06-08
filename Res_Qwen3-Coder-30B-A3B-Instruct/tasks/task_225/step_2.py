import sqlite3
import pandas as pd
from datetime import datetime
import os

# Function to check if a column contains date data
def has_date_column(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        date_tables = []
        for table in tables:
            table_name = table[0]
            # Get column info
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            # Check if any column looks like a date
            has_date = False
            for col in columns:
                col_name = col[1].lower()
                col_type = col[2].lower()
                if 'date' in col_name or 'time' in col_name or 'datetime' in col_type:
                    has_date = True
                    break
            
            if has_date:
                date_tables.append((table_name, columns))
        
        conn.close()
        return date_tables
    except Exception as e:
        print(f"Error checking {db_path}: {e}")
        return []

# Function to count records by year
def count_records_by_year(db_path, table_name, date_column):
    try:
        conn = sqlite3.connect(db_path)
        query = f"SELECT strftime('%Y', {date_column}) as year, COUNT(*) as count FROM {table_name} GROUP BY year ORDER BY year;"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error counting records for {db_path}:{table_name}:{date_column}: {e}")
        return pd.DataFrame()

# Find all SQLite databases
db_paths = [
    "/home/ai_admin/.ipython/profile_default/history.sqlite",
    "/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_CodeGemma-7B-IT/database.db",
    "/home/ai_admin/.config/libaccounts-glib/accounts.db",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/places.sqlite"
]

# Process each database
all_results = []

for db_path in db_paths:
    if os.path.exists(db_path):
        print(f"Processing {db_path}")
        date_tables = has_date_column(db_path)
        
        for table_name, columns in date_tables:
            # Find first date-like column
            date_col = None
            for col in columns:
                col_name = col[1].lower()
                if 'date' in col_name or 'time' in col_name:
                    date_col = col_name
                    break
            
            if date_col:
                print(f"  Table {table_name} has date column {date_col}")
                year_counts = count_records_by_year(db_path, table_name, date_col)
                if not year_counts.empty:
                    year_counts['database'] = db_path
                    year_counts['table'] = table_name
                    all_results.append(year_counts)

# Combine all results
if all_results:
    final_df = pd.concat(all_results, ignore_index=True)
    final_df.to_csv('yearly_counts.csv', index=False)
    
    # Find busiest year
    yearly_totals = final_df.groupby('year')['count'].sum()
    busiest_year = yearly_totals.idxmax()
    busiest_count = yearly_totals.max()
    
    print(f"Busiest year: {busiest_year} with {busiest_count} records")
else:
    print("No date columns found in any database")