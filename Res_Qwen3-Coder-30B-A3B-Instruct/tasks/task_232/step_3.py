# Print final top 10 coins as requested
df = pd.read_csv('crypto_prices.csv')
print("Top 10 Cryptocurrencies by Market Cap:")
top_10 = df.head(10)
for index, row in top_10.iterrows():
    print(f"{row['market_cap_rank']}. {row['name']} ({row['symbol'].upper()}) - ${row['current_price']:,.2f}")