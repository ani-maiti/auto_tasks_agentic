# Step 2: Load data into DataFrame
import pandas as pd

df = pd.DataFrame(data)
df['volatility'] = df['price_change_percentage_24h'].abs() / df['current_price']
df['rank'] = range(1, len(df) + 1)

print(df.head())