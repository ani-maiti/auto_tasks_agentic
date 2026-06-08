import requests
from bs4 import BeautifulSoup

# Download the homepage
response = requests.get('https://www.python.org')
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all link elements
links = soup.find_all('a')

# Count the links
link_count = len(links)

print(f"Number of links found: {link_count}")