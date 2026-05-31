import socket

# Check if DNS resolution works
host = 'www.boredapi.com'
try:
    ip_address = socket.gethostbyname(host)
    print(f"DNS resolved successfully: {ip_address}")
except socket.gaierror as e:
    print(f"Failed to resolve DNS: {e}")