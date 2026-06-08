import requests
from bs4 import BeautifulSoup

# Fetch the Python downloads page
url = "https://www.python.org/downloads/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the latest Python version
# The version is usually in a heading or a prominent div
version_element = soup.find('div', class_='download-button')
if version_element:
    version_text = version_element.get_text()
    print(version_text)
else:
    # Try another approach - look for version in download links
    download_links = soup.find_all('a', class_='download-button')
    if download_links:
        first_link = download_links[0]
        link_text = first_link.get_text()
        print(link_text)
    else:
        # Last resort: check for any version-like text
        all_text = soup.get_text()
        import re
        version_pattern = r'Python\s+(\d+\.\d+\.\d+)'
        match = re.search(version_pattern, all_text)
        if match:
            print(match.group(1))
        else:
            print("Version not found")