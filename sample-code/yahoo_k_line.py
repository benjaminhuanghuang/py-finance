
# -*- coding: utf-8 -*-
'''
    open, low, high, close
    red, green
'''
import datetime as dt
from matplotlib import style
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from mpl_finance import candlestick_ohlc


date1 = (2017,1,1)
date2 = (2017,12,31)

# open ,high, low, close
quotes = candlestick_ohlc('APPL', date1, date2)