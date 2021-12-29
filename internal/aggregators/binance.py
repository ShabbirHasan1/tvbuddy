import requests

from internal.aggregator import Aggregator


class BinanceAggregator(Aggregator):
    def get_markets_raw(self):
        response = requests.get("https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list")
        response = response.json()

        if not response["code"] or response["code"] != "000000":
            raise RuntimeError(
                "Invalid response from 'https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list'!")

        return response["data"]

    def normalize(self, markets):
        normalized_markets = []

        for market in markets:
            if market["price"] is None:
                market["price"] = 0
            if market["volume"] is None:
                market["volume"] = 0

            normalized_markets.append({
                "name": market["symbol"],
                "price": market["price"],
                "quote_volume": market["volume"] * market["price"]
            })

        return normalized_markets

    def get_tv_prefix(self):
        return "BINANCE"
