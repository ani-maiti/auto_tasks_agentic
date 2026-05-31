from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
print(len(links))