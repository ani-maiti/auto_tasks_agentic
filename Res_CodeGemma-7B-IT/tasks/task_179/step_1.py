import os
import csv

# Get all files in the current directory
files = os.listdir(".")

# Create a dictionary to store file sizes
file_sizes = {}

# Iterate over each file and get its size
for file in files:
    file_size = os.path.getsize(file)
    file_sizes[file] = file_size

# Create a list of file sizes in ascending order
file_sizes_sorted = sorted(file_sizes.items(), key=lambda x: x[1])

# Create a CSV writer object
with open("file_sizes.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["File Name", "File Size"])

    # Write the file sizes to the CSV file
    for file, size in file_sizes_sorted:
        writer.writerow([file, size])

print("Histogram of file sizes saved as file_sizes.csv")