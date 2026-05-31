# Import the requests library if it's not already available
try:
    import requests
except ImportError:
    !pip install requests
    import requests

# Re-fetch the top 100 GitHub repositories tagged with 'data-science'
url = "https://api.github.com/search/repositories?q=topic:data-science&sort=stars&order=desc&per_page=100"
response = requests.get(url)

if response.status_code == 200:
    repositories = response.json()['items']
    print("Fetched", len(repositories), "repositories.")
else:
    print("Failed to fetch repositories:", response.status_code)
    exit(1)