import requests
from bs4 import BeautifulSoup

url = "https://blog.mozilla.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all blog post titles
post_titles = soup.find_all('h2', class_='entry-title')

if post_titles:
    latest_post_title = post_titles[0].text.strip()
    print(latest_post_title)
else:
    print("No blog posts found.")