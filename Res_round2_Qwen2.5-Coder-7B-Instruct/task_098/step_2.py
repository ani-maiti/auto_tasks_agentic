import datetime

expiration_date_str = "Aug  2 23:59:59 2026 GMT"
expiration_date = datetime.datetime.strptime(expiration_date_str, "%b %d %H:%M:%S %Y %Z")
print("SSL Certificate Expiration Date:", expiration_date)