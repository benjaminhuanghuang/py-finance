import pandas as pd
import numpy as np
import quandl
from pathlib import Path
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import math

import private_config

FILE_PATH = 'data/google.csv'
STOCK_SYMBOL = 'WIKI/GOOGL'
start = "2017-01-01"

dataFile = Path(FILE_PATH)
if dataFile.is_file():
    df = pd.read_csv(FILE_PATH)
else:
    quandl.ApiConfig.api_key = private_config.QUANDL_KEY
    df = quandl.get(STOCK_SYMBOL, start_date=start)
    df.to_csv(FILE_PATH)

# print(df.head())
df = df[['Adj. Open', 'Adj. High', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. High']) /df['Adj. Close'] * 100.0
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) /df['Adj. Open'] * 100.0

df=df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

forecast_col = 'Adj. Close'   # the column to be predict
df.fillna(-9999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))  #  how many days we want to predict
df['label'] = df[forecast_col].shift(-forecast_out)
print(df.head())