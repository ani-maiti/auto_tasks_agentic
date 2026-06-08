import requests
from bs4 import BeautifulSoup

# Let's try a more targeted approach to get the exact latest version
url = "https://www.python.org/downloads/release/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Look for the latest release in the releases list
releases = soup.find_all('li', class_='release')
if releases:
    # Get the first release (most recent)
    latest_release = releases[0]
    release_title = latest_release.find('h3')
    if release_title:
        title_text = release_title.get_text()
        # Extract version number from title like "Python 3.14.5"
        import re
        version_match = re.search(r'Python\s+(\d+\.\d+\.\d+)', title_text)
        if version_match:
            print(version_match.group(1))
        else:
            print("Could not extract version from title")
    else:
        print("No title found in release")
else:
    print("No releases found")