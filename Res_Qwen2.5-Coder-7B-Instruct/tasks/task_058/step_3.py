from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
latest_release_tag = soup.find('h1', class_='release-header')

if latest_release_tag:
    latest_release_version = latest_release_tag.text.strip()
    print(f"The latest Python release version is: {latest_release_version}")
else:
    print("Could not find the latest Python release version.")