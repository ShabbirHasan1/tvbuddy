import requests

from internal.aggregator import Aggregator


class KucoinAggregator(Aggregator):
    def get_markets_raw(self):
        response = requests.get(
            "https://www.kucoin.com/_api/trade-front/market/getSymbol/USDS")
        response = response.json()

        if not response["success"]:
            raise RuntimeError(
                "Invalid response from 'https://www.kucoin.com/_api/trade-front/market/getSymbol/USDS'!")

        return response["data"]

    def normalize(self, markets):
        normalized_markets = []

        for market in markets:
            normalized_markets.append({
                "name": market["symbol"],
                "price": float(market["buy"]),
                "quote_volume": float(market["vol"])
            })

        return normalized_markets

    def get_tv_prefix(self):
        return "KUCOIN"
