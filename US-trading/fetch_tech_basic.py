
'''
Get sp500 from wiki S&P 500 Component Stocks

The S&P 500 is a stock market index that measures the stock performance of 500 large companies

'''
import pandas as pd
from datetime import date
import pandas_datareader.data as web
from datetime import datetime, timedelta

HEADERS = ['Symbol', 'Open', 'High', 'Low', 'Close', 'Volume']
TECH_SYMBOLS = [
    'AAPL',
    'GOOGL',
    'GOOG',
    'TSLA'
]


def fetchTodayStockInfo(symbol, headers):
  start = datetime.now() - timedelta(days=1)
  df = web.get_data_yahoo(symbol, start=start)
  result = df[headers]
  result.insert(loc=0, column="Symbol", value=[symbol])
  return result


if __name__ == '__main__':
  df_stocks = pd.DataFrame(columns=HEADERS)
  for symbol in TECH_SYMBOLS:
    stock_info = fetchTodayStockInfo(symbol, HEADERS[1:])
    df_stocks = df_stocks.append(stock_info, sort=False)

  #
  filePath = 'data/tech_{}.csv'.format(date.today().strftime("%Y-%m-%d"))
  df_stocks.to_csv(excel_writer=filePath, index=False)
