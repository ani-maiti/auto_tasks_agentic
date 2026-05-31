import socket

host = "wikipedia.org"
response = socket.gethostbyname_ex(host)

for a_record in response[2]:
    print(a_record)