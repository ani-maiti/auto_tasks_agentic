import json
response = '{"status":"success","country":"United States","countryCode":"US","region":"WV","regionName":"West Virginia","city":"Institute","zip":"25112","lat":38.3889,"lon":-81.7614,"timezone":"America/New_York","isp":"West Virginia State University","org":"West Virginia State University","as":"AS63274 West Virginia State University","query":"192.73.23.2"}'
data = json.loads(response)
print(f"Country: {data['country']}")
print(f"Region: {data['regionName']}")
print(f"City: {data['city']}")
print(f"Latitude: {data['lat']}")
print(f"Longitude: {data['lon']}")
print(f"Timezone: {data['timezone']}")