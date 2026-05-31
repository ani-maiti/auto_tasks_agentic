import os
import re
import json

# Find all Markdown files
markdown_files = [f for f in os.listdir('.') if f.endswith('.md')]

# Initialize data structures
code_blocks = []
language_counts = {}

# Iterate over Markdown files
for file in markdown_files:
    # Open the file
    with open(file, 'r') as f:
        # Read the file content
        content = f.read()

        # Extract code blocks
        for line in content.splitlines():
            if line.startswith('```'):
                code_block = []
                language = None
            elif line.startswith('```') and language is not None:
                # Add code block to list
                code_blocks.append({
                    'language': language,
                    'code': '\n'.join(code_block)
                })
                # Increment language count
                language_counts[language] = language_counts.get(language, 0) + 1
                code_block = []
                language = None
            else:
                code_block.append(line)

# Save code block statistics to JSON
with open('code_blocks.json', 'w') as f:
    json.dump({
        'code_blocks': code_blocks,
        'language_counts': language_counts
    }, f)