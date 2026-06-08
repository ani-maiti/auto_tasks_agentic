import requests

try:
    response = requests.get("https://some-random-api.ml/facts/dog")
    if response.status_code == 200:
        data = response.json()
        print(data['fact'])
    else:
        print("Failed to retrieve dog fact")
except Exception as e:
    print(f"Error: {e}")