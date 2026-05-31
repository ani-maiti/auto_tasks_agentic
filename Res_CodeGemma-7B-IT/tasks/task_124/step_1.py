import requests

response = requests.get("https://api.github.com/repos/numpy/numpy")

print(response.json()["stargazers_count"])