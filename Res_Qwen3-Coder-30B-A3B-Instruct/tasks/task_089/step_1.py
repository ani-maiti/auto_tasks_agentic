import requests
from bs4 import BeautifulSoup

# Fetch the Wikipedia page for Linux
url = "https://en.wikipedia.org/wiki/Linux"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the title element
    title = soup.find('h1', {'class': 'firstHeading'})
    
    # Extract and print the text
    if title:
        print(title.text)
    else:
        print("Title not found")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")