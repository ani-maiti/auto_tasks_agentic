import socket

host = 'api.unixtimestamp.com'
port = 443

try:
    ip_address = socket.gethostbyname(host)
    print(f"IP address of {host} is {ip_address}")
except socket.gaierror as e:
    print(f"Failed to resolve host: {e}")