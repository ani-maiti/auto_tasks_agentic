# Step 2: Load the exchange rates from the CSV file
import pandas as pd

df = pd.read_csv('exchange_rates.csv')

# Compute pairwise relationships
pairwise_relationships = df.set_index('Currency').T.corr()

# Identify the strongest and weakest currencies
strongest_currency = pairwise_relationships.idxmax().idxmax()
weakest_currency = pairwise_relationships.idxmin().idxmin()

print(f"Strongest currency: {strongest_currency}")
print(f"Weakest currency: {weakest_currency}")