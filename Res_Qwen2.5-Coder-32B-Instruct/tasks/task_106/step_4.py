import socket

print("Attempting to resolve all A records for github.com using socket.getaddrinfo")
try:
    addresses = socket.getaddrinfo('github.com', None, socket.AF_INET, socket.SOCK_STREAM)
    for addr in addresses:
        print(f"A record for github.com: {addr[4][0]}")
except socket.gaierror as e:
    print(f"Error resolving github.com: {e}")