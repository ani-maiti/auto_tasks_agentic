import json
from collections import Counter

# Load the entity inventory
with open('entity_inventory.json', 'r') as f:
    entity_data = json.load(f)

# Generate a summary report
total_files = len(entity_data)
entity_counts = Counter()

for file_path, entities in entity_data.items():
    for entity_type, values in entities.items():
        entity_counts[entity_type] += len(values)

# Print detailed report
print("=== ENTITY INVENTORY REPORT ===")
print(f"Total text files processed: {total_files}")
print("\nEntities found per type:")
for entity_type, count in entity_counts.most_common():
    print(f"  {entity_type}: {count}")

# Find and print the most common entity type
most_common = entity_counts.most_common(1)[0] if entity_counts else (None, 0)
print(f"\nMost common entity type: {most_common[0]} with {most_common[1]} occurrences")

# Show sample data from one file
print("\nSample entity data:")
for file_path, entities in list(entity_data.items())[:1]:  # Just first file
    print(f"File: {file_path}")
    for entity_type, values in entities.items():
        if values:  # Only show non-empty entity types
            print(f"  {entity_type}: {values}")
    break