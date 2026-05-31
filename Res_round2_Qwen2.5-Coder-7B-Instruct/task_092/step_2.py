print("Top 5 most starred Python repositories on GitHub:")
for repo in repositories:
    print(f"{repo['name']} - {repo['html_url']} - Stars: {repo['stargazers_count']}")