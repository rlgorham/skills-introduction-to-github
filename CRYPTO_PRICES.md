# Crypto Price Retrieval

This repository includes a simple Python script (`crypto_prices.py`) that demonstrates how cryptocurrency prices are retrieved.

## How It Works

Crypto prices are fetched from the [CoinGecko](https://www.coingecko.com/) public API — no API key required.

The script sends an HTTP GET request to:

```
https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd
```

The API returns a JSON object with the current USD price for each requested coin, for example:

```json
{
  "bitcoin": { "usd": 65000.00 },
  "ethereum": { "usd": 3200.00 },
  "litecoin": { "usd": 85.00 }
}
```

## Usage

```bash
python crypto_prices.py
```

Sample output:

```
bitcoin: $65,000.00
ethereum: $3,200.00
litecoin: $85.00
```

You can also import the function in your own code:

```python
from crypto_prices import get_crypto_prices

prices = get_crypto_prices(["bitcoin", "dogecoin"])
print(prices)  # {'bitcoin': 65000.0, 'dogecoin': 0.12}
```
