import socket

try:
    answers = socket.gethostbyname_ex('python.org')
    print(answers)
except Exception as e:
    print(str(e))