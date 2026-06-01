import json

# Get the top 50 story IDs
story_ids = [int(id) for id in open('topstories.json').read().strip().split(', ')[:50]]

# Prepare a list to store story data
stories = []

# Function to fetch story details
def fetch_story(story_id):
    import requests
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    return response.json()

# Fetch and store the first story to check structure
first_story = fetch_story(story_ids[0])
stories.append(first_story)

# Print the first story to inspect its structure
print(json.dumps(first_story, indent=2))