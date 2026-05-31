from datetime import datetime

expiration_date_str = "Jul  6 20:52:29 2026 GMT"
expiration_date = datetime.strptime(expiration_date_str, "%b %d %H:%M:%S %Y %Z")
print(f"SSL Certificate Expiration Date: {expiration_date}")