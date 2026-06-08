import requests

try:
    # Try a different timestamp API
    response = requests.get('https://www.timeapi.io/api/Time/current/zone?timeZone=UTC', timeout=10)
    if response.status_code == 200:
        data = response.json()
        # Extract timestamp from the response
        timestamp = data.get('totalMilliseconds')
        if timestamp:
            print(timestamp)
        else:
            print("Timestamp not found in response")
    else:
        print(f"Failed to get timestamp: {response.status_code}")
except Exception as e:
    print(f"Error occurred: {e}")