import requests
from bs4 import BeautifulSoup

# Fetch the Hacker News homepage
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all post titles
titles = []
for item in soup.find_all("a", class_="storylink"):
    titles.append(item.get_text())
    if len(titles) == 10:
        break

# Print the titles
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")