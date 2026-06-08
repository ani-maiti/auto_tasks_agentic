import requests
import json

# Fetch the latest XKCD comic metadata
response = requests.get('https://xkcd.com/info.0.json')
if response.status_code == 200:
    data = response.json()
    latest_comic_number = data['num']
    print(f"Latest XKCD comic number: {latest_comic_number}")
    
    # Now fetch the specific comic to get the title
    comic_response = requests.get(f'https://xkcd.com/{latest_comic_number}/info.0.json')
    if comic_response.status_code == 200:
        comic_data = comic_response.json()
        print(comic_data['title'])
    else:
        print("Failed to fetch comic data")
else:
    print("Failed to fetch latest comic info")