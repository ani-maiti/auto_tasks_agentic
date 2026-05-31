print("HTTP headers retrieved successfully:")
for header, value in response.headers.items():
    print(f"{header}: {value}")