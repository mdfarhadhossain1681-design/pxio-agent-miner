"""$PXIO price watch (read-only).

Fetches the current $PXIO price from the Dexscreener API (PancakeSwap V3
pair) and reports whether any alert level has been crossed.
Alert-only: this script never trades.
"""
import json
import urllib.request

TOKEN = "0x870aD5f304871eC0c63BE1e976406e0b095A32CD"
ALERT_LEVELS = [0.001, 0.80, 1.00]


def main():
    req = urllib.request.Request(
        f"https://api.dexscreener.com/latest/dex/tokens/{TOKEN}",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.load(r)
    pairs = data.get("pairs") or []
    if not pairs:
        print("No pair data")
        return
    price = float(pairs[0]["priceUsd"])
    print(f"$PXIO price: ${price}")
    for level in ALERT_LEVELS:
        if price >= level:
            print(f"ALERT: price crossed ${level}!")


if __name__ == "__main__":
    main()
