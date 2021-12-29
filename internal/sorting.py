from enum import Enum


class SortingMethods(Enum):
    nothing = "Nothing"
    price = "Price"
    quote_volume = "Volume (24h)"

    def __str__(self):
        return self.value


def by_price(markets):
    return sorted(markets, key=lambda market: market["price"], reverse=True)


def by_volume(markets):
    return sorted(markets, key=lambda market: market["quote_volume"], reverse=True)


def sort_markets(markets, method):
    if method == str(SortingMethods.nothing):
        return markets
    elif method == str(SortingMethods.price):
        return by_price(markets)
    elif method == str(SortingMethods.quote_volume):
        return by_volume(markets)

    raise RuntimeError(f"Invalid sorting method '{method}'!")
