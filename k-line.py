import numpy as np
import matplotlib.pyplot as plt
from mpl_finance  import quotes_historical_yahoo_ohlc

date1 = (2010,2,1)
data2= (2010,5,1)

quotes = quotes_historical_yahoo_ohlc('INTC', date1, data2)
left = 0.1
width = 0.8
rect_vol = [left, 0.1, width, 0.3]
rect_main = [left, 0.4, width, 0.5]