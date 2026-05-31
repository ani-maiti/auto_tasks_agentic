import requests

# Get the latest Python release page
response = requests.get("https://www.python.org/downloads/")

# Find the link to the latest release
latest_release_link = response.text.split("Latest Python 3 Release")[1].split("href=")[2].split('"')[1]

# Extract the release version from the link
latest_release_version = latest_release_link.split("/")[-1]

# Print the latest release version
print(latest_release_version)