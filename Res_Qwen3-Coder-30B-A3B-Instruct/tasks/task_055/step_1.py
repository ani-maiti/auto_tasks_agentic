import requests

try:
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        # GitHub API doesn't directly provide timestamp, so we'll try another approach
        # Let's try a different public API that provides Unix timestamp
        timestamp_response = requests.get('http://worldtimeapi.org/api/ip')
        if timestamp_response.status_code == 200:
            data = timestamp_response.json()
            unix_timestamp = data.get('unixtime')
            if unix_timestamp:
                print(unix_timestamp)
            else:
                print("Unix timestamp not found in response")
        else:
            print(f"Failed to get timestamp: {timestamp_response.status_code}")
    else:
        print(f"Failed to connect to GitHub API: {response.status_code}")
except Exception as e:
    print(f"Error occurred: {e}")