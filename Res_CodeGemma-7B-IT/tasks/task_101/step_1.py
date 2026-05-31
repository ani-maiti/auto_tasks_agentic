import ssl

try:
    with ssl.create_default_context().wrap_socket(ssl.socket(ssl.AF_INET, ssl.SOCK_STREAM)) as sock:
        sock.connect(('openai.com', 443))
        cert = sock.getpeercert()
        expiration_date = cert['notAfter']
        print(expiration_date)
except Exception as e:
    print(f"Error: {e}")