import requests

api_key = "YOUR_API_KEY"
city = "New York"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    print(f"The current temperature in {city} is {temperature}°C.")
else:
    print(f"Error fetching weather data: {response.status_code}")