import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(response.text, "html.parser")

top_story_link = soup.find("a", class_="storylink")
top_story_title = top_story_link.text.strip()

print(top_story_title)