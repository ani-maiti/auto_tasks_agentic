import os
import re
import json

# Get all Markdown files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.md')]

# Initialize variables
languages = {}

# Iterate over files
for file in files:
    # Read the file
    with open(file, 'r') as f:
        contents = f.read()

    # Extract code fences
    code_blocks = re.findall(r'```(.*?)```', contents, re.MULTILINE)

    # Update language statistics
    for code_block in code_blocks:
        language = code_block.split('\n')[0]
        languages[language] = languages.get(language, 0) + 1

# Sort languages by frequency
sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

# Create a dictionary of statistics
stats = {
    'files_analyzed': len(files),
    'most_common_language': sorted_languages[0][0],
    'language_stats': {lang: count for lang, count in sorted_languages}
}

# Save statistics to JSON
with open('language_stats.json', 'w') as f:
    json.dump(stats, f)

# Print a message
print("Language statistics saved to language_stats.json")