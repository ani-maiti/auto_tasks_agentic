import socket

host = "api.coindesk.com"
port = 443

try:
    socket.gethostbyname(host)
    print(f"{host} resolves to an IP address.")
except socket.gaierror:
    print(f"{host} could not be resolved. Check your network connection or DNS settings.")