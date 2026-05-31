import requests
from bs4 import BeautifulSoup

url = "https://kubernetes.io/blog/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check if the blog post title exists
latest_post_title = soup.find('h2', class_='blog-post-title')
if latest_post_title:
    latest_post_title = latest_post_title.text.strip()
else:
    latest_post_title = "Blog post title not found"

print(latest_post_title)