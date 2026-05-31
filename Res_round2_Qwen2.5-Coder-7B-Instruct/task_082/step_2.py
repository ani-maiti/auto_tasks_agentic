import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blog/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check if the blog title exists before trying to extract it
if soup.find('h2', class_='blog-title'):
    latest_post_title = soup.find('h2', class_='blog-title').text.strip()
else:
    latest_post_title = "Blog title not found"

print(latest_post_title)