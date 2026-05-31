# Extract repository details
repo_details = []
for repo in repositories:
    repo_info = {
        'name': repo['name'],
        'owner': repo['owner']['login'],
        'language': repo['language'],
        'stars': repo['stargazers_count'],
        'forks': repo['forks_count']
    }
    repo_details.append(repo_info)

# Save the results to JSON
with open('github_repos_data_science.json', 'w') as f:
    json.dump(repo_details, f, indent=4)

print("Repository details saved to github_repos_data_science.json")