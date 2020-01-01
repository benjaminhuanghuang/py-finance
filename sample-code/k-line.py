
# -*- coding: utf-8 -*-
'''
    open, low, high, close
    red, green
'''
import datetime as dt
from matplotlib import style
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
import matplotlib.dates

style.use('ggplot')
start  = dt.datetime(2010,2,1)
# end  = dt.datetime.now()
end  = dt.datetime(2010,5,1)

# read a stack data into dataframe
df = web.DataReader('INTC', 'google', start, end)
# print (df.head())
# conver dataframe to record array
quotes = df.to_records()
# quotes = quotes_historical_yahoo_ohlc('INTC', (2010,2,1), (2010,5,1))

volumns = np.array([])
dates = np.array([])

for row in quotes:
    row[0] = matplotlib.dates.date2num(row[0])
    dates = np.append(dates, row[0])
    volumns = np.append(volumns, row[5])
    
left, width = 0.1, 0.8
# rect for volumn plot
rect_vol = [ left, 0.1, width, 0.26]   # left, bottom, width, height
# rect for k line plot
rect_k = [ left, 0.4, width, 0.5 ]

fig = plt.figure()
ax_vol = fig.add_axes(rect_vol)
ax_vol.fill_between(dates, volumns, color='y')
ax_vol.xaxis_date()  # change x axis to date
plt.setp(ax_vol.get_xticklabels(), rotation=30, horizontalalignment='right' )

ax_k = fig.add_axes(rect_k)

candlestick_ohlc(ax_k, quotes.tolist(),  width=0.6, colorup='r', colordown='g')
ax_k.axes.get_xaxis().set_visible(False)
plt.show()