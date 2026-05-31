# Fix the API key
response = requests.get('https://openexchangerates.org/api/latest?app_id=YOUR_API_KEY&symbols=USD,EUR,JPY,GBP,AUD,CAD,CHF,CNY,DKK,EUR,HKD,ISK,INR,ILS,KRW,MXN,MYR,NOK,NZD,PHP,PLN,RUB,SAR,SEK,SGD,THB,TRY,USD,ZAR')

# Check for errors
if response.status_code != 200:
    print('Error retrieving exchange rates.')
    exit()

# Parse the response
rates = response.json()['rates']

# Create a list of currency pairs
pairs = []
for base in rates:
    for currency in rates:
        if base != currency:
            pairs.append((base, currency))

# Compute pairwise relationships
pair_values = []
for pair in pairs:
    base_rate = rates[pair[0]]
    currency_rate = rates[pair[1]]
    pair_values.append((pair, base_rate / currency_rate))

# Identify the strongest and weakest currencies
pair_values.sort(key=lambda x: x[1], reverse=True)
strongest_currencies = [pair[0] for pair in pair_values[:10]]
weakest_currencies = [pair[0] for pair in pair_values[-10:]]

# Save the data to CSV
with open('exchange_rates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Currency Pair', 'Strength'])
    for pair, value in pair_values:
        writer.writerow([pair, value])

# Generate a report
print('Top 10 Strongest Currencies:')
for currency in strongest_currencies:
    print(currency)

print('\nTop 10 Weakest Currencies:')
for currency in weakest_currencies:
    print(currency)