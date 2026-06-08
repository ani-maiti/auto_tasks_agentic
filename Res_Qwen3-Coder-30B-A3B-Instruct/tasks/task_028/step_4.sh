python3 -c "
import csv
with open('largest_files.txt', 'r') as f:
    lines = f.readlines()

with open('largest_files.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Size (bytes)', 'File Path'])
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            size, path = parts
            writer.writerow([size, path])
"