from enum import Enum

import requests
from requests.exceptions import HTTPError

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


class FtxAggregator(Aggregator):
    def get_markets_raw(self):
        response = requests.get("https://ftx.com/api/markets")
        response = response.json()

        if not response["success"]:
            raise RuntimeError("Invalid response from 'https://ftx.com/api/markets'!")

        return response["result"]

    def normalize(self, markets):
        normalized_markets = []

        for market in markets:
            normalized_markets.append({
                "name": market["name"],
                "price": market["price"],
                "usd_volume": market["volumeUsd24h"]
            })

        return normalized_markets

    def get_tv_prefix(self):
        return "FTX"


class Aggregators(Enum):
    ftx = "FTX"

    def __str__(self):
        return self.value


class AggregatorFactory:
    def create(aggregator):
        if aggregator == str(Aggregators.ftx):
            return FtxAggregator()

        raise RuntimeError(f"Invalid aggregator '{aggregator}'")
