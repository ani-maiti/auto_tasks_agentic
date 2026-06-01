import socket

print("Attempting to retrieve nameservers using socket.gethostbyname_ex...")
try:
    ns = socket.gethostbyname_ex('github.com')
    print(f"Nameservers for github.com: {ns}")
except Exception as e:
    print(f"Error: {e}")