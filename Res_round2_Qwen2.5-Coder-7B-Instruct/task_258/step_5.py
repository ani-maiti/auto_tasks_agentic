import json

# Load the repository details from JSON
with open('github_repos_data_science.json', 'r') as f:
    repo_details = json.load(f)

# Classify repositories by language
language_counts = {}
for repo in repo_details:
    language = repo['language']
    if language in language_counts:
        language_counts[language] += 1
    else:
        language_counts[language] = 1

# Print language statistics
print(json.dumps(language_counts, indent=4))