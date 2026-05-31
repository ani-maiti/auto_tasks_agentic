import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    story_titles = soup.find_all('a', class_='storylink')
    if story_titles:
        top_story_title = story_titles[0].get_text()
        print(top_story_title)
    else:
        print("No story titles found.")
else:
    print(f"Failed to retrieve Hacker News page: {response.status_code}")