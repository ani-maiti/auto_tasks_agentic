import requests

url = "https://www.wikipedia.org/robots.txt"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
elif response.status_code == 301:
    new_url = response.headers['Location']
    print(f"Redirected to: {new_url}")
    response = requests.get(new_url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed to retrieve robots.txt after redirect. Status code: {response.status_code}")
else:
    print(f"Failed to retrieve robots.txt. Status code: {response.status_code}")