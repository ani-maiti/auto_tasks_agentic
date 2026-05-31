import ssl
import datetime

# Get the SSL certificate for python.org
ssl_context = ssl.create_default_context()
with ssl_context.wrap_socket(socket.create_connection(('python.org', 443))) as sock:
    certificate = sock.getpeercert()

# Extract the certificate expiration date
expiration_date = certificate['notAfter']

# Convert the expiration date to a human-readable format
expiration_date_str = datetime.datetime.strptime(expiration_date.decode(), '%b %d %H:%M:%S %Y %Z').strftime('%Y-%m-%d')

# Print the expiration date
print(expiration_date_str)