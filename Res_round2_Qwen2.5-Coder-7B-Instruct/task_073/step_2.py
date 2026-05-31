print("The provided code did not fetch the top story title from Hacker News. Let's try another approach.")

import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    start_index = html_content.find('<span class="storylink">')
    if start_index != -1:
        end_index = html_content.find('</a>', start_index)
        if end_index != -1:
            story_title = html_content[start_index + len('<span class="storylink">'):end_index]
            print(story_title.strip())
        else:
            print("End tag not found.")
    else:
        print("Start tag not found.")
else:
    print(f"Failed to retrieve Hacker News page: {response.status_code}")