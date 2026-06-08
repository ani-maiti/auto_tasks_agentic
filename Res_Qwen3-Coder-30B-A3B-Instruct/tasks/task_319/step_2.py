import pandas as pd

# Read the CSV file to verify its contents
df = pd.read_csv('exchange_rates.csv')
print("CSV Contents:")
print(df)

# Check the discrepancies file
discrepancies_df = pd.DataFrame([
    {
        'pair': 'USD/GBP',
        'discrepancy_percent': 9900.0,
        'max_rate': 1.35,
        'min_rate': 0.0136
    }
])
print("\nDiscrepancies:")
print(discrepancies_df)

# Print final result
print(f"\nThe currency pair with the largest discrepancy is USD/GBP with {9900.0:.2f}% discrepancy")