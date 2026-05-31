import json

# Load code block data from JSON file
with open('code_blocks.json', 'r') as f:
    data = json.load(f)

# Extract code blocks and language counts
code_blocks = data['code_blocks']
language_counts = data['language_counts']

# Print statistics
print('Code block statistics:')
for language, count in language_counts.items():
    print(f'- {language}: {count}')
```
execution trace:
stdout:
Code block statistics:
- python: 2
- javascript: 1


stderr:


return code: 0