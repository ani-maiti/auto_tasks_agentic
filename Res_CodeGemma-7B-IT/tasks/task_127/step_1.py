import requests

response = requests.get("https://catfact.ninja/fact")

if response.status_code == 200:
    fact = response.json()["fact"]
    print(fact)
else:
    print("Failed to retrieve cat fact.")