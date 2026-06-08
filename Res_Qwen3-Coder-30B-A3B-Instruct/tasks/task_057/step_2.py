import requests
import json

# Get the latest XKCD comic info
response = requests.get('https://xkcd.com/info.0.json')
latest_comic = response.json()
latest_num = latest_comic['num']

# Fetch the alt text of the latest comic
comic_response = requests.get(f'https://xkcd.com/{latest_num}/info.0.json')
comic_data = comic_response.json()

print(comic_data['alt'])