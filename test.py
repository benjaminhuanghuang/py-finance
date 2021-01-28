import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime
import time
import yfinance as yf


tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']
data = yf.download(tickers_list,'2015-1-1')['Open']

print(data.head())