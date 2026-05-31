import requests

url = "https://www.python.org/sitemap.xml"
response = requests.get(url)

if response.status_code == 200:
    print("Download successful")
else:
    print(f"Failed to download, status code: {response.status_code}")
```

This code attempts to download the `sitemap.xml` file from `python.org`. If the download is successful, it prints "Download successful". If there's an error, it prints the status code.