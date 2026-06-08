import json

# Read the saved JSON file to verify its contents
with open('weather_forecast_data.json', 'r') as f:
    data = json.load(f)

print("Weather forecast data loaded successfully:")
print(json.dumps(data, indent=2))

# Verify the city with highest variability
max_var_city = max(data, key=lambda x: data[x]['variability'])
print(f"\nCity with highest forecast variability: {max_var_city}")
print(f"Variability score: {data[max_var_city]['variability']:.2f}")