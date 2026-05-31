# Check if API key is valid
url = "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=New York"
response = requests.get(url)
if response.status_code != 200:
    print("Invalid API key. Please check your API key.")
else:
    print("API key is valid.")