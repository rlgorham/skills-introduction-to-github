import json
import urllib.error
import urllib.request


def get_crypto_prices(coins=None):
    """
    Retrieve current cryptocurrency prices using the CoinGecko public API.

    Args:
        coins: list of coin IDs (default: ['bitcoin', 'ethereum', 'litecoin'])

    Returns:
        dict mapping coin ID to its current USD price

    Raises:
        RuntimeError: if the API request fails or returns an unexpected response
    """
    if coins is None:
        coins = ["bitcoin", "ethereum", "litecoin"]

    ids = "%2C".join(coins)
    url = (
        f"https://api.coingecko.com/api/v3/simple/price"
        f"?ids={ids}&vs_currencies=usd"
    )

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"API request failed with HTTP {e.code}: {e.reason}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Failed to reach the API: {e.reason}") from e

    return {
        coin: data[coin]["usd"]
        for coin in coins
        if isinstance(data.get(coin), dict) and "usd" in data[coin]
    }


if __name__ == "__main__":
    prices = get_crypto_prices()
    for coin, price in prices.items():
        print(f"{coin}: ${price:,.2f}")
