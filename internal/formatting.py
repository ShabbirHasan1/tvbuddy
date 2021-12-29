def format_markets(markets, tv_prefix):
    formatted_markets = []

    for market in markets:
        market = market["name"]
        market = "".join(char for char in market if char.isalnum())

        formatted_markets.append(f"{tv_prefix}:{market}")

    return ",".join(formatted_markets)
