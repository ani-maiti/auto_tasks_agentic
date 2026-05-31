import requests

url = "https://openai.com"
response = requests.get(url, allow_redirects=True)

redirect_chain = response.history
final_url = response.url

print("Redirect Chain:")
for url in redirect_chain:
    print(url)

print("\nFinal URL:", final_url)