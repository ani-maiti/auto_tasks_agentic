import requests

api_key = "YOUR_API_KEY"
city_id = "1850144"

url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    print(f"Current temperature in Tokyo: {temperature}°C")
else:
    print(f"Error: {response.status_code}")