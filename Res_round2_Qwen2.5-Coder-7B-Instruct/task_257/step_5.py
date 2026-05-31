import csv

# Read the CSV file containing duplicate groups
with open('duplicate_images.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    duplicate_groups = list(reader)

# Sort duplicate groups by size
sorted_duplicate_groups = sorted(duplicate_groups, key=lambda x: len(x), reverse=True)

# Print the largest duplicate group
if sorted_duplicate_groups:
    largest_group = sorted_duplicate_groups[0]
    print("Largest duplicate group:")
    for path in largest_group:
        print(path)
else:
    print("No duplicate groups found.")