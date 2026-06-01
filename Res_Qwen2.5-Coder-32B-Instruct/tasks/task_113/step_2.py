from bs4 import BeautifulSoup

with open('kernel_homepage.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
print(title)