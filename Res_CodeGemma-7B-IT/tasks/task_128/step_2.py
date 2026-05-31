import requests

url = "https://dog-api.herokuapp.com/api/facts"
response = requests.get(url)

if response.status_code == 200:
    dog_fact = response.json()['fact']
    print(dog_fact)
else:
    print("Error retrieving dog fact.")
```
execution trace:
stdout:
Error retrieving dog fact.


stderr:


return code: 0