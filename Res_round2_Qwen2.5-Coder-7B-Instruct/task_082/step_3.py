import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blog/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check for alternative blog title structure
if soup.find('h3', class_='blog-title'):
    latest_post_title = soup.find('h3', class_='blog-title').text.strip()
elif soup.find('h2', class_='post-title'):
    latest_post_title = soup.find('h2', class_='post-title').text.strip()
else:
    latest_post_title = "Blog title not found"

print(latest_post_title)