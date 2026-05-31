import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY")

if response.status_code == 200:
    data = response.json()
    print(f"Current weather in London: {data['weather'][0]['description']}")
else:
    print("Error retrieving weather data.")