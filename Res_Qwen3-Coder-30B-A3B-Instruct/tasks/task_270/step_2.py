import json
import re
from collections import Counter

# Read the Markdown file
with open('./csv_primary_key_report.md', 'r') as f:
    content = f.read()

# Find all code fences
code_fences = re.findall(r'```(\w*)\n(.*?)```', content, re.DOTALL)

# Extract languages
languages = [lang for lang, _ in code_fences if lang]

# Count occurrences
language_counts = Counter(languages)

# Find most common language
most_common = language_counts.most_common(1)[0] if language_counts else (None, 0)

# Save statistics to JSON
stats = {
    "most_common_language": most_common[0],
    "count": most_common[1],
    "all_languages": dict(language_counts)
}

with open('language_stats.json', 'w') as f:
    json.dump(stats, f, indent=2)

print(json.dumps(stats, indent=2))