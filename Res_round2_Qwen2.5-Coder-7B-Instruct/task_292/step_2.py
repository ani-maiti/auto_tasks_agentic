import pandas as pd

# Step 2: Load the exchange rates from the CSV file
df = pd.read_csv('exchange_rates.csv')

# Compute pairwise relationships
pairwise_relationships = df.set_index('Currency').T.dot(df.set_index('Currency'))

# Identify the strongest and weakest currencies
strongest_currency = pairwise_relationships.idxmax()
weakest_currency = pairwise_relationships.idxmin()

print(f"Strongest Currency: {strongest_currency}")
print(f"Weakest Currency: {weakest_currency}")