import ssl

try:
    with ssl.create_default_context().wrap_socket(
        ssl.socket(ssl.AF_INET, ssl.SOCK_STREAM),
        server_hostname='wikipedia.org',
    ) as sock:
        certificate = sock.getpeercert()
        print(certificate.get('notAfter'))
except Exception as e:
    print(f"Error retrieving certificate: {e}")