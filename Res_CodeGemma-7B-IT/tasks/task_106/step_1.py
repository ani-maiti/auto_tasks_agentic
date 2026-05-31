import socket

hostname = "github.com"

try:
    ip_addresses = socket.gethostbyname_ex(hostname)[2]
    for ip in ip_addresses:
        print(ip)
except Exception as e:
    print(f"Error retrieving IP address: {e}")