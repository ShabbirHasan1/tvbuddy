import streamlit as st

from internal.aggregator_wrapper import get_tv_formatted_markets

st.set_page_config(
    page_title="tvbuddy",
    page_icon=":chart_with_upwards_trend:",
    layout="centered"
)

name = st.text_input("Name", placeholder="...")
name_with_extension = name if name.endswith(".txt") else name + ".txt"

if not name:
    st.warning("Please enter a name.")
    st.stop()

aggregators = st.multiselect("Aggregators", options=(
    "FTX", "Binance", "Kucoin", "Bitfinex"))
if not aggregators:
    st.warning("Please select atleast one aggregator.")
    st.stop()

sort_by = st.radio("Sort by", options=("Nothing", "Price", "Volume (24h)"))
if not sort_by:
    st.warning("Please select a sorting method.")
    st.stop()

filtering = st.checkbox("Filters")

valid_volume = None
valid_price = None
only_perpetuals = None
custom_filter_expression = None

if filtering:
    valid_volume = st.checkbox("Valid volume")
    valid_price = st.checkbox("Valid price")

    if "FTX" in aggregators:
        only_perpetuals = st.checkbox("Only perpetuals (only supports FTX)")

    custom_filter_expression = st.text_input(
        "Custom expression", placeholder="...")


@st.cache()
def get_data(aggregators, valid_volume, valid_price, only_perpetuals, custom_filter_expression, sort_by):
    return get_tv_formatted_markets(
        aggregators, valid_volume, valid_price, only_perpetuals, custom_filter_expression, sort_by)


data = get_data(aggregators, valid_volume, valid_price,
                only_perpetuals, custom_filter_expression, sort_by)
if data.count(",") > 1000:
    st.error("Filtered market count exceeds TradingView watchlist limit!")
    st.stop()

st.download_button(
    f"Download '{name_with_extension}'",
    data=data,
    file_name=name_with_extension
)
