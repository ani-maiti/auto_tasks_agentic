import requests
from bs4 import BeautifulSoup

url = "https://apod.nasa.gov/apod/astropix.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Look for the title in different possible locations
title = None

# Try finding title in bold tags
bold_tags = soup.find_all('b')
for tag in bold_tags:
    text = tag.get_text().strip()
    if text and len(text) > 10:  # Filter out very short texts
        title = text
        break

# If no suitable bold text found, try meta description
if not title:
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        title = meta_desc.get('content', '')

# If still no title, try to find it in h1 or h2 tags
if not title:
    heading_tags = soup.find_all(['h1', 'h2'])
    for tag in heading_tags:
        text = tag.get_text().strip()
        if text and len(text) > 5:
            title = text
            break

print(title if title else "Title not found")