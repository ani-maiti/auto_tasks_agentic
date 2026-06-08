import requests
from bs4 import BeautifulSoup

# Fetch the Ubuntu download page
url = "https://ubuntu.com/download/server"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Look for version information in the page
page_text = soup.get_text()
versions = []
for line in page_text.split('\n'):
    if 'Ubuntu' in line and '.' in line:
        # Extract version numbers
        parts = line.strip().split()
        for part in parts:
            if part.count('.') == 1 and part.replace('.', '').isdigit():
                versions.append(part)

# Print the first version found
if versions:
    print(f"Latest Ubuntu release version: {versions[0]}")
else:
    print("Could not determine Ubuntu version from the webpage.")