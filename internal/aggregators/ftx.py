import requests

from internal.aggregator import Aggregator


class FtxAggregator(Aggregator):
    def get_markets_raw(self):
        response = requests.get("https://ftx.com/api/markets")
        response = response.json()

        if not response["success"]:
            raise RuntimeError(
                "Invalid response from 'https://ftx.com/api/markets'!")

        return response["result"]

    def normalize(self, markets):
        normalized_markets = []

        for market in markets:
            normalized_markets.append({
                "name": market["name"],
                "price": market["price"],
                "quote_volume": market["quoteVolume24h"]
            })

        return normalized_markets

    def get_tv_prefix(self):
        return "FTX"
