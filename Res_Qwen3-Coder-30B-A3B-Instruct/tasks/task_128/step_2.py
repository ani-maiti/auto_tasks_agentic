import requests

try:
    response = requests.get("https://dog-api.kinduff.com/api/facts")
    if response.status_code == 200:
        data = response.json()
        print("Raw response:", data)
    else:
        print("Failed to retrieve dog fact")
except Exception as e:
    print(f"Error: {e}")