import requests

try:
    response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")
    if response.status_code == 200:
        data = response.json()
        print(data[0]['fact'])
    else:
        print("Failed to retrieve dog fact")
except Exception as e:
    print(f"Error: {e}")