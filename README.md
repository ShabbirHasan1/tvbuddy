# tvbuddy
Aggregate real-time market data from cryptocurrency exchanges, filter, sort and format as TradingView watchlists.

Developed and tested on Python 3.10.

## Public instances
* [tvbuddy.disguised.host](https://tvbuddy.disguised.host/)
  Hosted by me, updated atleast once per day.

If you're hosting a public tvbuddy instance feel free to make a pull request adding it to the list!

## Setup
Install the required Python dependencies

`pip install -r requirements.txt`

and run the [Streamlit](https://github.com/streamlit/streamlit) server

`python -m streamlit run ui.py`

### Development
Navigate to [localhost:8501](http://localhost:8501) and have a look!

### Live
How you want to deploy tvbuddy in a live environment is completely up to you,
personally I use [Caddy](https://caddyserver.com/) as a reverse proxy.

## Roadmap

As of writing this the code is, well.. Pretty terrible. There's lots of things that
should be done before a first release.

- [x] It works! Basic proof of concept
- [ ] Implement other aggregators, in no particular order
  - [x] Binance
  - [x] Kucoin
  - [ ] Bybit
  - [x] Bitfinex
  - [ ] Huobi
  - [ ] Coinbase
  - [ ] Kraken
- [ ] Refactor code.. A ton of refactoring
- [ ] Abstractions, abstractions, abstractions. Rewriting code is tedious
- [ ] Improve sorting and filtering.
