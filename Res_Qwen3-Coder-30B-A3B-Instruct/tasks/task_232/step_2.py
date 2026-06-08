# Let's verify the CSV file was created correctly
import pandas as pd

df = pd.read_csv('crypto_prices.csv')
print("CSV file contents:")
print(df.head(10))
print(f"\nTotal rows: {len(df)}")
print(f"Columns: {list(df.columns)}")

# Check if we have the expected data structure
expected_columns = ['id', 'name', 'symbol', 'current_price', 'market_cap', 'market_cap_rank', 'total_volume']
for col in expected_columns:
    if col not in df.columns:
        print(f"Missing column: {col}")