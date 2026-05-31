import socket

nameservers = [
    "dns1.p08.nsone.net",
    "dns2.p08.nsone.net",
    "dns3.p08.nsone.net",
    "dns4.p08.nsone.net",
    "ns-421.awsdns-52.com",
    "ns-520.awsdns-01.net",
    "ns-1283.awsdns-32.org",
    "ns-1707.awsdns-21.co.uk"
]

for ns in nameservers:
    try:
        ip_address = socket.gethostbyname(ns)
        print(f"{ns} resolves to {ip_address}")
    except socket.gaierror:
        print(f"Failed to resolve {ns}")