import socket

# Define the URL of the documentation website
url = "https://docs.example.com"

# Set a timeout for the DNS lookup
timeout = 5

# Try to resolve the domain name
try:
    socket.setdefaulttimeout(timeout)
    ip_address = socket.gethostbyname(url.replace("https://", "").replace("http://", ""))
    print(f"Resolved IP address: {ip_address}")
except socket.gaierror as e:
    print(f"Failed to resolve the domain name. Error: {e}")