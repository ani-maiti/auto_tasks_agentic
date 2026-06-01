from bs4 import BeautifulSoup

with open('osm_homepage.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    title = soup.title.string
    print(title)