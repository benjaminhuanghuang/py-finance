import datetime as dt
from matplotlib import style
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import pandas as pd
import pandas_datareader.data as web
from urllib import request
from bs4 import BeautifulSoup as bs

def getStockPE(stock_name):
    site = "https://finance.yahoo.com/quote/"+stock_name+"/key-statistics?p="+stock_name
    page = request.urlopen(site)
    soup = bs(page.read(),"html.parser")
    table = soup.find('table', {'class': 'table-qsp-stats Mt(10px)'})
    row  = table.find('tr', {'data-reactid': '27'})
    td = row.find('td', {'data-reactid': '33'})
    pe = td.string.strip()   # Price-Earnings Ratio (P/E Ratio)
    if pe == 'N/A':
        return 0
    pe = float(pe)
    return pe
    
df = pd.read_csv('data/sp500.csv', header=None)
ticker =[]
for item in df[0]:
    ticker.append(item)

shortTicker = ticker[0:39]

site = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"
page = request.urlopen(site)
soup = bs(page.read(),"html.parser")
table = soup.find('table', {'class': 'table-qsp-stats Mt(10px)'})
row  = table.find('tr', {'data-reactid': '27'})
td = row.find('td', {'data-reactid': '33'})
pe = td.string.strip()   # Price-Earnings Ratio (P/E Ratio)


for stock_name in shortTicker:
    try:
        pe = getStockPE(stock_name)
        if pe> 10 and pe<30:
            print(stock_name, pe)
    except Exception as exp:
        print ('failed', exp.args) 


