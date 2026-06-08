import requests

try:
    response = requests.get('https://api.ipify.org', timeout=5)
    print(response.text)
except Exception as e:
    print(f"Error: {e}")