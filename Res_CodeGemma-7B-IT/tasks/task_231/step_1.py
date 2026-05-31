import requests
from bs4 import BeautifulSoup
from collections import Counter

url = "https://docs.python.org/3/library/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titles = []
for h1 in soup.find_all("h1"):
    titles.append(h1.text)

title_keywords = Counter([keyword for title in titles for keyword in title.lower().split()])

top_keywords = title_keywords.most_common(20)

print("Top 20 Title Keywords:")
for keyword, count in top_keywords:
    print(f"{keyword}: {count}")