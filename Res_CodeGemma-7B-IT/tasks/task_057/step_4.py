if response.status_code == 200:
    data = response.json()
    print(data["alt"])
else:
    print("Failed to fetch xkcd comic")