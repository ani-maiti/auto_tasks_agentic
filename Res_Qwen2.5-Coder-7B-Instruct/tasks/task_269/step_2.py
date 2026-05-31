# Step 1: Retrieve the latest one hundred stories from Hacker News
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []
for item in soup.find_all('tr', class_='athing'):
    title_tag = item.find('a', class_='storylink')
    if title_tag:
        title = title_tag.text
        link = title_tag['href']
        if link.startswith('//'):
            link = 'https:' + link
        stories.append((title, link))

print(f"Retrieved {len(stories)} stories.")