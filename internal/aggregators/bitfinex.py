import requests

from internal.aggregator import Aggregator


class BitfinexAggregator(Aggregator):
    def get_markets_raw(self):
        response = requests.get(
            "https://api-pub.bitfinex.com/v2/tickers?symbols=ALL")
        response = response.json()

        return response

    def normalize(self, markets):
        normalized_markets = []

        for market in markets:
            # Bitfinex' api is very odd.. :(
            market_name = market[0]
            if market_name[0] == "t" or market_name[0] == "f":
                market_name = market_name[1:]

            normalized_markets.append({
                "name": market_name,
                "price": market[1],
                "quote_volume": market[8] * market[1]
            })

        return normalized_markets

    def get_tv_prefix(self):
        return "BITFINEX"
