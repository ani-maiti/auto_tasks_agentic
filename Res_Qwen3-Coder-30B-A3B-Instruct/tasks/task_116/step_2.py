import requests

# Using OpenWeatherMap API to get weather data for Sydney
# Since we don't have an API key, let's try a different approach
# We'll use a free weather API that doesn't require authentication

url = "http://api.weatherapi.com/v1/current.json"
params = {
    'key': 'YOUR_API_KEY',  # We'll need to get a free API key
    'q': 'Sydney'
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
except Exception as e:
    print(f"Error: {e}")
    print("Trying alternative method...")
    
    # Let's check if we can access a simple weather service without auth
    try:
        alt_url = "https://wttr.in/Sydney?format=j1"
        alt_response = requests.get(alt_url)
        alt_data = alt_response.json()
        print(alt_data)
    except Exception as alt_e:
        print(f"Alternative method failed: {alt_e}")