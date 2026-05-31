import json

# Define the list of repositories if it's not already available
repositories = [
    {'name': 'repo1', 'owner': 'owner1', 'language': 'Python', 'stars': 100, 'forks': 50},
    {'name': 'repo2', 'owner': 'owner2', 'language': 'R', 'stars': 90, 'forks': 40},
    # Add more repositories as needed
]

# Extract repository details
repo_details = []
for repo in repositories:
    repo_info = {
        'name': repo['name'],
        'owner': repo['owner'],
        'language': repo['language'],
        'stars': repo['stars'],
        'forks': repo['forks']
    }
    repo_details.append(repo_info)

# Save the results to JSON
with open('github_repos_data_science.json', 'w') as f:
    json.dump(repo_details, f, indent=4)

print("Repository details saved to github_repos_data_science.json")