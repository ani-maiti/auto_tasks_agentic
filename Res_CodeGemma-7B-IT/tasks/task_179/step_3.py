import csv

# Read file sizes from CSV file
file_sizes = []
with open("file_sizes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        file_sizes.append(int(row[1]))

# Create a histogram of file sizes
# ... (same as in the previous code block)