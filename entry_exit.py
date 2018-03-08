import ffn

import pandas_datareader.data as web
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

# 讀取從指定日期之後的股價資訊
df = web.DataReader("TSLA", 'google', datetime(2016,8,1))

# 計算均線
df['20d'] = pd.Series.rolling(df['Close'], window=20).mean()
df['60d'] = pd.Series.rolling(df['Close'], window=60).mean()
df[['Close','20d','60d']].plot(grid=True, figsize=(10,8))
# Donchian Channel
df['20d_high'] = pd.Series.rolling(df['Close'], window=20).max()
df['10d_low'] = pd.Series.rolling(df['Close'], window=10).min()
df[['Close','20d_high','10d_low']].plot(grid=True, figsize=(10,8))


'''
https://www.quantstart.com/articles/Backtesting-a-Moving-Average-Crossover-in-Python-with-pandas
'''
def strategy1(df):
    # 計算均線
    df['20d'] = pd.Series.rolling(df['Close'], window=20).mean()
    df['60d'] = pd.Series.rolling(df['Close'], window=60).mean()
    
    df['positions'] = np.where(df['20d']-df['60d'] > 0, 1.0, 0.0)
    df['signals'] = df['positions'].diff()
    df[['signals', 'positions']].plot(subplots = True, ylim=(-1.1, 1.1), figsize = (10, 8))

