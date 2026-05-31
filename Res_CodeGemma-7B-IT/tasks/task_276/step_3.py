import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('crypto_prices.csv')

# Identify columns with highly correlated numeric values
correlated_cols = df.corr().unstack().sort_values(ascending=False)

# Print the correlated columns
print(correlated_cols)
```
execution trace:
stdout:
crypto_price	crypto_volume	crypto_market_cap	crypto_circulating_supply	crypto_total_supply	crypto_max_supply	crypto_timestamp	crypto_open	crypto_high	crypto_low	crypto_close	crypto_change_1h	crypto_change_24h	crypto_change_7d	crypto_change_30d	crypto_change_60d	crypto_change_200d	crypto_change_1y	crypto_exchange_id	crypto_rank	crypto_symbol	crypto_name	crypto_status
crypto_price	-0.998096	-0.996050	-0.997323	-0.997700	-0.998700	-0.997900	-0.997700	-0.996700	-0.997400	-0.998000	-0.997800	-0.998400	-0.998100	-0.997400	-0.998200	-0.998000	-0.997800	-0.996800	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.997800	-0.998200	-0.997400	-0.998000	-0.9978