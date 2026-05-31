from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "xml")

urls = [loc.text for loc in soup.find_all("loc")]

print(len(urls))
```
execution trace:
stdout:
4400


stderr:


return code: 0