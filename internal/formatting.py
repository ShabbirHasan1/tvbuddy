def format_markets(markets, tv_prefix):
    formatted = ""

    for market in markets:
        market = market["name"]
        market = "".join(char for char in market if char.isalnum())

        if formatted != "":
            formatted = f"{formatted}, {tv_prefix}:{market}"
        else:
            formatted = f"{tv_prefix}:{market}"

    return formatted
