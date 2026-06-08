# Since we can't actually access a weather API without credentials,
# let's create mock weather data for demonstration purposes
mock_weather_data = []

for i, city in enumerate(cities):
    # Generate mock temperature data (in Fahrenheit)
    temp = random.randint(-20, 100)
    humidity = random.randint(30, 95)
    pressure = random.randint(980, 1040)
    
    # Create a more realistic climate characteristic based on temperature
    if temp < 32:
        climate = "Cold"
    elif temp < 60:
        climate = "Cool"
    elif temp < 80:
        climate = "Warm"
    else:
        climate = "Hot"
        
    mock_weather_data.append({
        'city': city,
        'temperature': temp,
        'humidity': humidity,
        'pressure': pressure,
        'climate': climate
    })

print("Generated mock weather data for all cities")
print(f"Sample data: {mock_weather_data[:3]}")