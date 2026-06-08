import requests
from bs4 import BeautifulSoup
import re

url = "https://apod.nasa.gov/apod/astropix.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the title more specifically
title = None

# Look for text that appears to be the title (usually after "Explanation:" or similar)
for element in soup.find_all(text=True):
    if element.strip().startswith("Explanation:") or element.strip().startswith("APOD"):
        # Get the next sibling element which might contain the title
        next_element = element.find_next_sibling()
        if next_element and next_element.name == 'b':
            title = next_element.get_text().strip()
            break
        elif next_element and next_element.name == 'p':
            # Check if this paragraph contains the title
            title_text = next_element.get_text().strip()
            if len(title_text) > 10:  # Filter out very short texts
                title = title_text
                break

# If we still haven't found it, look for the first bold text that's likely to be the title
if not title:
    bold_elements = soup.find_all('b')
    for element in bold_elements:
        text = element.get_text().strip()
        # Look for text that seems like a title (not too short, not too long)
        if 10 < len(text) < 100:
            title = text
            break

print(title if title else "Title not found")