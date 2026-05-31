import requests

response = requests.get('https://blog.docker.com/')
title = response.text.split('<title>')[1].split('</title>')[0]
print(title)