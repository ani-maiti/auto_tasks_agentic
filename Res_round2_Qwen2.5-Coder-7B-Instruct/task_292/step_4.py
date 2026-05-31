import pandas as pd

# Step 4: Load the exchange rates from the CSV file
df = pd.read_csv('exchange_rates.csv')

# Compute pairwise relationships
pairwise_relationships = df.set_index('Currency').T.dot(df.set_index('Currency'))

# Identify the strongest and weakest currencies
strongest_currency = pairwise_relationships.idxmax().values[0]
weakest_currency = pairwise_relationships.idxmin().values[0]

# Sort the currencies by their strength
sorted_currencies = pairwise_relationships.sort_values(by=strongest_currency, ascending=False)

# Print the top ten currencies by strength
top_ten_currencies = sorted_currencies.head(10)
print(top_ten_currencies)