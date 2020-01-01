
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta
import api_keys


DATA_SROUCE = 'av-daily-adjusted'


def fetchTodayStockInfo(symbol, headers):
  end = datetime.now()
  start = datetime.now() - timedelta(days=1)
  df = web.DataReader(symbol, DATA_SROUCE, start, end,  api_key=api_keys.Alpha_Vantage_API)
  result = df[headers]
  result.insert(loc=0, column="symbol", value=[symbol])
  # print(result)
  return result

if __name__ == '__main__':
  fetchTodayStockInfo('AAPL', ['open', 'high', 'low','close','volume'])
