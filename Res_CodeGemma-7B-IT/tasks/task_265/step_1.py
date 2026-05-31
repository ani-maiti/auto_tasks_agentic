import glob
import re

# Get a list of CSV files
csv_files = glob.glob("*.csv")

# Create an empty list to store the results
results = []

# Iterate through each CSV file
for file_name in csv_files:
    # Open the CSV file
    with open(file_name, "r") as f:
        # Read the first row to get the column headers
        headers = f.readline().strip().split(",")

        # Check each column header for email addresses
        for i, header in enumerate(headers):
            if re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", header):
                results.append({
                    "file_name": file_name,
                    "column_name": header,
                    "column_index": i
                })

# Write the results to a CSV file
with open("email_addresses.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["file_name", "column_name", "column_index"])
    writer.writeheader()
    writer.writerows(results)

# Print a message to the console
print("Email addresses found in the following columns:")
for result in results:
    print(f"- {result['file_name']}, column {result['column_index']}: {result['column_name']}")