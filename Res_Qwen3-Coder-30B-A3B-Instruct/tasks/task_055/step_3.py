import requests

try:
    # Try yet another API
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=APIKEY', timeout=10)
    if response.status_code == 200:
        data = response.json()
        # Check if there's a timestamp in the response
        print(data)
    else:
        print(f"Failed to get data: {response.status_code}")
except Exception as e:
    print(f"Error occurred: {e}")