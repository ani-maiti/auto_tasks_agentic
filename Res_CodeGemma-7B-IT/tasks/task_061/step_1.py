import urllib.request

# Get the latest Debian stable release URL
url = "https://deb.debian.org/debian/dists/stable/Release.gz"

# Download the release file
response = urllib.request.urlopen(url)

# Get the release version from the file
version = response.read().decode("utf-8").splitlines()[1].split(":")[1].strip()

# Print the version
print(version)