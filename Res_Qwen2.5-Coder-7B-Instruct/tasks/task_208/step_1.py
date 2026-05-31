import requests

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
base_url = "http://api.openweathermap.org/data/2.5/weather"

responses = []

for city in cities:
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        responses.append(response.json())
    else:
        print(f"Failed to get weather data for {city}")

# Save responses to files
for i, response in enumerate(responses):
    with open(f"weather_{i}.json", "w") as file:
        json.dump(response, file)

print("Weather data saved to files.")