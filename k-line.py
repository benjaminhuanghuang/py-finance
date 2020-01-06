'''
    https://pythonprogramming.net/candlestick-ohlc-graph-matplotlib-tutorial/
    https://github.com/matplotlib/mpl-finance/blob/master/examples/finance_demo.py
    
    open, low, high, close
    red, green
'''
import matplotlib.pyplot as plt
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import numpy as np
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
from matplotlib import style
from matplotlib import ticker
import matplotlib
matplotlib.use('TkAgg')
import seaborn

# Set style
seaborn.set() 



'''
Fetch stock data
'''
STOCK_SAMBOL = 'AAPL'
start = dt.datetime(2019, 11, 1)
#end  = dt.datetime.now()
df = web.get_data_yahoo(STOCK_SAMBOL, start=start)


##
# Process data
#   convert index "Date" to a column, it is datetime64[ns]
df.reset_index(inplace=True)

# print(df.dtypes)
date_tickers = df['Date'].values
df['Date_Index'] = np.arange(0, len(df))   # make the k line is continuous

def get_date_text(x , pos):
    if x<0 or x>len(date_tickers)-1:
        return ''
    return np.datetime_as_string(date_tickers[int(x)], unit='D')

#   calculate ma
df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()
df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
df['30ma'] = df['Adj Close'].rolling(window=30, min_periods=0).mean()
df['60ma'] = df['Adj Close'].rolling(window=60, min_periods=0).mean()

# print(df)

# Create subplots
# 6rows, 1 col, Kline use rows, Volume use 1row
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
plt.setp(ax1.get_xticklabels(), visible=False)    # hide the x tick
plt.setp(ax2.get_yaxis().get_offset_text(), visible=False) # hide 1e7

##
# Setup ax
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(get_date_text))

##
# Draw K line
candlestick_ohlc(ax1,
                 quotes=df[['Date_Index', 'Open', 'High', 'Low','Adj Close']].values,
                 colorup='r', colordown='g', width=0.6, alpha=0.3)
ax1.set_ylabel('Price')
##
# Draw ma
for ma in ['5ma', '20ma', '30ma', '60ma']:
    ax1.plot(df['Date_Index'], df[ma], label=ma)

ax1.legend()

ax1.set_title('The K line of ' + STOCK_SAMBOL, fontsize=20)

##
# Draw valume
# Add new column determining up or down
df['Up'] = df.apply(
    lambda row: 1 if row['Adj Close'] >= row['Open'] else 0, axis=1)

ax2.bar(df.query('Up == 1')['Date_Index'], df.query('Up == 1')['Volume'], color='r', alpha=0.7)
ax2.bar(df.query('Up == 0')['Date_Index'], df.query('Up == 0')['Volume'], color='g', alpha=0.7)

ax2.set_ylabel('Volume')

plt.show()
