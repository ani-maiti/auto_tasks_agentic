import requests

url = "https://openai.com"
response = requests.get(url, allow_redirects=False)

print(response.status_code)
print(response.headers['Location'])