
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta

TECH_SYMBOLS = [
    'AAPL',
    'GOOGL',
    'GOOG',
    'TSLA'
]

HEADERS = ['Symbol', 'Open', 'High', 'Low', 'Close', 'Volume']


def fetchTodayStockInfo(symbol, headers):
  start = datetime.now() - timedelta(days=1)
  df = web.get_data_yahoo(symbol, start=start)
  result = df[headers]
  result.insert(loc=0, column="Symbol", value=[symbol])
  return result


def isGoodStock(symbol):
  start = datetime.now() - timedelta(days=10)
  try:
    df_stock = web.get_data_yahoo(symbol, start=start)

    # price
    prices = df_stock['Adj Close']
    if not (prices[-1] > prices[-2] and prices[-2] > prices[-3]):
      return False

    # 交易量
    volumns = df_stock['Volume']
    if not (volumns[-1] > volumns[-2] and volumns[-2] > volumns[-3]):
      return False

    # 涨幅
    diff = (prices[-1] - prices[-3]) / prices[-3]
    if diff < 0 or diff > 0.1:
      return False

    return True
  except Exception as e:
    print(e)
    return False


def isRaisingN(symbol, n):
  if n > 5:
    raise Exception("n should < 5")

  start = datetime.now() - timedelta(days=10)
  try:
    df_stock = web.get_data_yahoo(symbol, start=start)
    #print(df_stock)

    # price
    prices = df_stock['Adj Close']

    for i in range(n):
      if(prices[-1 - i] < prices[-1 - i-1]):
        return False
    # 涨幅
    diff = (prices[-1] - prices[-1 - n]) / prices[-1 - n]
    if diff < 0 or diff > 0.1:
      return False
    return True
  except Exception as e:
    print('Error for {} :{}'.format(symbol, e.args))
    return False


def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    import sys
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' %
                     (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


if __name__ == '__main__':
  # fetchTodayStockInfo('AAPL', ['Open', 'High', 'Low','Close','Volume'])
  # print(isGoodStock('AAPL'))
  print(isRaisingN('AAPL', 2))
