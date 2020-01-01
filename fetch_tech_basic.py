
'''
Get sp500 from wiki S&P 500 Component Stocks

The S&P 500 is a stock market index that measures the stock performance of 500 large companies

'''
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date

SYMBOLS = [
    'APPL',
    'GOOGL',
    'GOOG',
]


HEADERS = [
    'Symbol',
    'Company Name',
    'Open',
    'Close',
    'PE'
]


def fetchStockInfo(symbol):
  mock_info = [symbol, symbol, '10.0', '12.0', '15']

  return mock_info


if __name__ == '__main__':
  stocks = []
  for symbol in SYMBOLS:
    stock_info = fetchStockInfo(symbol)
    stocks.append(stock_info)

  #
  df = pd.DataFrame(data=stocks, columns=HEADERS)

  filePath = 'data/tech_{}.xlsx'.format(date.today().strftime("%Y-%m-%d"))
  df.to_excel(excel_writer=filePath, index=False)
