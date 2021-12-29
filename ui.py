import streamlit as st

from internal.aggregator import AggregatorFactory, Aggregators
from internal.filtering import filter_custom, filter_perpetuals, filter_price, filter_volume
from internal.formatting import format_markets
from internal.sorting import sort_markets

st.set_page_config(
    page_title="tvbuddy",
    page_icon=":chart_with_upwards_trend:",
    layout="centered"
)

name = st.text_input("Name", placeholder="...")
name_with_extension = name if name.endswith(".txt") else name + ".txt"

if not name:
    st.error("Please select a name.")
    st.stop()

aggregator = st.radio("Aggregators", options=("FTX",))
if not aggregator:
    st.error("Please select atleast one aggregator.")
    st.stop()

sort_by = st.radio("Sort by", options=("Nothing", "Price", "Volume (24h)"))
if not sort_by:
    st.error("Please select a sorting algorithm.")
    st.stop()

filtering = st.checkbox("Filtering")

valid_volume = None
valid_price = None
only_perpetuals = None
custom_filter_expression = None

if filtering:
    valid_volume = st.checkbox("Valid volume")
    valid_price = st.checkbox("Valid price")

    if aggregator == "FTX":
        only_perpetuals = st.checkbox("Only perpetuals")

    custom_filter_expression = st.text_input(
        "Custom filter expression", placeholder="...")


def export():
    aggregator_instance = AggregatorFactory.create(aggregator)
    markets = aggregator_instance.get_markets()

    if valid_volume:
        markets = filter_volume(markets)

    if valid_price:
        markets = filter_price(markets)

    if only_perpetuals:
        markets = filter_perpetuals(markets)

    if custom_filter_expression:
        markets = filter_custom(markets, custom_filter_expression)

    if sort_by:
        markets = sort_markets(markets, sort_by)

    markets = format_markets(markets, aggregator_instance.get_tv_prefix())

    return str(markets)


st.download_button(
    f"Download '{name_with_extension}'",
    data=export(),
    file_name=name_with_extension
)
