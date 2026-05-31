import requests

# Use a custom CA bundle to bypass the certificate error
response = requests.get('https://api.fact.nu/random', verify='/path/to/custom_ca_bundle.crt')
if response.status_code == 200:
    data = response.json()
    if 'text' in data:
        print(data['text'])
else:
    print("Failed to retrieve dog fact")
```

Please replace `/path/to/custom_ca_bundle.crt` with the actual path to a custom CA bundle file that includes the necessary certificates.