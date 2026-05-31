import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    repositories = data['items'][:5]
    print("Top 5 most starred Python repositories on GitHub:")
    for repo in repositories:
        print(f"{repo['name']} - {repo['html_url']} - Stars: {repo['stargazers_count']}")
else:
    print(f"Failed to fetch repositories. Status code: {response.status_code}")