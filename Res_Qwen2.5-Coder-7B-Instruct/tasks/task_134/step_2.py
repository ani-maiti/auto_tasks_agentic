from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
latest_post_title = soup.find('h2', class_='blog-post-title').text.strip()
print(latest_post_title)