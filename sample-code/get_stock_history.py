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
'''
You have exceeded the API speed limit of 20 calls per 10 minutes. 
'''
df = quandl.get("WIKI/TSLA")
print(df.tail())
df[['Close','Volume']].plot(subplots = True, figsize = (10, 8))
plt.legend(loc='best')

plt.show()