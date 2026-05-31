# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the currency pairs to retrieve
currency_pairs = ["EURUSD", "GBPUSD", "JPYUSD", "AUDUSD", "NZDUSD", "USDCHF", "USDCAD", "USDSEK", "USDKRW", "USDCNY"]

# Create an empty list to store the data
data = []

# Iterate over the currency pairs
for pair in currency_pairs:
    # Retrieve data from each provider
    for provider in ["oanda", "xe", "wise"]:
        # Construct the API endpoint for each provider
        url = f"https://www.{provider}.com/currency-converter/{pair}"

        # Send a request to the endpoint
        response = requests.get(url)

        # Parse the HTML response
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the exchange rate from the HTML
        rate = soup.find("span", class_="text-success").text.strip()

        # Store the data in the list
        data.append({
            "currency_pair": pair,
            "provider": provider,
            "rate": rate
        })

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate the discrepancies between providers
df["discrepancy"] = (df["rate"].astype(float) - df["rate"].groupby(level="currency_pair").transform("first").astype(float)) / df["rate"].groupby(level="currency_pair").transform("first").astype(float)

# Find the currency pair with the largest discrepancy
largest_discrepancy_pair = df.groupby("currency_pair")["discrepancy"].max().idxmax()

# Print the currency pair with the largest discrepancy
print(f"Currency pair with the largest discrepancy: {largest_discrepancy_pair}")

# Save the dataset to CSV
df.to_csv("currency_rates.csv", index=False)

# Generate a report
# ... (code for generating the report)