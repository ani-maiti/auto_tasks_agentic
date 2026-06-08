import ssl
import socket
from datetime import datetime

def get_ssl_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = cert['notAfter']
            return expiry_date

try:
    expiry = get_ssl_expiry_date('python.org')
    # Convert to datetime object for better formatting
    expiry_dt = datetime.strptime(expiry, "%b %d %H:%M:%S %Y %Z")
    print(f"SSL certificate for python.org expires on: {expiry_dt.strftime('%Y-%m-%d')}")
except Exception as e:
    print(f"Error retrieving SSL certificate: {e}")