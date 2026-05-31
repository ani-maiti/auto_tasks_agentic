import ssl
import socket

host = "github.com"
port = 443

with socket.create_connection((host, port)) as sock:
    with ssl.wrap_socket(sock) as ssl_sock:
        cert = ssl_sock.getpeercert()

issuer = cert.get('issuer')

print(issuer)