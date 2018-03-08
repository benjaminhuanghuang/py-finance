import ffn
from datetime import datetime
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import quandl

entry = datetime(2018,1,1)
exit = datetime(2018,3,8)

df = quandl.get("WIKI/TSLA")
dailyRet = df['Close'][entry:exit].pct_change()

# suppose 无风险利率为 4%, 每年 252个交易日
excessRet = dailyRet - 0.04/252
# 超额报酬 = (投资报酬 - 比较基准报酬) 
# sharpeRatio = 超额报酬平均值 ／ 超额保持标准差
sharpeRatio = np.sqrt(252.0)* np.mean(excessRet)/np.std(excessRet)
print (sharpeRatio)