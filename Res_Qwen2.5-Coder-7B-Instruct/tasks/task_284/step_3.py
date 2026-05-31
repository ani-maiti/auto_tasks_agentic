import csv
from collections import defaultdict

duplicates = defaultdict(int)

for key, items in content_inventory.items():
    seen = set()
    for item in items:
        if item in seen:
            duplicates[key] += 1
        else:
            seen.add(item)

most_duplicated_section_title = max(duplicates, key=duplicates.get)

print(most_duplicated_section_title)