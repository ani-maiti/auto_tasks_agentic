import socket

url = "www.wikipedia.org"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect((url, port))
    request = f"GET /robots.txt HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n"
    sock.sendall(request.encode('utf-8'))

    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data

    print(response.decode('utf-8'))
finally:
    sock.close()