from internal.aggregator_factory import AggregatorFactory

from internal.filtering import filter_custom, filter_perpetuals, filter_price, filter_volume
from internal.formatting import format_markets
from internal.sorting import sort_markets


def get_tv_formatted_markets(aggregators, valid_volume, valid_price, only_perpetuals, custom_filter_expression, sort_by):
    tv_formatted_markets = []

    for aggregator in aggregators:
        aggregator_instance = AggregatorFactory.create(aggregator)
        markets = aggregator_instance.get_markets()

        if valid_volume:
            markets = filter_volume(markets)

        if valid_price:
            markets = filter_price(markets)

        if aggregator == "FTX" and only_perpetuals:
            markets = filter_perpetuals(markets)

        if custom_filter_expression:
            markets = filter_custom(markets, custom_filter_expression)

        if sort_by:
            markets = sort_markets(markets, sort_by)

        markets = format_markets(markets, aggregator_instance.get_tv_prefix())

        tv_formatted_markets.append(str(markets))

    return ",".join(tv_formatted_markets)
