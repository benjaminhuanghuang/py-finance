
'''
Get sp500 from wiki S&P 500 Component Stocks
'''
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd

site = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
page = urllib.request.urlopen(site)
soup = bs(page.read(),"html.parser")

table = soup.find('table', {'class': 'wikitable'})

SD = dict()
for row in table.findAll('tr'):
    col = row.findAll('td')
    if len(col) > 0:
        stock_code = str(col[0].string.strip())
        sector = str(col[3].string.strip()).lower()
        SD[stock_code] = sector

stocks = pd.Series(SD)
stocks.to_csv('data/sp500.csv')