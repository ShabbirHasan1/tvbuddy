def by_price(markets):
    return sorted(markets, key=lambda market: market["price"], reverse=True)


def by_volume(markets):
    return sorted(markets, key=lambda market: market["quote_volume"], reverse=True)


def sort_markets(markets, algorithm):
    if algorithm == "Nothing":
        return markets
    elif algorithm == "Price":
        return by_price(markets)
    elif algorithm == "Volume (24h)":
        return by_volume(markets)

    raise RuntimeError(f"Invalid sorting algorithm '{algorithm}'")
