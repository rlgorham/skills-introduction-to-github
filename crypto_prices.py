"""
Retrieve current cryptocurrency prices using the CoinGecko public API.

CoinGecko API docs: https://docs.coingecko.com/reference/introduction
No API key is required for the free tier.
"""

import json
import urllib.error
import urllib.parse
import urllib.request


COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_crypto_prices(coin_ids: list[str], vs_currencies: list[str] = None) -> dict:
    """
    Fetch current prices for the given cryptocurrencies.

    Args:
        coin_ids: List of CoinGecko coin IDs (e.g. ["bitcoin", "ethereum"]).
        vs_currencies: List of target currency codes (default: ["usd"]).

    Returns:
        A dict mapping each coin ID to its prices, e.g.:
        {"bitcoin": {"usd": 60000.0}, "ethereum": {"usd": 3000.0}}

    Raises:
        ValueError: If coin_ids is empty.
        urllib.error.URLError: If the request to the API fails.
    """
    if not coin_ids:
        raise ValueError("coin_ids must not be empty")

    if vs_currencies is None:
        vs_currencies = ["usd"]

    params = urllib.parse.urlencode({
        "ids": ",".join(coin_ids),
        "vs_currencies": ",".join(vs_currencies),
    })
    url = f"{COINGECKO_API_URL}?{params}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        raise urllib.error.URLError(
            f"CoinGecko API returned HTTP {exc.code}: {exc.reason}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Unexpected response from CoinGecko API: {exc}") from exc

    return data


def main():
    coins = ["bitcoin", "ethereum", "litecoin"]
    currencies = ["usd", "eur"]

    print("Fetching crypto prices from CoinGecko...\n")
    prices = get_crypto_prices(coins, currencies)

    for coin, price_data in prices.items():
        price_str = ", ".join(
            f"{currency.upper()}: {price:,.2f}"
            for currency, price in price_data.items()
        )
        print(f"{coin.capitalize()}: {price_str}")


if __name__ == "__main__":
    main()
