import json

# Open the entity inventory file
with open('entities.json', 'r') as f:
    inventory = json.load(f)

# Print the most common entity type
most_common_entity, count = sorted(inventory.items(), key=lambda x: x[1], reverse=True)[0]
print(f'Most Common Entity Type: {most_common_entity}')
```
execution trace:
stdout:
Most Common Entity Type: 100


stderr:


return code: 0