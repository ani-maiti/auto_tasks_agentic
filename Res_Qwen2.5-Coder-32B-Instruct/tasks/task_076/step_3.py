import json

data = json.loads('''{
  "ip": "192.73.23.2",
  "hostname": "firewall.wvstateu.edu",
  "city": "Nitro",
  "region": "West Virginia",
  "country": "US",
  "loc": "38.4148,-81.8440",
  "org": "AS63274 West Virginia State University",
  "postal": "25143",
  "timezone": "America/New_York",
  "readme": "https://ipinfo.io/missingauth"
}''')

print(f"IP Address: {data['ip']}")
print(f"Hostname: {data['hostname']}")
print(f"City: {data['city']}")
print(f"Region: {data['region']}")
print(f"Country: {data['country']}")
print(f"Location: {data['loc']}")
print(f"Organization: {data['org']}")
print(f"Postal Code: {data['postal']}")
print(f"Timezone: {data['timezone']}")