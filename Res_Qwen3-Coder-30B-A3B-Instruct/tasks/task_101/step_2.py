from datetime import datetime

# Parse the expiration date from the openssl output
expiration_date_str = "Aug 26 19:33:25 2026 GMT"
expiration_date = datetime.strptime(expiration_date_str, "%b %d %H:%M:%S %Y %Z")

print(f"SSL certificate for openai.com expires on: {expiration_date.strftime('%Y-%m-%d')}")