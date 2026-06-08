import requests
from bs4 import BeautifulSoup

# Download the homepage
response = requests.get("http://example.com")
html_content = response.text

# Parse the HTML and count links
soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')
link_count = len(links)

print(link_count)