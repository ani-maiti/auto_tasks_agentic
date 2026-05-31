import datetime

expiration_date_str = "Aug 26 19:33:25 2026 GMT"
expiration_date = datetime.datetime.strptime(expiration_date_str, "%b %d %H:%M:%S %Y %Z")
print("SSL Certificate Expiration Date:", expiration_date)