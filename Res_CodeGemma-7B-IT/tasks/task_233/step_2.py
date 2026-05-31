# Check if rates key exists in the response
if 'rates' not in rates:
  print("Error: Unable to retrieve currency rates.")
  exit(1)

# Continue with the original code
for currency, rate in rates['rates'].items():
  currency_strengths.append((currency, rate))