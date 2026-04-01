# Crypto Price Retrieval

This document explains how cryptocurrency prices are retrieved in this project.

## API: CoinGecko

Crypto prices are fetched from the **[CoinGecko](https://www.coingecko.com/) public REST API**.

- **Base URL:** `https://api.coingecko.com/api/v3`
- **Authentication:** None required for the free tier
- **Rate limit:** ~30 requests/minute on the free tier

### Endpoint used

```
GET /simple/price
```

**Query parameters:**

| Parameter       | Description                                              | Example                    |
|-----------------|----------------------------------------------------------|----------------------------|
| `ids`           | Comma-separated list of CoinGecko coin IDs               | `bitcoin,ethereum`         |
| `vs_currencies` | Comma-separated list of target fiat/crypto currencies    | `usd,eur`                  |

**Example request:**

```
GET https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,eur
```

**Example response:**

```json
{
  "bitcoin": { "usd": 60000.00, "eur": 55000.00 },
  "ethereum": { "usd": 3000.00, "eur": 2750.00 }
}
```

## Usage

Run the script directly with Python (no extra dependencies needed):

```bash
python crypto_prices.py
```

The script will print the latest prices for Bitcoin, Ethereum, and Litecoin in USD and EUR.

## References

- [CoinGecko API Documentation](https://docs.coingecko.com/reference/introduction)
- [CoinGecko `/simple/price` endpoint](https://docs.coingecko.com/reference/simple-price)
