import socket

print("Using socket to gethostbyname for github.com")
try:
    ip_address = socket.gethostbyname('github.com')
    print(f"A record for github.com: {ip_address}")
except socket.gaierror as e:
    print(f"Error resolving github.com: {e}")