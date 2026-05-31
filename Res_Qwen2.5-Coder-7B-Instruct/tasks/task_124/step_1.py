import requests

url = "https://api.github.com/repos/numpy/numpy"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    stars = data['stargazers_count']
    print(f"The number of stars in the numpy GitHub repository is {stars}.")
else:
    print("Failed to retrieve the number of stars.")