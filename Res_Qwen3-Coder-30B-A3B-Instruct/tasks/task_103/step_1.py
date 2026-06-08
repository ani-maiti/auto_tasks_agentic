import ssl
import socket

def get_ssl_certificate_issuer(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            return cert['issuer']

try:
    issuer = get_ssl_certificate_issuer('python.org')
    print(issuer)
except Exception as e:
    print(f"Error: {e}")