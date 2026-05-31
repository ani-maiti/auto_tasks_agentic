import requests

url = "https://hacker-news.firebaseio.com/v0/item/18366604.json?print=pretty"

response = requests.get(url)

if response.status_code == 200:
    story_data = response.json()
    print(story_data["title"])
else:
    print("Error fetching story data.")