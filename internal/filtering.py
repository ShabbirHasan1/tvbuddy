def filter_custom(markets, expression):
    filtered_markets = []

    for market in markets:
        passes_filter = eval(expression, {"market": market})
        if passes_filter:
            filtered_markets.append(market)

    return filtered_markets


def filter_volume(markets):
    return filter_custom(markets, "market['usd_volume']>0")


def filter_price(markets):
    return filter_custom(markets, "market['price']>0")


def filter_perpetuals(markets):
    return filter_custom(markets, "market['name'].endswith('PERP')")
