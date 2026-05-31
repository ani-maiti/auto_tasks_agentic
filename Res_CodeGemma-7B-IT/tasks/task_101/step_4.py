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


stderr:
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_101/step_4.py", line 15
    print(expiration_date.isoformat())
         ^
AttributeError: 'datetime.datetime' object has no attribute 'isoformat'


return code: 1