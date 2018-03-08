from datetime import datetime
import pandas as pd

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

import quandl

# 波动性
def volatility(symbol):
    df = quandl.get("WIKI/"+symbol)
    dailyChange = df['Close'].pct_change()
    std = dailyChange.std()
    return std


companies = ['MSFT', 'TSLA', 'GOOG', 'AAPL']
result = []
for symbol in companies:
    v = volatility(symbol)
    result.append((v , symbol))

df_result = pd.DataFrame(result, columns=['volatility', 'symbol'])
print(df_result)




