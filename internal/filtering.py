import numexpr


def filter_markets(markets, predicate):
    filtered_markets = []

    for market in markets:
        if predicate(market):
            filtered_markets.append(market)

    return filtered_markets


def filter_custom(markets, expression):
    return filter_markets(markets, lambda market: numexpr.evaluate(expression, market))


def filter_volume(markets):
    return filter_markets(markets, lambda market: market["usd_volume"] > 0)


def filter_price(markets):
    return filter_markets(markets, lambda market: market["price"] > 0)


def filter_perpetuals(markets):
    return filter_markets(markets, lambda market: market["name"].endswith("PERP"))
