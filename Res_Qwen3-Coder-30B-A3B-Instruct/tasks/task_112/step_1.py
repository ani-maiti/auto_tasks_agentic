import requests
from bs4 import BeautifulSoup

# Download the OpenStreetMap homepage
url = "https://www.openstreetmap.org"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract and print the title
    title = soup.find('title')
    if title:
        print(title.text)
    else:
        print("No title found")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")