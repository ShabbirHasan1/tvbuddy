from enum import Enum

from internal.aggregators.ftx import FtxAggregator
from internal.aggregators.binance import BinanceAggregator
from internal.aggregators.kucoin import KucoinAggregator


class Aggregators(Enum):
    ftx = "FTX"
    binance = "Binance"
    kucoin = "Kucoin"

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

        raise RuntimeError(f"Invalid aggregator '{aggregator}'")
