import socket

def get_nameservers(domain):
    try:
        answers = socket.gethostbyname_ex(domain)
        return answers[2]
    except socket.gaierror as e:
        print(f"Error: {e}")
        return None

nameservers = get_nameservers("python.org")
print(nameservers)