import requests
from bs4 import BeautifulSoup

# Fetch the Hacker News homepage
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the first story link (top story)
    first_story = soup.find('tr', class_='athing')
    
    if first_story:
        # Get the title from the first story
        title_element = first_story.find('span', class_='titleline')
        if title_element:
            title = title_element.get_text(strip=True)
            print(title)
        else:
            print("Could not find title element")
    else:
        print("Could not find first story")
else:
    print(f"Failed to fetch page: {response.status_code}")