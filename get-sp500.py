
'''
Get sp500 from wiki S&P 500 Component Stocks

The S&P 500 is a stock market index that measures the stock performance of 500 large companies

'''
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url)
content = response.content

soup = bs(content,"html.parser")

table = soup.find('table', id='constituents')

SD = dict()
for row in table.tbody.findAll('tr'):
    tds = row.findAll('td')
    if len(tds) > 0:
        stock_code = str(tds[0].text.strip())
        GICS_sector = str(tds[3].text.strip()).lower()
        SD[stock_code] = GICS_sector

#print(len(SD))
stocks = pd.Series(SD).to_frame()

#print(stocks.shape)
#TODO: group by GICS_sector

stocks.to_csv('data/sp500.csv', header=False)