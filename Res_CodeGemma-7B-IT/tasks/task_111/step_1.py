import socket

domain = "github.com"

try:
    ns_records = socket.gethostbyname_ex(domain)
    print(ns_records[2])
except Exception as e:
    print(f"Error retrieving name servers for {domain}: {e}")