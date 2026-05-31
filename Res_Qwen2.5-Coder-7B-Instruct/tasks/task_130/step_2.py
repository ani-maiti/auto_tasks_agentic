import requests

response = requests.get('https://api.adviceslip.com/advice')
if response.status_code == 200:
    advice = response.json()
    print(advice['slip']['advice'])
else:
    print(f"Failed to fetch advice: {response.status_code}")