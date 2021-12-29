# tvbuddy

Aggregate real-time market data from cryptocurrency exchanges, filter, sort and finally format into TradingView's watchlist syntax!

Developed and tested on Python 3.10.

## Usage
Install the required Python dependencies

`pip install -r requirements.txt`

run the [Streamlit](https://github.com/streamlit/streamlit) frontend server

`python -m streamlit run ui.py`

and lastly navigate to [localhost:8501](http://localhost:8501) and have a look!

## Roadmap

As of writing this the code is, well.. Pretty terrible. There's lots of things 

- [x] It works! Basic proof of concept
- [ ] Implement other aggregators
- [ ] Refactor code.. A ton of refactoring
- [ ] Abstractions, abstractions, abstractions. Rewriting code is tedious. 
- [ ] Improve sorting and filtering.