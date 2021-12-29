from enum import Enum

import requests
from requests.exceptions import HTTPError


class Aggregator:
    def get_markets(self):
        pass

    def normalize(self, markets):
        pass

    def get_tv_prefix(self):
        pass


class FtxAggregator(Aggregator):
    def get_markets(self):
        response = requests.get("https://ftx.com/api/markets")
        response = response.json()

        if not response["success"]:
            raise HTTPError(
                "Aggregator 'FTX' endpoint '/api/markets' did not have a valid response.")

        return response["result"]

    def normalize(self, markets):
        normalized_markets = []
        for market in markets:
            if not market["price"]:
                market["price"] = 0

            if not market["volumeUsd24h"]:
                market["volumeUsd24h"] = 0

            normalized_market = {
                "name": market["name"],
                "price": market["price"],
                "usd_volume": market["volumeUsd24h"]
            }

            normalized_markets.append(normalized_market)

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
