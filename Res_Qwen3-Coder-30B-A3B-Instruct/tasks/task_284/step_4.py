# Extract all section titles and count occurrences
section_titles = defaultdict(int)
title_file_map = defaultdict(list)

for item in content_inventory:
    for level, title in item['headings']:
        # Normalize title for comparison (lowercase, remove extra whitespace)
        normalized_title = re.sub(r'\s+', ' ', title.strip()).lower()
        section_titles[normalized_title] += 1
        title_file_map[normalized_title].append(item['file'])

# Find duplicates (sections appearing in more than one file)
duplicates = {title: count for title, count in section_titles.items() if count > 1}

# Sort duplicates by frequency
sorted_duplicates = sorted(duplicates.items(), key=lambda x: x[1], reverse=True)

# Print the most duplicated section title
if sorted_duplicates:
    most_duplicated = sorted_duplicates[0]
    print(f"Most duplicated section title: '{most_duplicated[0]}' with {most_duplicated[1]} occurrences")
else:
    print("No duplicates found")
```

stdout:
Most duplicated section title: 'schema' with 3 occurrences

stderr:


return code: 0