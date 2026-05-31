# Ensure the repositories variable is properly defined before accessing it
if 'repositories' in locals():
    # Extract relevant information from the fetched repositories
    repo_data = []
    for repo in repositories:
        repo_info = {
            'name': repo['name'],
            'owner': repo['owner']['login'],
            'language': repo['language'],
            'stars': repo['stargazers_count'],
            'forks': repo['forks_count'],
            'open_issues': repo['open_issues_count']
        }
        repo_data.append(repo_info)

    print("Extracted data for", len(repo_data), "repositories.")
else:
    print("Repositories data is missing.")