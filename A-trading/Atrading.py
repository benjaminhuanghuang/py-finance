import requests
from time import sleep
from datetime import datetime, time, timedelta
from dateutil import parser

SYMBOL = 'https://hq.sinajs.cn/?format=text&list=sh600519'

# current price
def getTick():
  page = requests.get(SYMBOL)
  stock_info = page.text
  values = stock_info.split(',')

  last = float(values[1])
  trade_datetime = values[30]+' '+values[31]

  return (last, trade_datetime)
 
# trade_time = time(9,30)

# 
def getHistoryData():

  return dt, open, high, low, close, volume


#  buy or sell
def strategy(tick, Dt, Open, High, Low, Close):
  ma20 = Close[:19].sum() / 20
  
  pass

dt, open, high, low, close, volumn = getHistoryData()

while time(9) < < time(15, 1):
  tick = getTick()
  dt = parser.parse(tick[1]).time
  print(tick)
  sleep(3)

