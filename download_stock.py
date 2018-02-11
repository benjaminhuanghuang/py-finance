import pandas as pd
import pandas.io.data as web
import datetime as dt

start = dt.datetime(2017, 1, 1)
end = dt.date.today()

apple_stock = web.DataReader('AAPL', 'yahoo', start, end)


# Download sp500 stock
ticker = []
data = pd.read_cvs('SP500.csv', header=None)

for item in data[0]:   # column 0 of data
    ticker.append(item)
    
for name in ticker:
    vars()[name] = web.DataReader(name, 'yahoo' , start, end)

