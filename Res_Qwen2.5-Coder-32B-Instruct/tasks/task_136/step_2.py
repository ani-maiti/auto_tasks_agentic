with open('sitemap.xml', 'r') as file:
    content = file.read()
urls = content.split('<loc>')
print(f"Number of URLs: {len(urls) - 1}")