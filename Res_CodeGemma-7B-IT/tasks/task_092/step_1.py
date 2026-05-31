from github import Github

# Authenticate with GitHub
g = Github("YOUR_GITHUB_TOKEN")

# Get the list of Python repositories
python_repos = g.search_repositories(query="language:python")

# Sort the repositories by stars in descending order
python_repos = sorted(python_repos, key=lambda r: r.stargazers_count, reverse=True)

# Get the top 5 repositories
top_5_repos = python_repos[:5]

# Print the top 5 repositories
for repo in top_5_repos:
    print(f"{repo.name}: {repo.stargazers_count}")