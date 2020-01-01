
'''
Get sp500 from wiki S&P 500 Component Stocks

The S&P 500 is a stock market index that measures the stock performance of 500 large companies

'''
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date

import utils


SYMBOLS = [
    'AAPL',
    'GOOGL',
    'GOOG',
    'TSLA'
]


HEADERS = [
    'symbol',
    'open',
    'high',
    'low',
    'close',
    'volume'
]


if __name__ == '__main__':
  df_stocks = pd.DataFrame(columns=HEADERS)
  for symbol in SYMBOLS:
    stock_info = utils.fetchTodayStockInfo(symbol, HEADERS[1:])
    df_stocks = df_stocks.append(stock_info, sort=False)

  #
  filePath = 'data/tech_{}.xlsx'.format(date.today().strftime("%Y-%m-%d"))
  df_stocks.to_excel(excel_writer=filePath, index=False)
