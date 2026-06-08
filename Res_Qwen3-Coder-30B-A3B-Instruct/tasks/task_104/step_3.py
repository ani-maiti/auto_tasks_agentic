import urllib.request
from bs4 import BeautifulSoup

# Download the homepage
with urllib.request.urlopen('http://example.com') as response:
    html = response.read()

# Parse the HTML and count links
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
link_count = len(links)

print(link_count)