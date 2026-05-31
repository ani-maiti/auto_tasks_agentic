import ssl

try:
    with ssl.create_default_context().wrap_socket(ssl.socket(), server_hostname="github.com") as s:
        cert = s.getpeercert()
        print(cert.get('notAfter'))
except Exception as e:
    print(f"Error: {e}")