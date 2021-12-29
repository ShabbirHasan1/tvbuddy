from enum import Enum

from internal.aggregators.ftx import FtxAggregator
from internal.aggregators.binance import BinanceAggregator
from internal.aggregators.kucoin import KucoinAggregator
from internal.aggregators.bitfinex import BitfinexAggregator


class Aggregators(Enum):
    ftx = "FTX"
    binance = "Binance"
    kucoin = "Kucoin"
    bitfinex = "Bitfinex"

    def __str__(self):
        return self.value


class AggregatorFactory:
    def create(aggregator):
        if aggregator == str(Aggregators.ftx):
            return FtxAggregator()
        elif aggregator == str(Aggregators.binance):
            return BinanceAggregator()
        elif aggregator == str(Aggregators.kucoin):
            return KucoinAggregator()
        elif aggregator == str(Aggregators.bitfinex):
            return BitfinexAggregator()

        raise RuntimeError(f"Invalid aggregator '{aggregator}'")
