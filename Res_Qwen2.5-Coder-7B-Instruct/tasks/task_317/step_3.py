import json

# Step 6: Load the JSON data
with open('website_index.json', 'r') as f:
    data = json.load(f)

# Step 7: Flatten the list of headings into a single list
all_headings = [heading for item in data for heading in item['headings']]

# Step 8: Count the frequency of each heading
from collections import Counter
heading_counts = Counter(all_headings)

# Step 9: Find the most common heading
most_common_heading, count = heading_counts.most_common(1)[0]

print(f"The most common heading is '{most_common_heading}' with {count} occurrences.")