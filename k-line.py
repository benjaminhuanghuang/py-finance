
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


style.use('ggplot')
start  = dt.datetime(2017,1,1)
end  = dt.datetime.now()

# read a stack data into dataframe
df = web.DataReader('TSLA', 'google', start, end)
print (df.head())
left, width = 0.1, 0.8

volumns = np.array([])
dates = np.array([])

# for row in df.as_matrix():
#     print (row)
#     dates = np.append(dates, row[0])
#     volumns = np.append(volumns, row[4])
    
stock_array = np.array(df.reset_index()[['Date','Open','High','Low','Close']])
    

# rect for volumn plot
rect_vol = [ left, 0.1, width, 0.3 ]   # left, bottom, width, height
# rect for k line plot
rect_k = [ left, 0.4, width, 0.5 ]

fig = plt.figure()
ax_vol = fig.add_axes(rect_vol)
ax_vol.fill_between(dates, volumns)
ax_k = fig.add_axes(rect_k)


# plt.show()