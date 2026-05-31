import requests

response = requests.get('https://api.github.com/search/repositories', params={'q': 'language:rust', 'sort': 'stars', 'order': 'desc'})

repositories = response.json()['items']

# Extract repository names and stars
repository_info = [(repo['name'], repo['stargazers_count']) for repo in repositories]

# Sort by stars in descending order
repository_info.sort(key=lambda x: x[1], reverse=True)

# Print the top 5 repositories
for name, stars in repository_info[:5]:
    print(f"Repository: {name}, Stars: {stars}")