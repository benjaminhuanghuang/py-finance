'''
  策略：每月第一个交易日买入100股，每年最后一个交易日全卖出
'''
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SYMBOL = '600519'   # Mao Tai
# get history data 
df = ts.get_k_data(SYMBOL, start='1980-01-01')
df.to_csv(SYMBOL+'.csv')

df = pd.read_csv(SYMBOL+'.csv', index_col='date', parse_dates=['date'])(['open', 'close', 'hight', 'low'])


# date raise > 3%
df[(df['close']-df[open])/df['open']>=0.03].index


# drop than yesterday > 0.2
df[(df['open']- df['close'].shift(1))/ df['close'].shift(1)<=-0.2]

price_last = df['open'][-1]
# buy 100 stock at first day of every month
df = df['2001-09': '2017-11']
df_montyly = df.resample('MS').first
df_yearly = df.resample('A').last()[:-1]

cost_money = 0
hold = 0
for year in range(2001, 2018):
   cost = df_montyly[str(year)]['open'].sum() * 100
   hold += len(df_montyly[str(year)]['open']) * 100
   if year != 2017:
    cost_money -= df_yearly[str(year)]['open'][0] * hold
    hold = 0

cost_money -= hold * price_last

print(-cost_money)
