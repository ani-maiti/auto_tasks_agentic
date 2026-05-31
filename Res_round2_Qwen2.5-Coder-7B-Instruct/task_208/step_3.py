# Check if we have an API key
if api_key == "YOUR_API_KEY_HERE":
    print("Please replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key.")
else:
    # If we have an API key, try again
    responses = {}
    for city in cities:
        url = f"{base_url}appid={api_key}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            responses[city] = response.json()
        else:
            print(f"Failed to get weather data for {city}")

    print("Weather data retrieved.")