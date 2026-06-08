import requests
from bs4 import BeautifulSoup

# Fetch the Wikipedia page for Python programming language
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the title of the page
    title = soup.find('h1', {'class': 'firstHeading'}).text
    
    # Print the title
    print(title)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")