import csv
from collections import Counter

# Save inventory to CSV
with open('archive_inventory.csv', 'w', newline='') as csvfile:
    fieldnames = ['filename', 'archives']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for filename, archives in inventory.items():
        writer.writerow({'filename': filename, 'archives': ', '.join(archives)})

# Generate report
duplicates = {filename: archives for filename, archives in inventory.items() if len(archives) > 1}

with open('duplicate_report.txt', 'w') as reportfile:
    reportfile.write("Duplicate Files Report\n")
    reportfile.write("======================\n")
    for filename, archives in duplicates.items():
        reportfile.write(f"{filename}: Found in {len(archives)} archives - {', '.join(archives)}\n")

# Print the most frequently occurring filename
filename_counts = Counter(filename for filename in inventory.keys())
most_frequent_filename = filename_counts.most_common(1)[0]
print(f"Most frequently occurring filename: {most_frequent_filename[0]} (occurred {most_frequent_filename[1]} times)")