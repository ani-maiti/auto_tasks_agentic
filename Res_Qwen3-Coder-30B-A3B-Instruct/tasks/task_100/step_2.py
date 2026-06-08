from datetime import datetime

# Parse the expiration date from the openssl output
expiration_date_str = "Jul  6 20:52:29 2026 GMT"
expiration_date = datetime.strptime(expiration_date_str, "%b %d %H:%M:%S %Y %Z")

print(f"SSL certificate for wikipedia.org expires on: {expiration_date.strftime('%Y-%m-%d')}")