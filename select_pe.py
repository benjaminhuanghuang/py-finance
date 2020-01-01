'''
市盈率（PE）用来评估股价水平是否合理的指标之一，由股价除以年度每股盈余（EPS）得出.
PE = Price per share / Earnings per Share

PE标示几年回本
投资越快回本越好，那么就应该买PE低的股票呢？长期投资，买便宜（PE低）的股票，但最低的也不一定好，可能太不活跃或太大盘，盈利能力不强

1、同行业PE 排名
2、同支股票的历史PE走势

'''
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

def getPE(symbol):
  url = 'https://finance.yahoo.com/quote/{}/key-statistics?ltr=1&guccounter=1'.format(symbol)
  response = requests.get(url)
  content = response.content

  soup = bs(content,"html.parser")
  '''
  <tr>
    <td><span>Trailing P/E</span></td>
    <td>24.70</td>
  </tr>
  '''
  span = soup.find('span', text='Trailing P/E')
  td = span.parent
  price = td.find_next_sibling().text
  #print(price)
  return price



if __name__ == '__main__':
  df_sp500 = pd.read_csv('data/sp500.csv', header=None)
  #print(df_sp500.shape)

  symbols= df_sp500[0][0:40].values
  #print(tickers.size)

  for symbol in symbols:
    PE = getPE(symbol)
    print("{} : {}".format(symbol, PE))  



