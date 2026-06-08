import json

# Load the saved weather data
with open('weather_responses.json', 'r') as f:
    weather_data = json.load(f)

# Display all retrieved data
print("All European Capital Weather Data:")
print("-" * 50)
for item in weather_data:
    print(f"{item['city']}: {item['temperature']}°C ({item['description']})")

print("\n" + "="*50)
print("Summary Statistics:")
print(f"Total cities processed: {len(weather_data)}")
print(f"Average temperature: {sum(item['temperature'] for item in weather_data)/len(weather_data):.2f}°C")

# Find and display the warmest capital
warmest = max(weather_data, key=lambda x: x['temperature'])
print(f"Warmest capital: {warmest['city']} with {warmest['temperature']}°C")