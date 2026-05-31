import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)

if response.status_code == 200:
    top_stories = response.json()
    if len(top_stories) > 5:
        for i in range(5):
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{top_stories[i]}.json"
            item_response = requests.get(item_url)
            if item_response.status_code == 200:
                item_data = item_response.json()
                title = item_data.get("title", "No Title")
                print(f"{i+1}. {title}")
else:
    print("Failed to retrieve top stories.")