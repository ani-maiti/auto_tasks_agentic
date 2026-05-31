# Update the code to include the metadata variable
# List of popular Python repositories
repositories = [
    'numpy',
    'pandas',
    'scikit-learn',
    'tensorflow',
    'pytorch'
]

# Function to retrieve GitHub metadata for a repository
def get_repo_metadata(repo):
    url = f'https://api.github.com/repos/{repo}'
    response = requests.get(url)
    data = response.json()
    if 'stargazers_count' in data:
        return {
            'stars': data['stargazers_count'],
            'forks': data['forks_count'],
            'issues': data['open_issues_count']
        }
    else:
        return None

# Create a list to store the metadata
metadata = []

# Retrieve metadata for each repository
for repo in repositories:
    metadata.append(get_repo_metadata(repo))

# Check if metadata could be retrieved for all repositories
if any(metadata is None for metadata in metadata):
    print('Error: Could not retrieve metadata for all repositories.')
    exit(1)