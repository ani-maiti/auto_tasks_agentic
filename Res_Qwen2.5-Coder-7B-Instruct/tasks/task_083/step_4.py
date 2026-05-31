import requests
from bs4 import BeautifulSoup

url = "https://github.com/blog"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_post_title = soup.find('h1', class_='post-title')
    if latest_post_title:
        latest_post_title = latest_post_title.text.strip()
        print(latest_post_title)
    else:
        print("No blog post title found.")
else:
    print(f"Failed to retrieve the GitHub blog page. Status code: {response.status_code}")