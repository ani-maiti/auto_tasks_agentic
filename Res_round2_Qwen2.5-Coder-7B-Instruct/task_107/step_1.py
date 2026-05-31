import socket

hostname = 'wikipedia.org'
try:
    ip_address = socket.gethostbyname(hostname)
    print(f"The IP address for {hostname} is {ip_address}")
except socket.gaierror as e:
    print(f"Error retrieving IP address for {hostname}: {e}")