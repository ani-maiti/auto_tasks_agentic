import requests

url = "https://openai.com"
response = requests.get(url, allow_redirects=True)

redirect_chain = response.history
final_url = response.url

print("Redirect Chain:")
for resp in redirect_chain:
    print(resp.status_code, resp.url)

print("\nFinal URL:", final_url)