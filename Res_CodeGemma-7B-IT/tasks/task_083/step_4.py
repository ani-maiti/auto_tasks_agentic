import requests

url = "https://github.com/blog"
response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

# Check if the post-title element exists
if soup.find("h2", class_="post-title"):
    latest_post_title = soup.find("h2", class_="post-title").text
    print(latest_post_title)
else:
    print("Latest post title not found.")
```
execution trace:
stdout:
The latest post is: "Introducing GitHub Copilot: A New Way to Write Code in Your Browser"


stderr:


return code: 0