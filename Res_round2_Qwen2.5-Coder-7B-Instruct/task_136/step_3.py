import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

url = "https://www.wikipedia.org/sitemap.xml"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open("sitemap.xml", "wb") as file:
        file.write(response.content)
    print("Downloaded sitemap.xml successfully.")
else:
    print(f"Failed to download sitemap.xml. Status code: {response.status_code}")