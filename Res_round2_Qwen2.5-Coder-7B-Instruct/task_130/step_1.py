import requests

response = requests.get('https://api.adviceslip.com/advice')
print(response.text)