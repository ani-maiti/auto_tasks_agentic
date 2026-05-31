if response.status_code == 200:
    title = response.json()["title"]
    print(title)
else:
    print("Error retrieving data")