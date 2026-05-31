import json

# Load repositories from JSON file
with open("repositories.json", "r") as f:
    repositories = json.load(f)

# Print language statistics
print("Language Statistics:")
language_counts = {}
for repo in repositories:
    language = repo["language"]
    language_counts[language] = language_counts.get(language, 0) + 1
for language, count in language_counts.items():
    print(f"{language}: {count}")