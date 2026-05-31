# The API requires a list of cryptocurrencies and a currency to convert to.
# Let's try retrieving prices for the top 50 cryptocurrencies in USD
curl "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin,dogecoin,solana,tether,cardano,polkadot,chainlink,uniswap&vs_currencies=usd"