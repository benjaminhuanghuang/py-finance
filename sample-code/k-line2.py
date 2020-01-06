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
import matplotlib
matplotlib.use('TkAgg')

'''
Fetch stock data
'''
STOCK_SAMBOL = 'AAPL'
start = dt.datetime(2019, 11, 1)
#end  = dt.datetime.now()
df = web.get_data_yahoo(STOCK_SAMBOL, start=start)

# Create subplots
# 整张图 6rows, 1 col, K线图占5rows, 交易量占1row
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex = ax1)

#
# Set ticks
mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12


# ax1.xaxis.set_major_locator(mondays)
# ax1.xaxis.set_minor_locator(alldays)
# ax1.xaxis.set_major_formatter(weekFormatter)
# ax1.xaxis.set_minor_formatter(dayFormatter)

# plot_day_summary(ax, quotes, ticksize=3)

'''
Draw k-line using candlestick_ohlc
    ax为坐标轴，
    quotes 是包含time，open，high，low，close的序列，candlestick_ohlc方法只会读取序列的前5个，因此可以传入任意长度的序列。
           time必须是浮点类型，一般需要用matplotliab中的date2num方法进行格式转换。
    width为bar的宽度，
'''
quotes = zip(mdates.date2num(df.index.to_pydatetime()),
             df['Open'], df['High'],
             df['Low'], df['Close'])
print(quotes)

candlestick_ohlc(ax1, quotes, colorup='r', colordown='g', width=0.6, alpha=0.3)

'''
计算均线
'''
# ax1.xaxis_date()
# ax1.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

'''
交易量
'''
ax2.bar(df.index, df['Volume'])

plt.show()
