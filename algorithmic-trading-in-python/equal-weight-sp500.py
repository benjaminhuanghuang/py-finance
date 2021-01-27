import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secrets import IEX_CLOUD_API_TOKEN

symbol = 'AAPL'
api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}"
print(api_url)
data = requests.get(api_url).json()

# Adding stocks data to pd dataframe
my_columns = ['Ticker', 'Price',
              'Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns=my_columns)
final_dataframe

final_dataframe = final_dataframe.append(
    pd.Series(['AAPL',
               data['latestPrice'],
               data['marketCap'],
               'N/A'],
              index=my_columns),
    ignore_index=True)

print(data)
# 505 stocks
stocks = pd.read_csv('sp_500_stocks.csv')
#
pd.DataFrame()
