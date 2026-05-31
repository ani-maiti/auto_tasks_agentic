import os

# Get all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Initialize variables for the widest date range
widest_date_range = None
widest_file = None

# Iterate over CSV files
for file in csv_files:
    # Read the CSV file
    with open(file, 'r') as f:
        reader = csv.reader(f)

        # Get column headers
        headers = next(reader)

        # Check if any column contains a date
        for header in headers:
            for row in reader:
                try:
                    # Attempt to convert the value to a datetime object
                    date = datetime.strptime(row[headers.index(header)], '%Y-%m-%d')
                    
                    # If the date is earlier than the current widest date, update it
                    if widest_date_range is None or date > widest_date_range[1]:
                        widest_date_range = (date, date)
                        widest_file = file
                        
                except ValueError:
                    # If the value cannot be converted to a date, ignore it
                    pass

# Print the widest date range found
print(f"Widest date range found in '{widest_file}': {widest_date_range}")