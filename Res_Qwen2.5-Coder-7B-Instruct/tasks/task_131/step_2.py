import requests
from bs4 import BeautifulSoup

url = "https://blog.mozilla.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check if the post title exists before trying to extract it
if soup.find('h2', class_='entry-title'):
    latest_post_title = soup.find('h2', class_='entry-title').text.strip()
    print(latest_post_title)
else:
    print("No blog posts found.")