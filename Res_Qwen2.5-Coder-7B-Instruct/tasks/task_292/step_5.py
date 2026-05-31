# Step 4: Load the exchange rates from the CSV file
import pandas as pd

df = pd.read_csv('exchange_rates.csv')

# Check if the DataFrame is empty
if df.empty:
    print("No exchange rates available.")
else:
    # Compute pairwise relationships
    pairwise_relationships = df.set_index('Currency').T.corr()

    # Identify the strongest and weakest currencies
    strongest_currency = pairwise_relationships.idxmax().idxmax()
    weakest_currency = pairwise_relationships.idxmin().idxmin()

    if pd.isna(strongest_currency) or pd.isna(weakest_currency):
        print("Unable to determine strongest and weakest currencies due to missing data.")
    else:
        print(f"Strongest currency: {strongest_currency} with correlation: {pairwise_relationships.loc[strongest_currency, weakest_currency]}")
        print(f"Weakest currency: {weakest_currency} with correlation: {pairwise_relationships.loc[weakest_currency, strongest_currency]}")

# Step 5: Save the pairwise relationships to a CSV file
pairwise_relationships.to_csv('pairwise_relationships.csv')

print("Pairwise relationships saved to pairwise_relationships.csv")