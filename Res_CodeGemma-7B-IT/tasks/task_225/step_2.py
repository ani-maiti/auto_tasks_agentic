# Check if the database file exists
import os
if not os.path.isfile('path/to/database.db'):
    print('Error: Database file does not exist.')
    exit(1)

# Connect to the database
conn = sqlite3.connect('path/to/database.db')

# Get a cursor object
cursor = conn.cursor()

# Get a list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Create a dictionary to store the record counts by year
year_counts = {}

# Iterate over the tables
for table in tables:
    # Get the column names for the table
    cursor.execute("PRAGMA table_info('" + table[0] + "');")
    columns = cursor.fetchall()

    # Check if the table contains a date column
    has_date_column = False
    for column in columns:
        if column[1] == 'date':
            has_date_column = True
            break

    # If the table contains a date column, get the record count by year
    if has_date_column:
        cursor.execute("SELECT strftime('%Y', " + column[1] + ") AS year, COUNT(*) AS count FROM " + table[0] + " GROUP BY year;")
        year_counts.update(cursor.fetchall())

# Close the database connection
conn.close()

# Save the results to a CSV file
with open('year_counts.csv', 'w') as f:
    f.write('year,count\n')
    for year, count in year_counts.items():
        f.write(str(year) + ',' + str(count) + '\n')

# Print the busiest year
busiest_year = max(year_counts, key=year_counts.get)
print('The busiest year is:', busiest_year)