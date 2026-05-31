from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string
print(title)