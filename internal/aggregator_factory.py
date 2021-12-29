from enum import Enum

from internal.aggregators.ftx import FtxAggregator


class Aggregators(Enum):
    ftx = "FTX"

    def __str__(self):
        return self.value


class AggregatorFactory:
    def create(aggregator):
        if aggregator == str(Aggregators.ftx):
            return FtxAggregator()

        raise RuntimeError(f"Invalid aggregator '{aggregator}'")
