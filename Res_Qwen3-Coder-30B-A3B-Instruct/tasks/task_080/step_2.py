import json
import urllib.request

url = "https://api.github.com/repos/psf/requests"
with urllib.request.urlopen(url) as response:
    data = response.read()
    decoded_data = data.decode('utf-8')
    repo_info = json.loads(decoded_data)
    print(repo_info['forks_count'])