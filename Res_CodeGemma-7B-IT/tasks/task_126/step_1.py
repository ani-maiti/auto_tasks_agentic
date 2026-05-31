import requests

response = requests.get("https://www.boredapi.com/api/activity")

if response.status_code == 200:
    activity_data = response.json()
    print(f"Random activity: {activity_data['activity']}")
else:
    print("Error fetching activity suggestion.")