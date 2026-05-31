import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)

if response.status_code == 200:
    top_story_ids = response.json()
    if top_story_ids:
        story_id = top_story_ids[0]
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        if story_response.status_code == 200:
            story_data = story_response.json()
            title = story_data.get("title")
            if title:
                print(f"Top Story Title: {title}")
            else:
                print("No title found for the top story.")
        else:
            print(f"Failed to retrieve story details. Status code: {story_response.status_code}")
    else:
        print("No stories found.")
else:
    print(f"Failed to retrieve top stories. Status code: {response.status_code}")