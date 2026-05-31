import os
import csv

# Set the directory to search
directory = "/path/to/directory"

# Set the minimum file size in bytes
min_size = 1048576

# Create a list to store file information
file_list = []

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Get the full path to the file
    file_path = os.path.join(directory, filename)

    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Get the file size in bytes
        file_size = os.path.getsize(file_path)

        # Check if the file size meets the minimum threshold
        if file_size > min_size:
            # Add file information to the list
            file_list.append([filename, file_size])

# Create a CSV writer object
csv_file = open("large_files.csv", "w")
csv_writer = csv.writer(csv_file)

# Write the CSV header
csv_writer.writerow(["File Name", "File Size (Bytes)"])

# Write the file information to the CSV file
for filename, file_size in file_list:
    csv_writer.writerow([filename, file_size])

# Close the CSV file
csv_file.close()

# Print a success message
print("CSV report generated successfully.")