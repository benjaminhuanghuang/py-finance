import pandas as pd
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, as_completed
import utils


if __name__ == '__main__':
  good_stocks = []
  # Load stock symbols from csv file
  df = pd.read_csv('data/sp500.csv', header=None)
  symbols = df[0].values
  count = 1
  num_cpu = mp.cpu_count()
  print('CPU: {}'.format(num_cpu))
  with ThreadPoolExecutor(max_workers=num_cpu) as executor:
    # Start the task and mark each future with its parameter
    futures = {executor.submit(utils.isRaisingN, symbol, 3):symbol for symbol in symbols}
    for f in as_completed(futures):
      symbol = futures[f]
      #print('result: {}, {}'.format(symbol, f.result()))
      count += 1
      utils.printProgress(count, 505, prefix='Progress:', decimals=0)
      if f.result():
        good_stocks.append(symbol)
  df = pd.DataFrame(data = good_stocks)
  df.to_csv('data/good_stocks.csv', header=False)
