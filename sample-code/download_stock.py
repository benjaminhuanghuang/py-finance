'''
    download stock data by using pandas
    save to csv
'''
import datetime as dt
from matplotlib import style
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
start  = dt.datetime(2017,1,1)
end  = dt.datetime.now()

# read a stack data into dataframe
df = web.DataReader('TSLA', 'google', start, end)
print(df['Open', 'High'].head(10))  # default first 5

df.to_csv('data/tsla.csv')