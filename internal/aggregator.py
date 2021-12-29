MARKET_CHILDREN_SCHEMA = [
    {
        "name": "price",
        "default": 0
    },
    {
        "name": "usd_volume",
        "default": 0
    }
]


def verify_markets(markets):
    verified_markets = []

    for market in markets:
        for schema_child in MARKET_CHILDREN_SCHEMA:
            if not market[schema_child["name"]]:
                market[schema_child["name"]] = schema_child["default"]

        verified_markets.append(market)

    return verified_markets


class Aggregator:
    def get_markets_raw(self):
        pass

    def normalize(self, markets):
        pass

    def get_markets(self):
        markets = self.get_markets_raw()
        normalized_markets = self.normalize(markets)
        verified_markets = verify_markets(normalized_markets)

        return verified_markets

    def get_tv_prefix(self):
        pass
