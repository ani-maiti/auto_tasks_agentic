from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("https://www.openstreetmap.org/")
soup = BeautifulSoup(response.read(), "html.parser")
title = soup.title.string

print(title)