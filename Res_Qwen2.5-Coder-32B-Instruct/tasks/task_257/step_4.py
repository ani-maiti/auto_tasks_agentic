import csv
from collections import defaultdict

def find_largest_duplicate_group(hashes_csv):
    duplicates = defaultdict(list)
    
    with open(hashes_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            files = row['files'].split(', ')
            if len(files) > 1:
                duplicates[row['hash']].extend(files)
    
    if duplicates:
        largest_group = max(duplicates.values(), key=len)
        return largest_group
    else:
        return []

largest_duplicate_group = find_largest_duplicate_group('image_hashes.csv')
print("Largest duplicate group:")
for file in largest_duplicate_group:
    print(file)