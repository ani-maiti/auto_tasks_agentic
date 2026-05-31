from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
latest_post_title = soup.find('h1', class_='post-title').text.strip()
print(latest_post_title)