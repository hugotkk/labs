import requests

# Define the API URLs for getting the ETH/USD
eth_usd_url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

# Get the eth/USD price
response = requests.get(eth_usd_url)
eth_usd_price = float(response.json()["price"])

# Print the prices
print("ETH/USD Price:", eth_usd_price)
