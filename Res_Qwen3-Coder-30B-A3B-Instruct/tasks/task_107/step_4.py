import socket
try:
    result = socket.gethostbyname_ex('wikipedia.org')
    print("A records for wikipedia.org:")
    for ip in result[2]:
        print(ip)
except Exception as e:
    print(f"Error: {e}")