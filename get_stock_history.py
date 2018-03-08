from datetime import datetime

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 


import pandas_datareader.data as web
'''
Pandas data-reader does not work after 2017/05 
'''
# df = web.DataReader("TSLA", 'google', datetime(2016,1,1))

import quandl
df = quandl.get("WIKI/TSLA")
df[['Close','Volume']].plot(subplots = True, figsize = (10, 8))
plt.legend(loc='best')

plt.show()