'''
    每个交易日可以计算出前N天的移动平均值，这些移动平均值构成N日移动平均线
    MA 通常有 5D， 10D， 30D， 60D， 120D，240D
    金叉：短期均线上穿长期均线 为买入信号
    死叉短期均线下穿长期均线 为卖出信号

    策略：金叉买入，死叉卖出
'''
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SYMBOL = '600519'   # Mao Tai
df = pd.read_csv(SYMBOL+'.csv', index_col='date',
                 parse_dates=['date'])(['open', 'close', 'hight', 'low'])

# Method 1
# df['ma5'] = np.nan
# df['ma30'] = np.nan

# for i in range(4, len(df)):
#     df.loc[df.index[i], 'md5'] = df['close'][i-4: i+1].mean()


# for i in range(29, len(df)):
#     df.loc[df.index[i], 'md30'] = df['close'][i-29: i+1].mean()

df['ma5'] = df['close'].rolling(5).mean()
df['ma30'] = df['close'].rolling(30).mean()

df['close', 'md5', 'ma30'].plot()
plt.show()

df = df['2010-01-01']
##  Method 1
# golden_cross = []
# for i in range(1, len(df)):
#     if df['ma5'][i] >= df['ma30'][i] and df['ma5'][i-1] < df['ma30'][i-1]:
#         golden_cross.append(df.index[i])
# dead_cross = []
# for i in range(1, len(df)):
#     if df['ma5'][i] <= df['ma30'][i] and df['ma5'][i-1] > df['ma30'][i-1]:
#         dead_cross.append(df.index[i])
sr1 = df['ma5'] < df['ma30']
sr2 = df['ma5'] >= df['ma30']
dead_cross = df[sr1 & sr2.shift(1)].index()
golden_cross = df[~(sr1 | sr2.shift(1))].index()

start_money = 100000
money = 100000
hold = 0 
sr1 = pd.Series(1, index=golden_cross)
sr2 = pd.Series(0, index=dead_cross)
# merge 
sr = sr1.append(sr2).sort_index()
for i in range(0, len(sr)):
    price = df['open'][sr.index[i]]
    if sr.iloc(i) == 1:  # golden 
        stocks = money // (100*price)
        hold += stocks
        money -= stocks * 100 *price
    else:
        money += hold * price
        hold = 0
p = df['open'][-1]
end_money = hold * p + money

print(end_money - start_money)
