import requests
import json

# GitHub API endpoint for searching repositories
url = "https://api.github.com/search/repositories"

# Parameters for the search
params = {
    'q': 'machine-learning',
    'sort': 'updated',
    'order': 'desc',
    'per_page': 100
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract repository information
    repos = []
    for repo in data['items']:
        repos.append({
            'name': repo['full_name'],
            'stars': repo['stargazers_count'],
            'forks': repo['forks_count']
        })
    
    # Calculate averages
    total_stars = sum(repo['stars'] for repo in repos)
    total_forks = sum(repo['forks'] for repo in repos)
    avg_stars = total_stars / len(repos)
    avg_forks = total_forks / len(repos)
    
    # Save to JSON file
    result = {
        'repositories': repos,
        'average_stars': avg_stars,
        'average_forks': avg_forks
    }
    
    with open('github_repos.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    # Find the most starred repository
    most_starred = max(repos, key=lambda x: x['stars'])
    
    # Print results
    print(f"Average stars: {avg_stars:.2f}")
    print(f"Average forks: {avg_forks:.2f}")
    print(f"Most starred repository: {most_starred['name']} with {most_starred['stars']} stars")
    
else:
    print(f"Error: {response.status_code}")
    print(response.text)