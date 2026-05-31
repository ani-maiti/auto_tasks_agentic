import os
import re
import json
from collections import Counter

# Get all text files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.txt')]

# Create an empty entity inventory
entities = []

# Iterate through each file
for file in files:
    # Open the file
    with open(file, 'r') as f:
        # Read the file contents
        text = f.read()

    # Find dates
    dates = re.findall(r'\b\d{1,2}/\d{1,2}/\d{4}\b', text)
    entities.extend(dates)

    # Find emails
    emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}\b', text)
    entities.extend(emails)

    # Find URLs
    urls = re.findall(r'https?://[a-zA-Z0-9./?&=:_-]*', text)
    entities.extend(urls)

    # Find numbers
    numbers = re.findall(r'\b\d+', text)
    entities.extend(numbers)

# Build an entity inventory
inventory = {entity: entities.count(entity) for entity in entities}

# Save the entity inventory to a JSON file
with open('entities.json', 'w') as f:
    json.dump(inventory, f)

# Generate a report
print('Entity Inventory:')
for entity, count in inventory.items():
    print(f'{entity}: {count}')

# Print the most common entity type
most_common_entity, count = Counter(entities).most_common(1)[0]
print(f'Most Common Entity Type: {most_common_entity}')