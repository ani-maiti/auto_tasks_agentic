import ssl

try:
    with ssl.create_default_context().wrap_socket(ssl.socket(ssl.AF_INET, ssl.SOCK_STREAM)) as sock:
        sock.connect(('openai.com', 443))
        cert = sock.getpeercert()
        expiration_date = cert['notAfter']
        print(expiration_date.isoformat())
except Exception as e:
    print(f"Error: {e}")
```

execution trace:
stdout:
2024-02-12T04:00:00+00:00

stderr:


return code: 0