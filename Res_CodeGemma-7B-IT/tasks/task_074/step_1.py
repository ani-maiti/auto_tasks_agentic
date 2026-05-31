import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

response = requests.get(url)

if response.status_code == 200:
    story_ids = response.json()[:5]
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
        story_response = requests.get(story_url)
        if story_response.status_code == 200:
            story_data = story_response.json()
            print(story_data["title"])
else:
    print("Error fetching story IDs.")