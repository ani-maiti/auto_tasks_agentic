from bs4 import BeautifulSoup

with open('python_homepage.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    links = soup.find_all('a')
    print(f"Number of links: {len(links)}")