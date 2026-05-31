from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")

print(f"Number of links: {len(links)}")
```
execution trace:
stdout:
Number of links: 2

stderr:


return code: 0