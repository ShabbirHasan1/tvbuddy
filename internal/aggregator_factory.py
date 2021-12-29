from enum import Enum

from internal.aggregators.ftx import FtxAggregator
from internal.aggregators.binance import BinanceAggregator


class Aggregators(Enum):
    ftx = "FTX"
    binance = "Binance"

    def __str__(self):
        return self.value


class AggregatorFactory:
    def create(aggregator):
        if aggregator == str(Aggregators.ftx):
            return FtxAggregator()
        elif aggregator == str(Aggregators.binance):
            return BinanceAggregator()

        raise RuntimeError(f"Invalid aggregator '{aggregator}'")
