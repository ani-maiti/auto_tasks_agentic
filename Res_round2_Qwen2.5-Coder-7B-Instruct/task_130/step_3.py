import requests

response = requests.get('https://api.adviceslip.com/advice')
data = response.json()
print(data['slip']['advice'])