import requests
from bs4 import BeautifulSoup

url = "https://blog.python.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check for the presence of blog entries
entries = soup.find_all('div', class_='post')
if entries:
    latest_entry = entries[0]
    latest_post_title = latest_entry.find('h2', class_='post-title').text.strip()
    print(latest_post_title)
else:
    print("No blog posts found.")