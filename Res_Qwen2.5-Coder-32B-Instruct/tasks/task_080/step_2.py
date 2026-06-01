import json
import requests

response = requests.get('https://api.github.com/repos/psf/requests')
data = response.json()
print(f"Number of forks: {data['forks_count']}")