import yfinance as yf

data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

msft = yf.Ticker("MSFT")

# get stock info
msft.info