import json

with open('github_repos.json', 'r') as f:
    data = json.load(f)

# Print the most starred repository
most_starred = max(data['repositories'], key=lambda x: x['stars'])
print(f"Most starred repository: {most_starred['name']} with {most_starred['stars']} stars")