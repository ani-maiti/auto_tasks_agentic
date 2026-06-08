import requests
from bs4 import BeautifulSoup

# Fetch the Hacker News homepage
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all story links
    stories = soup.find_all('tr', class_='athing')
    
    if stories:
        # Print the structure of the first story to understand the layout
        print("First story HTML:")
        print(stories[0])
    else:
        print("Could not find any stories")
else:
    print(f"Failed to fetch page: {response.status_code}")