import socket

# Set a timeout for the socket connection
timeout_duration = 5

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('worldtimeapi.org', 443)
sock.settimeout(timeout_duration)
try:
    sock.connect(server_address)
except socket.timeout:
    print("Connection timed out")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    sock.close()